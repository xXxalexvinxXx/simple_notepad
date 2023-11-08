from datetime import datetime
import Controller.counter as counter

# Region note discribe
class Note:
    def __init__(self, id = int(counter.counter()), title="Header", body = "main text", date = str(datetime.now().strftime("%d.%m.%Y %H:%M:%S"))):
        self.id = id
        self.title = title
        self.body = body
        self.date = date
# endregion

    # region getters
    def get_id(note):
        return note.id

    def get_title(note):
        return note.title

    def get_body(note):
        return note.body

    def get_date(note):
        return note.date
    # endregion

    #region setters
    def set_id(note):
        note.id = int(counter.counter())

    def set_title(note):
        note.title = note

    def set_body(note):
        note.body = note

    def set_date(note):
        note.date = str(datetime.now().strftime("%d.%m.%Y %H:%M:%S"))
    # endregion

    #region definition to_string
    def to_string(note):
        return note.id + ';\n' + note.title + ';\n' + note.body + ';\n' + note.date
    #end region