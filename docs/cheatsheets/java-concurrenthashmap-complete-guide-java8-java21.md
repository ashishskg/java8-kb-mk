# Java ConcurrentHashMap — Cheat Sheet (Java 8, Java 21)

## Why `ConcurrentHashMap`

- **Thread-safe `Map`** without external synchronization.
- **Reads are non-blocking** for most operations.
- **No null keys/values** (throws `NullPointerException`).
- Iteration is **weakly consistent** (does not throw `ConcurrentModificationException`, but may or may not reflect concurrent updates).

## Core operations

### put / get

```java
ConcurrentHashMap<String, Integer> m = new ConcurrentHashMap<>();

m.put("a", 1);
Integer v = m.get("a");
Integer x = m.getOrDefault("missing", 0);
```

### putIfAbsent

```java
m.putIfAbsent("k", 10);   // sets only if absent
```

## Atomic update patterns (most important)

### Counter (use `merge`)

```java
ConcurrentHashMap<String, Integer> counts = new ConcurrentHashMap<>();

counts.merge("apple", 1, Integer::sum); // atomic increment
counts.merge("apple", 1, Integer::sum);
// apple => 2
```

### Compute

```java
ConcurrentHashMap<String, Integer> m = new ConcurrentHashMap<>();

m.compute("k", (key, old) -> old == null ? 1 : old + 1);
```

- If remapping returns `null`, the entry is removed.

### computeIfAbsent (thread-safe lazy init)

```java
ConcurrentHashMap<String, List<String>> m = new ConcurrentHashMap<>();

m.computeIfAbsent("fruits", k -> new CopyOnWriteArrayList<>()).add("apple");
```

- Ensure the **value type is itself thread-safe** if multiple threads mutate it.

## Replace / remove variants

```java
m.replace("k", 1);            // replace if present
m.replace("k", 1, 2);         // CAS-style: only replace if current is 1

m.remove("k");
m.remove("k", 2);             // remove only if current value is 2
```

## size caveat

- `size()` may be **inaccurate** under concurrent updates.
- Use `mappingCount()` (Java 8+) for a long count:

```java
long n = m.mappingCount();
```

## Transform / stream usage

### replaceAll

```java
m.replaceAll((k, v) -> v * 2);
```

### Build a new concurrent map from a stream

```java
ConcurrentHashMap<String, Integer> out = input.stream()
    .collect(Collectors.toConcurrentMap(Function.identity(), String::length));
```

Duplicates (merge):

```java
ConcurrentHashMap<String, Long> freq = input.stream()
    .collect(Collectors.toConcurrentMap(Function.identity(), x -> 1L, Long::sum));
```

## Iteration

```java
m.forEach((k, v) -> System.out.println(k + "=" + v));

for (Map.Entry<String, Integer> e : m.entrySet()) {
    // weakly consistent view
}
```

## When NOT to use it

- You need **ordering**: use `ConcurrentSkipListMap` (sorted) or external ordering.
- You need to store **nulls**.
- You need full-map locking semantics (rare): consider explicit locks.

## Java 21 note (SequencedMap)

Java 21 adds `SequencedMap` APIs, but **`ConcurrentHashMap` is not ordered**, so `firstEntry()/lastEntry()/reversed()` do **not** imply insertion order.

## Quick reference

| Task | Best API |
|---|---|
| Thread-safe counter | `merge(key, 1, Integer::sum)` |
| Lazy init value | `computeIfAbsent(key, k -> value)` |
| Update based on old | `compute(key, (k, old) -> ...)` |
| Replace if unchanged | `replace(key, old, new)` |
| Remove if matches | `remove(key, value)` |
