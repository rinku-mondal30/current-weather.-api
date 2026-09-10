# 🌦️ Real-Time Weather Prediction Dashboard

An interactive, dynamic Python web application built using the **Streamlit** framework and developed in **VS Code**. This project features a clean, responsive welcome/login portal and fetches authentic live global weather metrics (Temperature, Humidity, and Rainfall Probability) by connecting to a public meteorological API.

---

## 📱 Live Mobile Access Link
You can open and test this application directly from your smartphone or web browser by clicking the link below:

👉 **[Launch Live Weather App](https://streamlit.app)** 

---

## 🚀 Key Features

* **Secure Welcome Portal:** An entry-level interactive login screen that dynamically grants access to the dashboard.
* **Live Global Weather Data:** Fetches instant real-time data including current temperatures, relative humidity levels, and current daily weather conditions.
* **Precipitation Forecasting:** Calculates and presents the real-time probability percentage of rainfall for the searched destination.
* **Modern Dashboard UI:** Utilizes visual metric cards, multi-column layouts, and a dedicated account operations sidebar.

---

## 📁 Repository Directory Structure

```text
weather-app/
├── app.py              # Main Streamlit web application script
├── requirements.txt    # Declared project dependencies
└── README.md           # Project configuration guide & documentation
```

---

## 🛠️ Step-by-Step Local Setup & Web Deployment

Follow these sequential steps to get the web application running locally on your computer inside VS Code or deployed to the web:

### 1. Clone this Repository
Open your local terminal and clone the workspace repository:
```bash
git clone https://github.com
cd current-weather.-api
```

### 2. Install Project Dependencies
Install the required standard libraries using the pip package manager:
```bash
pip install streamlit requests
```

### 3. Obtain a Free WeatherAPI Developer Key
This project requires an active API key to fetch live data from the global servers:
1. Go to [WeatherAPI.com](https://weatherapi.com) and register a free account.
2. Navigate to your account dashboard and copy your generated **API Key**.
3. Open `app.py` in VS Code and update the configuration variable at the top of the file:
   ```python
   API_KEY = "YOUR_WEATHERAPI_KEY_HERE"
   ```

### 4. Launch the Application Locally
Run the local Streamlit application framework using your terminal:
```bash
streamlit run app.py
```
*Your operating system's default web browser will automatically open the responsive front page at `http://localhost:8501`.*

### 5. Deploy to Streamlit Cloud for Public Mobile Access
To access the application instantly from any mobile browser using a single shared URL link:
1. Push your finalized code to your public GitHub repository (`rinku-mondal30/current-weather.-api`).
2. Visit [share.streamlit.io](https://streamlit.io) and log in with your GitHub account.
3. Click **"Create app"** and target your repository, the `main` branch, and set the main file path to `app.py`.
4. Click **"Advanced settings..."** at the bottom right, and securely add your live token in the **Secrets** box:
   ```toml
   WEATHER_API_KEY = "136307eeeeb24a11bb831731261009"
   ```
5. Click **Save**, then hit **"Deploy!"** to generate your permanent public application link:
   👉 **https://streamlit.app**

---

## 🛡️ Security Best Practices for Production
> ⚠️ **Important Warning:** Never push your real, unencrypted production API keys directly to public GitHub repositories. 

To keep your personal developer keys completely safe on GitHub:
* Utilize an environment configuration file (like `.env`) or setup **Streamlit Secrets Management** (`.streamlit/secrets.toml`) to load keys safely using environment variables.
* Always add sensitive local configuration files to your project's `.gitignore` file before running a git commit.
