# Comparable vs Comparator

## 1. Concept explanation
`Comparable` defines a natural ordering inside the type. `Comparator` defines external/custom orderings.

ASCII:
Comparable: User implements compareTo
Comparator: Comparator<User> byName/byAge

## 2. Problem statement
Sort users by multiple keys (age asc, then name asc) without changing the domain model.

## 3. Algorithm intuition
Use Comparator composition (`comparing`, `thenComparing`) for flexible ordering and stable intent.

## 4. Java 8 implementation
```java
import java.util.*;

class User {
    final String name;
    final int age;
    User(String n, int a){ name=n; age=a; }
    public String toString(){ return name + ":" + age; }
}

public class ComparatorDemo {
    public static void main(String[] args) {
        List<User> users = Arrays.asList(new User("bob", 30), new User("amy", 30), new User("carl", 25));
        users.sort(Comparator.comparingInt((User u) -> u.age).thenComparing(u -> u.name));
        System.out.println(users);
    }
}
```

## 5. Stream API implementation
```java
import java.util.*;
import java.util.stream.*;

public class ComparatorStream {
    static class User { final String name; final int age; User(String n,int a){name=n;age=a;} public String toString(){return name+":"+age;} }
    public static void main(String[] args) {
        List<User> users = Arrays.asList(new User("bob", 30), new User("amy", 30), new User("carl", 25));
        List<User> out = users.stream()
                .sorted(Comparator.comparingInt((User u) -> u.age).thenComparing(u -> u.name))
                .collect(Collectors.toList());
        System.out.println(out);
    }
}
```

## 6. Sample input
- Input: [(bob,30),(amy,30),(carl,25)]

## 7. Execution steps
- Build comparator
- Sort
- Print

## 8. Output
- Output: [carl:25, amy:30, bob:30]

## 9. Time and space complexity
- Time: O(n log n)
- Space: O(n) (if collecting sorted stream)

## 10. Enterprise relevance
Sorting is common in API responses and reports. Comparator composition avoids changing domain classes for one-off sort rules.

## 11. Interview discussion points
- Comparator stability
- compareTo contract
- null handling (nullsFirst/nullsLast)

## 12. Best practices
- Prefer Comparator composition
- Keep ordering consistent with equals when required
- Be explicit about nulls
