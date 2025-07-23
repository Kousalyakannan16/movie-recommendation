
import streamlit as st
from recommender import load_data, build_recommender, get_recommendations

st.set_page_config(page_title="🎬 Movie Recommender", layout="centered")
st.title("🎬 Smart Movie Recommender")
st.markdown("Discover your next favorite movie based on what you already love!")


df = load_data()
sim_matrix = build_recommender(df)
movie_list = df['title'].tolist()


choice = st.selectbox("🎥 Pick a movie you like:", movie_list)

if st.button("🎁 Recommend"):
    results = get_recommendations(choice, df, sim_matrix)
    st.subheader("💡 Top Recommendations:")
    for _, row in results.iterrows():
        st.markdown(f"**🎞 {row['title']}** — *{row['genre']}*")
        st.markdown(f"> {row['description']}")
        st.markdown("---")
