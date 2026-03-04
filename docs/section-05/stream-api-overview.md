# Stream API Overview

## 1. Concept explanation
Streams are *lazy pipelines* over a data source. You build a pipeline with intermediate ops, and it runs when you call a terminal op.

This page gives a quick production-oriented overview with multiple examples you’ll see in services and batch jobs.

## 2. Problem statement
Implement common real-world transformations and aggregations using Stream API.

## 3. Algorithm intuition
Think in stages: source -> (0..n intermediate ops) -> terminal. Keep lambdas pure and output deterministic.

## 4. Java 8 implementation
```java
import java.util.*;

public class StreamOverviewLoop {
    public static void main(String[] args) {
        // Example 1: filter + distinct + sort
        List<String> names = Arrays.asList("amy", "bob", "carl", "bob");
        List<String> out1 = new ArrayList<>();
        for (String n : names) {
            if (n.length() >= 3 && !out1.contains(n)) out1.add(n);
        }
        Collections.sort(out1);
        System.out.println("E1=" + out1);

        // Example 2: map (normalize)
        List<String> raw = Arrays.asList("  Foo ", "BAR", "");
        List<String> out2 = new ArrayList<>();
        for (String s : raw) {
            String v = s.trim().toLowerCase();
            if (!v.isEmpty()) out2.add(v);
        }
        System.out.println("E2=" + out2);

        // Example 3: sum
        int[] a = {1, 2, 3, 4, 5};
        int sum = 0;
        for (int x : a) sum += x;
        System.out.println("E3=" + sum);

        // Example 4: grouping (dept -> names)
        class Emp { String d; String n; Emp(String d,String n){this.d=d;this.n=n;} }
        List<Emp> emps = Arrays.asList(new Emp("ENG","amy"), new Emp("ENG","bob"), new Emp("HR","carl"));
        Map<String, List<String>> byDept = new LinkedHashMap<>();
        for (Emp e : emps) {
            byDept.computeIfAbsent(e.d, k -> new ArrayList<>()).add(e.n);
        }
        System.out.println("E4=" + byDept);

        // Example 5: first match
        Integer firstGt3 = null;
        for (int x : a) { if (x > 3) { firstGt3 = x; break; } }
        System.out.println("E5=" + firstGt3);

        // Example 6: join strings
        String joined = "";
        for (int i = 0; i < out1.size(); i++) {
            if (i > 0) joined += ",";
            joined += out1.get(i);
        }
        System.out.println("E6=" + joined);
    }
}
```

## 5. Stream API implementation
```java
import java.util.*;
import java.util.stream.*;

public class StreamOverview {
    static class Emp { final String dept; final String name; Emp(String d,String n){dept=d;name=n;} }

    public static void main(String[] args) {
        List<String> names = Arrays.asList("amy", "bob", "carl", "bob");
        System.out.println("E1=" + names.stream().filter(n -> n.length() >= 3).distinct().sorted().collect(Collectors.toList()));

        List<String> raw = Arrays.asList("  Foo ", "BAR", "");
        System.out.println("E2=" + raw.stream().map(s -> s.trim().toLowerCase()).filter(s -> !s.isEmpty()).collect(Collectors.toList()));

        int[] a = {1, 2, 3, 4, 5};
        System.out.println("E3=" + IntStream.of(a).sum());

        List<Emp> emps = Arrays.asList(new Emp("ENG","amy"), new Emp("ENG","bob"), new Emp("HR","carl"));
        System.out.println("E4=" + emps.stream().collect(Collectors.groupingBy(e -> e.dept, LinkedHashMap::new, Collectors.mapping(e -> e.name, Collectors.toList()))));

        System.out.println("E5=" + IntStream.of(a).filter(x -> x > 3).findFirst().orElse(-1));

        System.out.println("E6=" + names.stream().distinct().sorted().collect(Collectors.joining(",")));
    }
}
```

## 6. Sample input
- Input: names=["amy","bob","carl","bob"]
- Input: raw=["  Foo ","BAR",""]
- Input: a=[1,2,3,4,5]

## 7. Execution steps
- Build pipelines
- Run terminal ops
- Print E1..E6

## 8. Output
- Output: E1=[amy, bob, carl]
- Output: E2=[foo, bar]
- Output: E3=15
- Output: E4={ENG=[amy, bob], HR=[carl]}
- Output: E5=4
- Output: E6=amy,bob,carl

## 9. Time and space complexity
- Depends on ops: many are O(n); sorting is O(n log n)
- Space: O(n)

## 10. Enterprise relevance
Streams are great for in-memory mapping/aggregation. Don’t stream huge datasets without chunking/backpressure.

## 11. Interview discussion points
- Lazy evaluation
- Intermediate vs terminal
- Stateful ops (sorted/distinct)
- When NOT to use streams

## 12. Best practices
- Keep lambdas pure
- Prefer primitive streams
- Avoid collecting huge lists
- Use LinkedHashMap supplier when order matters
