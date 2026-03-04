# toMap

## 1. Concept explanation
`Collectors.toMap` builds a Map from stream elements; duplicates require a merge function.

## 2. Problem statement
Index users by id while handling duplicate ids deterministically.

## 3. Algorithm intuition
Always provide a merge function unless you can prove uniqueness.

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

public class ToMapDemo {
    static class User { final String id; final String name; User(String i, String n){ id=i; name=n; } }
    public static void main(String[] args) {
        List<User> users = Arrays.asList(new User("u1","amy"), new User("u1","amy2"), new User("u2","bob"));
        Map<String, String> byId = users.stream().collect(Collectors.toMap(
                u -> u.id,
                u -> u.name,
                (left, right) -> left
        ));
        System.out.println(byId);
    }
}
```

## 6. Sample input
- Input: [(u1,amy),(u1,amy2),(u2,bob)]

## 7. Execution steps
- Key extractor
- Value extractor
- Merge duplicates
- Collect

## 8. Output
- Output: {u1=amy, u2=bob}

## 9. Time and space complexity
- Time: O(n)
- Space: O(n)

## 10. Enterprise relevance
Core for caching/indexing; wrong merge policy can cause data loss or inconsistent behavior.

## 11. Interview discussion points
- Why toMap throws without merge
- Map supplier overload

## 12. Best practices
- Always define merge for non-unique keys
- Avoid heavy work in merge
