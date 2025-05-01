# Chat Rooms Mediator Pattern in Python

A Python implementation of the Mediator design pattern for chat room communication, where a central server mediates messages between clients without them needing direct references to each other.

## Features

- Implements the Mediator design pattern for decoupled communication
- Chat room server manages all message routing between clients
- Clients can join the chat room and send/receive messages
- Simple and extensible design

## Design Pattern Overview

The Mediator pattern is used here to:

1. Reduce direct dependencies between chat users
2. Centralize communication logic in the `ChatRoom` class
3. Make it easy to add new participants without changing existing code

```bash
python chat_mediator.py
```
## Example Output
```
Alice sends: Hi everyone!
Bob received: Alice: Hi everyone!
Charlie received: Alice: Hi everyone!
Bob sends: Hello Alice!
Alice received: Bob: Hello Alice!
Charlie received: Bob: Hello Alice!
Charlie sends: Hey there!
Alice received: Charlie: Hey there!
Bob received: Charlie: Hey there!
```

## Design Pattern Benefits
- Decoupling: Chat users don't need to know about each other
- Centralized Control: All communication logic is in one place
- Easy Maintenance: Adding new features only requires mediator changes
- Reusability: User classes can be reused in different contexts
