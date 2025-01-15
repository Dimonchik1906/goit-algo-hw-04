from sys import argv
from pathlib import Path
from colorama import Fore, Back, Style

def parth_folder(path, depth:int = 0): #функція ввидення в консоль папок і файлів
    groups = {True: [], False: []}
    count = 0
    path = Path(path)
    
    if path.exists() and path.is_dir():
        
        if depth == 0:  #Перевірка та виведення початку дерева
            print(Back.BLACK, '📦', Fore.GREEN, path.absolute().name, sep='')
    
        for item in path.iterdir(): # pfgовнюэмо словник з папок і файлів
            groups[item.is_dir()].append(item.name)
            count += 1
            
        for is_dir, items in groups.items(): #Друкуємо 
            for item in sorted(items):
                count -= 1
            
                print(Back.BLACK,
                        Fore.WHITE,
                        '┃ ' * depth,
                        '┣ ' if count else '┗ ',
                        '📂' if is_dir else '📜',
                        Fore.BLACK if is_dir else Fore.BLUE,
                        item,
                        sep='',)
                
                if is_dir:
                    parth_folder(f'{path}/{item}', depth + 1)
                
    else:
        print(f'{Back.BLACK}{Fore.RED}{path} is absent or it is a file.')
        
    print(Style.RESET_ALL, end='')
        
def main():
    parth_folder(argv[1] if len(argv) > 1 else '.')

if __name__ == '__main__':
    main()