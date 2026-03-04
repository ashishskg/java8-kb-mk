# Set Interface

## 1. Concept explanation
`Set` is a collection that contains no duplicate elements. Uniqueness is defined by equals/hashCode.

## 2. Problem statement
Deduplicate user ids and keep membership checks fast.

## 3. Algorithm intuition
Use a Set when you need membership tests and uniqueness; avoid using List.contains in hot paths.

## 4. Java 8 implementation
```java
import java.util.*;

public class SetBasics {
    public static void main(String[] args) {
        List<String> ids = Arrays.asList("u1", "u2", "u1");
        Set<String> uniq = new HashSet<>(ids);
        System.out.println(uniq.contains("u2"));
        System.out.println(uniq);
    }
}
```

## 5. Stream API implementation
```java
import java.util.*;
import java.util.stream.*;

public class SetStream {
    public static void main(String[] args) {
        List<String> ids = Arrays.asList("u1", "u2", "u1");
        Set<String> uniq = ids.stream().collect(Collectors.toSet());
        System.out.println(uniq);
    }
}
```

## 6. Sample input
- Input: ["u1","u2","u1"]

## 7. Execution steps
- Insert into HashSet
- Check contains
- Print

## 8. Output
- Output: true
- Output: Set contains u1,u2

## 9. Time and space complexity
- add/contains: O(1) average
- Space: O(n)

## 10. Enterprise relevance
Sets are used for authorization checks, deduping event ids, and preventing duplicate processing.

## 11. Interview discussion points
- equals/hashCode contract
- HashSet vs TreeSet
- Why duplicates are dropped

## 12. Best practices
- Use Set for membership
- Don’t mutate keys
- Be explicit about ordering needs
