# Group Employees by Department

## 1. Concept explanation
Use groupingBy to partition items by a key and collect grouped values.

## 2. Problem statement
Group employees by department and list names.

## 3. Algorithm intuition
groupingBy(dept, mapping(name, toList())) gives one-pass grouping.

## 4. Java 8 implementation
```java
import java.util.*;

public class GroupByDeptLoop {
    static class Emp { final String dept; final String name; Emp(String d,String n){dept=d;name=n;} }

    public static void main(String[] args) {
        List<Emp> emps = Arrays.asList(new Emp("ENG","amy"), new Emp("ENG","bob"), new Emp("HR","carl"));
        Map<String, List<String>> byDept = new LinkedHashMap<>();
        for (Emp e : emps) {
            byDept.computeIfAbsent(e.dept, k -> new ArrayList<>()).add(e.name);
        }
        System.out.println(byDept);
    }
}
```

## 5. Stream API implementation
```java
import java.util.*;
import java.util.stream.*;

public class GroupByDept {
    static class Emp { final String dept; final String name; Emp(String d,String n){dept=d;name=n;} }
    public static void main(String[] args) {
        List<Emp> emps = Arrays.asList(new Emp("ENG","amy"), new Emp("ENG","bob"), new Emp("HR","carl"));
        Map<String, List<String>> byDept = emps.stream().collect(
                Collectors.groupingBy(e -> e.dept, Collectors.mapping(e -> e.name, Collectors.toList()))
        );
        System.out.println(byDept);
    }
}
```

## 6. Sample input
- Input: [(ENG,amy),(ENG,bob),(HR,carl)]

## 7. Execution steps
- groupingBy dept
- downstream mapping(name)
- collect

## 8. Output
- Output: {ENG=[amy, bob], HR=[carl]}

## 9. Time and space complexity
- Time: O(n)
- Space: O(n)

## 10. Enterprise relevance
Used in org charts, reporting, and building response DTOs.

## 11. Interview discussion points
- groupingBy vs partitioningBy
- downstream collectors

## 12. Best practices
- Use LinkedHashMap supplier for deterministic ordering when needed
- Avoid grouping huge datasets in memory
