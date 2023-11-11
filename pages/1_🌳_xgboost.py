import joblib
import numpy as np
import pandas as pd
import pickle
import streamlit as st
import xgboost


st.title("Model XGBoost Mengenai Churn")

model_churn = joblib.load("models/pipeline_model_tree.pkl")

left_col, right_col = st.columns(2)

with left_col:
    tenure_months = st.number_input("Tenure Months", min_value=0)
    device_class = st.selectbox("Device Class", ("Low End", "Medium End", "High End"))
    music_product = st.selectbox("have Music Product ?", ("No", "Yes"))
    call_center = st.selectbox("have Call Center ?", ("No", "Yes"))
    use_myapp = st.selectbox("have Use MyApp ?", ("No", "Yes"))
    monthly_purchase = st.number_input("Monthly Purchase (Thou. IDR)", min_value=0)


with right_col:
    location = st.selectbox("Lokasi Pengguna ?", ("Jakarta", "Bandung"))
    games_product = st.selectbox("have Games Product ?", ("No", "Yes"))
    education_product = st.selectbox("have Education Product ?", ("No", "Yes"))
    video_product = st.selectbox("have Video Product ?", ("No", "Yes"))
    payment_method = st.selectbox(
        "have Payment Method ?",
        ("Pulsa", "Credit", "Digital Wallet", "Debit"),
    )
    cltv = st.number_input("CLTV (Predicted Thou. IDR)", min_value=0)

inputan = np.array(
    [
        [
            tenure_months,
            # location,
            device_class,
            games_product,
            music_product,
            education_product,
            call_center,
            video_product,
            use_myapp,
            payment_method,
            monthly_purchase,
            cltv,
        ]
    ]
)
# col_name = []
# st.write(dir(model_churn))
# st.write(model_churn.feature_names_in_)

# st.write(model_churn.feature_names_in_)
input_var = pd.DataFrame(inputan, columns=model_churn.feature_names_in_)
# st.write(input_var)
hasilnya = model_churn.predict(input_var)
if hasilnya == 1:
    hasilnya = "Churn"
else:
    hasilnya = "No Churn"


# st.write(model_churn.nam7ed_steps)
# df_one = model_churn.steps[0][1].transform(input_var)
# st.write(df_one)
# st.write(model_churn.steps)
# st.write(model_churn.steps[2][1])
st.write(
    f"""
    Bahwa Customer itu churn ? __{hasilnya}__
"""
)
