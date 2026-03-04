# Abstract Class vs Interface

## 1. Concept explanation
Interfaces define capabilities (contracts). Abstract classes share state and partial implementations.

Java 8 interfaces can have default/static methods, but they still should not own mutable instance state.

## 2. Problem statement
Design an API where multiple implementations share some logic but must enforce a contract.

## 3. Algorithm intuition
Use interface for capability; use abstract class when you need shared state/constructor logic.

## 4. Java 8 implementation
```java
interface Serializer<T> {
    String serialize(T t);
}

abstract class BaseJsonSerializer<T> implements Serializer<T> {
    protected String quote(String s) { return "\"" + s + "\""; }
}

class User { final String name; User(String n){ name=n; } }

class UserSerializer extends BaseJsonSerializer<User> {
    public String serialize(User u) { return "{\"name\":" + quote(u.name) + "}"; }
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
- Input: User(name=amy)

## 7. Execution steps
- Define contract interface
- Share helper in abstract base
- Implement serialize

## 8. Output
- Output: {"name":"amy"}

## 9. Time and space complexity
- N/A (concept)

## 10. Enterprise relevance
Important for SDK/library design and service boundaries (SPI/API separation).

## 11. Interview discussion points
- Multiple inheritance of type via interfaces
- Default methods vs abstract methods

## 12. Best practices
- Prefer interface-first
- Avoid deep inheritance
- Keep base classes small
