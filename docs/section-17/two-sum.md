# Two Sum

## 1. Concept explanation
Two Sum is a canonical hash-map lookup problem.

## 2. Problem statement
Find indices i, j where a[i] + a[j] = target.

## 3. Algorithm intuition
Scan once, store seen values->index, look for complement.

## 4. Java 8 implementation
```java
import java.util.*;

public class TwoSum {
    public static int[] twoSum(int[] a, int target) {
        Map<Integer, Integer> seen = new HashMap<>();
        for (int i = 0; i < a.length; i++) {
            int need = target - a[i];
            Integer j = seen.get(need);
            if (j != null) return new int[]{j, i};
            seen.put(a[i], i);
        }
        return new int[]{-1, -1};
    }
}
```

## 5. Stream API implementation
```java
public class TwoSumStreamNote {
    // Streams are not ideal for index-based lookups; prefer the loop.
}
```

## 6. Sample input
- Input: a=[2,7,11,15], target=9

## 7. Execution steps
- need=target-x
- if seen contains need -> answer

## 8. Output
- Output: [0,1]

## 9. Time and space complexity
- Time: O(n)
- Space: O(n)

## 10. Enterprise relevance
Used in rule engines and complement lookups in ETL pipelines.

## 11. Interview discussion points
- Duplicates
- No-solution behavior
- Two-pointer alternative

## 12. Best practices
- Define failure behavior
- Consider overflow
