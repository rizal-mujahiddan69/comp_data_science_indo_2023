import streamlit as st
import pickle

model_churn = pickle.load(open("models/churn_model.sav", "rb"))

left_col, right_col = st.columns(2)

with left_col:
    tenure_months = st.number_input("Tenure Months", min_value=0)
    device_class = st.selectbox("Device Class", ("Low End", "Medium End", "High End"))
    device_class = 1 if device_class == "High End" else 0


with right_col:
    location = st.selectbox("Lokasi Pengguna?", ("Jakarta", "Bandung"))
    location = 1 if location == "Jakarta" else 0
    games_product = st.selectbox("have Games Product ?", ("No", "Yes"))
    games_product = 1 if games_product == "Yes" else 0

st.write(games_product)
st.write(model_churn)

# df = pd.read_excel('Telco_customer_churn_adapted_v2.xlsx')
# df = df.drop(columns=['Longitude', 'Latitude', 'Customer ID'])
# scaler = MinMaxScaler()
# columns_to_normalize = ["Tenure Months","Monthly Purchase (Thou. IDR)","CLTV (Predicted Thou. IDR)"]
# df[columns_to_normalize] = scaler.fit_transform(df[columns_to_normalize])
# df = df[df['Games Product'] != 'No internet service']
# df[['Games Product','Music Product','Education Product','Call Center','Video Product','Use MyApp','Churn Label']] = (df[['Games Product','Music Product','Education Product','Call Center','Video Product','Use MyApp','Churn Label']] == 'Yes').astype(int)
# df['Location'] = (df['Location'] == 'Jakarta').astype(int)
# df['Device Class'] = (df['Device Class'] == 'High End').astype(int)
# df = pd.get_dummies(df, columns=['Payment Method'])
# X = df.drop(columns=['Churn Label'])
# y = df['Churn Label']
