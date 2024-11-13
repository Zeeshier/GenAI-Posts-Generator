import streamlit as st
from fewshot import FewShot
from postgenerate import generate_post

length_options = ["Short", "Medium", "Long"]

creators = {
    "Hisham Sarwar": "Data/hisham_sarwar_processed.json",
    "Irfan Malik": "Data/irfan_malik_processed.json",
    "Usman Asif": "Data/usman_asif_processed.json"
}


def main():
   
    st.set_page_config(page_title="LinkedIn Post Generator", page_icon="🔗")


    st.sidebar.title("👥 Select Creator")
    st.sidebar.markdown("""
    <p style='text-align: center;'><a href="https://www.linkedin.com/in/Zeeshier" target="_blank">
    <img src="https://static.vecteezy.com/system/resources/previews/023/986/926/large_2x/linkedin-logo-linkedin-logo-transparent-linkedin-icon-transparent-free-free-png.png" width="40" height="40" alt="LinkedIn Logo"></a></p>
    """, unsafe_allow_html=True)
    
    selected_creator = st.sidebar.selectbox("Choose a creator:", options=creators.keys())
    

    fs = FewShot([creators[selected_creator]])
    tags = fs.get_tags()
    
    st.markdown("""
    <h2 style='text-align: center; color: #0072B1;'>LinkedIn Post Generator ✨</h2>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        selected_tag = st.selectbox("🎯 Topic", options=tags)

    with col2:
        selected_length = st.selectbox("📏 Length", options=length_options)

    if st.button("🚀 Generate Post"):
        post = generate_post(selected_length, selected_tag)
        st.markdown("<div style='background-color: #f0f8ff; padding: 10px; border-radius: 10px;'>"
                    f"<p style='color: #333333;'>{post}</p>"
                    "</div>", unsafe_allow_html=True)


if __name__ == "__main__":
    main()
