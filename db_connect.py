from pymongo import MongoClient
# db 연동
conn = MongoClient('127.0.0.1')
# "testDB"라는 이름을 가진 DB에 접속한다. 없다면 새로 만든다.
db = conn.get_database("testDB")