my_dict = {}
my_dict["key"] = "value"
print(my_dict)

# Dictionary 추가
person = {"name" : "홍길동", "age" : "30", "city" : "서울"}
name = person["name"]
print(f"이름은 {person['name']}, 나이는 {person['age']}, 고향은 {person['city']} 입니다.")

# Dictionary 얻어오기기
country = person.get("country", "알 수 없음")
print(f"국적은 {country} 입니다.")

# Dictionary 수정
person["age"] = 35
print(f"이름은 {person['name']}, 나이는 {person['age']}, 고향은 {person['city']} 입니다.")

# Dictionary 병합
person_detail = {"country" : "대한민국", "married" : True}

person.update(person_detail)
country = person.get("country", "알 수 없음")
print(f"국적은 {country} 입니다.")

# Dictionary 삭제
print("Before :", person.keys())
del person["married"]
print("After :", person.keys())