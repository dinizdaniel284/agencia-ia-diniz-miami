import streamlit as st
import time

# 1. Configuração de Estilo "Ultra-Luxury Dark"
st.set_page_config(
    page_title="Agencia IA Diniz | Luxury Concierge", 
    page_icon="💎", 
    layout="centered"
)

# CSS Customizado para forçar o visual premium
st.markdown("""
    <style>
    .stApp {
        background: radial-gradient(circle, #1a1a1a 0%, #050505 100%);
    }
    .gold-text {
        color: #d4af37 !important;
        font-family: 'Playfair Display', serif;
        font-weight: bold;
    }
    .stButton>button {
        background: linear-gradient(135deg, #d4af37 0%, #996515 100%);
        color: black !important;
        font-weight: bold;
        border-radius: 50px;
        border: none;
        padding: 0.5rem 2rem;
        transition: all 0.3s;
    }
    .stButton>button:hover {
        transform: scale(1.05);
        box-shadow: 0 10px 20px rgba(212, 175, 55, 0.3);
    }
    div[data-testimonial="chat"] {
        border-left: 2px solid #d4af37;
    }
    </style>
    """, unsafe_allow_html=True)

# 2. Header de Impacto
st.markdown("<h1 class='gold-text'>AGENCIA IA DINIZ</h1>", unsafe_allow_html=True)
st.write("### Private AI Concierge | Marea PH602 Edition")
st.info("Status: Live Monitoring | Target: High-Net-Worth Leads")

# Sidebar com Métricas (Dica do Mentor: Falar de dinheiro)
with st.sidebar:
    st.markdown("<h2 class='gold-text'>Performance Metrics</h2>", unsafe_allow_html=True)
    st.metric(label="Response Time", value="1.8s", delta="-0.5s")
    st.metric(label="Lead Qualification Rate", value="94%")
    st.write("---")
    st.write("🛡️ **Vexus-AI Engine Active**")

# 3. Execução da Demo
if st.button("▶️ LAUNCH INTERACTIVE DEMO"):
    # Simulação do fluxo com foco em FECHAMENTO
    flow = [
        ("assistant", "🤖 AI Concierge", "System initialized for Ivan & Mike. Monitoring Marea PH602..."),
        ("user", "👤 High-End Lead", "I saw the listing for PH602. Does it have the private rooftop pool?"),
        ("assistant", "🤖 AI Concierge", "Absolutely. It features a private rooftop pool with 360° views of South Pointe. It's the crown jewel of the building."),
        ("user", "👤 High-End Lead", "Stunning. Is there a private showing available this week?"),
        ("assistant", "🤖 AI Concierge", "I can arrange an exclusive tour for you. Before we proceed, are you currently represented by an agent or inquiring privately?"),
        ("user", "👤 High-End Lead", "Inquiring privately. My budget is around $8M."),
        ("assistant", "🤖 AI Concierge", "Perfect. PH602 is listed at $7.7M. I'm notifying Ivan and Mike right now. Please leave your WhatsApp for the private access code.")
    ]

    for role, name, text in flow:
        with st.chat_message(role):
            st.markdown(f"**{name}**")
            placeholder = st.empty()
            full_text = ""
            # Efeito de digitação suave
            for char in text:
                full_text += char
                placeholder.markdown(full_text + "▌")
                time.sleep(0.02)
            placeholder.markdown(full_text)
        time.sleep(0.5)

    # Resultado Final (O que o corretor quer ver)
    st.markdown("---")
    st.success("✅ **LEAD QUALIFIED:** High-Priority prospect identified ($8M Budget).")
    
    col1, col2 = st.columns(2)
    with col1:
        st.write("📧 **Email Sent to Ivan & Mike**")
    with col2:
        st.write("📱 **Lead Data Synced with CRM**")
    
    st.balloons()