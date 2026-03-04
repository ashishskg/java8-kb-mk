# Linear Search

## 1. Concept explanation
Linear search scans sequentially until it finds the target or reaches the end.

## 2. Problem statement
Return index of x in array (or -1).

## 3. Algorithm intuition
No assumptions about ordering; check each element.

## 4. Java 8 implementation
```java
public class LinearSearch {
    public static int search(int[] a, int x) {
        for (int i = 0; i < a.length; i++) {
            if (a[i] == x) return i;
        }
        return -1;
    }

    public static void main(String[] args) {
        int[] a = {5, 2, 9};
        System.out.println(search(a, 9));
    }
}
```

## 5. Stream API implementation
```java
import java.util.*;
import java.util.stream.*;

public class LinearSearchStreamNote {
    public static void main(String[] args) {
        List<Integer> xs = Arrays.asList(5, 2, 9);
        boolean found = xs.stream().anyMatch(v -> v == 9);
        System.out.println(found);
    }
}
```

## 6. Sample input
- Input: a=[5,2,9], x=9

## 7. Execution steps
- i=0 compare
- i=1 compare
- i=2 match

## 8. Output
- Output: 2
- Output(stream): true

## 9. Time and space complexity
- Time: O(n)
- Space: O(1)

## 10. Enterprise relevance
Used when data is small/unsorted or when you can’t afford preprocessing.

## 11. Interview discussion points
- Best/worst case
- When linear is better than binary

## 12. Best practices
- Short-circuit early
- Prefer binary search if sorted and queried often
