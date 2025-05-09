# netflix_analysis.py

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Set seaborn style
sns.set_style("whitegrid")

# Create plots folder
os.makedirs("plots", exist_ok=True)

# Load dataset
df = pd.read_csv('netflix_titles.csv')

# Handle missing values
df['director'].fillna('unknown', inplace=True)
df['cast'].fillna('Not Available', inplace=True)
df['country'].fillna('Not Specified', inplace=True)
df['date_added'].fillna('Unknown', inplace=True)
df['rating'].fillna('Not Rated', inplace=True)
df['duration'].fillna('Not Specified', inplace=True)

# Date processing
df['date_added'] = pd.to_datetime(df['date_added'], errors='coerce')
df['year_added'] = df['date_added'].dt.year
df['month_added'] = df['date_added'].dt.month

# Duration processing
df['duration_minutes'] = None
df['duration_seasons'] = None
df.loc[df['type'] == 'Movie', 'duration_minutes'] = df['duration'].str.extract('(\d+)').astype(float)
df.loc[df['type'] == 'TV Show', 'duration_seasons'] = df['duration'].str.extract('(\d+)').astype(float)

# Visualizations

# A) Movies vs TV Shows
plt.figure(figsize=(6,4))
type_counts = df['type'].value_counts()
sns.barplot(x=type_counts.index, y=type_counts.values, palette='Paired')
plt.title("Movies vs TV Shows")
plt.tight_layout()
plt.savefig("plots/Movies_vs_TV_Shows.png", dpi=300)
plt.show()

# B) Top 10 Countries
plt.figure(figsize=(8,5))
top_countries = df['country'].value_counts().head(10)
sns.barplot(y=top_countries.index, x=top_countries.values, palette='Spectral')
plt.title("Top 10 Producing Countries")
plt.tight_layout()
plt.savefig("plots/Top_10_Producing_Countries.png", dpi=300)
plt.show()

# C) Yearly Additions
plt.figure(figsize=(10,5))
yearly = df['year_added'].value_counts().sort_index()
sns.lineplot(x=yearly.index, y=yearly.values, marker='o')
plt.title("Titles Added Over Years")
plt.tight_layout()
plt.savefig("plots/Titles_Added_Over_Years.png", dpi=300)
plt.show()

# D) Top 10 Genres
plt.figure(figsize=(8,5))
genres = df['listed_in'].str.split(',').explode().str.strip()
top_genres = genres.value_counts().head(10)
sns.barplot(y=top_genres.index, x=top_genres.values, palette='cubehelix')
plt.title("Top 10 Genres")
plt.tight_layout()
plt.savefig("plots/Top_10_Genres.png", dpi=300)
plt.show()

# E) Ratings Distribution
plt.figure(figsize=(10,6))
rating_counts = df['rating'].value_counts()
sns.barplot(x=rating_counts.values, y=rating_counts.index, palette='coolwarm')
plt.title("Content by Rating")
plt.tight_layout()
plt.savefig("plots/Content_by_Rating.png", dpi=300)
plt.show()

# F) Release Year Trend
plt.figure(figsize=(12,6))
releases = df['release_year'].value_counts().sort_index()
sns.lineplot(x=releases.index, y=releases.values, marker='o', color='seagreen')
plt.title("Release Years Over Time")
plt.tight_layout()
plt.savefig("plots/Release_Years_Over_Time.png", dpi=300)
plt.show()

# G) Top 10 Directors
plt.figure(figsize=(10,5))
directors = df['director'].value_counts().head(10)
sns.barplot(x=directors.values, y=directors.index, palette='viridis')
plt.title("Top 10 Directors")
plt.tight_layout()
plt.savefig("plots/Top_10_Directors.png", dpi=300)
plt.show()

# H) Top 10 Actors
plt.figure(figsize=(10,6))
cast_series = df['cast'].replace("Not Available", pd.NA).dropna() \
                 .str.split(',').explode().str.strip()
top_actors = cast_series.value_counts().head(10)
sns.barplot(x=top_actors.values, y=top_actors.index, palette='magma')
plt.title("Top 10 Actors")
plt.tight_layout()
plt.savefig("plots/Top_10_Actors.png", dpi=300)
plt.show()

# K) Ratings by Type
plt.figure(figsize=(12,6))
sns.countplot(data=df, y='rating', hue='type',
              order=rating_counts.index, palette='Spectral')
plt.title("Ratings by Content Type")
plt.tight_layout()
plt.savefig("plots/Ratings_by_Content_Type.png", dpi=300)
plt.show()

# L) Release vs Added Year
sns.jointplot(data=df.dropna(subset=['year_added']),
              x='release_year', y='year_added',
              kind='hex', cmap='Oranges')
plt.suptitle("Release vs Added Year", y=1.02)
plt.tight_layout()
plt.savefig("plots/Release_vs_Added_Year.png", dpi=300)
plt.show()

# M) Monthly Additions
plt.figure(figsize=(10,6))
monthly = df['month_added'].value_counts().sort_index()
sns.lineplot(x=monthly.index, y=monthly.values, marker='o')
plt.title("Monthly Content Additions")
plt.tight_layout()
plt.savefig("plots/Monthly_Content_Additions.png", dpi=300)
plt.show()
