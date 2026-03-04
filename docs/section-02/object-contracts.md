# equals/hashCode/toString contracts

## 1. Concept explanation
`equals` and `hashCode` must be consistent for correct behavior in hash-based collections.

ASCII:
HashMap uses hashCode() -> bucket, then equals() to match key

## 2. Problem statement
Make a value object safe to use as a key in HashMap/HashSet.

## 3. Algorithm intuition
If two objects are equal, they must have the same hashCode. Use immutable fields for keys.

## 4. Java 8 implementation
```java
import java.util.*;

final class Key {
    final String id;
    Key(String id) { this.id = id; }

    @Override public boolean equals(Object o) {
        if (this == o) return true;
        if (!(o instanceof Key)) return false;
        Key k = (Key) o;
        return Objects.equals(id, k.id);
    }

    @Override public int hashCode() { return Objects.hash(id); }

    @Override public String toString() { return "Key(" + id + ")"; }
}

public class Contracts {
    public static void main(String[] args) {
        Map<Key, Integer> m = new HashMap<>();
        m.put(new Key("a"), 1);
        System.out.println(m.get(new Key("a")));
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
- Input: put(Key(a)->1), get(Key(a))

## 7. Execution steps
- Compute hashCode
- Find bucket
- Use equals to match

## 8. Output
- Output: 1

## 9. Time and space complexity
- Time: O(1) avg map operations
- Space: O(n)

## 10. Enterprise relevance
Broken contracts cause production cache misses, duplicate keys, and memory leaks in maps/sets.

## 11. Interview discussion points
- equals properties (reflexive/symmetric/transitive)
- hash collisions
- mutable keys

## 12. Best practices
- Use immutable fields
- Never mutate map keys
- Use Objects.equals/hash
