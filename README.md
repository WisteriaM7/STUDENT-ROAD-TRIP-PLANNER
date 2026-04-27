# 🗺️ Road Trip Planner
**Plan affordable, fun, and memorable getaways — powered by AI.**  
This Streamlit app helps you plan road trips by estimating budgets, visualizing cost breakdowns, and generating a personalized AI itinerary based on your preferences.

---

![WEBSITE VIEW](https://github.com/WisteriaM7/ROAD-TRIP-PLANNER/blob/main/APP%20VIEW/Screenshot%202025-10-14%20120116.png)

---

## ✨ Features

* 🧭 **Trip Input Panel** – Enter trip details like cities, duration, and travel mode  
* 💰 **Smart Budget Estimation** – Get instant per-person and total cost breakdowns  
* 📊 **Visual Insights** – Pie chart showing distribution of costs  
* 🧠 **AI-Powered Trip Plan** – Automatically generate a personalized itinerary using **OpenRouter's DeepSeek R1T2 Chimera** model  
* 🌈 **Simple & Interactive UI** – Built with Streamlit for smooth, real-time updates  

---

## 🧩 Tech Stack

| Tool / Library              | Purpose                         |
| --------------------------- | ------------------------------- |
| **Streamlit**               | Interactive web app UI — write data apps in pure Python with no frontend experience needed |
| **Pandas**                  | Data handling and table display |
| **Matplotlib**              | Cost distribution pie chart     |
| **OpenRouter API**          | Unified access to 400+ models; routes requests to the best available provider with fallbacks for high uptime |
| **Z.ai/GLM4.5-AIR**   | High-performance AI model (`z-ai/glm-4.5-air:free`) via OpenRouter |

> 💡 **Why OpenRouter?**  
> OpenRouter provides a single, OpenAI-compatible API to access top models like DeepSeek with **lower latency (~2.5s)**, **edge-based inference**, and **automatic failover** — so your app stays reliable even under load.

---

## ⚙️ Installation & Setup

1. **Clone this repository**
   ```bash
   git clone https://github.com/yourusername/road-trip-planner.git
   cd road-trip-planner
   ```

2. **Create a virtual environment (recommended)**
   ```bash
   python -m venv venv
   source venv/bin/activate    # Mac/Linux
   venv\Scripts\activate       # Windows
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up your OpenRouter API key**
   * Sign up at https://openrouter.ai  
   * Get your API key from the dashboard  
   * Create a `.streamlit/secrets.toml` file in your project root:
     ```toml
     OPENROUTER_API_KEY = "your_openrouter_api_key_here"
     ```

---

## 📜 License

This project is open-source and available under the Apache 2.0 License.  
Feel free to fork, remix, and make it your own travel planner.
