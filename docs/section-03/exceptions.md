# Exceptions (Checked vs Unchecked)

## 1. Concept explanation
Checked exceptions must be declared/handled; unchecked exceptions (RuntimeException) do not.

Production guidance: use checked exceptions for recoverable cases at boundaries, unchecked for programmer errors.

## 2. Problem statement
Design error handling for an API that can fail due to validation vs system failures.

## 3. Algorithm intuition
Use exception types to encode recoverability and to separate validation errors from infrastructure failures.

## 4. Java 8 implementation
```java
class ValidationException extends Exception {
    ValidationException(String msg) { super(msg); }
}

public class ExceptionsDemo {
    static int parseAge(String s) throws ValidationException {
        try {
            int n = Integer.parseInt(s);
            if (n < 0) throw new ValidationException("age");
            return n;
        } catch (NumberFormatException e) {
            throw new ValidationException("not a number");
        }
    }

    public static void main(String[] args) {
        try {
            System.out.println(parseAge("12"));
        } catch (ValidationException e) {
            System.out.println("BAD_REQUEST");
        }
    }
}
```

## 5. Stream API implementation
```java
import java.util.*;
import java.util.stream.*;

public class ExceptionInStreamNote {
    public static void main(String[] args) {
        // Avoid throwing checked exceptions inside stream lambdas.
        // Prefer mapping to Either-like result or pre-validate.
    }
}
```

## 6. Sample input
- Input: "12"

## 7. Execution steps
- Parse
- Validate
- Return or throw

## 8. Output
- Output: 12

## 9. Time and space complexity
- N/A (concept)

## 10. Enterprise relevance
Exception taxonomy drives API error mapping (400 vs 500), retries, and observability (error rates).

## 11. Interview discussion points
- When to use checked
- finally semantics
- try-with-resources

## 12. Best practices
- Don’t swallow exceptions
- Add context
- Preserve cause
- Avoid exceptions for control flow
