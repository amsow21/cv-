import streamlit as st

# 1. Configuration de la page
st.set_page_config(
    page_title="Aminata Minielle Sow | Géomaticienne",
    page_icon="🌍",
    layout="wide"
)

# ---- STYLE PERSONNALISÉ ----
st.markdown("""
<style>
    .main {
        background-color: #0e1117;
        color: white;
    }
    h1 {
        color: #4da6ff !important;
        font-size: 42px;
    }
    h2, h3 {
        color: #4da6ff !important;
    }
    section[data-testid="stSidebar"] {
        background-color: #161b22;
    }
</style>
""", unsafe_allow_html=True)

# ---- BARRE LATÉRALE (SIDEBAR) ----
with st.sidebar:
    st.markdown("## Aminata Minielle Sow")
    st.write("🎓 Étudiante en BTS Géomatique")
    st.write("📍 Saint-Louis, Sénégal")
    st.write("📧 aminaminiellesow@gmail.com")
    st.write("[LinkedIn](https://www.linkedin.com/in/aminata-minielle-sow-282400369)")

    st.markdown("---")
    st.subheader("Compétences clés")
    st.markdown("""
    - SIG: QGIS, ArcGIS
    - Data: Python, SQL, Analyse spatiale
    - Web: HTML, CSS, JavaScript
    - Cartographie: Numérique & Thématique
    """)

# ---- SECTION D'ACCUEIL (HERO) ----
col1, col2 = st.columns([2, 1], gap="medium")

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
    try:
        st.image("oip.png", use_container_width=True)
   

st.markdown("---")

# ---- FORMATIONS & PROJETS ----
col_f, col_p = st.columns(2)

with col_f:
    st.header("🎓 Formations")
    st.write("**BTS Géomatique** – CEDT (En cours)")
    st.write("**Licence Web** – Développement & Administration")
    st.write("**Baccalauréat L2** – Lycée Ameth Fall, Saint-Louis")
    st.write("**BFEM** – Lycée Ameth Fall")

with col_p:
    st.header("📌 Projets académiques")
    st.write("• Base de données géospatiale du Sénégal")
    st.write("• Analyse du réseau routier (ArcGIS)")
    st.write("• Cartographie hydrologique et administrative")

st.markdown("---")

# ---- CONTACT ----
st.header("📫 Me contacter")
st.write("Je suis actuellement à la recherche d'opportunités de stage ou de collaboration.")
st.info("Contactez-moi directement par mail : **aminaminiellesow@gmail.com**")

st.markdown("---")
st.success("Merci d’avoir visité mon portfolio.")
