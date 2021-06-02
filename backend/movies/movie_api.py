from .secret import kobis_key

class URLMaker_kobis:
    
    url = 'http://www.kobis.or.kr/kobisopenapi/webservice/rest'
    key = kobis_key()

    # key값 defalt 받기
    def __init__(self, key=key):
        self.key = key

    def get_url(self, category='boxoffice', feature='searchWeeklyBoxOfficeList'):
        return f'{self.url}/{category}/{feature}.json?key={self.key}'


class URLMaker_naver:
    
    url = 'https://openapi.naver.com/v1/search/movie.json'

    def get_url(self, query):
        return f'{self.url}?query={query}'