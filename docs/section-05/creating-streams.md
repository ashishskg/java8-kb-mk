# Creating Streams

## 1. Concept explanation
Common ways to create streams: collections, arrays, Stream.of, builder, generate/iterate, file/lines (IO).

## 2. Problem statement
Create streams from multiple sources and produce deterministic results.

## 3. Algorithm intuition
Choose the correct source; avoid infinite streams without limit.

## 4. Java 8 implementation
```java
import java.util.*;

public class CreatingStreamsLoop {
    public static void main(String[] args) {
        // E1: list
        List<Integer> xs = Arrays.asList(1,2,3);
        System.out.println("E1=" + xs);
        // E2: array
        int[] a = {1,2,3};
        System.out.println("E2=" + Arrays.toString(a));
        // E3: varargs
        System.out.println("E3=" + Arrays.asList("a","b"));
        // E4: map entrySet loop
        Map<String,Integer> m = new LinkedHashMap<>(); m.put("a",1); m.put("b",2);
        List<String> pairs = new ArrayList<>();
        for (Map.Entry<String,Integer> e : m.entrySet()) pairs.add(e.getKey() + "=" + e.getValue());
        System.out.println("E4=" + pairs);
        // E5: range (manual)
        List<Integer> r = new ArrayList<>();
        for (int i=1;i<=5;i++) r.add(i);
        System.out.println("E5=" + r);
        // E6: generate (manual)
        List<Integer> gen = new ArrayList<>();
        for (int i=0;i<5;i++) gen.add(7);
        System.out.println("E6=" + gen);
    }
}
```

## 5. Stream API implementation
```java
import java.util.*;
import java.util.stream.*;

public class CreatingStreams {
    public static void main(String[] args) {
        System.out.println("E1=" + Arrays.asList(1,2,3).stream().collect(Collectors.toList()));
        System.out.println("E2=" + IntStream.of(1,2,3).boxed().collect(Collectors.toList()));
        System.out.println("E3=" + Stream.of("a","b").collect(Collectors.toList()));

        Map<String,Integer> m = new LinkedHashMap<>(); m.put("a",1); m.put("b",2);
        System.out.println("E4=" + m.entrySet().stream().map(e -> e.getKey() + "=" + e.getValue()).collect(Collectors.toList()));

        System.out.println("E5=" + IntStream.rangeClosed(1,5).boxed().collect(Collectors.toList()));
        System.out.println("E6=" + Stream.generate(() -> 7).limit(5).collect(Collectors.toList()));
    }
}
```

## 6. Sample input
- Input: [1,2,3]
- Input: map={a=1,b=2}
- Input: range 1..5

## 7. Execution steps
- Create source
- Stream it
- Collect/print E1..E6

## 8. Output
- Output: E1=[1, 2, 3]
- Output: E2=[1, 2, 3]
- Output: E3=[a, b]
- Output: E4=[a=1, b=2]
- Output: E5=[1, 2, 3, 4, 5]
- Output: E6=[7, 7, 7, 7, 7]

## 9. Time and space complexity
- Mostly O(n)
- Space: O(n) if collected

## 10. Enterprise relevance
Creating streams is easy; controlling size/backpressure is the hard part. Avoid infinite streams without `limit()`.

## 11. Interview discussion points
- Stream.generate vs iterate
- range vs rangeClosed
- boxing costs

## 12. Best practices
- Prefer primitive streams
- Use LinkedHashMap when order matters
- Avoid creating streams in tight loops
