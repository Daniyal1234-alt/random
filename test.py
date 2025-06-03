import streamlit as st
from streamlit_lottie import st_lottie
import requests

st.set_page_config(page_title="Love U Muzzaqa 💖", page_icon="💘", layout="centered")

def load_lottie_url(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_hearts = load_lottie_url("https://lottie.host/ed6ce1e2-58ff-40dc-9d29-8e5d1e0466d2/yyMjv2a1yl.json")

st.markdown(
    """
    <style>
    .lottie-container {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        z-index: -1;
        opacity: 0.5;
    }
    .content-container {
        padding-top: 150px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown('<div class="lottie-container">', unsafe_allow_html=True)
st_lottie(lottie_hearts, speed=1, height=800, key="hearts")
st.markdown('</div>', unsafe_allow_html=True)
spotify_embed_code = """
<iframe style="border-radius:12px" 
src="https://open.spotify.com/embed/track/3uRSnYGEw2ZKwUjo2Hz5I1?utm_source=generator" 
width="100%" height="152" frameBorder="0" allowfullscreen="" 
allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture" 
loading="lazy"></iframe>
"""

st.markdown(spotify_embed_code, unsafe_allow_html=True)

st.markdown('<div class="content-container">', unsafe_allow_html=True)
st.title("💘 Love U Muzzaqa Twin💘")

st.markdown("""
### 💌

I just wanted to say — I love you so much, Muzzaqa.  
I know today wasn’t easy, and things might’ve felt a little heavy.  
But I hope this small thing brings a smile to your face, even if just for a second.  

You mean the world to me — and I’m always here for you.  \n
Rate karo kesi lagi? 
""")


st.markdown("---")
st.markdown("Made with 💖 by Daniyal")

