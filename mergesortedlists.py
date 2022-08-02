
from operator import ne


def helloworld(*lists):
    endlist = []
    for list in lists:
        list.sort()
        endlist.extend(list)
    endlist.sort()
    print(endlist)


helloworld([1,2,12,4,5,16,77,8,9], [12,11,1,8, 5,16,7,18])


