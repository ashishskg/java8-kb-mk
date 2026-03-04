# TreeSet

## 1. Concept explanation
`TreeSet` is a sorted set backed by a Red-Black tree. Ordering uses Comparable or a Comparator.

## 2. Problem statement
Keep unique items sorted for range queries and ordered iteration.

## 3. Algorithm intuition
Balanced BST gives O(log n) add/contains and ordered traversal.

## 4. Java 8 implementation
```java
import java.util.*;

public class TreeSetDemo {
    public static void main(String[] args) {
        SortedSet<Integer> s = new TreeSet<>(Arrays.asList(3, 1, 2, 2));
        System.out.println(s);
        System.out.println(s.subSet(1, 3));
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
- Input: [3,1,2,2]

## 7. Execution steps
- Insert into RB-tree
- Iterate sorted
- Use subSet range view

## 8. Output
- Output: [1, 2, 3]
- Output: [1, 2]

## 9. Time and space complexity
- add/contains: O(log n)
- Space: O(n)

## 10. Enterprise relevance
Used for ordered leaderboards, time-based indices, and range queries; slower than HashSet for pure membership.

## 11. Interview discussion points
- Why TreeSet is log n
- Comparator consistency
- NavigableSet operations

## 12. Best practices
- Provide Comparator for domain types
- Keep comparator consistent with equals
