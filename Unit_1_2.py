class ListNode:
    def __init__(self,val=0,next=None):
        self.val=val
        self.next=next
def reverseKGroup(head,k):
    if not head or k==1:
        return head
    dummy=ListNode(0)
    dummy.next=head
    prev=dummy
    while prev:
        prev=reverseNextK(prev,k)
    return dummy.next
def reverseNextK(prev,k):
    last=prev
    for _ in range(k+1):
        last=last.next
        if not last and _ < k:
            return None
    if not last:
        return None
    tail=prev.next
    curr=prev.next.next
    for _ in range(k-1):
        temp=curr.next
        curr.next=prev.next
        prev.next=curr
        tail.next=temp
        curr=temp
    return tail
def printLinkedList(node):
    while node:
        print(node.val,end=" ")
        node=node.next
    print()
if __name__=="__main__":
    head=ListNode(1)
    head.next=ListNode(2)
    head.next.next=ListNode(3)
    head.next.next.next=ListNode(4)
    head.next.next.next.next=ListNode(5)
    k=2
    print("\nOriginal linked list = ")
    printLinkedList(head)
    head=reverseKGroup(head,k)
    print("\nLinked list after reversing nodes in groups of",k)
    printLinkedList(head)