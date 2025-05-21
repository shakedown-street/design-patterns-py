from abc import ABC, abstractmethod


"""
This is an example of the observer behavioral pattern implemented in Python.

Scenario:
We have a chat application that notifies all connected clients when a
new message is sent.
"""


class Subject(ABC):
    @abstractmethod
    def attach(self, observer: "Observer"):
        pass

    @abstractmethod
    def detach(self, observer: "Observer"):
        pass

    @abstractmethod
    def notify(self, **kwargs):
        pass


class Observer(ABC):
    @abstractmethod
    def update(self, subject: Subject, **kwargs):
        pass


class ChatRoom(Subject):
    def __init__(self):
        self.observers: list[Observer] = []
        self.messages: list[str] = []

    def attach(self, observer: "Observer"):
        self.observers.append(observer)

    def detach(self, observer: "Observer"):
        self.observers.remove(observer)

    def notify(self, **kwargs):
        for observer in self.observers:
            observer.update(self, **kwargs)

    def send_message(self, message: str):
        self.messages.append(message)
        self.notify(message=message)


class ChatClient(Observer):
    def __init__(self, name: str):
        self.name = name

    def update(self, room: ChatRoom, **kwargs):
        print(
            f"{self.name} received a new message in the chat room: {kwargs['message']}"
        )


chat_room = ChatRoom()
client1 = ChatClient("Alice")
client2 = ChatClient("Bob")

chat_room.attach(client1)
chat_room.attach(client2)

chat_room.send_message("Hello, everyone!")
