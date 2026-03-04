# Immutability

## 1. Concept explanation
Immutable objects cannot change after construction. They are inherently thread-safe and easier to reason about.

ASCII:
Create -> Use -> Discard (no mutation)

## 2. Problem statement
Design a thread-safe value object used across threads (e.g., DTOs, keys, configs).

## 3. Algorithm intuition
Make fields final, validate in constructor, avoid exposing mutable internals, and use defensive copies.

## 4. Java 8 implementation
```java
import java.util.*;

public final class Config {
    private final String env;
    private final List<String> hosts;

    public Config(String env, List<String> hosts) {
        this.env = env;
        this.hosts = Collections.unmodifiableList(new ArrayList<>(hosts));
    }

    public String env() { return env; }
    public List<String> hosts() { return hosts; }
}
```

## 5. Stream API implementation
```java
import java.util.*;
import java.util.stream.*;

public class ImmutableCollectors {
    public static void main(String[] args) {
        List<String> xs = Arrays.asList("a", "b", "c");
        List<String> imm = xs.stream()
                .collect(Collectors.collectingAndThen(Collectors.toList(), Collections::unmodifiableList));
        System.out.println(imm);
    }
}
```

## 6. Sample input
- Input: env=prod
- Input: hosts=[h1,h2]

## 7. Execution steps
- Copy mutable inputs
- Wrap as unmodifiable
- Expose read-only accessors

## 8. Output
- Output: immutable config/immutable list

## 9. Time and space complexity
- Time: O(n) for defensive copy
- Space: O(n)

## 10. Enterprise relevance
Immutable configs and DTOs reduce concurrency bugs and simplify caching and retries.

## 11. Interview discussion points
- Defensive copying
- Immutability vs unmodifiable
- Thread-safety reasoning

## 12. Best practices
- final fields
- no setters
- defensive copy mutable inputs
- avoid exposing internals
