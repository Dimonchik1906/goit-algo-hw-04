from pathlib import Path

def total_salary(path):
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
            total += int(salary[1])
            count += 1
        average = total / count
    except ValueError:
        print('Помиллка в данных')
        return(0,0)
    
    return total, int(average)
total, average = total_salary("first_task/text.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")