import streamlit as st
from nltk.stem.isri import ISRIStemmer

# Initialize the ISRI stemmer
stemmer = ISRIStemmer()

st.set_page_config(page_title="Arabic Root Extractor", layout="centered")
st.title("🔎 Arabic Root Extractor (ISRIStemmer)")

# Input text
user_input = st.text_input("اكتب كلمة عربية:", "")

# Button to trigger stemming
if st.button("تحليل الجذر"):
    if user_input.strip():
        try:
            stemmed = stemmer.stem(user_input.strip())
            st.success(f"🔤 الجذر المحتمل: **{stemmed}**")
        except Exception as e:
            st.error(f"حدث خطأ أثناء التحليل: {e}")
    else:
        st.warning("⚠️ الرجاء إدخال كلمة أولاً.")
