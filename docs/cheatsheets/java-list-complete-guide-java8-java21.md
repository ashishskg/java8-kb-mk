# Java List — Cheat Sheet (Java 8, Java 21)

## What `List` guarantees

- **Ordered** (preserves insertion order)
- **Index-based access** (`get(i)`, `set(i, x)`)
- **Duplicates allowed**
- **Nulls**
  - Allowed in `ArrayList`, `LinkedList`
  - Not allowed in `List.of(...)` / `List.copyOf(...)` (throws `NullPointerException`)

## Common implementations

| Type | Best for | Notes |
|---|---|---|
| `ArrayList` | Fast random access | `get`/`set` are O(1); middle inserts/removes O(n) |
| `LinkedList` | Frequent add/remove at ends | Index access is O(n); also implements `Deque` |
| `CopyOnWriteArrayList` | Many reads, few writes | Writes copy the entire array |
| `List.of(...)` (Java 9+) | Immutable lists | Fixed, unmodifiable, no nulls |
| `Arrays.asList(...)` | Fixed-size view of array | No structural change (`add/remove` throws) |

## Core methods (with gotchas)

### Add

```java
List<String> l = new ArrayList<>();
l.add("a");               // append
l.add(0, "first");        // insert
l.addAll(List.of("x", "y"));
```

- `add(int, E)` shifts elements to the right (O(n)).

### Read / update

```java
List<String> l = new ArrayList<>(List.of("a", "b", "c"));
String x = l.get(1);           // "b"
String old = l.set(1, "B");   // old="b", l=[a, B, c]
int n = l.size();
boolean e = l.isEmpty();
```

### Remove (overload trap)

```java
List<Integer> l = new ArrayList<>(List.of(10, 20, 30));

l.remove(1);                 // removes index 1 => removes 20
l.remove(Integer.valueOf(30)); // removes element 30
```

- For `List<Integer>`, `remove(1)` calls **remove by index**. Use `Integer.valueOf(...)` to remove by value.

### Bulk ops

```java
List<Integer> l = new ArrayList<>(List.of(1,2,3,4,5));

l.removeAll(List.of(2,4));     // [1,3,5]
l.retainAll(List.of(1,5));     // [1,5]
```

### Contains / index

```java
List<String> l = List.of("a", "b", "c", "b");

l.contains("b");      // true
l.indexOf("b");       // 1
l.lastIndexOf("b");   // 3
```

### `subList` (view, not copy)

```java
List<String> l = new ArrayList<>(List.of("a","b","c","d"));
List<String> sub = l.subList(1, 3); // [b, c]
sub.set(0, "B");                 // l becomes [a, B, c, d]
```

- `subList` is a **view** backed by the original list.

### Convert

```java
List<String> l = List.of("a", "b", "c");

Object[] a1 = l.toArray();
String[] a2 = l.toArray(new String[0]);
```

## Java 8: functional list operations

### `replaceAll`

```java
List<Integer> l = new ArrayList<>(List.of(1,2,3));
l.replaceAll(x -> x * 2); // [2,4,6]
```

### `sort`

```java
List<Integer> l = new ArrayList<>(List.of(3,1,2));
l.sort(Comparator.naturalOrder()); // [1,2,3]
l.sort(Comparator.reverseOrder()); // [3,2,1]
```

### Remove by predicate

```java
List<String> l = new ArrayList<>(List.of("a","bb","c"));
l.removeIf(s -> s.length() == 1); // [bb]
```

## List transforms (Java 8)

### List → List (map)

```java
List<String> in = List.of("apple", "banana");
List<String> out = in.stream()
    .map(String::toUpperCase)
    .collect(Collectors.toList());
```

### List → Map

```java
List<String> in = List.of("apple", "banana", "mango");

// key=string, value=length
Map<String, Integer> m = in.stream()
    .collect(Collectors.toMap(Function.identity(), String::length));
```

Duplicates (merge):

```java
List<String> in = List.of("a", "b", "a");
Map<String, Integer> freq = in.stream()
    .collect(Collectors.toMap(Function.identity(), x -> 1, Integer::sum));
// {a=2, b=1}
```

### groupBy / partition

```java
List<String> in = List.of("apple", "apricot", "banana");

Map<Character, List<String>> byFirst = in.stream()
    .collect(Collectors.groupingBy(s -> s.charAt(0)));

Map<Boolean, List<String>> partition = in.stream()
    .collect(Collectors.partitioningBy(s -> s.length() >= 6));
```

## Java 21 (SequencedCollection) additions

`List` extends `SequencedCollection` in Java 21.

```java
List<String> l = new ArrayList<>(List.of("a","b","c"));

l.getFirst();     // "a"
l.getLast();      // "c"

List<String> r = l.reversed(); // view: [c,b,a]

l.addFirst("0");
l.addLast("d");

l.removeFirst();
l.removeLast();
```

## Quick “choose this”

- Use **`ArrayList`** by default.
- Use **`LinkedList`** only when you truly need deque-like behavior and you don’t do lots of `get(i)`.
- Use **`List.of` / `List.copyOf`** for immutable lists.
