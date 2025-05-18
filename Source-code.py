import matplotlib.pyplot as plt
import seaborn as sns

# Basic Info
print("Movies DataFrame Info:")
print(movies.info())
print("\nRatings DataFrame Info:")
print(ratings.info())

# First few records
print("\nMovies Head:\n", movies.head())
print("\nRatings Head:\n", ratings.head())

# Number of unique users and movies
print("\nUnique Users:", ratings['userId'].nunique())
print("Unique Movies Rated:", ratings['movieId'].nunique())
print("Total Ratings:", ratings.shape[0])

# Most rated movies
top_movies = ratings['movieId'].value_counts().head(5).reset_index()
top_movies.columns = ['movieId', 'rating_count']
top_movies = top_movies.merge(movies, on='movieId')
print("\nTop Rated Movies:\n", top_movies[['title', 'rating_count']])

# Distribution of ratings
plt.figure(figsize=(6, 4))
sns.countplot(x='rating', data=ratings)
plt.title('Rating Distribution')
plt.xlabel('Rating')
plt.ylabel('Count')
plt.show()

# Average rating per movie
avg_rating = ratings.groupby('movieId')['rating'].mean().reset_index()
avg_rating = avg_rating.merge(movies, on='movieId')
avg_rating = avg_rating.sort_values(by='rating', ascending=False)
print("\nTop Movies by Average Rating:\n", avg_rating[['title', 'rating']].head(5))

# Ratings per user
user_activity = ratings.groupby('userId')['rating'].count().reset_index(name='num_ratings')
print("\nUser Activity:\n", user_activity)

# Ratings per genre (if genres are split)
genre_count = movies['genres'].str.get_dummies(sep='|').sum().sort_values(ascending=False)
print("\nNumber of Movies per Genre:\n", genre_count)

# Plot genre distribution
plt.figure(figsize=(10, 5))
genre_count.plot(kind='bar')
plt.title('Number of Movies per Genre')
plt.xlabel('Genre')
plt.ylabel('Number of Movies')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
