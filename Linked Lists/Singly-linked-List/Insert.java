class Node {
    int data;
    Node next;

    Node(int x){
        data = x;
        next = null;
    }
}

public class Insert {

    static Node insertPos(Node head, int pos, int val){
        if (pos < 1){
            return head;
        }
        if (pos == 1){
            Node newNode = new Node (val);
            newNode.next = head;
            return newNode;
        }
        Node curr = head;

        for (int i = 1; i < pos-1 && curr != null; i++){
            curr = curr.next;
        }
        
        if (curr == null){
            return head;
        }

        Node newNode = new Node(val);
        curr.next = newNode;
        return head;

    }

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

        Node head  = new Node(1);
        head.next = new Node(2);
        head.next.next = new Node(4);

        int val = 3, pos = 3;
        head = insertPos(head, pos, val);
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
