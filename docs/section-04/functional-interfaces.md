# Functional Interfaces

## 1. Concept explanation
Functional interfaces have a single abstract method (SAM) and are targets for lambdas/method references.

Prefer standard types in `java.util.function` (Predicate, Function, Supplier, Consumer) for interoperability.

## 2. Problem statement
Define a reusable validation policy and apply it in a pipeline.

## 3. Algorithm intuition
SAM type inference lets the compiler map a lambda to the interface method signature.

## 4. Java 8 implementation
```java
@FunctionalInterface
interface Validator<T> { boolean isValid(T t); }

public class ValidatorDemo {
    public static void main(String[] args) {
        Validator<String> nonEmpty = s -> s != null && !s.trim().isEmpty();
        System.out.println(nonEmpty.isValid(""));
    }
}
```

## 5. Stream API implementation
```java
import java.util.*;
import java.util.stream.*;

public class ValidatorStream {
    public static void main(String[] args) {
        List<String> xs = Arrays.asList("a", "", "b");
        List<String> out = xs.stream().filter(s -> !s.isEmpty()).collect(Collectors.toList());
        System.out.println(out);
    }
}
```

## 6. Sample input
- Input: [a, "", b]

## 7. Execution steps
- Define functional interface
- Implement via lambda
- Use in stream filter

## 8. Output
- Output: [a, b]

## 9. Time and space complexity
- Time: O(n)
- Space: O(n)

## 10. Enterprise relevance
Used for domain predicates, policies, authorization checks, and reusable composition in service layers.

## 11. Interview discussion points
- @FunctionalInterface meaning
- Default methods allowed?
- Why prefer standard java.util.function types

## 12. Best practices
- Prefer java.util.function types
- Document null-handling
- Keep implementations pure; avoid checked exceptions in lambdas
