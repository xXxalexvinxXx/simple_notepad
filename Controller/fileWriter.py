import Moldel.Note

def file_write(array, mode):
    file = open('notes.csv', mode  ='w', encoding = 'utf-8')
    file.seek(0)
    file.close()
    file = open('notes.csv', mode = mode, encoding = 'utf-8')
    for notes in array:
        file.write(Model.Note.Note.to_string(notes))
        file.write('\n')
    file.close