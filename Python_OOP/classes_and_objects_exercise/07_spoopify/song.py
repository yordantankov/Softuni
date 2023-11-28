class Song:
    def __init__(self, name, lenght, single):
        self.name = name
        self.lenght = lenght
        self.single = single


    def get_info(self):
        return f"{self.name} - {self.lenght}"


