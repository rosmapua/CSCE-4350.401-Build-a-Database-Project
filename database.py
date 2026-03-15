db = []  # stores key-value pairs.
main_file = "data.db" 

# loads previous data.
def load_data():
    try:
        working_file = open(main_file, "r")

        for line in working_file:
            line = line.strip()
            parts = line.split(" ")

            if parts[0] == "SET":
                key = parts[1]
                value = parts[2]

                found = False

                # checks if key already exists, updates or appends.
                for i in range(len(db)):
                    if db[i][0] == key:
                        db[i] = [key, value]
                        found = True

                if found == False:
                    db.append([key, value])

        working_file.close()

    except:
        pass

# save new command to file.
def input_file(key, value):
    working_file = open(main_file, "a")
    working_file.write("SET " + key + " " + value + "\n")
    working_file.close()

# establishes set command, updates memory.
def set(key, value):
    found = False
    
    for i in range(len(db)):
        if db[i][0] == key:
            db[i] = [key, value]
            found = True

    if found == False:
        db.append([key, value])

    input_file(key, value)


# establishes get command, linear search.
def get(key):

    for pair in db:
        if pair[0] == key:
            print(pair[1])
            return

    print("NULL")

# start of program.
load_data()

while True:

    try:
        command = input() # reads command.
    except:
        break # exits loop.

    parts = command.split(" ")

    if parts[0] == "SET":
        set(parts[1], parts[2])

    elif parts[0] == "GET":
        get(parts[1])

    elif parts[0] == "EXIT":
        break
