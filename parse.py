# Jacob Faulk

import sys
from Chat import Chat
from Message import Message, SMSMessage, MMSMessage, MMSPart
import xml.etree.ElementTree as ET
import base64


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
            current_chat = Chat(child.get("address"),
                                child.get("contact_name"))
            chats.append(current_chat)
        else:
            addresses[child.get("contact_name")] += 1
            current_chat = [
                chat for chat in chats if chat.contact_name == child.get("contact_name")][0]
        if child.tag == "sms":
            current_chat.messages.append(SMSMessage(child.get("contact_name") if child.get(
                "type") == "1" else "Me", child.get("date"), child.get("readable_date"), child.get("body")))
        elif child.tag == "mms":
            if len(child[1]) == 2:
                parts = []
                for part in child[0]:
                    if part.get("seq") != "-1":
                        if part.get("ct") == "text/plain":
                            parts.append(MMSPart(part.get("ct"), part.get("text")))
                        elif part.get("ct")[:5] == "image":
                            parts.append(MMSPart(part.get("ct"), part.get("cl")))
                            f = open(
                                "./out/img/{}_{}".format(child.get("date"), part.get("cl")), 'wb')
                            f.write(base64.b64decode(part.get("data")))
                            f.close()
                        else:
                            parts.append(MMSPart(part.get("ct"), part.get("cl")))
                current_chat.messages.append(MMSMessage(child.get(
                    "contact_name") if child.get("msg_box") == "1" else "Me", child.get("date"), child.get("readable_date"), parts))
            else:
                print("This is a group message.")
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
