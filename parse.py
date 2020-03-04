# Jacob Faulk

import sys
from Chat import Chat
from Message import Message, SMSMessage, MMSMessage, MMSPart
import xml.etree.ElementTree as ET


def main():
    if len(sys.argv) != 2:
        print("Input format must match: python parse.py [input file]")

    filename = "./in/" + sys.argv[1]
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
        if child.tag == "sms":
            current_chat.messages.append(SMSMessage(child.get("contact_name") if child.get(
                "type") == "1" else "Me", child.get("date"), child.get("readable_date"), child.get("body")))
        elif child.tag == "mms":  # NOTE: base64 decode the data value of an MMS message to get the image
            parts = []
            for part in child[0]:
                if part.get("seq") != "-1":
                    parts.append(MMSPart(part.get("ct"), part.get("cl") if part.get("ct") != "text/plain" else part.get("text")))
            current_chat.messages.append(MMSMessage(child.get("contact_name"), child.get("date"), child.get("readable_date"), parts))
        else:
            print("Neither SMS or MMS")

    for chat in chats:
        chat.messages.sort()

    for chat in chats:
        f = open("./out/" + chat.contact_name + ".txt", 'w')
        for m in chat.messages:
            f.write(str(m) + '\n')
        f.close()


if __name__ == "__main__":
    main()
