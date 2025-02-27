import random

for i in range(0, 5):
    print(random.randint(1000000, 9999999))
    
basket = ["사과", "복숭아", "레몬", "블루베리"]
print(random.choice(basket))
