# README

## 개요

> API 데이터를 시각화하여 원하는 영화 정보를 얻을 수 있는 사이트이다.
>
> 리뷰와 댓글 기능, 그리고 리뷰의 좋아요 기능을 활용하여 사용자 간의 원활한 소통이 가능하다.
>
> 자신과 다른 사용자들이 매긴 영화에 대한 평점과, 영화 관객 수 등을 종합 평가해 사용자에게 맞춤 영화 추천 서비스를 제공한다.
>
> Single page aplication와 부드러운 모션 이벤트를 이용해 높은 사용자 경험을 제공한다.
>
> 영화에 대한 필요한 모든 정보(개봉일, 장르, 줄거리, 감독, 등장인물, 영화 트레일러 등)를 제공하여 사용자 편리성을 확대하였다.
>
> 장르별 영화검색, 영화 제목과 배우 검색 등을 통해 편리한 영화 필터링 서비스를 제공한다.



### 팀 정보

![image-20201126213316912](README.assets/image-20201126213316912.png)

팀명: 늑대와 개미핥기

팀원: 홍진표, 박철완



### 업무 분담

| 홍진표                               | 박철완                                 |
| ------------------------------------ | -------------------------------------- |
| Back-end                             | Front-end                              |
| 데이터 크롤링                        | 메인 페이지 모델링                     |
| 데이터 모델링                        | Flip-card, 네비게이션 디자인 및 구현   |
| 영화, 영화인 검색 시스템 구현        | 카테고리별 검색 시스템 구현            |
| 영화 카드, Detail 디자인             | Back ground 디자인                     |
| 영화 평점, 리뷰, 좋아요 등 로직 처리 | 영화 평점, 리뷰, 좋아요 등 기능 활성화 |



### 목표 및 실제 서비스 구현 정도

대부분의 목표 수행 완료하였음.

구현하지 못한 부분

- 개인 프로필: 필요성이 저하되어 계획 취소
- 영화인 좋아요 기능: 시간 부족의 문제로 계획 취소
- 리뷰 댓글 기능: 리뷰가 영화 상세 페이지 밑에 달리면서 댓글의 기능을 동시에 수행하게 됐다. 댓글의 필요성이 저하되어 계획 취소



### 필수 기능 설명

- 로그인 기능

  ![image-20201126214910581](README.assets/image-20201126214910581.png)

  자신의 로그 기록을 남길 수 있는 기능. 추천 서비스 등 다양한 기능을 이용하기 위해 필요하다.

  

- 추천 서비스

  ![image-20201126215025361](README.assets/image-20201126215025361.png)

  사용자들의 데이터를 분석하여 리뷰가 많은 순서대로 추천 영화를 나타낸다.

  또한 관객 수가 많았던 영화들도 함께 종합 평가하여 출력한다.

  

- 영화, 영화인 검색 기능

  ![image-20201126215406023](README.assets/image-20201126215406023.png)

  텍스트를 입력하여 영화 제목과 배우의 이름을 자동완성하여 검색할 수 있다.

  검색 결과는 해당 단어를 포함한 영화와 해당 영화인이 참여한 영화를 출력한다.

  

- 카테고리 검색기능

  ![image-20201126215537157](README.assets/image-20201126215537157.png)

  해당 카테고리를 포함한 모든 영화들을 검색하는 시스템이다. 클릭 한 카테고리가 늘어나면, 해당 카테고리들을 포함한 더 많은 영화정보가 주어진다.

  

- 평가 한 영화

  ![image-20201126215650346](README.assets/image-20201126215650346.png)

  사용자가 평가 한 영화들의 목록을 보여준다. 사용자는 자신이 평가했던 영화를 잊어버리지 않고 찾을 수 있다.

  

- 영화 세부정보

  ![image-20201126215805741](README.assets/image-20201126215805741.png)

  ![image-20201126215950958](README.assets/image-20201126215950958.png)

  

  영화 트레일러, 포스터, 줄거이, 제작진 등 영화에 대한 필요한 모든 정보를 얻을 수 있는 화면이다.

  모달 형식으로 구상해 사용자 경험을 향상시켰다.

  

- 영화 평점 및 리뷰, 좋아요 기능

  ![image-20201126220102676](README.assets/image-20201126220102676.png)

  영화 상세 페이지에 직접 리뷰를 작성할 수 있고, 다른 사람이 작성한 리뷰를 보고 좋아요 할 수 있다.

  영화에 대한 평가를 5점 척도로 매길 수 있다.

  

## 개발 환경

### 데이터

- 영화 진흥 위원회
  - 기본적인 영화 정보들을 가져옴

![image-20201126211430635](README.assets/image-20201126211430635.png)

- 네이버 검색 시스템에서 크롤링 (beautifulsoup4 라이브러리 이용)
  - 출연진과 영화 포스터 등 부가적인 정보들을 가져옴

![image-20201126211621635](README.assets/image-20201126211621635.png)

- Youtube API
  - 영화 트레일러를 가져옴

![image-20201126211748912](README.assets/image-20201126211748912.png)





### 서버 (Django)

```javascript
// requirement.txt

asgiref==3.3.1
beautifulsoup4==4.9.3
bs4==0.0.1
certifi==2020.11.8
chardet==3.0.4
Django==3.1.3
django-cors-headers==3.5.0
django-seed==0.2.2
djangorestframework==3.12.2
djangorestframework-jwt==1.11.0
Faker==4.16.0
idna==2.10
PyJWT==1.7.1
python-dateutil==2.8.1
pytz==2020.4
requests==2.25.0
six==1.15.0
soupsieve==2.0.1
sqlparse==0.4.1
text-unidecode==1.3
urllib3==1.26.2
```

서버에서는 데이터를 가져와 모델링을 하는 작업이 전반적으로 이루어진다.

각 모델들을 정리하여 클라이언트에게 전달한다.



### 클라이언트 (Vue)

```json
//package.json

{
  "name": "movie_review",
  "version": "0.1.0",
  "private": true,
  "scripts": {
    "serve": "vue-cli-service serve",
    "build": "vue-cli-service build",
    "lint": "vue-cli-service lint"
  },
  "dependencies": {
    "@trevoreyre/autocomplete-vue": "^2.2.0",
    "axios": "^0.21.0",
    "bootstrap": "^4.5.3",
    "bootstrap-vue": "^2.19.0",
    "core-js": "^3.6.5",
    "lodash": "^4.17.20",
    "require": "^2.4.20",
    "router": "^1.3.5",
    "vue": "^2.6.12",
    "vue-bootstrap-typeahead": "^0.2.6",
    "vue-carousel-3d": "^1.0.1",
    "vue-js-modal": "^2.0.0-rc.6",
    "vue-jwt-decode": "^0.1.0",
    "vue-router": "^3.2.0",
    "vuex": "^3.5.1"
  },
  "devDependencies": {
    "@vue/cli-plugin-babel": "~4.5.0",
    "@vue/cli-plugin-eslint": "~4.5.0",
    "@vue/cli-plugin-router": "^4.5.9",
    "@vue/cli-plugin-vuex": "^4.5.9",
    "@vue/cli-service": "~4.5.0",
    "babel-eslint": "^10.1.0",
    "eslint": "^6.7.2",
    "eslint-plugin-vue": "^6.2.2",
    "vue-template-compiler": "^2.6.11"
  },
  "eslintConfig": {
    "root": true,
    "env": {
      "node": true
    },
    "extends": [
      "plugin:vue/essential",
      "eslint:recommended"
    ],
    "parserOptions": {
      "parser": "babel-eslint"
    },
    "rules": {}
  },
  "browserslist": [
    "> 1%",
    "last 2 versions",
    "not dead"
  ]
}
```

클라이언트에서는 사용자가 손쉽게 데이터에 접근할 수 있도록 데이터 시각화 작업을 수행한다.

이용자가 쉽고 간편하게 다양한 서비스를 이용할 수 있도록 지원한다.

또한 서버에서 처리하지 못한 모델의 연산을 수행한다.



## 모델(ERD)

![image-20201126212354501](README.assets/image-20201126212354501.png)

- User: 사용자에 대한 정보를 담고있다. User 테이블은 다른 모든 테이블과 연결되어있다.
- Movie: 영화 정보들을 담고있는 테이블이다.
- user_movie_score: User와 Movie의 서로상속 테이블이다. 영화에 대한 유저의 점수 정보를 담고있다.
- People: 감독과 등장인물에 대한 정보를 담고있다.
- Review: 영화 리뷰 정보를 담고있다. Movie와 User가 Foreign Key이다. User의 좋아요가 가능하다.
- Comment: 리뷰에 대한 댓글 정보를 담고있다. User의 좋아요가 가능하다.

front로 정보를 전달할 때에는 `serializer`를 이용해 `JSON` 형태로 전달한다.



## 느낀점

```
홍진표

처음에는 전체 제작 시간을 3일 정도로 예측했습니다. 이미 다 배웠던 것들이기 때문에 빠르게 할 수 있을 줄 알았습니다.
그러나 막상 해보니까 그렇지 못했습니다. 가장 첫 단계인 API를 가져오는 것부터 예상치 못한 일들의 연속이었습니다.
데이터를 model화 하고, 부족한 데이터들을 크롤링 하는 방법을 공부했습니다.
데이터를 다루는 작업들은 눈에 보이지 않아서 처음에는 조금 힘들었는데, 프로젝트를 진행하면서 감이 잡히기 시작했습니다.
다음 프로젝트에서는 더 능숙하게 데이터를 다룰 수 있을 것 같습니다.
```

```
박철완


```

