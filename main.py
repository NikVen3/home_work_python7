# Функция для загрузки контактов из файла
def load_contacts(filepath):
    try:
        with open(filepath, "r") as file:
            # Читаем все строки из файла
            lines = file.readlines()
            # Создаем словарь для хранения контактов
            contacts = {}
            # Обрабатываем строки из файла и добавляем контакты в словарь
            for line in lines:
                name, phone = line.strip().split(":")
                contacts[name] = phone
            return contacts
    except FileNotFoundError:
        # Если файл не найден, возвращаем пустой словарь
        return {}


# Функция для сохранения контактов в файл
def save_contacts_to_file(filepath, contacts):
    with open(filepath, "w") as file:
        # Записываем в файл каждый контакт в формате "имя:номер\n"
        for name, phone in contacts.items():
            file.write(f"{name}:{phone}\n")


# Функция для добавления нового контакта
def add_contact(contacts):
    name = input("Введите имя контакта: ")
    phone = input("Введите номер телефона: ")
    if name in contacts:
        print("Контакт уже существует!")
    else:
        contacts[name] = phone
        print("Контакт успешно добавлен.")


# Функция для поиска контакта по имени
def search_contact(contacts):
    name = input("Введите имя контакта: ")
    if name in contacts:
        print(f"{name}: {contacts[name]}")
    else:
        print("Контакт не найден.")


# Функция для удаления контакта
def delete_contact(contacts):
    name = input("Введите имя контакта: ")
    if name in contacts:
        del contacts[name]
        print("Контакт успешно удален.")
    else:
        print("Контакт не найден.")


# Функция для отображения всех контактов
def show_all_contacts(contacts):
    if len(contacts) == 0:
        print("Телефонная книга пуста.")
    else:
        for name, phone in contacts.items():
            print(f"{name}: {phone}")



def main():

    filepath = "data.txt"
    contacts = load_contacts(filepath)


    while True:

        print("Телефонная книга")
        print("================")
        print("1. Добавить контакт")
        print("2. Найти контакт")
        print("3. Удалить контакт")
        print("4. Показать все контакты")
        print("5. Экспорт контактов в файл")
        print("6. Выход")


        choice = input("Введите номер действия: ")


        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            search_contact(contacts)
        elif choice == "3":
            delete_contact(contacts)
        elif choice == "4":
            show_all_contacts(contacts)
        elif choice == "5":
            save_contacts_to_file(filepath, contacts)
            print("Контакты успешно сохранены.")
        elif choice == "6":
            save_contacts_to_file(filepath, contacts)
            print("Контакты успешно сохранены.")
            break
        else:
            print("Неправильный ввод! Попробуйте еще раз.")


if __name__ == "__main__":
    main()



