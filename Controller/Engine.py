import Controller.fileReader as fileReader
import Controller.fileWriter as fileWriter
import Model.Note

def add_note():
    title = input('Введите заголовок: ')
    body = input('Введите основной текст: ')
    note = Model.Note.Note(title = title, body = body)
    array_notes = fileReader.fileReader()
    for i in array_notes:
        if Model.Note.Note.get_id(note) == Model.Note.Note.get_id(i):
            Model.Note.Note.set_id(note)
    array_notes.append(note)
    fileWriter.fileWriter(array_notes, 'a')
    print('Заметка добавлена в блокнот')

