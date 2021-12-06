

def reverse(head):
    prev, current = None, head
    
    while current:
        tmp = current.next
        current.next = prev
        prev = current
        current = tmp

    return prev

