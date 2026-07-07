from datetime import datetime

# Represent a user in the chat system
class User :
    def __init__(self,name):
        self.name= name


# Stores message details including sender,text and timestamp
class Message:
    def __init__(self,sender, message):
        self.sender = sender
        self.message = message
        self.timestamp = datetime.now().strftime("%I:%M %p")


# Manages users and messages inside a chat room
class ChatRoom:
    def __init__(self,name):
        self.name = name
        self.users=[]
        self.messages=[]


    # Adds a user only if they have not already joined
    def join(self, user):
        if user not in self.users:
            self.users.append(user)
            print(f"{user.name} joined {self.name}")
        else:
            print("User already joined") 


    # Removes a user if they are currently in the room
    def leave(self,user):
        if user in self.users:
            self.users.remove(user)
            print(f"{user.name} left {self.name}")
        else:
            print("User is not in the Chat Room")   


    # Allows only joined users to send messages    
    def send_message(self, user, message):
        if user in self.users:
            new_message = Message(user, message)
            self.messages.append(new_message)
        else:
            print("You must join the chat room first")


    # Display all messages stored in the chat history
    def show_history(self):
        for message in self.messages:
            print(f"[{message.timestamp}]"  f"{message.sender.name}: {message.message}") 


    # Display all users currently in the room
    def show_users(self):
        print(f"Users in {self.name}:")

        for user in self.users:
            print(f"- {user.name}") 


# ----------------Demo / Testing ------------------                   

# Create users
user1 = User("Heena")
user2 = User("Kanika")


# Craete a chat room
room = ChatRoom("Python Learners")

print(f"\n--- {room.name} ---")


# Users join the room
room.join(user1)
room.join(user2)


# Display active users
room.show_users()

print("\n--- Chat ---")


# Send messages
room.send_message(user1, "Hello")
room.send_message(user2, "Hi Heena")


# Display Chat history
room.show_history()

print("\n--- Leaving ---")


# User leave the room
room.leave(user2)