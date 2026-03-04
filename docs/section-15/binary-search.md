# Binary Search

## 1. Concept explanation
Binary search finds an element in a sorted array by halving the search range.

## 2. Problem statement
Return index of x in sorted array or -1.

## 3. Algorithm intuition
Compare mid, discard half each iteration.

## 4. Java 8 implementation
```java
public class BinarySearch {
    public static int search(int[] a, int x) {
        int lo = 0, hi = a.length - 1;
        while (lo <= hi) {
            int mid = lo + (hi - lo) / 2;
            if (a[mid] == x) return mid;
            if (a[mid] < x) lo = mid + 1;
            else hi = mid - 1;
        }
        return -1;
    }
}
```

## 5. Stream API implementation
```java
public class BinarySearchStreamNote {
    // Index-based algorithm; streams reduce clarity.
}
```

## 6. Sample input
- Input: [1,3,5,8,12], x=8

## 7. Execution steps
- mid=(lo+hi)/2
- discard half

## 8. Output
- Output: 3

## 9. Time and space complexity
- Time: O(log n)
- Space: O(1)

## 10. Enterprise relevance
Used in routing tables and range lookups.

## 11. Interview discussion points
- Overflow-safe mid
- first/last occurrence

## 12. Best practices
- Add boundary tests
- Document sorted precondition
