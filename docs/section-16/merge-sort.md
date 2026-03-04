# Merge Sort

## 1. Concept explanation
Merge sort is a divide-and-conquer stable sort: split array, sort halves, merge sorted halves.

## 2. Problem statement
Sort an integer array ascending.

## 3. Algorithm intuition
Merging two sorted arrays is linear; recursion gives O(n log n).

## 4. Java 8 implementation
```java
import java.util.*;

public class MergeSort {
    static void sort(int[] a) {
        int[] tmp = new int[a.length];
        sort(a, tmp, 0, a.length - 1);
    }

    static void sort(int[] a, int[] tmp, int lo, int hi) {
        if (lo >= hi) return;
        int mid = lo + (hi - lo) / 2;
        sort(a, tmp, lo, mid);
        sort(a, tmp, mid + 1, hi);
        merge(a, tmp, lo, mid, hi);
    }

    static void merge(int[] a, int[] tmp, int lo, int mid, int hi) {
        int i = lo, j = mid + 1, k = lo;
        while (i <= mid && j <= hi) {
            if (a[i] <= a[j]) tmp[k++] = a[i++];
            else tmp[k++] = a[j++];
        }
        while (i <= mid) tmp[k++] = a[i++];
        while (j <= hi) tmp[k++] = a[j++];
        for (int p = lo; p <= hi; p++) a[p] = tmp[p];
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
- Split into halves
- Sort halves
- Merge

## 8. Output
- Output: [1, 2, 4, 5, 8]

## 9. Time and space complexity
- Time: O(n log n)
- Space: O(n)

## 10. Enterprise relevance
Stable sorting is important for multi-key sorting and deterministic reports.

## 11. Interview discussion points
- Stability
- Why O(n) extra space
- Merge step

## 12. Best practices
- Use stable sort when needed
- Avoid recursion depth issues for huge arrays
