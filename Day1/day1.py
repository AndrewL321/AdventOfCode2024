with open("input.txt", 'r') as file:
    data = [*map(int,file.read().split())]

left = data[0::2]
right = data[1::2]

left.sort()
right.sort()


answer_1 = 0
for i in range(len(left)):
    answer_1 += abs(left[i] - right[i])

print(answer_1)


l = r = 0

answer_2 = 0

while l < len(left) and r < len(right):
    if left[l] == right[r]:
        answer_2 += right[r]
        r += 1
    elif left[l] < right[r]:
        l += 1
    else:
        r += 1

print(answer_2)
