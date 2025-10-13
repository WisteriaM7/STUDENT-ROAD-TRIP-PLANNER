# STUDENT-ROAD-TRIP-PLANNER
Plan affordable, fun, and memorable student getaways 💸
🚗 Student Road Trip Planner

Plan affordable, fun, and memorable student getaways — powered by AI.
This Streamlit app helps students plan road trips by estimating budgets, visualizing cost breakdowns, and generating a personalized AI trip itinerary based on your preferences.

✨ Features

🧭 Trip Input Panel – Enter trip details like cities, duration, and travel mode

💰 Smart Budget Estimation – Get instant per-person and total cost breakdowns

📊 Visual Insights – Pie chart showing distribution of costs

🧠 AI-Powered Trip Plan – Automatically generate a student-friendly itinerary using OpenRouter’s DeepSeek model

🌈 Simple & Interactive UI – Built with Streamlit for smooth, real-time updates

🧩 Tech Stack
Tool / Library	Purpose
Streamlit	Interactive web app UI
Pandas	Data handling and table display
Matplotlib	Cost distribution pie chart
OpenAI / OpenRouter API	AI-powered trip plan generation
⚙️ Installation & Setup

Clone this repository

git clone https://github.com/yourusername/student-road-trip-planner.git
cd student-road-trip-planner


Create a virtual environment (recommended)

python -m venv venv
source venv/bin/activate    # Mac/Linux
venv\Scripts\activate       # Windows


Install dependencies

pip install -r requirements.txt


If you don’t have a requirements.txt, create one manually:

streamlit
pandas
matplotlib
openai


Set up your API key

Create a .streamlit/secrets.toml file in your project root:

OPENROUTER_API_KEY = "your_openrouter_api_key_here"


Get your free API key from https://openrouter.ai/

▶️ Run the App

Start the Streamlit app:

streamlit run app.py


Then open the app in your browser — it usually runs at:

http://localhost:8501

🧠 How It Works

You enter details like:

Start and destination city

Number of friends

Trip duration and vibe

The app estimates total cost (travel, stay, food, misc) and shows:

A breakdown table

A pie chart visualization

Hit “✨ Generate My Trip Plan”
→ The app calls OpenRouter’s DeepSeek model to create a:

Route overview

Day-by-day student itinerary

Budget hacks

Vibe-based recommendations

🧾 Example Output

Trip Summary:
A 5-day road trip from Delhi to Goa by Train with 4 friends.
Total Budget: ₹32,000 (~₹8,000 per person).
Day 1: Board overnight train, group games & snacks...
Day 2–4: Beach hopping, scooter rides, Goan street food, flea markets...
Day 5: Chill morning brunch and train back.

Tip: Carry refillable bottles & pre-book Airbnb for cheaper stays!

❤️ Credits

App Developer: You 😉

Powered by: Streamlit
, OpenRouter
, and DeepSeek

📜 License

This project is open-source and available under the MIT License.
Feel free to fork, remix, and make it your own student travel planner.
