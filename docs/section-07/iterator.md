# Iterator

## 1. Concept explanation
`Iterator` provides `hasNext/next` and optional `remove`. It’s the safe way to traverse and (carefully) modify collections.

## 2. Problem statement
Remove elements during iteration without `ConcurrentModificationException`.

## 3. Algorithm intuition
Use `Iterator.remove()` (or `removeIf`) instead of removing from the collection directly in a for-each.

## 4. Java 8 implementation
```java
import java.util.*;

public class IteratorRemove {
    public static void main(String[] args) {
        List<Integer> xs = new ArrayList<>(Arrays.asList(1,2,3,4));
        Iterator<Integer> it = xs.iterator();
        while (it.hasNext()) {
            int x = it.next();
            if (x % 2 == 0) it.remove();
        }
        System.out.println(xs);
    }
}
```

## 5. Stream API implementation
```java
import java.util.*;

public class RemoveIfDemo {
    public static void main(String[] args) {
        List<Integer> xs = new ArrayList<>(Arrays.asList(1,2,3,4));
        xs.removeIf(x -> x % 2 == 0);
        System.out.println(xs);
    }
}
```

## 6. Sample input
- Input: [1,2,3,4]

## 7. Execution steps
- Iterate with iterator
- Call iterator.remove() on matches
- Print list

## 8. Output
- Output: [1, 3]

## 9. Time and space complexity
- Time: O(n)
- Space: O(1)

## 10. Enterprise relevance
Common in in-memory filtering in batch jobs; `removeIf` is clearer and less error-prone.

## 11. Interview discussion points
- Why CME happens
- Iterator.remove semantics
- fail-fast vs fail-safe

## 12. Best practices
- Prefer removeIf
- Don’t mutate collection in for-each
- Use concurrent collections when needed
