# Jacob Faulk

import sys
import xml.etree.ElementTree as ET


class Chat():
    def __init__(self, address, contact_name):
        self.address = address
        self.contact_name = contact_name
        self.messages = []


class Message():
    def __init__(self, body, name, date):
        self.body = body
        self.name = name
        self.date = date

    def __str__(self):
        return "{}: {}".format(self.name, self.body)

    def __repr__(self):
        return self.__str__()


def main():
    if len(sys.argv) != 2:
        print("Input format must match: python parse.py [input file]")

    filename = sys.argv[1]
    tree = ET.parse(filename)
    root = tree.getroot()

    addresses = {}
    chats = []

    for child in root:
        if not child.get("contact_name") in addresses:
            addresses[child.get("contact_name")] = 1
            current_chat = Chat(child.get("contact_name"),
                                child.get("contact_name"))
            chats.append(current_chat)
        else:
            addresses[child.get("contact_name")] += 1
            current_chat = [
                chat for chat in chats if chat.address == child.get("contact_name")][0]
        current_chat.messages.append(Message(child.get("body"), child.get(
            "contact_name") if child.get("type") == "1" else "Me", child.get("readable_date")))

    for chat in chats:
        f = open("./out/" + chat.contact_name + ".txt", 'w')
        for m in chat.messages:
            f.write(str(m) + '\n')
        f.close()


if __name__ == "__main__":
    main()
