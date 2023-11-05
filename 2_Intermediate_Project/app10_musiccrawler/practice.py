class User:
    def __init__(self, name, birthyear):
        self.name = name
        self.birthyear = birthyear

    def get_name(self):
        return self.name

    def age(self, current_year):
        age = current_year - self.birthyear
        return age


if __name__ == "__main__":
    user = User(name="John", birthyear=1999)
    john_age = user.age(current_year=2023)
    print(john_age)
    print(user.get_name())
