number_list = []
for i in range(9):
    temp = int(input())
    number_list.append(temp)


def getIdx():
    for i in range(len(number_list)):
        if number_list[i] == max(number_list):
            return i + 1


print(max(number_list))
print(getIdx())