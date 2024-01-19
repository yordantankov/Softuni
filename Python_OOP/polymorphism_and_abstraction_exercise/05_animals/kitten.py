from project.cat import Cat


class Kitten(Cat):

    __sound = "Meow"

    def __init__(self, name: str, age: int):
        super().__init__(name,age, "Female")

    @classmethod
    def make_sound(cls):
        return cls.__sound

    def __repr__(self):
        return f"This is {self.name}. {self.name} is a {self.age} year old {self.gender} {self.__class__.__name__}"
