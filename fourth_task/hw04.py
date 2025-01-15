
def parse_input(user_input): #Функція отримання команди від користувача
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args, contacts): #Функція додавання нового контакту
    name, phone = args
    contacts[name] = phone
    return "Contact added"

def change_contact(args, contacts): #Функція зміну номеру 
    name, phone = args
    contacts[name] = phone
    return "Phone change"

def show_phone(args,contacs): #Функція показати конакт імя та номер телефону
    name = args
    return print(contacts[name])

def show_all(contacts): #Функція показу всіх контактів
    phone_book = list(contacts.items())
    return phone_book

def main(): #Функція обробки команд
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ").strip().lower()
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break

        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(change_contact(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
