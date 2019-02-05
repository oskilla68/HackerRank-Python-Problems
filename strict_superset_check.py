# Strict Superset Check
super_set = list(map(int, input().split()))
amount = int(input())
while amount > 0:
    sub_set = list(map(int, input().split()))
    for number in sub_set:
        if super_set.count(number) == 0:
            print(False)
            exit()
    amount -= 1
print(True)
