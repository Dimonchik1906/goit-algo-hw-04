from pathlib import Path

def total_salary(path): # функція підрахунку заробітної плати та середнього значення
    try:
        with open(path,'r',encoding='utf-8') as file:
            lines = file.readlines()
    except OSError:
        print('file not found')
        return(0,0)
    total = 0
    count = 0
    average = 0
    try:
        for line in lines:
            salary = line.strip().split(',')
            total += float(salary[1])
            count += 1
        if count == 0:
            raise ValueError
        average = total / count
    except ValueError:
        print('Помилка в данных')
        return(0,0)
    
    return total, average

total, average = total_salary("first_task/text.txt") #Шлях до файлу
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")