input_list = []

while 1:
    start = input()
    if start == "ENDOFINPUT":
        break
    input_list.append(list(input()))
    end = input()

for message in input_list:
    for i in range(len(message)):
        if ord(message[i]) >= 65 and ord(message[i]) <= 90:
            if ord(message[i]) < 70:
                message[i] = chr(ord(message[i]) + 21)
            else:
                message[i] = chr(ord(message[i]) - 5)

for message in input_list:
    for i in range(len(message)):
        print(message[i], end="")
    print()
