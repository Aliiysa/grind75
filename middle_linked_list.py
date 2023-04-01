def middleNode(head):
    
    # Floyd's cycle finding algorithm
    #  Hare-Tortoise Algorithm

    slow, fast = head, head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow