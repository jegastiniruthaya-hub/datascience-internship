import os
import re
from html.parser import HTMLParser
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

import streamlit as st

# =====================================
# PAGE CONFIGURATION
# =====================================

st.set_page_config(
    page_title="AI Knowledge Assistant",
    page_icon="🤖",
    layout="wide"
)

# =====================================
# KNOWLEDGE BASE FOLDER
# =====================================

folder = "knowledge_base"


class TextExtractor(HTMLParser):
    def __init__(self):
        super().__init__()
        self.parts = []

    def handle_data(self, data):
        cleaned = data.strip()
        if cleaned:
            self.parts.append(cleaned)


def fetch_webpage_text(url):
    request = Request(url, headers={"User-Agent": "Mozilla/5.0"})

    with urlopen(request, timeout=10) as response:
        html = response.read().decode("utf-8", errors="ignore")

    parser = TextExtractor()
    parser.feed(html)
    text = " ".join(parser.parts)
    return re.sub(r"\s+", " ", text).strip()


def answer_from_text(question_text, source_text, max_sentences=3):
    stop_words = {
        "what", "when", "where", "which", "who", "why", "how",
        "the", "and", "for", "with", "from", "about", "this",
        "that", "are", "was", "were", "can", "does", "do"
    }
    question_words = {
        word for word in re.findall(r"[a-zA-Z]{3,}", question_text.lower())
        if word not in stop_words
    }

    sentences = re.split(r"(?<=[.!?])\s+", source_text)
    ranked_sentences = []

    for sentence in sentences:
        words = set(re.findall(r"[a-zA-Z]{3,}", sentence.lower()))
        score = len(words & question_words)
        if score:
            ranked_sentences.append((score, sentence.strip()))

    if ranked_sentences:
        ranked_sentences.sort(key=lambda item: item[0], reverse=True)
        return " ".join(sentence for _, sentence in ranked_sentences[:max_sentences])

    return source_text[:700] + ("..." if len(source_text) > 700 else "")

# =====================================
# SIDEBAR
# =====================================

with st.sidebar:
    st.title("📚 Project Information")
    st.write("Dynamic Knowledge Expansion Chatbot")
    st.write("Internship Project")
    st.write("Built using Python & Streamlit")

    st.markdown("---")
    st.subheader("🌐 External Website")
    web_url = st.text_input(
        "Website URL",
        placeholder="https://en.wikipedia.org/wiki/Artificial_intelligence"
    )
    load_web = st.button("Load website content")

    if "web_text" not in st.session_state:
        st.session_state.web_text = ""
        st.session_state.web_source = ""

    if load_web:
        if web_url.strip():
            try:
                st.session_state.web_text = fetch_webpage_text(web_url.strip())
                st.session_state.web_source = web_url.strip()
                st.success("Website content loaded.")
            except (HTTPError, TimeoutError, URLError, ValueError) as error:
                st.session_state.web_text = ""
                st.session_state.web_source = ""
                st.error(f"Could not load website content: {error}")
        else:
            st.warning("Enter a website URL first.")

# =====================================
# MAIN TITLE
# =====================================

st.title("🤖 AI Knowledge Assistant")
st.write("Ask questions from the knowledge base.")

# =====================================
# LOAD TOPICS
# =====================================

topics = []

if os.path.exists(folder):
    for file in os.listdir(folder):
        if file.endswith(".txt"):
            topics.append(file.replace(".txt", ""))

# =====================================
# DISPLAY INFO
# =====================================

st.info(f"Knowledge Base Loaded: {len(topics)} files")

if st.session_state.web_text:
    st.info(f"External website loaded: {st.session_state.web_source}")

st.subheader("📖 Available Topics")

if topics:
    st.write(", ".join(topics))
else:
    st.warning("No knowledge files found.")

# =====================================
# QUESTION INPUT
# =====================================

question = st.text_input("Ask a question:")

# =====================================
# SEARCH ANSWER
# =====================================

if question:

    q = question.lower()

    answer_found = False

    for file in os.listdir(folder):

        if file.endswith(".txt"):

            topic = file.replace(".txt", "").lower()

            if topic in q:

                with open(
                    os.path.join(folder, file),
                    "r",
                    encoding="utf-8"
                ) as f:

                    content = f.read()

                st.subheader("✅ Answer")

                st.success(content)

                st.caption(f"Source: {file}")

                answer_found = True

                break

    if not answer_found:
        if st.session_state.web_text:
            st.subheader("✅ Answer from Website")
            st.success(answer_from_text(question, st.session_state.web_text))
            st.caption(f"Source: {st.session_state.web_source}")
            answer_found = True
        else:
            st.error(
                "❌ Sorry, I couldn't find information about that topic."
            )

            st.write("Try asking about:")

            for topic in topics:
                st.write(f"• {topic}")

# =====================================
# FOOTER
# =====================================

st.markdown("---")
st.write("Created by Danu 🚀")
