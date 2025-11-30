
class Node{
    int data;
    Node next;

    Node(int x){
        this.data = x;
        this.next = null;

    }
}
public class Main{
    public static void main (String[] args){
        Node head = new Node(10);
        head.next = new Node(20);
        head.next.next = new Node(30);
        head.next.next.next = new Node(40);
        recursiveTraverseListNode(head);

        //traverserList(head);  can be inplemented for the iterattive approach
    }

    public static void traverselList(Node head){
        while(head.next != null){
            System.out.println(head.data);
            head = head.next;
        }
    }

    // recursive function
    //time complexity O(n)
    //space complexity O(n)
    static void recursiveTraverseListNode(Node head){
        if(head == null){
            return;
        }
        System.out.println(head.data);
        traverselList(head.next);
    }

}