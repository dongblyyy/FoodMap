# 불변적 속성

# 빈 튜플 생성
my_tuple = (1, )

# 과일 바구니
fruits = ("apple", "banana", "blueberry")
first = fruits[0]
print("first : ", first)

# 패킹과 언패킹
tp = 1, 2, 3
print(tp)

v1, v2, v3 = tp
print(f"{v1}, {v2}, {v3}")

a = 10
b = 20

a, b = b, a # (20, 10)

tp = (1, 2, 3, 4, 5, 6, 7, 8)
val1, val2, val3, *vals, _ = tp
print(vals)
vals.append(10)
print(vals)