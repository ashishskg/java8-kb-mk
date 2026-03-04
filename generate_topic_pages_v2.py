from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import re
import textwrap


@dataclass(frozen=True)
class PageSpec:
    rel_path: str
    title: str


TEMPLATE = """# {title}

## 1. Concept explanation
{concept}

## 2. Problem statement
{problem}

## 3. Algorithm intuition
{intuition}

## 4. Java 8 implementation
```java
{java_impl}
```

## 5. Stream API implementation
```java
{stream_impl}
```

## 6. Sample input
{sample_input}

## 7. Execution steps
{execution_steps}

## 8. Output
{output}

## 9. Time and space complexity
{complexity}

## 10. Enterprise relevance
{enterprise}

## 11. Interview discussion points
{interview}

## 12. Best practices
{best_practices}
"""


def bullets(*items: str) -> str:
    return "\n".join(f"- {x}" for x in items)


def render(
    title: str,
    *,
    concept: str,
    problem: str,
    intuition: str,
    java_impl: str,
    stream_impl: str,
    sample_input: str,
    execution_steps: str,
    output: str,
    complexity: str,
    enterprise: str,
    interview: str,
    best_practices: str,
) -> str:
    return TEMPLATE.format(
        title=title,
        concept=concept,
        problem=problem,
        intuition=intuition,
        java_impl=java_impl.strip(),
        stream_impl=stream_impl.strip(),
        sample_input=sample_input,
        execution_steps=execution_steps,
        output=output,
        complexity=complexity,
        enterprise=enterprise,
        interview=interview,
        best_practices=best_practices,
    )


GEN_JAVA = textwrap.dedent(
    """\
    import java.util.*;

    public class Example {
        public static void main(String[] args) {
            List<Integer> xs = Arrays.asList(1, 2, 3, 4, 5);
            int sum = 0;
            for (int x : xs) sum += x;
            System.out.println(sum);
        }
    }
    """
)


def title_stream_api_cheatsheet() -> str:
    return textwrap.dedent(
        """\
        ## 1. Stream API essentials (with output)

        ### 1.1 filter, map, flatMap

        ```java
        List<String> list = List.of("apple", "banana", "apricot", "berry");
        List<String> filtered = list.stream()
                .filter(s -> s.startsWith("a"))
                .collect(Collectors.toList());
        // filtered = [apple, apricot]

        List<Integer> lengths = list.stream()
                .map(String::length)
                .collect(Collectors.toList());
        // lengths = [5, 6, 7, 5]

        List<List<Integer>> nested = List.of(List.of(1, 2), List.of(3, 4), List.of(5));
        List<Integer> flat = nested.stream()
                .flatMap(List::stream)
                .collect(Collectors.toList());
        // flat = [1, 2, 3, 4, 5]
        ```

        **Output:** `filtered = [apple, apricot]`, `lengths = [5, 6, 7, 5]`, `flat = [1, 2, 3, 4, 5]`

        ---

        ### 1.2 distinct, sorted, limit, skip

        ```java
        List<Integer> list = List.of(3, 1, 2, 1, 3);
        List<Integer> distinct = list.stream().distinct().collect(Collectors.toList());
        List<Integer> sorted = list.stream().sorted().collect(Collectors.toList());
        List<Integer> limited = list.stream().limit(2).collect(Collectors.toList());
        List<Integer> skipped = list.stream().skip(2).collect(Collectors.toList());
        ```

        **Output:** `distinct = [3, 1, 2]`, `sorted = [1, 1, 2, 3, 3]`, `limited = [3, 1]`, `skipped = [2, 1, 3]`

        ---

        ### 1.3 reduce (with and without identity)

        ```java
        List<Integer> list = List.of(1, 2, 3, 4, 5);
        Optional<Integer> sumOpt = list.stream().reduce(Integer::sum);
        Integer sumWithIdentity = list.stream().reduce(0, Integer::sum);
        Optional<Integer> product = list.stream().reduce((a, b) -> a * b);
        ```

        **Output:** `sumOpt = Optional[15]`, `sumWithIdentity = 15`, `product = Optional[120]`

        ---

        ### 1.4 collect: toList, toSet, toMap, joining, groupingBy, partitioningBy

        ```java
        List<String> list = List.of("a", "b", "c");
        List<String> toList = list.stream().collect(Collectors.toList());
        Set<String> toSet = list.stream().collect(Collectors.toSet());
        Map<String, Integer> toMap = list.stream()
                .collect(Collectors.toMap(Function.identity(), String::length));
        String joined = list.stream().collect(Collectors.joining(", "));

        List<String> words = List.of("apple", "banana", "apricot");
        Map<Character, List<String>> byFirst = words.stream()
                .collect(Collectors.groupingBy(s -> s.charAt(0)));
        Map<Boolean, List<Integer>> evensOdds = List.of(1, 2, 3, 4, 5).stream()
                .collect(Collectors.partitioningBy(n -> n % 2 == 0));
        ```

        **Output:** `toList = [a, b, c]`, `toSet = [a, b, c]`, `toMap = {a=1, b=1, c=1}`, `joined = "a, b, c"`, `byFirst = {a=[apple, apricot], b=[banana]}`, `evensOdds = {false=[1, 3, 5], true=[2, 4]}`

        ---

        ### 1.5 Optional: findFirst, findAny, max, min

        ```java
        List<String> list = List.of("a", "bb", "ccc", "dd");
        Optional<String> first = list.stream().filter(s -> s.length() > 1).findFirst();
        Optional<String> any = list.stream().filter(s -> s.length() > 1).findAny();
        Optional<String> maxLen = list.stream().max(Comparator.comparingInt(String::length));
        Optional<String> minLen = list.stream().min(Comparator.comparingInt(String::length));
        ```

        **Output:** `first = Optional[bb]`, `any = Optional[bb]` (or another length>1), `maxLen = Optional[ccc]`, `minLen = Optional[a]`

        ---

        ### 1.6 Primitive streams: IntStream.range, mapToInt, sum

        ```java
        List<Integer> range = IntStream.range(0, 5).boxed().collect(Collectors.toList());
        int sum = IntStream.range(1, 6).sum();
        List<String> words = List.of("a", "bb", "ccc");
        int totalChars = words.stream().mapToInt(String::length).sum();
        ```

        **Output:** `range = [0, 1, 2, 3, 4]`, `sum = 15`, `totalChars = 6`

        ---

        ## 2. Conversions (with output)

        ### 2.1 List → Map (element as key, index as value)

        ```java
        List<String> list = List.of("apple", "banana", "mango");
        Map<String, Integer> indexMap = IntStream.range(0, list.size())
                .boxed()
                .collect(Collectors.toMap(list::get, i -> i));
        ```

        **Output:** `{apple=0, banana=1, mango=2}`

        ---

        ### 2.2 List → Map with duplicate-key merge

        ```java
        List<String> list = List.of("a", "b", "a", "c", "b");
        Map<String, Long> count = list.stream()
                .collect(Collectors.toMap(Function.identity(), v -> 1L, Long::sum));
        ```

        **Output:** `{a=2, b=2, c=1}`

        ---

        ### 2.3 Map → List (keys, values, entries, keys sorted by value)

        ```java
        Map<String, Integer> map = new HashMap<>(Map.of("apple", 30, "banana", 10, "mango", 20));
        List<String> keys = new ArrayList<>(map.keySet());
        List<Integer> values = new ArrayList<>(map.values());
        List<String> keysByValue = map.entrySet().stream()
                .sorted(Map.Entry.comparingByValue())
                .map(Map.Entry::getKey)
                .collect(Collectors.toList());
        ```

        **Output:** `keys = [apple, banana, mango]` (order may vary), `values = [30, 10, 20]`, `keysByValue = [banana, mango, apple]`

        ---

        ### 2.4 flatMap: list of lists → single list; string → words/chars

        ```java
        List<List<Integer>> lists = List.of(List.of(1, 2), List.of(3, 4), List.of(5));
        List<Integer> flat = lists.stream().flatMap(List::stream).collect(Collectors.toList());

        String sentence = "hello world";
        List<String> words = Arrays.stream(sentence.split("\\s+")).collect(Collectors.toList());
        List<String> chars = sentence.chars()
                .mapToObj(c -> String.valueOf((char) c))
                .collect(Collectors.toList());
        ```

        **Output:** `flat = [1, 2, 3, 4, 5]`, `words = [hello, world]`, `chars = [h, e, l, l, o,  , w, o, r, l, d]`

        ---

        ## 3. General interview examples (with output)

        ### 3.1 Count frequency (list and string)

        ```java
        List<String> list = List.of("a", "b", "a", "c", "b", "a");
        Map<String, Long> freqList = list.stream()
                .collect(Collectors.groupingBy(Function.identity(), Collectors.counting()));
        // {a=3, b=2, c=1}

        String s = "hello";
        Map<Character, Long> freqStr = s.chars()
                .mapToObj(c -> (char) c)
                .collect(Collectors.groupingBy(Function.identity(), Collectors.counting()));
        // {h=1, e=1, l=2, o=1}
        ```

        **Output:** `freqList = {a=3, b=2, c=1}`, `freqStr = {h=1, e=1, l=2, o=1}`

        ---

        ### 3.2 First non-repeated character

        ```java
        List<String> list = List.of("a", "b", "a", "c", "b");
        Optional<String> first = list.stream()
                .collect(Collectors.groupingBy(Function.identity(), Collectors.counting()))
                .entrySet().stream()
                .filter(e -> e.getValue() == 1)
                .map(Map.Entry::getKey)
                .findFirst();
        ```

        **Output:** `Optional[c]`

        ---

        ### 3.3 Sort by frequency then by value

        ```java
        List<String> list = List.of("a", "b", "a", "c", "b", "a");
        Map<String, Long> freq = list.stream()
                .collect(Collectors.groupingBy(Function.identity(), Collectors.counting()));
        List<String> sorted = list.stream()
                .distinct()
                .sorted(Comparator.comparing(freq::get).reversed().thenComparing(Function.identity()))
                .collect(Collectors.toList());
        ```

        **Output:** `[a, b, c]` (a=3, b=2, c=1)

        ---

        ### 3.4 Two lists → Map

        ```java
        List<String> keys = List.of("a", "b", "c");
        List<Integer> values = List.of(1, 2, 3);
        Map<String, Integer> map = IntStream.range(0, keys.size())
                .boxed()
                .collect(Collectors.toMap(keys::get, values::get));
        ```

        **Output:** `{a=1, b=2, c=3}`

        ---

        ### 3.5 Chunk list into sublists of size n

        ```java
        List<Integer> list = List.of(1, 2, 3, 4, 5, 6);
        int chunkSize = 2;
        List<List<Integer>> chunks = IntStream.range(0, (list.size() + chunkSize - 1) / chunkSize)
                .mapToObj(i -> list.subList(i * chunkSize, Math.min((i + 1) * chunkSize, list.size())))
                .collect(Collectors.toList());
        ```

        **Output:** `[[1, 2], [3, 4], [5, 6]]`

        ---

        ### 3.6 Remove duplicates preserving order

        ```java
        List<String> list = List.of("a", "b", "a", "c", "b");
        List<String> distinct = list.stream().distinct().collect(Collectors.toList());
        ```

        **Output:** `[a, b, c]`

        ---

        ### 3.7 Second largest / nth element

        ```java
        List<Integer> list = List.of(5, 2, 8, 1, 9);
        Optional<Integer> secondLargest = list.stream()
                .sorted(Comparator.reverseOrder())
                .skip(1)
                .findFirst();
        ```

        **Output:** `Optional[8]`

        ---

        ### 3.8 Partition by predicate (evens/odds)

        ```java
        List<Integer> list = List.of(1, 2, 3, 4, 5);
        Map<Boolean, List<Integer>> partition = list.stream()
                .collect(Collectors.partitioningBy(n -> n % 2 == 0));
        List<Integer> evens = partition.get(true);   // [2, 4]
        List<Integer> odds = partition.get(false);   // [1, 3, 5]
        ```

        **Output:** `evens = [2, 4]`, `odds = [1, 3, 5]`

        ---

        ### 3.9 Group anagrams

        ```java
        List<String> words = List.of("eat", "tea", "tan", "ate", "nat", "bat");
        Map<String, List<String>> anagrams = words.stream()
                .collect(Collectors.groupingBy(word -> {
                    char[] chars = word.toCharArray();
                    Arrays.sort(chars);
                    return new String(chars);
                }));
        ```

        **Output:** `{aet=[eat, tea, ate], ant=[tan, nat], abt=[bat]}`

        ---

        ### 3.10 Two Sum (indices)

        ```java
        int[] nums = {2, 7, 11, 15};
        int target = 9;
        Map<Integer, Integer> map = new HashMap<>();
        int[] result = {-1, -1};
        for (int i = 0; i < nums.length; i++) {
            int complement = target - nums[i];
            if (map.containsKey(complement)) {
                result[0] = map.get(complement);
                result[1] = i;
                break;
            }
            map.put(nums[i], i);
        }
        // result = [0, 1]
        ```

        **Output:** `result = [0, 1]` (indices of 2 and 7)

        ---

        ### 3.11 Merge two maps (sum values for same key)

        ```java
        Map<String, Integer> map1 = new HashMap<>(Map.of("a", 1, "b", 2));
        Map<String, Integer> map2 = new HashMap<>(Map.of("b", 3, "c", 4));
        Map<String, Integer> merged = Stream.concat(map1.entrySet().stream(), map2.entrySet().stream())
                .collect(Collectors.toMap(Map.Entry::getKey, Map.Entry::getValue, Integer::sum));
        ```

        **Output:** `{a=1, b=5, c=4}`

        ---

        ## 4. String operations (with output)

        ### 4.1 Search: contains, indexOf, lastIndexOf, stream findFirst

        ```java
        String text = "hello world";
        boolean has = text.contains("world");           // true
        int first = text.indexOf("o");                  // 4
        int last = text.lastIndexOf("o");               // 7

        List<String> words = Arrays.asList("apple", "banana", "apricot");
        Optional<String> firstStartsWithA = words.stream()
                .filter(w -> w.startsWith("a"))
                .findFirst();
        ```

        **Output:** `has = true`, `first = 4`, `last = 7`, `firstStartsWithA = Optional[apple]`

        ---

        ### 4.2 Replace: replace, replaceAll, replaceFirst

        ```java
        String s = "hello world";
        String r1 = s.replace("l", "L");           // "heLLo worLd"
        String r2 = s.replaceAll("l+", "L");       // "heLo worLd"
        String r3 = s.replaceFirst("l+", "L");     // "heLo world"
        ```

        **Output:** `r1 = "heLLo worLd"`, `r2 = "heLo worLd"`, `r3 = "heLo world"`

        ---

        ### 4.3 Word reverse (reverse each word in sentence)

        ```java
        String sentence = "hello world";
        String reversed = Arrays.stream(sentence.split("\\s+"))
                .map(word -> new StringBuilder(word).reverse().toString())
                .collect(Collectors.joining(" "));
        ```

        **Output:** `"olleh dlrow"`

        ---

        ### 4.4 Find word: first/last occurrence, all indices

        ```java
        String text = "the cat and the dog";
        String word = "the";
        int firstIdx = text.indexOf(word);                    // 0
        int lastIdx = text.lastIndexOf(word);                 // 12

        List<Integer> allIndices = new ArrayList<>();
        int from = 0;
        while ((from = text.indexOf(word, from)) != -1) {
            allIndices.add(from);
            from += word.length();
        }
        // allIndices = [0, 12]
        ```

        **Output:** `firstIdx = 0`, `lastIdx = 12`, `allIndices = [0, 12]`

        ---

        ### 4.5 Palindrome: check if string is palindrome

        ```java
        String s = "racecar";
        boolean isPalindrome = s.equals(new StringBuilder(s).reverse().toString());
        // true

        // Using two pointers
        boolean isPal = true;
        for (int i = 0, j = s.length() - 1; i < j; i++, j--) {
            if (s.charAt(i) != s.charAt(j)) {
                isPal = false;
                break;
            }
        }
        // isPal = true
        ```

        **Output:** `isPalindrome = true`, `isPal = true`

        ---

        ### 4.6 Palindrome: list palindromic substrings (short example)

        ```java
        String s = "aba";
        List<String> palindromes = new ArrayList<>();
        for (int i = 0; i < s.length(); i++) {
            for (int j = i + 1; j <= s.length(); j++) {
                String sub = s.substring(i, j);
                if (sub.equals(new StringBuilder(sub).reverse().toString())) {
                    palindromes.add(sub);
                }
            }
        }
        // ["a", "b", "a", "aba"]
        ```

        **Output:** `["a", "b", "a", "aba"]`

        ---

        ### 4.7 Permutation: check if two strings are permutations

        ```java
        String a = "listen";
        String b = "silent";
        boolean arePermutations = a.length() == b.length() &&
                a.chars().sorted().boxed().collect(Collectors.toList())
                        .equals(b.chars().sorted().boxed().collect(Collectors.toList()));
        ```

        **Output:** `arePermutations = true`

        ---

        ### 4.8 Permutation: generate all permutations of a string

        ```java
        public static List<String> permutations(String s) {
            if (s.length() <= 1) return Collections.singletonList(s);
            List<String> result = new ArrayList<>();
            for (int i = 0; i < s.length(); i++) {
                String rest = s.substring(0, i) + s.substring(i + 1);
                for (String perm : permutations(rest)) {
                    result.add(s.charAt(i) + perm);
                }
            }
            return result;
        }
        // permutations("ab") -> [ab, ba]
        ```

        **Output:** `permutations("ab") = [ab, ba]`

        ---

        ## 5. Quick reference table

        | Problem type | Main Stream / API |
        |--------------|-------------------|
        | List → Map (index) | `IntStream.range().boxed().collect(Collectors.toMap(list::get, i -> i))` |
        | List → Map (duplicate merge) | `Collectors.toMap(..., v -> 1L, Long::sum)` |
        | Map → List (keys sorted by value) | `entrySet().stream().sorted(comparingByValue()).map(getKey).collect(Collectors.toList())` |
        | flatMap (nested lists) | `list.stream().flatMap(List::stream)` |
        | Count frequency | `Collectors.groupingBy(Function.identity(), Collectors.counting())` |
        | Partition | `Collectors.partitioningBy(predicate)` |
        | Group anagrams | `groupingBy(word -> sortedChars(word))` |
        | Word reverse in sentence | `Arrays.stream(split).map(sb::reverse).join(" ")` |
        | Palindrome check | `s.equals(new StringBuilder(s).reverse().toString())` |
        | Two strings permutations | Compare sorted char lists |
        | Permutations of string | Recursion: fix one char, permute rest, prepend |

        ---

        All examples use **Java 8** syntax (`Collectors.toList()`, `Function.identity()`, etc.) and include explicit output.
        """
    ).lstrip()


def title_hashmap_cheatsheet() -> str:
    # Full reference text is intentionally kept as-is (copy/paste friendly)
    # and is generated so it stays in nav and doesn't get overwritten.
    return textwrap.dedent(
        """\
        # Java HashMap — Complete Guide (Java 8, Java 21)

        Introduction to `HashMap`, all its methods with examples and output, transformations, Map → List conversions, insertion, deletion, replace operations, and Java 8 / Java 21 examples.

        ---

        ## Table of Contents

        - [1. HashMap introduction](#1-hashmap-introduction)
        - [2. All HashMap methods with examples and output](#2-all-hashmap-methods-with-examples-and-output)
          - [2.1 put, putIfAbsent, putAll](#21-put-putifabsent-putall)
          - [2.2 get, getOrDefault](#22-get-getordefault)
          - [2.3 remove](#23-remove)
          - [2.4 replace, replaceAll](#24-replace-replaceall)
          - [2.5 containsKey, containsValue](#25-containskey-containsvalue)
          - [2.6 size, isEmpty, clear](#26-size-isempty-clear)
          - [2.7 keySet, values, entrySet](#27-keyset-values-entryset)
          - [2.8 compute, computeIfAbsent, computeIfPresent](#28-compute-computeifabsent-computeifpresent)
          - [2.9 merge](#29-merge)
          - [2.10 forEach (Java 8)](#210-foreach-java-8)
          - [2.11 Java 21: SequencedMap methods](#211-java-21-sequencedmap-methods)
        - [3. Transformations](#3-transformations)
          - [3.1 Transform values (e.g., multiply all values by 2)](#31-transform-values-e-g-multiply-all-values-by-2)
          - [3.2 Transform keys](#32-transform-keys)
          - [3.3 Filter entries](#33-filter-entries)
        - [4. Insertion operations](#4-insertion-operations)
          - [4.1 Basic insertion](#41-basic-insertion)
          - [4.2 Insert only if absent](#42-insert-only-if-absent)
          - [4.3 Insert with computeIfAbsent](#43-insert-with-computeifabsent)
          - [4.4 Insert all from another map](#44-insert-all-from-another-map)
        - [5. Deletion operations](#5-deletion-operations)
          - [5.1 Remove by key](#51-remove-by-key)
          - [5.2 Remove by key-value pair](#52-remove-by-key-value-pair)
          - [5.3 Remove entries matching condition](#53-remove-entries-matching-condition)
          - [5.4 Clear all](#54-clear-all)
        - [6. Replace operations](#6-replace-operations)
          - [6.1 Replace value for key](#61-replace-value-for-key)
          - [6.2 Replace if value matches](#62-replace-if-value-matches)
          - [6.3 Replace all values](#63-replace-all-values)
        - [7. Map to List conversions](#7-map-to-list-conversions)
          - [7.1 Keys to List](#71-keys-to-list)
          - [7.2 Values to List](#72-values-to-list)
          - [7.3 Entries to List](#73-entries-to-list)
          - [7.4 Stream: keys to List](#74-stream-keys-to-list)
          - [7.5 Stream: values to List](#75-stream-values-to-list)
          - [7.6 Stream: entries to List of custom objects](#76-stream-entries-to-list-of-custom-objects)
          - [7.7 Map to List of keys sorted by values](#77-map-to-list-of-keys-sorted-by-values)
        - [8. List to Map conversions](#8-list-to-map-conversions)
          - [8.1 List to Map (element as key, index as value)](#81-list-to-map-element-as-key-index-as-value)
          - [8.2 List to Map (element as key, transformed value)](#82-list-to-map-element-as-key-transformed-value)
          - [8.3 List to Map with duplicate keys (merge)](#83-list-to-map-with-duplicate-keys-merge)
        - [9. Java 8 Stream operations with Map](#9-java-8-stream-operations-with-map)
          - [9.1 Filter entries](#91-filter-entries)
          - [9.2 Map entries to different type](#92-map-entries-to-different-type)
          - [9.3 Sort by key](#93-sort-by-key)
          - [9.4 Sort by value](#94-sort-by-value)
          - [9.5 Group by value](#95-group-by-value)
        - [10. Coding interview questions](#10-coding-interview-questions)
          - [10.1 Count frequency of characters in string](#101-count-frequency-of-characters-in-string)
          - [10.2 Find first non-repeated character](#102-find-first-non-repeated-character)
          - [10.3 Two Sum (indices)](#103-two-sum-indices)
          - [10.4 Group anagrams](#104-group-anagrams)
          - [10.5 Merge two maps (sum values for same keys)](#105-merge-two-maps-sum-values-for-same-keys)
          - [10.6 Find duplicate elements](#106-find-duplicate-elements)
          - [10.7 Sort map by value (descending)](#107-sort-map-by-value-descending)
          - [10.8 Invert map (swap keys and values)](#108-invert-map-swap-keys-and-values)
          - [10.9 Find key with maximum value](#109-find-key-with-maximum-value)
          - [10.10 Check if two maps are equal (ignoring order)](#1010-check-if-two-maps-are-equal-ignoring-order)
        - [11. Quick reference table](#11-quick-reference-table)

        ---

        ## 1. HashMap introduction

        - **`HashMap<K, V>`** is a hash table-based implementation of the `Map` interface. It stores key-value pairs, allows one null key and multiple null values, and does not guarantee order (Java 7 and earlier) or insertion order (Java 8+).
        - **Key characteristics:**
          - **O(1)** average time for `get()` and `put()` operations (assuming good hash distribution).
          - **Not thread-safe** — use `ConcurrentHashMap` or `Collections.synchronizedMap()` for multi-threaded access.
          - **No duplicate keys** — adding a duplicate key replaces the old value.
          - **Allows null** — one null key, multiple null values.

        ```java
        Map<String, Integer> map = new HashMap<>();
        Map<String, Integer> withCapacity = new HashMap<>(16);  // initial capacity
        Map<String, Integer> withLoadFactor = new HashMap<>(16, 0.75f);  // capacity, load factor
        ```

        ---

        ## 2. All HashMap methods with examples and output

        ### 2.1 put, putIfAbsent, putAll

        | Method | Description |
        |--------|-------------|
        | `V put(K key, V value)` | Associates key with value; returns previous value (or null) |
        | `V putIfAbsent(K key, V value)` | Puts only if key is absent; returns existing value or null |
        | `void putAll(Map<? extends K, ? extends V> m)` | Copies all mappings from m |

        ```java
        Map<String, Integer> map = new HashMap<>();
        Integer old1 = map.put("apple", 10);        // old1 = null, map = {apple=10}
        Integer old2 = map.put("apple", 20);        // old2 = 10, map = {apple=20}
        Integer old3 = map.putIfAbsent("banana", 30); // old3 = null, map = {apple=20, banana=30}
        Integer old4 = map.putIfAbsent("apple", 25);  // old4 = 20 (unchanged), map = {apple=20, banana=30}
        map.putAll(Map.of("mango", 40, "berry", 50)); // map = {apple=20, banana=30, mango=40, berry=50}
        ```

        **Output:** `old1 = null`, `old2 = 10`, `old3 = null`, `old4 = 20`; final map: `{apple=20, banana=30, mango=40, berry=50}`

        ---

        ### 2.2 get, getOrDefault

        | Method | Description |
        |--------|-------------|
        | `V get(Object key)` | Value for key, or null if absent |
        | `V getOrDefault(Object key, V defaultValue)` | Value for key, or defaultValue if absent |

        ```java
        Map<String, Integer> map = new HashMap<>(Map.of("apple", 10, "banana", 20));
        Integer val1 = map.get("apple");              // 10
        Integer val2 = map.get("mango");              // null
        Integer val3 = map.getOrDefault("mango", 0);   // 0
        Integer val4 = map.getOrDefault("apple", 0);   // 10
        ```

        **Output:** `val1 = 10`, `val2 = null`, `val3 = 0`, `val4 = 10`

        ---

        ### 2.3 remove

        | Method | Description |
        |--------|-------------|
        | `V remove(Object key)` | Removes mapping for key; returns value (or null) |
        | `boolean remove(Object key, Object value)` | Removes only if key maps to value; returns true if removed |

        ```java
        Map<String, Integer> map = new HashMap<>(Map.of("apple", 10, "banana", 20, "mango", 30));
        Integer removed1 = map.remove("banana");              // removed1 = 20, map = {apple=10, mango=30}
        boolean removed2 = map.remove("apple", 10);          // removed2 = true, map = {mango=30}
        boolean removed3 = map.remove("mango", 50);          // removed3 = false (value mismatch)
        Integer removed4 = map.remove("berry");               // removed4 = null
        ```

        **Output:** `removed1 = 20`, `removed2 = true`, `removed3 = false`, `removed4 = null`; final map: `{mango=30}`

        ---

        ### 2.4 replace, replaceAll

        | Method | Description |
        |--------|-------------|
        | `V replace(K key, V value)` | Replaces value for key if present; returns old value (or null) |
        | `boolean replace(K key, V oldValue, V newValue)` | Replaces only if key maps to oldValue; returns true if replaced |
        | `void replaceAll(BiFunction<? super K, ? super V, ? extends V> function)` | Replaces each value with function(key, value) |

        ```java
        Map<String, Integer> map = new HashMap<>(Map.of("apple", 10, "banana", 20));
        Integer old1 = map.replace("apple", 15);              // old1 = 10, map = {apple=15, banana=20}
        boolean replaced = map.replace("banana", 20, 25);     // replaced = true, map = {apple=15, banana=25}
        boolean notReplaced = map.replace("banana", 30, 35);  // notReplaced = false
        map.replaceAll((k, v) -> v * 2);                      // map = {apple=30, banana=50}
        ```

        **Output:** `old1 = 10`, `replaced = true`, `notReplaced = false`; after replaceAll: `{apple=30, banana=50}`

        ---

        ### 2.5 containsKey, containsValue

        | Method | Description |
        |--------|-------------|
        | `boolean containsKey(Object key)` | true if map contains key |
        | `boolean containsValue(Object value)` | true if map contains value |

        ```java
        Map<String, Integer> map = new HashMap<>(Map.of("apple", 10, "banana", 20));
        boolean hasKey = map.containsKey("apple");      // true
        boolean hasValue = map.containsValue(20);        // true
        boolean noKey = map.containsKey("mango");       // false
        boolean noValue = map.containsValue(100);       // false
        ```

        **Output:** `hasKey = true`, `hasValue = true`, `noKey = false`, `noValue = false`

        ---

        ### 2.6 size, isEmpty, clear

        | Method | Description |
        |--------|-------------|
        | `int size()` | Number of key-value mappings |
        | `boolean isEmpty()` | true if size is 0 |
        | `void clear()` | Removes all mappings |

        ```java
        Map<String, Integer> map = new HashMap<>(Map.of("a", 1, "b", 2));
        int size = map.size();          // 2
        boolean empty = map.isEmpty();  // false
        map.clear();                    // map = {}
        boolean emptyAfter = map.isEmpty(); // true
        ```

        **Output:** `size = 2`, `empty = false`, after clear `emptyAfter = true`

        ---

        ### 2.7 keySet, values, entrySet

        | Method | Description |
        |--------|-------------|
        | `Set<K> keySet()` | Set view of keys (changes reflect in map) |
        | `Collection<V> values()` | Collection view of values (changes reflect in map) |
        | `Set<Map.Entry<K, V>> entrySet()` | Set view of entries (changes reflect in map) |

        ```java
        Map<String, Integer> map = new HashMap<>(Map.of("apple", 10, "banana", 20));
        Set<String> keys = map.keySet();
        Collection<Integer> values = map.values();
        Set<Map.Entry<String, Integer>> entries = map.entrySet();
        keys.remove("apple");
        ```

        **Output:** Removing from `keySet` removes from map.

        ---

        ### 2.8 compute, computeIfAbsent, computeIfPresent

        | Method | Description |
        |--------|-------------|
        | `V compute(K key, BiFunction<? super K, ? super V, ? extends V> remappingFunction)` | Computes new value; removes if function returns null |
        | `V computeIfAbsent(K key, Function<? super K, ? extends V> mappingFunction)` | Computes value only if key is absent |
        | `V computeIfPresent(K key, BiFunction<? super K, ? super V, ? extends V> remappingFunction)` | Computes value only if key is present |

        ```java
        Map<String, Integer> map = new HashMap<>();
        map.put("apple", 10);
        Integer computed = map.compute("apple", (k, v) -> v + 5);
        Integer computed2 = map.compute("banana", (k, v) -> 20);
        map.compute("apple", (k, v) -> null);

        map.put("apple", 10);
        Integer absent = map.computeIfAbsent("mango", k -> 30);
        Integer absent2 = map.computeIfAbsent("apple", k -> 50);

        Integer present = map.computeIfPresent("apple", (k, v) -> v * 2);
        Integer present2 = map.computeIfPresent("berry", (k, v) -> 100);
        ```

        **Output:** Values as commented; map changes accordingly.

        ---

        ### 2.9 merge

        | Method | Description |
        |--------|-------------|
        | `V merge(K key, V value, BiFunction<? super V, ? super V, ? extends V> remappingFunction)` | If key absent, puts value; else merges |

        ```java
        Map<String, Integer> map = new HashMap<>();
        map.put("apple", 10);
        Integer merged1 = map.merge("apple", 5, Integer::sum);
        Integer merged2 = map.merge("banana", 20, Integer::sum);
        map.merge("apple", 10, (old, newVal) -> null);
        ```

        **Output:** `merged1 = 15`, `merged2 = 20`; after null merge, apple is removed.

        ---

        ### 2.10 forEach (Java 8)

        | Method | Description |
        |--------|-------------|
        | `void forEach(BiConsumer<? super K, ? super V> action)` | Performs action for each entry |

        ```java
        Map<String, Integer> map = new HashMap<>(Map.of("apple", 10, "banana", 20));
        map.forEach((k, v) -> System.out.println(k + " -> " + v));
        // apple -> 10
        // banana -> 20
        ```

        ---

        ### 2.11 Java 21: SequencedMap methods

        `HashMap` implements **`SequencedMap`** in Java 21.

        **Note:** `HashMap` does not maintain insertion order by default. Use **`LinkedHashMap`** for ordered behavior with these methods.

        ```java
        LinkedHashMap<String, Integer> map = new LinkedHashMap<>(Map.of("a", 1, "b", 2, "c", 3));
        SequencedMap<String, Integer> reversed = map.reversed();
        Map.Entry<String, Integer> first = map.firstEntry();
        Map.Entry<String, Integer> last = map.lastEntry();
        ```

        ---

        ## 3. Transformations

        ### 3.1 Transform values (e.g., multiply all values by 2)

        ```java
        Map<String, Integer> map = new HashMap<>(Map.of("apple", 10, "banana", 20));
        map.replaceAll((k, v) -> v * 2);
        Map<String, Integer> doubled = map.entrySet().stream()
                .collect(Collectors.toMap(Map.Entry::getKey, e -> e.getValue() * 2));
        ```

        **Output:** `{apple=20, banana=40}`

        ---

        ### 3.2 Transform keys

        ```java
        Map<String, Integer> map = new HashMap<>(Map.of("apple", 10, "banana", 20));
        Map<String, Integer> upperKeys = map.entrySet().stream()
                .collect(Collectors.toMap(e -> e.getKey().toUpperCase(), Map.Entry::getValue));
        // {APPLE=10, BANANA=20}
        ```

        ---

        ### 3.3 Filter entries

        ```java
        Map<String, Integer> map = new HashMap<>(Map.of("apple", 10, "banana", 20, "mango", 5));
        Map<String, Integer> filtered = map.entrySet().stream()
                .filter(e -> e.getValue() >= 10)
                .collect(Collectors.toMap(Map.Entry::getKey, Map.Entry::getValue));
        // {apple=10, banana=20}
        ```

        ---

        ## 4. Insertion operations

        ### 4.1 Basic insertion

        ```java
        Map<String, Integer> map = new HashMap<>();
        map.put("apple", 10);
        map.put("banana", 20);
        map.put("apple", 15);
        ```

        ---

        ### 4.2 Insert only if absent

        ```java
        Map<String, Integer> map = new HashMap<>();
        map.putIfAbsent("apple", 10);
        map.putIfAbsent("apple", 20);
        ```

        ---

        ### 4.3 Insert with computeIfAbsent

        ```java
        Map<String, List<String>> map = new HashMap<>();
        map.computeIfAbsent("fruits", k -> new ArrayList<>()).add("apple");
        map.computeIfAbsent("fruits", k -> new ArrayList<>()).add("banana");
        // {fruits=[apple, banana]}
        ```

        ---

        ### 4.4 Insert all from another map

        ```java
        Map<String, Integer> map1 = new HashMap<>(Map.of("apple", 10));
        Map<String, Integer> map2 = Map.of("banana", 20, "mango", 30);
        map1.putAll(map2);
        ```

        ---

        ## 5. Deletion operations

        ### 5.1 Remove by key

        ```java
        Map<String, Integer> map = new HashMap<>(Map.of("apple", 10, "banana", 20));
        map.remove("apple");
        ```

        ---

        ### 5.2 Remove by key-value pair

        ```java
        Map<String, Integer> map = new HashMap<>(Map.of("apple", 10, "banana", 20));
        map.remove("apple", 10);
        map.remove("banana", 30);
        ```

        ---

        ### 5.3 Remove entries matching condition

        ```java
        Map<String, Integer> map = new HashMap<>(Map.of("apple", 10, "banana", 20, "mango", 5));
        map.entrySet().removeIf(e -> e.getValue() < 10);
        ```

        ---

        ### 5.4 Clear all

        ```java
        map.clear();
        ```

        ---

        ## 6. Replace operations

        ### 6.1 Replace value for key

        ```java
        Map<String, Integer> map = new HashMap<>(Map.of("apple", 10));
        map.replace("apple", 20);
        map.replace("banana", 30);
        ```

        ---

        ### 6.2 Replace if value matches

        ```java
        Map<String, Integer> map = new HashMap<>(Map.of("apple", 10));
        map.replace("apple", 10, 20);
        map.replace("apple", 10, 30);
        ```

        ---

        ### 6.3 Replace all values

        ```java
        Map<String, Integer> map = new HashMap<>(Map.of("apple", 10, "banana", 20));
        map.replaceAll((k, v) -> v * 2);
        ```

        ---

        ## 7. Map to List conversions

        ### 7.1 Keys to List

        ```java
        Map<String, Integer> map = new HashMap<>(Map.of("apple", 10, "banana", 20));
        List<String> keys = new ArrayList<>(map.keySet());
        ```

        ---

        ### 7.2 Values to List

        ```java
        List<Integer> values = new ArrayList<>(map.values());
        ```

        ---

        ### 7.3 Entries to List

        ```java
        List<Map.Entry<String, Integer>> entries = new ArrayList<>(map.entrySet());
        ```

        ---

        ### 7.4 Stream: keys to List

        ```java
        List<String> keys = map.keySet().stream().collect(Collectors.toList());
        List<String> sortedKeys = map.keySet().stream().sorted().collect(Collectors.toList());
        ```

        ---

        ### 7.5 Stream: values to List

        ```java
        List<Integer> values = map.values().stream().collect(Collectors.toList());
        List<Integer> sortedValues = map.values().stream().sorted().collect(Collectors.toList());
        ```

        ---

        ### 7.6 Stream: entries to List of custom objects

        ```java
        List<String> keyValuePairs = map.entrySet().stream()
                .map(e -> e.getKey() + "=" + e.getValue())
                .collect(Collectors.toList());
        ```

        ---

        ### 7.7 Map to List of keys sorted by values

        ```java
        Map<String, Integer> map = new HashMap<>(Map.of("apple", 30, "banana", 10, "mango", 20));
        List<String> keysByValue = map.entrySet().stream()
                .sorted(Map.Entry.comparingByValue())
                .map(Map.Entry::getKey)
                .collect(Collectors.toList());
        ```

        ---

        ## 8. List to Map conversions

        ### 8.1 List to Map (element as key, index as value)

        ```java
        List<String> list = List.of("apple", "banana", "mango");
        Map<String, Integer> map = IntStream.range(0, list.size())
                .boxed()
                .collect(Collectors.toMap(list::get, i -> i));
        ```

        ---

        ### 8.2 List to Map (element as key, transformed value)

        ```java
        List<String> list = List.of("apple", "banana", "mango");
        Map<String, Integer> map = list.stream()
                .collect(Collectors.toMap(Function.identity(), String::length));
        ```

        ---

        ### 8.3 List to Map with duplicate keys (merge)

        ```java
        List<String> list = List.of("apple", "banana", "apple", "mango");
        Map<String, Long> count = list.stream()
                .collect(Collectors.toMap(Function.identity(), v -> 1L, Long::sum));
        ```

        ---

        ## 9. Java 8 Stream operations with Map

        ### 9.1 Filter entries

        ```java
        Map<String, Integer> map = new HashMap<>(Map.of("apple", 10, "banana", 20, "mango", 5));
        Map<String, Integer> filtered = map.entrySet().stream()
                .filter(e -> e.getValue() >= 10)
                .collect(Collectors.toMap(Map.Entry::getKey, Map.Entry::getValue));
        ```

        ---

        ### 9.2 Map entries to different type

        ```java
        Map<String, Integer> map = new HashMap<>(Map.of("apple", 10, "banana", 20));
        Map<String, String> stringValues = map.entrySet().stream()
                .collect(Collectors.toMap(Map.Entry::getKey, e -> String.valueOf(e.getValue())));
        ```

        ---

        ### 9.3 Sort by key

        ```java
        Map<String, Integer> sortedByKey = map.entrySet().stream()
                .sorted(Map.Entry.comparingByKey())
                .collect(Collectors.toMap(Map.Entry::getKey, Map.Entry::getValue,
                        (e1, e2) -> e1, LinkedHashMap::new));
        ```

        ---

        ### 9.4 Sort by value

        ```java
        Map<String, Integer> sortedByValue = map.entrySet().stream()
                .sorted(Map.Entry.comparingByValue())
                .collect(Collectors.toMap(Map.Entry::getKey, Map.Entry::getValue,
                        (e1, e2) -> e1, LinkedHashMap::new));
        ```

        ---

        ### 9.5 Group by value

        ```java
        Map<String, Integer> map = new HashMap<>(Map.of("apple", 10, "banana", 20, "mango", 10));
        Map<Integer, List<String>> grouped = map.entrySet().stream()
                .collect(Collectors.groupingBy(Map.Entry::getValue,
                        Collectors.mapping(Map.Entry::getKey, Collectors.toList())));
        ```

        ---

        ## 10. Coding interview questions

        ### 10.1 Count frequency of characters in string

        ```java
        String s = "hello";
        Map<Character, Long> freq = s.chars()
                .mapToObj(c -> (char) c)
                .collect(Collectors.groupingBy(Function.identity(), Collectors.counting()));
        ```

        ---

        ### 10.2 Find first non-repeated character

        ```java
        String s = "hello";
        Optional<Character> first = s.chars()
                .mapToObj(c -> (char) c)
                .collect(Collectors.groupingBy(Function.identity(), Collectors.counting()))
                .entrySet().stream()
                .filter(e -> e.getValue() == 1)
                .map(Map.Entry::getKey)
                .findFirst();
        ```

        ---

        ### 10.3 Two Sum (indices)

        ```java
        int[] nums = {2, 7, 11, 15};
        int target = 9;
        Map<Integer, Integer> map = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            int complement = target - nums[i];
            if (map.containsKey(complement)) {
                // return new int[]{map.get(complement), i};
            }
            map.put(nums[i], i);
        }
        ```

        ---

        ### 10.4 Group anagrams

        ```java
        List<String> words = List.of("eat", "tea", "tan", "ate", "nat", "bat");
        Map<String, List<String>> anagrams = words.stream()
                .collect(Collectors.groupingBy(word -> {
                    char[] chars = word.toCharArray();
                    Arrays.sort(chars);
                    return new String(chars);
                }));
        ```

        ---

        ### 10.5 Merge two maps (sum values for same keys)

        ```java
        Map<String, Integer> map1 = Map.of("a", 1, "b", 2);
        Map<String, Integer> map2 = Map.of("b", 3, "c", 4);
        Map<String, Integer> merged = Stream.concat(map1.entrySet().stream(), map2.entrySet().stream())
                .collect(Collectors.toMap(Map.Entry::getKey, Map.Entry::getValue, Integer::sum));
        ```

        ---

        ### 10.6 Find duplicate elements

        ```java
        List<String> list = List.of("a", "b", "a", "c", "b");
        Set<String> duplicates = list.stream()
                .collect(Collectors.groupingBy(Function.identity(), Collectors.counting()))
                .entrySet().stream()
                .filter(e -> e.getValue() > 1)
                .map(Map.Entry::getKey)
                .collect(Collectors.toSet());
        ```

        ---

        ### 10.7 Sort map by value (descending)

        ```java
        Map<String, Integer> map = new HashMap<>(Map.of("apple", 30, "banana", 10, "mango", 20));
        Map<String, Integer> sorted = map.entrySet().stream()
                .sorted(Map.Entry.<String, Integer>comparingByValue().reversed())
                .collect(Collectors.toMap(Map.Entry::getKey, Map.Entry::getValue,
                        (e1, e2) -> e1, LinkedHashMap::new));
        ```

        ---

        ### 10.8 Invert map (swap keys and values)

        ```java
        Map<String, Integer> map = new HashMap<>(Map.of("apple", 10, "banana", 20));
        Map<Integer, String> inverted = map.entrySet().stream()
                .collect(Collectors.toMap(Map.Entry::getValue, Map.Entry::getKey));
        ```

        ---

        ### 10.9 Find key with maximum value

        ```java
        Map<String, Integer> map = new HashMap<>(Map.of("apple", 30, "banana", 10, "mango", 20));
        Optional<String> maxKey = map.entrySet().stream()
                .max(Map.Entry.comparingByValue())
                .map(Map.Entry::getKey);
        ```

        ---

        ### 10.10 Check if two maps are equal (ignoring order)

        ```java
        Map<String, Integer> map1 = new HashMap<>(Map.of("a", 1, "b", 2));
        Map<String, Integer> map2 = new HashMap<>(Map.of("b", 2, "a", 1));
        boolean equal = map1.equals(map2);  // true
        ```

        ---

        ## 11. Quick reference table

        | Operation | Method / Code |
        |-----------|---------------|
        | Insert | `map.put(key, value)` |
        | Insert if absent | `map.putIfAbsent(key, value)` |
        | Get | `map.get(key)` or `map.getOrDefault(key, defaultValue)` |
        | Remove | `map.remove(key)` or `map.remove(key, value)` |
        | Replace | `map.replace(key, value)` or `map.replace(key, oldValue, newValue)` |
        | Replace all | `map.replaceAll((k, v) -> newValue)` |
        | Contains | `map.containsKey(key)`, `map.containsValue(value)` |
        | Transform values | `map.replaceAll((k, v) -> transform(v))` or stream |
        | Filter entries | `map.entrySet().stream().filter(...).collect(...)` |
        | Sort by key | `entrySet().stream().sorted(Map.Entry.comparingByKey())` |
        | Sort by value | `entrySet().stream().sorted(Map.Entry.comparingByValue())` |
        | Map → List (keys) | `new ArrayList<>(map.keySet())` |
        | Map → List (values) | `new ArrayList<>(map.values())` |
        | Map → List (entries) | `new ArrayList<>(map.entrySet())` |
        | List → Map | `list.stream().collect(Collectors.toMap(...))` |
        | Group by value | `entrySet().stream().collect(Collectors.groupingBy(...))` |

        ---

        All examples use **Java 8** streams and collectors; Java 21 **SequencedMap** methods are noted where applicable.
        """
    ).lstrip()

GEN_STREAM = textwrap.dedent(
    """\
    import java.util.*;
    import java.util.stream.*;

    public class Example {
        public static void main(String[] args) {
            List<Integer> xs = Arrays.asList(1, 2, 3, 4, 5);
            int sumOfEvens = xs.stream().filter(x -> x % 2 == 0).mapToInt(x -> x).sum();
            System.out.println(sumOfEvens);
        }
    }
    """
)


def page_for(title: str) -> str:
    low = title.strip().lower()

    if low in (
        "java 8 stream api & interview examples",
        "java 8 stream api and interview examples",
    ):
        return textwrap.dedent(
            """\
            # Java 8 Stream API & Interview Examples

            A single reference for Java 8 Stream API usage, collection conversions, general interview-style problems, and string operations—each with code and explicit output.

            **Typical imports:**
            ```java
            import java.util.*;
            import java.util.stream.*;
            import java.util.function.*;
            ```

            ---

            ## Table of Contents

            - [1. Stream API essentials (with output)](#1-stream-api-essentials-with-output)
              - [1.1 filter, map, flatMap](#1-1-filter-map-flatmap)
              - [1.2 distinct, sorted, limit, skip](#1-2-distinct-sorted-limit-skip)
              - [1.3 reduce (with and without identity)](#1-3-reduce-with-and-without-identity)
              - [1.4 collect: toList, toSet, toMap, joining, groupingBy, partitioningBy](#1-4-collect-tolist-toset-tomap-joining-groupingby-partitioningby)
              - [1.5 Optional: findFirst, findAny, max, min](#1-5-optional-findfirst-findany-max-min)
              - [1.6 Primitive streams: IntStream.range, mapToInt, sum](#1-6-primitive-streams-intstream-range-maptoint-sum)
            - [2. Conversions (with output)](#2-conversions-with-output)
              - [2.1 List → Map (element as key, index as value)](#2-1-list-map-element-as-key-index-as-value)
              - [2.2 List → Map with duplicate-key merge](#2-2-list-map-with-duplicate-key-merge)
              - [2.3 Map → List (keys, values, entries, keys sorted by value)](#2-3-map-list-keys-values-entries-keys-sorted-by-value)
              - [2.4 flatMap: list of lists → single list; string → words/chars](#2-4-flatmap-list-of-lists-single-list-string-words-chars)
            - [3. General interview examples (with output)](#3-general-interview-examples-with-output)
              - [3.1 Count frequency (list and string)](#3-1-count-frequency-list-and-string)
              - [3.2 First non-repeated character](#3-2-first-non-repeated-character)
              - [3.3 Sort by frequency then by value](#3-3-sort-by-frequency-then-by-value)
              - [3.4 Two lists → Map](#3-4-two-lists-map)
              - [3.5 Chunk list into sublists of size n](#3-5-chunk-list-into-sublists-of-size-n)
              - [3.6 Remove duplicates preserving order](#3-6-remove-duplicates-preserving-order)
              - [3.7 Second largest / nth element](#3-7-second-largest-nth-element)
              - [3.8 Partition by predicate (evens/odds)](#3-8-partition-by-predicate-evens-odds)
              - [3.9 Group anagrams](#3-9-group-anagrams)
              - [3.10 Two Sum (indices)](#3-10-two-sum-indices)
              - [3.11 Merge two maps (sum values for same key)](#3-11-merge-two-maps-sum-values-for-same-key)
            - [4. String operations (with output)](#4-string-operations-with-output)
              - [4.1 Search: contains, indexOf, lastIndexOf, stream findFirst](#4-1-search-contains-indexof-lastindexof-stream-findfirst)
              - [4.2 Replace: replace, replaceAll, replaceFirst](#4-2-replace-replace-replaceall-replacefirst)
              - [4.3 Word reverse (reverse each word in sentence)](#4-3-word-reverse-reverse-each-word-in-sentence)
              - [4.4 Find word: first/last occurrence, all indices](#4-4-find-word-first-last-occurrence-all-indices)
              - [4.5 Palindrome: check if string is palindrome](#4-5-palindrome-check-if-string-is-palindrome)
              - [4.6 Palindrome: list palindromic substrings (short example)](#4-6-palindrome-list-palindromic-substrings-short-example)
              - [4.7 Permutation: check if two strings are permutations](#4-7-permutation-check-if-two-strings-are-permutations)
              - [4.8 Permutation: generate all permutations of a string](#4-8-permutation-generate-all-permutations-of-a-string)
            - [5. Quick reference table](#5-quick-reference-table)

            ---

            """
        ).lstrip() + title_stream_api_cheatsheet()

    if low in (
        "java hashmap — complete guide (java 8, java 21)",
        "java hashmap - complete guide (java 8, java 21)",
    ):
        return title_hashmap_cheatsheet()

    # Section 1
    if low.startswith("java platform overview"):
        return render(
            title,
            concept="JDK is the developer kit, JRE is the runtime environment, JVM executes bytecode. These layers matter for build vs run decisions.",
            problem="Explain what runs your Java code and what you need installed in dev vs prod.",
            intuition=(
                "Think: source -> bytecode -> JVM runtime.\n\n"
                "ASCII:\nHello.java --javac--> Hello.class --JVM--> native\n\n"
                "JDK = JRE + tools; JRE = JVM + core libs."
            ),
            java_impl=textwrap.dedent(
                """\
                public class Hello {
                    public static void main(String[] args) {
                        System.out.println("Hello, Java");
                    }
                }
                """
            ),
            stream_impl=GEN_STREAM,
            sample_input="- Input: `javac Hello.java` then `java Hello`",
            execution_steps=bullets("Compile", "Load/verify classes", "Execute main"),
            output="- Output: Hello, Java",
            complexity="- N/A (concept)",
            enterprise="Affects container images, CI toolchains, and runtime tuning (GC/JIT flags).",
            interview=bullets("What is bytecode?", "What is JIT?", "What is the classloader?"),
            best_practices=bullets("Pin JDK version", "Monitor GC", "Use minimal runtime images where appropriate"),
        )

    # Section 3 (JVM Essentials)
    if low == "jvm memory areas (heap, stack, metaspace)":
        return render(
            title,
            concept=(
                "The JVM divides memory into areas with different lifetimes and ownership:\n\n"
                "- Heap: objects/arrays, GC-managed\n"
                "- Stack (per thread): frames/local variables/return addresses\n"
                "- Metaspace: class metadata (HotSpot), native memory\n\n"
                "ASCII (simplified):\n"
                "+-------------------------+\n"
                "| Heap (Young / Old)     |\n"
                "+-------------------------+\n"
                "| Metaspace (classes)    |\n"
                "+-------------------------+\n"
                "| Thread Stack (per thr) |\n"
                "+-------------------------+"
            ),
            problem="Explain where memory goes when you allocate objects, call methods, and load classes.",
            intuition=(
                "Local primitives and references live in stack frames; the objects they reference live on the heap.\n\n"
                "Class loading increases Metaspace usage; excessive classloading can exhaust it."
            ),
            java_impl=textwrap.dedent(
                """\
                public class MemoryAreas {
                    static int f(int x) {
                        int local = x + 1; // stack
                        Integer boxed = local; // boxed object on heap
                        return boxed;
                    }

                    public static void main(String[] args) {
                        System.out.println(f(41));
                    }
                }
                """
            ),
            stream_impl=GEN_STREAM,
            sample_input="- Input: x = 41",
            execution_steps=bullets(
                "Call f(41) -> new frame on stack",
                "Allocate Integer -> heap",
                "Return value",
            ),
            output="- Output: 42",
            complexity="- N/A (concept)",
            enterprise=(
                "Heap sizing and GC tuning are core production concerns. Metaspace issues appear with dynamic proxies, class reloading, and large frameworks."
            ),
            interview=bullets(
                "Heap vs stack",
                "What triggers GC?",
                "What lives in Metaspace?",
                "Escape analysis (conceptual)",
            ),
            best_practices=bullets(
                "Avoid unnecessary allocations in hot paths",
                "Watch Metaspace with frameworks/proxies",
                "Use profiling (JFR/jcmd) before tuning",
            ),
        )

    if low == "garbage collection basics":
        return render(
            title,
            concept=(
                "Garbage collection (GC) reclaims heap memory for objects that are no longer reachable.\n\n"
                "Java 8 HotSpot generational GC idea:\n"
                "- Young gen: many short-lived objects\n"
                "- Old gen: long-lived objects\n\n"
                "ASCII:\n[allocate] -> Eden -> (minor GC) -> Survivor -> ... -> Old"
            ),
            problem="Explain why allocation rate and object lifetime distribution impacts latency.",
            intuition="Many short-lived allocations cause frequent minor GCs; large old-gen pressure can cause long pauses depending on collector.",
            java_impl=textwrap.dedent(
                """\
                import java.util.*;

                public class AllocationPressure {
                    public static void main(String[] args) {
                        List<byte[]> keep = new ArrayList<>();
                        for (int i = 0; i < 1000; i++) {
                            // 1MB allocations
                            keep.add(new byte[1024 * 1024]);
                        }
                        System.out.println(keep.size());
                    }
                }
                """
            ),
            stream_impl=GEN_STREAM,
            sample_input="- Input: allocate 1000 arrays of 1MB",
            execution_steps=bullets("Allocate objects", "Keep references so they survive", "Observe GC impact under profiling"),
            output="- Output: 1000",
            complexity="- N/A (concept)",
            enterprise=(
                "Allocation rate and GC pauses directly affect p99 latency. High-throughput services require controlling allocation and using appropriate collectors/settings."
            ),
            interview=bullets("Reachability", "Stop-the-world", "Minor vs major GC", "GC roots"),
            best_practices=bullets("Reduce temporary objects", "Prefer primitives", "Reuse buffers carefully", "Profile before tuning"),
        )

    if low == "exceptions (checked vs unchecked)":
        return render(
            title,
            concept=(
                "Checked exceptions must be declared/handled; unchecked exceptions (RuntimeException) do not.\n\n"
                "Production guidance: use checked exceptions for recoverable cases at boundaries, unchecked for programmer errors."
            ),
            problem="Design error handling for an API that can fail due to validation vs system failures.",
            intuition="Use exception types to encode recoverability and to separate validation errors from infrastructure failures.",
            java_impl=textwrap.dedent(
                """\
                class ValidationException extends Exception {
                    ValidationException(String msg) { super(msg); }
                }

                public class ExceptionsDemo {
                    static int parseAge(String s) throws ValidationException {
                        try {
                            int n = Integer.parseInt(s);
                            if (n < 0) throw new ValidationException("age");
                            return n;
                        } catch (NumberFormatException e) {
                            throw new ValidationException("not a number");
                        }
                    }

                    public static void main(String[] args) {
                        try {
                            System.out.println(parseAge("12"));
                        } catch (ValidationException e) {
                            System.out.println("BAD_REQUEST");
                        }
                    }
                }
                """
            ),
            stream_impl=textwrap.dedent(
                """\
                import java.util.*;
                import java.util.stream.*;

                public class ExceptionInStreamNote {
                    public static void main(String[] args) {
                        // Avoid throwing checked exceptions inside stream lambdas.
                        // Prefer mapping to Either-like result or pre-validate.
                    }
                }
                """
            ),
            sample_input="- Input: \"12\"",
            execution_steps=bullets("Parse", "Validate", "Return or throw"),
            output="- Output: 12",
            complexity="- N/A (concept)",
            enterprise="Exception taxonomy drives API error mapping (400 vs 500), retries, and observability (error rates).",
            interview=bullets("When to use checked", "finally semantics", "try-with-resources"),
            best_practices=bullets("Don’t swallow exceptions", "Add context", "Preserve cause", "Avoid exceptions for control flow"),
        )

    if low == "common performance pitfalls":
        return render(
            title,
            concept=(
                "Common JVM performance pitfalls are usually about allocation, boxing, synchronization, and accidental O(n^2) behavior.\n\n"
                "ASCII (typical perf loop):\nmeasure -> identify hotspot -> change -> measure again"
            ),
            problem="Avoid turning a linear transform into O(n^2) or creating excessive garbage.",
            intuition="Look for nested loops, repeated `contains` on lists, boxing in hot paths, and building large intermediate lists.",
            java_impl=textwrap.dedent(
                """\
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
                """
            ),
            stream_impl=textwrap.dedent(
                """\
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
                """
            ),
            sample_input="- Input: a=[1,2,3,4,5], b=[3,4]",
            execution_steps=bullets("Spot nested contains", "Convert lookup list to HashSet", "Re-measure"),
            output="- Output: [3,4]",
            complexity="- Time: O(n*m) pitfall, O(n) with HashSet membership\n- Space: O(m)",
            enterprise="This is a classic production regression pattern (latency spikes after small refactors).",
            interview=bullets("Big-O reasoning", "Allocation and GC", "Profiling approach"),
            best_practices=bullets("Use sets for membership", "Avoid boxing", "Profile with real data"),
        )

    # Section 2 (OOP and Design Basics)
    if low.startswith("oop pillars"):
        return render(
            title,
            concept=(
                "OOP pillars are the core design tools for building maintainable systems:\n\n"
                "- Encapsulation: hide invariants behind methods\n"
                "- Inheritance: reuse behavior (use sparingly)\n"
                "- Polymorphism: program to interfaces\n"
                "- Abstraction: model domain concepts\n\n"
                "ASCII:\nService -> Interface -> Implementation"
            ),
            problem="Model a domain type with validation and a stable interface boundary.",
            intuition="Encapsulation keeps invariants local; polymorphism decouples call sites from implementations.",
            java_impl=textwrap.dedent(
                """\
                interface PaymentGateway {
                    boolean charge(String accountId, int cents);
                }

                class StripeGateway implements PaymentGateway {
                    public boolean charge(String accountId, int cents) { return true; }
                }

                final class Money {
                    private final int cents;
                    Money(int cents) {
                        if (cents < 0) throw new IllegalArgumentException("cents");
                        this.cents = cents;
                    }
                    int cents() { return cents; }
                }
                """
            ),
            stream_impl=textwrap.dedent(
                """\
                import java.util.*;
                import java.util.stream.*;

                public class OopStreamExample {
                    static class User { final String role; User(String r){ role=r; } }
                    public static void main(String[] args) {
                        List<User> users = Arrays.asList(new User("ADMIN"), new User("USER"));
                        long admins = users.stream().filter(u -> "ADMIN".equals(u.role)).count();
                        System.out.println(admins);
                    }
                }
                """
            ),
            sample_input=bullets("Input: cents = 1200", "Input: users roles = [ADMIN, USER]"),
            execution_steps=bullets("Validate invariants in constructor", "Program to interface", "Count via stream filter"),
            output=bullets("Output: Money created", "Output: admins = 1"),
            complexity="- Time: O(n) for stream filter\n- Space: O(1) extra",
            enterprise="These principles reduce coupling and allow swapping implementations (e.g., gateways, repositories) without rewriting callers.",
            interview=bullets("Composition vs inheritance", "Interface-driven design", "Immutability and invariants"),
            best_practices=bullets("Prefer composition", "Keep classes small", "Hide invariants", "Program to interfaces"),
        )

    if low == "abstract class vs interface":
        return render(
            title,
            concept=(
                "Interfaces define capabilities (contracts). Abstract classes share state and partial implementations.\n\n"
                "Java 8 interfaces can have default/static methods, but they still should not own mutable instance state."
            ),
            problem="Design an API where multiple implementations share some logic but must enforce a contract.",
            intuition="Use interface for capability; use abstract class when you need shared state/constructor logic.",
            java_impl=textwrap.dedent(
                """\
                interface Serializer<T> {
                    String serialize(T t);
                }

                abstract class BaseJsonSerializer<T> implements Serializer<T> {
                    protected String quote(String s) { return \"\\\"\" + s + \"\\\"\"; }
                }

                class User { final String name; User(String n){ name=n; } }

                class UserSerializer extends BaseJsonSerializer<User> {
                    public String serialize(User u) { return \"{\\\"name\\\":\" + quote(u.name) + \"}\"; }
                }
                """
            ),
            stream_impl=GEN_STREAM,
            sample_input="- Input: User(name=amy)",
            execution_steps=bullets("Define contract interface", "Share helper in abstract base", "Implement serialize"),
            output="- Output: {\"name\":\"amy\"}",
            complexity="- N/A (concept)",
            enterprise="Important for SDK/library design and service boundaries (SPI/API separation).",
            interview=bullets("Multiple inheritance of type via interfaces", "Default methods vs abstract methods"),
            best_practices=bullets("Prefer interface-first", "Avoid deep inheritance", "Keep base classes small"),
        )

    if low == "equals/hashcode/tostring contracts":
        return render(
            title,
            concept=(
                "`equals` and `hashCode` must be consistent for correct behavior in hash-based collections.\n\n"
                "ASCII:\nHashMap uses hashCode() -> bucket, then equals() to match key"
            ),
            problem="Make a value object safe to use as a key in HashMap/HashSet.",
            intuition="If two objects are equal, they must have the same hashCode. Use immutable fields for keys.",
            java_impl=textwrap.dedent(
                """\
                import java.util.*;

                final class Key {
                    final String id;
                    Key(String id) { this.id = id; }

                    @Override public boolean equals(Object o) {
                        if (this == o) return true;
                        if (!(o instanceof Key)) return false;
                        Key k = (Key) o;
                        return Objects.equals(id, k.id);
                    }

                    @Override public int hashCode() { return Objects.hash(id); }

                    @Override public String toString() { return "Key(" + id + ")"; }
                }

                public class Contracts {
                    public static void main(String[] args) {
                        Map<Key, Integer> m = new HashMap<>();
                        m.put(new Key("a"), 1);
                        System.out.println(m.get(new Key("a")));
                    }
                }
                """
            ),
            stream_impl=GEN_STREAM,
            sample_input="- Input: put(Key(a)->1), get(Key(a))",
            execution_steps=bullets("Compute hashCode", "Find bucket", "Use equals to match"),
            output="- Output: 1",
            complexity="- Time: O(1) avg map operations\n- Space: O(n)",
            enterprise="Broken contracts cause production cache misses, duplicate keys, and memory leaks in maps/sets.",
            interview=bullets("equals properties (reflexive/symmetric/transitive)", "hash collisions", "mutable keys"),
            best_practices=bullets("Use immutable fields", "Never mutate map keys", "Use Objects.equals/hash"),
        )

    if low == "immutability":
        return render(
            title,
            concept=(
                "Immutable objects cannot change after construction. They are inherently thread-safe and easier to reason about.\n\n"
                "ASCII:\nCreate -> Use -> Discard (no mutation)"
            ),
            problem="Design a thread-safe value object used across threads (e.g., DTOs, keys, configs).",
            intuition="Make fields final, validate in constructor, avoid exposing mutable internals, and use defensive copies.",
            java_impl=textwrap.dedent(
                """\
                import java.util.*;

                public final class Config {
                    private final String env;
                    private final List<String> hosts;

                    public Config(String env, List<String> hosts) {
                        this.env = env;
                        this.hosts = Collections.unmodifiableList(new ArrayList<>(hosts));
                    }

                    public String env() { return env; }
                    public List<String> hosts() { return hosts; }
                }
                """
            ),
            stream_impl=textwrap.dedent(
                """\
                import java.util.*;
                import java.util.stream.*;

                public class ImmutableCollectors {
                    public static void main(String[] args) {
                        List<String> xs = Arrays.asList("a", "b", "c");
                        List<String> imm = xs.stream()
                                .collect(Collectors.collectingAndThen(Collectors.toList(), Collections::unmodifiableList));
                        System.out.println(imm);
                    }
                }
                """
            ),
            sample_input=bullets("Input: env=prod", "Input: hosts=[h1,h2]"),
            execution_steps=bullets("Copy mutable inputs", "Wrap as unmodifiable", "Expose read-only accessors"),
            output="- Output: immutable config/immutable list",
            complexity="- Time: O(n) for defensive copy\n- Space: O(n)",
            enterprise="Immutable configs and DTOs reduce concurrency bugs and simplify caching and retries.",
            interview=bullets("Defensive copying", "Immutability vs unmodifiable", "Thread-safety reasoning"),
            best_practices=bullets("final fields", "no setters", "defensive copy mutable inputs", "avoid exposing internals"),
        )

    # Section 4 (Java 8 features)
    if low == "lambda expressions":
        return render(
            title,
            concept=(
                "Lambdas implement functional interfaces without anonymous-class boilerplate. They enable *behavior passing* and composition.\n\n"
                "Key rules:\n"
                "- Captured variables must be effectively-final\n"
                "- Prefer pure functions (no side effects)\n"
                "- Understand scope: `this` refers to the enclosing instance (unlike anonymous classes)"
            ),
            problem="Implement sorting and a service-style transformation pipeline with minimal boilerplate.",
            intuition=(
                "A lambda is a method body + captured context. The runtime may use invokedynamic for efficient linkage.\n\n"
                "ASCII (behavior passed into API):\n"
                "List.sort( Comparator )\n"
                "Stream.map( Function )\n"
                "Stream.filter( Predicate )"
            ),
            java_impl=textwrap.dedent(
                """\
                import java.util.*;

                public class LambdaSort {
                    public static void main(String[] args) {
                        List<String> names = Arrays.asList("amy", "bob", "carl");
                        names.sort((a, b) -> a.compareTo(b));
                        System.out.println(names);
                    }
                }
                """
            ),
            stream_impl=textwrap.dedent(
                """\
                import java.util.*;
                import java.util.stream.*;

                public class LambdaStream {
                    public static void main(String[] args) {
                        List<String> names = Arrays.asList("amy", "bob", "carl");
                        List<String> out = names.stream().map(s -> s.toUpperCase()).collect(Collectors.toList());
                        System.out.println(out);
                    }
                }
                """
            ),
            sample_input="- Input: [amy, bob, carl]",
            execution_steps=bullets(
                "Pass comparator lambda into sort",
                "Pass mapping lambda into stream map",
                "Collect results",
            ),
            output="- Output: [AMY, BOB, CARL] (stream example)",
            complexity="- Time: O(n log n) sort; O(n) map\n- Space: O(n)",
            enterprise=(
                "Used in DTO mapping, validation, and executor callbacks.\n\n"
                "Production pitfall: side effects inside parallel pipelines can corrupt shared state."
            ),
            interview=bullets(
                "What is effectively-final?",
                "Lambda vs anonymous class (`this`, capture, serialization)",
                "When lambdas hurt readability/debugging",
            ),
            best_practices=bullets(
                "Keep lambdas small; extract named methods for complex logic",
                "Avoid capturing mutable state",
                "Prefer method references when they improve readability",
            ),
        )

    if low == "functional interfaces":
        return render(
            title,
            concept=(
                "Functional interfaces have a single abstract method (SAM) and are targets for lambdas/method references.\n\n"
                "Prefer standard types in `java.util.function` (Predicate, Function, Supplier, Consumer) for interoperability."
            ),
            problem="Define a reusable validation policy and apply it in a pipeline.",
            intuition="SAM type inference lets the compiler map a lambda to the interface method signature.",
            java_impl=textwrap.dedent(
                """\
                @FunctionalInterface
                interface Validator<T> { boolean isValid(T t); }

                public class ValidatorDemo {
                    public static void main(String[] args) {
                        Validator<String> nonEmpty = s -> s != null && !s.trim().isEmpty();
                        System.out.println(nonEmpty.isValid(""));
                    }
                }
                """
            ),
            stream_impl=textwrap.dedent(
                """\
                import java.util.*;
                import java.util.stream.*;

                public class ValidatorStream {
                    public static void main(String[] args) {
                        List<String> xs = Arrays.asList("a", "", "b");
                        List<String> out = xs.stream().filter(s -> !s.isEmpty()).collect(Collectors.toList());
                        System.out.println(out);
                    }
                }
                """
            ),
            sample_input='- Input: [a, "", b]',
            execution_steps=bullets("Define functional interface", "Implement via lambda", "Use in stream filter"),
            output="- Output: [a, b]",
            complexity="- Time: O(n)\n- Space: O(n)",
            enterprise="Used for domain predicates, policies, authorization checks, and reusable composition in service layers.",
            interview=bullets(
                "@FunctionalInterface meaning",
                "Default methods allowed?",
                "Why prefer standard java.util.function types",
            ),
            best_practices=bullets(
                "Prefer java.util.function types",
                "Document null-handling",
                "Keep implementations pure; avoid checked exceptions in lambdas",
            ),
        )

    if low == "method references":
        return render(
            title,
            concept="Method references are shorthand for lambdas that forward to an existing method/constructor.",
            problem="Make stream pipelines and callbacks more readable.",
            intuition=(
                "Replace `x -> foo(x)` with `Type::foo` when signatures match.\n\n"
                "Forms:\n- static: Type::staticMethod\n- bound: instance::method\n- unbound: Type::instanceMethod\n- ctor: Type::new"
            ),
            java_impl=textwrap.dedent(
                """\
                import java.util.*;

                public class MethodRef {
                    public static void main(String[] args) {
                        Arrays.asList("a", "b").forEach(System.out::println);
                    }
                }
                """
            ),
            stream_impl=textwrap.dedent(
                """\
                import java.util.*;
                import java.util.stream.*;

                public class MethodRefStream {
                    public static void main(String[] args) {
                        List<Integer> out = Arrays.asList("amy", "bob").stream().map(String::length).collect(Collectors.toList());
                        System.out.println(out);
                    }
                }
                """
            ),
            sample_input="- Input: [amy, bob]",
            execution_steps=bullets("Use System.out::println", "Use String::length"),
            output="- Output: [3, 3]",
            complexity="- Time: O(n)\n- Space: O(n)",
            enterprise="Improves code review readability and standardizes house-style streams.",
            interview=bullets(
                "Bound vs unbound references",
                "Constructor references",
                "Overload resolution edge cases",
            ),
            best_practices=bullets("Use only when clearer", "Avoid when it hides intent"),
        )

    if low in ("default methods", "static methods in interfaces"):
        return render(
            title,
            concept=(
                "Interfaces can have default implementations and static utility methods. This enables API evolution without forcing every implementor to change immediately.\n\n"
                "Default methods are inherited; if multiple defaults conflict, the implementing class must explicitly override."
            ),
            problem="Add a new behavior to an interface in a backward-compatible way and keep callers consistent.",
            intuition=(
                "Use default methods for small shared behavior that logically belongs to the interface.\n\n"
                "Use static methods for utilities that support the contract (normalization, parsing, guards)."
            ),
            java_impl=textwrap.dedent(
                """\
                interface Auditable {
                    default String tag() { return "AUDIT"; }
                    static String norm(String s) { return s == null ? "" : s.trim(); }
                }

                class Order implements Auditable {}

                public class InterfaceMethods {
                    public static void main(String[] args) {
                        System.out.println(new Order().tag());
                        System.out.println(Auditable.norm(" x "));
                    }
                }
                """
            ),
            stream_impl=GEN_STREAM,
            sample_input=bullets(
                "Input: new Order().tag()",
                "Input: Auditable.norm(\" x \")",
            ),
            execution_steps=bullets(
                "Invoke default method on instance",
                "Invoke static helper method on interface",
            ),
            output=bullets(
                "Output: AUDIT",
                "Output: x",
            ),
            complexity="- N/A (concept)",
            enterprise="Common in library evolution, SPI design, and backward-compatible platform APIs.",
            interview=bullets(
                "Diamond problem and conflict resolution",
                "Binary compatibility vs source compatibility",
                "Interface vs abstract class trade-offs",
            ),
            best_practices=bullets(
                "Keep default methods small and side-effect free",
                "Avoid mutable state in interfaces",
                "Document behavior clearly when adding defaults",
            ),
        )

    if low == "optional api":
        return render(
            title,
            concept=(
                "Optional makes absence explicit for return values and reduces null-related bugs.\n\n"
                "Guidance: return Optional, avoid Optional fields/serialization, and avoid `get()` without a presence check."
            ),
            problem="Model missing data at service boundaries (e.g., user lookup) without returning null.",
            intuition=(
                "Use `map` to transform present values, `flatMap` to avoid nested Optional, and `orElseGet` for lazy defaults.\n\n"
                "In Java 8, when converting `List<Optional<T>>` to `List<T>`, you typically filter+get; avoid `get()` without checking presence."
            ),
            java_impl=textwrap.dedent(
                """\
                import java.util.*;

                public class OptionalDemo {
                    static Optional<String> email(String id) {
                        return "u1".equals(id) ? Optional.of("u1@example.com") : Optional.empty();
                    }
                    public static void main(String[] args) {
                        System.out.println(email("u2").orElse("unknown"));
                    }
                }
                """
            ),
            stream_impl=textwrap.dedent(
                """\
                import java.util.*;
                import java.util.stream.*;

                public class OptionalStream {
                    public static void main(String[] args) {
                        List<Optional<Integer>> xs = Arrays.asList(Optional.of(1), Optional.empty(), Optional.of(3));
                        List<Integer> out = xs.stream().filter(Optional::isPresent).map(Optional::get).collect(Collectors.toList());
                        System.out.println(out);
                    }
                }
                """
            ),
            sample_input=bullets(
                "Input: userId = u2",
                "Input: xs = [Optional(1), Optional.empty, Optional(3)]",
            ),
            execution_steps=bullets(
                "Lookup returns Optional.empty for missing user",
                "Apply `orElse` at boundary for default value",
                "Filter present optionals and unwrap",
            ),
            output=bullets(
                "Output: unknown",
                "Output: [1, 3]",
            ),
            complexity="- Time: O(1)\n- Space: O(1)",
            enterprise="Reduces NPEs and clarifies service contracts; improves API documentation and caller behavior.",
            interview=bullets("orElse vs orElseGet", "Optional.map vs flatMap", "Optional in fields?"),
            best_practices=bullets("Return Optional", "Prefer orElseGet for expensive defaults", "Avoid Optional.get"),
        )

    if low == "new date and time api":
        return render(
            title,
            concept=(
                "java.time is immutable, thread-safe, and timezone-correct (unlike java.util.Date/Calendar).\n\n"
                "Use:\n- Instant for machine time\n- LocalDate for business dates\n- ZonedDateTime for user/timezone"
            ),
            problem="Convert and format a timestamp for a user-facing timezone without losing correctness.",
            intuition=(
                "Store timestamps as UTC `Instant` in systems of record, then convert to `ZonedDateTime` at the boundary (UI/API response).\n\n"
                "Use `Duration` for machine-time differences; use `Period` for date-based differences."
            ),
            java_impl=textwrap.dedent(
                """\
                import java.time.*;
                import java.time.format.*;

                public class TimeDemo {
                    public static void main(String[] args) {
                        Instant fixed = Instant.parse("2020-01-02T03:04:05Z");
                        ZonedDateTime ist = fixed.atZone(ZoneId.of("Asia/Kolkata"));
                        System.out.println(DateTimeFormatter.ISO_ZONED_DATE_TIME.format(ist));
                    }
                }
                """
            ),
            stream_impl=GEN_STREAM,
            sample_input="- Input: 2020-01-02T03:04:05Z",
            execution_steps=bullets("Parse Instant", "Convert to Asia/Kolkata", "Format ISO string"),
            output="- Output: 2020-01-02T08:34:05+05:30[Asia/Kolkata]",
            complexity="- N/A (concept)",
            enterprise="Critical for audit logs, SLAs, scheduling, and cross-timezone correctness.",
            interview=bullets("Instant vs LocalDate", "Duration vs Period", "Zone conversions (DST)"),
            best_practices=bullets("Store UTC instants", "Convert at edges", "Avoid legacy Date/Calendar"),
        )

    # ---------------- Section 5: Stream API ----------------
    if low == "stream api overview":
        return render(
            title,
            concept=(
                "Streams are *lazy pipelines* over a data source. You build a pipeline with intermediate ops, and it runs when you call a terminal op.\n\n"
                "This page gives a quick production-oriented overview with multiple examples you’ll see in services and batch jobs."
            ),
            problem="Implement common real-world transformations and aggregations using Stream API.",
            intuition="Think in stages: source -> (0..n intermediate ops) -> terminal. Keep lambdas pure and output deterministic.",
            java_impl=textwrap.dedent(
                """\
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
                """\
            ),
            stream_impl=textwrap.dedent(
                """\
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
                """\
            ),
            sample_input=bullets(
                'Input: names=["amy","bob","carl","bob"]',
                'Input: raw=["  Foo ","BAR",""]',
                "Input: a=[1,2,3,4,5]",
            ),
            execution_steps=bullets("Build pipelines", "Run terminal ops", "Print E1..E6"),
            output=bullets(
                "Output: E1=[amy, bob, carl]",
                "Output: E2=[foo, bar]",
                "Output: E3=15",
                "Output: E4={ENG=[amy, bob], HR=[carl]}",
                "Output: E5=4",
                "Output: E6=amy,bob,carl",
            ),
            complexity="- Depends on ops: many are O(n); sorting is O(n log n)\n- Space: O(n)",
            enterprise="Streams are great for in-memory mapping/aggregation. Don’t stream huge datasets without chunking/backpressure.",
            interview=bullets("Lazy evaluation", "Intermediate vs terminal", "Stateful ops (sorted/distinct)", "When NOT to use streams"),
            best_practices=bullets("Keep lambdas pure", "Prefer primitive streams", "Avoid collecting huge lists", "Use LinkedHashMap supplier when order matters"),
        )

    if low == "creating streams":
        return render(
            title,
            concept="Common ways to create streams: collections, arrays, Stream.of, builder, generate/iterate, file/lines (IO).",
            problem="Create streams from multiple sources and produce deterministic results.",
            intuition="Choose the correct source; avoid infinite streams without limit.",
            java_impl=textwrap.dedent(
                """\
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
                """\
            ),
            stream_impl=textwrap.dedent(
                """\
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
                """\
            ),
            sample_input=bullets("Input: [1,2,3]", "Input: map={a=1,b=2}", "Input: range 1..5"),
            execution_steps=bullets("Create source", "Stream it", "Collect/print E1..E6"),
            output=bullets(
                "Output: E1=[1, 2, 3]",
                "Output: E2=[1, 2, 3]",
                "Output: E3=[a, b]",
                "Output: E4=[a=1, b=2]",
                "Output: E5=[1, 2, 3, 4, 5]",
                "Output: E6=[7, 7, 7, 7, 7]",
            ),
            complexity="- Mostly O(n)\n- Space: O(n) if collected",
            enterprise="Creating streams is easy; controlling size/backpressure is the hard part. Avoid infinite streams without `limit()`.",
            interview=bullets("Stream.generate vs iterate", "range vs rangeClosed", "boxing costs"),
            best_practices=bullets("Prefer primitive streams", "Use LinkedHashMap when order matters", "Avoid creating streams in tight loops"),
        )

    if low == "stream pipeline":
        return render(
            title,
            concept="A pipeline is a chain of stages. Intermediate ops are lazy; terminal ops trigger execution.",
            problem="Build production-like pipelines for normalization, enrichment, and aggregation.",
            intuition="Make each stage single-purpose. Keep side effects out of intermediate ops.",
            java_impl=textwrap.dedent(
                """\
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
                """\
            ),
            stream_impl=textwrap.dedent(
                """\
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
                """\
            ),
            sample_input=bullets('Input: tags=["  Java ","JAVA",""," streams "]', "Input: ids=[10,20,30]", 'Input: words=["a","b","a"]'),
            execution_steps=bullets("Build pipeline per example", "Terminal op prints E1..E6"),
            output=bullets(
                "Output: E1=[java, streams]",
                "Output: E2=[u-10, u-20, u-30]",
                "Output: E3=[9, 9]",
                "Output: E4={a=2, b=1}",
                "Output: E5=true",
                "Output: E6=java|streams",
            ),
            complexity="- Depends: sort is O(n log n), others often O(n)",
            enterprise="Pipelines are ideal for DTO mapping and in-memory analytics. Be explicit about ordering and memory.",
            interview=bullets("Laziness", "Fusion", "Why distinct/sorted are stateful"),
            best_practices=bullets("Avoid side effects", "Use primitive streams", "Prefer LinkedHashMap for deterministic maps"),
        )

    if low == "intermediate operations":
        return render(
            title,
            concept="Intermediate operations are lazy: filter, map, flatMap, distinct, sorted, limit/skip, peek.",
            problem="Apply common intermediate operations with deterministic outputs.",
            intuition="Intermediate ops transform the stream; no work happens until a terminal op is invoked.",
            java_impl=textwrap.dedent(
                """\
                import java.util.*;

                public class IntermediateOpsLoop {
                    public static void main(String[] args) {
                        List<Integer> xs = Arrays.asList(5,1,2,2,9);

                        // E1 filter
                        List<Integer> e1 = new ArrayList<>();
                        for (int x : xs) if (x % 2 == 0) e1.add(x);
                        System.out.println("E1=" + e1);

                        // E2 map
                        List<Integer> e2 = new ArrayList<>();
                        for (int x : xs) e2.add(x * 10);
                        System.out.println("E2=" + e2);

                        // E3 distinct (manual)
                        List<Integer> e3 = new ArrayList<>();
                        for (int x : xs) if (!e3.contains(x)) e3.add(x);
                        System.out.println("E3=" + e3);

                        // E4 sorted
                        List<Integer> e4 = new ArrayList<>(xs);
                        Collections.sort(e4);
                        System.out.println("E4=" + e4);

                        // E5 limit
                        System.out.println("E5=" + e4.subList(0, 3));

                        // E6 skip
                        System.out.println("E6=" + e4.subList(2, e4.size()));
                    }
                }
                """\
            ),
            stream_impl=textwrap.dedent(
                """\
                import java.util.*;
                import java.util.stream.*;

                public class IntermediateOpsStream {
                    public static void main(String[] args) {
                        List<Integer> xs = Arrays.asList(5,1,2,2,9);
                        System.out.println("E1=" + xs.stream().filter(x -> x % 2 == 0).collect(Collectors.toList()));
                        System.out.println("E2=" + xs.stream().map(x -> x * 10).collect(Collectors.toList()));
                        System.out.println("E3=" + xs.stream().distinct().collect(Collectors.toList()));
                        System.out.println("E4=" + xs.stream().sorted().collect(Collectors.toList()));
                        System.out.println("E5=" + xs.stream().sorted().limit(3).collect(Collectors.toList()));
                        System.out.println("E6=" + xs.stream().sorted().skip(2).collect(Collectors.toList()));
                    }
                }
                """\
            ),
            sample_input="- Input: [5,1,2,2,9]",
            execution_steps=bullets("Apply each intermediate op", "Collect to trigger execution"),
            output=bullets(
                "Output: E1=[2, 2]",
                "Output: E2=[50, 10, 20, 20, 90]",
                "Output: E3=[5, 1, 2, 9]",
                "Output: E4=[1, 2, 2, 5, 9]",
                "Output: E5=[1, 2, 2]",
                "Output: E6=[2, 5, 9]",
            ),
            complexity="- filter/map/distinct: ~O(n) (distinct uses set)\n- sorted: O(n log n)",
            enterprise="Intermediate ops are where most bugs happen: ordering, distinctness, and stateful lambdas.",
            interview=bullets("Why intermediate ops are lazy", "Stateful ops and memory", "peek usage"),
            best_practices=bullets("Avoid stateful lambdas", "Be explicit about order", "Use limit for safety"),
        )

    if low == "terminal operations":
        return render(
            title,
            concept="Terminal operations trigger execution: collect, forEach, reduce, count, min/max, findFirst/anyMatch, etc.",
            problem="Demonstrate common terminal ops with deterministic outputs.",
            intuition="Intermediate ops build; terminal ops consume and produce a result or side effect.",
            java_impl=textwrap.dedent(
                """\
                import java.util.*;

                public class TerminalOpsLoop {
                    public static void main(String[] args) {
                        List<Integer> xs = Arrays.asList(1,2,3,4,5);
                        // E1 count
                        System.out.println("E1=" + xs.size());
                        // E2 sum
                        int sum = 0; for (int x : xs) sum += x; System.out.println("E2=" + sum);
                        // E3 min/max
                        int min = Integer.MAX_VALUE, max = Integer.MIN_VALUE;
                        for (int x : xs) { if (x < min) min = x; if (x > max) max = x; }
                        System.out.println("E3=" + min + "/" + max);
                        // E4 findFirst (first even)
                        Integer firstEven = null; for (int x : xs) { if (x % 2 == 0) { firstEven = x; break; } }
                        System.out.println("E4=" + firstEven);
                        // E5 anyMatch
                        boolean anyGt4 = false; for (int x : xs) { if (x > 4) { anyGt4 = true; break; } }
                        System.out.println("E5=" + anyGt4);
                        // E6 collect (to list of strings)
                        List<String> s = new ArrayList<>(); for (int x : xs) s.add("v" + x);
                        System.out.println("E6=" + s);
                    }
                }
                """\
            ),
            stream_impl=textwrap.dedent(
                """\
                import java.util.*;
                import java.util.stream.*;

                public class TerminalOpsStream {
                    public static void main(String[] args) {
                        List<Integer> xs = Arrays.asList(1,2,3,4,5);
                        System.out.println("E1=" + xs.stream().count());
                        System.out.println("E2=" + xs.stream().mapToInt(x -> x).sum());
                        System.out.println("E3=" + xs.stream().min(Integer::compareTo).get() + "/" + xs.stream().max(Integer::compareTo).get());
                        System.out.println("E4=" + xs.stream().filter(x -> x % 2 == 0).findFirst().orElse(-1));
                        System.out.println("E5=" + xs.stream().anyMatch(x -> x > 4));
                        System.out.println("E6=" + xs.stream().map(x -> "v" + x).collect(Collectors.toList()));
                    }
                }
                """\
            ),
            sample_input="- Input: [1,2,3,4,5]",
            execution_steps=bullets("Call a terminal op", "Print results E1..E6"),
            output=bullets("Output: E1=5", "Output: E2=15", "Output: E3=1/5", "Output: E4=2", "Output: E5=true", "Output: E6=[v1, v2, v3, v4, v5]"),
            complexity="- Most terminals: O(n)\n- min/max: O(n)",
            enterprise="Terminal ops determine materialization. Be careful with `forEach` ordering and side effects.",
            interview=bullets("findFirst vs findAny", "short-circuiting terminals", "collect vs reduce"),
            best_practices=bullets("Prefer collect for containers", "Use mapToInt for numeric", "Avoid forEach for business logic"),
        )

    if low in ("map vs flatmap", "filter", "reduce", "collect", "parallel streams"):
        if low == "filter":
            return render(
                title,
                concept="`filter` keeps elements that match a predicate. In production it’s used for validation, eligibility, and data quality rules.",
                problem="Apply multiple real-world filters with deterministic results.",
                intuition="A good filter predicate is pure, fast, and does not mutate external state.",
                java_impl=textwrap.dedent(
                    """\
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
                    """\
                ),
                stream_impl=textwrap.dedent(
                    """\
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
                    """\
                ),
                sample_input=bullets("Input: xs=[1,2,3,4,5]", 'Input: raw=[" a ",""," b "]', "Input: amounts=[50,100,150]"),
                execution_steps=bullets("Define predicate", "filter", "collect/terminal op prints E1..E6"),
                output=bullets("Output: E1=[2, 4]", "Output: E2=[a, b]", "Output: E3=[100, 150]", "Output: E4=[10, 30]", "Output: E5=[3, 4]", "Output: E6=[a, b]"),
                complexity="- Time: O(n) (per pipeline)\n- Space: O(n) if collected",
                enterprise="Filtering is ubiquitous in request validation, fraud checks, and ETL. Keep predicates pure and cheap.",
                interview=bullets("Predicate purity", "limit short-circuit", "null handling"),
                best_practices=bullets("Avoid side effects", "Prefer method references", "Use Objects::nonNull"),
            )

        if low == "map vs flatmap":
            return render(
                title,
                concept="`map` transforms 1->1; `flatMap` transforms 1->many and flattens nested streams.",
                problem="Parse user-provided tags and produce a single normalized list of tokens.",
                intuition=(
                    "Use map when the output is one value per input. Use flatMap when each input yields multiple values.\n\n"
                    "ASCII:\nmap:    Stream<String> -> Stream<String[]>\nflatMap:Stream<String> -> Stream<String>"
                ),
                java_impl=textwrap.dedent(
                    """\
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
                    """
                ),
                stream_impl=textwrap.dedent(
                    """\
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
                    """
                ),
                sample_input=bullets(
                    'Input: lines=["  Java  spring ", "java  ", " "]',
                    'Input: csv=["1,2","3",""]',
                    'Input: words=["ab","c"]',
                ),
                execution_steps=bullets(
                    "E1: flatMap tokens -> normalize -> distinct -> sort",
                    "E2: map to nested token lists",
                    "E3: flatMap CSV numbers",
                    "E4: filter empties (optional flatten)",
                    "E5: map to lengths",
                    "E6: flatMap characters",
                ),
                output=bullets(
                    "Output: E1=[java, spring]",
                    "Output: E2=[[java, spring], [java], []]",
                    "Output: E3=[1, 2, 3]",
                    "Output: E4=[a, b]",
                    "Output: E5=[4, 6]",
                    "Output: E6=[a, b, c]",
                ),
                complexity="- Time: O(n) for scans; sorting unique tokens adds O(k log k)\n- Space: O(k)",
                enterprise="Common in parsing free-text inputs, log normalization, search indexing, and ingestion pipelines.",
                interview=bullets("flatMap vs map", "flatMap with Optional", "why distinct/sorted are stateful"),
                best_practices=bullets(
                    "Avoid regex split in hot paths",
                    "Normalize at boundaries (trim/case)",
                    "Be aware that distinct/sorted may hold elements in memory",
                ),
            )

        if low == "reduce":
            return render(
                title,
                concept="`reduce` folds elements into a single value using an associative accumulator.",
                problem="Compute common aggregates deterministically and understand when reduce is appropriate.",
                intuition="Use reduce for associative operations; prefer specialized terminals (sum/min/max) when available.",
                java_impl=textwrap.dedent(
                    """\
                    import java.util.*;

                    public class ReduceLoop {
                        public static void main(String[] args) {
                            int[] a = {1,2,3,4};
                            // E1 sum
                            int s = 0; for (int x : a) s += x; System.out.println("E1=" + s);
                            // E2 product
                            int p = 1; for (int x : a) p *= x; System.out.println("E2=" + p);
                            // E3 max
                            int mx = Integer.MIN_VALUE; for (int x : a) if (x > mx) mx = x; System.out.println("E3=" + mx);
                            // E4 concat
                            List<String> xs = Arrays.asList("a","b","c");
                            String c = ""; for (String x : xs) c += x; System.out.println("E4=" + c);
                            // E5 gcd
                            int g = 48;
                            int[] b = {18, 30};
                            for (int x : b) {
                                int aa = g, bb = x;
                                while (bb != 0) { int t = aa % bb; aa = bb; bb = t; }
                                g = aa;
                            }
                            System.out.println("E5=" + g);
                            // E6 set union
                            Set<Integer> u = new LinkedHashSet<>(Arrays.asList(1,2));
                            for (int x : Arrays.asList(2,3)) u.add(x);
                            System.out.println("E6=" + u);
                        }
                    }
                    """
                ),
                stream_impl=textwrap.dedent(
                    """\
                    import java.util.stream.*;
                    import java.util.*;

                    public class ReduceStream {
                        public static void main(String[] args) {
                            int[] a = {1,2,3,4};
                            System.out.println("E1=" + IntStream.of(a).reduce(0, Integer::sum));
                            System.out.println("E2=" + IntStream.of(a).reduce(1, (acc,x) -> acc * x));
                            System.out.println("E3=" + IntStream.of(a).reduce(Integer.MIN_VALUE, Math::max));
                            System.out.println("E4=" + Arrays.asList("a","b","c").stream().reduce("", (acc,x) -> acc + x));
                            System.out.println("E5=" + IntStream.of(48, 18, 30).reduce((left, right) -> {
                                int a1 = left, b1 = right;
                                while (b1 != 0) { int t = a1 % b1; a1 = b1; b1 = t; }
                                return a1;
                            }).getAsInt());
                            System.out.println("E6=" + Stream.of(new LinkedHashSet<>(Arrays.asList(1,2)), new LinkedHashSet<>(Arrays.asList(2,3)))
                                    .reduce(new LinkedHashSet<>(), (acc, s) -> { acc.addAll(s); return acc; }));
                        }
                    }
                    """
                ),
                sample_input=bullets("Input: a=[1,2,3,4]", 'Input: xs=["a","b","c"]', "Input: gcd=[48,18,30]"),
                execution_steps=bullets("Pick associative operation", "Use identity carefully", "Reduce and print E1..E6"),
                output=bullets("Output: E1=10", "Output: E2=24", "Output: E3=4", "Output: E4=abc", "Output: E5=6", "Output: E6=[1, 2, 3]"),
                complexity="- Time: O(n)\n- Space: O(1)",
                enterprise="Reduction is used for totals and metrics; prefer primitive streams to avoid boxing.",
                interview=bullets("Associativity requirement", "Parallel reduce pitfalls"),
                best_practices=bullets("Prefer sum()/summingInt when available", "Use collect for mutable reductions"),
            )

        if low == "collect":
            return render(
                title,
                concept="`collect` performs a mutable reduction (e.g., toList, groupingBy).",
                problem="Build common enterprise containers (lists, sets, maps, grouping) using collectors safely.",
                intuition=(
                    "Collector defines supplier/accumulator/combiner/finisher.\n\n"
                    "In production, `Collectors.toMap` often needs a merge function to decide what to do on duplicates."
                ),
                java_impl=textwrap.dedent(
                    """\
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
                    """\
                ),
                stream_impl=textwrap.dedent(
                    """\
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
                    """\
                ),
                sample_input=bullets("Input: xs=[1,2,2,3]", "Input: users=[(u1,amy),(u1,amy2),(u2,bob)]", 'Input: emps=[(ENG,amy),(ENG,bob),(HR,carl)]'),
                execution_steps=bullets("E1..E6 collectors", "Print deterministic maps using LinkedHashMap where needed"),
                output=bullets(
                    "Output: E1=[1, 2, 2, 3]",
                    "Output: E2=[1, 2, 3]",
                    "Output: E3={u1=amy, u2=bob}",
                    "Output: E4={ENG=[amy, bob], HR=[carl]}",
                    "Output: E5=abc",
                    "Output: E6={false=[1, 3], true=[2, 2]}",
                ),
                complexity="- Time: O(n)\n- Space: O(n)",
                enterprise="Used for lookup maps, grouping/reporting, and response shaping; always define collision policy for keys.",
                interview=bullets("collect vs reduce", "collector combiner", "toMap merge function"),
                best_practices=bullets("Always provide merge for toMap when duplicates are possible", "Prefer immutable at boundaries"),
            )

        if low == "parallel streams":
            return render(
                title,
                concept="Parallel streams split work across threads (ForkJoinPool common pool by default).",
                problem="Use parallel streams safely: CPU-bound, stateless operations, deterministic outputs.",
                intuition=(
                    "Parallelism helps CPU-bound work when operations are associative and have no side effects.\n\n"
                    "In servers, common-pool contention can hurt tail latency."
                ),
                java_impl=textwrap.dedent(
                    """\
                    import java.util.*;

                    public class ParallelNotesLoop {
                        public static void main(String[] args) {
                            // E1 baseline sum
                            long s = 0;
                            for (int i = 1; i <= 10; i++) s += i;
                            System.out.println("E1=" + s);

                            // E2 expensive CPU loop (deterministic)
                            long acc = 0;
                            for (int i = 1; i <= 5; i++) acc += (long)i * i;
                            System.out.println("E2=" + acc);

                            // E3 demonstrate why shared mutation is bad
                            // (loop version is deterministic; parallel version would be unsafe)
                            List<Integer> xs = Arrays.asList(1,2,3,4,5);
                            List<Integer> out = new ArrayList<>();
                            for (int x : xs) out.add(x * 2);
                            System.out.println("E3=" + out);

                            // E4 ordering
                            System.out.println("E4=" + xs); // encounter order

                            // E5 associative reduce example (sum)
                            int sum = 0; for (int x : xs) sum += x;
                            System.out.println("E5=" + sum);

                            // E6 IO-bound should not be parallelized (concept)
                            System.out.println("E6=avoid parallel for IO");
                        }
                    }
                    """\
                ),
                stream_impl=textwrap.dedent(
                    """\
                    import java.util.*;
                    import java.util.stream.*;

                    public class ParallelStreamExamples {
                        public static void main(String[] args) {
                            // E1 parallel sum (small range for determinism)
                            System.out.println("E1=" + LongStream.rangeClosed(1, 10).parallel().sum());

                            // E2 parallel map (CPU-ish)
                            System.out.println("E2=" + IntStream.rangeClosed(1, 5).parallel().mapToLong(x -> (long)x * x).sum());

                            // E3 avoid side effects: use collect not shared list mutation
                            List<Integer> xs = Arrays.asList(1,2,3,4,5);
                            System.out.println("E3=" + xs.parallelStream().map(x -> x * 2).sorted().collect(Collectors.toList()));

                            // E4 ordering: forEach vs forEachOrdered
                            String a = IntStream.rangeClosed(1, 5).parallel().mapToObj(String::valueOf).collect(Collectors.joining(""));
                            String b = IntStream.rangeClosed(1, 5).parallel().mapToObj(String::valueOf).sequential().collect(Collectors.joining(""));
                            System.out.println("E4=" + a + "/" + b);

                            // E5 associative reduction safe; non-associative is not
                            System.out.println("E5=" + IntStream.rangeClosed(1, 5).parallel().reduce(0, Integer::sum));

                            // E6 limit may behave differently with unordered; keep it ordered here
                            System.out.println("E6=" + IntStream.rangeClosed(1, 100).parallel().filter(x -> x % 10 == 0).limit(3).boxed().collect(Collectors.toList()));
                        }
                    }
                    """\
                ),
                sample_input=bullets("Input: range 1..10", "Input: xs=[1,2,3,4,5]"),
                execution_steps=bullets("Use parallel only where it helps", "Avoid shared mutation", "Prefer forEachOrdered if you need order"),
                output=bullets(
                    "Output: E1=55",
                    "Output: E2=55",
                    "Output: E3=[2, 4, 6, 8, 10]",
                    "Output: E5=15",
                    "Output: E6=[10, 20, 30]",
                ),
                complexity="- Work: O(n)\n- Speedup: depends on cores/data size/overhead",
                enterprise="Parallel streams can harm latency in servers due to shared common pool. Prefer explicit executors for isolation.",
                interview=bullets("forEach vs forEachOrdered", "Associativity", "Common pool contention"),
                best_practices=bullets("Measure", "Keep lambdas pure", "Avoid IO in parallel streams", "Use explicit pools in servers"),
            )

    # ---------------- Section 6: Collectors ----------------
    if low in ("collectors overview", "tolist", "toset", "tomap", "groupingby", "partitioningby", "joining", "counting", "summarizing"):
        if low == "collectors overview":
            return render(
                title,
                concept=(
                    "Collectors are reduction strategies for `Stream.collect(...)`. A Collector defines how to accumulate elements into a container or summary.\n\n"
                    "Key idea: Collectors let you do *one pass* aggregation (grouping, counting, joining) instead of multiple loops."
                ),
                problem="Compute multiple aggregates from a list of events (counts + CSV of unique categories).",
                intuition="Pick the right collector (groupingBy/partitioningBy/toMap/joining/summarizing) and define key collision policies.",
                java_impl=GEN_JAVA,
                stream_impl=textwrap.dedent(
                    """\
                    import java.util.*;
                    import java.util.stream.*;

                    public class CollectorsOverview {
                        public static void main(String[] args) {
                            List<String> names = Arrays.asList("amy", "bob", "carl", "bob");
                            Map<Integer, Long> counts = names.stream()
                                    .collect(Collectors.groupingBy(String::length, Collectors.counting()));
                            String csv = names.stream().distinct().sorted().collect(Collectors.joining(","));
                            System.out.println(counts);
                            System.out.println(csv);
                        }
                    }
                    """\
                ),
                sample_input="- Input: [amy, bob, carl, bob]",
                execution_steps=bullets("groupingBy(length, counting)", "distinct + sorted + joining"),
                output=bullets("Output: {3=3, 4=1}", "Output: amy,bob,carl"),
                complexity="- Time: O(n log n) with sorting; O(n) without sorting\n- Space: O(n)",
                enterprise="Collectors power reporting endpoints and batch aggregations; always decide key collision policies (toMap merge).",
                interview=bullets("collect vs reduce", "collector components", "parallel collector safety"),
                best_practices=bullets("Prefer one-pass collectors", "Be explicit about merge behavior", "Avoid collecting massive datasets into memory"),
            )

        if low == "tolist":
            return render(
                title,
                concept="`Collectors.toList()` accumulates elements into a List (not guaranteed to be mutable/ArrayList).",
                problem="Build a list of normalized emails from a list of raw inputs.",
                intuition="Use `map` for normalization and `collect(toList())` to materialize results.",
                java_impl=GEN_JAVA,
                stream_impl=textwrap.dedent(
                    """\
                    import java.util.*;
                    import java.util.stream.*;

                    public class ToListDemo {
                        public static void main(String[] args) {
                            List<String> raw = Arrays.asList(" A@x.com ", "", "b@x.com");
                            List<String> emails = raw.stream()
                                    .map(String::trim)
                                    .map(String::toLowerCase)
                                    .filter(s -> !s.isEmpty())
                                    .collect(Collectors.toList());
                            System.out.println(emails);
                        }
                    }
                    """\
                ),
                sample_input='- Input: [" A@x.com ", "", "b@x.com"]',
                execution_steps=bullets("Trim/lowercase", "Filter empty", "Collect to list"),
                output="- Output: [a@x.com, b@x.com]",
                complexity="- Time: O(n)\n- Space: O(n)",
                enterprise="Used for response shaping; beware collecting extremely large streams (prefer paging).",
                interview=bullets("toList vs toCollection", "mutability guarantees"),
                best_practices=bullets("Prefer immutable at API boundaries", "Don’t assume ArrayList"),
            )

        if low == "toset":
            return render(
                title,
                concept="`Collectors.toSet()` accumulates elements into a Set (no ordering guarantee).",
                problem="Deduplicate roles from a list of user records.",
                intuition="Sets encode uniqueness; use `toCollection(LinkedHashSet::new)` if you need stable order.",
                java_impl=GEN_JAVA,
                stream_impl=textwrap.dedent(
                    """\
                    import java.util.*;
                    import java.util.stream.*;

                    public class ToSetDemo {
                        static class User { final String role; User(String r){ role=r; } }
                        public static void main(String[] args) {
                            List<User> users = Arrays.asList(new User("ADMIN"), new User("USER"), new User("USER"));
                            Set<String> roles = users.stream().map(u -> u.role).collect(Collectors.toSet());
                            System.out.println(roles);
                        }
                    }
                    """\
                ),
                sample_input="- Input: roles=[ADMIN, USER, USER]",
                execution_steps=bullets("Map to role", "Collect to set"),
                output="- Output: [ADMIN, USER] (order may vary)",
                complexity="- Time: O(n)\n- Space: O(n)",
                enterprise="Used for dedupe in authorization and feature flags; be explicit about ordering expectations.",
                interview=bullets("HashSet vs LinkedHashSet", "distinct vs toSet"),
                best_practices=bullets("Use LinkedHashSet when you care about order", "Use TreeSet when you need sorting"),
            )

        if low == "tomap":
            return render(
                title,
                concept="`Collectors.toMap` builds a Map from stream elements; duplicates require a merge function.",
                problem="Index users by id while handling duplicate ids deterministically.",
                intuition="Always provide a merge function unless you can prove uniqueness.",
                java_impl=GEN_JAVA,
                stream_impl=textwrap.dedent(
                    """\
                    import java.util.*;
                    import java.util.stream.*;

                    public class ToMapDemo {
                        static class User { final String id; final String name; User(String i, String n){ id=i; name=n; } }
                        public static void main(String[] args) {
                            List<User> users = Arrays.asList(new User("u1","amy"), new User("u1","amy2"), new User("u2","bob"));
                            Map<String, String> byId = users.stream().collect(Collectors.toMap(
                                    u -> u.id,
                                    u -> u.name,
                                    (left, right) -> left
                            ));
                            System.out.println(byId);
                        }
                    }
                    """\
                ),
                sample_input="- Input: [(u1,amy),(u1,amy2),(u2,bob)]",
                execution_steps=bullets("Key extractor", "Value extractor", "Merge duplicates", "Collect"),
                output="- Output: {u1=amy, u2=bob}",
                complexity="- Time: O(n)\n- Space: O(n)",
                enterprise="Core for caching/indexing; wrong merge policy can cause data loss or inconsistent behavior.",
                interview=bullets("Why toMap throws without merge", "Map supplier overload"),
                best_practices=bullets("Always define merge for non-unique keys", "Avoid heavy work in merge"),
            )

        if low == "groupingby":
            return render(
                title,
                concept="`groupingBy` groups elements by a classifier function and optionally applies a downstream collector.",
                problem="Group orders by customerId and count orders per customer.",
                intuition="Use downstream collectors (`counting`, `mapping`, `summingInt`) to avoid multiple passes.",
                java_impl=GEN_JAVA,
                stream_impl=textwrap.dedent(
                    """\
                    import java.util.*;
                    import java.util.stream.*;

                    public class GroupingByDemo {
                        static class Order { final String customer; final int cents; Order(String c, int s){ customer=c; cents=s; } }
                        public static void main(String[] args) {
                            List<Order> orders = Arrays.asList(new Order("c1", 500), new Order("c1", 700), new Order("c2", 100));
                            Map<String, Long> counts = orders.stream()
                                    .collect(Collectors.groupingBy(o -> o.customer, Collectors.counting()));
                            System.out.println(counts);
                        }
                    }
                    """\
                ),
                sample_input="- Input: [(c1,500),(c1,700),(c2,100)]",
                execution_steps=bullets("Classify by customer", "Downstream counting", "Collect"),
                output="- Output: {c1=2, c2=1}",
                complexity="- Time: O(n)\n- Space: O(n)",
                enterprise="Used in reporting and analytics endpoints. For huge datasets, prefer DB-side group-by.",
                interview=bullets("groupingBy vs groupingByConcurrent", "downstream collectors"),
                best_practices=bullets("Use downstream collectors", "Avoid grouping huge streams in memory"),
            )

        if low == "partitioningby":
            return render(
                title,
                concept="`partitioningBy` splits elements into exactly two groups based on a predicate.",
                problem="Partition transactions into fraud-suspected vs normal.",
                intuition="Use partitioning when the key is boolean; it always returns keys true/false.",
                java_impl=GEN_JAVA,
                stream_impl=textwrap.dedent(
                    """\
                    import java.util.*;
                    import java.util.stream.*;

                    public class PartitioningDemo {
                        public static void main(String[] args) {
                            List<Integer> amounts = Arrays.asList(50, 5000, 20);
                            Map<Boolean, List<Integer>> parts = amounts.stream()
                                    .collect(Collectors.partitioningBy(a -> a >= 1000));
                            System.out.println(parts);
                        }
                    }
                    """\
                ),
                sample_input="- Input: [50, 5000, 20]",
                execution_steps=bullets("Apply predicate a>=1000", "Collect into true/false buckets"),
                output="- Output: {false=[50, 20], true=[5000]}",
                complexity="- Time: O(n)\n- Space: O(n)",
                enterprise="Common in eligibility checks, filtering audit candidates, and risk pipelines.",
                interview=bullets("partitioningBy vs groupingBy", "downstream collector"),
                best_practices=bullets("Use downstream collectors to compute counts/totals", "Keep predicate pure"),
            )

        if low == "joining":
            return render(
                title,
                concept="`joining` concatenates CharSequences, optionally with delimiter/prefix/suffix.",
                problem="Build a CSV string of unique, sorted product codes.",
                intuition="Combine `distinct`/`sorted` with joining to get deterministic output.",
                java_impl=GEN_JAVA,
                stream_impl=textwrap.dedent(
                    """\
                    import java.util.*;
                    import java.util.stream.*;

                    public class JoiningDemo {
                        public static void main(String[] args) {
                            List<String> codes = Arrays.asList("p2", "p1", "p2");
                            String csv = codes.stream().distinct().sorted().collect(Collectors.joining(","));
                            System.out.println(csv);
                        }
                    }
                    """\
                ),
                sample_input='- Input: ["p2","p1","p2"]',
                execution_steps=bullets("distinct", "sorted", "joining(',')"),
                output="- Output: p1,p2",
                complexity="- Time: O(n log n)\n- Space: O(n)",
                enterprise="Useful for logs, cache keys, and export endpoints; beware very large strings.",
                interview=bullets("joining vs StringBuilder", "ordering and determinism"),
                best_practices=bullets("Sort for deterministic outputs", "Avoid joining extremely large streams"),
            )

        if low == "counting":
            return render(
                title,
                concept="`counting()` is a downstream collector that counts elements (often used with groupingBy).",
                problem="Count requests per endpoint.",
                intuition="Counting is O(1) per element; combine it with groupingBy for one-pass aggregation.",
                java_impl=GEN_JAVA,
                stream_impl=textwrap.dedent(
                    """\
                    import java.util.*;
                    import java.util.stream.*;

                    public class CountingDemo {
                        public static void main(String[] args) {
                            List<String> paths = Arrays.asList("/a", "/b", "/a");
                            Map<String, Long> counts = paths.stream()
                                    .collect(Collectors.groupingBy(p -> p, Collectors.counting()));
                            System.out.println(counts);
                        }
                    }
                    """\
                ),
                sample_input='- Input: ["/a","/b","/a"]',
                execution_steps=bullets("groupingBy(path, counting)", "Print map"),
                output="- Output: {/a=2, /b=1}",
                complexity="- Time: O(n)\n- Space: O(n)",
                enterprise="Used for metrics and log analysis; be mindful of high-cardinality keys.",
                interview=bullets("count() terminal vs counting() collector", "cardinality concerns"),
                best_practices=bullets("Control cardinality", "Consider approximate counting for huge domains"),
            )

        # summarizing
        return render(
            title,
            concept="`summarizingInt/Long/Double` computes count, sum, min, max, average in one pass.",
            problem="Compute summary stats for order amounts.",
            intuition="Use summarizing when you need multiple numeric aggregates without multiple traversals.",
            java_impl=GEN_JAVA,
            stream_impl=textwrap.dedent(
                """\
                import java.util.*;
                import java.util.stream.*;

                public class SummarizingDemo {
                    public static void main(String[] args) {
                        List<Integer> cents = Arrays.asList(100, 200, 700);
                        IntSummaryStatistics st = cents.stream().collect(Collectors.summarizingInt(x -> x));
                        System.out.println(st.getCount());
                        System.out.println(st.getSum());
                        System.out.println(st.getMin());
                        System.out.println(st.getMax());
                        System.out.println(st.getAverage());
                    }
                }
                """\
            ),
            sample_input="- Input: [100,200,700]",
            execution_steps=bullets("Collect summarizingInt", "Read count/sum/min/max/avg"),
            output=bullets(
                "Output: count=3",
                "Output: sum=1000",
                "Output: min=100",
                "Output: max=700",
                "Output: avg=333.3333333333333",
            ),
            complexity="- Time: O(n)\n- Space: O(1)",
            enterprise="Used in reporting endpoints and dashboards; prefer primitive specializations for performance.",
            interview=bullets("summingInt vs summarizingInt", "boxing pitfalls"),
            best_practices=bullets("Use primitive collectors", "Be aware of double precision for averages"),
        )

    # ---------------- Section 7: Collection Framework ----------------
    if low == "collection hierarchy":
        return render(
            title,
            concept=(
                "The Collection Framework is centered around `Iterable` and `Collection`, with specializations like `List`, `Set`, and `Queue`.\n\n"
                "ASCII (simplified):\n"
                "Iterable\n  └─ Collection\n      ├─ List\n      ├─ Set\n      └─ Queue"
            ),
            problem="Choose the right collection type for ordering, uniqueness, and access patterns.",
            intuition="Pick by constraints: need duplicates/order -> List; uniqueness -> Set; FIFO -> Queue; key-value -> Map (separate hierarchy).",
            java_impl=textwrap.dedent(
                """\
                import java.util.*;

                public class CollectionChoices {
                    public static void main(String[] args) {
                        List<String> list = Arrays.asList("a", "b", "a");
                        Set<String> set = new HashSet<>(list);
                        Queue<String> q = new ArrayDeque<>(list);

                        System.out.println(list); // keeps duplicates + order
                        System.out.println(set);  // unique, order not guaranteed
                        System.out.println(q.remove()); // FIFO
                    }
                }
                """\
            ),
            stream_impl=textwrap.dedent(
                """\
                import java.util.*;
                import java.util.stream.*;

                public class HierarchyStream {
                    public static void main(String[] args) {
                        List<String> xs = Arrays.asList("a", "b", "a");
                        Set<String> uniq = xs.stream().collect(Collectors.toSet());
                        System.out.println(uniq);
                    }
                }
                """\
            ),
            sample_input='- Input: ["a","b","a"]',
            execution_steps=bullets("Use List for order", "Convert to Set for uniqueness", "Use Queue for FIFO"),
            output=bullets("Output: [a, b, a]", "Output: Set contains a,b", "Output: a"),
            complexity="- Time: O(n) conversions\n- Space: O(n)",
            enterprise="Correct collection choice impacts performance, memory, and correctness (e.g., uniqueness constraints, ordering in APIs).",
            interview=bullets("List vs Set", "Queue use cases", "Why Map is not a Collection"),
            best_practices=bullets("Program to interfaces", "Choose based on access patterns", "Be explicit about ordering"),
        )

    if low == "iterable interface":
        return render(
            title,
            concept="`Iterable` is the root that enables the enhanced for-loop and provides `iterator()`.",
            problem="Implement a custom iterable and iterate safely.",
            intuition="Expose iteration via `Iterator` without exposing internal representation.",
            java_impl=textwrap.dedent(
                """\
                import java.util.*;

                class Range implements Iterable<Integer> {
                    private final int start, endInclusive;
                    Range(int start, int endInclusive) { this.start = start; this.endInclusive = endInclusive; }

                    public Iterator<Integer> iterator() {
                        return new Iterator<Integer>() {
                            int cur = start;
                            public boolean hasNext() { return cur <= endInclusive; }
                            public Integer next() { return cur++; }
                        };
                    }
                }

                public class IterableDemo {
                    public static void main(String[] args) {
                        for (int x : new Range(1, 3)) System.out.println(x);
                    }
                }
                """\
            ),
            stream_impl=textwrap.dedent(
                """\
                import java.util.*;
                import java.util.stream.*;

                public class IterableStream {
                    public static void main(String[] args) {
                        Iterable<Integer> it = Arrays.asList(1,2,3);
                        // Streams require a Collection or Spliterator; most Iterables are Collections in practice.
                        List<Integer> out = StreamSupport.stream(it.spliterator(), false)
                                .map(x -> x * 2)
                                .collect(Collectors.toList());
                        System.out.println(out);
                    }
                }
                """\
            ),
            sample_input="- Input: Range(1..3)",
            execution_steps=bullets("Implement iterator()", "Use for-each", "(Optional) Stream via spliterator"),
            output=bullets("Output: 1", "Output: 2", "Output: 3"),
            complexity="- Time: O(n) iteration\n- Space: O(1)",
            enterprise="Useful for exposing domain-specific iteration without leaking internal collections (e.g., paged results wrappers).",
            interview=bullets("Iterable vs Iterator", "Why Iterator is stateful", "Spliterator basics"),
            best_practices=bullets("Don’t return null iterators", "Document iteration order", "Prefer immutability"),
        )

    if low == "iterator":
        return render(
            title,
            concept="`Iterator` provides `hasNext/next` and optional `remove`. It’s the safe way to traverse and (carefully) modify collections.",
            problem="Remove elements during iteration without `ConcurrentModificationException`.",
            intuition="Use `Iterator.remove()` (or `removeIf`) instead of removing from the collection directly in a for-each.",
            java_impl=textwrap.dedent(
                """\
                import java.util.*;

                public class IteratorRemove {
                    public static void main(String[] args) {
                        List<Integer> xs = new ArrayList<>(Arrays.asList(1,2,3,4));
                        Iterator<Integer> it = xs.iterator();
                        while (it.hasNext()) {
                            int x = it.next();
                            if (x % 2 == 0) it.remove();
                        }
                        System.out.println(xs);
                    }
                }
                """\
            ),
            stream_impl=textwrap.dedent(
                """\
                import java.util.*;

                public class RemoveIfDemo {
                    public static void main(String[] args) {
                        List<Integer> xs = new ArrayList<>(Arrays.asList(1,2,3,4));
                        xs.removeIf(x -> x % 2 == 0);
                        System.out.println(xs);
                    }
                }
                """\
            ),
            sample_input="- Input: [1,2,3,4]",
            execution_steps=bullets("Iterate with iterator", "Call iterator.remove() on matches", "Print list"),
            output="- Output: [1, 3]",
            complexity="- Time: O(n)\n- Space: O(1)",
            enterprise="Common in in-memory filtering in batch jobs; `removeIf` is clearer and less error-prone.",
            interview=bullets("Why CME happens", "Iterator.remove semantics", "fail-fast vs fail-safe"),
            best_practices=bullets("Prefer removeIf", "Don’t mutate collection in for-each", "Use concurrent collections when needed"),
        )

    if low == "comparable vs comparator":
        return render(
            title,
            concept=(
                "`Comparable` defines a natural ordering inside the type. `Comparator` defines external/custom orderings.\n\n"
                "ASCII:\nComparable: User implements compareTo\nComparator: Comparator<User> byName/byAge"
            ),
            problem="Sort users by multiple keys (age asc, then name asc) without changing the domain model.",
            intuition="Use Comparator composition (`comparing`, `thenComparing`) for flexible ordering and stable intent.",
            java_impl=textwrap.dedent(
                """\
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
                """\
            ),
            stream_impl=textwrap.dedent(
                """\
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
                """\
            ),
            sample_input='- Input: [(bob,30),(amy,30),(carl,25)]',
            execution_steps=bullets("Build comparator", "Sort", "Print"),
            output="- Output: [carl:25, amy:30, bob:30]",
            complexity="- Time: O(n log n)\n- Space: O(n) (if collecting sorted stream)",
            enterprise="Sorting is common in API responses and reports. Comparator composition avoids changing domain classes for one-off sort rules.",
            interview=bullets("Comparator stability", "compareTo contract", "null handling (nullsFirst/nullsLast)"),
            best_practices=bullets("Prefer Comparator composition", "Keep ordering consistent with equals when required", "Be explicit about nulls"),
        )

    # ---------------- Section 8: List Implementations ----------------
    if low == "list interface":
        return render(
            title,
            concept=(
                "`List` is an ordered collection that allows duplicates and supports positional access.\n\n"
                "Common implementations:\n- ArrayList: fast random access\n- LinkedList: fast adds/removes near ends (but poor locality)\n- CopyOnWriteArrayList: read-mostly concurrency"
            ),
            problem="Pick the right List implementation for read-heavy vs write-heavy workloads.",
            intuition="Choose by operations: random access -> ArrayList; frequent inserts/removals in middle -> usually still ArrayList unless proven otherwise; concurrent read-mostly -> CopyOnWriteArrayList.",
            java_impl=textwrap.dedent(
                """\
                import java.util.*;

                public class ListBasics {
                    public static void main(String[] args) {
                        List<String> xs = new ArrayList<>();
                        xs.add("a");
                        xs.add("b");
                        xs.add(1, "x");
                        System.out.println(xs);
                        System.out.println(xs.get(0));
                    }
                }
                """\
            ),
            stream_impl=textwrap.dedent(
                """\
                import java.util.*;
                import java.util.stream.*;

                public class ListStream {
                    public static void main(String[] args) {
                        List<String> xs = Arrays.asList(" a ", "b", "");
                        List<String> out = xs.stream().map(String::trim).filter(s -> !s.isEmpty()).collect(Collectors.toList());
                        System.out.println(out);
                    }
                }
                """\
            ),
            sample_input=bullets('Input: add a,b then add(1,"x")', 'Input: [" a ","b",""]'),
            execution_steps=bullets("Use positional add/get", "Normalize via stream", "Collect"),
            output=bullets("Output: [a, x, b]", "Output: [a, b]"),
            complexity="- get/set by index: O(1) for ArrayList, O(n) for LinkedList\n- insert at index: O(n)",
            enterprise="List choice affects latency and memory; ArrayList is the default in most services due to cache locality.",
            interview=bullets("ArrayList vs LinkedList", "Random access cost", "Fail-fast iterators"),
            best_practices=bullets("Program to List", "Prefer ArrayList by default", "Avoid LinkedList unless measured"),
        )

    if low == "arraylist internals":
        return render(
            title,
            concept=(
                "`ArrayList` is a resizable array. It stores elements in a contiguous `Object[]` and grows when capacity is exceeded.\n\n"
                "Key costs:\n- get/set: O(1)\n- add at end: amortized O(1)\n- insert/remove in middle: O(n) due to shifting"
            ),
            problem="Avoid performance regressions caused by repeated reallocation and shifting.",
            intuition="Pre-size when you know approximate size; avoid inserting/removing near the front in tight loops.",
            java_impl=textwrap.dedent(
                """\
                import java.util.*;

                public class ArrayListGrowth {
                    public static void main(String[] args) {
                        List<Integer> xs = new ArrayList<>(8); // pre-size
                        for (int i = 1; i <= 5; i++) xs.add(i);
                        xs.add(0, 99); // shifts elements right
                        System.out.println(xs);
                    }
                }
                """\
            ),
            stream_impl=textwrap.dedent(
                """\
                import java.util.*;
                import java.util.stream.*;

                public class ArrayListCollectors {
                    public static void main(String[] args) {
                        List<Integer> out = IntStream.rangeClosed(1, 5).boxed().collect(Collectors.toCollection(ArrayList::new));
                        System.out.println(out);
                    }
                }
                """\
            ),
            sample_input="- Input: add 1..5 then add(0,99)",
            execution_steps=bullets("Pre-size", "Append elements", "Insert at index (shift)"),
            output="- Output: [99, 1, 2, 3, 4, 5]",
            complexity="- add(end): amortized O(1)\n- add(index): O(n)\n- remove(index): O(n)",
            enterprise="ArrayList dominates typical service code; performance issues often come from accidental O(n^2) inserts/removes.",
            interview=bullets("Amortized analysis", "Growth factor", "Why shifting is costly"),
            best_practices=bullets("Pre-size when possible", "Prefer append", "Use ArrayDeque for queue semantics"),
        )

    if low == "linkedlist internals":
        return render(
            title,
            concept=(
                "`LinkedList` is a doubly-linked list. Each node stores prev/next pointers and the item.\n\n"
                "Costs:\n- get(i): O(n) traversal\n- add/remove at ends: O(1)\n- high memory overhead due to node objects"
            ),
            problem="Understand why LinkedList is rarely faster than ArrayList in real services.",
            intuition="Pointer chasing defeats CPU cache locality; only use when you truly need deque semantics and can’t use ArrayDeque.",
            java_impl=textwrap.dedent(
                """\
                import java.util.*;

                public class LinkedListDemo {
                    public static void main(String[] args) {
                        Deque<Integer> dq = new LinkedList<>();
                        dq.addFirst(2);
                        dq.addFirst(1);
                        dq.addLast(3);
                        System.out.println(dq.removeFirst());
                        System.out.println(dq);
                    }
                }
                """\
            ),
            stream_impl=GEN_STREAM,
            sample_input="- Input: addFirst(2), addFirst(1), addLast(3)",
            execution_steps=bullets("Use as Deque", "Remove from front", "Inspect remaining"),
            output=bullets("Output: 1", "Output: [2, 3]"),
            complexity="- addFirst/addLast/removeFirst: O(1)\n- get(i): O(n)",
            enterprise="Prefer ArrayDeque for queues/stacks. LinkedList adds allocation overhead and GC pressure.",
            interview=bullets("Why get(i) is O(n)", "Memory overhead", "LinkedList vs ArrayDeque"),
            best_practices=bullets("Use Deque interface", "Prefer ArrayDeque", "Avoid LinkedList for random access"),
        )

    if low == "vector":
        return render(
            title,
            concept=(
                "`Vector` is a legacy synchronized resizable array (pre-Collections framework era). Most methods are synchronized.\n\n"
                "Today: prefer `ArrayList` + external synchronization, or concurrent collections depending on requirements."
            ),
            problem="Understand why Vector is rarely used in modern Java.",
            intuition="Coarse-grained synchronization adds overhead and does not automatically make compound actions atomic.",
            java_impl=textwrap.dedent(
                """\
                import java.util.*;

                public class VectorDemo {
                    public static void main(String[] args) {
                        Vector<Integer> v = new Vector<>();
                        v.add(1);
                        v.add(2);
                        System.out.println(v);
                    }
                }
                """\
            ),
            stream_impl=GEN_STREAM,
            sample_input="- Input: add 1,2",
            execution_steps=bullets("Create Vector", "Add elements", "Print"),
            output="- Output: [1, 2]",
            complexity="- Similar to ArrayList, plus synchronization overhead",
            enterprise="Often appears in legacy code. Modern services typically avoid it unless constrained by old APIs.",
            interview=bullets("Vector vs ArrayList", "Synchronization semantics", "Why legacy"),
            best_practices=bullets("Prefer ArrayList", "Use Collections.synchronizedList when needed", "Prefer concurrent collections for high concurrency"),
        )

    if low == "copyonwritearraylist":
        return render(
            title,
            concept=(
                "`CopyOnWriteArrayList` is a thread-safe list optimized for read-mostly workloads. Writes copy the entire backing array.\n\n"
                "Iteration happens over a snapshot, so iterators do not throw ConcurrentModificationException."
            ),
            problem="Support safe iteration under concurrent reads while keeping reads lock-free.",
            intuition="Great when reads >> writes (config lists, listeners). Terrible for write-heavy workloads due to copying.",
            java_impl=textwrap.dedent(
                """\
                import java.util.*;
                import java.util.concurrent.*;

                public class COWDemo {
                    public static void main(String[] args) {
                        CopyOnWriteArrayList<String> xs = new CopyOnWriteArrayList<>(Arrays.asList("a", "b"));
                        for (String s : xs) {
                            if ("a".equals(s)) xs.add("c");
                        }
                        System.out.println(xs);
                    }
                }
                """\
            ),
            stream_impl=GEN_STREAM,
            sample_input='- Input: ["a","b"], add "c" during iteration',
            execution_steps=bullets("Iterate snapshot", "Write copies array", "Print list"),
            output="- Output: [a, b, c]",
            complexity="- read: O(1)\n- write: O(n) copy",
            enterprise="Common for listener registries and configuration snapshots. Avoid for frequently-updated lists.",
            interview=bullets("Snapshot iteration", "Why no CME", "When it’s a bad choice"),
            best_practices=bullets("Use for read-mostly", "Avoid large lists", "Consider alternatives (ReadWriteLock)"),
        )

    # ---------------- Section 9: Set Implementations ----------------
    if low == "set interface":
        return render(
            title,
            concept="`Set` is a collection that contains no duplicate elements. Uniqueness is defined by equals/hashCode.",
            problem="Deduplicate user ids and keep membership checks fast.",
            intuition="Use a Set when you need membership tests and uniqueness; avoid using List.contains in hot paths.",
            java_impl=textwrap.dedent(
                """\
                import java.util.*;

                public class SetBasics {
                    public static void main(String[] args) {
                        List<String> ids = Arrays.asList("u1", "u2", "u1");
                        Set<String> uniq = new HashSet<>(ids);
                        System.out.println(uniq.contains("u2"));
                        System.out.println(uniq);
                    }
                }
                """\
            ),
            stream_impl=textwrap.dedent(
                """\
                import java.util.*;
                import java.util.stream.*;

                public class SetStream {
                    public static void main(String[] args) {
                        List<String> ids = Arrays.asList("u1", "u2", "u1");
                        Set<String> uniq = ids.stream().collect(Collectors.toSet());
                        System.out.println(uniq);
                    }
                }
                """\
            ),
            sample_input='- Input: ["u1","u2","u1"]',
            execution_steps=bullets("Insert into HashSet", "Check contains", "Print"),
            output=bullets("Output: true", "Output: Set contains u1,u2"),
            complexity="- add/contains: O(1) average\n- Space: O(n)",
            enterprise="Sets are used for authorization checks, deduping event ids, and preventing duplicate processing.",
            interview=bullets("equals/hashCode contract", "HashSet vs TreeSet", "Why duplicates are dropped"),
            best_practices=bullets("Use Set for membership", "Don’t mutate keys", "Be explicit about ordering needs"),
        )

    if low == "hashset internals":
        return render(
            title,
            concept=(
                "`HashSet` is backed by a `HashMap` (elements are stored as keys with a dummy value).\n\n"
                "Lookup uses hashCode to find a bucket, then equals to resolve collisions."
            ),
            problem="Explain collisions and why poor hashCode causes performance regressions.",
            intuition="If many keys land in the same bucket, operations degrade toward O(n).",
            java_impl=textwrap.dedent(
                """\
                import java.util.*;

                public class HashSetDemo {
                    public static void main(String[] args) {
                        Set<String> s = new HashSet<>();
                        s.add("a");
                        s.add("a");
                        s.add("b");
                        System.out.println(s.size());
                        System.out.println(s.contains("b"));
                    }
                }
                """\
            ),
            stream_impl=GEN_STREAM,
            sample_input='- Input: add("a"), add("a"), add("b")',
            execution_steps=bullets("Compute hash", "Check bucket", "Use equals to detect duplicate"),
            output=bullets("Output: 2", "Output: true"),
            complexity="- Time: O(1) avg, O(n) worst-case\n- Space: O(n)",
            enterprise="Hot-path caches and dedupe sets rely on good hashing; poor keys can cause latency spikes.",
            interview=bullets("Collision handling", "Why equals/hashCode matters", "Load factor and resizing"),
            best_practices=bullets("Implement stable hashCode", "Avoid mutable keys", "Use appropriate initial capacity when large"),
        )

    if low == "linkedhashset":
        return render(
            title,
            concept="`LinkedHashSet` preserves insertion order while maintaining HashSet-like membership performance.",
            problem="Deduplicate while preserving the first-seen order for stable API responses.",
            intuition="Hash table + linked list of entries => deterministic iteration order.",
            java_impl=textwrap.dedent(
                """\
                import java.util.*;

                public class LinkedHashSetDemo {
                    public static void main(String[] args) {
                        Set<String> s = new LinkedHashSet<>(Arrays.asList("b", "a", "b", "c"));
                        System.out.println(s);
                    }
                }
                """\
            ),
            stream_impl=textwrap.dedent(
                """\
                import java.util.*;
                import java.util.stream.*;

                public class LinkedHashSetStream {
                    public static void main(String[] args) {
                        List<String> xs = Arrays.asList("b", "a", "b", "c");
                        Set<String> s = xs.stream().collect(Collectors.toCollection(LinkedHashSet::new));
                        System.out.println(s);
                    }
                }
                """\
            ),
            sample_input='- Input: ["b","a","b","c"]',
            execution_steps=bullets("Insert while keeping links", "Iterate in insertion order"),
            output="- Output: [b, a, c]",
            complexity="- Time: O(1) avg membership\n- Space: O(n)",
            enterprise="Stable iteration order avoids flaky tests and ensures deterministic JSON output.",
            interview=bullets("How order is preserved", "LinkedHashSet vs HashSet"),
            best_practices=bullets("Use for deterministic ordering", "Avoid if you don’t need order"),
        )

    if low == "treeset":
        return render(
            title,
            concept="`TreeSet` is a sorted set backed by a Red-Black tree. Ordering uses Comparable or a Comparator.",
            problem="Keep unique items sorted for range queries and ordered iteration.",
            intuition="Balanced BST gives O(log n) add/contains and ordered traversal.",
            java_impl=textwrap.dedent(
                """\
                import java.util.*;

                public class TreeSetDemo {
                    public static void main(String[] args) {
                        SortedSet<Integer> s = new TreeSet<>(Arrays.asList(3, 1, 2, 2));
                        System.out.println(s);
                        System.out.println(s.subSet(1, 3));
                    }
                }
                """\
            ),
            stream_impl=GEN_STREAM,
            sample_input="- Input: [3,1,2,2]",
            execution_steps=bullets("Insert into RB-tree", "Iterate sorted", "Use subSet range view"),
            output=bullets("Output: [1, 2, 3]", "Output: [1, 2]"),
            complexity="- add/contains: O(log n)\n- Space: O(n)",
            enterprise="Used for ordered leaderboards, time-based indices, and range queries; slower than HashSet for pure membership.",
            interview=bullets("Why TreeSet is log n", "Comparator consistency", "NavigableSet operations"),
            best_practices=bullets("Provide Comparator for domain types", "Keep comparator consistent with equals"),
        )

    # ---------------- Section 10: Map Implementations ----------------
    if low == "map interface":
        return render(
            title,
            concept=(
                "`Map` stores key->value associations. Keys are unique (as defined by equals/hashCode), values may repeat.\n\n"
                "Map is not a Collection: it has different semantics (key-based lookup)."
            ),
            problem="Count occurrences of items and query by key efficiently.",
            intuition="Use HashMap for average O(1) get/put; use TreeMap when you need sorted keys.",
            java_impl=textwrap.dedent(
                """\
                import java.util.*;

                public class MapBasics {
                    public static void main(String[] args) {
                        Map<String, Integer> m = new HashMap<>();
                        m.put("a", 1);
                        m.put("b", 2);
                        m.put("a", 9); // overwrite
                        System.out.println(m.get("a"));
                        System.out.println(m.containsKey("c"));
                    }
                }
                """\
            ),
            stream_impl=textwrap.dedent(
                """\
                import java.util.*;
                import java.util.stream.*;

                public class MapCountingStream {
                    public static void main(String[] args) {
                        List<String> xs = Arrays.asList("a", "b", "a");
                        Map<String, Long> counts = xs.stream()
                                .collect(Collectors.groupingBy(s -> s, Collectors.counting()));
                        System.out.println(counts);
                    }
                }
                """\
            ),
            sample_input=bullets('Input: put a=1, b=2, a=9', 'Input: ["a","b","a"]'),
            execution_steps=bullets("Put values (overwrite on same key)", "Get by key", "Count via groupingBy"),
            output=bullets("Output: 9", "Output: false", "Output: {a=2, b=1}"),
            complexity="- put/get: O(1) avg for HashMap\n- Space: O(n)",
            enterprise="Maps back caches, request-context attributes, aggregations, and indexing in services.",
            interview=bullets("Key uniqueness", "containsKey vs get==null", "Why Map isn't a Collection"),
            best_practices=bullets("Use immutable keys", "Be explicit about null values", "Prefer Map API methods (compute/merge)"),
        )

    if low == "hashmap internals":
        return render(
            title,
            concept=(
                "`HashMap` uses an array of buckets. A key's hash determines the bucket; collisions are handled within the bucket.\n\n"
                "In Java 8, heavily-collided buckets may be treeified (converted to a small tree) to improve worst-case performance."
            ),
            problem="Explain collisions, resizing, and why hashCode quality matters.",
            intuition="Average O(1) relies on good hash distribution; resizing rehashes entries when load factor threshold is exceeded.",
            java_impl=textwrap.dedent(
                """\
                import java.util.*;

                public class HashMapDemo {
                    public static void main(String[] args) {
                        Map<String, Integer> m = new HashMap<>();
                        m.put("a", 1);
                        m.put("b", 2);
                        System.out.println(m.get("b"));
                        System.out.println(m.size());
                    }
                }
                """\
            ),
            stream_impl=GEN_STREAM,
            sample_input='- Input: put(a,1), put(b,2), get(b)',
            execution_steps=bullets("Compute hash", "Locate bucket", "Scan bucket (equals)", "Return value"),
            output=bullets("Output: 2", "Output: 2"),
            complexity="- Time: O(1) avg, O(n) worst-case (improved in Java 8 with tree bins)\n- Space: O(n)",
            enterprise="HashMap performance impacts caches and hot-path lookups; bad keys can cause CPU spikes and GC pressure.",
            interview=bullets("Load factor and resizing", "Collision resolution", "Why mutable keys are dangerous"),
            best_practices=bullets("Implement stable hashCode/equals", "Avoid mutable keys", "Consider initial capacity for large maps"),
        )

    if low == "hashmap java 8 improvements":
        return render(
            title,
            concept=(
                "Java 8 improved HashMap under high collision by introducing *tree bins* (bucket can become a tree) and also added richer Map APIs (`computeIfAbsent`, `merge`, etc.).\n\n"
                "Practical impact: worst-case performance improves, and common update patterns become less error-prone."
            ),
            problem="Build a frequency map safely and concisely using Java 8 Map APIs.",
            intuition="Use `merge` for counters and `computeIfAbsent` for initializing collections.",
            java_impl=textwrap.dedent(
                """\
                import java.util.*;

                public class MapImprovements {
                    public static void main(String[] args) {
                        List<String> xs = Arrays.asList("a", "b", "a");
                        Map<String, Integer> freq = new HashMap<>();
                        for (String s : xs) {
                            freq.merge(s, 1, Integer::sum);
                        }
                        System.out.println(freq);

                        Map<String, List<String>> groups = new HashMap<>();
                        groups.computeIfAbsent("k", k -> new ArrayList<>()).add("v1");
                        System.out.println(groups);
                    }
                }
                """\
            ),
            stream_impl=textwrap.dedent(
                """\
                import java.util.*;
                import java.util.stream.*;

                public class FreqStream {
                    public static void main(String[] args) {
                        List<String> xs = Arrays.asList("a", "b", "a");
                        Map<String, Long> freq = xs.stream().collect(Collectors.groupingBy(s -> s, Collectors.counting()));
                        System.out.println(freq);
                    }
                }
                """\
            ),
            sample_input=bullets('Input: ["a","b","a"]', 'Input: computeIfAbsent("k").add("v1")'),
            execution_steps=bullets("Use merge for counters", "Use computeIfAbsent for multi-map", "Print maps"),
            output=bullets("Output: {a=2, b=1}", "Output: {k=[v1]}", "Output: {a=2, b=1} (stream)"),
            complexity="- Time: O(n)\n- Space: O(n)",
            enterprise="Map API methods reduce race-prone and bug-prone update code, especially with ConcurrentHashMap.",
            interview=bullets("merge vs compute", "computeIfAbsent pitfalls", "tree bins conceptually"),
            best_practices=bullets("Keep remapping functions pure", "Avoid heavy work inside computeIfAbsent", "Prefer merge for counters"),
        )

    # ---------------- Section 11: Map API methods ----------------
    if low in ("putifabsent", "compute", "computeifabsent", "computeifpresent", "merge", "replace", "replaceall", "getordefault", "foreach"):
        method = title.strip()
        spec = {
            "putifabsent": {
                "setup": 'm.put("a", 1);',
                "before": "{a=1}",
                "op": 'm.putIfAbsent("a", 9);',
                "stdout": "",
                "after": "{a=1}",
                "note": "Existing value is kept; only inserts if key missing.",
            },
            "compute": {
                "setup": 'm.put("a", 1);',
                "before": "{a=1}",
                "op": 'm.compute("a", (k,v) -> v == null ? 1 : v + 1);',
                "stdout": "",
                "after": "{a=2}",
                "note": "Recomputes value using remapping function (can remove by returning null).",
            },
            "computeifabsent": {
                "setup": 'm.put("a", 1);',
                "before": "{a=1}",
                "op": 'm.computeIfAbsent("b", k -> 10);',
                "stdout": "",
                "after": "{a=1, b=10}",
                "note": "Computes value only when key is missing.",
            },
            "computeifpresent": {
                "setup": 'm.put("a", 1);',
                "before": "{a=1}",
                "op": 'm.computeIfPresent("a", (k,v) -> v + 100);',
                "stdout": "",
                "after": "{a=101}",
                "note": "Runs only when key exists.",
            },
            "merge": {
                "setup": 'm.put("a", 1);',
                "before": "{a=1}",
                "op": 'm.merge("a", 5, Integer::sum);',
                "stdout": "",
                "after": "{a=6}",
                "note": "Great for counters; merges existing with new value.",
            },
            "replace": {
                "setup": 'm.put("a", 1);',
                "before": "{a=1}",
                "op": 'm.replace("a", 999);',
                "stdout": "",
                "after": "{a=999}",
                "note": "Replaces value only if key exists.",
            },
            "replaceall": {
                "setup": 'm.put("a", 1); m.put("b", 2);',
                "before": "{a=1, b=2}",
                "op": 'm.replaceAll((k,v) -> v * 2);',
                "stdout": "",
                "after": "{a=2, b=4}",
                "note": "Applies remapping to every entry.",
            },
            "getordefault": {
                "setup": 'm.put("a", 1);',
                "before": "{a=1}",
                "op": 'System.out.println(m.getOrDefault("missing", -1));',
                "stdout": "-1",
                "after": "{a=1}",
                "note": "Returns default when key absent; does not mutate map.",
            },
            "foreach": {
                "setup": 'm.put("a", 1); m.put("b", 2);',
                "before": "{a=1, b=2}",
                "op": 'm.forEach((k,v) -> System.out.println(k + "=" + v));',
                "stdout": "a=1\nb=2",
                "after": "{a=1, b=2}",
                "note": "Iterates entries; use LinkedHashMap if you need deterministic iteration order.",
            },
        }[low]
        return render(
            title,
            concept=f"Java 8 Map method `{method}` reduces boilerplate map-update code.",
            problem="Update counters and defaults safely without containsKey/get/put patterns.",
            intuition="Centralize update logic in one atomic-ish call (still understand ConcurrentHashMap guarantees).",
            java_impl=textwrap.dedent(
                f"""\
                import java.util.*;

                public class MapApiDemo {{
                    public static void main(String[] args) {{
                        Map<String, Integer> m = new LinkedHashMap<>();
                        {spec["setup"]}
                        {spec["op"]}
                        if (!"".equals("{spec['stdout']}")) {{
                            // stdout already printed by op
                        }}
                        System.out.println(m);
                    }}
                }}
                """
            ),
            stream_impl=GEN_STREAM,
            sample_input=bullets(
                f"Input: before = {spec['before']}",
                f"Input: operation = {method}",
            ),
            execution_steps=bullets("Initialize map", f"Run {method}", "Print after"),
            output=bullets(
                f"Output: stdout = {spec['stdout'] if spec['stdout'] else '(none)'}",
                f"Output: after = {spec['after']}",
                f"Output note: {spec['note']}",
            ),
            complexity="- Time: O(1) average\n- Space: O(1)",
            enterprise="Common in caches, aggregation maps, and counters. Avoid expensive remapping functions.",
            interview=bullets("computeIfAbsent vs putIfAbsent", "merge vs compute", "ConcurrentHashMap semantics"),
            best_practices=bullets("Keep functions pure", "Avoid heavy work in computeIfAbsent"),
        )

    # ---------------- Section 12: Concurrency ----------------
    if low == "threads vs processes":
        return render(
            title,
            concept=(
                "A *process* has its own address space (memory isolation). A *thread* is a unit of execution within a process and shares heap memory with other threads in the same process.\n\n"
                "Threads are cheaper to create/switch than processes, but require careful synchronization when sharing mutable state."
            ),
            problem="Run two tasks concurrently and understand what is shared (heap) vs isolated (process memory).",
            intuition=(
                "Use threads for concurrency inside a JVM process. Use processes/containers for isolation and separate failure domains.\n\n"
                "ASCII:\nProcess: [Heap] shared by Thread-1, Thread-2"
            ),
            java_impl=textwrap.dedent(
                """\
                public class ThreadsVsProcesses {
                    static class Counter { int x = 0; }

                    public static void main(String[] args) throws Exception {
                        Counter c = new Counter();
                        Thread t1 = new Thread(() -> c.x++);
                        Thread t2 = new Thread(() -> c.x++);
                        t1.start();
                        t2.start();
                        t1.join();
                        t2.join();
                        System.out.println(c.x); // shared heap state
                    }
                }
                """\
            ),
            stream_impl=GEN_STREAM,
            sample_input="- Input: start two threads that increment shared counter once",
            execution_steps=bullets("Create shared object", "Start threads", "Join", "Read shared state"),
            output="- Output: 2",
            complexity="- Time: O(1)\n- Space: O(1)",
            enterprise="Threads are used for request handling and async work. Processes are used for isolation and scaling boundaries.",
            interview=bullets("What is shared between threads?", "Context switching", "Isolation trade-offs"),
            best_practices=bullets("Prefer thread pools", "Avoid sharing mutable state", "Use processes for isolation"),
        )

    if low == "thread lifecycle":
        return render(
            title,
            concept=(
                "A thread moves through states like NEW -> RUNNABLE -> (BLOCKED/WAITING/TIMED_WAITING) -> TERMINATED.\n\n"
                "In practice, you use `start()`, coordinate with `join()`, and synchronize via locks/monitors/conditions."
            ),
            problem="Observe a thread state before start and after completion deterministically.",
            intuition="`getState()` is a snapshot; the thread may move between states quickly.",
            java_impl=textwrap.dedent(
                """\
                public class ThreadLifecycleDemo {
                    public static void main(String[] args) throws Exception {
                        Thread t = new Thread(() -> System.out.println("work"));
                        System.out.println(t.getState()); // NEW
                        t.start();
                        t.join();
                        System.out.println(t.getState()); // TERMINATED
                    }
                }
                """\
            ),
            stream_impl=GEN_STREAM,
            sample_input="- Input: create thread, start, join",
            execution_steps=bullets("Create thread (NEW)", "Start", "Join", "Observe TERMINATED"),
            output=bullets("Output: NEW", "Output: work", "Output: TERMINATED"),
            complexity="- Time: O(1)\n- Space: O(1)",
            enterprise="Understanding lifecycle helps debug stuck threads, deadlocks, and slowdowns in production.",
            interview=bullets("Difference between RUNNABLE and RUNNING", "BLOCKED vs WAITING", "join semantics"),
            best_practices=bullets("Name threads", "Avoid creating threads per request", "Use executors"),
        )

    if low == "synchronization":
        return render(
            title,
            concept=(
                "Synchronization ensures mutual exclusion and establishes *happens-before* relationships so threads see consistent memory updates.\n\n"
                "In Java, `synchronized` uses an intrinsic monitor lock on an object."
            ),
            problem="Update a shared counter from multiple threads and get the correct final result.",
            intuition="Without synchronization, increments can be lost. With synchronization, the critical section is protected.",
            java_impl=textwrap.dedent(
                """\
                public class SyncCounter {
                    static class Counter {
                        private int x = 0;
                        synchronized void inc() { x++; }
                        synchronized int get() { return x; }
                    }

                    public static void main(String[] args) throws Exception {
                        Counter c = new Counter();
                        Thread t1 = new Thread(() -> { for (int i = 0; i < 10000; i++) c.inc(); });
                        Thread t2 = new Thread(() -> { for (int i = 0; i < 10000; i++) c.inc(); });
                        t1.start();
                        t2.start();
                        t1.join();
                        t2.join();
                        System.out.println(c.get());
                    }
                }
                """\
            ),
            stream_impl=GEN_STREAM,
            sample_input="- Input: two threads, each inc 10000 times",
            execution_steps=bullets("Enter synchronized inc", "Prevent lost updates", "Join threads", "Print counter"),
            output="- Output: 20000",
            complexity="- Time: O(n)\n- Space: O(1)",
            enterprise="Incorrect synchronization leads to data corruption, flaky behavior, and hard-to-debug incidents.",
            interview=bullets("Monitor lock", "Happens-before", "Why ++ is not atomic"),
            best_practices=bullets("Keep critical sections small", "Prefer higher-level concurrency primitives", "Avoid deadlocks"),
        )

    if low == "volatile keyword":
        return render(
            title,
            concept=(
                "`volatile` provides visibility guarantees: writes to a volatile field by one thread become visible to reads by other threads.\n\n"
                "It does *not* make compound actions (like ++ or check-then-act) atomic."
            ),
            problem="Safely publish a stop flag so a worker thread can terminate.",
            intuition="Use volatile for simple state flags; use locks/atomics for compound updates.",
            java_impl=textwrap.dedent(
                """\
                public class VolatileFlag {
                    static volatile boolean stop = false;

                    public static void main(String[] args) throws Exception {
                        Thread worker = new Thread(() -> {
                            while (!stop) {
                                // busy wait
                            }
                            System.out.println("stopped");
                        });
                        worker.start();
                        stop = true;
                        worker.join();
                    }
                }
                """\
            ),
            stream_impl=GEN_STREAM,
            sample_input="- Input: stop=false then stop=true",
            execution_steps=bullets("Worker polls volatile", "Main writes stop=true", "Worker observes and exits"),
            output="- Output: stopped",
            complexity="- Time: depends on polling\n- Space: O(1)",
            enterprise="Volatile flags are common in shutdown hooks and component lifecycle management.",
            interview=bullets("Visibility vs atomicity", "Why volatile doesn't fix ++", "Memory barriers (conceptual)"),
            best_practices=bullets("Avoid busy-wait in production (use interrupts/locks)", "Use Atomic* for counters", "Keep volatile fields simple"),
        )

    if low == "locks and reentrantlock":
        return render(
            title,
            concept=(
                "`ReentrantLock` is an explicit lock with features beyond `synchronized` (tryLock, fairness, conditions).\n\n"
                "It is reentrant: the same thread can acquire it multiple times."
            ),
            problem="Protect a critical section with try/finally to avoid deadlocks on exceptions.",
            intuition="Always unlock in a finally block; prefer lock-based code when you need tryLock/timeouts/conditions.",
            java_impl=textwrap.dedent(
                """\
                import java.util.concurrent.locks.*;

                public class LockCounter {
                    static class Counter {
                        private final Lock lock = new ReentrantLock();
                        private int x = 0;
                        void inc() {
                            lock.lock();
                            try { x++; }
                            finally { lock.unlock(); }
                        }
                        int get() { return x; }
                    }

                    public static void main(String[] args) throws Exception {
                        Counter c = new Counter();
                        Thread t1 = new Thread(() -> { for (int i = 0; i < 10000; i++) c.inc(); });
                        Thread t2 = new Thread(() -> { for (int i = 0; i < 10000; i++) c.inc(); });
                        t1.start();
                        t2.start();
                        t1.join();
                        t2.join();
                        System.out.println(c.get());
                    }
                }
                """\
            ),
            stream_impl=GEN_STREAM,
            sample_input="- Input: two threads inc 10000 each",
            execution_steps=bullets("Acquire lock", "Update shared state", "Unlock in finally", "Join", "Print"),
            output="- Output: 20000",
            complexity="- Time: O(n)\n- Space: O(1)",
            enterprise="Locks are common in in-memory caches, rate limiters, and shared state. Prefer minimizing lock contention.",
            interview=bullets("synchronized vs ReentrantLock", "fairness", "tryLock and deadlock avoidance"),
            best_practices=bullets("Always unlock in finally", "Keep critical sections small", "Prefer lock-free/atomics when possible"),
        )

    # ---------------- Section 13: Executor Framework ----------------
    if low == "executor interface":
        return render(
            title,
            concept="`Executor` is the minimal abstraction for running tasks asynchronously via `execute(Runnable)`.",
            problem="Decouple task submission from the threading policy.",
            intuition="Callers submit work; the executor decides how/when to run it (thread-per-task, pool, etc.).",
            java_impl=textwrap.dedent(
                """\
                import java.util.concurrent.*;

                public class ExecutorInterfaceDemo {
                    public static void main(String[] args) throws Exception {
                        Executor ex = command -> new Thread(command).start();
                        CountDownLatch latch = new CountDownLatch(1);
                        ex.execute(() -> {
                            System.out.println("done");
                            latch.countDown();
                        });
                        latch.await();
                    }
                }
                """\
            ),
            stream_impl=GEN_STREAM,
            sample_input="- Input: submit one Runnable",
            execution_steps=bullets("Create Executor", "Execute task", "Await latch"),
            output="- Output: done",
            complexity="- N/A (concept)",
            enterprise="Executor abstraction enables swapping policies (bounded pools, tracing executors) without changing business logic.",
            interview=bullets("Executor vs ExecutorService", "Why execute returns void"),
            best_practices=bullets("Prefer ExecutorService for lifecycle control", "Avoid creating raw threads per task"),
        )

    if low == "executorservice":
        return render(
            title,
            concept="`ExecutorService` extends Executor with lifecycle (`shutdown`) and task submission returning `Future`.",
            problem="Run a Callable task and get its result deterministically.",
            intuition="Use `submit(Callable)` to get a Future; always shutdown the pool.",
            java_impl=textwrap.dedent(
                """\
                import java.util.concurrent.*;

                public class ExecutorServiceDemo {
                    public static void main(String[] args) throws Exception {
                        ExecutorService es = Executors.newFixedThreadPool(2);
                        try {
                            Future<Integer> f = es.submit(() -> 40 + 2);
                            System.out.println(f.get());
                        } finally {
                            es.shutdown();
                        }
                    }
                }
                """\
            ),
            stream_impl=GEN_STREAM,
            sample_input="- Input: Callable returns 42",
            execution_steps=bullets("Create pool", "Submit callable", "Future.get", "Shutdown"),
            output="- Output: 42",
            complexity="- N/A (concept)",
            enterprise="Thread pools prevent unbounded thread creation and support graceful shutdowns.",
            interview=bullets("shutdown vs shutdownNow", "Future.get blocking", "submit vs execute"),
            best_practices=bullets("Always shutdown", "Use bounded queues", "Set thread names"),
        )

    if low == "threadpoolexecutor":
        return render(
            title,
            concept=(
                "`ThreadPoolExecutor` is the configurable implementation behind most executor factories.\n\n"
                "Key knobs: corePoolSize, maxPoolSize, keepAliveTime, workQueue, RejectedExecutionHandler."
            ),
            problem="Use a bounded queue and observe deterministic completion of submitted tasks.",
            intuition="Bounded queues and rejection policies protect services from overload (backpressure).",
            java_impl=textwrap.dedent(
                """\
                import java.util.concurrent.*;
                import java.util.*;

                public class ThreadPoolExecutorDemo {
                    public static void main(String[] args) throws Exception {
                        ThreadPoolExecutor ex = new ThreadPoolExecutor(
                                1, 1,
                                0L, TimeUnit.MILLISECONDS,
                                new ArrayBlockingQueue<>(10)
                        );
                        try {
                            List<Future<Integer>> fs = new ArrayList<>();
                            for (int i = 0; i < 3; i++) {
                                final int x = i;
                                fs.add(ex.submit(() -> x * 2));
                            }
                            for (Future<Integer> f : fs) System.out.println(f.get());
                        } finally {
                            ex.shutdown();
                        }
                    }
                }
                """\
            ),
            stream_impl=GEN_STREAM,
            sample_input="- Input: tasks i=0..2 return i*2",
            execution_steps=bullets("Create bounded pool", "Submit tasks", "Future.get", "Shutdown"),
            output=bullets("Output: 0", "Output: 2", "Output: 4"),
            complexity="- N/A (concept)",
            enterprise="Configuring pool sizes/queues is crucial for API servers to avoid OOM and latency collapse under load.",
            interview=bullets("Work queue types", "Rejection policies", "Core vs max threads"),
            best_practices=bullets("Use bounded queues", "Instrument queue depth", "Avoid unbounded cached pools"),
        )

    if low == "scheduledexecutorservice":
        return render(
            title,
            concept="`ScheduledExecutorService` schedules delayed or periodic tasks (better than Timer).",
            problem="Run a delayed task and block until it completes.",
            intuition="Use `schedule` for one-shot delayed tasks; prefer fixed-rate/fixed-delay for periodic tasks.",
            java_impl=textwrap.dedent(
                """\
                import java.util.concurrent.*;

                public class ScheduledDemo {
                    public static void main(String[] args) throws Exception {
                        ScheduledExecutorService ses = Executors.newScheduledThreadPool(1);
                        try {
                            ScheduledFuture<String> f = ses.schedule(() -> "tick", 10, TimeUnit.MILLISECONDS);
                            System.out.println(f.get());
                        } finally {
                            ses.shutdown();
                        }
                    }
                }
                """\
            ),
            stream_impl=GEN_STREAM,
            sample_input="- Input: schedule callable with 10ms delay",
            execution_steps=bullets("Create scheduler", "Schedule", "Future.get", "Shutdown"),
            output="- Output: tick",
            complexity="- N/A (concept)",
            enterprise="Used for retries, timeouts, cache refresh, and cron-like background tasks.",
            interview=bullets("Fixed-rate vs fixed-delay", "Timer pitfalls"),
            best_practices=bullets("Handle exceptions inside tasks", "Use separate pools for long tasks", "Shutdown gracefully"),
        )

    if low == "forkjoinpool":
        return render(
            title,
            concept="`ForkJoinPool` is a work-stealing pool optimized for many small CPU-bound tasks (used by parallel streams).",
            problem="Run a small recursive task and get deterministic result.",
            intuition="Split work into subtasks (fork) and combine results (join).",
            java_impl=textwrap.dedent(
                """\
                import java.util.concurrent.*;

                public class ForkJoinDemo {
                    static class SumTask extends RecursiveTask<Integer> {
                        final int lo, hi;
                        SumTask(int lo, int hi) { this.lo = lo; this.hi = hi; }
                        protected Integer compute() {
                            if (hi - lo <= 2) {
                                int s = 0;
                                for (int i = lo; i <= hi; i++) s += i;
                                return s;
                            }
                            int mid = (lo + hi) / 2;
                            SumTask left = new SumTask(lo, mid);
                            SumTask right = new SumTask(mid + 1, hi);
                            left.fork();
                            int r = right.compute();
                            return left.join() + r;
                        }
                    }

                    public static void main(String[] args) {
                        ForkJoinPool p = new ForkJoinPool(2);
                        int sum = p.invoke(new SumTask(1, 5));
                        System.out.println(sum);
                        p.shutdown();
                    }
                }
                """\
            ),
            stream_impl=GEN_STREAM,
            sample_input="- Input: sum range 1..5",
            execution_steps=bullets("Split task", "Fork/join", "Combine sums"),
            output="- Output: 15",
            complexity="- Work: O(n)\n- Span: O(log n) splits",
            enterprise="ForkJoin excels for CPU-bound divide-and-conquer; avoid for IO-bound tasks.",
            interview=bullets("Work stealing", "RecursiveTask vs RecursiveAction", "Common pool"),
            best_practices=bullets("Keep tasks small but not tiny", "Avoid blocking inside FJ threads", "Prefer explicit pools in servers"),
        )

    # ---------------- Section 14: CompletableFuture ----------------
    if low == "completablefuture overview":
        return render(
            title,
            concept=(
                "`CompletableFuture` represents a value that will be available later. It supports non-blocking composition (thenApply/thenCompose/thenCombine) and error handling.\n\n"
                "Key idea: build a pipeline of stages; block only at the boundary (`join`/`get`)."
            ),
            problem="Compose two async steps and get a final result deterministically.",
            intuition="Prefer composition over blocking. Each stage runs after the previous completes.",
            java_impl=textwrap.dedent(
                """\
                import java.util.concurrent.*;

                public class CfOverview {
                    public static void main(String[] args) {
                        CompletableFuture<Integer> cf = CompletableFuture.supplyAsync(() -> 40)
                                .thenApply(x -> x + 2);
                        System.out.println(cf.join());
                    }
                }
                """\
            ),
            stream_impl=GEN_STREAM,
            sample_input="- Input: supply 40 then +2",
            execution_steps=bullets("Create CF", "Compose thenApply", "Join at boundary"),
            output="- Output: 42",
            complexity="- N/A (concept)",
            enterprise="Used for async IO orchestration, fan-out/fan-in calls, and non-blocking pipelines in services.",
            interview=bullets("join vs get", "Default executor", "Threading of stages"),
            best_practices=bullets("Avoid blocking inside stages", "Use explicit executors", "Handle exceptions"),
        )

    if low == "supplyasync":
        return render(
            title,
            concept="`supplyAsync` runs a Supplier asynchronously and completes with a value.",
            problem="Run async computation and return a value.",
            intuition="Use supplyAsync when you produce a value; use an Executor to control threads.",
            java_impl=textwrap.dedent(
                """\
                import java.util.concurrent.*;

                public class SupplyAsyncDemo {
                    public static void main(String[] args) {
                        ExecutorService es = Executors.newFixedThreadPool(1);
                        try {
                            CompletableFuture<String> cf = CompletableFuture.supplyAsync(() -> "hello", es);
                            System.out.println(cf.join());
                        } finally {
                            es.shutdown();
                        }
                    }
                }
                """\
            ),
            stream_impl=GEN_STREAM,
            sample_input="- Input: Supplier returns 'hello'",
            execution_steps=bullets("Create executor", "supplyAsync", "join", "shutdown"),
            output="- Output: hello",
            complexity="- N/A (concept)",
            enterprise="Use explicit executors to avoid saturating the common pool in application servers.",
            interview=bullets("Common pool", "Executor overloads"),
            best_practices=bullets("Always shutdown custom executors", "Keep suppliers fast or isolate them"),
        )

    if low == "runasync":
        return render(
            title,
            concept="`runAsync` runs a Runnable asynchronously and completes with no value.",
            problem="Fire an async side-effect (logging/audit) and wait for completion at boundary.",
            intuition="Use runAsync for side effects; prefer keeping side effects at edges.",
            java_impl=textwrap.dedent(
                """\
                import java.util.concurrent.*;

                public class RunAsyncDemo {
                    public static void main(String[] args) {
                        CompletableFuture<Void> cf = CompletableFuture.runAsync(() -> System.out.println("audit"));
                        cf.join();
                        System.out.println("done");
                    }
                }
                """\
            ),
            stream_impl=GEN_STREAM,
            sample_input="- Input: runnable prints audit",
            execution_steps=bullets("runAsync", "join", "continue"),
            output=bullets("Output: audit", "Output: done"),
            complexity="- N/A (concept)",
            enterprise="Useful for async audit trails and background updates, but ensure failures are handled/observed.",
            interview=bullets("Void CF", "exception propagation"),
            best_practices=bullets("Observe exceptions", "Avoid fire-and-forget without monitoring"),
        )

    if low == "thenapply":
        return render(
            title,
            concept="`thenApply` transforms a completed value (T -> U).",
            problem="Parse and transform a value in an async pipeline.",
            intuition="Use thenApply for synchronous mapping; use thenCompose for async flattening.",
            java_impl=textwrap.dedent(
                """\
                import java.util.concurrent.*;

                public class ThenApplyDemo {
                    public static void main(String[] args) {
                        CompletableFuture<Integer> cf = CompletableFuture.supplyAsync(() -> "21")
                                .thenApply(Integer::parseInt)
                                .thenApply(x -> x * 2);
                        System.out.println(cf.join());
                    }
                }
                """\
            ),
            stream_impl=GEN_STREAM,
            sample_input='- Input: "21"',
            execution_steps=bullets("supplyAsync", "thenApply parse", "thenApply multiply", "join"),
            output="- Output: 42",
            complexity="- N/A (concept)",
            enterprise="Used for decoding responses and mapping DTOs in async client pipelines.",
            interview=bullets("thenApply vs thenApplyAsync", "Which thread runs it?"),
            best_practices=bullets("Keep mapping fast", "Use explicit executors for heavy transforms"),
        )

    if low == "thencompose":
        return render(
            title,
            concept="`thenCompose` flattens nested futures: T -> CompletionStage<U> becomes CompletionStage<U>.",
            problem="Call async step2 that depends on result of step1.",
            intuition="thenCompose is like flatMap for futures.",
            java_impl=textwrap.dedent(
                """\
                import java.util.concurrent.*;

                public class ThenComposeDemo {
                    static CompletableFuture<Integer> fetchUserId() {
                        return CompletableFuture.completedFuture(7);
                    }
                    static CompletableFuture<String> fetchEmail(int userId) {
                        return CompletableFuture.completedFuture("u" + userId + "@x.com");
                    }
                    public static void main(String[] args) {
                        String email = fetchUserId().thenCompose(ThenComposeDemo::fetchEmail).join();
                        System.out.println(email);
                    }
                }
                """\
            ),
            stream_impl=GEN_STREAM,
            sample_input="- Input: userId=7",
            execution_steps=bullets("Fetch userId", "thenCompose fetchEmail", "join"),
            output="- Output: u7@x.com",
            complexity="- N/A (concept)",
            enterprise="Common for dependent remote calls (user -> profile -> preferences) without blocking.",
            interview=bullets("thenCompose vs thenApply", "flatMap analogy"),
            best_practices=bullets("Avoid blocking between stages", "Add timeouts/retries at boundaries"),
        )

    if low == "thencombine":
        return render(
            title,
            concept="`thenCombine` combines two independent futures when both complete.",
            problem="Fetch two independent values and merge into one response.",
            intuition="Fan-out two futures, thenCombine to build the final DTO.",
            java_impl=textwrap.dedent(
                """\
                import java.util.concurrent.*;

                public class ThenCombineDemo {
                    public static void main(String[] args) {
                        CompletableFuture<Integer> a = CompletableFuture.completedFuture(40);
                        CompletableFuture<Integer> b = CompletableFuture.completedFuture(2);
                        CompletableFuture<Integer> c = a.thenCombine(b, Integer::sum);
                        System.out.println(c.join());
                    }
                }
                """\
            ),
            stream_impl=GEN_STREAM,
            sample_input="- Input: a=40, b=2",
            execution_steps=bullets("Create futures", "thenCombine(sum)", "join"),
            output="- Output: 42",
            complexity="- N/A (concept)",
            enterprise="Used for aggregating data from multiple services in parallel.",
            interview=bullets("thenCombine vs allOf", "failure propagation"),
            best_practices=bullets("Use timeouts", "Limit concurrency", "Handle partial failures"),
        )

    if low == "exceptionally":
        return render(
            title,
            concept="`exceptionally` provides a fallback value when a stage completes exceptionally.",
            problem="Return a default value when parsing fails.",
            intuition="Handle exceptions close to where they can occur, or map them to domain errors.",
            java_impl=textwrap.dedent(
                """\
                import java.util.concurrent.*;

                public class ExceptionallyDemo {
                    public static void main(String[] args) {
                        CompletableFuture<Integer> cf = CompletableFuture.supplyAsync(() -> "x")
                                .thenApply(Integer::parseInt)
                                .exceptionally(ex -> -1);
                        System.out.println(cf.join());
                    }
                }
                """\
            ),
            stream_impl=GEN_STREAM,
            sample_input='- Input: "x" (invalid int)',
            execution_steps=bullets("supplyAsync", "thenApply parse (throws)", "exceptionally fallback", "join"),
            output="- Output: -1",
            complexity="- N/A (concept)",
            enterprise="Critical for resilient clients. Decide if fallback is acceptable or you must propagate errors.",
            interview=bullets("exceptionally vs handle", "Where exception is caught"),
            best_practices=bullets("Don’t swallow errors silently", "Add metrics/logging", "Map to domain errors"),
        )

    if low == "allof":
        return render(
            title,
            concept="`allOf` completes when all futures complete (returns CompletableFuture<Void>).",
            problem="Wait for multiple async operations and then build a combined result.",
            intuition="Use allOf for fan-in; read individual results after it completes.",
            java_impl=textwrap.dedent(
                """\
                import java.util.concurrent.*;

                public class AllOfDemo {
                    public static void main(String[] args) {
                        CompletableFuture<Integer> a = CompletableFuture.completedFuture(1);
                        CompletableFuture<Integer> b = CompletableFuture.completedFuture(2);
                        CompletableFuture<Void> all = CompletableFuture.allOf(a, b);
                        all.join();
                        System.out.println(a.join() + b.join());
                    }
                }
                """\
            ),
            stream_impl=GEN_STREAM,
            sample_input="- Input: a=1, b=2",
            execution_steps=bullets("Create futures", "allOf", "join all", "read results"),
            output="- Output: 3",
            complexity="- N/A (concept)",
            enterprise="Used for batching independent downstream calls with a single synchronization point.",
            interview=bullets("Why allOf returns Void", "Exception behavior"),
            best_practices=bullets("Avoid blocking inside pipeline", "Handle timeouts", "Propagate exceptions carefully"),
        )

    if low == "anyof":
        return render(
            title,
            concept="`anyOf` completes when any future completes (first result wins).",
            problem="Return the first successful response (e.g., from two replicas).",
            intuition="Race two futures and take the fastest; cancel the slower if appropriate.",
            java_impl=textwrap.dedent(
                """\
                import java.util.concurrent.*;

                public class AnyOfDemo {
                    public static void main(String[] args) {
                        CompletableFuture<String> a = CompletableFuture.completedFuture("A");
                        CompletableFuture<String> b = CompletableFuture.completedFuture("B");
                        Object first = CompletableFuture.anyOf(a, b).join();
                        System.out.println(first);
                    }
                }
                """\
            ),
            stream_impl=GEN_STREAM,
            sample_input='- Input: a="A", b="B"',
            execution_steps=bullets("Create futures", "anyOf", "join"),
            output="- Output: A (or B depending on completion order)",
            complexity="- N/A (concept)",
            enterprise="Useful for hedged requests and replica reads; requires careful cancellation and cost control.",
            interview=bullets("Type of anyOf", "Cancellation", "first-completes semantics"),
            best_practices=bullets("Use timeouts", "Cancel losers when possible", "Avoid duplicate side effects"),
        )

    # ---------------- Section 15: Searching Algorithms ----------------
    if low == "linear search":
        return render(
            title,
            concept="Linear search scans sequentially until it finds the target or reaches the end.",
            problem="Return index of x in array (or -1).",
            intuition="No assumptions about ordering; check each element.",
            java_impl=textwrap.dedent(
                """\
                public class LinearSearch {
                    public static int search(int[] a, int x) {
                        for (int i = 0; i < a.length; i++) {
                            if (a[i] == x) return i;
                        }
                        return -1;
                    }

                    public static void main(String[] args) {
                        int[] a = {5, 2, 9};
                        System.out.println(search(a, 9));
                    }
                }
                """\
            ),
            stream_impl=textwrap.dedent(
                """\
                import java.util.*;
                import java.util.stream.*;

                public class LinearSearchStreamNote {
                    public static void main(String[] args) {
                        List<Integer> xs = Arrays.asList(5, 2, 9);
                        boolean found = xs.stream().anyMatch(v -> v == 9);
                        System.out.println(found);
                    }
                }
                """\
            ),
            sample_input="- Input: a=[5,2,9], x=9",
            execution_steps=bullets("i=0 compare", "i=1 compare", "i=2 match"),
            output=bullets("Output: 2", "Output(stream): true"),
            complexity="- Time: O(n)\n- Space: O(1)",
            enterprise="Used when data is small/unsorted or when you can’t afford preprocessing.",
            interview=bullets("Best/worst case", "When linear is better than binary"),
            best_practices=bullets("Short-circuit early", "Prefer binary search if sorted and queried often"),
        )

    if low == "search in rotated array":
        return render(
            title,
            concept="A rotated sorted array is sorted but shifted (e.g., [4,5,6,1,2,3]). You can search in O(log n).",
            problem="Given rotated sorted array with distinct values, return index of target or -1.",
            intuition="At each mid, one side is sorted. Decide which side to keep based on target range.",
            java_impl=textwrap.dedent(
                """\
                public class SearchRotated {
                    public static int search(int[] a, int x) {
                        int lo = 0, hi = a.length - 1;
                        while (lo <= hi) {
                            int mid = lo + (hi - lo) / 2;
                            if (a[mid] == x) return mid;

                            // left half sorted
                            if (a[lo] <= a[mid]) {
                                if (a[lo] <= x && x < a[mid]) hi = mid - 1;
                                else lo = mid + 1;
                            } else { // right half sorted
                                if (a[mid] < x && x <= a[hi]) lo = mid + 1;
                                else hi = mid - 1;
                            }
                        }
                        return -1;
                    }

                    public static void main(String[] args) {
                        int[] a = {4,5,6,1,2,3};
                        System.out.println(search(a, 2));
                    }
                }
                """\
            ),
            stream_impl=textwrap.dedent(
                """\
                public class SearchRotatedStreamNote {
                    // Index-based O(log n) algorithm; streams reduce clarity.
                }
                """\
            ),
            sample_input="- Input: a=[4,5,6,1,2,3], x=2",
            execution_steps=bullets("mid=2 (6) decide right side", "mid=4 (2) match"),
            output="- Output: 4",
            complexity="- Time: O(log n)\n- Space: O(1)",
            enterprise="Used in circular buffers, time-window indices, and some partitioned keyspaces.",
            interview=bullets("Handling duplicates", "Invariant reasoning", "Edge cases (not rotated)"),
            best_practices=bullets("Use overflow-safe mid", "Add tests for boundaries"),
        )

    # ---------------- Section 16: Sorting Algorithms ----------------
    if low == "bubble sort":
        return render(
            title,
            concept="Bubble sort repeatedly swaps adjacent out-of-order elements, bubbling the largest to the end each pass.",
            problem="Sort an integer array ascending.",
            intuition="After i passes, the last i elements are in final position.",
            java_impl=textwrap.dedent(
                """\
                import java.util.*;

                public class BubbleSort {
                    public static void sort(int[] a) {
                        for (int i = 0; i < a.length; i++) {
                            boolean swapped = false;
                            for (int j = 0; j < a.length - 1 - i; j++) {
                                if (a[j] > a[j + 1]) {
                                    int t = a[j]; a[j] = a[j + 1]; a[j + 1] = t;
                                    swapped = true;
                                }
                            }
                            if (!swapped) return;
                        }
                    }

                    public static void main(String[] args) {
                        int[] a = {5, 1, 4, 2, 8};
                        sort(a);
                        System.out.println(Arrays.toString(a));
                    }
                }
                """\
            ),
            stream_impl=textwrap.dedent(
                """\
                import java.util.*;
                import java.util.stream.*;

                public class SortStreamNote {
                    public static void main(String[] args) {
                        int[] a = {5, 1, 4, 2, 8};
                        int[] out = IntStream.of(a).sorted().toArray();
                        System.out.println(Arrays.toString(out));
                    }
                }
                """\
            ),
            sample_input="- Input: [5,1,4,2,8]",
            execution_steps=bullets("Pass through array swapping adjacent inversions", "Early exit if no swaps"),
            output="- Output: [1, 2, 4, 5, 8]",
            complexity="- Time: O(n^2) worst/avg, O(n) best with early-exit\n- Space: O(1)",
            enterprise="Mostly for teaching; rarely used in production due to O(n^2).",
            interview=bullets("Stability", "Best-case optimization", "When it’s acceptable"),
            best_practices=bullets("Use built-in sort in real systems", "Use bubble sort only for tiny n / education"),
        )

    if low == "selection sort":
        return render(
            title,
            concept="Selection sort selects the minimum element from the unsorted region and swaps it into place.",
            problem="Sort an integer array ascending.",
            intuition="After i iterations, prefix [0..i] is sorted and fixed.",
            java_impl=textwrap.dedent(
                """\
                import java.util.*;

                public class SelectionSort {
                    public static void sort(int[] a) {
                        for (int i = 0; i < a.length; i++) {
                            int min = i;
                            for (int j = i + 1; j < a.length; j++) {
                                if (a[j] < a[min]) min = j;
                            }
                            int t = a[i]; a[i] = a[min]; a[min] = t;
                        }
                    }

                    public static void main(String[] args) {
                        int[] a = {5, 1, 4, 2, 8};
                        sort(a);
                        System.out.println(Arrays.toString(a));
                    }
                }
                """\
            ),
            stream_impl=GEN_STREAM,
            sample_input="- Input: [5,1,4,2,8]",
            execution_steps=bullets("For each i, find min in suffix", "Swap into position i"),
            output="- Output: [1, 2, 4, 5, 8]",
            complexity="- Time: O(n^2)\n- Space: O(1)",
            enterprise="Used when swaps are expensive and comparisons are cheap (still uncommon vs built-ins).",
            interview=bullets("Why not stable", "Swap count vs bubble/insertion"),
            best_practices=bullets("Prefer built-in TimSort/dual-pivot quicksort", "Mention when selection sort is reasonable"),
        )

    if low == "insertion sort":
        return render(
            title,
            concept="Insertion sort builds a sorted prefix by inserting each new element into its correct position.",
            problem="Sort an integer array ascending.",
            intuition="Good for nearly-sorted arrays; shifts elements to make room.",
            java_impl=textwrap.dedent(
                """\
                import java.util.*;

                public class InsertionSort {
                    public static void sort(int[] a) {
                        for (int i = 1; i < a.length; i++) {
                            int key = a[i];
                            int j = i - 1;
                            while (j >= 0 && a[j] > key) {
                                a[j + 1] = a[j];
                                j--;
                            }
                            a[j + 1] = key;
                        }
                    }

                    public static void main(String[] args) {
                        int[] a = {5, 1, 4, 2, 8};
                        sort(a);
                        System.out.println(Arrays.toString(a));
                    }
                }
                """\
            ),
            stream_impl=GEN_STREAM,
            sample_input="- Input: [5,1,4,2,8]",
            execution_steps=bullets("Take next key", "Shift larger elements right", "Insert key"),
            output="- Output: [1, 2, 4, 5, 8]",
            complexity="- Time: O(n^2) worst/avg, O(n) best (nearly sorted)\n- Space: O(1)",
            enterprise="Used as a subroutine for small partitions (hybrid sorts) and for nearly-sorted data.",
            interview=bullets("Stability", "Why good for nearly-sorted", "Comparison count"),
            best_practices=bullets("Use for small n", "Prefer built-in sort for general use"),
        )

    if low == "merge sort":
        return render(
            title,
            concept="Merge sort is a divide-and-conquer stable sort: split array, sort halves, merge sorted halves.",
            problem="Sort an integer array ascending.",
            intuition="Merging two sorted arrays is linear; recursion gives O(n log n).",
            java_impl=textwrap.dedent(
                """\
                import java.util.*;

                public class MergeSort {
                    static void sort(int[] a) {
                        int[] tmp = new int[a.length];
                        sort(a, tmp, 0, a.length - 1);
                    }

                    static void sort(int[] a, int[] tmp, int lo, int hi) {
                        if (lo >= hi) return;
                        int mid = lo + (hi - lo) / 2;
                        sort(a, tmp, lo, mid);
                        sort(a, tmp, mid + 1, hi);
                        merge(a, tmp, lo, mid, hi);
                    }

                    static void merge(int[] a, int[] tmp, int lo, int mid, int hi) {
                        int i = lo, j = mid + 1, k = lo;
                        while (i <= mid && j <= hi) {
                            if (a[i] <= a[j]) tmp[k++] = a[i++];
                            else tmp[k++] = a[j++];
                        }
                        while (i <= mid) tmp[k++] = a[i++];
                        while (j <= hi) tmp[k++] = a[j++];
                        for (int p = lo; p <= hi; p++) a[p] = tmp[p];
                    }

                    public static void main(String[] args) {
                        int[] a = {5, 1, 4, 2, 8};
                        sort(a);
                        System.out.println(Arrays.toString(a));
                    }
                }
                """\
            ),
            stream_impl=GEN_STREAM,
            sample_input="- Input: [5,1,4,2,8]",
            execution_steps=bullets("Split into halves", "Sort halves", "Merge"),
            output="- Output: [1, 2, 4, 5, 8]",
            complexity="- Time: O(n log n)\n- Space: O(n)",
            enterprise="Stable sorting is important for multi-key sorting and deterministic reports.",
            interview=bullets("Stability", "Why O(n) extra space", "Merge step"),
            best_practices=bullets("Use stable sort when needed", "Avoid recursion depth issues for huge arrays"),
        )

    if low == "quick sort":
        return render(
            title,
            concept="Quick sort partitions around a pivot and recursively sorts partitions. Average O(n log n), worst O(n^2).",
            problem="Sort an integer array ascending.",
            intuition="Partition so left<pivot and right>pivot; recursion sorts subarrays.",
            java_impl=textwrap.dedent(
                """\
                import java.util.*;

                public class QuickSort {
                    static void sort(int[] a) { sort(a, 0, a.length - 1); }

                    static void sort(int[] a, int lo, int hi) {
                        if (lo >= hi) return;
                        int p = partition(a, lo, hi);
                        sort(a, lo, p - 1);
                        sort(a, p + 1, hi);
                    }

                    static int partition(int[] a, int lo, int hi) {
                        int pivot = a[hi];
                        int i = lo;
                        for (int j = lo; j < hi; j++) {
                            if (a[j] <= pivot) {
                                int t = a[i]; a[i] = a[j]; a[j] = t;
                                i++;
                            }
                        }
                        int t = a[i]; a[i] = a[hi]; a[hi] = t;
                        return i;
                    }

                    public static void main(String[] args) {
                        int[] a = {5, 1, 4, 2, 8};
                        sort(a);
                        System.out.println(Arrays.toString(a));
                    }
                }
                """\
            ),
            stream_impl=GEN_STREAM,
            sample_input="- Input: [5,1,4,2,8]",
            execution_steps=bullets("Choose pivot", "Partition", "Recurse left/right"),
            output="- Output: [1, 2, 4, 5, 8]",
            complexity="- Time: O(n log n) avg, O(n^2) worst\n- Space: O(log n) avg recursion",
            enterprise="Built-in sorts are heavily optimized (dual-pivot quicksort for primitives). In interviews, discuss pivot choice and worst-case.",
            interview=bullets("Partition schemes", "Pivot selection", "Why worst-case happens"),
            best_practices=bullets("Prefer built-in sort", "Randomize/median-of-three pivot to reduce worst-case"),
        )

    # ---------------- Algorithms / interview ----------------
    if low == "two sum":
        return render(
            title,
            concept="Two Sum is a canonical hash-map lookup problem.",
            problem="Find indices i, j where a[i] + a[j] = target.",
            intuition="Scan once, store seen values->index, look for complement.",
            java_impl=textwrap.dedent(
                """\
                import java.util.*;

                public class TwoSum {
                    public static int[] twoSum(int[] a, int target) {
                        Map<Integer, Integer> seen = new HashMap<>();
                        for (int i = 0; i < a.length; i++) {
                            int need = target - a[i];
                            Integer j = seen.get(need);
                            if (j != null) return new int[]{j, i};
                            seen.put(a[i], i);
                        }
                        return new int[]{-1, -1};
                    }
                }
                """
            ),
            stream_impl=textwrap.dedent(
                """\
                public class TwoSumStreamNote {
                    // Streams are not ideal for index-based lookups; prefer the loop.
                }
                """
            ),
            sample_input="- Input: a=[2,7,11,15], target=9",
            execution_steps=bullets("need=target-x", "if seen contains need -> answer"),
            output="- Output: [0,1]",
            complexity="- Time: O(n)\n- Space: O(n)",
            enterprise="Used in rule engines and complement lookups in ETL pipelines.",
            interview=bullets("Duplicates", "No-solution behavior", "Two-pointer alternative"),
            best_practices=bullets("Define failure behavior", "Consider overflow"),
        )

    # ---------------- Section 17: Array Interview Problems ----------------
    if low == "three sum":
        return render(
            title,
            concept="Three Sum finds all unique triplets (i,j,k) such that a[i]+a[j]+a[k]=0.",
            problem="Given an int array, return all unique triplets that sum to 0.",
            intuition="Sort the array, then fix i and use two pointers (l/r) to find complements while skipping duplicates.",
            java_impl=textwrap.dedent(
                """\
                import java.util.*;

                public class ThreeSum {
                    public static List<List<Integer>> threeSum(int[] a) {
                        Arrays.sort(a);
                        List<List<Integer>> res = new ArrayList<>();
                        for (int i = 0; i < a.length; i++) {
                            if (i > 0 && a[i] == a[i-1]) continue;
                            int l = i + 1, r = a.length - 1;
                            while (l < r) {
                                int s = a[i] + a[l] + a[r];
                                if (s == 0) {
                                    res.add(Arrays.asList(a[i], a[l], a[r]));
                                    l++; r--;
                                    while (l < r && a[l] == a[l-1]) l++;
                                    while (l < r && a[r] == a[r+1]) r--;
                                } else if (s < 0) {
                                    l++;
                                } else {
                                    r--;
                                }
                            }
                        }
                        return res;
                    }

                    public static void main(String[] args) {
                        int[] a = {-1, 0, 1, 2, -1, -4};
                        System.out.println(threeSum(a));
                    }
                }
                """\
            ),
            stream_impl=textwrap.dedent(
                """\
                public class ThreeSumStreamNote {
                    // Streams are not ideal for the two-pointer + duplicate-skip pattern.
                    // Prefer the loop-based approach for clarity and performance.
                }
                """\
            ),
            sample_input="- Input: [-1,0,1,2,-1,-4]",
            execution_steps=bullets("Sort", "Fix i", "Two-pointer scan", "Skip duplicates"),
            output="- Output: [[-1, -1, 2], [-1, 0, 1]]",
            complexity="- Time: O(n^2)\n- Space: O(1) extra (excluding output)",
            enterprise="Useful pattern for k-sum style matching and risk rules (combinations) after sorting.",
            interview=bullets("Duplicate handling", "Why sorting helps", "Generalizing to k-sum"),
            best_practices=bullets("Skip duplicates carefully", "Use long if sums can overflow"),
        )

    if low == "find duplicate numbers":
        return render(
            title,
            concept="Detect duplicates in an array. Approach depends on constraints (range, memory, modify array allowed).",
            problem="Given array a, return any duplicate value if present.",
            intuition="Use a HashSet to track seen values in O(n) time.",
            java_impl=textwrap.dedent(
                """\
                import java.util.*;

                public class FindDuplicate {
                    public static Integer find(int[] a) {
                        Set<Integer> seen = new HashSet<>();
                        for (int x : a) {
                            if (!seen.add(x)) return x;
                        }
                        return null;
                    }

                    public static void main(String[] args) {
                        int[] a = {1,3,4,2,2};
                        System.out.println(find(a));
                    }
                }
                """\
            ),
            stream_impl=textwrap.dedent(
                """\
                import java.util.*;
                import java.util.stream.*;

                public class FindDuplicateStream {
                    public static void main(String[] args) {
                        List<Integer> xs = Arrays.asList(1,3,4,2,2);
                        Set<Integer> seen = new HashSet<>();
                        Optional<Integer> dup = xs.stream().filter(x -> !seen.add(x)).findFirst();
                        System.out.println(dup.orElse(null));
                    }
                }
                """\
            ),
            sample_input="- Input: [1,3,4,2,2]",
            execution_steps=bullets("Track seen in set", "First value that cannot be added is duplicate"),
            output=bullets("Output: 2", "Output(stream): 2"),
            complexity="- Time: O(n)\n- Space: O(n)",
            enterprise="Used in idempotency checks, deduping event ids, and detecting bad data in ingestion.",
            interview=bullets("Memory trade-off", "Can you do O(1) space? (Floyd's cycle with constraints)"),
            best_practices=bullets("Clarify constraints", "Prefer set unless memory is constrained"),
        )

    if low == "missing number":
        return render(
            title,
            concept="Missing number in [0..n] can be found via XOR or sum formula.",
            problem="Given array containing n distinct numbers from 0..n, find the missing one.",
            intuition="XOR cancels pairs: a^a=0; XOR all indices and values to get missing.",
            java_impl=textwrap.dedent(
                """\
                public class MissingNumber {
                    public static int missing(int[] a) {
                        int n = a.length;
                        int x = 0;
                        for (int i = 0; i <= n; i++) x ^= i;
                        for (int v : a) x ^= v;
                        return x;
                    }

                    public static void main(String[] args) {
                        int[] a = {3,0,1};
                        System.out.println(missing(a));
                    }
                }
                """\
            ),
            stream_impl=textwrap.dedent(
                """\
                import java.util.stream.*;

                public class MissingNumberStreamNote {
                    public static void main(String[] args) {
                        int[] a = {3,0,1};
                        int n = a.length;
                        int xor = IntStream.rangeClosed(0, n).reduce(0, (acc, i) -> acc ^ i);
                        for (int v : a) xor ^= v;
                        System.out.println(xor);
                    }
                }
                """\
            ),
            sample_input="- Input: [3,0,1]",
            execution_steps=bullets("XOR 0..n", "XOR all values", "Remaining is missing"),
            output="- Output: 2",
            complexity="- Time: O(n)\n- Space: O(1)",
            enterprise="Useful for detecting gaps in sequences (with correct constraints) and sanity checks in ETL.",
            interview=bullets("XOR properties", "Sum overflow vs XOR", "Constraints"),
            best_practices=bullets("Prefer XOR to avoid overflow", "Validate constraints before applying"),
        )

    # ---------------- Section 18: String Interview Problems ----------------
    if low == "reverse string":
        return render(
            title,
            concept="Reverse a string by swapping characters from both ends toward the center.",
            problem="Given s, return reversed string.",
            intuition="Two pointers i/j swap until i>=j.",
            java_impl=textwrap.dedent(
                """\
                public class ReverseString {
                    public static String rev(String s) {
                        char[] a = s.toCharArray();
                        int i = 0, j = a.length - 1;
                        while (i < j) {
                            char t = a[i]; a[i] = a[j]; a[j] = t;
                            i++; j--;
                        }
                        return new String(a);
                    }

                    public static void main(String[] args) {
                        System.out.println(rev("abcd"));
                    }
                }
                """\
            ),
            stream_impl=textwrap.dedent(
                """\
                import java.util.stream.*;

                public class ReverseStreamNote {
                    public static void main(String[] args) {
                        String s = "abcd";
                        String out = IntStream.range(0, s.length())
                                .mapToObj(i -> s.charAt(s.length() - 1 - i))
                                .collect(StringBuilder::new, StringBuilder::append, StringBuilder::append)
                                .toString();
                        System.out.println(out);
                    }
                }
                """\
            ),
            sample_input='- Input: "abcd"',
            execution_steps=bullets("Convert to char[]", "Swap i/j", "Build new String"),
            output="- Output: dcba",
            complexity="- Time: O(n)\n- Space: O(n) for char array",
            enterprise="Common utility in parsing and transformations; pay attention to Unicode grapheme clusters in real products.",
            interview=bullets("Two-pointer technique", "String immutability"),
            best_practices=bullets("Use StringBuilder for many concatenations", "Clarify Unicode requirements"),
        )

    if low == "palindrome detection":
        return render(
            title,
            concept="A palindrome reads the same forward and backward.",
            problem="Given s, return true if it is a palindrome (exact match).",
            intuition="Two pointers compare from ends; early-exit on mismatch.",
            java_impl=textwrap.dedent(
                """\
                public class Palindrome {
                    public static boolean isPal(String s) {
                        int i = 0, j = s.length() - 1;
                        while (i < j) {
                            if (s.charAt(i) != s.charAt(j)) return false;
                            i++; j--;
                        }
                        return true;
                    }
                    public static void main(String[] args) {
                        System.out.println(isPal("abba"));
                        System.out.println(isPal("abca"));
                    }
                }
                """\
            ),
            stream_impl=GEN_STREAM,
            sample_input=bullets('Input: "abba"', 'Input: "abca"'),
            execution_steps=bullets("Compare ends", "Move inward", "Early exit on mismatch"),
            output=bullets("Output: true", "Output: false"),
            complexity="- Time: O(n)\n- Space: O(1)",
            enterprise="Often used in validation rules; variants include ignoring non-alphanumerics and case.",
            interview=bullets("Two pointers", "Variants (ignore punctuation/case)"),
            best_practices=bullets("Clarify normalization rules", "Avoid building reversed copies if not needed"),
        )

    if low == "longest substring without repeating characters":
        return render(
            title,
            concept="Find the longest substring with all unique characters.",
            problem="Given s, return length of longest substring with no repeated characters.",
            intuition="Sliding window with a set/map: expand right; shrink left until unique.",
            java_impl=textwrap.dedent(
                """\
                import java.util.*;

                public class LongestUniqueSubstring {
                    public static int length(String s) {
                        Set<Character> win = new HashSet<>();
                        int best = 0;
                        int l = 0;
                        for (int r = 0; r < s.length(); r++) {
                            char c = s.charAt(r);
                            while (win.contains(c)) {
                                win.remove(s.charAt(l));
                                l++;
                            }
                            win.add(c);
                            best = Math.max(best, r - l + 1);
                        }
                        return best;
                    }

                    public static void main(String[] args) {
                        System.out.println(length("abcabcbb"));
                    }
                }
                """\
            ),
            stream_impl=textwrap.dedent(
                """\
                public class LongestUniqueStreamNote {
                    // Sliding window is stateful; streams are not a good fit.
                }
                """\
            ),
            sample_input='- Input: "abcabcbb"',
            execution_steps=bullets("Expand right pointer", "If repeat, shrink left", "Track best window"),
            output="- Output: 3",
            complexity="- Time: O(n)\n- Space: O(min(n, alphabet))",
            enterprise="Used in rate-limiting token parsing, uniqueness constraints, and window-based analytics.",
            interview=bullets("Why O(n)", "Set vs last-seen index map optimization"),
            best_practices=bullets("Use last-seen index map for faster shrink", "Clarify character set (ASCII/Unicode)"),
        )

    if low == "anagram detection":
        return render(
            title,
            concept="Two strings are anagrams if they contain the same characters with the same counts.",
            problem="Given s and t, return true if they are anagrams.",
            intuition="Count frequencies and compare. For lowercase a-z, use int[26].",
            java_impl=textwrap.dedent(
                """\
                public class Anagram {
                    public static boolean isAnagram(String s, String t) {
                        if (s.length() != t.length()) return false;
                        int[] cnt = new int[26];
                        for (int i = 0; i < s.length(); i++) {
                            cnt[s.charAt(i) - 'a']++;
                            cnt[t.charAt(i) - 'a']--;
                        }
                        for (int c : cnt) if (c != 0) return false;
                        return true;
                    }
                    public static void main(String[] args) {
                        System.out.println(isAnagram("listen", "silent"));
                    }
                }
                """\
            ),
            stream_impl=textwrap.dedent(
                """\
                import java.util.*;
                import java.util.stream.*;

                public class AnagramStreamNote {
                    public static void main(String[] args) {
                        String s = "listen", t = "silent";
                        String a = s.chars().sorted().mapToObj(c -> String.valueOf((char)c)).collect(Collectors.joining());
                        String b = t.chars().sorted().mapToObj(c -> String.valueOf((char)c)).collect(Collectors.joining());
                        System.out.println(a.equals(b));
                    }
                }
                """\
            ),
            sample_input=bullets('Input: s="listen"', 'Input: t="silent"'),
            execution_steps=bullets("Count chars", "Compare counts"),
            output="- Output: true",
            complexity="- Time: O(n) (counting)\n- Space: O(1) for fixed alphabet",
            enterprise="Used in dedupe/normalization pipelines; clarify normalization (case, spaces, Unicode).",
            interview=bullets("Counting vs sorting approach", "Unicode considerations"),
            best_practices=bullets("Prefer counting for fixed alphabet", "Normalize inputs at boundaries"),
        )

    if low == "first non-repeating character":
        return render(
            title,
            concept="Find the first character that occurs exactly once.",
            problem="Given s, return index of first non-repeating character, or -1.",
            intuition="Count frequencies, then scan again to find first char with count==1.",
            java_impl=textwrap.dedent(
                """\
                import java.util.*;

                public class FirstUniqueChar {
                    public static int firstUnique(String s) {
                        int[] cnt = new int[256];
                        for (int i = 0; i < s.length(); i++) cnt[s.charAt(i)]++;
                        for (int i = 0; i < s.length(); i++) {
                            if (cnt[s.charAt(i)] == 1) return i;
                        }
                        return -1;
                    }

                    public static void main(String[] args) {
                        System.out.println(firstUnique("leetcode"));
                    }
                }
                """\
            ),
            stream_impl=GEN_STREAM,
            sample_input='- Input: "leetcode"',
            execution_steps=bullets("Count frequencies", "Second pass find first count==1"),
            output="- Output: 0",
            complexity="- Time: O(n)\n- Space: O(1) for fixed alphabet",
            enterprise="Useful in log analysis and token parsing; confirm character set requirements.",
            interview=bullets("Two-pass approach", "LinkedHashMap alternative"),
            best_practices=bullets("Clarify charset", "Use LinkedHashMap for Unicode-safe frequency tracking"),
        )

    # ---------------- Section 19: Stream Interview Problems ----------------
    if low == "second highest salary":
        return render(
            title,
            concept="Find the second highest distinct value from a set of salaries.",
            problem="Given employee salaries, return the second highest distinct salary.",
            intuition="Sort distinct salaries descending and skip the first.",
            java_impl=textwrap.dedent(
                """\
                import java.util.*;

                public class SecondHighestSalaryLoop {
                    public static Integer secondHighest(List<Integer> xs) {
                        Set<Integer> set = new HashSet<>(xs);
                        List<Integer> vals = new ArrayList<>(set);
                        Collections.sort(vals);
                        if (vals.size() < 2) return null;
                        return vals.get(vals.size() - 2);
                    }

                    public static void main(String[] args) {
                        System.out.println(secondHighest(Arrays.asList(100, 200, 300, 300)));
                    }
                }
                """\
            ),
            stream_impl=textwrap.dedent(
                """\
                import java.util.*;
                import java.util.stream.*;

                public class SecondHighestSalaryStream {
                    public static void main(String[] args) {
                        List<Integer> salaries = Arrays.asList(100, 200, 300, 300);
                        Integer second = salaries.stream()
                                .distinct()
                                .sorted(Comparator.reverseOrder())
                                .skip(1)
                                .findFirst()
                                .orElse(null);
                        System.out.println(second);
                    }
                }
                """\
            ),
            sample_input="- Input: [100,200,300,300]",
            execution_steps=bullets("distinct", "sort desc", "skip 1", "findFirst"),
            output="- Output: 200",
            complexity="- Time: O(n log n)\n- Space: O(n)",
            enterprise="Used in compensation reports and analytics; clarify ties and distinctness rules.",
            interview=bullets("Second highest vs second distinct", "Handling <2 values"),
            best_practices=bullets("Define behavior for duplicates", "Avoid sorting if you can do single-pass with two max variables"),
        )

    if low == "group employees by department":
        return render(
            title,
            concept="Use groupingBy to partition items by a key and collect grouped values.",
            problem="Group employees by department and list names.",
            intuition="groupingBy(dept, mapping(name, toList())) gives one-pass grouping.",
            java_impl=textwrap.dedent(
                """\
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
                """\
            ),
            stream_impl=textwrap.dedent(
                """\
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
                """\
            ),
            sample_input='- Input: [(ENG,amy),(ENG,bob),(HR,carl)]',
            execution_steps=bullets("groupingBy dept", "downstream mapping(name)", "collect"),
            output="- Output: {ENG=[amy, bob], HR=[carl]}",
            complexity="- Time: O(n)\n- Space: O(n)",
            enterprise="Used in org charts, reporting, and building response DTOs.",
            interview=bullets("groupingBy vs partitioningBy", "downstream collectors"),
            best_practices=bullets("Use LinkedHashMap supplier for deterministic ordering when needed", "Avoid grouping huge datasets in memory"),
        )

    if low == "find duplicate elements using streams":
        return render(
            title,
            concept="Detect duplicates by tracking seen values and selecting values that appear more than once.",
            problem="Given a list, return the set of duplicate elements.",
            intuition="Maintain a 'seen' set; values that fail to add are duplicates.",
            java_impl=textwrap.dedent(
                """\
                import java.util.*;

                public class FindDuplicatesLoop {
                    public static void main(String[] args) {
                        List<Integer> xs = Arrays.asList(1,2,2,3,3,3);
                        Set<Integer> seen = new HashSet<>();
                        Set<Integer> dup = new HashSet<>();
                        for (int x : xs) {
                            if (!seen.add(x)) dup.add(x);
                        }
                        System.out.println(dup);
                    }
                }
                """\
            ),
            stream_impl=textwrap.dedent(
                """\
                import java.util.*;
                import java.util.stream.*;

                public class FindDuplicatesStream {
                    public static void main(String[] args) {
                        List<Integer> xs = Arrays.asList(1,2,2,3,3,3);
                        Set<Integer> seen = new HashSet<>();
                        Set<Integer> dup = xs.stream().filter(x -> !seen.add(x)).collect(Collectors.toSet());
                        System.out.println(dup);
                    }
                }
                """\
            ),
            sample_input="- Input: [1,2,2,3,3,3]",
            execution_steps=bullets("Track seen", "Filter those that repeat", "Collect to set"),
            output="- Output: [2, 3] (order may vary)",
            complexity="- Time: O(n)\n- Space: O(n)",
            enterprise="Useful for dedupe in ingestion; note this stream approach uses side effects and is not parallel-safe.",
            interview=bullets("Side effects in streams", "Parallel stream safety"),
            best_practices=bullets("Prefer groupingBy/counting for pure approach", "Keep it sequential"),
        )

    if low == "convert list to map":
        return render(
            title,
            concept="Convert a list of objects into a Map keyed by some unique attribute.",
            problem="Convert employees list to map by id, handling duplicate ids.",
            intuition="Use Collectors.toMap with a merge function for duplicates.",
            java_impl=textwrap.dedent(
                """\
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
                """\
            ),
            stream_impl=textwrap.dedent(
                """\
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
                """\
            ),
            sample_input='- Input: [(e1,amy),(e1,amy2),(e2,bob)]',
            execution_steps=bullets("Key=id", "Value=name", "Merge duplicates", "Collect"),
            output="- Output: {e1=amy, e2=bob}",
            complexity="- Time: O(n)\n- Space: O(n)",
            enterprise="Common for building lookup maps and caches; always define collision policy.",
            interview=bullets("Why toMap needs merge", "Map supplier"),
            best_practices=bullets("Use LinkedHashMap for deterministic iteration", "Avoid heavy merge functions"),
        )

    if low == "frequency map using streams":
        return render(
            title,
            concept="Build a frequency map (value -> count) using Streams.",
            problem="Given a list of tokens, build a frequency map.",
            intuition="groupingBy(identity, counting) is a pure collector approach.",
            java_impl=textwrap.dedent(
                """\
                import java.util.*;

                public class FrequencyMapLoop {
                    public static void main(String[] args) {
                        List<String> xs = Arrays.asList("a", "b", "a");
                        Map<String, Long> freq = new LinkedHashMap<>();
                        for (String s : xs) {
                            freq.put(s, freq.getOrDefault(s, 0L) + 1L);
                        }
                        System.out.println(freq);
                    }
                }
                """\
            ),
            stream_impl=textwrap.dedent(
                """\
                import java.util.*;
                import java.util.stream.*;

                public class FrequencyMap {
                    public static void main(String[] args) {
                        List<String> xs = Arrays.asList("a", "b", "a");
                        Map<String, Long> freq = xs.stream().collect(Collectors.groupingBy(s -> s, LinkedHashMap::new, Collectors.counting()));
                        System.out.println(freq);
                    }
                }
                """\
            ),
            sample_input='- Input: ["a","b","a"]',
            execution_steps=bullets("groupingBy token", "downstream counting", "Print map"),
            output="- Output: {a=2, b=1}",
            complexity="- Time: O(n)\n- Space: O(n)",
            enterprise="Foundational for analytics, logs aggregation, and batch metrics.",
            interview=bullets("groupingBy vs toMap+merge", "LinkedHashMap supplier"),
            best_practices=bullets("Control key cardinality", "Prefer LinkedHashMap when ordering matters"),
        )

    # ---------------- Section 20: Enterprise Java Use Cases ----------------
    if low == "parallel api calls":
        return render(
            title,
            concept="Run independent remote calls concurrently and combine results (fan-out/fan-in).",
            problem="Call two independent services in parallel and build a combined response.",
            intuition="Use CompletableFuture.supplyAsync on a bounded executor, thenCombine/allOf to merge.",
            java_impl=textwrap.dedent(
                """\
                import java.util.concurrent.*;

                public class ParallelApiCalls {
                    static String serviceA() { return "A"; }
                    static String serviceB() { return "B"; }

                    public static void main(String[] args) {
                        ExecutorService es = Executors.newFixedThreadPool(2);
                        try {
                            CompletableFuture<String> a = CompletableFuture.supplyAsync(ParallelApiCalls::serviceA, es);
                            CompletableFuture<String> b = CompletableFuture.supplyAsync(ParallelApiCalls::serviceB, es);
                            String out = a.thenCombine(b, (x, y) -> x + y).join();
                            System.out.println(out);
                        } finally {
                            es.shutdown();
                        }
                    }
                }
                """\
            ),
            stream_impl=GEN_STREAM,
            sample_input="- Input: serviceA returns A; serviceB returns B",
            execution_steps=bullets("Create bounded executor", "Run supplyAsync for each call", "thenCombine", "join"),
            output="- Output: AB",
            complexity="- Latency: ~max(latA, latB) (idealized)\n- Work: sum of calls",
            enterprise="Core pattern for API aggregators/BFFs. Must add timeouts, retries, bulkheads, and circuit breakers.",
            interview=bullets("Fan-out/fan-in", "Timeouts", "Thread pool isolation"),
            best_practices=bullets("Use explicit executors", "Add timeouts", "Limit concurrency", "Avoid blocking inside stages"),
        )

    if low == "async database queries":
        return render(
            title,
            concept="Run DB queries asynchronously using dedicated executors (since JDBC is blocking).",
            problem="Fetch user and orders concurrently via async wrappers and combine.",
            intuition="Wrap blocking IO in supplyAsync on a dedicated IO pool to avoid blocking request threads.",
            java_impl=textwrap.dedent(
                """\
                import java.util.concurrent.*;

                public class AsyncDbQueries {
                    static String fetchUser() { return "user:u1"; }
                    static String fetchOrders() { return "orders:2"; }

                    public static void main(String[] args) {
                        ExecutorService io = Executors.newFixedThreadPool(4);
                        try {
                            CompletableFuture<String> u = CompletableFuture.supplyAsync(AsyncDbQueries::fetchUser, io);
                            CompletableFuture<String> o = CompletableFuture.supplyAsync(AsyncDbQueries::fetchOrders, io);
                            String out = u.thenCombine(o, (a,b) -> a + "," + b).join();
                            System.out.println(out);
                        } finally {
                            io.shutdown();
                        }
                    }
                }
                """\
            ),
            stream_impl=GEN_STREAM,
            sample_input="- Input: fetchUser->user:u1, fetchOrders->orders:2",
            execution_steps=bullets("Use IO pool", "Wrap blocking calls in supplyAsync", "thenCombine", "join"),
            output="- Output: user:u1,orders:2",
            complexity="- Latency: ~max(query1, query2) (idealized)",
            enterprise="In real systems consider async DB drivers/reactive stacks, connection pool limits, and backpressure.",
            interview=bullets("Why JDBC isn't async", "Thread pool sizing", "Connection pool interaction"),
            best_practices=bullets("Isolate IO pool", "Never block CPU pool", "Propagate MDC/trace context"),
        )

    if low == "batch processing":
        return render(
            title,
            concept="Batch jobs process many records with chunking, retries, and idempotency.",
            problem="Process records in chunks and compute an aggregate deterministically.",
            intuition="Chunk to control memory, and make each chunk idempotent for retries.",
            java_impl=textwrap.dedent(
                """\
                import java.util.*;

                public class BatchProcessing {
                    static long chunkSum(List<Integer> chunk) {
                        long s = 0;
                        for (int x : chunk) s += x;
                        return s;
                    }

                    public static void main(String[] args) {
                        List<Integer> xs = Arrays.asList(1,2,3,4,5,6);
                        int chunkSize = 2;
                        long total = 0;
                        for (int i = 0; i < xs.size(); i += chunkSize) {
                            List<Integer> chunk = xs.subList(i, Math.min(i + chunkSize, xs.size()));
                            total += chunkSum(chunk);
                        }
                        System.out.println(total);
                    }
                }
                """\
            ),
            stream_impl=textwrap.dedent(
                """\
                import java.util.*;
                import java.util.stream.*;

                public class BatchStreamNote {
                    public static void main(String[] args) {
                        List<Integer> xs = Arrays.asList(1,2,3,4,5,6);
                        long total = xs.stream().mapToLong(x -> x).sum();
                        System.out.println(total);
                    }
                }
                """\
            ),
            sample_input="- Input: xs=[1,2,3,4,5,6], chunkSize=2",
            execution_steps=bullets("Split into chunks", "Process chunk", "Accumulate", "Print"),
            output="- Output: 21",
            complexity="- Time: O(n)\n- Space: O(1) extra",
            enterprise="Batch patterns appear in ETL, reporting, billing, and reprocessing. Correctness needs idempotency and checkpointing.",
            interview=bullets("Idempotency", "Checkpointing", "Exactly-once vs at-least-once"),
            best_practices=bullets("Chunk to control memory", "Make handlers idempotent", "Add retries with DLQ strategy"),
        )

    if low == "event driven processing":
        return render(
            title,
            concept="Event-driven systems process messages asynchronously (queues/streams) with handlers and retries.",
            problem="Simulate a simple event queue and process events deterministically.",
            intuition="Decouple producers and consumers; ensure idempotent handling and ordering guarantees where required.",
            java_impl=textwrap.dedent(
                """\
                import java.util.*;

                public class EventDriven {
                    public static void main(String[] args) {
                        Queue<String> q = new ArrayDeque<>();
                        q.add("E1");
                        q.add("E2");
                        while (!q.isEmpty()) {
                            String e = q.remove();
                            System.out.println("handled:" + e);
                        }
                    }
                }
                """\
            ),
            stream_impl=GEN_STREAM,
            sample_input='- Input: queue=["E1","E2"]',
            execution_steps=bullets("Enqueue events", "Dequeue", "Handle"),
            output=bullets("Output: handled:E1", "Output: handled:E2"),
            complexity="- Time: O(n)\n- Space: O(n)",
            enterprise="Real implementations use Kafka/Rabbit/SQS. Key concerns: ordering, retries, DLQ, and idempotency.",
            interview=bullets("At-least-once delivery", "Idempotent consumers", "Ordering per key"),
            best_practices=bullets("Use idempotency keys", "Add DLQ", "Instrument lag and failure rate"),
        )

    if low == "binary search":
        return render(
            title,
            concept="Binary search finds an element in a sorted array by halving the search range.",
            problem="Return index of x in sorted array or -1.",
            intuition="Compare mid, discard half each iteration.",
            java_impl=textwrap.dedent(
                """\
                public class BinarySearch {
                    public static int search(int[] a, int x) {
                        int lo = 0, hi = a.length - 1;
                        while (lo <= hi) {
                            int mid = lo + (hi - lo) / 2;
                            if (a[mid] == x) return mid;
                            if (a[mid] < x) lo = mid + 1;
                            else hi = mid - 1;
                        }
                        return -1;
                    }
                }
                """
            ),
            stream_impl=textwrap.dedent(
                """\
                public class BinarySearchStreamNote {
                    // Index-based algorithm; streams reduce clarity.
                }
                """
            ),
            sample_input="- Input: [1,3,5,8,12], x=8",
            execution_steps=bullets("mid=(lo+hi)/2", "discard half"),
            output="- Output: 3",
            complexity="- Time: O(log n)\n- Space: O(1)",
            enterprise="Used in routing tables and range lookups.",
            interview=bullets("Overflow-safe mid", "first/last occurrence"),
            best_practices=bullets("Add boundary tests", "Document sorted precondition"),
        )

    if low == "maximum subarray":
        return render(
            title,
            concept="Kadane’s algorithm computes maximum subarray sum in one pass.",
            problem="Find max contiguous sum.",
            intuition="At each i, best ending at i is max(a[i], a[i]+prev).",
            java_impl=textwrap.dedent(
                """\
                public class MaxSubarray {
                    public static int maxSum(int[] a) {
                        int cur = a[0], best = a[0];
                        for (int i = 1; i < a.length; i++) {
                            cur = Math.max(a[i], cur + a[i]);
                            best = Math.max(best, cur);
                        }
                        return best;
                    }
                }
                """
            ),
            stream_impl=textwrap.dedent(
                """\
                public class MaxSubarrayStreamNote {
                    // Sequential stateful; loop is clearer.
                }
                """
            ),
            sample_input="- Input: [-2,1,-3,4,-1,2,1,-5,4]",
            execution_steps=bullets("cur=max(a[i],cur+a[i])", "best=max(best,cur)"),
            output="- Output: 6",
            complexity="- Time: O(n)\n- Space: O(1)",
            enterprise="Useful for best-window analytics (profit/loss, traffic deltas).",
            interview=bullets("All-negative arrays", "Return indices too"),
            best_practices=bullets("Validate non-empty input", "Use long if sums can overflow"),
        )

    # ---------------- Concurrency / Executor / CF ----------------
    if low in ("threads vs processes", "thread lifecycle", "synchronization", "volatile keyword", "locks and reentrantlock"):
        return render(
            title,
            concept="Concurrency requires both mutual exclusion (atomicity) and visibility. volatile provides visibility; locks/synchronized provide mutual exclusion.",
            problem="Increment a shared counter safely from a worker thread.",
            intuition="Protect shared state with a lock; use volatile for stop flag visibility.",
            java_impl=textwrap.dedent(
                """\
                import java.util.concurrent.locks.*;

                public class ConcurrencyDemo {
                    private static volatile boolean stop = false;
                    private static int shared = 0;
                    private static final Lock lock = new ReentrantLock();

                    public static void main(String[] args) throws Exception {
                        Thread t = new Thread(() -> {
                            while (!stop) {
                                lock.lock();
                                try { shared++; }
                                finally { lock.unlock(); }
                            }
                        });
                        t.start();
                        Thread.sleep(50);
                        stop = true;
                        t.join();
                        System.out.println(shared);
                    }
                }
                """
            ),
            stream_impl=GEN_STREAM,
            sample_input="- Input: 1 worker thread",
            execution_steps=bullets("Start thread", "Increment under lock", "Stop via volatile", "Join"),
            output="- Output: some positive count",
            complexity="- N/A (concept)",
            enterprise="Incorrect synchronization causes race conditions and corrupted caches.",
            interview=bullets("volatile vs AtomicInteger", "ReentrantLock vs synchronized"),
            best_practices=bullets("Prefer higher-level concurrency utilities", "Keep critical sections small"),
        )

    if low in ("executor interface", "executorservice", "threadpoolexecutor", "scheduledexecutorservice", "forkjoinpool"):
        return render(
            title,
            concept="Executors manage thread pools so you don’t create raw threads per task.",
            problem="Compute a value asynchronously and fetch it.",
            intuition="Submit tasks to a pool; get results via Future.",
            java_impl=textwrap.dedent(
                """\
                import java.util.concurrent.*;

                public class ExecutorExample {
                    public static void main(String[] args) throws Exception {
                        ExecutorService pool = Executors.newFixedThreadPool(4);
                        Future<Integer> f = pool.submit(() -> 40 + 2);
                        System.out.println(f.get());
                        pool.shutdown();
                    }
                }
                """
            ),
            stream_impl=GEN_STREAM,
            sample_input="- Input: compute 40+2",
            execution_steps=bullets("Create pool", "Submit", "get()", "shutdown"),
            output="- Output: 42",
            complexity="- N/A (concept)",
            enterprise="Thread pool sizing and queueing impacts latency and tail behavior.",
            interview=bullets("Fixed vs cached pool", "shutdown semantics"),
            best_practices=bullets("Always shutdown pools", "Separate IO vs CPU pools", "Avoid unbounded queues"),
        )

    if low in ("completablefuture overview", "supplyasync", "runasync", "thenapply", "thencompose", "thencombine", "exceptionally", "allof", "anyof"):
        return render(
            title,
            concept="CompletableFuture composes async computations with clear chaining and centralized error handling.",
            problem="Run two async computations and combine results.",
            intuition="thenApply maps result, thenCompose flattens async, thenCombine combines two futures.",
            java_impl=textwrap.dedent(
                """\
                import java.util.concurrent.*;

                public class CfExample {
                    public static void main(String[] args) {
                        CompletableFuture<Integer> a = CompletableFuture.supplyAsync(() -> 20);
                        CompletableFuture<Integer> b = CompletableFuture.supplyAsync(() -> 22);
                        CompletableFuture<Integer> c = a.thenCombine(b, Integer::sum)
                                .exceptionally(ex -> 0);
                        System.out.println(c.join());
                    }
                }
                """
            ),
            stream_impl=GEN_STREAM,
            sample_input="- Input: async values 20 and 22",
            execution_steps=bullets("Start futures", "Combine", "join"),
            output="- Output: 42",
            complexity="- N/A (concept)",
            enterprise="Used for parallel API calls; use explicit executors and timeouts.",
            interview=bullets("thenCompose vs thenApply", "join vs get", "exception propagation"),
            best_practices=bullets("Use dedicated executor", "Add timeouts", "Avoid blocking in async stages"),
        )

    # For remaining topics: non-empty page with safe reference snippet
    return render(
        title,
        concept=f"{title} is a Java 8 topic relevant in production and interviews. This page gives a concise reference and example.",
        problem=f"Demonstrate {title} with a small example and discuss edge cases.",
        intuition="Start with the simplest correct approach. Optimize only when required by constraints.\n\nASCII: input -> process -> output",
        java_impl=GEN_JAVA,
        stream_impl=GEN_STREAM,
        sample_input="- Input: (choose a minimal representative input)",
        execution_steps=bullets("Define sample input", "Run logic", "Verify output"),
        output="- Output: (expected output)",
        complexity="- Time: depends on approach\n- Space: depends on approach",
        enterprise="Explain where this appears in real systems and production pitfalls.",
        interview=bullets("Edge cases", "Complexity", "Alternatives", "Testing"),
        best_practices=bullets("Prefer clarity", "Write tests", "Document assumptions"),
    )


def main() -> None:
    root = Path(__file__).resolve().parent

    mkdocs_yml = (root / "mkdocs.yml").read_text(encoding="utf-8")

    # Extract lines like "- Title: section-XX/file.md" or "- Title: cheatsheets/x.md"
    specs: list[PageSpec] = []
    for line in mkdocs_yml.splitlines():
        m = re.search(r"-\s+(.+?):\s+([^\s]+\.md)\s*$", line)
        if not m:
            continue
        title = m.group(1).strip()
        rel = "docs/" + m.group(2).strip()
        specs.append(PageSpec(rel, title))

    wrote = 0
    for spec in specs:
        target = root / spec.rel_path
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(page_for(spec.title), encoding="utf-8")
        wrote += 1

    idx = root / "docs" / "index.md"
    idx.write_text("# Java 8 Engineering & Interview Preparation\n\nUse the navigation to browse topics by section.\n", encoding="utf-8")

    print(f"Wrote {wrote} pages from mkdocs.yml (v2 generator).")


if __name__ == "__main__":
    main()
