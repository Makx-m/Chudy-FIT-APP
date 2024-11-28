from PersonData import PersonData;

class Exercises(PersonData):
    def __init__(self, name, weight, height, sex, age, image, activePerDay, goal_weight, goal_fat, goal_muscle) -> None:
        super().__init__(name, weight, height, sex, age, image, activePerDay, goal_weight, goal_fat, goal_muscle)    
        self.exercises = []    
    
    def add_exercise(self, name, duration, calories_burned):
        
        exercise = {
            "name": name,
            "duration": duration,
            "calories_burned": calories_burned
        }
        self.exercises.append(exercise)
        print(f"Ćwiczenie '{name}' zostało dodane.")

    def calculate_bmi(self):
        
        height_in_meters = self.height / 100
        bmi = self.weight / (height_in_meters ** 2)
        print(f"Twoje BMI wynosi: {bmi:.2f}")
        return bmi

    def suggest_exercises_based_on_bmi(self):
        
        bmi = self.calculate_bmi()
        if bmi < 18.5:
            print("Twoje BMI wskazuje na niedowagę. Skoncentruj się na ćwiczeniach siłowych i odpowiedniej diecie.")
            return [{"name": "Trening siłowy", "duration": 30, "calories_burned": 200}]
        elif 18.5 <= bmi < 24.9:
            print("Twoje BMI jest w normie. Możesz realizować różnorodne aktywności.")
            return [{"name": "Joga", "duration": 30, "calories_burned": 150}, {"name": "Bieganie", "duration": 30, "calories_burned": 300}]
        else:
            print("Twoje BMI wskazuje na nadwagę. Postaw na ćwiczenia cardio.")
            return [{"name": "Spacer szybkim tempem", "duration": 40, "calories_burned": 300}]

    def monitor_progress(self):
       
        print(f"Postęp użytkownika {self.name}:")
        weight_diff = self.weight - self.goal_weight
        fat_diff = self.weight * 0.2 - self.goal_fat  # Przyjęcie 20% tłuszczu jako standardu
        muscle_diff = self.goal_muscle - (self.weight * 0.1)  # Przyjęcie 10% mięśni jako standardu

        if weight_diff > 0:
            print(f"Musisz schudnąć jeszcze {weight_diff:.1f} kg.")
        elif weight_diff < 0:
            print(f"Osiągnąłeś wagę poniżej celu o {abs(weight_diff):.1f} kg.")
        else:
            print("Osiągnąłeś cel wagowy!")

        if fat_diff > 0:
            print(f"Zredukuj jeszcze {fat_diff:.1f} kg tłuszczu.")
        else:
            print("Osiągnąłeś cel redukcji tłuszczu!")

        if muscle_diff > 0:
            print(f"Zbuduj jeszcze {muscle_diff:.1f} kg mięśni.")
        else:
            print("Osiągnąłeś cel budowy mięśni!")

    def personalized_exercise_plan(self):
        
        print(f"Tworzenie planu treningowego dla {self.name}...")
        plan = []

        # Użytkownik z małą aktywnością
        if self.activePerDay < 30:
            plan.append({"name": "Spacer", "duration": 20, "calories_burned": 100})
        elif self.activePerDay < 60:
            plan.append({"name": "Bieganie", "duration": 30, "calories_burned": 300})
        else:
            plan.append({"name": "Trening siłowy", "duration": 40, "calories_burned": 250})

        # Uwzględnienie celu wagowego
        if self.weight > self.goal_weight:
            plan.append({"name": "Trening cardio", "duration": 40, "calories_burned": 400})
        else:
            plan.append({"name": "Joga", "duration": 30, "calories_burned": 150})

        # Uwzględnienie celu mięśniowego
        if self.goal_muscle > self.weight * 0.1:
            plan.append({"name": "Trening siłowy", "duration": 50, "calories_burned": 300})

        print("Plan treningowy:")
        for exercise in plan:
            print(f"{exercise['name']} - {exercise['duration']} min, {exercise['calories_burned']} kcal")
        return plan