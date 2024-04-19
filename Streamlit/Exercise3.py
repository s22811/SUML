import streamlit as st
import numpy as np

def kg_to_lbs(kg):
    return kg * 2.20462

def lbs_to_kg(lbs):
    return lbs / 2.20462

def km_to_miles(km):
    return km * 0.621371

def miles_to_km(miles):
    return miles / 0.621371

def c_to_f(c):
    return (c * 9/5) + 32

def f_to_c(f):
    return (f - 32) * 5/9

st.title('Konwerter Jednostek')

conversion_type = st.selectbox("Wybierz typ konwersji", ["Kilogramy na Funty", "Funty na Kilogramy", 
                                                         "Kilometry na Mile", "Mile na Kilometry",
                                                         "Celsjusz na Fahrenheita", "Fahrenheit na Celsjusza"])

value = st.number_input("Wprowadź wartość do konwersji", step=1.0, format="%.2f")

if st.button('Konwertuj'):
    result = 0
    if conversion_type == "Kilogramy na Funty":
        result = kg_to_lbs(value)
    elif conversion_type == "Funty na Kilogramy":
        result = lbs_to_kg(value)
    elif conversion_type == "Kilometry na Mile":
        result = km_to_miles(value)
    elif conversion_type == "Mile na Kilometry":
        result = miles_to_km(value)
    elif conversion_type == "Celsjusz na Fahrenheita":
        result = c_to_f(value)
    elif conversion_type == "Fahrenheit na Celsjusza":
        result = f_to_c(value)
    
    st.success(f"Wynik: {result:.2f}")
else:
    st.info("Wprowadź wartość i kliknij przycisk 'Konwertuj' aby zobaczyć wynik.")

