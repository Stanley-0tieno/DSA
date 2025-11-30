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

    public static void main(String[] args){

        Node head  = new Node(10);
        head.next = new Node(20);
        head.next.next = new Node(30);

        head = InsertAtFront (head, 40);
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
