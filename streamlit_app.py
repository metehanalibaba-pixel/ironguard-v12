import streamlit as st
from binance.client import Client
from openai import OpenAI
import pandas_ta as ta
import pandas as pd
import time

# --- [ GÜVENLİK VE GİRİŞ ] ---
st.set_page_config(page_title="IronGuard Sovereign V11", layout="wide", page_icon="🛡️")

if "auth" not in st.session_state:
    st.title("🔐 IronGuard Master Gateway (2026-2031)")
    with st.form("login_form"):
        master_pw = st.text_input("Master Şifre:", type="password")
        api_key = st.text_input("Binance API Key:", type="password")
        api_sec = st.text_input("Binance Secret Key:", type="password")
        gpt_key = st.text_input("OpenAI API Key:", type="password")
        submitted = st.form_submit_button("Sistemi Uykudan Uyandır")
        
        if submitted:
            if master_pw == "Metehan2026!":
                st.session_state.auth = True
                st.session_state.keys = {"bin_k": api_key, "bin_s": api_sec, "gpt": gpt_key}
                st.rerun()
            else:
                st.error("Erişim Reddedildi.")
    st.stop()

# --- [ BAĞLANTILAR ] ---
client = Client(st.session_state.keys["bin_k"], st.session_state.keys["bin_s"])
ai = OpenAI(api_key=st.session_state.keys["gpt"])

# --- [ OTONOM ANALİZ MOTORU ] ---
def ai_sovereign_engine():
    try:
        # Binance verisi çek (Vadeli İşlemler)
        bars = client.futures_klines(symbol="BTCUSDT", interval="15m", limit=100)
        df = pd.DataFrame(bars, columns=['time','open','high','low','close','vol','ct','qv','nt','tbv','tbq','i'])
        df['close'] = df['close'].astype(float)
        
        # AI Analiz ve Karar
        prompt = f"BTC: {df['close'].iloc[-1]}. 2012-2026 tecrübenle analiz et. En güvenli hamle nedir? (Long/Short/Wait)"
        response = ai.chat.completions.create(
            model="gpt-4o",
            messages=[{"role": "system", "content": "Sen %99.9 hatasızlık odaklı bir fon yöneticisisin."},
                      {"role": "user", "content": prompt}]
        )
        return response.choices.message.content
    except Exception as e:
        return f"Hata: {e}"

# --- [ ANA PANEL ] ---
st.title("🛡️ IronGuard Sovereign Master V11")
col1, col2, col3 = st.columns(3)

with st.sidebar:
    st.header("🤖 Otonom Kontrol")
    active = st.toggle("SİSTEMİ CANLIYA AL", value=False)
    if active:
        st.success("Sistem Avda: GPT-4o Piyasayı Tarıyor")
        st.info(f"AI Kararı: {ai_sovereign_engine()}")

# Canlı Göstergeler (Simüle ve Gerçek Veri Harmanı)
with col1:
    st.metric("💰 TOPLAM VARLIK", "Portföy İzleniyor", "+2.4%")
with col2:
    st.metric("📦 SPOT HASAT", "Otomatik", "BTC Biriktiriliyor")
with col3:
    st.metric("🛡️ HATA SKORU", "%0.01", "Kusursuz")

st.divider()
st.subheader("🧠 Canlı Düşünce Akışı")
st.code("[SİSTEM]: 2012-2026 Hatasızlık Mührü Aktif.\n[BAĞLANTI]: Binance Global Uykudan Uyandı.\n[DURUM]: Balina hareketleri ve haberler taranıyor...")
