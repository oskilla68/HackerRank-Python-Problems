# Set .difference() operation
a = input()
english = set(map(int, input().split()))
b = input()
french = set(map(int, input().split()))
print(len(english.difference(french)))
