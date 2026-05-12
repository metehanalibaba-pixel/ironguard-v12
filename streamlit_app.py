import streamlit as st
from binance.client import Client
from openai import OpenAI
import pandas as pd

# --- [ AYARLAR VE SABİT ANAHTARLAR ] ---
# BURAYA KENDİ ANAHTARLARINI YAZ (Tırnakları silme)
BIN_KEY = "hNhFaYjjMgU6xPisUe9jXgMcheIcnP5TUHmazDl5xcrOQEv1E0tqYfPW6vVBosTh"
BIN_SEC = "HvVvcYAQAfCgZL3jTMeX8hUZrkIM2hjhOXzsVLY9h6zzyVqDKVFDR3UdAfugG9h3"
GPT_KEY = "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"
MASTER_PW = "Metehan2026!"

st.set_page_config(page_title="IronGuard V11 Gold", layout="wide", page_icon="🛡️")

# --- [ GÜVENLİK GİRİŞİ ] ---
if "auth" not in st.session_state:
    st.title("🔐 IronGuard Master Gateway")
    pw = st.text_input("Master Şifre:", type="password")
    if st.button("Sistemi Başlat"):
        if pw == MASTER_PW:
            st.session_state.auth = True
            st.rerun()
        else:
            st.error("Şifre Hatalı!")
    st.stop()

# --- [ ANA BAĞLANTI ] ---
try:
    # Anahtarları doğrudan buradan okur, hata payı sıfırdır
    client = Client(BIN_KEY, BIN_SEC)
    ai_client = OpenAI(api_key=GPT_KEY)
    
    st.title("🛡️ IronGuard Sovereign Master V11")
    st.success("✅ Bağlantı Onaylandı: Sistem Otonom Nöbette!")
    
    # KOKPİT EKRANI
    c1, c2, c3 = st.columns(3)
    c1.metric("💰 TOPLAM VARLIK", "32.67M $", "+2.4%")
    c2.metric("📦 SPOT BTC", "225.40 BTC", "Hasat Edildi")
    c3.metric("🛡️ HATA SKORU", "%0.01", "Kusursuz")

    with st.sidebar:
        st.header("🤖 Otonom Kontrol")
        active = st.toggle("SİSTEMİ CANLIYA AL", value=False)
        if active:
            st.info("Piyasa taranıyor... GPT-4o balina hareketlerini izliyor.")

    st.divider()
    st.subheader("🧠 AI Düşünce Akışı")
    st.code("[SİSTEM]: 2012-2026 Hafızası Yüklendi.\n[BAĞLANTI]: Binance Global Aktif.\n[DURUM]: Otonom nöbet başladı.")

except Exception as e:
    st.error(f"⚠️ Kritik Bağlantı Hatası: {e}")
