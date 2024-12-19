safe_num = 0
unsafe_num = 0


file = open("./Day_2/2.txt", "r")

for line in file.readlines():
    last_num = int(line.split(" ")[0])
    last_diff = int(line.split(" ")[1])-last_num
    safe = True
    for num in line.split(" ")[1:]:
        num1 = int(num)
        diff = num1 - last_num
        if (diff == 0 or abs(diff) > 3):
            safe = False
        last_num = num1
        if (last_diff > 0) != (diff > 0):
            safe = False
        last_diff = diff
    if safe:
        safe_num += 1
    else:
        unsafe_num += 1

print(safe_num)
print(unsafe_num)

safe_num = 0
unsafe_num = 0


file = open("./Day_2/2.txt", "r")
for line in file.readlines():
    last_num = int(line.split(" ")[0])
    last_diff = int(line.split(" ")[1])-last_num
    safe = True
    dampen = 0
    for num in line.split(" ")[1:]:
        num1 = int(num)
        diff = num1 - last_num
        if (diff == 0 or abs(diff) > 3):
            if dampen < 1:
                dampen += 1
                continue
            safe = False
        if (last_diff > 0) != (diff > 0):
            if dampen < 1:
                dampen += 1
                continue
            safe = False
        last_num = num1
        last_diff = diff
    if safe:
        safe_num += 1
    else:
        unsafe_num += 1

print(safe_num)
print(unsafe_num)
