# Primitive streams (IntStream/LongStream/DoubleStream)

## `IntStream.of(int...)` / `LongStream.of(long...)` / `DoubleStream.of(double...)`
```java
IntStream is = IntStream.of(1, 2, 3);
```
Input: `1, 2, 3`

Output: `IntStream` elements `[1, 2, 3]`

Production note: Prefer primitive streams when doing numeric aggregation.

## `range` / `rangeClosed`
```java
IntStream r1 = IntStream.range(0, 3);       // 0,1,2
IntStream r2 = IntStream.rangeClosed(0, 3); // 0,1,2,3
```
Input: `range(0,3)`, `rangeClosed(0,3)`

Output: `r1=[0,1,2]`, `r2=[0,1,2,3]`

Production note: `range` is exclusive at end; watch off-by-one.

## `boxed()`
```java
List<Integer> boxed = IntStream.range(0, 3).boxed().collect(Collectors.toList());
```
Input: `IntStream.range(0,3)`

Output: `boxed = [0, 1, 2]`

Production note: Boxing allocates; avoid unless required by APIs.

## `sum()` / `average()` / `summaryStatistics()`
```java
int sum = IntStream.of(1,2,3).sum();
OptionalDouble avg = IntStream.of(1,2,3).average();
IntSummaryStatistics stats = IntStream.of(1,2,3).summaryStatistics();
```
Input: `[1, 2, 3]`

Output: `sum=6`, `avg=OptionalDouble[2.0]`, `stats(count=3, sum=6, min=1, max=3, average=2.0)`

Production note: `average()` returns `OptionalDouble` for empty streams.

## Primitive `map` / `filter`
```java
int[] squares = IntStream.rangeClosed(1, 3).map(x -> x * x).toArray();
```
Input: `rangeClosed(1,3) => [1,2,3]`

Output: `squares = [1, 4, 9]`

Production note: Prefer primitives to keep the pipeline allocation-light.

## `asLongStream()` / `asDoubleStream()`
```java
LongStream ls = IntStream.rangeClosed(1, 3).asLongStream();
DoubleStream ds = IntStream.rangeClosed(1, 3).asDoubleStream();
```
Input: `IntStream [1,2,3]`

Output: `ls=[1L,2L,3L]`, `ds=[1.0,2.0,3.0]`

Production note: Use when widening numeric type without boxing.

## `mapToObj(...)`
```java
List<String> labels = IntStream.rangeClosed(1, 3)
    .mapToObj(i -> "id-" + i)
    .collect(Collectors.toList());
```
Input: `IntStream [1,2,3]`

Output: `labels = ["id-1", "id-2", "id-3"]`

Production note: Keep numeric work primitive until the last possible step.

## Primitive `flatMap(...)`
```java
int[] expanded = IntStream.of(1, 3)
    .flatMap(n -> IntStream.rangeClosed(1, n))
    .toArray();
```
Input: `[1, 3]`

Output: `expanded = [1, 1, 2, 3]`

Production note: Like `Stream.flatMap`, but stays primitive.

## Primitive `reduce` / `min` / `max`
```java
int prod = IntStream.rangeClosed(1, 5).reduce(1, (a, b) -> a * b);
OptionalInt mn = IntStream.of(4, 2, 9).min();
OptionalInt mx = IntStream.of(4, 2, 9).max();
```
Input: `rangeClosed(1,5) => [1,2,3,4,5]`, `[4,2,9]`

Output: `prod=120`, `mn=OptionalInt[2]`, `mx=OptionalInt[9]`

Production note: Use identity overloads to avoid optionals when the identity makes sense.

## Primitive `findFirst` / `findAny` / matches
```java
OptionalInt firstEven = IntStream.rangeClosed(1, 10).filter(x -> x % 2 == 0).findFirst();
OptionalInt anyEven = IntStream.rangeClosed(1, 10).parallel().filter(x -> x % 2 == 0).findAny();
boolean anyGt100 = IntStream.of(1, 50, 200).anyMatch(x -> x > 100);
```
Input: `rangeClosed(1,10)`, `[1,50,200]`

Output: `firstEven=OptionalInt[2]`, `anyEven=OptionalInt[2]` (or another even), `anyGt100=true`

Production note: `findAny` can be faster on parallel.

## `boxed()` vs primitive-first pipelines
```java
List<Integer> odds = IntStream.rangeClosed(1, 9)
    .filter(x -> (x & 1) == 1)
    .boxed()
    .collect(Collectors.toList());
```
Input: `rangeClosed(1,9) => [1..9]`

Output: `odds = [1, 3, 5, 7, 9]`

Production note: Do all numeric filtering/mapping before `boxed()`.

## Enterprise example: numeric aggregation without boxing
```java
class Invoice {
    final String customerId;
    final int cents;
    Invoice(String customerId, int cents) { this.customerId = customerId; this.cents = cents; }
}

List<Invoice> invoices = Arrays.asList(
    new Invoice("c1", 1200),
    new Invoice("c1", 800),
    new Invoice("c2", 500)
);

IntSummaryStatistics stats = invoices.stream()
    .mapToInt(i -> i.cents)
    .summaryStatistics();
```
Input: cents `[1200, 800, 500]`

Output: `stats(count=3, sum=2500, min=500, max=1200, average=833.33...)`

Production note: `mapToInt(...).summaryStatistics()` is a clean single-pass aggregate.
