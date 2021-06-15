from typing import Dict, List
import os
import sys

print("topic for learning classes and objects")
class person:
    directories: List[str] = ["/etc/dhcp", "/var/lib/dhcp"]
    default_services: Dict[str, List[str]] = {
            "mdr": ["zebra", "OSPFv3MDR", "IPForward"],
            "PC": ["DefaultRoute"],
            "prouter": [],
            "router": ["zebra", "OSPFv2", "OSPFv3", "IPForward"],
            "host": ["DefaultRoute", "SSH"],
        }

    def __init__(self, name, age):
        self.name = name
        self.age = age
    def printname(self, name, age):
        print(mydetails.name, mydetails.age)
        print("name and age: ", name, age)

mydetails = person("manoj", 25)
print(mydetails.directories[0])
print(mydetails.default_services["router"])
print(mydetails.name, mydetails.age)
mydetails.name = "naveen"
mydetails.age = 26
mydetails.printname("charan", 25)
class nicePersons(person):
    pass

newNicePersons = nicePersons("sai", 25)
print(newNicePersons.name, newNicePersons.age)
friends = ("manoj", "sai", "charan")
friends_list = iter(friends)
print(next(friends_list))
print(next(friends_list))
for friendsList in friends:
    print("my friends List:", friendsList)
