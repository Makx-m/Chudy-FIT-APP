from PersonModel import Person;

class PersonData(Person): 
    def __init__(self, name, weight, height, sex, age, image, activePerDay, goal_weight, goal_fat, goal_muscle) -> None:
        super().__init__(name, weight, height, sex, age, image, activePerDay)
        self.goal_weight = goal_weight
        self.goal_fat = goal_fat
        self.goal_muscle = goal_muscle


        