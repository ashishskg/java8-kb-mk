# map vs flatMap

## 1. Concept explanation
`map` transforms 1->1; `flatMap` transforms 1->many and flattens nested streams.

## 2. Problem statement
Parse user-provided tags and produce a single normalized list of tokens.

## 3. Algorithm intuition
Use map when the output is one value per input. Use flatMap when each input yields multiple values.

ASCII:
map:    Stream<String> -> Stream<String[]>
flatMap:Stream<String> -> Stream<String>

## 4. Java 8 implementation
```java
import java.util.*;

public class MapFlatMapLoop {
    public static void main(String[] args) {
        // E1: split tags by spaces and flatten
        List<String> lines = Arrays.asList("  Java  spring ", "java  ", " ");
        List<String> out1 = new ArrayList<>();
        for (String s : lines) {
            for (String tok : s.split(" ")) {
                String t = tok.trim().toLowerCase();
                if (!t.isEmpty() && !out1.contains(t)) out1.add(t);
            }
        }
        Collections.sort(out1);
        System.out.println("E1=" + out1);

        // E2: map only (keep lists nested)
        List<List<String>> out2 = new ArrayList<>();
        for (String s : lines) {
            List<String> toks = new ArrayList<>();
            for (String tok : s.split(" ")) {
                String t = tok.trim().toLowerCase();
                if (!t.isEmpty()) toks.add(t);
            }
            out2.add(toks);
        }
        System.out.println("E2=" + out2);

        // E3: parse CSV lines to ints (flat)
        List<String> csv = Arrays.asList("1,2", "3", "");
        List<Integer> out3 = new ArrayList<>();
        for (String s : csv) {
            if (s.trim().isEmpty()) continue;
            for (String p : s.split(",")) out3.add(Integer.parseInt(p.trim()));
        }
        System.out.println("E3=" + out3);

        // E4: Optional-like flatten (manual)
        List<String> maybe = Arrays.asList("a", "", "b");
        List<String> out4 = new ArrayList<>();
        for (String s : maybe) {
            String v = s.trim();
            if (!v.isEmpty()) out4.add(v);
        }
        System.out.println("E4=" + out4);

        // E5: map to lengths
        List<Integer> out5 = new ArrayList<>();
        for (String t : out1) out5.add(t.length());
        System.out.println("E5=" + out5);

        // E6: flatMap characters from words
        List<String> words = Arrays.asList("ab", "c");
        List<Character> out6 = new ArrayList<>();
        for (String w : words) {
            for (int i = 0; i < w.length(); i++) out6.add(w.charAt(i));
        }
        System.out.println("E6=" + out6);
    }
}
```

## 5. Stream API implementation
```java
import java.util.*;
import java.util.stream.*;

public class MapFlatMap {
    public static void main(String[] args) {
        List<String> lines = Arrays.asList("  Java  spring ", "java  ", " ");

        // E1: flatMap tokens
        List<String> e1 = lines.stream()
                .flatMap(s -> Arrays.stream(s.split(" ")))
                .map(String::trim)
                .map(String::toLowerCase)
                .filter(t -> !t.isEmpty())
                .distinct()
                .sorted()
                .collect(Collectors.toList());
        System.out.println("E1=" + e1);

        // E2: map keeps nested lists
        List<List<String>> e2 = lines.stream()
                .map(s -> Arrays.stream(s.split(" "))
                        .map(String::trim)
                        .map(String::toLowerCase)
                        .filter(t -> !t.isEmpty())
                        .collect(Collectors.toList()))
                .collect(Collectors.toList());
        System.out.println("E2=" + e2);

        // E3: flat CSV to ints
        List<String> csv = Arrays.asList("1,2", "3", "");
        List<Integer> e3 = csv.stream()
                .map(String::trim)
                .filter(s -> !s.isEmpty())
                .flatMap(s -> Arrays.stream(s.split(",")))
                .map(String::trim)
                .map(Integer::parseInt)
                .collect(Collectors.toList());
        System.out.println("E3=" + e3);

        // E4: flatten optionals (represented as empty strings)
        List<String> maybe = Arrays.asList("a", "", "b");
        List<String> e4 = maybe.stream().map(String::trim).filter(s -> !s.isEmpty()).collect(Collectors.toList());
        System.out.println("E4=" + e4);

        // E5: map to lengths
        System.out.println("E5=" + e1.stream().map(String::length).collect(Collectors.toList()));

        // E6: flatMap characters
        List<String> words = Arrays.asList("ab", "c");
        List<Character> e6 = words.stream()
                .flatMap(w -> w.chars().mapToObj(c -> (char) c))
                .collect(Collectors.toList());
        System.out.println("E6=" + e6);
    }
}
```

## 6. Sample input
- Input: lines=["  Java  spring ", "java  ", " "]
- Input: csv=["1,2","3",""]
- Input: words=["ab","c"]

## 7. Execution steps
- E1: flatMap tokens -> normalize -> distinct -> sort
- E2: map to nested token lists
- E3: flatMap CSV numbers
- E4: filter empties (optional flatten)
- E5: map to lengths
- E6: flatMap characters

## 8. Output
- Output: E1=[java, spring]
- Output: E2=[[java, spring], [java], []]
- Output: E3=[1, 2, 3]
- Output: E4=[a, b]
- Output: E5=[4, 6]
- Output: E6=[a, b, c]

## 9. Time and space complexity
- Time: O(n) for scans; sorting unique tokens adds O(k log k)
- Space: O(k)

## 10. Enterprise relevance
Common in parsing free-text inputs, log normalization, search indexing, and ingestion pipelines.

## 11. Interview discussion points
- flatMap vs map
- flatMap with Optional
- why distinct/sorted are stateful

## 12. Best practices
- Avoid regex split in hot paths
- Normalize at boundaries (trim/case)
- Be aware that distinct/sorted may hold elements in memory
