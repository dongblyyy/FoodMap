# 문자열
str_val = "This is my python code."
print(str_val)

# 인덱싱
print(str_val[11])          # p
print(str_val[-1])          # .
print(str_val[-5])          # c

# 슬라이싱
print(str_val[11:17])       # python
print(str_val[11:-6])       # python
print(str_val[:10])         # This is my

# 문자열 변수 선언
print(str_val.isalpha())    # false
print(str_val.isdecimal())  # false
print(str_val.upper())      # THIS IS MY PYTHON CODE
print(str_val.replace("my", "your")) # This is your python code.

# ======================================================================================
# Format String
weather = "흐림"
temp = 15.8

# % code (%s, %d, %f)
res = "[%s / %f] 오늘 날씨는 %s 입니다. 기온은 %f도 입니다." % (weather, temp, weather, temp)
print(res)

res = "[%s / %f] 오늘 날씨는 %s 입니다. 기온은 %f도 입니다." % (weather, temp, weather, temp)
print(res)

#.format()
res = "[{0} / {1}도] 오늘 기온은 {1}도 입니다. 오늘 날씨는 {0} 입니다.".format(weather, temp)
print(res)

#f"
res = f"오늘 날씨는 {weather}입니다. 기온은 {temp}도 입니다."
print(res)
# ======================================================================================

# 문자열의 더하기.
inum1 = 12
inum2 = 34
print(inum1 + inum2)        # 46

snum1 = "12"
snum2 = "34"
print(snum1 + snum2)        # 1234
print(snum1 * 3)            # 121212

# 문자열 입력받기
input = input("숫자를 입력해주세요.")
num = int(input) + 1
print(f"입력받은 값에 1을 더하면, {num} 입니다.")
