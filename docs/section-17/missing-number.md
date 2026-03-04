# Missing Number

## 1. Concept explanation
Missing number in [0..n] can be found via XOR or sum formula.

## 2. Problem statement
Given array containing n distinct numbers from 0..n, find the missing one.

## 3. Algorithm intuition
XOR cancels pairs: a^a=0; XOR all indices and values to get missing.

## 4. Java 8 implementation
```java
public class MissingNumber {
    public static int missing(int[] a) {
        int n = a.length;
        int x = 0;
        for (int i = 0; i <= n; i++) x ^= i;
        for (int v : a) x ^= v;
        return x;
    }

    public static void main(String[] args) {
        int[] a = {3,0,1};
        System.out.println(missing(a));
    }
}
```

## 5. Stream API implementation
```java
import java.util.stream.*;

public class MissingNumberStreamNote {
    public static void main(String[] args) {
        int[] a = {3,0,1};
        int n = a.length;
        int xor = IntStream.rangeClosed(0, n).reduce(0, (acc, i) -> acc ^ i);
        for (int v : a) xor ^= v;
        System.out.println(xor);
    }
}
```

## 6. Sample input
- Input: [3,0,1]

## 7. Execution steps
- XOR 0..n
- XOR all values
- Remaining is missing

## 8. Output
- Output: 2

## 9. Time and space complexity
- Time: O(n)
- Space: O(1)

## 10. Enterprise relevance
Useful for detecting gaps in sequences (with correct constraints) and sanity checks in ETL.

## 11. Interview discussion points
- XOR properties
- Sum overflow vs XOR
- Constraints

## 12. Best practices
- Prefer XOR to avoid overflow
- Validate constraints before applying
