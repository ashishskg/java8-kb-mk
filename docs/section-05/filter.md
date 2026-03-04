# filter

## 1. Concept explanation
`filter` keeps elements that match a predicate. In production it’s used for validation, eligibility, and data quality rules.

## 2. Problem statement
Apply multiple real-world filters with deterministic results.

## 3. Algorithm intuition
A good filter predicate is pure, fast, and does not mutate external state.

## 4. Java 8 implementation
```java
import java.util.*;

public class FilterLoop {
    public static void main(String[] args) {
        // E1 even numbers
        List<Integer> xs = Arrays.asList(1,2,3,4,5);
        List<Integer> e1 = new ArrayList<>();
        for (int x : xs) if (x % 2 == 0) e1.add(x);
        System.out.println("E1=" + e1);

        // E2 non-empty trimmed strings
        List<String> raw = Arrays.asList(" a ", "", " b ");
        List<String> e2 = new ArrayList<>();
        for (String s : raw) {
            String v = s.trim();
            if (!v.isEmpty()) e2.add(v);
        }
        System.out.println("E2=" + e2);

        // E3 eligible orders (amount >= 100)
        int[] amounts = {50, 100, 150};
        List<Integer> e3 = new ArrayList<>();
        for (int a : amounts) if (a >= 100) e3.add(a);
        System.out.println("E3=" + e3);

        // E4 whitelist ids
        Set<Integer> allow = new HashSet<>(Arrays.asList(10, 30));
        int[] ids = {10, 20, 30};
        List<Integer> e4 = new ArrayList<>();
        for (int id : ids) if (allow.contains(id)) e4.add(id);
        System.out.println("E4=" + e4);

        // E5 keep first 2 after filter
        List<Integer> e5 = new ArrayList<>();
        for (int x : xs) {
            if (x > 2) {
                e5.add(x);
                if (e5.size() == 2) break;
            }
        }
        System.out.println("E5=" + e5);

        // E6 drop nulls
        List<String> maybe = Arrays.asList("a", null, "b");
        List<String> e6 = new ArrayList<>();
        for (String s : maybe) if (s != null) e6.add(s);
        System.out.println("E6=" + e6);
    }
}
```

## 5. Stream API implementation
```java
import java.util.*;
import java.util.stream.*;

public class FilterStream {
    public static void main(String[] args) {
        System.out.println("E1=" + Arrays.asList(1,2,3,4,5).stream().filter(x -> x % 2 == 0).collect(Collectors.toList()));
        System.out.println("E2=" + Arrays.asList(" a ", "", " b ").stream().map(String::trim).filter(s -> !s.isEmpty()).collect(Collectors.toList()));
        System.out.println("E3=" + IntStream.of(50,100,150).filter(a -> a >= 100).boxed().collect(Collectors.toList()));

        Set<Integer> allow = new HashSet<>(Arrays.asList(10, 30));
        System.out.println("E4=" + IntStream.of(10,20,30).filter(allow::contains).boxed().collect(Collectors.toList()));
        System.out.println("E5=" + Arrays.asList(1,2,3,4,5).stream().filter(x -> x > 2).limit(2).collect(Collectors.toList()));
        System.out.println("E6=" + Arrays.asList("a", null, "b").stream().filter(Objects::nonNull).collect(Collectors.toList()));
    }
}
```

## 6. Sample input
- Input: xs=[1,2,3,4,5]
- Input: raw=[" a ",""," b "]
- Input: amounts=[50,100,150]

## 7. Execution steps
- Define predicate
- filter
- collect/terminal op prints E1..E6

## 8. Output
- Output: E1=[2, 4]
- Output: E2=[a, b]
- Output: E3=[100, 150]
- Output: E4=[10, 30]
- Output: E5=[3, 4]
- Output: E6=[a, b]

## 9. Time and space complexity
- Time: O(n) (per pipeline)
- Space: O(n) if collected

## 10. Enterprise relevance
Filtering is ubiquitous in request validation, fraud checks, and ETL. Keep predicates pure and cheap.

## 11. Interview discussion points
- Predicate purity
- limit short-circuit
- null handling

## 12. Best practices
- Avoid side effects
- Prefer method references
- Use Objects::nonNull
