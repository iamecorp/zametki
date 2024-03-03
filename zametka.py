import json
import os
from datetime import datetime

NOTES_FILE = "notes.json"

def load_notes():
    if not os.path.exists(NOTES_FILE):
        return []
    with open(NOTES_FILE, "r") as file:
        return json.load(file)

def save_notes(notes):
    with open(NOTES_FILE, "w") as file:
        json.dump(notes, file, indent=4)

def create_note(title, message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return {"id": len(load_notes()) + 1, "title": title, "message": message, "timestamp": timestamp}

def add_note(title, message):
    notes = load_notes()
    note = create_note(title, message)
    notes.append(note)
    save_notes(notes)
    print("Заметка успешно сохранена")

def read_notes():
    notes = load_notes()
    for note in notes:
        print(f"ID: {note['id']}, Заголовок: {note['title']}, Тело: {note['message']}, Дата/время: {note['timestamp']}")

def edit_note(note_id, new_title, new_message):
    notes = load_notes()
    for note in notes:
        if note["id"] == note_id:
            note["title"] = new_title
            note["message"] = new_message
            note["timestamp"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            break
    else:
        print("Заметка с указанным ID не найдена")
        return
    save_notes(notes)
    print("Заметка успешно отредактирована")

def delete_note(note_id):
    notes = load_notes()
    for note in notes:
        if note["id"] == note_id:
            notes.remove(note)
            break
    else:
        print("Заметка с указанным ID не найдена")
        return
    save_notes(notes)
    print("Заметка успешно удалена")

def filter_notes_by_date(date_str):
    try:
        date = datetime.strptime(date_str, "%Y-%m-%d").date()
    except ValueError:
        print("Некорректный формат даты. Используйте YYYY-MM-DD.")
        return

    notes = load_notes()
    filtered_notes = [note for note in notes if datetime.strptime(note["timestamp"], "%Y-%m-%d %H:%M:%S").date() == date]
    for note in filtered_notes:
        print(f"ID: {note['id']}, Заголовок: {note['title']}, Тело: {note['message']}, Дата/время: {note['timestamp']}")

def main():
    while True:
        print("Выберите действие:")
        print("1. Создать новую заметку")
        print("2. Показать список заметок")
        print("3. Редактировать заметку")
        print("4. Удалить заметку")
        print("5. Показать заметки по дате")
        print("6. Выйти")

        choice = input("Введите номер действия: ")

        if choice == "1":
            title = input("Введите заголовок заметки: ")
            message = input("Введите тело заметки: ")
            add_note(title, message)
        elif choice == "2":
            read_notes()
        elif choice == "3":
            note_id = int(input("Введите ID заметки для редактирования: "))
            new_title = input("Введите новый заголовок заметки: ")
            new_message = input("Введите новое тело заметки: ")
            edit_note(note_id, new_title, new_message)
        elif choice == "4":
            note_id = int(input("Введите ID заметки для удаления: "))
            delete_note(note_id)
        elif choice == "5":
            date_str = input("Введите дату для фильтрации заметок (YYYY-MM-DD): ")
            filter_notes_by_date(date_str)
        elif choice == "6":
            break
        else:
            print("Некорректный ввод. Попробуйте ещё раз.")

if __name__ == "__main__":
    main()
