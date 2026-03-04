# Three Sum

## 1. Concept explanation
Three Sum finds all unique triplets (i,j,k) such that a[i]+a[j]+a[k]=0.

## 2. Problem statement
Given an int array, return all unique triplets that sum to 0.

## 3. Algorithm intuition
Sort the array, then fix i and use two pointers (l/r) to find complements while skipping duplicates.

## 4. Java 8 implementation
```java
import java.util.*;

public class ThreeSum {
    public static List<List<Integer>> threeSum(int[] a) {
        Arrays.sort(a);
        List<List<Integer>> res = new ArrayList<>();
        for (int i = 0; i < a.length; i++) {
            if (i > 0 && a[i] == a[i-1]) continue;
            int l = i + 1, r = a.length - 1;
            while (l < r) {
                int s = a[i] + a[l] + a[r];
                if (s == 0) {
                    res.add(Arrays.asList(a[i], a[l], a[r]));
                    l++; r--;
                    while (l < r && a[l] == a[l-1]) l++;
                    while (l < r && a[r] == a[r+1]) r--;
                } else if (s < 0) {
                    l++;
                } else {
                    r--;
                }
            }
        }
        return res;
    }

    public static void main(String[] args) {
        int[] a = {-1, 0, 1, 2, -1, -4};
        System.out.println(threeSum(a));
    }
}
```

## 5. Stream API implementation
```java
public class ThreeSumStreamNote {
    // Streams are not ideal for the two-pointer + duplicate-skip pattern.
    // Prefer the loop-based approach for clarity and performance.
}
```

## 6. Sample input
- Input: [-1,0,1,2,-1,-4]

## 7. Execution steps
- Sort
- Fix i
- Two-pointer scan
- Skip duplicates

## 8. Output
- Output: [[-1, -1, 2], [-1, 0, 1]]

## 9. Time and space complexity
- Time: O(n^2)
- Space: O(1) extra (excluding output)

## 10. Enterprise relevance
Useful pattern for k-sum style matching and risk rules (combinations) after sorting.

## 11. Interview discussion points
- Duplicate handling
- Why sorting helps
- Generalizing to k-sum

## 12. Best practices
- Skip duplicates carefully
- Use long if sums can overflow
