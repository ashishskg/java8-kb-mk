# Stream creation (Java 8)

## Conventions used in examples
```java
import java.util.*;
import java.util.function.*;
import java.util.stream.*;

List<String> names = Arrays.asList("amy", "bob", "carl", "bob");
Stream<String> s = names.stream();
```

## `Stream.of(T...)`
```java
Stream<Integer> xs = Stream.of(1, 2, 3);
```
Input: `1, 2, 3`

Output: stream elements `[1, 2, 3]`

Production note: Prefer `Stream.ofNullable` only exists in Java 9+; in Java 8 guard nulls explicitly.

## `Stream.empty()`
```java
Stream<String> none = Stream.empty();
```
Input: none

Output: stream elements `[]`

Production note: Use to avoid returning `null` streams.

## `Stream.builder()`
```java
Stream<String> built = Stream.<String>builder().add("a").add("b").build();
```
Input: added elements `"a"`, `"b"`

Output: stream elements `["a", "b"]`

Production note: Useful when conditionally adding elements.

## `Stream.generate(Supplier<T>)`
```java
Stream<Double> rnd = Stream.generate(Math::random).limit(3);
```
Input: `Math.random()` supplier, `limit(3)`

Output: 3 pseudo-random doubles (example: `[0.12, 0.98, 0.44]`)

Production note: Always bound it (`limit`) to avoid infinite streams.

## `Stream.iterate(T, UnaryOperator<T>)`
```java
Stream<Integer> powers2 = Stream.iterate(1, x -> x * 2).limit(5);
```
Input: seed `1`, rule `x -> x * 2`, `limit(5)`

Output: stream elements `[1, 2, 4, 8, 16]`

Production note: Infinite unless bounded.

## `Stream.concat(Stream<? extends T>, Stream<? extends T>)`
```java
Stream<Integer> a = Stream.of(1, 2);
Stream<Integer> b = Stream.of(3, 4);
Stream<Integer> c = Stream.concat(a, b);
```
Input: streams `[1, 2]` and `[3, 4]`

Output: concatenated stream elements `[1, 2, 3, 4]`

Production note: Concatenation is lazy, but both sources must still be consumed in order.

## `Collection.stream()` / `Collection.parallelStream()`
```java
Stream<String> st = names.stream();
Stream<String> pst = names.parallelStream();
```
Input: `names = ["amy", "bob", "carl", "bob"]`

Output: stream elements `["amy", "bob", "carl", "bob"]` (same elements; execution mode differs)

Production note: Prefer `stream()` by default; parallel needs measurement + non-interfering operations.

## Enterprise example: building an optional filter pipeline safely
```java
class Employee {
    final String dept;
    final int salary;
    Employee(String dept, int salary) { this.dept = dept; this.salary = salary; }
}

List<Employee> emps = Arrays.asList(new Employee("ENG", 200), new Employee("HR", 120));

Optional<String> deptFilter = Optional.of("ENG");
OptionalInt minSalary = OptionalInt.empty();

Stream<Employee> base = emps.stream();
if (deptFilter.isPresent()) base = base.filter(e -> deptFilter.get().equals(e.dept));
if (minSalary.isPresent()) base = base.filter(e -> e.salary >= minSalary.getAsInt());

List<Employee> out = base.collect(Collectors.toList());
```
Input: `deptFilter=ENG`, `minSalary=empty`, employees `[(ENG,200),(HR,120)]`

Output: `[(ENG,200)]`

Production note: Prefer composing pure predicates; avoid building streams from nullable sources.
