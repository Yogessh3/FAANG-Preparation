#Time - O(N) || Space - O(1)
def removeNthFromEnd(head, n):
    counter = 1
    first = head
    second = head
    while counter <= n:
        second = second.next
        counter += 1
    if second is None:
        head = head.next
    else:
        while second.next is not None:
            first = first.next
            second = second.next
        first.next = first.next.next
    return head