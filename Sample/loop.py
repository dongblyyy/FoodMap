# for loop
for i in range(5):
    print(i)
else:
    print("For End")

for i in range(1, 5):
    print(i)
else:
    print("For End")

fruits = ["사과", "딸기", "복숭아", "참외"]

for fruit in fruits:
    if fruit == "사과":
        print(f"{fruit}는 맛있습니다.")

for index, fruit in enumerate(fruits, start = 2):
    print(f"{index}번째 과일은 {fruit} 입니다.")
    index = index + 1

# while
i = 0
while i < 5:
    print(i)
    i += 1
else:
    print("while End")

while True:
    user_input = input("명령어를 입력해주세요: ")
    if user_input == "exit":
        break
    else:   
        pass    # Todo 추후 개발 예정.
    
