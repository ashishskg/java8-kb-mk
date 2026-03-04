# Default Methods

## 1. Concept explanation
Interfaces can have default implementations and static utility methods. This enables API evolution without forcing every implementor to change immediately.

Default methods are inherited; if multiple defaults conflict, the implementing class must explicitly override.

## 2. Problem statement
Add a new behavior to an interface in a backward-compatible way and keep callers consistent.

## 3. Algorithm intuition
Use default methods for small shared behavior that logically belongs to the interface.

Use static methods for utilities that support the contract (normalization, parsing, guards).

## 4. Java 8 implementation
```java
interface Auditable {
    default String tag() { return "AUDIT"; }
    static String norm(String s) { return s == null ? "" : s.trim(); }
}

class Order implements Auditable {}

public class InterfaceMethods {
    public static void main(String[] args) {
        System.out.println(new Order().tag());
        System.out.println(Auditable.norm(" x "));
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
- Input: new Order().tag()
- Input: Auditable.norm(" x ")

## 7. Execution steps
- Invoke default method on instance
- Invoke static helper method on interface

## 8. Output
- Output: AUDIT
- Output: x

## 9. Time and space complexity
- N/A (concept)

## 10. Enterprise relevance
Common in library evolution, SPI design, and backward-compatible platform APIs.

## 11. Interview discussion points
- Diamond problem and conflict resolution
- Binary compatibility vs source compatibility
- Interface vs abstract class trade-offs

## 12. Best practices
- Keep default methods small and side-effect free
- Avoid mutable state in interfaces
- Document behavior clearly when adding defaults
