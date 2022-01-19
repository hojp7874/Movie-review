from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.parse import quote


def get_movie_data(movie):
    movieNm = quote(movie['movieNm'])
    response = urlopen(f'https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query={movieNm}+{quote("영화")}')
    soup = BeautifulSoup(response, 'html.parser')
    return soup