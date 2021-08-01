from db_connect import db

# "testCollection"이라는 Collection에 접속한다. 없다면 새로 만든다.
collection = db.get_collection("testCollection")

# 하나 삽입
result = collection.insert_one(
	{ "user": 1 }
)