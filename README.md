# 🚗 Student Road Trip Planner

**Plan affordable, fun, and memorable student getaways — powered by AI.**  
This Streamlit app helps students plan road trips by estimating budgets, visualizing cost breakdowns, and generating a personalized AI trip itinerary based on your preferences.

---

## ✨ Features

* 🧭 **Trip Input Panel** – Enter trip details like cities, duration, and travel mode  
* 💰 **Smart Budget Estimation** – Get instant per-person and total cost breakdowns  
* 📊 **Visual Insights** – Pie chart showing distribution of costs  
* 🧠 **AI-Powered Trip Plan** – Automatically generate a student-friendly itinerary using **OpenRouter’s DeepSeek R1T2 Chimera** model  
* 🌈 **Simple & Interactive UI** – Built with Streamlit for smooth, real-time updates  

---

## 🧩 Tech Stack

| Tool / Library              | Purpose                         |
| --------------------------- | ------------------------------- |
| **Streamlit**               | Interactive web app UI — write data apps in pure Python with no frontend experience needed |
| **Pandas**                  | Data handling and table display |
| **Matplotlib**              | Cost distribution pie chart     |
| **OpenRouter API**          | Unified access to 400+ models; routes requests to the best available provider with fallbacks for high uptime |
| **DeepSeek R1T2 Chimera**   | High-performance, student-optimized AI model (`tngtech/deepseek-r1t2-chimera`) via OpenRouter |

> 💡 **Why OpenRouter?**  
> OpenRouter provides a single, OpenAI-compatible API to access top models like DeepSeek with **lower latency (~2.5s)**, **edge-based inference**, and **automatic failover**—so your app stays reliable even under load.

---

## ⚙️ Installation & Setup

1. **Clone this repository**

   ```bash
   git clone https://github.com/yourusername/student-road-trip-planner.git
   cd student-road-trip-planner

2. **Create a virtual environment (recommended)**

   ```bash
   python -m venv venv
   source venv/bin/activate    # Mac/Linux
   venv\Scripts\activate       # Windows

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt

4. **Set up your OpenRouter API key**
   * Sign up at https://openrouter.ai
   * Get your API key from the dashboard
   * Create a .streamlit/secrets.toml file in your project root:
     ```bash
     OPENROUTER_API_KEY = "your_openrouter_api_key_here"

## 📜 License

This project is open-source and available under the Apache 2.0 License.
Feel free to fork, remix, and make it your own student travel planner.
