axiom = "A"
result = axiom
iteration = 8

for i in range(iteration):
    print(result)
    new_result = ""
    for i in result:
        if (i == "A"):
            new_result += "AB"
        elif (i == "B"):
            new_result += "A"
    result = new_result