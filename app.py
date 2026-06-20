import streamlit as st
import streamlit.components.v1 as components
import os

# Configure the Streamlit Page
st.set_page_config(
    page_title="SVC Failure Rate Analysis Dashboard",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS to hide Streamlit header, footer, MainMenu, and remove default container paddings
# This forces the embedded iframe to scale and look like a native standalone web app
st.markdown("""
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .block-container {
        padding-top: 0rem !important;
        padding-bottom: 0rem !important;
        padding-left: 0rem !important;
        padding-right: 0rem !important;
        max-width: 100% !important;
    }
    iframe {
        width: 100% !important;
        height: 95vh !important;
        border: none !important;
    }
    body {
        margin: 0;
        padding: 0;
        background-color: #0a0b10;
    }
    </style>
""", unsafe_allow_html=True)

# Load and embed the index.html dashboard
def main():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    html_file_path = os.path.join(current_dir, "index.html")
    
    if os.path.exists(html_file_path):
        with open(html_file_path, "r", encoding="utf-8") as f:
            html_content = f.read()
        
        # Set scrolling=True and height to fill viewport smoothly
        components.html(html_content, height=1000, scrolling=True)
    else:
        st.error("index.html 파일을 찾을 수 없습니다. 작업 디렉토리 내에 파일이 위치해 있는지 확인해 주세요.")

if __name__ == "__main__":
    main()
