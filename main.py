from chat_room import ChatRoom
from user import User
#hardcoded room
room1 = ChatRoom()


class Main:
    NEXT_ROOM = 1

    def __init__(self):
        self.users = []
        self.rooms = [room1]
        self.main_loop()

    def register(self):
        username = input("Username should be at least 6 symbols long: ").strip()
        password = input("Password: ")
        user = User(username, password)
        self.users.append(user)
        return user

    def find_user(self, username):
        for user in self.users:
            if user.username == username:
                return user
        return "User is not registered in app."

    def user_actions(self, user, flag):
        while not flag:
            self.user_info(user)
            action = input().strip()
            action = int(action)
            if action == 1:
                print(f"Select room: {self.display_rooms()}")
                n = int(input())
                room = self.rooms[n]
                user.enter_room(room)
                room.add_user(user)
                print(f"Entered room №: {n}")
            elif action == 2:
                if user.chat_room is None:
                    print("You are not in room.")
                else:
                    user.chat_room.list_users()
            elif action == 3:
                user.leave_room()
            elif action == 4:
                user.chat_room.list_users()
                print("To who? (enter num)")
                n = int(input())
                room = user.chat_room
                to = room.get_user(n)
                if to is None:
                    print("Cant write to nobody.")
                    continue
                else:
                    message = input("Enter your message here.")
                    user.write_message(to, message, room)
            elif action == 5:
                return self.main_loop()
            elif action == 6:
                user.display_message()
        return flag

    def welcome(self):
        print("""Welcome to our Chat App.
    If you want to register: Press 1
    If you want to login: press 2
    If you want to Quit: press 3""")

    def user_info(self, user='test'):
        if isinstance(user, User):
            pass
        else:
            user = {
                'username': '',
            }
        if user.chat_room:
            text = "leave"
        else:
            text = "enter"
        print(f"""Welcome. {user.username}
    If you want to {text} room: press 1.
    For list room users, press 2.
    For exit room press 3.
    For send message, press 4.
    For logout press 5:
    For open messages press 6:
    """)

    def login(self, username, password):
        if not self.users:
            print("Sorry. Cant login.")
        else:
            for user in self.users:
                if user.username == username and password == user.password:
                    return user
        return "Wrong user &&|| password."

    def main_loop(self):
        self.welcome()
        flag = False
        while not flag:
            action = int(input().strip())
            if action == 1:
                user = self.register()
                self.user_actions(user, flag)
                flag = True
                self.main_loop()
            if action == 2:
                username = input("Username: ").strip()
                password = input("Password: ")
                user = self.login(username, password)
                flag = self.user_actions(user, flag)
            if action == 3:
                return

    def add_room(self):
        next_room = self.get_room_next_num()
        self.rooms.append(next_room)

    def get_room_next_num(cls):
        num = cls.NEXT_ROOM
        instance_room = ChatRoom()
        cls.NEXT_ROOM += 1
        return instance_room

    def display_rooms(self):
        res = ""
        for i in range(len(self.rooms)):
            res += f"Room: {i}: num: {self.rooms[i].num-1}"
        return res


main = Main()
