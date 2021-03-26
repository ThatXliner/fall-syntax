// NOTE: I Don't even *know* Java. I guessed this program which miracously works.
public class MyClass {
    static int method(int[] v) {
        int total = 0;
        for (int i = 0; i < v.length; i++) {
            total += v[i];
        }
        return total / v.length;
    }
    public static void main(String[] args) {
        int[] a = {1 , 2, 3};
        System.out.println(method(a));
    }
}
