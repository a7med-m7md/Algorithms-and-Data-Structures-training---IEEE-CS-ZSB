def has_cycle(head):
    pointer = []
    current = head
    while current!=None:
        if(current  in pointer):
            return 1
        pointer.append(current)
        current = current.next
    return 0