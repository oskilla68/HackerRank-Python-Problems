# Set symmetric difference
a = input()
english = set(map(int, input().split()))
b = input()
french = set(map(int, input().split()))
print(len(english.symmetric_difference(french)))
