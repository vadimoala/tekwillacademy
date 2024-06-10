import matplotlib.pyplot as plt

with open("ds_salaries.csv", "r") as f:
    li = []
    data = f.readlines()
    for rand in data:
        rand = rand.replace("\n", "")
        li.append(rand.split(","))

    for element in li:
        print(element)

header = li.pop(0)
print(header)