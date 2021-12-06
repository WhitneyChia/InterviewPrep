class Stack:

    def __init__(self):
        self.__list = []

    def pop(self):
        return self.__list.pop()

    def push(self, value):
        self.__list.append(value)

    def peek(self):
        if not self.__list:
            return None
        return self.__list[-1]


class Queue:
    # LinkedList probably makes more sense for this....

    def __init__(self):
        self.__list = []

    def enqueue(self, value):
        self.__list.insert(0, value)

    def dequeue(self):
        return self.__list.pop()

    def peek(self):
        if not self.__list:
            return None
        return self.__list[-1]


if __name__ == "__main__":

    print("STACK Operations")
    my_stack = Stack()
    my_stack.push(1)
    my_stack.push(2)
    print(my_stack.peek())
    my_stack.push(3)
    print(my_stack.peek())
    print(my_stack.pop())
    print(my_stack.pop())
    print(my_stack.pop())
    print(my_stack.peek())

    print("\n")
    print("QUEUE Operations")
    my_queue = Queue()
    my_queue.enqueue(1)
    my_queue.enqueue(2)
    my_queue.enqueue(3)
    print(my_queue.peek())
    print(my_queue.dequeue())
    print(my_queue.dequeue())
    print(my_queue.peek())
    print(my_queue.dequeue())
    print(my_queue.peek())

