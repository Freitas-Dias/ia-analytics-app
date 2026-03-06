import streamlit as st
import pandas as pd

st.title("Análise de Ferramentas de IA")

uploaded_file = st.file_uploader("Envie sua planilha", type=["csv","xlsx"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write("Dados carregados:")
    st.dataframe(df)
