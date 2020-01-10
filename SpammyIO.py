import json
import os


def jsonToTxt():
    jason = json.loads(open('savedIDs.json').read())
    
    try:
        os.makedirs("output")
        print("Directory Created")
    except FileExistsError:
        print("Directory already exists")
    
    for key,value in jason.items():
        file = open('output/{0}.txt'.format(key), 'w+')
        for line in value:
            file.write(line+'\n')

def TxtToJson():
    try:
        IDLists = json.loads(open('savedIDs.json').read())
    except:
        IDLists = {}
        file = open("savedIDs.json", "w+")
        file.close()

    path = input("Insert Path of TXT: ")

    file = open(path)

    ids = list(map(lambda s: s.strip(), file.readlines()))
    print(ids)
    listname = input("Insert ListName: ")
    IDLists[listname] = ids
    with open("savedIDs.json", "w") as write_file:
        json.dump(IDLists, write_file)

choice = -1
while choice not in [0,1]:
    choice = input("[0] Import IDS | [1] Export IDS")

if choice == 0:
    TxtToJson()
else:
    jsonToTxt()
