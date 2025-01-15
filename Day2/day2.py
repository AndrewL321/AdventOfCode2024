
with open("input.txt", "r") as file:
    data = [list(y) for y in (map(int, x.split()) for x in file.readlines())]


answer_1 = len(data)

for row in data:
    decreasing = -1 if row[1] < row[0] else 1

    for i in range(len(row)-1):
        difference = (row[i+1] - row[i]) * decreasing
        if difference <= 0 or difference > 3:
            answer_1 -= 1
            break

print(answer_1)


answer_2 = len(data)

def check_list(list):
    decrease = -1 if list[1] < list[0] else 1
    for z in range(len(list)-1):
        diff = (list[z+1] - list[z]) * decrease
        if diff <= 0 or diff > 3:
            return False
    return True


for row in data:

    decreasing = -1 if row[1] < row[0] else 1

    for i in range(len(row)-1):
        difference = (row[i+1] - row[i]) * decreasing
        if difference <= 0 or difference > 3:
            if not (check_list(row[:i] + row[i+1:]) or check_list(row[:i+1] + row[i+2:]) or check_list(row[:i -1] + row[i:])):
                answer_2 -= 1
            break

print(answer_2)