class ChatRoom:
    CHAT_NUM = 1
    def __init__(self):
        self.users = []
        self.num = self.get_num()

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
            return "User kicked"
        return "User isn't here"

    def list_users(self):
        res = ""
        n = 0
        for user in self.users:
            res += f"{user.username} num: {n}\n"
            n += 1
        print(res)

    def get_user(self, n):
        for i in range(len(self.users)):
            if n == i:
                return self.users[i]
        return None

    def get_num(cls):
        num = cls.CHAT_NUM
        cls.CHAT_NUM += 1
        return num