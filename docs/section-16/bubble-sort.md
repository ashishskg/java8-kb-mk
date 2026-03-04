# Bubble Sort

## 1. Concept explanation
Bubble sort repeatedly swaps adjacent out-of-order elements, bubbling the largest to the end each pass.

## 2. Problem statement
Sort an integer array ascending.

## 3. Algorithm intuition
After i passes, the last i elements are in final position.

## 4. Java 8 implementation
```java
import java.util.*;

public class BubbleSort {
    public static void sort(int[] a) {
        for (int i = 0; i < a.length; i++) {
            boolean swapped = false;
            for (int j = 0; j < a.length - 1 - i; j++) {
                if (a[j] > a[j + 1]) {
                    int t = a[j]; a[j] = a[j + 1]; a[j + 1] = t;
                    swapped = true;
                }
            }
            if (!swapped) return;
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

public class SortStreamNote {
    public static void main(String[] args) {
        int[] a = {5, 1, 4, 2, 8};
        int[] out = IntStream.of(a).sorted().toArray();
        System.out.println(Arrays.toString(out));
    }
}
```

## 6. Sample input
- Input: [5,1,4,2,8]

## 7. Execution steps
- Pass through array swapping adjacent inversions
- Early exit if no swaps

## 8. Output
- Output: [1, 2, 4, 5, 8]

## 9. Time and space complexity
- Time: O(n^2) worst/avg, O(n) best with early-exit
- Space: O(1)

## 10. Enterprise relevance
Mostly for teaching; rarely used in production due to O(n^2).

## 11. Interview discussion points
- Stability
- Best-case optimization
- When it’s acceptable

## 12. Best practices
- Use built-in sort in real systems
- Use bubble sort only for tiny n / education
