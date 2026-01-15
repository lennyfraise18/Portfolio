import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import requests
from streamlit_lottie import st_lottie

# --- CONFIGURATION DE LA PAGE ---
st.set_page_config(
    page_title="Lenny Fraise | Growth & Data",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- FONCTION CHARGEMENT LOTTIE ---
def load_lottieurl(url):
    try:
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()
    except:
        return None

# Assets
lottie_marketing = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_fcfjwiyb.json")
lottie_contact = load_lottieurl("https://assets8.lottiefiles.com/packages/lf20_u25cckyh.json")

# --- CSS ULTRA-STYLISE & CORRIGÉ ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;800&display=swap');
    
    /* 1. RESET GLOBAL & POLICE */
    html, body, [class*="css"], .stApp {
        font-family: 'Poppins', sans-serif;
        background-color: #FAFAFA;
        color: #333;
    }

    /* 2. CORRECTION SIDEBAR (FOND BLANC & TEXTE FONCÉ) */
    [data-testid="stSidebar"] {
        background-color: #ffffff !important;
        border-right: 1px solid #eaeaea;
        box-shadow: 2px 0 10px rgba(0,0,0,0.02);
    }

    /* Force la couleur du texte dans la sidebar */
    [data-testid="stSidebar"] h1, 
    [data-testid="stSidebar"] h2, 
    [data-testid="stSidebar"] h3, 
    [data-testid="stSidebar"] p, 
    [data-testid="stSidebar"] span, 
    [data-testid="stSidebar"] li, 
    [data-testid="stSidebar"] div,
    [data-testid="stSidebar"] label {
        color: #2c3e50 !important;
    }

    /* Style spécifique pour l'image de profil (Rond + Animation) */
    [data-testid="stSidebar"] [data-testid="stImage"] img {
        border-radius: 50%;
        border: 4px solid #FF416C;
        padding: 3px;
        transition: transform 0.4s ease, box-shadow 0.4s ease;
    }
    [data-testid="stSidebar"] [data-testid="stImage"] img:hover {
        transform: scale(1.08);
        box-shadow: 0 10px 25px rgba(255, 65, 108, 0.4);
        cursor: pointer;
    }

    /* 3. STYLE DES BOUTONS SOCIAUX (SIDEBAR) */
    .social-link {
        display: flex;
        align-items: center;
        background: #f8f9fa;
        padding: 10px 15px;
        border-radius: 10px;
        margin-bottom: 8px;
        text-decoration: none !important;
        transition: all 0.3s ease;
        border: 1px solid transparent;
    }
    .social-link:hover {
        background: white;
        border: 1px solid #FF416C;
        transform: translateX(5px);
        box-shadow: 0 4px 10px rgba(0,0,0,0.05);
    }
    .social-icon {
        font-size: 1.2rem;
        margin-right: 10px;
    }
    .social-text {
        font-weight: 600;
        font-size: 0.9rem;
        color: #333 !important;
    }

    /* 4. BOUTON DOWNLOAD CV */
    .stDownloadButton button {
        background: linear-gradient(90deg, #FF4B2B, #FF416C) !important;
        color: white !important;
        border: none !important;
        width: 100%;
        padding: 12px !important;
        border-radius: 10px !important;
        font-weight: bold !important;
        text-transform: uppercase;
        letter-spacing: 1px;
        transition: transform 0.2s;
    }
    .stDownloadButton button:hover {
        transform: scale(1.02);
        box-shadow: 0 5px 15px rgba(255, 65, 108, 0.4);
    }

    /* 5. TITRES ET TEXTES PRINCIPAUX */
    .hero-title {
        font-size: 3.5rem;
        font-weight: 800;
        background: linear-gradient(120deg, #FF4B2B, #FF416C);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        line-height: 1.2;
    }
    
    .section-title {
        font-size: 2rem;
        font-weight: 700;
        margin-top: 60px;
        margin-bottom: 30px;
        border-left: 5px solid #FF416C;
        padding-left: 15px;
        color: #2c3e50 !important;
    }

    /* 6. CARDS & TIMELINE */
    .glass-card {
        background: white;
        border-radius: 15px;
        padding: 25px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.05);
        border: 1px solid rgba(0,0,0,0.05);
        transition: transform 0.3s ease, box-shadow 0.3s ease;
        height: 100%;
    }
    .glass-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 15px 30px rgba(255, 65, 108, 0.15);
        border-color: #FF416C;
    }

    .timeline-item {
        border-left: 3px solid #FF416C;
        padding-left: 30px;
        margin-left: 10px;
        position: relative;
        padding-bottom: 30px;
    }
    .timeline-dot {
        position: absolute; left: -9px; top: 0;
        width: 15px; height: 15px;
        background: #FF416C; border-radius: 50%;
    }
    .timeline-date {
        color: #FF4B2B !important;
        font-weight: 700; font-size: 0.9rem; text-transform: uppercase;
    }

    /* BADGES */
    .badge {
        display: inline-block; padding: 5px 15px; margin: 3px;
        border-radius: 20px; color: white !important;
        font-weight: 600; font-size: 0.8rem;
    }
    .badge-marketing { background: linear-gradient(90deg, #FF416C, #FF4B2B); }
    .badge-data { background: linear-gradient(90deg, #3498DB, #2E86C1); }
    
    /* CUSTOM ALERTS */
    .stAlert { border-radius: 10px; }
    
    a { text-decoration: none; }
    </style>
""", unsafe_allow_html=True)

# --- SIDEBAR (CONTENU) ---
with st.sidebar:
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Photo de profil
    try:
        st.image("photo_lenny.jpg", width=140)
    except:
        st.markdown('<div style="text-align:center; font-size:4rem;">👨‍💻</div>', unsafe_allow_html=True)

    st.markdown("""
    <div style="text-align: center; margin-top: 15px;">
        <h2 style="margin:0; font-size: 1.8rem;">Lenny Fraise</h2>
        <p style="font-style: italic; color: #666 !important; font-size: 0.9rem;">Making Data Speak Business</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)

    # Status Box
    st.markdown("""
    <div style="background: #E8F5E9; padding: 15px; border-radius: 10px; border-left: 4px solid #2ECC71; margin-bottom: 25px;">
        <div style="font-weight:bold; color: #27AE60 !important; font-size: 0.9rem;">🚀 DISPONIBLE JUIN 2026</div>
        <div style="font-size: 0.85rem; color: #1E8449 !important;">Recherche Stage Marketing IA</div>
    </div>
    """, unsafe_allow_html=True)
    
    # CV Download
    st.write("**📄 Mon CV**")
    try:
        with open("CV_Lenny_Fraise.pdf", "rb") as f:
            st.download_button("📥 Télécharger le PDF", f, "CV_Lenny_Fraise.pdf", "application/pdf")
    except:
        st.warning("⚠️ Ajoute 'CV_Lenny_Fraise.pdf'")

    st.markdown("---")

    # Liens Sociaux Stylisés
    st.write("**🌐 Mes Réseaux**")
    
    st.markdown("""
    <a href="https://linkedin.com/in/lenny-fraise" target="_blank" class="social-link">
        <span class="social-icon">🔗</span>
        <span class="social-text">LinkedIn</span>
    </a>
    
    <a href="https://github.com/lennyfraise18" target="_blank" class="social-link">
        <span class="social-icon">🐙</span>
        <span class="social-text">GitHub Portfolio</span>
    </a>
    
    <a href="mailto:lenny.fraise@gmail.com" class="social-link">
        <span class="social-icon">📧</span>
        <span class="social-text">Me Contacter</span>
    </a>
    """, unsafe_allow_html=True)

# --- HERO SECTION ---
c1, c2 = st.columns([1.5, 1])

with c1:
    st.markdown('<div class="hero-title">Marketing Strategist<br>& Data Analyst</div>', unsafe_allow_html=True)
    st.markdown("""
    <div style="font-size: 1.2rem; margin-top: 20px; margin-bottom: 30px; color: #555 !important;">
    Je transforme la donnée complexe en stratégie marketing claire, rentable et automatisée.<br>
    <b>Objectif :</b> Maximiser votre ROI grâce à l'Intelligence Artificielle.
    </div>
    """, unsafe_allow_html=True)
    
    # --- MODIFICATION ICI : MASTER 2 EN BLEU (st.info) ---
    k1, k2 = st.columns(2)
    with k1: st.info("💡 **Profil Hybride**\n\nBusiness + Tech")
    with k2: st.info("🎓 **Master 2**\n\nIESEG School of Management") 

with c2:
    if lottie_marketing:
        st_lottie(lottie_marketing, height=350)

# --- KPI BANNER ---
st.markdown("<br>", unsafe_allow_html=True)
cols = st.columns(4)
metrics = [
    ("30 k€", "CA Généré", "💰"),
    ("+30 %", "Trafic SEO", "🚀"),
    ("10k", "Visites/Mois", "👀"),
    ("Bilingue", "FR / EN / ES", "🌍")
]

for col, (val, label, icon) in zip(cols, metrics):
    with col:
        st.markdown(f"""
        <div class="glass-card" style="text-align:center; padding: 15px;">
            <div style="font-size: 2rem;">{icon}</div>
            <div style="font-size: 1.8rem; font-weight: 800; color: #FF416C !important;">{val}</div>
            <div style="font-size: 0.8rem; color: #888; text-transform: uppercase;">{label}</div>
        </div>
        """, unsafe_allow_html=True)

# --- EXPÉRIENCES (TIMELINE) ---
st.markdown('<div class="section-title">⚡ Parcours & Impact</div>', unsafe_allow_html=True)

c_exp1, c_exp2 = st.columns([1, 1.5])

with c_exp1:
    st.markdown("""
    <div style="background: white; padding: 20px; border-radius: 15px; box-shadow: 0 4px 15px rgba(0,0,0,0.05); border-top: 5px solid #FF416C;">
        <h4>💡 Ma Philosophie</h4>
        <p style="color: #666;">Le marketing moderne ne se fait plus au "feeling".</p>
        <p style="color: #666;">Je combine :</p>
        <ul>
            <li><b>L'analyse</b> (pour comprendre)</li>
            <li><b>La créativité</b> (pour engager)</li>
            <li><b>L'automatisation</b> (pour scaler)</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

with c_exp2:
    st.markdown("""
    <div class="timeline-item">
        <div class="timeline-dot"></div>
        <div class="timeline-date">2024 • Optima Media</div>
        <h4 style="margin: 5px 0;">SEO Manager & Data Analyst</h4>
        <p style="color: #555;">Pilotage de la stratégie digitale secteur bancaire.</p>
        <span class="badge badge-marketing">SEO</span> <span class="badge badge-data">Python</span> <span class="badge badge-marketing">+30% Trafic</span>
    </div>
    
    <div class="timeline-item">
        <div class="timeline-dot"></div>
        <div class="timeline-date">2021-2023 • Lafrip2luxe</div>
        <h4 style="margin: 5px 0;">Fondateur E-commerce</h4>
        <p style="color: #555;">Création d'une marque de A à Z (30k€ CA).</p>
        <span class="badge badge-marketing">Growth</span> <span class="badge badge-marketing">Social Ads</span> <span class="badge badge-soft">Leadership</span>
    </div>
    """, unsafe_allow_html=True)

# --- PROJETS ---
st.markdown('<div class="section-title">💻 Labo Marketing & IA</div>', unsafe_allow_html=True)
st.caption("👇 Cliquez sur les cartes pour voir le code sur GitHub.")

col_p1, col_p2, col_p3 = st.columns(3)

def project_card(title, icon, desc, tags, link):
    return f"""
    <a href="{link}" target="_blank" style="text-decoration: none; color: inherit;">
        <div class="glass-card">
            <div style="font-size: 2.5rem; margin-bottom: 10px;">{icon}</div>
            <h4 style="color: #333; margin: 0;">{title}</h4>
            <p style="font-size: 0.9rem; color: #666; margin-top: 10px;">{desc}</p>
            <div style="margin-top: 15px;">{tags}</div>
        </div>
    </a>
    """
# Lien générique
linkong = "https://github.com/lennyfraise18/ONG-Predictive-Analytics-Project"
linksql= "https://github.com/lennyfraise18/SQL-Project"
linkdecatlhon = "https://github.com/lennyfraise18/Decathlon-Data-Marketing-Analysis"

with col_p1:
    tags = '<span class="badge badge-marketing">Stratégie</span> <span class="badge badge-marketing">Predictive Analytics</span>'
    st.markdown(project_card("Innovation ONG", "🌱", "Analyse prédictive & optimisation collecte de dons.", tags, linkong), unsafe_allow_html=True)

# --- CORRECTION ICI : Ajout du titre et de l'icône manquants ---
with col_p2:
    tags = '<span class="badge badge-data">Analyse des ventes</span> <span class="badge badge-data">SQL</span>'
    st.markdown(project_card(
        "Reporting Pharma", 
        "💊", 
        "Analyse des ventes pour piloter la performance, calcul de rentabilité, segmentation client.", 
        tags, 
        linksql
    ), unsafe_allow_html=True)

with col_p3:
    tags = '<span class="badge badge-data">Tableau</span> <span class="badge badge-marketing">Social Listening</span>'
    st.markdown(project_card("Decathlon x Sissy Mua", "👟", "Analyse de rentabilité ROI et best sellers.", tags, linkdecatlhon), unsafe_allow_html=True)

# --- CONTACT SECTION ---
st.markdown("---")
st.markdown('<div class="section-title">📬 Travaillons ensemble !</div>', unsafe_allow_html=True)

c_contact_text, c_contact_anim = st.columns([1.5, 1])

with c_contact_text:
    st.markdown("""
    <div style="background: white; padding: 30px; border-radius: 15px; border-left: 5px solid #FF416C; box-shadow: 0 5px 15px rgba(0,0,0,0.05);">
        <h3>Un projet ou une opportunité ?</h3>
        <p style="font-size: 1.1rem; color: #555;">
            Je suis actuellement à la recherche d'un <b>Stage en Marketing IA</b> pour Juin 2026.
            <br>Discutons de vos enjeux Data & Growth autour d'un café (ou d'une visio).
        </p>
        <br>
        <div style="display: flex; gap: 15px;">
            <a href="mailto:lenny.fraise@gmail.com" style="background: linear-gradient(90deg, #FF4B2B, #FF416C); color: white; padding: 12px 25px; border-radius: 30px; text-decoration: none; font-weight: bold; box-shadow: 0 4px 10px rgba(255, 65, 108, 0.3);">
                📧 Envoyer un email
            </a>
            <a href="https://linkedin.com/in/lenny-fraise" target="_blank" style="background: #0077B5; color: white; padding: 12px 25px; border-radius: 30px; text-decoration: none; font-weight: bold; box-shadow: 0 4px 10px rgba(0, 119, 181, 0.3);">
                🔗 LinkedIn
            </a>
        </div>
    </div>
    """, unsafe_allow_html=True)

with c_contact_anim:
    if lottie_contact:
        st_lottie(lottie_contact, height=300)

# --- CORRECTION ICI : Correction de "Trc" en "True" ---
st.markdown("<br><center style='color:#bbb; font-size:0.8rem;'>© 2026 Lenny Fraise • Design Streamlit</center>", unsafe_allow_html=True)