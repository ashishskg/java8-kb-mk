# Search in Rotated Array

## 1. Concept explanation
A rotated sorted array is sorted but shifted (e.g., [4,5,6,1,2,3]). You can search in O(log n).

## 2. Problem statement
Given rotated sorted array with distinct values, return index of target or -1.

## 3. Algorithm intuition
At each mid, one side is sorted. Decide which side to keep based on target range.

## 4. Java 8 implementation
```java
public class SearchRotated {
    public static int search(int[] a, int x) {
        int lo = 0, hi = a.length - 1;
        while (lo <= hi) {
            int mid = lo + (hi - lo) / 2;
            if (a[mid] == x) return mid;

            // left half sorted
            if (a[lo] <= a[mid]) {
                if (a[lo] <= x && x < a[mid]) hi = mid - 1;
                else lo = mid + 1;
            } else { // right half sorted
                if (a[mid] < x && x <= a[hi]) lo = mid + 1;
                else hi = mid - 1;
            }
        }
        return -1;
    }

    public static void main(String[] args) {
        int[] a = {4,5,6,1,2,3};
        System.out.println(search(a, 2));
    }
}
```

## 5. Stream API implementation
```java
public class SearchRotatedStreamNote {
    // Index-based O(log n) algorithm; streams reduce clarity.
}
```

## 6. Sample input
- Input: a=[4,5,6,1,2,3], x=2

## 7. Execution steps
- mid=2 (6) decide right side
- mid=4 (2) match

## 8. Output
- Output: 4

## 9. Time and space complexity
- Time: O(log n)
- Space: O(1)

## 10. Enterprise relevance
Used in circular buffers, time-window indices, and some partitioned keyspaces.

## 11. Interview discussion points
- Handling duplicates
- Invariant reasoning
- Edge cases (not rotated)

## 12. Best practices
- Use overflow-safe mid
- Add tests for boundaries
