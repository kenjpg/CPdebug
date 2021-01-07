import os  # Need to allow it to run in the same directory


def clean(file, filename):
    savedr = open("save_"+filename+".txt", "r")
    stack = []
    for line in savedr:
        stack.append(line.rstrip("\n"))
    stack.reverse()
    building = []
    for line in file:
        if (len(stack) > 0):
            if (line.rstrip("\n") == stack[-1]):
                del stack[-1]
                continue
        building.append(line)
    filew = open(filename, 'w')
    for line in building:
        filew.write(line)
    savedr.close()
    filew.close()
    savedw = open("save_"+filename+".txt", 'w')
    savedw.write("")
    savedw.close()
    print("Cleaned!")


while True:
    filename = input()
    if len(filename.split(" ")) == 2:
        pass
    else:
        print("Error")
        continue
    [cmd, filename] = filename.split(" ")
    try:
        file = open(filename, 'r')
        pass
    except FileNotFoundError:
        print("File does not exist")
        continue
    cmd = cmd.lower()
    if (cmd == "debug"):
        break
    elif (cmd == "clean"):
        break
    else:
        print("Incorrect command")
        continue

if (cmd == "debug"):
    try:
        savedr = open("save_"+filename+".txt", "r")
        checklist = []
        for line in savedr:
            checklist.append(1)
        if (len(checklist) != 0):
            clean(file, filename)
    except FileNotFoundError:
        pass
    savedw = open("save_"+filename+".txt", "w")
    index = -1
    building = []
    file.close()
    file = open(filename, "r")
    for line in file:
        building.append(line.rstrip("\n"))
        variable = []
        index += 1
        line = line.rstrip("\n")
        line = line.lstrip("	")
        diff = (len(building[-1]) - len(line))
        fortype = ""
        if (line[0:3] == "for"):
            found = False
            stack = ""
            for char in line:
                if (char == ";" or char == ":"):
                    fortype = char
                    break
                if (char == "("):
                    found = True
                if found:
                    stack += char
            if (fortype == ":"):
                for item in (stack.split("[")[1].split("]")[0].split(",")):
                    item = item.rstrip(" ").lstrip(" ")
                    variable.append(item)
            else:
                variable.append(stack.split(" ")[1])
                if (line.count(" "+variable[0]) != 3):
                    print("line", index+1, ">", "for loop may be incorrect")
            newbuild = "cout <<"
            newbuild = (diff + 1) * "	" + newbuild
            for item in variable:
                newbuild += " " + item + " << " + '" "' + " <<"
            newbuild += r' "\n";'
            building.append(newbuild)
            savedw.write(newbuild+"\n")
        else:
            continue

    file.close()
    filew = open(filename, 'w')
    for line in building:
        line += "\n"
        filew.write(line)
    print("done!")
else:
    clean(file, filename)
