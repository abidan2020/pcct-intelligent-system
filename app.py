import streamlit as st
import pandas as pd

st.set_page_config(page_title="PCCT Intelligent", layout="centered")

st.title("🧠 Système embarqué intelligent - PCCT")

# Charger données
df = pd.read_csv("data.csv")

index = st.slider("Choisir un cycle (patient)", 0, len(df)-1)

ligne = df.iloc[index]

snr = ligne['SNR']
delta = ligne['Delta_SNR']
stress = ligne['Stress_score']
decision = ligne['Decision_dose_min_v2']

st.subheader("📡 Capteurs")
st.write(f"SNR : {snr}")
st.write(f"Delta SNR : {delta}")
st.write(f"Stress : {stress}")

st.subheader("🔍 Analyse")

if decision == "Conserver ou réduire la dose":
    st.success("🟢 Stable")
elif decision == "Recalibration avant ajustement":
    st.warning("🟡 Dégradé")
elif decision == "Ajustement léger mAs si nécessaire":
    st.info("🟠 Surveillance")
else:
    st.error("🔴 Critique")

st.subheader("⚙️ Décision")
st.write(decision)
