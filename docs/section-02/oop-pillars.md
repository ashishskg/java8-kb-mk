# OOP Pillars (Encapsulation, Inheritance, Polymorphism, Abstraction)

## 1. Concept explanation
OOP pillars are the core design tools for building maintainable systems:

- Encapsulation: hide invariants behind methods
- Inheritance: reuse behavior (use sparingly)
- Polymorphism: program to interfaces
- Abstraction: model domain concepts

ASCII:
Service -> Interface -> Implementation

## 2. Problem statement
Model a domain type with validation and a stable interface boundary.

## 3. Algorithm intuition
Encapsulation keeps invariants local; polymorphism decouples call sites from implementations.

## 4. Java 8 implementation
```java
interface PaymentGateway {
    boolean charge(String accountId, int cents);
}

class StripeGateway implements PaymentGateway {
    public boolean charge(String accountId, int cents) { return true; }
}

final class Money {
    private final int cents;
    Money(int cents) {
        if (cents < 0) throw new IllegalArgumentException("cents");
        this.cents = cents;
    }
    int cents() { return cents; }
}
```

## 5. Stream API implementation
```java
import java.util.*;
import java.util.stream.*;

public class OopStreamExample {
    static class User { final String role; User(String r){ role=r; } }
    public static void main(String[] args) {
        List<User> users = Arrays.asList(new User("ADMIN"), new User("USER"));
        long admins = users.stream().filter(u -> "ADMIN".equals(u.role)).count();
        System.out.println(admins);
    }
}
```

## 6. Sample input
- Input: cents = 1200
- Input: users roles = [ADMIN, USER]

## 7. Execution steps
- Validate invariants in constructor
- Program to interface
- Count via stream filter

## 8. Output
- Output: Money created
- Output: admins = 1

## 9. Time and space complexity
- Time: O(n) for stream filter
- Space: O(1) extra

## 10. Enterprise relevance
These principles reduce coupling and allow swapping implementations (e.g., gateways, repositories) without rewriting callers.

## 11. Interview discussion points
- Composition vs inheritance
- Interface-driven design
- Immutability and invariants

## 12. Best practices
- Prefer composition
- Keep classes small
- Hide invariants
- Program to interfaces
