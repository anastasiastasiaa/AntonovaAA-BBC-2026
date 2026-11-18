class CalorieCounter:
    def __init__(self, goal):
        self.goal = goal
        self.total = 0
        self.products = {
    "яблоко": 52,
    "банан": 89,
    "рис": 130,
    "курица": 165
     }
    def calculate(self, calories, weight):
        result = calories * weight / 100
        return result
    def show_status(self):
        remaining = self.goal - self.total
        print("Потреблено:", self.total)
        if remaining < 0:
            print("Вы превысили вашу цель на:", abs(remaining))
        else:
            print("Осталось до нормы:", remaining)
    def get_calories(self, name):
        if name in self.products:
            calories = self.products[name]
        else:
            print("Этого продукта нет в нашей базе. Введите его калорийность.")
            calories = float(input())
            self.products[name] = calories
        return calories

print("Установите вашу ежедневную цель. Введите число:")
goal = int(input())
counter = CalorieCounter(goal)
while True:
    print("Введите продукт")
    name = input()
    calories = counter.get_calories(name)
    print("Введите вес продукта")
    weight = float(input())
    result = counter.calculate(calories, weight)
    counter.total += result
    counter.show_status()
    print("Вы хотите добавить прием пищи? Введите Да или Нет")
    v = input()
    if v != "Да":
        break
print(counter.total)
