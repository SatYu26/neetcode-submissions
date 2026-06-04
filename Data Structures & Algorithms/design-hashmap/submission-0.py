class ListNode:

    def __init__(self, val: list = None, next: "ListNode" = None):
        self.val = val
        self.next = next

class MyHashMap:

    def __init__(self):
        self.head = None

    def put(self, key: int, value: int) -> None:
        if not self.head:
            self.head = ListNode([key, value])

        # key doesnt exist already
        if self.get(key) == -1:
            curr = self.head
            while curr and curr.next:
                curr = curr.next
            
            curr.next = ListNode([key, value])
        # key exists, simply replace value
        else:
            curr = self.head
            while curr:
                if curr.val[0] == key:
                    curr.val[1] = value
                    return None
                curr = curr.next
            # key was not found, lets add it
            curr.next = ListNode([key, value])

    def get(self, key: int) -> int:
        if not self.head:
            return -1

        curr = self.head
        while curr:
            if curr.val[0] == key:
                return curr.val[1]
            curr = curr.next
        return -1

    def remove(self, key: int) -> None:
        if not self.head:
            return None

        dummy = ListNode([0, 0], self.head)
        curr, prev = self.head, dummy
        while curr:
            if curr.val[0] == key: # remove it!
                prev.next = curr.next
                self.head = dummy.next
                return None
            prev = curr
            curr = curr.next

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)