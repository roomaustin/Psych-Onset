class Person:
    def __init__(self, name):
        self.name = name
        self.potential_conditions = []
        self.confirmed_conditions = []

    def suggest_potential_condition(self, condition):
        if condition not in self.potential_conditions:
            self.potential_conditions.append(condition)
            print(f"{condition} is suggested as a potential condition for {self.name}.")

    def confirm_condition(self, condition):
        if condition in self.potential_conditions:
            self.confirmed_conditions.append(condition)
            self.potential_conditions.remove(condition)
            print(f"{condition} is confirmed for {self.name}.")
        else:
            print(f"{condition} cannot be confirmed as it is not a suggested potential condition.")

    def get_conditions(self):
        print(f"{self.name}'s potential conditions: {self.potential_conditions}")
        print(f"{self.name}'s confirmed conditions: {self.confirmed_conditions}")

# usage
person = Person("John Doe")
person.suggest_potential_condition("anxiety")
person.confirm_condition("depression")  # not a suggested potential condition
person.confirm_condition("anxiety")
person.get_conditions()
