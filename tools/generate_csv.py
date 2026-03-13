import csv
import random

students = [f"Студент_{i}" for i in range(500000)]

with open('big_data.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['student', 'date', 'coffee_spent', 'sleep_hours', 'study_hours', 'mood', 'exam'])
    for student in students:
        dates = ["2024-06-01"] * random.randint(1, 20)
        for date in dates:
            coffee_spent = random.randint(100, 1000)
            sleep_hours = round(random.uniform(2, 10), 1)
            study_hours = random.randint(1, 20)
            moods = ['норм', 'устал', 'зомби', 'отл', 'не выжил']
            mood = random.choice(moods)
            exam = 'Математика'
            writer.writerow([student, date, coffee_spent, sleep_hours, study_hours, mood, exam])
