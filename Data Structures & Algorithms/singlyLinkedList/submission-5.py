class LinkedList:
    
    def __init__(self):
        self.head = None
        self.tail = None
    
    def get(self, index: int) -> int:
        curr = self.head
        for i in range(index):
            if curr is None:
                return -1
            curr = curr.nxt
        return curr.val if curr is not None else -1

    def insertHead(self, val: int) -> None:
        node = Node(val)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            node.nxt = self.head
            self.head = node

        # print(self.getValues())
            
    def insertTail(self, val: int) -> None:
        node = Node(val)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.nxt = node
            self.tail = node
        
        # print(self.getValues())

    def remove(self, index: int) -> bool:
        prev = self.head
        curr = self.head.nxt if self.head is not None else None

        if index == 0:
            if self.head is None:
                return False
            else:
                self.head = self.head.nxt
                if self.head is None:
                    self.tail = None
                # print(self.getValues())
                return True

        for i in range(index - 1):
            if curr is None:
                return False
            prev = curr
            curr = curr.nxt
        
        if curr is None:
            return False
        prev.nxt = curr.nxt
        if prev.nxt is None:
            self.tail = prev
        # print(self.getValues())
        return True

    def getValues(self) -> List[int]:
        curr = self.head
        res = []
        while curr is not None:
            res.append(curr.val)
            curr = curr.nxt
        return res
        
class Node:
    def __init__(self, val: int):
        self.val = val
        self.nxt = None