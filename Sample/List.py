# 가변적 속성

# my_list = [] # 기본선언
my_list = [10, 20, 30]
print(my_list)

# append
my_list.append(40)
my_list.append(50)
my_list.append(60)
print(my_list)

# Length
print(len(my_list))

# Index
element = my_list[4]
print(element)

# Slice
sliced = my_list[4:]
print("Sliced : ", sliced)

# find
fruits = ["banana", "apple", "blueberry", "cherry"]

is_banana_include = "banana" in fruits
print("Is banana included?", is_banana_include)

index_cherry = fruits.index("cherry")
print("Cherry is ", index_cherry)

# Sort
numbers = [4, 2, 1, 3, 8, 6, 7, 5]
print("Unsort : ", numbers)

numbers.sort()
print("sort : ", numbers)

numbers.sort(reverse=True)
print("sort (Reverse): ", numbers)

# List 요소 추가 및 제거
my_list.clear()

my_list.append(10)
my_list.append(11)
my_list.append(12)
print(my_list)

my_list.extend([13, 14, 15])    # 요소로 추가 
my_list.append([16, 17])        # 복합리스트로 추가
print(my_list)

print(my_list[-1])              # [16, 17]

del my_list[6]
print(my_list)

# List 연산
new_list = my_list + [0, 1, 2]
print(new_list)             

multi_list = [0, 1, 3] * 3
print(multi_list)         

max_value = max(my_list)
min_value = min(my_list)
print(f"최대 값은 {max_value}, 최소 값은 {min_value} 입니다.")