from message import Message


class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.contacts = []
        self.chat_room = None
        self.messages = []

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, value):
        if value.strip() == "" or len(value) < 6:
            print("Username can't be less than 6 symbols or empty spaces")
        if not value.isalpha():
            print("Username can't be only numbers")
        self.__username = value

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, value):
        value = str(value)
        if len(value) < 6 or len(value) > 30:
            print("Password shall be long at least 6 symbols and less than 30")
        self.__password = value

    def add_contact(self, contact):
        if contact not in self.contacts:
            self.contacts.append(contact)
            return f"{contact} successful added."
        return f"Contact already in contacts list"

    def find_contact(self, contact):
        for contact in self.contacts:
            if contact.username == contact:
                return contact
        return f"Contact {contact} not in list."

    def remove_contact(self, contact):
        for contact in self.contacts:
            if contact.username == contact:
                self.contacts.remove(contact)
                return f"{contact} successful removed"
        return f"Contact {contact} not in list."

    def sort_ascending_contacts(self):
        if len(self.contacts) == 0:
            return "No contacts to sort."
        self.contacts.sort()
        res = ""
        for contact in self.contacts:
            res += f"Contact {contact.username} {contact.email}\n"
        return res

    def sort_descending_contacts(self):
        if len(self.contacts) == 0:
            return "No contacts to sort."
        res = ''
        self.contacts.sort(reverse=True)
        for contact in self.contacts:
            res += f"Contact {contact.username} {contact.email}\n"
        return res

    def write_message(self, contact, content, room):
        self.chat_room = room
        message = Message(__class__, contact, content)
        room.add_message(contact, message)

    def enter_room(self, room):
        self.chat_room = room
        room.add_user(self)

    def display_message(self):
        if not self.messages:
            return "Nothing here."
        message = self.messages.pop()
        return f"{message.content} from: {message.sender} at: {message.datetime}"

    def leave_room(self):
        if self.chat_room:
            self.chat_room = None
        else:
            return "you are not in any room."
