from programmer import Programmer
from actor import Actor
from farmer import Farmer

# case 1
dave = Programmer("Dave", 42, "Python")
dave.introduce()

song = Actor("Song", 55, "Parasite")
song.introduce()

kim = Farmer("Kim", 40, "Apple")
kim.introduce()

# case 2
people = [
    Programmer("Dave", 42, "Python"),
    Actor("Song", 55, "Parasite"),
    Farmer("Kim", 40, "Apple"),
]

for person in people:
    person.introduce()


# 캡슐화
dave.age = -1  # private 설정으로 접근 제어.
dave._hello()
