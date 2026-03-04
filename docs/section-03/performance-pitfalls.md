# Common Performance Pitfalls

## 1. Concept explanation
Common JVM performance pitfalls are usually about allocation, boxing, synchronization, and accidental O(n^2) behavior.

ASCII (typical perf loop):
measure -> identify hotspot -> change -> measure again

## 2. Problem statement
Avoid turning a linear transform into O(n^2) or creating excessive garbage.

## 3. Algorithm intuition
Look for nested loops, repeated `contains` on lists, boxing in hot paths, and building large intermediate lists.

## 4. Java 8 implementation
```java
import java.util.*;

public class PitfallContains {
    public static void main(String[] args) {
        List<Integer> a = Arrays.asList(1,2,3,4,5);
        List<Integer> b = Arrays.asList(3,4);

        // O(n*m) pitfall with List.contains
        List<Integer> out = new ArrayList<>();
        for (int x : a) {
            if (b.contains(x)) out.add(x);
        }
        System.out.println(out);

        // Better: HashSet membership
        Set<Integer> bs = new HashSet<>(b);
        List<Integer> out2 = new ArrayList<>();
        for (int x : a) if (bs.contains(x)) out2.add(x);
        System.out.println(out2);
    }
}
```

## 5. Stream API implementation
```java
import java.util.*;
import java.util.stream.*;

public class PitfallStream {
    public static void main(String[] args) {
        List<Integer> a = Arrays.asList(1,2,3,4,5);
        Set<Integer> b = new HashSet<>(Arrays.asList(3,4));
        List<Integer> out = a.stream().filter(b::contains).collect(Collectors.toList());
        System.out.println(out);
    }
}
```

## 6. Sample input
- Input: a=[1,2,3,4,5], b=[3,4]

## 7. Execution steps
- Spot nested contains
- Convert lookup list to HashSet
- Re-measure

## 8. Output
- Output: [3,4]

## 9. Time and space complexity
- Time: O(n*m) pitfall, O(n) with HashSet membership
- Space: O(m)

## 10. Enterprise relevance
This is a classic production regression pattern (latency spikes after small refactors).

## 11. Interview discussion points
- Big-O reasoning
- Allocation and GC
- Profiling approach

## 12. Best practices
- Use sets for membership
- Avoid boxing
- Profile with real data
