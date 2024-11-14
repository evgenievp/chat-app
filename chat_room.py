class ChatRoom:
    def __init__(self):
        self.users = []

    def add_message(self, to, message):
        for user in self.users:
            if user.username == to or user.mail == to:
                user.messages.append(message)
                return "Sent."
        else:
            return "User isn't here"

    def add_user(self, user):
        self.users.append(user)

    def remove_user(self, user):
        if user in self.users:
            self.users.remove(user)
            return "User logout"
        return "User isn't here"

    def list_users(self):
        res = ""
        for user in self.users:
            res += f"{user.username}\n"
        return res