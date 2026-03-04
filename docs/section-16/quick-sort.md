# Quick Sort

## 1. Concept explanation
Quick sort partitions around a pivot and recursively sorts partitions. Average O(n log n), worst O(n^2).

## 2. Problem statement
Sort an integer array ascending.

## 3. Algorithm intuition
Partition so left<pivot and right>pivot; recursion sorts subarrays.

## 4. Java 8 implementation
```java
import java.util.*;

public class QuickSort {
    static void sort(int[] a) { sort(a, 0, a.length - 1); }

    static void sort(int[] a, int lo, int hi) {
        if (lo >= hi) return;
        int p = partition(a, lo, hi);
        sort(a, lo, p - 1);
        sort(a, p + 1, hi);
    }

    static int partition(int[] a, int lo, int hi) {
        int pivot = a[hi];
        int i = lo;
        for (int j = lo; j < hi; j++) {
            if (a[j] <= pivot) {
                int t = a[i]; a[i] = a[j]; a[j] = t;
                i++;
            }
        }
        int t = a[i]; a[i] = a[hi]; a[hi] = t;
        return i;
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
- Choose pivot
- Partition
- Recurse left/right

## 8. Output
- Output: [1, 2, 4, 5, 8]

## 9. Time and space complexity
- Time: O(n log n) avg, O(n^2) worst
- Space: O(log n) avg recursion

## 10. Enterprise relevance
Built-in sorts are heavily optimized (dual-pivot quicksort for primitives). In interviews, discuss pivot choice and worst-case.

## 11. Interview discussion points
- Partition schemes
- Pivot selection
- Why worst-case happens

## 12. Best practices
- Prefer built-in sort
- Randomize/median-of-three pivot to reduce worst-case
