
import streamlit as st
from utils import extract_candles_from_image
from strategy_functions import detect_strategy, get_signal_from_strategy
from signal_reporter import generate_report

st.set_page_config(page_title="RihatX AI Signal Bot", layout="centered")

st.title("📈 RihatX AI Signal Bot")

uploaded_file = st.file_uploader("📥 Import your Quotex chart screenshot", type=["jpg", "jpeg", "png"])

if uploaded_file:
    st.image(uploaded_file, caption="🖼️ Uploaded Chart", use_column_width=True)

    if st.button("📡 Generate Signal"):
        with st.spinner("Analyzing your chart..."):
            candles = extract_candles_from_image(uploaded_file)

            if candles:
                strategy = detect_strategy(candles)
                if strategy:
                    signal = get_signal_from_strategy(strategy)
                    report = generate_report(signal, strategy)
                    st.success("✅ Signal Generated!")
                    st.markdown(report)
                else:
                    st.warning("❌ No matching strategy found.")
            else:
                st.error("⚠️ Could not extract candles from image.")
