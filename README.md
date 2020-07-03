# Web Crawler
Text Mining을 위한 데이터 수집용 크롤러

# New Features
  - Naver 지식인 크롤링

### Tech

사용기술 목록
* [Python 3.7.3](https://www.python.org/) - 파이썬
* [Scrapy 1.6.0](https://scrapy.org/) - 파이썬 오픈소스 Cralwer

### Installation
Python Scrapy 설치

```sh
$ pip install scrapy
$ pip install scrapy_user_agents # random user-agent 생성
```

pymysql 설치(optional)
```sh
$ pip install pymysql
```

### Run Crawler
Scrapy Crawler 실행

Crawler 실행 명령:
```sh
$ scrapy crawl [크롤러명]
```
#### Example
Naver 지식인 Crawler 실행 명령:
```sh
$ scrapy crawl NaverKinCrawler
```

### TODO list
 - 
 
License
----
MIT License
