import streamlit as st
import joblib
import pandas as pd

# Load trained model
model = joblib.load('threat_model.pkl')

# App title and description
st.set_page_config(page_title="System Threat Predictor")
st.title("🛡️ System Threat Forecasting App")
st.write("Enter system configuration to predict whether it's at risk.")

# Collect user inputs
ram = st.number_input("Total Physical RAM (in MB)", min_value=512, max_value=65536, step=512)
core_count = st.slider("Processor Core Count", 1, 16)
chassis_type = st.selectbox("Chassis Type", [3, 8, 9, 10, 14])  # Example values
is_protected = st.selectbox("Is System Protected?", [0, 1])
is_gamer = st.selectbox("Is Gamer?", [0, 1])
power_platform_role = st.selectbox("Power Platform Role", [1, 2, 3])  # Example values


# Build DataFrame with required columns
input_data = pd.DataFrame([{
    'TotalPhysicalRAMMB': ram,
    'ProcessorCoreCount': core_count,
    'ChassisType': chassis_type,
    'IsSystemProtected': is_protected,
    'IsGamer': is_gamer,
    'PowerPlatformRole': power_platform_role,
}])

# Prediction
if st.button("🔍 Predict"):
    prediction = model.predict(input_data)[0]

    proba = model.predict_proba(input_data)[0][1]

    if prediction == 1:
        st.error(f"⚠️ High Risk: System is likely to be under threat! (Probability: {proba:.2f})")
    else:
        st.success(f"✅ Safe: System is unlikely to be under threat. (Probability: {proba:.2f})")
