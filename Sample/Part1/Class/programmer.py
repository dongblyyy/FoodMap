from person import Person

class Programmer(Person):
    def __init__(self, name, age, launguage):
        super().__init__(name, 
        age, job="Programmer"),
        self.language = launguage
        
    def introduce(self):
        print(f"나는 {self.language} 언어로 프로그래밍을 할 수 있습니다.")
    