with open("onemillion.txt", "w") as file:
    for i in range(1,1000000):
        file.write("{}\n".format(i))
