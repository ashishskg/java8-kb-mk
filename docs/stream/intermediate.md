# Intermediate operations (Java 8)

## `filter(Predicate<? super T>)`
```java
List<String> bNames = Arrays.asList("amy", "bob", "carl", "bob")
    .stream()
    .filter(n -> n.startsWith("b"))
    .collect(Collectors.toList());
```
Input: `["amy", "bob", "carl", "bob"]`

Output: `["bob", "bob"]`

Production note: Avoid predicates with side-effects.

## `map(Function<? super T,? extends R>)`
```java
List<Integer> lens = Arrays.asList("amy", "bob", "carl")
    .stream()
    .map(String::length)
    .collect(Collectors.toList());
```
Input: `["amy", "bob", "carl"]`

Output: `[3, 3, 4]`

Production note: Mapping should be fast and deterministic.

## `flatMap(Function<? super T,? extends Stream<? extends R>>)`
```java
List<List<Integer>> matrix = Arrays.asList(Arrays.asList(1,2), Arrays.asList(3));
List<Integer> flat = matrix.stream().flatMap(List::stream).collect(Collectors.toList());
```
Input: `[[1,2],[3]]`

Output: `[1, 2, 3]`

Production note: `flatMap` is the correct tool for 1-to-many transformations.

## `distinct()`
```java
List<String> uniq = Arrays.asList("amy", "bob", "carl", "bob")
    .stream()
    .distinct()
    .collect(Collectors.toList());
```
Input: `["amy", "bob", "carl", "bob"]`

Output: `["amy", "bob", "carl"]`

Production note: Uses `equals`/`hashCode`; can be memory-heavy on large streams.

## `sorted()` / `sorted(Comparator)`
```java
List<String> sorted = Arrays.asList("amy", "bob", "carl")
    .stream()
    .sorted()
    .collect(Collectors.toList());

List<String> sortedLen = Arrays.asList("amy", "bob", "carl")
    .stream()
    .sorted(Comparator.comparingInt(String::length))
    .collect(Collectors.toList());
```
Input: `["amy", "bob", "carl"]`

Output (sorted): `["amy", "bob", "carl"]`

Output (sorted by length): `["amy", "bob", "carl"]`

Production note: `sorted()` is stateful; avoid in hot paths if not needed.

## `peek(Consumer<? super T>)`
```java
List<String> out = Arrays.asList("amy", "bob", "carl")
    .stream()
    .peek(n -> System.out.println("DBG: " + n))
    .filter(n -> n.length() >= 3)
    .collect(Collectors.toList());
```
Input: `["amy", "bob", "carl"]`

Output: `["amy", "bob", "carl"]`

Production note: Use for debugging only; do not build business logic on `peek`.

## `limit(long)` / `skip(long)`
```java
List<String> first2 = Arrays.asList("a", "b", "c").stream().limit(2).collect(Collectors.toList());
List<String> after2 = Arrays.asList("a", "b", "c").stream().skip(2).collect(Collectors.toList());
```
Input: `["a", "b", "c"]`

Output (limit 2): `["a", "b"]`

Output (skip 2): `["c"]`

Production note: `limit` is short-circuiting; works best with ordered streams.

## `mapToInt` / `mapToLong` / `mapToDouble`
```java
IntStream lengths = Arrays.asList("amy", "bob", "carl").stream().mapToInt(String::length);
```
Input: `["amy", "bob", "carl"]`

Output: `IntStream` elements `[3, 3, 4]`

Production note: Prefer primitive streams to avoid boxing.

## `flatMapToInt` / `flatMapToLong` / `flatMapToDouble`
```java
Stream<String> csv = Stream.of("1,2", "10");
IntStream nums = csv.flatMapToInt(line -> Arrays.stream(line.split(",")).mapToInt(Integer::parseInt));
```
Input: `["1,2", "10"]`

Output: `IntStream` elements `[1, 2, 10]`

Production note: Keep parsing/IO out of parallel streams unless carefully controlled.

## Enterprise example: stream pipeline for service-layer DTO mapping
```java
class Order {
    final String id;
    final int cents;
    Order(String id, int cents) { this.id = id; this.cents = cents; }
}
class OrderDto {
    final String id;
    final String amount;
    OrderDto(String id, String amount) { this.id = id; this.amount = amount; }
}

List<Order> orders = Arrays.asList(new Order("o1", 1200), new Order("o2", 50));

List<OrderDto> dtos = orders.stream()
    .filter(o -> o.cents >= 100)
    .sorted(Comparator.comparingInt((Order o) -> o.cents).reversed())
    .map(o -> new OrderDto(o.id, String.format("$%.2f", o.cents / 100.0)))
    .collect(Collectors.toList());
```
Input: `[(o1,1200),(o2,50)]`

Output: `[(o1,"$12.00")]`

Production note: Keep the pipeline pure; do IO/logging outside (or only with debug `peek`).
