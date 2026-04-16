import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Carregar dados
df = pd.read_csv("resultado.csv")

st.title("🌱 Dashboard de Monitoramento Agrícola")

# Métrica 1: quantidade de imagens
st.metric("Quantidade de imagens analisadas", len(df))

# Métrica 2: saudáveis vs doentes
st.subheader("Distribuição de folhas")

categoria_counts = df["categoria"].value_counts()

fig, ax = plt.subplots()
ax.pie(categoria_counts, labels=categoria_counts.index, autopct='%1.1f%%')
st.pyplot(fig)

# Métrica 3: confiança média
st.subheader("Confiança média por categoria")

media = df.groupby("categoria")["confianca"].mean()

st.bar_chart(media)

# Tabela
st.subheader("Dados detalhados")
st.dataframe(df)