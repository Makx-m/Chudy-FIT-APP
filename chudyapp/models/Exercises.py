from PersonData import PersonData;

class Exercises(PersonData):
    def __init__(self, name, weight, height, sex, age, image, activePerDay, goal_weight, goal_fat, goal_muscle) -> None:
        super().__init__(name, weight, height, sex, age, image, activePerDay, goal_weight, goal_fat, goal_muscle)    
        self.exercises = []    
    
    def add_exercise(self, name, duration, calories_burned):
        
        exercise = {
            'name': name,
            'duration': duration,
            'calories_burned': calories_burned
        }
        self.exercises.append(exercise)
        print(f"Ćwiczenie '{name}' zostało dodane.")

    def list_exercises(self):
    
        if not self.exercises:
            print("Brak ćwiczeń do wyświetlenia.")
            return
        print("Lista ćwiczeń:")
        for idx, exercise in enumerate(self.exercises, 1):
            print(f"{idx}. {exercise['name']} - {exercise['duration']} min, {exercise['calories_burned']} kcal")

    def total_calories(self):
   
        total = sum(exercise['calories_burned'] for exercise in self.exercises)
        print(f"Całkowita liczba spalonych kalorii: {total} kcal")
        return total

    def remove_exercise(self, index):
       
        if 0 <= index < len(self.exercises):
            removed = self.exercises.pop(index)
            print(f"Ćwiczenie '{removed['name']}' zostało usunięte.")
        else:
            print("Nieprawidłowy indeks. Spróbuj ponownie.")

    def suggest_exercises(self):
     
        suggestions = []
        if self.goal_fat > self.weight * 0.2:
            suggestions.append({'name': 'Bieganie', 'duration': 30, 'calories_burned': 300})
        if self.goal_muscle > self.weight * 0.1:
            suggestions.append({'name': 'Trening siłowy', 'duration': 45, 'calories_burned': 200})
        if self.activePerDay < 30:
            suggestions.append({'name': 'Joga', 'duration': 20, 'calories_burned': 100})

        print("Sugerowane ćwiczenia:")
        for exercise in suggestions:
            print(f"{exercise['name']} - {exercise['duration']} min, {exercise['calories_burned']} kcal")

        return suggestions