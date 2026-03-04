# Maximum Subarray

## 1. Concept explanation
Kadane’s algorithm computes maximum subarray sum in one pass.

## 2. Problem statement
Find max contiguous sum.

## 3. Algorithm intuition
At each i, best ending at i is max(a[i], a[i]+prev).

## 4. Java 8 implementation
```java
public class MaxSubarray {
    public static int maxSum(int[] a) {
        int cur = a[0], best = a[0];
        for (int i = 1; i < a.length; i++) {
            cur = Math.max(a[i], cur + a[i]);
            best = Math.max(best, cur);
        }
        return best;
    }
}
```

## 5. Stream API implementation
```java
public class MaxSubarrayStreamNote {
    // Sequential stateful; loop is clearer.
}
```

## 6. Sample input
- Input: [-2,1,-3,4,-1,2,1,-5,4]

## 7. Execution steps
- cur=max(a[i],cur+a[i])
- best=max(best,cur)

## 8. Output
- Output: 6

## 9. Time and space complexity
- Time: O(n)
- Space: O(1)

## 10. Enterprise relevance
Useful for best-window analytics (profit/loss, traffic deltas).

## 11. Interview discussion points
- All-negative arrays
- Return indices too

## 12. Best practices
- Validate non-empty input
- Use long if sums can overflow
