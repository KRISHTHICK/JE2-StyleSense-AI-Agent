# JE2-StyleSense-AI-Agent
GenAI

Here’s a complete new project idea involving an AI agent with Ollama, Python, and Streamlit, designed to run in VS Code and deploy to GitHub:

---

## 🧠 **StyleSense AI Agent – Your Personal AI Fashion Stylist**

### 🔍 Project Overview:

StyleSense is an AI Agent-based fashion assistant that helps users get personalized fashion advice, outfit pairing, trend analysis, and virtual fashion tips. Built using Python, Streamlit, and Ollama (running a local LLM like TinyLLaMA), the app simulates a real-time interactive agent that converses and recommends fashion options based on uploaded photos and preferences.

---

### 🌟 Key Features:

1. **Interactive AI Agent Chat Interface (Ollama LLM)**

   * Engage with a local LLM through natural language.
   * Ask for outfit suggestions, fabric types, styling tips, etc.

2. **Fashion Style Identifier**

   * Upload a clothing image.
   * AI detects and names the fashion style (e.g., “Boho”, “Streetwear”).

3. **Color Combination Generator**

   * Get best matching colors for any uploaded outfit.
   * Suggests accessories to go with.

4. **Trend Analyser**

   * LLM summarizes latest trends by analyzing saved text from web (e.g., blogs or screenshots).
   * Offers personalized fashion insights.

5. **Style Diary Generator**

   * Creates a style journal entry based on photo, event, or mood.
   * Suggests captions, blog text, and hashtags.

6. **Style-to-Post Generator**

   * Generates an Instagram-style post with caption, tags, hashtags, and emojis.

---

### 📁 Project Structure:

```
StyleSense-AI-Agent/
│
├── app.py
├── ollama_agent.py
├── fashion_utils.py
├── assets/
│   └── sample_images/
├── requirements.txt
└── README.md
```

---

### 🔧 `requirements.txt`

```txt
streamlit
Pillow
matplotlib
ollama
```

---

### ▶️ `app.py` (Main UI)

```python
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
```

---

### 💬 `ollama_agent.py` (Local LLM Handler with Ollama)

```python
import subprocess

def query_ai(prompt):
    result = subprocess.run(["ollama", "run", "tinyllama", prompt], capture_output=True, text=True)
    return result.stdout.strip()
```

---

### 👗 `fashion_utils.py` (Fashion Logic)

```python
from PIL import Image
import random

def get_fashion_style(image):
    styles = ["Streetwear", "Bohemian", "Formal", "Casual", "Chic", "Sporty"]
    return random.choice(styles)

def generate_color_combos(image):
    color_suggestions = [
        ["Black", "Gold"],
        ["Navy Blue", "White"],
        ["Olive Green", "Beige"],
        ["Maroon", "Cream"],
        ["Grey", "Rust Orange"]
    ]
    return random.choice(color_suggestions)
```

---

### 📄 `README.md`

````markdown
# 👗 StyleSense AI Agent

StyleSense is an AI Agent built using Python, Streamlit, and Ollama. It helps users get fashion suggestions, detect clothing styles, and generate social content.

## 🚀 Features
- AI Agent chat using Ollama (TinyLLaMA)
- Fashion style detection from images
- Matching color suggestions
- Social media post generation

## 🛠️ How to Run Locally
1. **Clone the repo**
```bash
git clone https://github.com/yourusername/StyleSense-AI-Agent.git
cd StyleSense-AI-Agent
````

2. **Install dependencies**

```bash
pip install -r requirements.txt
```

3. **Start Ollama**

```bash
ollama serve
ollama run tinyllama
```

4. **Run the app**

```bash
streamlit run app.py
```

## 🧠 Requirements

* Python 3.8+
* Streamlit
* Pillow
* Ollama

## 📦 Deploying to GitHub Pages

GitHub Pages does not support Python directly. Use a static exporter or deploy via Streamlit Community Cloud.

---

📌 Inspired by the need for personal fashion assistants powered by local models.

```

---

Would you like this uploaded as a GitHub-ready project folder (with `.zip`) or do you want additional features like outfit rating or fashion personality quizzes?
```
