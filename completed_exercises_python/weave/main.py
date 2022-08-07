#  --- Directions
#  1) Complete the task in weave/queue.js
#  2) Implement the 'weave' function.  Weave
#  receives two queues as arguments and combines the
#  contents of each into a new, third queue.
#  The third queue should contain the *alterating* content
#  of the two queues.  The function should handle
#  queues of different lengths without inserting
#  'undefined' into the new one.
#  *Do not* access the array inside of any queue, only
#  use the 'enqueue', 'dequeue' and 'peek' functions.
#  --- Example
# queue1 = Queue()
# queue1.add(1)
# queue1.add(2)
# queue2 = Queue()
# queue2.add('Hi')
# queue2.add('There')
# weaved_queue = weave(queue1, queue2)
# weaved_queue.remove() // 1
# weaved_queue.remove() // 'Hi'
# weaved_queue.remove() // 2
# weaved_queue.remove() // 'There'

from queue import Queue

def weave(sourceOne, sourceTwo):

    queue = Queue()

    while sourceOne.peek() != None and sourceTwo.peek() != None:

        if sourceOne.peek() != None:
          queue.enqueue(sourceOne.dequeue())

        if sourceTwo.peek() != None:
          queue.enqueue(sourceTwo.dequeue())

    return queue
