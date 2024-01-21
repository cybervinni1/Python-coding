'''
    Sort a LinkedList

    Time: O(N^2) where N is the number of nodes in the linkedlist
    Space: O(1)

'''
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

def sort(linkedList):
    isSorted = False
    while not isSorted:
        isSorted = True
        currentNode = linkedList
        while currentNode.next is not None:
            if currentNode.value > currentNode.next.value:
                currentNode.value, currentNode.next.value = currentNode.next.value, currentNode.value
                isSorted = False
            currentNode = currentNode.next
    print(linkedList)

# Build a LinkedList
linkedList = LinkedList(10)
nextNode = linkedList
for i in reversed(range(10)):
    nextNode.next = LinkedList(i)
    nextNode = nextNode.next

print(linkedList)
sort(linkedList)
