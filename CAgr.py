import streamlit as st

st.title("CAGR Calculator")

beginning_value = st.number_input("Enter Beginning Value", min_value=0.0)
ending_value = st.number_input("Enter Ending Value", min_value=0.0)
years = st.number_input("Enter Number of Years", min_value=0.0)

if st.button("Calculate CAGR"):
    if beginning_value > 0 and years > 0:
        cagr = ((ending_value / beginning_value) ** (1 / years)) - 1
        st.success(f"CAGR: {cagr * 100:.2f}%")
    else:
        st.error("Beginning value and years must be greater than 0.")
