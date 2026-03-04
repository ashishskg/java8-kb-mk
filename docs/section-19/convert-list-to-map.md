# Convert List to Map

## 1. Concept explanation
Convert a list of objects into a Map keyed by some unique attribute.

## 2. Problem statement
Convert employees list to map by id, handling duplicate ids.

## 3. Algorithm intuition
Use Collectors.toMap with a merge function for duplicates.

## 4. Java 8 implementation
```java
import java.util.*;

public class ListToMapLoop {
    static class Emp { final String id; final String name; Emp(String i,String n){id=i;name=n;} }
    public static void main(String[] args) {
        List<Emp> xs = Arrays.asList(new Emp("e1","amy"), new Emp("e1","amy2"), new Emp("e2","bob"));
        Map<String, String> m = new LinkedHashMap<>();
        for (Emp e : xs) {
            // keep first seen
            m.putIfAbsent(e.id, e.name);
        }
        System.out.println(m);
    }
}
```

## 5. Stream API implementation
```java
import java.util.*;
import java.util.stream.*;

public class ListToMap {
    static class Emp { final String id; final String name; Emp(String i,String n){id=i;name=n;} }
    public static void main(String[] args) {
        List<Emp> xs = Arrays.asList(new Emp("e1","amy"), new Emp("e1","amy2"), new Emp("e2","bob"));
        Map<String, String> m = xs.stream().collect(Collectors.toMap(
                e -> e.id,
                e -> e.name,
                (left, right) -> left,
                LinkedHashMap::new
        ));
        System.out.println(m);
    }
}
```

## 6. Sample input
- Input: [(e1,amy),(e1,amy2),(e2,bob)]

## 7. Execution steps
- Key=id
- Value=name
- Merge duplicates
- Collect

## 8. Output
- Output: {e1=amy, e2=bob}

## 9. Time and space complexity
- Time: O(n)
- Space: O(n)

## 10. Enterprise relevance
Common for building lookup maps and caches; always define collision policy.

## 11. Interview discussion points
- Why toMap needs merge
- Map supplier

## 12. Best practices
- Use LinkedHashMap for deterministic iteration
- Avoid heavy merge functions
