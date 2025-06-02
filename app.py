import streamlit as st
from fashion_utils import get_fashion_style, generate_color_combos
from ollama_agent import query_ai

st.set_page_config(page_title="StyleSense AI", layout="wide")

st.title("👗 StyleSense AI Agent")
st.write("Your Personal Fashion Stylist")

with st.sidebar:
    st.header("Upload Outfit")
    uploaded_img = st.file_uploader("Choose an outfit image", type=["jpg", "png", "jpeg"])
    user_prompt = st.text_input("Ask anything about fashion 👠🧠", "")

if uploaded_img:
    st.image(uploaded_img, caption="Your Uploaded Outfit", use_column_width=True)

    st.subheader("🔍 Detected Fashion Style:")
    fashion_style = get_fashion_style(uploaded_img)
    st.success(fashion_style)

    st.subheader("🎨 Matching Color Suggestions")
    colors = generate_color_combos(uploaded_img)
    st.write(", ".join(colors))

if user_prompt:
    st.subheader("🤖 StyleSense Agent Response")
    response = query_ai(user_prompt)
    st.markdown(response)
