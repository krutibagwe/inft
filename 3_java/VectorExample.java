import java.util.Vector;

public class VectorExample {
    public static void main(String[] args) {
    
        Vector<String> v = new Vector<>();

        v.add("Apple");
        v.add("Banana");
        v.add("Orange");

        System.out.println("Vector elements: " + v);

        System.out.println("Size of the Vector: " + v.size());

        System.out.println("Contains 'Apple': " + v.contains("Apple"));

        System.out.println("Element at index 1: " + v.get(1));

        v.remove("Banana");
        System.out.println("Vector after removing 'Banana': " + v);
    }
}
