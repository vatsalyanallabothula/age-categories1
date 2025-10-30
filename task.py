import streamlit as st

st.set_page_config(layout="wide")
st.title("Wallpaper Gallery")

# --- Initialize session state ---
if "open_section" not in st.session_state:
    st.session_state.open_section = None

def toggle_section(name):
    """Only one info section open at a time."""
    if st.session_state.open_section == name:
        st.session_state.open_section = None
    else:
        st.session_state.open_section = name

# --- Create 3 equal columns for buttons ---
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("Info1"):
        toggle_section("Info1")

with col2:
    if st.button("Info2"):
        toggle_section("Info2")

with col3:
    if st.button("Info3"):
        toggle_section("Info3")

st.markdown("---")  # Divider for clarity

# --- Info1 Content ---
if st.session_state.open_section == "Info1":
    col1_1, col1_2 = st.columns(2)
    with col1_1:
        st.image("https://wallpaperaccess.com/full/1239388.jpg", use_container_width=True)
        st.caption("Sunrise")
    with col1_2:
        st.image("https://wallpapers.com/images/hd/2560x1440-fall-sunrise-on-landscape-0471974z9mnguo68.jpg", use_container_width=True)
        st.caption("Sunrise Landscape")

# --- Info2 Content ---
elif st.session_state.open_section == "Info2":
    col2_1, col2_2 = st.columns(2)
    with col2_1:
        st.image("https://images.wallpaperscraft.com/image/single/tulips_flowers_field_1369025_2560x1440.jpg", use_container_width=True)
        st.caption("Tulip Field")
    with col2_2:
        st.image("https://wallpapershome.com/images/pages/pic_h/10299.jpg", use_container_width=True)
        st.caption("Colorful Flower Field")

# --- Info3 Content ---
elif st.session_state.open_section == "Info3":
    col3_1, col3_2 = st.columns(2)
    with col3_1:
        st.image("https://images.wallpaperscraft.com/image/single/starry_sky_mountains_stars_119711_2560x1440.jpg", use_container_width=True)
        st.caption("Starry Sky Over Mountains")
    with col3_2:
        st.image("https://cdn.bhdw.net/im/the-nighttime-beauty-of-clouds-and-moonlight-reflected-in-the-clear-93223_w635.webp", use_container_width=True)
        st.caption("Moonlight Reflections")
