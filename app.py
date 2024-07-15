import streamlit as st
import pickle
import pandas as pd
import requests


def fetch_poster(poster):
    response = requests.get('https://www.omdbapi.com/?apikey=c9eb1bb2&t=' + poster)
    data = response.json()
    return data['Poster']


def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    recommended_movies = []
    recommended_movies_poster = []
    for i in movies_list:
        # fetch poster of the movie
        recommended_movies.append(movies.iloc[i[0]].title)
        # fetching poster from API
        recommended_movies_poster.append(fetch_poster(movies.iloc[i[0]].title))
    return recommended_movies, recommended_movies_poster


movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarity.pkl', 'rb'))

st.logo(image='https://static.vecteezy.com/system/resources/thumbnails/012/657/549/small/illustration-negative-film'
              '-reel-roll-tapes-for-movie-cinema-video-logo-vector.jpg')
st.title('Movies Recommendation System')

selected_movie_name = st.selectbox('Displays 5 similar movies from your selected one.',
                                   movies['title'].values)

if st.button('Recommend'):
    name, poster = recommend(selected_movie_name)
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.image(poster[0])
        st.text(name[0])

    with col2:
        st.image(poster[1])
        st.text(name[1])

    with col3:
        st.image(poster[2])
        st.text(name[2])

    with col4:
        st.image(poster[3])
        st.text(name[3])

    with col5:
        st.image(poster[4])
        st.text(name[4])
