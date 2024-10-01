import streamlit as st
import pickle
import pandas as pd
import requests
import json 

def fetch_poster(movie_id):
    print("a")
    # url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US"
    
    # api_key = "8265bd1679663a7ea12ac168da84d2e8"
    # base_url = "https://api.themoviedb.org/3/movie/{}"
    # url = base_url.format(movie_id) + "?api_key={api_key}&language=en-US"

    
    # response=requests.get(real)
    # url = "https://api.themoviedb.org/3/movie/{}?api_key=3493193e5cd269ef4545246ca20d959d".format(movie_id)
    # response = requests.get(url)
    # mov = str(movie_id)
    # response = requests.get("https://api.themoviedb.org/3/movie/65?api_key=3493193e5cd269ef4545246ca20d959d".format(movie_id))
    response = requests.get("https://api.themoviedb.org/3/movie/{}?api_key=3493193e5cd269ef4545246ca20d959d".format(movie_id))
    print(response)
    data = response.json()
    print("data")
    print(data)
    # view at online json viewer
    return "https://image.tmdb.org/t/p/w500/"+data['poster_path']

# since we have to pickle dump similarity matrix
similarity = pickle.load(open('similarity.pkl', 'rb'))
def recommend(movie):
    movie_index = movies_list[movies_list['title'] == movie].index[0] #get index of movie
    distances = similarity[movie_index] #get the row of movie to find max similarity with other movies
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x:x[1])[1:6] #top 5 similar movies
    recommended_movies = []
    recommended_movies_poster = []
    # for i in movie_list:
    #     movie_id = i[0]
    #     recommended_movies.append(movies_list['title'].iloc[i[0]])
    #     #fetch poster from API
    #     recommended_movies_poster.append(fetch_poster(movie_id))
    for i in movie_list:
        movie_id = movies_list.iloc[i[0]].movie_id
        recommended_movies.append(movies_list.iloc[i[0]].title)
        recommended_movies_poster.append(fetch_poster(movie_id))
    return recommended_movies, recommended_movies_poster


movies_list = pickle.load(open('movies.pkl', 'rb'))

st.title('Movie Recommender System')
selected_movie_name = st.selectbox('Enter movie name!', movies_list['title'].values)
if st.button('Recommend'):
    names, posters = recommend(selected_movie_name)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(names[0])
        st.image(posters[0])
    
    with col2:
        st.text(names[1])
        st.image(posters[1])

    with col3:
        st.text(names[2])
        st.image(posters[2])
    
    with col4:
        st.text(names[3])
        st.image(posters[3])

    with col5:
        st.text(names[4])
        st.image(posters[4])

    # for i in recommendations:
    #     st.write(i)


# streamlit run app.py