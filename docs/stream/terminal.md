# Terminal operations (Java 8)

## `forEach(Consumer)` / `forEachOrdered(Consumer)`
```java
List<String> names = Arrays.asList("amy", "bob", "carl", "bob");

names.stream().forEach(System.out::println);
names.parallelStream().forEachOrdered(System.out::println);
```
Input: `names = ["amy", "bob", "carl", "bob"]`

Output: prints elements (order deterministic for `stream()`, encounter-order for `forEachOrdered`)

Production note: In parallel, `forEach` is not ordered; prefer `forEachOrdered` when order matters.

## `toArray()` / `toArray(IntFunction<A[]>)`
```java
List<String> names = Arrays.asList("amy", "bob");
Object[] arr = names.stream().toArray();
String[] arr2 = names.stream().toArray(String[]::new);
```
Input: `names = ["amy", "bob"]`

Output: `arr = ["amy", "bob"]`, `arr2 = ["amy", "bob"]`

Production note: Prefer the typed overload.

## `reduce(...)`
```java
Optional<Integer> sum1 = Stream.of(1,2,3).reduce(Integer::sum);
int sum2 = Stream.of(1,2,3).reduce(0, Integer::sum);
```
Input: `[1, 2, 3]`

Output: `sum1 = Optional[6]`, `sum2 = 6`

Production note: For mutable reductions, prefer `collect`.

## `collect(...)`
```java
List<String> names = Arrays.asList("amy", "bob", "carl", "bob");

List<String> list = names.stream().collect(Collectors.toList());
String joined = names.stream().collect(StringBuilder::new, StringBuilder::append, StringBuilder::append).toString();
```
Input: `names = ["amy", "bob", "carl", "bob"]`

Output: `list = ["amy", "bob", "carl", "bob"]`, `joined = "amybobcarlbob"`

Production note: In parallel, ensure the combiner is correct and associative.

## `min(Comparator)` / `max(Comparator)`
```java
List<String> names = Arrays.asList("amy", "bob", "carl");
Optional<String> min = names.stream().min(String::compareTo);
Optional<String> max = names.stream().max(String::compareTo);
```
Input: `names = ["amy", "bob", "carl"]`

Output: `min = Optional[amy]`, `max = Optional[carl]`

Production note: For empty streams, result is `Optional.empty()`.

## `count()`
```java
long c = Arrays.asList("amy", "bob").stream().count();
```
Input: `["amy", "bob"]`

Output: `2`

Production note: `count()` forces traversal unless source has known size optimizations.

## `anyMatch` / `allMatch` / `noneMatch`
```java
List<String> names = Arrays.asList("amy", "bob", "carl", "bob");

boolean anyBob = names.stream().anyMatch("bob"::equals);
boolean allLen3 = names.stream().allMatch(n -> n.length() == 3);
boolean noneZ = names.stream().noneMatch(n -> n.startsWith("z"));
```
Input: `names = ["amy", "bob", "carl", "bob"]`

Output: `anyBob=true`, `allLen3=false`, `noneZ=true`

Production note: Short-circuiting; predicate must be non-interfering.

## `findFirst()` / `findAny()`
```java
List<String> names = Arrays.asList("amy", "bob", "carl", "bob");

Optional<String> first = names.stream().findFirst();
Optional<String> any = names.parallelStream().findAny();
```
Input: `names = ["amy", "bob", "carl", "bob"]`

Output: `first = Optional[amy]`, `any = Optional[amy]` (or another element in parallel)

Production note: `findAny` can be faster on parallel streams.

## Enterprise example: build a reporting map (service-layer aggregation)
```java
class Txn {
    final String accountId;
    final int cents;
    Txn(String accountId, int cents) { this.accountId = accountId; this.cents = cents; }
}

List<Txn> txns = Arrays.asList(
    new Txn("a1", 1200),
    new Txn("a1", 800),
    new Txn("a2", 500)
);

Map<String, Integer> totalCentsByAccount = txns.stream().collect(
    Collectors.groupingBy(t -> t.accountId, Collectors.summingInt(t -> t.cents))
);
```
Input: `[(a1,1200),(a1,800),(a2,500)]`

Output: `{a1=2000, a2=500}`

Production note: Prefer primitive summing collectors for numeric aggregation; they’re concise and avoid manual mutation.
