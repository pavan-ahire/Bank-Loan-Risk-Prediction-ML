import streamlit as st
import numpy as np
import joblib

st.set_page_config(page_title="Loan Risk Predictor 💳", layout="wide")

# Custom CSS Styling
st.markdown("""
<style>
.main-title {
    font-size:42px;
    font-weight:700;
    text-align:center;
    color:#2E86C1;
}
.subtitle {
    text-align:center;
    font-size:18px;
    color:#5D6D7E;
}
.card {
    padding:20px;
    border-radius:12px;
    text-align:center;
    font-size:30px;
    font-weight:bold;
    margin-top:20px;
}
.low {
    background: linear-gradient(90deg,#d4fc79,#96e6a1);
    color:#145A32;
}
.high {
    background: linear-gradient(90deg,#f6d365,#fda085);
    color:#641E16;
}
.footer {
    text-align:center;
    font-size:14px;
    color:gray;
    margin-top:30px;
}
</style>
""", unsafe_allow_html=True)
st.markdown("""
<style>

/* Button styling */
div.stButton > button {
    background: linear-gradient(90deg, #36D1DC, #5B86E5);
    color: white;
    font-size:18px;
    font-weight:600;
    padding:12px 25px;
    border-radius:10px;
    border:none;
    transition: 0.3s ease;
    width:100%;
}

/* Hover effect */
div.stButton > button:hover {
    background: linear-gradient(90deg, #FF7E5F, #FEB47B);
    transform: scale(1.03);
    box-shadow: 0px 4px 12px rgba(0,0,0,0.25);
    color:white;
}

/* Click effect */
div.stButton > button:active {
    transform: scale(0.97);
}

</style>
""", unsafe_allow_html=True)


# Header
st.write("")
col1, col2, col3 = st.columns([1,2,1])

with col2:
    st.image("bankloan.png", width=700)

st.write("")

#st.image('bankloan.png',width=700,)
st.markdown('<div class="main-title">💳 Loan Risk Prediction System</div>', unsafe_allow_html=True)
#st.markdown('<div class="subtitle">Machine Learning Project • Random Forest • Streamlit Deployment 🚀</div>', unsafe_allow_html=True)

st.write("")

# Load model
model = joblib.load("rf_model.pkl")
scaler = joblib.load("scaler.pkl")

# Layout
col1, col2 = st.columns(2)

# Column 1: Numeric Inputs
with col1:
    st.subheader("📊 Financial Information")

    person_age = st.slider("👤 Age", 18, 70, 30)
    person_income = st.number_input("💰 Annual Income", value=50000)
    person_emp_length = st.slider("💼 Employment Length (Years)", 0, 40, 5)

    loan_amnt = st.number_input("🏦 Loan Amount", value=10000)
    loan_int_rate = st.slider("📈 Interest Rate (%)", 1.0, 30.0, 10.0)
    loan_percent_income = st.slider("📉 Loan Percent of Income", 0.0, 1.0, 0.2)
    cb_person_cred_hist_length = st.slider("📜 Credit History Length", 1, 30, 5)

# Column 2: Categorical Inputs
with col2:
    st.subheader("📝 Loan & Profile Details")

    home_ownership = st.selectbox("🏠 Home Ownership",
        ["RENT", "OWN", "MORTGAGE", "OTHER"])

    loan_intent = st.selectbox("🎯 Loan Purpose",
        ["EDUCATION","MEDICAL","PERSONAL","VENTURE",
         "HOMEIMPROVEMENT","DEBTCONSOLIDATION"])

    loan_grade = st.selectbox("⭐ Loan Grade",
        ["A","B","C","D","E","F","G"])

    default_history = st.selectbox("⚠ Previous Default",
        ["N","Y"])

# Encoding maps
home_map = {"RENT":0, "OWN":1, "MORTGAGE":2, "OTHER":3}
intent_map = {
    "EDUCATION":0,
    "MEDICAL":1,
    "PERSONAL":2,
    "VENTURE":3,
    "HOMEIMPROVEMENT":4,
    "DEBTCONSOLIDATION":5
}
grade_map = {"A":0,"B":1,"C":2,"D":3,"E":4,"F":5,"G":6}
default_map = {"N":0,"Y":1}

st.write("")

# Predict button
if st.button("🔍 Predict Loan Risk", use_container_width=True):

    input_data = np.array([[
        person_age,
        person_income,
        home_map[home_ownership],
        person_emp_length,
        intent_map[loan_intent],
        grade_map[loan_grade],
        loan_amnt,
        loan_int_rate,
        loan_percent_income,
        default_map[default_history],
        cb_person_cred_hist_length
    ]])

    input_scaled = scaler.transform(input_data)

    prediction = model.predict(input_scaled)[0]
    prob = model.predict_proba(input_scaled)[0]

    low_risk_prob = prob[0] * 100
    high_risk_prob = prob[1] * 100

    # Confidence logic
    confidence = max(low_risk_prob, high_risk_prob)

    if confidence < 60:
        confidence_label = "⚠ Low Confidence Prediction"
    elif confidence < 80:
        confidence_label = "🔶 Medium Confidence"
    else:
        confidence_label = "✅ High Confidence"

    # Result Display
    st.markdown("---")

    if prediction == 1:
        st.error(f"🚨 HIGH RISK LOAN")
    else:
        st.success(f"✅ LOW RISK LOAN")

    st.markdown(f"### {confidence_label}")

    # Probability bars
    st.write("### Risk Breakdown")
    st.progress(int(high_risk_prob))
    st.write(f"High Risk Probability: **{high_risk_prob:.2f}%**")

    st.progress(int(low_risk_prob))
    st.write(f"Low Risk Probability: **{low_risk_prob:.2f}%**")

#footer
st.markdown("---")
st.caption("📊 Machine Learning Powered | Streamlit App | Created by Pavan Ahire")
