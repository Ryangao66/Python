# Owner: Ryan
# Date: 02-Oct-2024


messages = [
    "How are you today?",
    "Nice weather!",
    "What you up to this weekend?"
]


def show_message(messages, sent_messages):
    while messages:
        current_message = messages.pop()
        print("Current message: {}".format(current_message))
        sent_messages.append(current_message)


def send_message(sent_messages):
    print("\nThe following messages have been sent: ")
    for sent_message in sent_messages:
        print("You have {}".format(sent_message))


sent_messages = []
show_message(messages, sent_messages)
send_message(sent_messages)