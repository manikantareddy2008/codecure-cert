import streamlit as st
st.title('Codecure Health AI - manikantareddy2008')
age = st.slider('Patient Age', 18, 80)
risk = 'High Risk' if age > 65 else 'Low Risk' 
st.success(f'Diabetes Risk: {risk}')
st.caption('IIT BHU Spirit 2026 Submission')
