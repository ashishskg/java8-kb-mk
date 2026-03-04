# toSet

## 1. Concept explanation
`Collectors.toSet()` accumulates elements into a Set (no ordering guarantee).

## 2. Problem statement
Deduplicate roles from a list of user records.

## 3. Algorithm intuition
Sets encode uniqueness; use `toCollection(LinkedHashSet::new)` if you need stable order.

## 4. Java 8 implementation
```java
import java.util.*;

public class Example {
    public static void main(String[] args) {
        List<Integer> xs = Arrays.asList(1, 2, 3, 4, 5);
        int sum = 0;
        for (int x : xs) sum += x;
        System.out.println(sum);
    }
}
```

## 5. Stream API implementation
```java
import java.util.*;
import java.util.stream.*;

public class ToSetDemo {
    static class User { final String role; User(String r){ role=r; } }
    public static void main(String[] args) {
        List<User> users = Arrays.asList(new User("ADMIN"), new User("USER"), new User("USER"));
        Set<String> roles = users.stream().map(u -> u.role).collect(Collectors.toSet());
        System.out.println(roles);
    }
}
```

## 6. Sample input
- Input: roles=[ADMIN, USER, USER]

## 7. Execution steps
- Map to role
- Collect to set

## 8. Output
- Output: [ADMIN, USER] (order may vary)

## 9. Time and space complexity
- Time: O(n)
- Space: O(n)

## 10. Enterprise relevance
Used for dedupe in authorization and feature flags; be explicit about ordering expectations.

## 11. Interview discussion points
- HashSet vs LinkedHashSet
- distinct vs toSet

## 12. Best practices
- Use LinkedHashSet when you care about order
- Use TreeSet when you need sorting
