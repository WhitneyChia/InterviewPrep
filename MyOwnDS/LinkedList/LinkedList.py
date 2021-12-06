
class AbstractLinkedListNode:

    def __init__(self, val):
        self.val = val
        self.next = None


class SinglyLinkedListNode(AbstractLinkedListNode):

    def __init__(self, val):
        super().__init__(val)


class DoublyLinkedListNode(AbstractLinkedListNode):

    def __init__(self, val):
        super().__init__(val)
        self.prev = None


class AbstractLinkedList:

    def __init__(self, head: AbstractLinkedListNode):
        self.head = head


class SinglyLinkedList(AbstractLinkedList):

    def __init__(self, head: SinglyLinkedListNode):
        super().__init__(head)


class DoublyLinkedList(AbstractLinkedList):

    def __init__(self, head: DoublyLinkedListNode):
        super().__init__(head)
