# BaseStream controls (Java 8)

## `iterator()` / `spliterator()`
```java
List<String> names = Arrays.asList("amy", "bob");
Iterator<String> it = names.stream().iterator();
Spliterator<String> sp = names.stream().spliterator();
```
Input: `names = ["amy", "bob"]`

Output: `it` iterates `"amy"`, then `"bob"`; `sp` splits/traverses the same elements

Production note: Prefer staying in stream pipeline; iterators often reintroduce external iteration complexity.

## `sequential()` / `parallel()` / `isParallel()`
```java
List<String> names = Arrays.asList("amy", "bob");
Stream<String> seq = names.stream().parallel().sequential();
boolean p = names.stream().parallel().isParallel();
```
Input: `names = ["amy", "bob"]`

Output: `seq` is sequential; `p = true`

Production note: Parallelism changes execution characteristics; measure and avoid shared mutable state.

## `unordered()`
```java
List<String> names = Arrays.asList("amy", "bob", "carl", "bob");
long cnt = names.stream().unordered().distinct().count();
```
Input: `names = ["amy", "bob", "carl", "bob"]`

Output: `cnt = 3`

Production note: Can improve parallel performance when encounter order isn’t required.

## `onClose(Runnable)` / `close()`
```java
List<String> names = Arrays.asList("amy", "bob");
Stream<String> st = names.stream().onClose(() -> System.out.println("closed"));
st.close();
```
Input: `names = ["amy", "bob"]`, close handler prints `"closed"`

Output: prints `closed`

Production note: Typically relevant for IO-backed streams (e.g., `Files.lines`).

## Enterprise guidance: parallel stream safety checklist
- Input: a parallel pipeline over a collection

- Output: correct results *only if* operations are non-interfering and stateless

Production note: In service code, default to sequential streams unless you can prove:
1) work is CPU-bound and sufficiently large,
2) you are not saturating shared pools,
3) lambdas don’t touch shared mutable state,
4) ordering requirements are explicit (`forEachOrdered`, avoid `unordered()` unless safe).
