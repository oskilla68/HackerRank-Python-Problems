# Strict Superset Check
super_set = list(map(int, input().split()))
# amount = int(input())
# while amount > 0:
#     sub_set = list(map(int, input().split()))
#     for number in sub_set:
#         if super_set.count(number) == 0:
#             print(False)
#             exit()
#     amount -= 1
# print(True)

# A better approach
# > checks for proper/strict superset
# Lambda functions, combined with mapping allows for convenient and shorter code
# Lambda functions simplify functions, where x is the parameter and is followed by the expression
# This is followed by what should be mapped/passed into the lambda function, which is a list of sets of subsets
print(all(map(lambda x: (super_set > x), [set(map(int, input().split())) for i in range(int(input()))])))
