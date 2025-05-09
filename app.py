import streamlit as st
import pandas as pd
from PIL import Image
import os

# -------------------------------
# Page Configuration
# -------------------------------
st.set_page_config(page_title="Netflix Data Analysis", layout="wide")

# -------------------------------
# Load Data
# -------------------------------
@st.cache_data
def load_data():
    df = pd.read_csv("netflix_titles.csv")
    return df

df = load_data()

# -------------------------------
# Header Section
# -------------------------------
st.title("🎬 Netflix Data Analysis")
st.markdown("""
This interactive dashboard provides deep insights into Netflix's content distribution, top genres, countries, and more.
""")

# -------------------------------
# Dataset Overview
# -------------------------------
with st.expander("📊 Dataset Overview"):
    st.write("Shape of the dataset:", df.shape)
    st.dataframe(df.head(10))

# -------------------------------
# Load and Display Plots
# -------------------------------
st.markdown("## 📈 Visual Insights")

plot_files = {
    "Movies vs TV Shows": "Movies_vs_TV_Shows.png",
    "Top 10 Producing Countries": "Top_10_Producing_Countries.png",
    "Titles Added Over Years": "Titles_Added_Over_Years.png",
    "Top 10 Genres": "Top_10_Genres.png",
    "Content by Rating": "Content_by_Rating.png",
    "Release Years Over Time": "Release_Years_Over_Time.png",
    "Top 10 Directors": "Top_10_Directors.png",
    "Top 10 Actors": "Top_10_Actors.png",
    "Ratings by Content Type": "Ratings_by_Content_Type.png",
    "Release vs Added Year": "Release_vs_Added_Year.png",
    "Monthly Content Additions": "Monthly_Content_Additions.png",
}

for title, file in plot_files.items():
    with st.expander(f"📌 {title}"):
        image = Image.open(os.path.join("plots", file))
        st.image(image, use_column_width=True, caption=title)

# -------------------------------
# Footer
# -------------------------------
st.markdown("---")
st.markdown("""
🔗 **Connect with Me**  
📩 Email: [charankumar.career@gmail.com](mailto:charankumar.career@gmail.com)  
🔗 LinkedIn: [linkedin.com/in/charankumar-g](https://linkedin.com/in/charankumar-g)
""")
