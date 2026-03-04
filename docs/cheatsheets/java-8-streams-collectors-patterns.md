# Java 8 Streams + Collectors — Cheat Sheet (Patterns + Recipes)

## Imports you almost always need

```java
import java.util.*;
import java.util.function.*;
import java.util.stream.*;
```

## Stream pipeline mental model

- **Source** → **0..n intermediate ops** → **terminal op**
- Intermediate ops are **lazy**.
- Terminal ops trigger execution.

## Core intermediate ops

### filter / map

```java
List<String> in = List.of("apple", "banana", "apricot");

List<String> a = in.stream()
    .filter(s -> s.startsWith("a"))
    .map(String::toUpperCase)
    .collect(Collectors.toList());
// [APPLE, APRICOT]
```

### flatMap (List<List<T>> → List<T>)

```java
List<List<Integer>> nested = List.of(List.of(1,2), List.of(3,4));

List<Integer> flat = nested.stream()
    .flatMap(List::stream)
    .collect(Collectors.toList());
// [1,2,3,4]
```

### distinct / sorted / limit / skip

```java
List<Integer> in = List.of(3, 1, 2, 1, 3);

List<Integer> out = in.stream()
    .distinct()
    .sorted()
    .skip(1)
    .limit(2)
    .collect(Collectors.toList());
// [2, 3]
```

## Terminal ops

### forEach

```java
in.stream().forEach(System.out::println);
```

### reduce

```java
int sum = List.of(1,2,3).stream().reduce(0, Integer::sum);
Optional<Integer> product = List.of(1,2,3).stream().reduce((a,b) -> a*b);
```

### findFirst / findAny / match

```java
Optional<String> first = in.stream().filter(s -> s.length() > 5).findFirst();
boolean any = in.stream().anyMatch(s -> s.startsWith("b"));
boolean all = in.stream().allMatch(s -> !s.isEmpty());
```

## Collectors (the workhorses)

### toList / toSet

```java
List<String> l = in.stream().collect(Collectors.toList());
Set<String> s = in.stream().collect(Collectors.toSet());
```

### joining

```java
String joined = in.stream().collect(Collectors.joining(", "));
```

### toMap (basic)

```java
Map<String, Integer> len = in.stream()
    .collect(Collectors.toMap(Function.identity(), String::length));
```

### toMap with duplicates (merge)

```java
List<String> in2 = List.of("a", "b", "a");

Map<String, Integer> freq = in2.stream()
    .collect(Collectors.toMap(Function.identity(), x -> 1, Integer::sum));
// {a=2, b=1}
```

### groupingBy (List → Map<K, List<V>>)

```java
Map<Character, List<String>> byFirst = in.stream()
    .collect(Collectors.groupingBy(s -> s.charAt(0)));
```

### groupingBy + downstream (counting)

```java
Map<Character, Long> countByFirst = in.stream()
    .collect(Collectors.groupingBy(s -> s.charAt(0), Collectors.counting()));
```

### groupingBy + downstream (mapping)

```java
Map<Character, String> upperJoined = in.stream()
    .collect(Collectors.groupingBy(s -> s.charAt(0),
        Collectors.mapping(String::toUpperCase, Collectors.joining(","))
    ));
```

### partitioningBy

```java
Map<Boolean, List<String>> parts = in.stream()
    .collect(Collectors.partitioningBy(s -> s.length() >= 6));

List<String> longOnes = parts.get(true);
List<String> shortOnes = parts.get(false);
```

## Interview-style recipes

### Frequency map

```java
List<String> xs = List.of("a","b","a","c","b","a");
Map<String, Long> freq = xs.stream()
    .collect(Collectors.groupingBy(Function.identity(), Collectors.counting()));
```

### Remove duplicates preserving order

```java
List<String> distinct = xs.stream().distinct().collect(Collectors.toList());
```

### Sort by frequency then by value

```java
Map<String, Long> freq = xs.stream()
    .collect(Collectors.groupingBy(Function.identity(), Collectors.counting()));

List<String> sorted = xs.stream()
    .distinct()
    .sorted(Comparator.comparing(freq::get).reversed().thenComparing(Function.identity()))
    .collect(Collectors.toList());
```

### Zip two lists to a map

```java
List<String> keys = List.of("a","b","c");
List<Integer> vals = List.of(1,2,3);

Map<String, Integer> m = IntStream.range(0, keys.size())
    .boxed()
    .collect(Collectors.toMap(keys::get, vals::get));
```

### Chunk a list into sublists of size n

```java
List<Integer> xs = List.of(1,2,3,4,5,6);
int n = 2;

List<List<Integer>> chunks = IntStream
    .range(0, (xs.size() + n - 1) / n)
    .mapToObj(i -> xs.subList(i * n, Math.min((i + 1) * n, xs.size())))
    .collect(Collectors.toList());
```

## Parallel streams: when to avoid

- Avoid when:
  - you do blocking I/O
  - your work is small
  - you rely on encounter order (`forEachOrdered` is slower)
  - you mutate shared state

