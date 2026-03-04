# Selection Sort

## 1. Concept explanation
Selection sort selects the minimum element from the unsorted region and swaps it into place.

## 2. Problem statement
Sort an integer array ascending.

## 3. Algorithm intuition
After i iterations, prefix [0..i] is sorted and fixed.

## 4. Java 8 implementation
```java
import java.util.*;

public class SelectionSort {
    public static void sort(int[] a) {
        for (int i = 0; i < a.length; i++) {
            int min = i;
            for (int j = i + 1; j < a.length; j++) {
                if (a[j] < a[min]) min = j;
            }
            int t = a[i]; a[i] = a[min]; a[min] = t;
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
- For each i, find min in suffix
- Swap into position i

## 8. Output
- Output: [1, 2, 4, 5, 8]

## 9. Time and space complexity
- Time: O(n^2)
- Space: O(1)

## 10. Enterprise relevance
Used when swaps are expensive and comparisons are cheap (still uncommon vs built-ins).

## 11. Interview discussion points
- Why not stable
- Swap count vs bubble/insertion

## 12. Best practices
- Prefer built-in TimSort/dual-pivot quicksort
- Mention when selection sort is reasonable
