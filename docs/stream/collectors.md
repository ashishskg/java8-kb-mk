# Collectors (Java 8)

## `toList()` / `toSet()`
```java
List<String> names = Arrays.asList("amy", "bob", "carl", "bob");
List<String> l = names.stream().collect(Collectors.toList());
Set<String> set = names.stream().collect(Collectors.toSet());
```
Input: `names=["amy","bob","carl","bob"]`

Output: `l=["amy","bob","carl","bob"]`, `set` contains `["amy","bob","carl"]`

Production note: `toList()` does not guarantee mutability type; don’t rely on `ArrayList`.

## `toCollection(Supplier<C>)`
```java
List<String> names = Arrays.asList("amy", "bob");
LinkedList<String> ll = names.stream().collect(Collectors.toCollection(LinkedList::new));
```
Input: `names=["amy","bob"]`

Output: `ll=["amy","bob"]` as a `LinkedList`

Production note: Use when you need a specific collection type.

## `joining()`
```java
List<String> names = Arrays.asList("amy", "bob");
String csv = names.stream().collect(Collectors.joining(","));
```
Input: `names=["amy","bob"]`

Output: `"amy,bob"`

Production note: If elements can be null, map to safe strings first.

## `counting()`
```java
List<String> names = Arrays.asList("amy", "bob");
long n = names.stream().collect(Collectors.counting());
```
Input: `names=["amy","bob"]`

Output: `2`

Production note: Equivalent to `count()` but composes inside downstream collectors.

## `groupingBy(...)`
```java
List<String> names = Arrays.asList("amy", "bob", "carl", "bob");
Map<Integer, List<String>> byLen = names.stream().collect(Collectors.groupingBy(String::length));
Map<Integer, Long> byLenCount = names.stream().collect(Collectors.groupingBy(String::length, Collectors.counting()));
```
Input: `names=["amy","bob","carl","bob"]`

Output: `byLen={3=["amy","bob","bob"], 4=["carl"]}`, `byLenCount={3=3, 4=1}`

Production note: For parallel streams, consider `groupingByConcurrent`.

## `partitioningBy(...)`
```java
List<String> names = Arrays.asList("amy", "bob", "carl", "bob");
Map<Boolean, List<String>> parts = names.stream().collect(Collectors.partitioningBy(n -> n.length() == 3));
```
Input: `names=["amy","bob","carl","bob"]`

Output: `parts={true=["amy","bob","bob"], false=["carl"]}`

Production note: Always yields exactly two keys: `true` and `false`.

## `mapping(...)` (downstream transform)
```java
List<String> names = Arrays.asList("amy", "bob", "carl", "bob");
Map<Integer, Set<Character>> firstCharByLen = names.stream().collect(
    Collectors.groupingBy(String::length, Collectors.mapping(n -> n.charAt(0), Collectors.toSet()))
);
```
Input: `names=["amy","bob","carl","bob"]`

Output: `firstCharByLen={3=['a','b'], 4=['c']}`

Production note: Prefer `mapping` over manual post-processing.

## `collectingAndThen(...)` (immutability)
```java
List<String> names = Arrays.asList("amy", "bob");
List<String> unmodifiable = names.stream().collect(
    Collectors.collectingAndThen(Collectors.toList(), Collections::unmodifiableList)
);
```
Input: `names=["amy","bob"]`

Output: unmodifiable list `["amy","bob"]`

Production note: Use to enforce immutability at the boundary.

## `toMap(...)` (merge collisions)
```java
List<String> names = Arrays.asList("amy", "bob", "bob");
Map<String, Integer> lastLen = names.stream().collect(Collectors.toMap(n -> n, String::length, (a, b) -> b));
```
Input: `names=["amy","bob","bob"]`

Output: `lastLen={amy=3, bob=3}`

Production note: Always specify a merge function if duplicates are possible.

## `summarizingInt(...)` / `averagingInt(...)`
```java
List<String> names = Arrays.asList("amy", "bob", "carl");
IntSummaryStatistics st = names.stream().collect(Collectors.summarizingInt(String::length));
double avgLen = names.stream().collect(Collectors.averagingInt(String::length));
```
Input: `names=["amy","bob","carl"]`

Output: `st(count=3,sum=10,min=3,max=4,avg=3.333...)`, `avgLen=3.333...`

Production note: Prefer summarizing collectors to avoid multiple passes.

## `reducing(...)`
```java
List<String> names = Arrays.asList("amy", "bob", "carl");
Optional<String> longest = names.stream().collect(
    Collectors.reducing((a, b) -> a.length() >= b.length() ? a : b)
);
```
Input: `names=["amy","bob","carl"]`

Output: `longest=Optional[carl]`

Production note: Prefer `max(comparingInt(...))` when it reads better.

## `groupingByConcurrent(...)`
```java
List<String> names = Arrays.asList("amy", "bob", "carl", "bob");
Map<Integer, List<String>> byLen = names.parallelStream().collect(Collectors.groupingByConcurrent(String::length));
```
Input: `names=["amy","bob","carl","bob"]` (parallel)

Output: same key grouping as `groupingBy` (ordering of lists may differ)

Production note: Only consider for parallel pipelines; still validate ordering requirements.

## `partitioningBy(..., downstream)`
```java
List<String> names = Arrays.asList("amy", "bob", "carl", "bob");
Map<Boolean, Long> countLen3 = names.stream().collect(
    Collectors.partitioningBy(n -> n.length() == 3, Collectors.counting())
);
```
Input: `names=["amy","bob","carl","bob"]`

Output: `countLen3={true=3, false=1}`

Production note: Partitioning is a specialized 2-bucket grouping; downstream collectors are common.

## `teeing(...)` is not in Java 8
Production note: The `teeing` collector is Java 12+. In Java 8, compute multiple aggregates using `summaryStatistics` (primitive) or a custom mutable container.

## Enterprise example: aggregation for an API response
```java
class Event {
    final String service;
    final String level;
    Event(String service, String level) { this.service = service; this.level = level; }
}

List<Event> events = Arrays.asList(
    new Event("orders", "INFO"),
    new Event("orders", "ERROR"),
    new Event("billing", "INFO")
);

Map<String, Map<String, Long>> counts = events.stream().collect(
    Collectors.groupingBy(
        e -> e.service,
        Collectors.groupingBy(e -> e.level, Collectors.counting())
    )
);
```
Input: `[(orders,INFO),(orders,ERROR),(billing,INFO)]`

Output: `{orders={INFO=1, ERROR=1}, billing={INFO=1}}`

Production note: Multi-level grouping is common for dashboards; keep keys stable and document missing keys.
