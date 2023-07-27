from write_to_file import addToList

while True:
    name = input("Input series name: ('q' to quit)\n")
    if name == "q":
        break
    addToList(name)
