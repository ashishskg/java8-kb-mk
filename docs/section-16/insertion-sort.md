# Insertion Sort

## 1. Concept explanation
Insertion sort builds a sorted prefix by inserting each new element into its correct position.

## 2. Problem statement
Sort an integer array ascending.

## 3. Algorithm intuition
Good for nearly-sorted arrays; shifts elements to make room.

## 4. Java 8 implementation
```java
import java.util.*;

public class InsertionSort {
    public static void sort(int[] a) {
        for (int i = 1; i < a.length; i++) {
            int key = a[i];
            int j = i - 1;
            while (j >= 0 && a[j] > key) {
                a[j + 1] = a[j];
                j--;
            }
            a[j + 1] = key;
        }
    }

    public static void main(String[] args) {
        int[] a = {5, 1, 4, 2, 8};
        sort(a);
        System.out.println(Arrays.toString(a));
    }
}
```

## 5. Stream API implementation
```java
import java.util.*;
import java.util.stream.*;

public class Example {
    public static void main(String[] args) {
        List<Integer> xs = Arrays.asList(1, 2, 3, 4, 5);
        int sumOfEvens = xs.stream().filter(x -> x % 2 == 0).mapToInt(x -> x).sum();
        System.out.println(sumOfEvens);
    }
}
```

## 6. Sample input
- Input: [5,1,4,2,8]

## 7. Execution steps
- Take next key
- Shift larger elements right
- Insert key

## 8. Output
- Output: [1, 2, 4, 5, 8]

## 9. Time and space complexity
- Time: O(n^2) worst/avg, O(n) best (nearly sorted)
- Space: O(1)

## 10. Enterprise relevance
Used as a subroutine for small partitions (hybrid sorts) and for nearly-sorted data.

## 11. Interview discussion points
- Stability
- Why good for nearly-sorted
- Comparison count

## 12. Best practices
- Use for small n
- Prefer built-in sort for general use
