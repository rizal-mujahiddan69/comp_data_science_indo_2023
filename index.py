import streamlit as st

st.title("Keterangan")

st.markdown(
    """
    * __Customer ID__ (A unique customer identifier)
* __Tenure Months__ (How long the customer has been with the company by the end of the quarter specified above)
* __Location__ (Customer's residence - City)
* __Device Class__ (Device classification)
* __Games Product__ (Whether the customer uses the internet service for games product)
* __Music Product__ (Whether the customer uses the internet service for music product)
* __Education Product__ (Whether the customer uses the internet service for education product)
* __Call Center__ (Whether the customer uses the call center service)
* __Video Product__ (Whether the customer uses video product service)
* __Use MyApp__ (Whether the customer uses MyApp service)
* __Payment Method__ (The method used for paying the bill)
* __Monthly Purchase__ (Total customer’s monthly spent for all services with the unit of thousands of IDR)
* __Churn Label__ (Whether the customer left the company in this quarter)
* __Longitude__ (Customer’s residence - Longitude)
* __Latitude__ (Customer’s residence - Latitude)
* __CLTV__ (Customer Lifetime Value with the unit of thousands of IDR - Calculated using company's formulas)
    """
)
