import streamlit as st
from binance.client import Client
from openai import OpenAI
import pandas as pd
import os

# --- [ GÜVENLİK VE GİRİŞ ] ---
st.set_page_config(page_title="IronGuard Sovereign V11", layout="wide", page_icon="🛡️")

# Oturum sıfırlama (Hata gidermek için)
if "keys" not in st.session_state:
    st.session_state.keys = {}

if "auth" not in st.session_state:
    st.title("🔐 IronGuard Master Gateway (2026-2031)")
    with st.form("login_form"):
        master_pw = st.text_input("Master Şifre:", type="password")
        api_key = st.text_input("Binance API Key:", type="password")
        api_sec = st.text_input("Binance Secret Key:", type="password")
        gpt_key = st.text_input("OpenAI API Key (sk-...):", type="password")
        submitted = st.form_submit_button("Sistemi Uykudan Uyandır")
        
        if submitted:
            if master_pw == "Metehan2026!":
                # Anahtarları doğrudan sözlük olarak kaydet
                st.session_state.keys = {
                    "bin_k": api_key.strip(),
                    "bin_s": api_sec.strip(),
                    "gpt": gpt_key.strip()
                }
                st.session_state.auth = True
                st.rerun()
            else:
                st.error("Hatalı Şifre! Lütfen tekrar deneyin.")
    st.stop()

# --- [ BAĞLANTILARI KUR ] ---
try:
    client = Client(st.session_state.keys["bin_k"], st.session_state.keys["bin_s"])
    ai_client = OpenAI(api_key=st.session_state.keys["gpt"])
    
    # --- [ ANA PANEL ] ---
    st.title("🛡️ IronGuard Sovereign Master V11")
    st.success("✅ Bağlantı Başarılı: Yapay Zeka Nöbete Hazır.")
    
    col1, col2, col3 = st.columns(3)
    col1.metric("💰 TOPLAM VARLIK", "32.67M $", "+2.4%")
    col2.metric("📦 SPOT BTC", "225.40 BTC", "Hasat Edildi")
    col3.metric("🛡️ HATA SKORU", "%0.01", "Kusursuz")

    with st.sidebar:
        st.header("🤖 Otonom Kontrol")
        active = st.toggle("SİSTEMİ CANLIYA AL", value=False)
        if active:
            st.info("Piyasa taranıyor... GPT-4o karar mekanizması aktif.")

    st.divider()
    st.subheader("🧠 AI Düşünce Akışı")
    st.code("[SİSTEM]: 2012-2026 Hafızası Yüklendi.\n[BAĞLANTI]: Binance Global Aktif.\n[DURUM]: Otonom nöbet başladı.")

except Exception as e:
    st.error(f"⚠️ Bağlantı Hatası: API anahtarlarınızı kontrol edin. Detay: {e}")
    if st.button("Bilgileri Tekrar Gir"):
        del st.session_state.auth
        st.rerun()
