class LL:
    def __init__(self, data, next):
        self.data = data
        self.next = next

    def __repr__(self):
        return str(self.data)


def mergeLists(head1, head2):
    if head2.data < head1.data:
        head1, head2 = head2, head1

    res = head1

    while head2 and head1.next:
        if head2.data < head1.next.data:
            head1.next, head2 = head2, head1.next
        else:
            head1 = head1.next

    if head2:
        head1.next = head2

    return res


print(mergeLists(LL(1, LL(2, LL(3, None))),
                 LL(3, LL(4, None))))
