
static int findMergeNode(SinglyLinkedListNode headA, SinglyLinkedListNode headB) {
    int headALen = 0, headBLen = 0;
    SinglyLinkedListNode headAcopy = headA, headBcopy = headB;
    while(headAcopy != null){
        headAcopy = headAcopy.next;
        headALen++;
    }
    while(headBcopy != null){
        headBcopy = headBcopy.next;
        headBLen++;
    }
    while(headALen > headBLen){
        headA = headA.next;
        headALen--;
    }
    while(headBLen > headALen){
        headB = headB.next;
        headBLen--;
    }
    while(headA != null){
        if (headA == headB){
            return headA.data;
        }
        headA = headA.next;
        headB = headB.next;
    }
    return -1;
    }
    
