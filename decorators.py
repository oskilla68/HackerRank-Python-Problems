# Decorators 2 - Name Directory
import operator
from operator import itemgetter

def person_lister(f):
    def inner(people):
        # complete the function
        # print("ABC {0}".format(f(people)))

        for person in people:
            person[2] = int(person[2])

        people.sort(key = itemgetter(2))

        abc = []

        for person in people:
            person[3] = person[3].upper()
            abc.append("{0}".format(f(person)))

        # return people
        # ageSorted = people.sort(itemgetter(2))
        # for peep in ageSorted:
        #     return name_format(peep)
        # return people
        return abc
    # return inner(f)
    return inner

@person_lister
def name_format(person):
    return ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]

if __name__ == '__main__':
    people = [input().split() for i in range(int(input()))]
    print(*name_format(people), sep='\n')
