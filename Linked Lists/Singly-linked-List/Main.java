class Node{
    int data;
    Node next;

    //constructor to initialize a new node
    Node(int new_data){
        this.data = new_data;
        this.next = null;
    }
}

public class Main{
    public static void main(String[] args){

        //create the first node(head of the list)
        Node head = new Node(10);

        //link the second node
        head.next = new Node(20);

        //link the third node
        head.next.next = new Node(40);

        head.next.next.next = new Node(50);

        //print linked list
        while(head != null){
            System.out.println(head.data + " ");
            System.out.println(head.next + " ");
            head = head.next;
        }

    }
}