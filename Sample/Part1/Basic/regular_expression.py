import re

# 핸드폰 번호 찾기기
phone_number_pattern = re.compile(r"01[016789]-\d{3,4}-\d{4}")

personal_info = """
이름: 홍길동
주소: 서울시 강남구
전화번호: 010-1234-5678
주민등록번호: 930101-1234567
"""
match = phone_number_pattern.search(personal_info)
if match:
    print(f"핸드폰 번호: {match.group()}")


# 순서 바꾸기
input_string = "서울-대구-대전-부산"
result = re.sub(r"(\w+)-(\w+)-(\w+)-(\w+)", r"\1-\3-\2-\4", input_string)
print(result)


# 개인정보 마스킹
def mask_phone_numbers(match):
    return f"{match.group(1)}-****-{match.group(3)}"


def mask_ssn(match):
    return f"{match.group(1)}─{match.group(2)}******"

phone_number_pattern = re.compile(r"(01[016789])-(\d{3,4})-(\d{4})")
ssn_pattern = re.compile(r"(\d{6})-(\d)\d{6}")

masked_info = phone_number_pattern.sub(mask_phone_numbers, personal_info)
masked_info = ssn_pattern.sub(mask_ssn, masked_info)

print(masked_info)


# HTML 태그 제거하기
def remove_html_tags(input):
    pattern = re.compile(r"<.*?>")
    result = re.sub(pattern, "", input)
    return result

input = "<p>This is <b>Python</b> and <i>Regular Expression</i>.</p>"

result = remove_html_tags(input)
print(result)


# 주민번호에서 생년월일 추출하기
def generate_birthday(matches):
    return f"{'19' if matches[4] in ('1', '2') else '20'}{matches[1]}. {matches[2]}. {matches[3]}"

ssn = "900101 - 4234567"

patten = re.compile(r'(\d{2})(\d{2})(\d{2})-(\d)\d{6}')
result = patten.sub(generate_birthday, ssn)
print(result)

# 정규 표현식 테스트 도구
# https://regexr.com