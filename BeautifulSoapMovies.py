import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt

def get_movie_data(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    movies = []
    for movie in soup.find_all('div', class_='lister-item mode-advanced'):
        title = movie.h3.a.text
        year = movie.h3.find('span', class_='lister-item-year').text
        imdb_rating = movie.find('div', class_='ratings-bar').strong.text
        movies.append({'Title': title, 'Year': year, 'IMDb Rating': float(imdb_rating)})
    return movies

url = 'https://www.imdb.com/search/title/?groups=top_1000&sort=user_rating'
movie_data = get_movie_data(url)

df = pd.DataFrame(movie_data)
df['Year'] = df['Year'].str.extract('(\d+)').astype(int)

grouped_data = df.groupby('Year').mean()

plt.plot(grouped_data.index, grouped_data['IMDb Rating'])
plt.xlabel('Year')
plt.ylabel('Average IMDb Rating')
plt.title('Average IMDb Rating of Top 1000 Movies by Year')
plt.show()
