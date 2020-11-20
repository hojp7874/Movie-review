class URLMaker_kobis:
    
    url = 'http://www.kobis.or.kr/kobisopenapi/webservice/rest'
    key = '597eda625c46b844119d1b2633386262'

    # key값 defalt 받기
    def __init__(self, key=key):
        self.key = key


    def get_url(self, category='boxoffice', feature='searchWeeklyBoxOfficeList'):
        return f'{self.url}/{category}/{feature}.json?key={self.key}'


class URLMaker_naver:
    
    url = 'https://openapi.naver.com/v1/search/movie.json'

    def get_url(self, query):
        return f'{self.url}?query={query}'