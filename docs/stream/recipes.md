# Stream recipes (advanced patterns)

## Fibonacci (first N numbers)
```java
int n = 10;
List<Long> fib = Stream.iterate(new long[]{0L, 1L}, a -> new long[]{a[1], a[0] + a[1]})
    .limit(n)
    .map(a -> a[0])
    .collect(Collectors.toList());
```
Input: `n=10`

Output: `fib=[0,1,1,2,3,5,8,13,21,34]`

Production note: This allocates arrays; for hot paths prefer a loop.

## Factorial (stream)
```java
int k = 6;
long fact = LongStream.rangeClosed(1, k).reduce(1L, (a, b) -> a * b);
```
Input: `k=6`

Output: `fact=720`

Production note: Watch overflow; factorial grows fast.

## Second highest salary (overall)
```java
class Emp {
    final String name;
    final String dept;
    final int salary;
    Emp(String name, String dept, int salary) { this.name = name; this.dept = dept; this.salary = salary; }
}

List<Emp> emps = Arrays.asList(
    new Emp("A", "HR", 100),
    new Emp("B", "HR", 120),
    new Emp("C", "ENG", 200),
    new Emp("D", "ENG", 180)
);

Optional<Integer> second = emps.stream()
    .map(e -> e.salary)
    .distinct()
    .sorted(Comparator.reverseOrder())
    .skip(1)
    .findFirst();
```
Input: salaries `[100,120,200,180]`

Output: `second=Optional[180]`

Production note: `sorted().skip(1)` is fine for small/medium data; for very large data use a top-2 reduction.

## Second highest salary per department
```java
Map<String, Optional<Integer>> secondPerDept = emps.stream().collect(
    Collectors.groupingBy(
        e -> e.dept,
        Collectors.collectingAndThen(
            Collectors.mapping(e -> e.salary, Collectors.toSet()),
            s -> s.stream().sorted(Comparator.reverseOrder()).skip(1).findFirst()
        )
    )
);
```
Input: HR `[100,120]`, ENG `[200,180]`

Output: `{HR=Optional[100], ENG=Optional[180]}`

Production note: Using `toSet()` removes duplicates; define whether duplicates should matter.

## `partitioningBy` + downstream aggregation
```java
Map<Boolean, Double> avgByHighPay = emps.stream().collect(
    Collectors.partitioningBy(e -> e.salary >= 150, Collectors.averagingInt(e -> e.salary))
);
```
Input: salaries `[100,120,200,180]`, threshold `>=150`

Output: `{false=110.0, true=190.0}`

Production note: Partitioning is clearer than `groupingBy(e -> predicate)` for boolean splits.

## Multi-level `groupingBy` (dept -> salary band -> count)
```java
Function<Emp, String> band = e -> e.salary >= 150 ? "HIGH" : "LOW";

Map<String, Map<String, Long>> counts = emps.stream().collect(
    Collectors.groupingBy(
        e -> e.dept,
        Collectors.groupingBy(band, Collectors.counting())
    )
);
```
Input: HR salaries `[100,120]`, ENG salaries `[200,180]`

Output: `{HR={LOW=2}, ENG={HIGH=2}}`

Production note: Multi-level grouping can get hard to read; consider extracting named functions.

## `toMap` with merge function
```java
Map<String, Integer> maxSalaryByDept = emps.stream().collect(
    Collectors.toMap(
        e -> e.dept,
        e -> e.salary,
        Integer::max
    )
);
```
Input: ENG `[200,180]`, HR `[100,120]`

Output: `{ENG=200, HR=120}`

Production note: Always decide how to resolve key collisions.

## Top-N pattern
```java
List<Emp> top2 = emps.stream()
    .sorted(Comparator.comparingInt((Emp e) -> e.salary).reversed())
    .limit(2)
    .collect(Collectors.toList());
```
Input: salaries `[100,120,200,180]`

Output: top2 salaries `[200,180]`

Production note: Sorting is O(n log n). For massive inputs, consider a bounded heap.

## Parallel stream pitfalls (stateful lambda anti-pattern)
```java
List<Integer> out = new ArrayList<>();
// Anti-pattern:
// IntStream.range(0, 1000).parallel().forEach(out::add);
```
Input: `range(0,1000)` with shared mutable list

Output: race conditions / lost updates / `ArrayIndexOutOfBoundsException` risk

Production note: Never mutate shared non-thread-safe state from parallel pipelines.

## Enterprise scenario: payroll analytics (safe aggregation)
Input: employee stream of `(dept, salary)` records

Output: stable aggregates (counts, max, second-highest, averages) suitable for APIs/dashboards

Production note: Prefer deterministic collectors (`groupingBy` + `counting/summingInt/averagingInt`) and keep sorting-based “top N” to bounded datasets (or replace with top-k reduction).
