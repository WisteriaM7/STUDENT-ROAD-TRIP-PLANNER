import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from langchain.chat_models import ChatOllama
from langchain.memory import ConversationBufferMemory
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate

# ---- Streamlit Setup ---- #
st.set_page_config(layout="wide")
st.title("🚗 Student Road Trip Planner")
st.caption("Plan budget-friendly, fun student trips 💸")

# ---- Memory Management ---- #
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

if "memory" not in st.session_state:
    st.session_state.memory = ConversationBufferMemory(return_messages=True)

MAX_HISTORY = 2  # Keep last 2 interactions

def trim_memory():
    while len(st.session_state.chat_history) > MAX_HISTORY * 2:
        st.session_state.chat_history.pop(0)
        if st.session_state.chat_history:
            st.session_state.chat_history.pop(0)

# ---- LangChain LLM Setup ---- #
llm = ChatOllama(model="mistral", streaming=True)

prompt_template = PromptTemplate(
    input_variables=["history", "human_input"],
    template="""
You are a fun, student-friendly travel planner.
History: {history}
User Trip Input: {human_input}
Provide:
- A detailed day-by-day itinerary
- Budget-friendly tips
- Activities matching the student vibe
- Keep it casual and concise
Assistant:
"""
)

chain = LLMChain(llm=llm, prompt=prompt_template, memory=st.session_state.memory)

# ---- Trip Input Section ---- #
st.header("🧭 Trip Details")

col1, col2 = st.columns(2)
with col1:
    start_city = st.text_input("Starting City", "Delhi")
    num_people = st.slider("Number of Students", 1, 10, 4)
with col2:
    dest_city = st.text_input("Destination City", "Goa")
    days = st.slider("Trip Duration (Days)", 1, 10, 5)

mode = st.radio("🚙 Travel Mode", ["Car", "Bus", "Train"], horizontal=True)
vibe = st.selectbox("🎭 Trip Vibe", ["Adventure 🌄", "Chill 🌴", "Culture 🏛️", "Foodie 🍲", "Nature 🌿"])

# ---- Budget Estimation ---- #
st.header("💰 Quick Budget Estimate")
distance = st.slider("📏 Estimated Distance (km)", 100, 2000, 500)

travel_cost = distance * (10 if mode == "Car" else 5 if mode == "Bus" else 6)
stay_cost = 800 * days * num_people
food_cost = 300 * days * num_people
misc_cost = 500 * num_people
total_cost = travel_cost + stay_cost + food_cost + misc_cost
per_person = total_cost / num_people

budget_data = {
    "Category": ["Travel", "Stay", "Food", "Misc"],
    "Cost (INR)": [travel_cost, stay_cost, food_cost, misc_cost],
}
df_budget = pd.DataFrame(budget_data)

col_table, col_chart = st.columns(2, gap="medium")
with col_table:
    st.subheader("🧾 Budget Breakdown")
    st.table(df_budget)
    st.metric("💸 Total Cost", f"₹{total_cost:,.0f}")
    st.metric("🧍 Per Person", f"₹{per_person:,.0f}")

with col_chart:
    st.subheader("📊 Cost Distribution")
    fig, ax = plt.subplots()
    ax.pie(df_budget["Cost (INR)"], labels=df_budget["Category"], autopct="%1.1f%%", startangle=90)
    ax.axis("equal")
    st.pyplot(fig)

st.divider()

# ---- Display Chat History ---- #
for msg in st.session_state.chat_history:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# ---- Handle Trip Plan Generation ---- #
trip_prompt = f"""
Plan a {days}-day student road trip for {num_people} students from {start_city} to {dest_city} by {mode}.
Budget: ₹{total_cost:,.0f} (~₹{per_person:,.0f} per person)
Trip vibe: {vibe}
Include a daily itinerary, budget tips, and fun student activities.
Keep it concise and casual.
"""

if st.button("✨ Generate Trip Plan"):
    # Add user message
    st.session_state.chat_history.append({"role": "user", "content": trip_prompt})
    trim_memory()

    # Stream assistant response
    with st.chat_message("assistant"):
        response_container = st.empty()
        full_response = ""

        for chunk in chain.stream({"human_input": trip_prompt}):
            if isinstance(chunk, dict) and "text" in chunk:
                full_response += chunk["text"]
                response_container.markdown(full_response)

    st.session_state.chat_history.append({"role": "assistant", "content": full_response})
    trim_memory()

st.divider()