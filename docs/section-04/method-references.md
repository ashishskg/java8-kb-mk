# Method References

## 1. Concept explanation
Method references are shorthand for lambdas that forward to an existing method/constructor.

## 2. Problem statement
Make stream pipelines and callbacks more readable.

## 3. Algorithm intuition
Replace `x -> foo(x)` with `Type::foo` when signatures match.

Forms:
- static: Type::staticMethod
- bound: instance::method
- unbound: Type::instanceMethod
- ctor: Type::new

## 4. Java 8 implementation
```java
import java.util.*;

public class MethodRef {
    public static void main(String[] args) {
        Arrays.asList("a", "b").forEach(System.out::println);
    }
}
```

## 5. Stream API implementation
```java
import java.util.*;
import java.util.stream.*;

public class MethodRefStream {
    public static void main(String[] args) {
        List<Integer> out = Arrays.asList("amy", "bob").stream().map(String::length).collect(Collectors.toList());
        System.out.println(out);
    }
}
```

## 6. Sample input
- Input: [amy, bob]

## 7. Execution steps
- Use System.out::println
- Use String::length

## 8. Output
- Output: [3, 3]

## 9. Time and space complexity
- Time: O(n)
- Space: O(n)

## 10. Enterprise relevance
Improves code review readability and standardizes house-style streams.

## 11. Interview discussion points
- Bound vs unbound references
- Constructor references
- Overload resolution edge cases

## 12. Best practices
- Use only when clearer
- Avoid when it hides intent
