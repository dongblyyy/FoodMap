# Empty Set
empty_set = set() #빈 {}을 채우면 Dictionary로 인식.

# Init set
my_set = {1, 2, 3, 3}
print(my_set)

fruits = {"apple", "banana", "blueberry"}
print(fruits)

# 추가. (요소들의 순서를 보장하지 않음.)
fruits.add("oranage")
print(fruits)

# 제거 
fruits.remove("banana")
print(fruits)

fruits1 = {"apple", "strawberry", "peach"}
fruits2 = {"banana", "strawberry", "orange"}

# 합집합
union = fruits1.union(fruits2)
print("합집합: ", union);
print("합집합: ", fruits1 | fruits2)

# 교집합
intersection = fruits1.intersection(fruits2)
print("교집합: ", intersection)

# 차집합
diff1 = fruits1.difference(fruits2)
diff2 = fruits2.difference(fruits1)
print("차집합 (f1 - f2): ", diff1)
print("차집합:(f2 - f1): ", diff2)