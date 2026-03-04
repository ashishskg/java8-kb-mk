# collect

## 1. Concept explanation
`collect` performs a mutable reduction (e.g., toList, groupingBy).

## 2. Problem statement
Build common enterprise containers (lists, sets, maps, grouping) using collectors safely.

## 3. Algorithm intuition
Collector defines supplier/accumulator/combiner/finisher.

In production, `Collectors.toMap` often needs a merge function to decide what to do on duplicates.

## 4. Java 8 implementation
```java
import java.util.*;

public class CollectLoop {
    static class User { final String id; final String name; User(String i, String n){ id=i; name=n; } }

    public static void main(String[] args) {
        List<User> users = Arrays.asList(new User("u1","amy"), new User("u1","amy2"), new User("u2","bob"));
        List<Integer> xs = Arrays.asList(1,2,2,3);

        // E1 toList (copy)
        List<Integer> e1 = new ArrayList<>();
        for (int x : xs) e1.add(x);
        System.out.println("E1=" + e1);

        // E2 toSet (dedupe)
        Set<Integer> e2 = new LinkedHashSet<>();
        for (int x : xs) e2.add(x);
        System.out.println("E2=" + e2);

        // E3 toMap (id->name, keep first)
        Map<String, String> e3 = new LinkedHashMap<>();
        for (User u : users) e3.putIfAbsent(u.id, u.name);
        System.out.println("E3=" + e3);

        // E4 groupingBy dept (manual)
        class Emp { String d; String n; Emp(String d,String n){this.d=d;this.n=n;} }
        List<Emp> emps = Arrays.asList(new Emp("ENG","amy"), new Emp("ENG","bob"), new Emp("HR","carl"));
        Map<String, List<String>> e4 = new LinkedHashMap<>();
        for (Emp e : emps) e4.computeIfAbsent(e.d, k -> new ArrayList<>()).add(e.n);
        System.out.println("E4=" + e4);

        // E5 joining
        String e5 = "";
        for (String u : Arrays.asList("a","b","c")) e5 += u;
        System.out.println("E5=" + e5);

        // E6 partitioning (even/odd)
        Map<Boolean, List<Integer>> e6 = new LinkedHashMap<>();
        e6.put(true, new ArrayList<>());
        e6.put(false, new ArrayList<>());
        for (int x : xs) e6.get(x % 2 == 0).add(x);
        System.out.println("E6=" + e6);
    }
}
```

## 5. Stream API implementation
```java
import java.util.*;
import java.util.stream.*;

public class CollectToMap {
    static class User { final String id; final String name; User(String i, String n){ id=i; name=n; } }
    public static void main(String[] args) {
        List<User> users = Arrays.asList(new User("u1","amy"), new User("u1","amy2"), new User("u2","bob"));
        List<Integer> xs = Arrays.asList(1,2,2,3);

        System.out.println("E1=" + xs.stream().collect(Collectors.toList()));
        System.out.println("E2=" + xs.stream().collect(Collectors.toCollection(LinkedHashSet::new)));
        System.out.println("E3=" + users.stream().collect(Collectors.toMap(u -> u.id, u -> u.name, (l,r) -> l, LinkedHashMap::new)));

        class Emp { final String d; final String n; Emp(String d,String n){this.d=d;this.n=n;} }
        List<Emp> emps = Arrays.asList(new Emp("ENG","amy"), new Emp("ENG","bob"), new Emp("HR","carl"));
        System.out.println("E4=" + emps.stream().collect(Collectors.groupingBy(e -> e.d, LinkedHashMap::new, Collectors.mapping(e -> e.n, Collectors.toList()))));

        System.out.println("E5=" + Stream.of("a","b","c").collect(Collectors.joining("")));
        System.out.println("E6=" + xs.stream().collect(Collectors.partitioningBy(x -> x % 2 == 0)));
    }
}
```

## 6. Sample input
- Input: xs=[1,2,2,3]
- Input: users=[(u1,amy),(u1,amy2),(u2,bob)]
- Input: emps=[(ENG,amy),(ENG,bob),(HR,carl)]

## 7. Execution steps
- E1..E6 collectors
- Print deterministic maps using LinkedHashMap where needed

## 8. Output
- Output: E1=[1, 2, 2, 3]
- Output: E2=[1, 2, 3]
- Output: E3={u1=amy, u2=bob}
- Output: E4={ENG=[amy, bob], HR=[carl]}
- Output: E5=abc
- Output: E6={false=[1, 3], true=[2, 2]}

## 9. Time and space complexity
- Time: O(n)
- Space: O(n)

## 10. Enterprise relevance
Used for lookup maps, grouping/reporting, and response shaping; always define collision policy for keys.

## 11. Interview discussion points
- collect vs reduce
- collector combiner
- toMap merge function

## 12. Best practices
- Always provide merge for toMap when duplicates are possible
- Prefer immutable at boundaries
