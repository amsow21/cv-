import streamlit as st

# Configuration page
st.set_page_config(
    page_title="Aminata Minielle Sow | Géomaticienne",
    page_icon="🌍",
    layout="wide"
)

# ---- STYLE ----
st.markdown("""
<style>
body {
    background-color: #0e1117;
}
.main {
    background-color: #0e1117;
    color: white;
}
h1 {
    color: #4da6ff;
    font-size: 42px;
}
h2, h3 {
    color: #4da6ff;
}
section[data-testid="stSidebar"] {
    background-color: #161b22;
}
.block-container {
    padding-top: 2rem;
}
</style>
""", unsafe_allow_html=True)

# ---- SIDEBAR ----
with st.sidebar:
    st.markdown("## Aminata Minielle Sow")
    st.write("🎓 Étudiante en BTS Géomatique")
    st.write("📍 Saint-Louis, Sénégal")
    st.write("📧 aminaminiellesow@gmail.com")
    st.write("[LinkedIn](https://www.linkedin.com/in/aminata-minielle-sow-282400369)")

    st.markdown("---")
    st.subheader("Compétences clés")
    st.write("• QGIS")
    st.write("• ArcGIS")
    st.write("• Analyse spatiale")
    st.write("• Python")
    st.write("• SQL")
    st.write("• Cartographie numérique")

# ---- HERO SECTION ----
col1, col2 = st.columns([2,1])

with col1:
    st.title("Aminata Minielle Sow")
    st.markdown("### Géomaticienne | Analyse spatiale | SIG")
    st.write(
        "Étudiante en deuxième année de BTS en Géomatique au CEDT, "
        "je développe des compétences solides en systèmes d’information géographique, "
        "analyse spatiale et gestion de données territoriales. "
        "Je m’intéresse particulièrement aux projets liés à l’aménagement du territoire "
        "et à la cartographie moderne."
    )

with col2:
    st.image("profile.jpg", use_column_width=True)

st.markdown("---")

# ---- FORMATIONS ----
st.header("🎓 Formations")

st.write("*BTS Géomatique* – CEDT (en cours)")
st.write("*Licence Développement & Administration d’Applications Web*")
st.write("*Baccalauréat L2* – Lycée Ameth Fall, Saint-Louis")
st.write("*BFEM* – Lycée Ameth Fall")

st.markdown("---")

# ---- PROJETS ----
st.header("📌 Projets académiques")

st.write("• Base de données géospatiale des régions du Sénégal")
st.write("• Analyse du réseau routier par région (ArcGIS)")
st.write("• Cartographie des villages, limites administratives et réseaux hydrologiques")

st.markdown("---")

# ---- CARTE INTERACTIVE ----
st.header("🗺️ Localisation")

m = folium.Map(location=[16.0179, -16.4896], zoom_start=10)
folium.Marker(
    [16.0179, -16.4896],
    popup="Saint-Louis, Sénégal",
    tooltip="Ma localisation"
).add_to(m)

st_folium(m, width=700, height=400)

st.markdown("---")

# ---- BOUTON TELECHARGEMENT ----
try:
    with open("cv.pdf", "rb") as file:
        st.download_button(
            label="📄 Télécharger mon CV (PDF)",
            data=file,
            file_name="CV_Aminata_Minielle_Sow.pdf",
            mime="application/pdf"
        )
except:
    pass

st.markdown("---")
st.success("Merci d’avoir visité mon portfolio.")
