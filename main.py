from abc import ABC, abstractmethod
from typing import List

# Mediator interface
class ChatRoomMediator(ABC):
    @abstractmethod
    def send_message(self, message: str, sender: 'User'):
        pass

    @abstractmethod
    def add_user(self, user: 'User'):
        pass

# Colleague interface
class User(ABC):
    def __init__(self, name: str, mediator: ChatRoomMediator):
        self.name = name
        self.mediator = mediator

    @abstractmethod
    def send(self, message: str):
        pass

    @abstractmethod
    def receive(self, message: str):
        pass

# Concrete Mediator
class ChatRoom(ChatRoomMediator):
    def __init__(self):
        self.users: List[User] = []

    def add_user(self, user: User):
        self.users.append(user)
        self.send_message(f"{user.name} has joined the chat", user)

    def send_message(self, message: str, sender: User):
        for user in self.users:
            if user != sender:  # Don't send the message back to the sender
                user.receive(f"{sender.name}: {message}")

# Concrete Colleague
class ChatUser(User):
    def send(self, message: str):
        print(f"{self.name} sends: {message}")
        self.mediator.send_message(message, self)

    def receive(self, message: str):
        print(f"{self.name} received: {message}")

# Client code
if __name__ == "__main__":
    # Create mediator
    chat_room = ChatRoom()

    # Create users
    alice = ChatUser("Alice", chat_room)
    bob = ChatUser("Bob", chat_room)
    charlie = ChatUser("Charlie", chat_room)

    # Add users to chat room
    chat_room.add_user(alice)
    chat_room.add_user(bob)
    chat_room.add_user(charlie)

    # Users communicate through the mediator
    alice.send("Hi everyone!")
    bob.send("Hello Alice!")
    charlie.send("Hey there!")

    # Output:
    # Alice sends: Hi everyone!
    # Bob received: Alice: Hi everyone!
    # Charlie received: Alice: Hi everyone!
    # Bob sends: Hello Alice!
    # Alice received: Bob: Hello Alice!
    # Charlie received: Bob: Hello Alice!
    # Charlie sends: Hey there!
    # Alice received: Charlie: Hey there!
    # Bob received: Charlie: Hey there!
