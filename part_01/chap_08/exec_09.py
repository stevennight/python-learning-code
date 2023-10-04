def show_messages(messages):
    for message in messages:
        print(message)

messages = ['test1', 'test2', 'test3']
show_messages(messages)

def send_messages(messages, sent_messages):
    while messages:
        message = messages.pop()
        print(message)
        sent_messages.append(message)

sent_messages = []
send_messages(messages, sent_messages)
print(messages, sent_messages)

messages = ['test1', 'test2', 'test3']
sent_messages = []
send_messages(messages[:], sent_messages)
print(messages, sent_messages)