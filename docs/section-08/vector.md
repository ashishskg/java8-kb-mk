# Vector

## 1. Concept explanation
`Vector` is a legacy synchronized resizable array (pre-Collections framework era). Most methods are synchronized.

Today: prefer `ArrayList` + external synchronization, or concurrent collections depending on requirements.

## 2. Problem statement
Understand why Vector is rarely used in modern Java.

## 3. Algorithm intuition
Coarse-grained synchronization adds overhead and does not automatically make compound actions atomic.

## 4. Java 8 implementation
```java
import java.util.*;

public class VectorDemo {
    public static void main(String[] args) {
        Vector<Integer> v = new Vector<>();
        v.add(1);
        v.add(2);
        System.out.println(v);
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
- Input: add 1,2

## 7. Execution steps
- Create Vector
- Add elements
- Print

## 8. Output
- Output: [1, 2]

## 9. Time and space complexity
- Similar to ArrayList, plus synchronization overhead

## 10. Enterprise relevance
Often appears in legacy code. Modern services typically avoid it unless constrained by old APIs.

## 11. Interview discussion points
- Vector vs ArrayList
- Synchronization semantics
- Why legacy

## 12. Best practices
- Prefer ArrayList
- Use Collections.synchronizedList when needed
- Prefer concurrent collections for high concurrency
