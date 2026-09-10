import streamlit as st
import requests

# ==========================================
# ⚙️ CONFIGURATION & API SETUP
# ==========================================
# Get your free API key from https://weatherapi.com and paste it below
API_KEY = st.secrets["136307eeeeb24a11bb831731261009 "]

st.set_page_config(
    page_title="Live Weather Dashboard",
    page_icon="🌦️",
    layout="centered"
)

# ==========================================
# 🔒 USER AUTHENTICATION STATE
# ==========================================
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# ==========================================
# 🚪 WELCOME / LOGIN FRONT PAGE
# ==========================================
if not st.session_state.logged_in:
    st.title("👋 Welcome to the Weather Dashboard")
    st.write("Please sign in below to unlock live global weather metrics.")
    
    with st.form("login_form"):
        username = st.text_input("Username", placeholder="Enter your username")
        password = st.text_input("Password", type="password", placeholder="Enter your password")
        submit_btn = st.form_submit_button("Sign In")
        
        if submit_btn:
            # Flexible validation for demo purposes—accepts any input
            if username.strip() != "" and password.strip() != "":
                st.session_state.logged_in = True
                st.success(f"Welcome back, {username}! Loading dashboard...")
                st.rerun()
            else:
                st.error("Please enter a valid Username and Password.")

# ==========================================
# 🌦️ MAIN APP: LIVE WEATHER DASHBOARD
# ==========================================
else:
    # Sidebar logout controls
    with st.sidebar:
        st.header("👤 Account Operations")
        if st.button("Log Out"):
            st.session_state.logged_in = False
            st.rerun()

    st.title("🌦️ Real-Time Weather Forecast")
    st.write("Enter any global city or location below to fetch live meteorological data.")

    # Location Lookup Input
    location = st.text_input("📍 Location Target", placeholder="e.g., London, New York, Tokyo, Kolkata")

    if location:
        if API_KEY == "YOUR_WEATHERAPI_KEY_HERE":
            # Fallback mock placeholder if user hasn't inserted a live API Key yet
            st.warning("⚠️ Using local simulation mode. Replace 'YOUR_WEATHERAPI_KEY_HERE' in the script with a real key for live tracking.")
            
            st.subheader(f"📊 Weather Insights for: {location.title()}")
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric(label="🌡️ Temperature", value="24.5 °C")
            with col2:
                st.metric(label="💧 Humidity", value="68 %")
            with col3:
                st.metric(label="🌧️ Rainfall Probability", value="42 %")
        else:
            # Executing authentic external live API call
            with st.spinner("Connecting to global meteorological relays..."):
                try:
                    # Using WeatherAPI Forecast endpoint to access daily parameters (chance of rain)
                    api_url =  f"http://api.weatherapi.com/v1/forecast.json?key={API_KEY}&q={location}&days=1&aqi=no&alerts=no"

                    response = requests.get(api_url, timeout=10)
                    
                    if response.status_code == 200:
                        data = response.json()
                        
                        # Parsing targeted metrics from JSON payload
                        city_name = data["location"]["name"]
                        country = data["location"]["country"]
                        temp_c = data["current"]["temp_c"]
                        humidity = data["current"]["humidity"]
                        
                        # Extracting rainfall chance from the today's forecast hours/day profile
                        forecast_day = data["forecast"]["forecastday"][0]["day"]
                        rain_chance = forecast_day.get("daily_chance_of_rain", "N/A")
                        condition = data["current"]["condition"]["text"]
                        
                        # Displaying results to the frontend layout
                        st.subheader(f"📊 Weather Insights for: {city_name}, {country}")
                        st.info(f"Current Condition: **{condition}**")
                        
                        col1, col2, col3 = st.columns(3)
                        with col1:
                            st.metric(label="🌡️ Temperature", value=f"{temp_c} °C")
                        with col2:
                            st.metric(label="💧 Humidity", value=f"{humidity} %")
                        with col3:
                            st.metric(label="🌧️ Rainfall Probability", value=f"{rain_chance} %")
                            
                    elif response.status_code == 400:
                        st.error("❌ Location not found. Please verify the spelling and try again.")
                    else:
                        st.error("🔒 Invalid API Key or server authorization issues.")
                except Exception as e:
                    st.error(f"🌐 Connectivity error: {e}")
