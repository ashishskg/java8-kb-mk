# Lambda Expressions

## 1. Concept explanation
Lambdas implement functional interfaces without anonymous-class boilerplate. They enable *behavior passing* and composition.

Key rules:
- Captured variables must be effectively-final
- Prefer pure functions (no side effects)
- Understand scope: `this` refers to the enclosing instance (unlike anonymous classes)

## 2. Problem statement
Implement sorting and a service-style transformation pipeline with minimal boilerplate.

## 3. Algorithm intuition
A lambda is a method body + captured context. The runtime may use invokedynamic for efficient linkage.

ASCII (behavior passed into API):
List.sort( Comparator )
Stream.map( Function )
Stream.filter( Predicate )

## 4. Java 8 implementation
```java
import java.util.*;

public class LambdaSort {
    public static void main(String[] args) {
        List<String> names = Arrays.asList("amy", "bob", "carl");
        names.sort((a, b) -> a.compareTo(b));
        System.out.println(names);
    }
}
```

## 5. Stream API implementation
```java
import java.util.*;
import java.util.stream.*;

public class LambdaStream {
    public static void main(String[] args) {
        List<String> names = Arrays.asList("amy", "bob", "carl");
        List<String> out = names.stream().map(s -> s.toUpperCase()).collect(Collectors.toList());
        System.out.println(out);
    }
}
```

## 6. Sample input
- Input: [amy, bob, carl]

## 7. Execution steps
- Pass comparator lambda into sort
- Pass mapping lambda into stream map
- Collect results

## 8. Output
- Output: [AMY, BOB, CARL] (stream example)

## 9. Time and space complexity
- Time: O(n log n) sort; O(n) map
- Space: O(n)

## 10. Enterprise relevance
Used in DTO mapping, validation, and executor callbacks.

Production pitfall: side effects inside parallel pipelines can corrupt shared state.

## 11. Interview discussion points
- What is effectively-final?
- Lambda vs anonymous class (`this`, capture, serialization)
- When lambdas hurt readability/debugging

## 12. Best practices
- Keep lambdas small; extract named methods for complex logic
- Avoid capturing mutable state
- Prefer method references when they improve readability
