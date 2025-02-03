def calculate_love_score(name,name1):
    name_final = name+ " " +name1
    name_final.lower()
    length = len(name) + len(name1)
    store = []
    count = 0

    for i in range(length):
        if name_final[i] == 't':
            count += 1
    for i in range(length):
        if name_final[i] == 'r':
            count += 1
    for i in range(length):
        if name_final[i] == 'u':
            count += 1
    for i in range(length):
        if name_final[i] == 'e':
            count += 1


    count2 = 0

    for i in range(length):
        if name_final[i] == 'l':
            count2 += 1
    for i in range(length):
        if name_final[i] == 'o':
            count2 += 1
    for i in range(length):
        if name_final[i] == 'v':
            count2 += 1
    for i in range(length):
        if name_final[i] == 'e':
            count2 += 1
            
    print(f"TRUE  count is: {count}")
    print(f"Love count is: {count2}")

    print(f"Total love score = {count}{count2}")
    


op = 'Y'
while op == 'y' or op == 'Y':
    name = input("What will be the  first person's name: ")
    name1 = input("What will be the  Second person's name: ")
    calculate_love_score(name,name1)
    op = input("You do want to continue: [y] or [n]")
    