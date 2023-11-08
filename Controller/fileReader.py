import Model.Note

def file_read():
    try:
        array = []
        file = open('notes.csv', 'r', encoding = 'utf-8')
        notes = file.read().strip().split('\n')
        for n in notes:
            split_note = n.split(';')
            note = Model.Note.Note(id = split_note[0], title = split_note[1], body = split_note[2], date = split_note[3])
        array.append(note)
    except Exception:
        print('Блокнот пуст')
    finally:
        return array