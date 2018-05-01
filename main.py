file = open("text.txt", "r")

c = 0
for i in file:
    for j in i:
        if j == " ":
            c += 1
print(c+1)
