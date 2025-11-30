class Node {
    int data;
    Node next;

    Node(int x){
        data = x;
        next = null;
    }
}

public class Insert {

    static Node InsertAtFront(Node head, int y){
        Node newNode = new Node(y);
        newNode.next = head;
        return newNode;
    }
    
    static Node InsertAtEnd(Node head, int y){
        Node newNode = new Node(y);
        // if LL is empty , make the new node as the head and return
        if (head == null){
            return newNode;
        }

        //store head reference in a temp variable
        Node last = head;

        while(last.next != null){
            last = last.next;
        }
        last.next = newNode;
        return head;

    }

    public static void main(String[] args){

        Node head  = new Node(10);
        head.next = new Node(20);
        head.next.next = new Node(30);

        head = InsertAtEnd(head, 40);
        printList(head);
    }

    public static void printList(Node head){

        Node curr = head;
        while (curr != null) {
            System.out.print(curr.data);
            if (curr.next != null){
                System.out.print(" -> ");
            }
            curr = curr.next;
        }
        System.out.println();
    }
}
