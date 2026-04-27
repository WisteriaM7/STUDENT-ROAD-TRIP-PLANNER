import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from openai import OpenAI

# -------------------------
# CONFIG
# -------------------------
st.set_page_config(page_title="Student Road Trip Planner", layout="wide")

st.title("🚗 Student Road Trip Planner")
st.caption("Plan affordable, fun, and memorable student getaways 💸")

# -------------------------
# TRIP INPUTS
# -------------------------
st.header("🧭 Trip Details")

col1, col2 = st.columns(2)
with col1:
    start_city = st.text_input("Starting City", placeholder="e.g., Delhi")
    num_people = st.slider("Number of Friends", 1, 50, 4)
with col2:
    dest_city = st.text_input("Destination City", placeholder="e.g., Goa")
    days = st.slider("Trip Duration (Days)", 1, 25, 5)

mode = st.radio("🚙 Travel Mode", ["Car", "Bus", "Train"], horizontal=True)

vibe = st.selectbox(
    "🎭 Trip Vibe",
    ["Adventure 🌄", "Chill 🌴", "Culture 🏛️", "Foodie 🍲", "Nature 🌿"],
)

st.divider()

# -------------------------
# BUDGET ESTIMATION
# -------------------------
st.header("💰 Quick Budget Estimate")

distance = st.slider("📏 Estimated Distance (km)", 100, 2000, 500)

if mode == "Car":
    travel_cost = distance * 10
elif mode == "Bus":
    travel_cost = distance * 5
else:
    travel_cost = distance * 6

stay_cost = 800 * days * num_people
food_cost = 300 * days * num_people
misc_cost = 500 * num_people

total_cost = travel_cost + stay_cost + food_cost + misc_cost
per_person = total_cost / num_people

data = {
    "Category": ["Travel", "Accommodation", "Food", "Misc"],
    "Cost (INR)": [travel_cost, stay_cost, food_cost, misc_cost],
}
df = pd.DataFrame(data)

# -------------------------
# SIDE-BY-SIDE
# -------------------------
col_table, col_chart = st.columns(2, gap="medium")

with col_table:
    st.subheader("🧾 Budget Breakdown")
    st.table(df)
    st.metric("💸 Total Trip Cost", f"₹{total_cost:,.0f}")
    st.metric("🧍 Per Person", f"₹{per_person:,.0f}")

with col_chart:
    st.subheader("📊 Cost Distribution")
    fig, ax = plt.subplots()
    ax.pie(df["Cost (INR)"], labels=df["Category"], autopct="%1.1f%%", startangle=90)
    ax.axis("equal")
    st.pyplot(fig)

st.divider()

# -------------------------
# AI TRIP PLANNER
# -------------------------
st.header("🧠 AI Trip Plan")

# Hardcoded OpenRouter API key (replace this with your own key)
if st.button("✨ Generate My Trip Plan"):
    with st.spinner("Planning your road trip..."):
        try:
            client = OpenAI(
                base_url="https://openrouter.ai/api/v1",
                api_key=st.secrets.OPENROUTER_API_KEY,
            )

            prompt = f"""
            You are an expert student travel planner.
            Plan a {days}-day road trip for {num_people} students
            from {start_city} to {dest_city} by {mode}.
            The total budget is ₹{total_cost:,.0f} (about ₹{per_person:,.0f} per person).
            Trip vibe: {vibe}.
            Include:
            - A short route summary
            - A day-by-day itinerary (in a student tone)
            - Budget tips and hacks
            - How to match the trip vibe in activities and stay choices
            Keep it under 250 words and sound fun, conversational, and practical.
            """

            completion = client.chat.completions.create(
                extra_headers={
                    "HTTP-Referer": "https://student-trip-planner.streamlit.app",  # optional
                    "X-Title": "Student Road Trip Planner",  # optional
                },
                model="z-ai/glm-4.5-air:free",
                messages=[{"role": "user", "content": prompt}],
            )

            plan = completion.choices[0].message.content
            st.success("✅ Trip Plan Generated!")
            st.write(plan)

        except Exception as e:
            st.error(f"⚠️ Error generating trip plan: {e}")

st.divider()
st.caption("Made with ❤️ using Streamlit + OpenRouter")






