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

    i = 0

    for child in root:
        # if i > 50:
            # break
        if not child.get("address") in addresses:
            addresses[child.get("address")] = 1
            current_chat = Chat(child.get("address"),
                                child.get("contact_name"))
            chats.append(current_chat)
        else:
            addresses[child.get("address")] += 1
            current_chat = [
                chat for chat in chats if chat.address == child.get("address")][0]
        current_chat.messages.append(Message(child.get("body"), child.get(
            "contact_name") if child.get("type") == "1" else "Me", child.get("readable_date")))
        i += 1

if __name__ == "__main__":
    main()