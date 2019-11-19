import sys

max_number_of_cases = 20
min_range = 10
max_range = 30

number_of_cases = int(input())
if number_of_cases < 1 or number_of_cases > max_number_of_cases:
    sys.exit(0)

candies = []
for i in range(0, number_of_cases):
    kids_in_groups = list(map(int, input().split()))
    if len(kids_in_groups) != 2 or int(kids_in_groups[0]) < min_range or int(kids_in_groups[0]) > max_range \
            or int(kids_in_groups[1]) < min_range or int(kids_in_groups[1]) > max_range:
        sys.exit(0)

    bigger_group = max(kids_in_groups)
    smaller_group = min(kids_in_groups)

    if bigger_group % smaller_group == 0:
        candies.append(bigger_group)
        continue

    bigger_group_temp = bigger_group
    smaller_group_temp = smaller_group
    while True:

        if smaller_group_temp == bigger_group_temp:
            candies.append(smaller_group_temp)
            break
        else:
            smaller_group_temp += smaller_group
            if smaller_group_temp > bigger_group_temp:
                bigger_group_temp += bigger_group


for i in candies:
    print(i)
