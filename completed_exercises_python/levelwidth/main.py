#  --- Directions
#  Given the root node of a tree, return
#  an array where each element is the width
#  of the tree at each level.
#  --- Example
#  Given:
#      0
#   /  |  \
#  1   2   3
#  |       |
#  4       5
#  Answer: [1, 3, 2]

def level_width(root):
    arr = [root, 't']
    counters = [0]

    while (len(arr) > 1):
        node = arr.pop(0)

        if (node == 't'):
            counters.append(0)
            arr.append('t')
        else:
            for child in node.children:
              arr.append(child)
            counters[len(counters) - 1] += 1
    
  

    return counters

