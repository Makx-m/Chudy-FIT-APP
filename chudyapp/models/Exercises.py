from PersonData import PersonData

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
        return {"message": f"Ćwiczenie '{name}' zostało dodane."}

    def calculate_bmi(self):
        height_in_meters = self.height / 100
        bmi = self.weight / (height_in_meters ** 2)
        return {"bmi": f"Twoje BMI wynosi: {bmi:.2f}", "bmi_value": bmi}

    def suggest_exercises_based_on_bmi(self):
        bmi_result = self.calculate_bmi()
        bmi = bmi_result["bmi_value"]
        if bmi < 18.5:
            return {
                "message": "Twoje BMI wskazuje na niedowagę. Skoncentruj się na ćwiczeniach siłowych i odpowiedniej diecie.",
                "suggestions": [{"name": "Trening siłowy", "duration": 30, "calories_burned": 200}]
            }
        elif 18.5 <= bmi < 24.9:
            return {
                "message": "Twoje BMI jest w normie. Możesz realizować różnorodne aktywności.",
                "suggestions": [
                    {"name": "Joga", "duration": 30, "calories_burned": 150},
                    {"name": "Bieganie", "duration": 30, "calories_burned": 300}
                ]
            }
        else:
            return {
                "message": "Twoje BMI wskazuje na nadwagę. Postaw na ćwiczenia cardio.",
                "suggestions": [{"name": "Spacer szybkim tempem", "duration": 40, "calories_burned": 300}]
            }

    def monitor_progress(self):
        weight_diff = self.weight - self.goal_weight
        fat_diff = self.weight * 0.2 - self.goal_fat  # Przyjęcie 20% tłuszczu jako standardu
        muscle_diff = self.goal_muscle - (self.weight * 0.1)  # Przyjęcie 10% mięśni jako standardu

        progress = {
            "weight": {
                "message": f"Musisz schudnąć jeszcze {weight_diff:.1f} kg." if weight_diff > 0 else 
                           f"Osiągnąłeś wagę poniżej celu o {abs(weight_diff):.1f} kg." if weight_diff < 0 else "Osiągnąłeś cel wagowy!"
            },
            "fat": {
                "message": f"Zredukuj jeszcze {fat_diff:.1f} kg tłuszczu." if fat_diff > 0 else "Osiągnąłeś cel redukcji tłuszczu!"
            },
            "muscle": {
                "message": f"Zbuduj jeszcze {muscle_diff:.1f} kg mięśni." if muscle_diff > 0 else "Osiągnąłeś cel budowy mięśni!"
            }
        }

        return progress

    def personalized_exercise_plan(self):
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

        # Return the exercise plan as a dictionary that can be used by the front-end
        plan_info = {
            "message": "Plan treningowy:",
            "plan": [{"name": exercise['name'], "duration": exercise['duration'], "calories_burned": exercise['calories_burned']} for exercise in plan]
        }

        return plan_info
