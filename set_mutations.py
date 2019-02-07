# Set Mutations
# What I learned:
# .update(set) will affect the calling set unlike without .update(set)
# getattr(caller, command)(arguments) can be used to use strings to call methods instead of if/elif conditionals
a_size = int(input())
set_a = set(map(int, input().split()))

for i in range(int(input())):
    command = input().split()[0]
    set_b = set(map(int, input().split()))
    getattr(set_a, command)(set_b)
    # if command == "update":
    #     set_a.update(set_b)
    # elif command == "intersection_update":
    #     set_a.intersection_update(set_b)
    # elif command == "symmetric_difference_update":
    #     set_a.symmetric_difference_update(set_b)
    # elif command == "difference_update":
    #     set_a.difference_update(set_b)

print(sum(set_a))
