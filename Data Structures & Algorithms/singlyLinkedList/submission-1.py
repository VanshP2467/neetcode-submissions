class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class LinkedList:

    def __init__(self):
        self.head = ListNode(-1)
        self.tail = self.head
        self.length = 0

    def get(self, index: int) -> int:

        current = self.head.next
        i = 0
        while current:
            if i == index:
                return current.val
            i += 1
            current = current.next
        return -1


    def insertHead(self, val: int) -> None:
        newNode = ListNode(val)
        newNode.next = self.head.next
        self.head.next = newNode

        if not newNode.next:
            self.tail = newNode


    def insertTail(self, val: int) -> None:

        self.tail.next = ListNode(val)
        self.tail = self.tail.next


    def remove(self, index: int) -> bool:
        i = 0
        current = self.head
        while i < index and current:
            i += 1
            current = current.next

        if current and current.next:
            if current.next == self.tail:
                self.tail = current
            current.next = current.next.next
            return True
        return False
    
    def getValues(self) -> List[int]:
        current = self.head.next
        result = []
        while current:
            result.append(current.val)
            current = current.next
        return result
