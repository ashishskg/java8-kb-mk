# Stream Pipeline

## 1. Concept explanation
A pipeline is a chain of stages. Intermediate ops are lazy; terminal ops trigger execution.

## 2. Problem statement
Build production-like pipelines for normalization, enrichment, and aggregation.

## 3. Algorithm intuition
Make each stage single-purpose. Keep side effects out of intermediate ops.

## 4. Java 8 implementation
```java
import java.util.*;

public class PipelineLoop {
    public static void main(String[] args) {
        // E1 normalize tags
        List<String> tags = Arrays.asList("  Java ", "JAVA", "", " streams ");
        List<String> out1 = new ArrayList<>();
        for (String t : tags) {
            String v = t.trim().toLowerCase();
            if (!v.isEmpty() && !out1.contains(v)) out1.add(v);
        }
        Collections.sort(out1);
        System.out.println("E1=" + out1);

        // E2 enrich ids->prefix
        int[] ids = {10, 20, 30};
        List<String> out2 = new ArrayList<>();
        for (int id : ids) out2.add("u-" + id);
        System.out.println("E2=" + out2);

        // E3 top-N (manual sort)
        List<Integer> xs = Arrays.asList(5,1,9,2,9);
        List<Integer> tmp = new ArrayList<>(xs);
        Collections.sort(tmp, Collections.reverseOrder());
        List<Integer> top2 = tmp.subList(0, 2);
        System.out.println("E3=" + top2);

        // E4 count by key
        List<String> words = Arrays.asList("a","b","a");
        Map<String, Long> freq = new LinkedHashMap<>();
        for (String w : words) freq.put(w, freq.getOrDefault(w, 0L) + 1L);
        System.out.println("E4=" + freq);

        // E5 anyMatch
        boolean hasRisk = false;
        for (int x : ids) if (x == 20) { hasRisk = true; break; }
        System.out.println("E5=" + hasRisk);

        // E6 join
        System.out.println("E6=" + String.join("|", out1));
    }
}
```

## 5. Stream API implementation
```java
import java.util.*;
import java.util.stream.*;

public class PipelineStream {
    public static void main(String[] args) {
        List<String> tags = Arrays.asList("  Java ", "JAVA", "", " streams ");
        System.out.println("E1=" + tags.stream().map(s -> s.trim().toLowerCase()).filter(s -> !s.isEmpty()).distinct().sorted().collect(Collectors.toList()));

        int[] ids = {10, 20, 30};
        System.out.println("E2=" + IntStream.of(ids).mapToObj(id -> "u-" + id).collect(Collectors.toList()));

        List<Integer> xs = Arrays.asList(5,1,9,2,9);
        System.out.println("E3=" + xs.stream().sorted(Comparator.reverseOrder()).limit(2).collect(Collectors.toList()));

        List<String> words = Arrays.asList("a","b","a");
        System.out.println("E4=" + words.stream().collect(Collectors.groupingBy(w -> w, LinkedHashMap::new, Collectors.counting())));

        System.out.println("E5=" + IntStream.of(ids).anyMatch(x -> x == 20));
        System.out.println("E6=" + tags.stream().map(s -> s.trim().toLowerCase()).filter(s -> !s.isEmpty()).distinct().sorted().collect(Collectors.joining("|")));
    }
}
```

## 6. Sample input
- Input: tags=["  Java ","JAVA",""," streams "]
- Input: ids=[10,20,30]
- Input: words=["a","b","a"]

## 7. Execution steps
- Build pipeline per example
- Terminal op prints E1..E6

## 8. Output
- Output: E1=[java, streams]
- Output: E2=[u-10, u-20, u-30]
- Output: E3=[9, 9]
- Output: E4={a=2, b=1}
- Output: E5=true
- Output: E6=java|streams

## 9. Time and space complexity
- Depends: sort is O(n log n), others often O(n)

## 10. Enterprise relevance
Pipelines are ideal for DTO mapping and in-memory analytics. Be explicit about ordering and memory.

## 11. Interview discussion points
- Laziness
- Fusion
- Why distinct/sorted are stateful

## 12. Best practices
- Avoid side effects
- Use primitive streams
- Prefer LinkedHashMap for deterministic maps
