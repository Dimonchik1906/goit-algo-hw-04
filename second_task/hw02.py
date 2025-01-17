from pathlib import Path

def get_cats_info(path): #функція отримання даних про котів
    try:
        with open(path,'r',encoding='utf-8') as file:
            lines = file.readlines()
    except OSError: #опрацювання помилки відкриття файлу
        print('file not found')
        return(0)
    try:
        cats_dict = {}
        cats_info = []
        for line in lines:
            data = line.strip().split(',')
            cats_dict["id"]= data[0]
            cats_dict["name"]= data[1]
            cats_dict["age"]= data[2]
            cats_info.append({"id":cats_dict["id"],"name":cats_dict["name"],"age":cats_dict["age"]})    
    except ValueError:  #опрацювання помилки данних
        print('Помиллка в данных')
        return(0)
    
    return cats_info #виведення результату

cats_info = get_cats_info("second_task/cats_file.txt")
print(cats_info)