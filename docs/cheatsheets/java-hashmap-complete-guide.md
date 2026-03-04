# Java HashMap — Complete Guide (Java 8, Java 21)

Introduction to `HashMap`, all its methods with examples and output, transformations, Map → List conversions, insertion, deletion, replace operations, and Java 8 / Java 21 examples.

---

## Table of Contents

- [1. HashMap introduction](#1-hashmap-introduction)
- [2. All HashMap methods with examples and output](#2-all-hashmap-methods-with-examples-and-output)
  - [2.1 put, putIfAbsent, putAll](#21-put-putifabsent-putall)
  - [2.2 get, getOrDefault](#22-get-getordefault)
  - [2.3 remove](#23-remove)
  - [2.4 replace, replaceAll](#24-replace-replaceall)
  - [2.5 containsKey, containsValue](#25-containskey-containsvalue)
  - [2.6 size, isEmpty, clear](#26-size-isempty-clear)
  - [2.7 keySet, values, entrySet](#27-keyset-values-entryset)
  - [2.8 compute, computeIfAbsent, computeIfPresent](#28-compute-computeifabsent-computeifpresent)
  - [2.9 merge](#29-merge)
  - [2.10 forEach (Java 8)](#210-foreach-java-8)
  - [2.11 Java 21: SequencedMap methods](#211-java-21-sequencedmap-methods)
- [3. Transformations](#3-transformations)
  - [3.1 Transform values (e.g., multiply all values by 2)](#31-transform-values-e-g-multiply-all-values-by-2)
  - [3.2 Transform keys](#32-transform-keys)
  - [3.3 Filter entries](#33-filter-entries)
- [4. Insertion operations](#4-insertion-operations)
  - [4.1 Basic insertion](#41-basic-insertion)
  - [4.2 Insert only if absent](#42-insert-only-if-absent)
  - [4.3 Insert with computeIfAbsent](#43-insert-with-computeifabsent)
  - [4.4 Insert all from another map](#44-insert-all-from-another-map)
- [5. Deletion operations](#5-deletion-operations)
  - [5.1 Remove by key](#51-remove-by-key)
  - [5.2 Remove by key-value pair](#52-remove-by-key-value-pair)
  - [5.3 Remove entries matching condition](#53-remove-entries-matching-condition)
  - [5.4 Clear all](#54-clear-all)
- [6. Replace operations](#6-replace-operations)
  - [6.1 Replace value for key](#61-replace-value-for-key)
  - [6.2 Replace if value matches](#62-replace-if-value-matches)
  - [6.3 Replace all values](#63-replace-all-values)
- [7. Map to List conversions](#7-map-to-list-conversions)
  - [7.1 Keys to List](#71-keys-to-list)
  - [7.2 Values to List](#72-values-to-list)
  - [7.3 Entries to List](#73-entries-to-list)
  - [7.4 Stream: keys to List](#74-stream-keys-to-list)
  - [7.5 Stream: values to List](#75-stream-values-to-list)
  - [7.6 Stream: entries to List of custom objects](#76-stream-entries-to-list-of-custom-objects)
  - [7.7 Map to List of keys sorted by values](#77-map-to-list-of-keys-sorted-by-values)
- [8. List to Map conversions](#8-list-to-map-conversions)
  - [8.1 List to Map (element as key, index as value)](#81-list-to-map-element-as-key-index-as-value)
  - [8.2 List to Map (element as key, transformed value)](#82-list-to-map-element-as-key-transformed-value)
  - [8.3 List to Map with duplicate keys (merge)](#83-list-to-map-with-duplicate-keys-merge)
- [9. Java 8 Stream operations with Map](#9-java-8-stream-operations-with-map)
  - [9.1 Filter entries](#91-filter-entries)
  - [9.2 Map entries to different type](#92-map-entries-to-different-type)
  - [9.3 Sort by key](#93-sort-by-key)
  - [9.4 Sort by value](#94-sort-by-value)
  - [9.5 Group by value](#95-group-by-value)
- [10. Coding interview questions](#10-coding-interview-questions)
  - [10.1 Count frequency of characters in string](#101-count-frequency-of-characters-in-string)
  - [10.2 Find first non-repeated character](#102-find-first-non-repeated-character)
  - [10.3 Two Sum (indices)](#103-two-sum-indices)
  - [10.4 Group anagrams](#104-group-anagrams)
  - [10.5 Merge two maps (sum values for same keys)](#105-merge-two-maps-sum-values-for-same-keys)
  - [10.6 Find duplicate elements](#106-find-duplicate-elements)
  - [10.7 Sort map by value (descending)](#107-sort-map-by-value-descending)
  - [10.8 Invert map (swap keys and values)](#108-invert-map-swap-keys-and-values)
  - [10.9 Find key with maximum value](#109-find-key-with-maximum-value)
  - [10.10 Check if two maps are equal (ignoring order)](#1010-check-if-two-maps-are-equal-ignoring-order)
- [11. Quick reference table](#11-quick-reference-table)

---

## 1. HashMap introduction

- **`HashMap<K, V>`** is a hash table-based implementation of the `Map` interface. It stores key-value pairs, allows one null key and multiple null values, and does not guarantee order (Java 7 and earlier) or insertion order (Java 8+).
- **Key characteristics:**
  - **O(1)** average time for `get()` and `put()` operations (assuming good hash distribution).
  - **Not thread-safe** — use `ConcurrentHashMap` or `Collections.synchronizedMap()` for multi-threaded access.
  - **No duplicate keys** — adding a duplicate key replaces the old value.
  - **Allows null** — one null key, multiple null values.

```java
Map<String, Integer> map = new HashMap<>();
Map<String, Integer> withCapacity = new HashMap<>(16);  // initial capacity
Map<String, Integer> withLoadFactor = new HashMap<>(16, 0.75f);  // capacity, load factor
```

---

## 2. All HashMap methods with examples and output

### 2.1 put, putIfAbsent, putAll

| Method | Description |
|--------|-------------|
| `V put(K key, V value)` | Associates key with value; returns previous value (or null) |
| `V putIfAbsent(K key, V value)` | Puts only if key is absent; returns existing value or null |
| `void putAll(Map<? extends K, ? extends V> m)` | Copies all mappings from m |

```java
Map<String, Integer> map = new HashMap<>();
Integer old1 = map.put("apple", 10);        // old1 = null, map = {apple=10}
Integer old2 = map.put("apple", 20);        // old2 = 10, map = {apple=20}
Integer old3 = map.putIfAbsent("banana", 30); // old3 = null, map = {apple=20, banana=30}
Integer old4 = map.putIfAbsent("apple", 25);  // old4 = 20 (unchanged), map = {apple=20, banana=30}
map.putAll(Map.of("mango", 40, "berry", 50)); // map = {apple=20, banana=30, mango=40, berry=50}
```

**Output:** `old1 = null`, `old2 = 10`, `old3 = null`, `old4 = 20`; final map: `{apple=20, banana=30, mango=40, berry=50}`

---

### 2.2 get, getOrDefault

| Method | Description |
|--------|-------------|
| `V get(Object key)` | Value for key, or null if absent |
| `V getOrDefault(Object key, V defaultValue)` | Value for key, or defaultValue if absent |

```java
Map<String, Integer> map = new HashMap<>(Map.of("apple", 10, "banana", 20));
Integer val1 = map.get("apple");              // 10
Integer val2 = map.get("mango");              // null
Integer val3 = map.getOrDefault("mango", 0);   // 0
Integer val4 = map.getOrDefault("apple", 0);   // 10
```

**Output:** `val1 = 10`, `val2 = null`, `val3 = 0`, `val4 = 10`

---

### 2.3 remove

| Method | Description |
|--------|-------------|
| `V remove(Object key)` | Removes mapping for key; returns value (or null) |
| `boolean remove(Object key, Object value)` | Removes only if key maps to value; returns true if removed |

```java
Map<String, Integer> map = new HashMap<>(Map.of("apple", 10, "banana", 20, "mango", 30));
Integer removed1 = map.remove("banana");              // removed1 = 20, map = {apple=10, mango=30}
boolean removed2 = map.remove("apple", 10);          // removed2 = true, map = {mango=30}
boolean removed3 = map.remove("mango", 50);          // removed3 = false (value mismatch)
Integer removed4 = map.remove("berry");               // removed4 = null
```

**Output:** `removed1 = 20`, `removed2 = true`, `removed3 = false`, `removed4 = null`; final map: `{mango=30}`

---

### 2.4 replace, replaceAll

| Method | Description |
|--------|-------------|
| `V replace(K key, V value)` | Replaces value for key if present; returns old value (or null) |
| `boolean replace(K key, V oldValue, V newValue)` | Replaces only if key maps to oldValue; returns true if replaced |
| `void replaceAll(BiFunction<? super K, ? super V, ? extends V> function)` | Replaces each value with function(key, value) |

```java
Map<String, Integer> map = new HashMap<>(Map.of("apple", 10, "banana", 20));
Integer old1 = map.replace("apple", 15);              // old1 = 10, map = {apple=15, banana=20}
boolean replaced = map.replace("banana", 20, 25);     // replaced = true, map = {apple=15, banana=25}
boolean notReplaced = map.replace("banana", 30, 35);  // notReplaced = false
map.replaceAll((k, v) -> v * 2);                      // map = {apple=30, banana=50}
```

**Output:** `old1 = 10`, `replaced = true`, `notReplaced = false`; after replaceAll: `{apple=30, banana=50}`

---

### 2.5 containsKey, containsValue

| Method | Description |
|--------|-------------|
| `boolean containsKey(Object key)` | true if map contains key |
| `boolean containsValue(Object value)` | true if map contains value |

```java
Map<String, Integer> map = new HashMap<>(Map.of("apple", 10, "banana", 20));
boolean hasKey = map.containsKey("apple");      // true
boolean hasValue = map.containsValue(20);        // true
boolean noKey = map.containsKey("mango");       // false
boolean noValue = map.containsValue(100);       // false
```

**Output:** `hasKey = true`, `hasValue = true`, `noKey = false`, `noValue = false`

---

### 2.6 size, isEmpty, clear

| Method | Description |
|--------|-------------|
| `int size()` | Number of key-value mappings |
| `boolean isEmpty()` | true if size is 0 |
| `void clear()` | Removes all mappings |

```java
Map<String, Integer> map = new HashMap<>(Map.of("a", 1, "b", 2));
int size = map.size();          // 2
boolean empty = map.isEmpty();  // false
map.clear();                    // map = {}
boolean emptyAfter = map.isEmpty(); // true
```

**Output:** `size = 2`, `empty = false`, after clear `emptyAfter = true`

---

### 2.7 keySet, values, entrySet

| Method | Description |
|--------|-------------|
| `Set<K> keySet()` | Set view of keys (changes reflect in map) |
| `Collection<V> values()` | Collection view of values (changes reflect in map) |
| `Set<Map.Entry<K, V>> entrySet()` | Set view of entries (changes reflect in map) |

```java
Map<String, Integer> map = new HashMap<>(Map.of("apple", 10, "banana", 20));
Set<String> keys = map.keySet();
Collection<Integer> values = map.values();
Set<Map.Entry<String, Integer>> entries = map.entrySet();
keys.remove("apple");
```

**Output:** Removing from `keySet` removes from map.

---

### 2.8 compute, computeIfAbsent, computeIfPresent

| Method | Description |
|--------|-------------|
| `V compute(K key, BiFunction<? super K, ? super V, ? extends V> remappingFunction)` | Computes new value; removes if function returns null |
| `V computeIfAbsent(K key, Function<? super K, ? extends V> mappingFunction)` | Computes value only if key is absent |
| `V computeIfPresent(K key, BiFunction<? super K, ? super V, ? extends V> remappingFunction)` | Computes value only if key is present |

```java
Map<String, Integer> map = new HashMap<>();
map.put("apple", 10);
Integer computed = map.compute("apple", (k, v) -> v + 5);
Integer computed2 = map.compute("banana", (k, v) -> 20);
map.compute("apple", (k, v) -> null);

map.put("apple", 10);
Integer absent = map.computeIfAbsent("mango", k -> 30);
Integer absent2 = map.computeIfAbsent("apple", k -> 50);

Integer present = map.computeIfPresent("apple", (k, v) -> v * 2);
Integer present2 = map.computeIfPresent("berry", (k, v) -> 100);
```

**Output:** Values as commented; map changes accordingly.

---

### 2.9 merge

| Method | Description |
|--------|-------------|
| `V merge(K key, V value, BiFunction<? super V, ? super V, ? extends V> remappingFunction)` | If key absent, puts value; else merges |

```java
Map<String, Integer> map = new HashMap<>();
map.put("apple", 10);
Integer merged1 = map.merge("apple", 5, Integer::sum);
Integer merged2 = map.merge("banana", 20, Integer::sum);
map.merge("apple", 10, (old, newVal) -> null);
```

**Output:** `merged1 = 15`, `merged2 = 20`; after null merge, apple is removed.

---

### 2.10 forEach (Java 8)

| Method | Description |
|--------|-------------|
| `void forEach(BiConsumer<? super K, ? super V> action)` | Performs action for each entry |

```java
Map<String, Integer> map = new HashMap<>(Map.of("apple", 10, "banana", 20));
map.forEach((k, v) -> System.out.println(k + " -> " + v));
// apple -> 10
// banana -> 20
```

---

### 2.11 Java 21: SequencedMap methods

`HashMap` implements **`SequencedMap`** in Java 21.

**Note:** `HashMap` does not maintain insertion order by default. Use **`LinkedHashMap`** for ordered behavior with these methods.

```java
LinkedHashMap<String, Integer> map = new LinkedHashMap<>(Map.of("a", 1, "b", 2, "c", 3));
SequencedMap<String, Integer> reversed = map.reversed();
Map.Entry<String, Integer> first = map.firstEntry();
Map.Entry<String, Integer> last = map.lastEntry();
```

---

## 3. Transformations

### 3.1 Transform values (e.g., multiply all values by 2)

```java
Map<String, Integer> map = new HashMap<>(Map.of("apple", 10, "banana", 20));
map.replaceAll((k, v) -> v * 2);
Map<String, Integer> doubled = map.entrySet().stream()
        .collect(Collectors.toMap(Map.Entry::getKey, e -> e.getValue() * 2));
```

**Output:** `{apple=20, banana=40}`

---

### 3.2 Transform keys

```java
Map<String, Integer> map = new HashMap<>(Map.of("apple", 10, "banana", 20));
Map<String, Integer> upperKeys = map.entrySet().stream()
        .collect(Collectors.toMap(e -> e.getKey().toUpperCase(), Map.Entry::getValue));
// {APPLE=10, BANANA=20}
```

---

### 3.3 Filter entries

```java
Map<String, Integer> map = new HashMap<>(Map.of("apple", 10, "banana", 20, "mango", 5));
Map<String, Integer> filtered = map.entrySet().stream()
        .filter(e -> e.getValue() >= 10)
        .collect(Collectors.toMap(Map.Entry::getKey, Map.Entry::getValue));
// {apple=10, banana=20}
```

---

## 4. Insertion operations

### 4.1 Basic insertion

```java
Map<String, Integer> map = new HashMap<>();
map.put("apple", 10);
map.put("banana", 20);
map.put("apple", 15);
```

---

### 4.2 Insert only if absent

```java
Map<String, Integer> map = new HashMap<>();
map.putIfAbsent("apple", 10);
map.putIfAbsent("apple", 20);
```

---

### 4.3 Insert with computeIfAbsent

```java
Map<String, List<String>> map = new HashMap<>();
map.computeIfAbsent("fruits", k -> new ArrayList<>()).add("apple");
map.computeIfAbsent("fruits", k -> new ArrayList<>()).add("banana");
// {fruits=[apple, banana]}
```

---

### 4.4 Insert all from another map

```java
Map<String, Integer> map1 = new HashMap<>(Map.of("apple", 10));
Map<String, Integer> map2 = Map.of("banana", 20, "mango", 30);
map1.putAll(map2);
```

---

## 5. Deletion operations

### 5.1 Remove by key

```java
Map<String, Integer> map = new HashMap<>(Map.of("apple", 10, "banana", 20));
map.remove("apple");
```

---

### 5.2 Remove by key-value pair

```java
Map<String, Integer> map = new HashMap<>(Map.of("apple", 10, "banana", 20));
map.remove("apple", 10);
map.remove("banana", 30);
```

---

### 5.3 Remove entries matching condition

```java
Map<String, Integer> map = new HashMap<>(Map.of("apple", 10, "banana", 20, "mango", 5));
map.entrySet().removeIf(e -> e.getValue() < 10);
```

---

### 5.4 Clear all

```java
map.clear();
```

---

## 6. Replace operations

### 6.1 Replace value for key

```java
Map<String, Integer> map = new HashMap<>(Map.of("apple", 10));
map.replace("apple", 20);
map.replace("banana", 30);
```

---

### 6.2 Replace if value matches

```java
Map<String, Integer> map = new HashMap<>(Map.of("apple", 10));
map.replace("apple", 10, 20);
map.replace("apple", 10, 30);
```

---

### 6.3 Replace all values

```java
Map<String, Integer> map = new HashMap<>(Map.of("apple", 10, "banana", 20));
map.replaceAll((k, v) -> v * 2);
```

---

## 7. Map to List conversions

### 7.1 Keys to List

```java
Map<String, Integer> map = new HashMap<>(Map.of("apple", 10, "banana", 20));
List<String> keys = new ArrayList<>(map.keySet());
```

---

### 7.2 Values to List

```java
List<Integer> values = new ArrayList<>(map.values());
```

---

### 7.3 Entries to List

```java
List<Map.Entry<String, Integer>> entries = new ArrayList<>(map.entrySet());
```

---

### 7.4 Stream: keys to List

```java
List<String> keys = map.keySet().stream().collect(Collectors.toList());
List<String> sortedKeys = map.keySet().stream().sorted().collect(Collectors.toList());
```

---

### 7.5 Stream: values to List

```java
List<Integer> values = map.values().stream().collect(Collectors.toList());
List<Integer> sortedValues = map.values().stream().sorted().collect(Collectors.toList());
```

---

### 7.6 Stream: entries to List of custom objects

```java
List<String> keyValuePairs = map.entrySet().stream()
        .map(e -> e.getKey() + "=" + e.getValue())
        .collect(Collectors.toList());
```

---

### 7.7 Map to List of keys sorted by values

```java
Map<String, Integer> map = new HashMap<>(Map.of("apple", 30, "banana", 10, "mango", 20));
List<String> keysByValue = map.entrySet().stream()
        .sorted(Map.Entry.comparingByValue())
        .map(Map.Entry::getKey)
        .collect(Collectors.toList());
```

---

## 8. List to Map conversions

### 8.1 List to Map (element as key, index as value)

```java
List<String> list = List.of("apple", "banana", "mango");
Map<String, Integer> map = IntStream.range(0, list.size())
        .boxed()
        .collect(Collectors.toMap(list::get, i -> i));
```

---

### 8.2 List to Map (element as key, transformed value)

```java
List<String> list = List.of("apple", "banana", "mango");
Map<String, Integer> map = list.stream()
        .collect(Collectors.toMap(Function.identity(), String::length));
```

---

### 8.3 List to Map with duplicate keys (merge)

```java
List<String> list = List.of("apple", "banana", "apple", "mango");
Map<String, Long> count = list.stream()
        .collect(Collectors.toMap(Function.identity(), v -> 1L, Long::sum));
```

---

## 9. Java 8 Stream operations with Map

### 9.1 Filter entries

```java
Map<String, Integer> map = new HashMap<>(Map.of("apple", 10, "banana", 20, "mango", 5));
Map<String, Integer> filtered = map.entrySet().stream()
        .filter(e -> e.getValue() >= 10)
        .collect(Collectors.toMap(Map.Entry::getKey, Map.Entry::getValue));
```

---

### 9.2 Map entries to different type

```java
Map<String, Integer> map = new HashMap<>(Map.of("apple", 10, "banana", 20));
Map<String, String> stringValues = map.entrySet().stream()
        .collect(Collectors.toMap(Map.Entry::getKey, e -> String.valueOf(e.getValue())));
```

---

### 9.3 Sort by key

```java
Map<String, Integer> sortedByKey = map.entrySet().stream()
        .sorted(Map.Entry.comparingByKey())
        .collect(Collectors.toMap(Map.Entry::getKey, Map.Entry::getValue,
                (e1, e2) -> e1, LinkedHashMap::new));
```

---

### 9.4 Sort by value

```java
Map<String, Integer> sortedByValue = map.entrySet().stream()
        .sorted(Map.Entry.comparingByValue())
        .collect(Collectors.toMap(Map.Entry::getKey, Map.Entry::getValue,
                (e1, e2) -> e1, LinkedHashMap::new));
```

---

### 9.5 Group by value

```java
Map<String, Integer> map = new HashMap<>(Map.of("apple", 10, "banana", 20, "mango", 10));
Map<Integer, List<String>> grouped = map.entrySet().stream()
        .collect(Collectors.groupingBy(Map.Entry::getValue,
                Collectors.mapping(Map.Entry::getKey, Collectors.toList())));
```

---

## 10. Coding interview questions

### 10.1 Count frequency of characters in string

```java
String s = "hello";
Map<Character, Long> freq = s.chars()
        .mapToObj(c -> (char) c)
        .collect(Collectors.groupingBy(Function.identity(), Collectors.counting()));
```

---

### 10.2 Find first non-repeated character

```java
String s = "hello";
Optional<Character> first = s.chars()
        .mapToObj(c -> (char) c)
        .collect(Collectors.groupingBy(Function.identity(), Collectors.counting()))
        .entrySet().stream()
        .filter(e -> e.getValue() == 1)
        .map(Map.Entry::getKey)
        .findFirst();
```

---

### 10.3 Two Sum (indices)

```java
int[] nums = {2, 7, 11, 15};
int target = 9;
Map<Integer, Integer> map = new HashMap<>();
for (int i = 0; i < nums.length; i++) {
    int complement = target - nums[i];
    if (map.containsKey(complement)) {
        // return new int[]{map.get(complement), i};
    }
    map.put(nums[i], i);
}
```

---

### 10.4 Group anagrams

```java
List<String> words = List.of("eat", "tea", "tan", "ate", "nat", "bat");
Map<String, List<String>> anagrams = words.stream()
        .collect(Collectors.groupingBy(word -> {
            char[] chars = word.toCharArray();
            Arrays.sort(chars);
            return new String(chars);
        }));
```

---

### 10.5 Merge two maps (sum values for same keys)

```java
Map<String, Integer> map1 = Map.of("a", 1, "b", 2);
Map<String, Integer> map2 = Map.of("b", 3, "c", 4);
Map<String, Integer> merged = Stream.concat(map1.entrySet().stream(), map2.entrySet().stream())
        .collect(Collectors.toMap(Map.Entry::getKey, Map.Entry::getValue, Integer::sum));
```

---

### 10.6 Find duplicate elements

```java
List<String> list = List.of("a", "b", "a", "c", "b");
Set<String> duplicates = list.stream()
        .collect(Collectors.groupingBy(Function.identity(), Collectors.counting()))
        .entrySet().stream()
        .filter(e -> e.getValue() > 1)
        .map(Map.Entry::getKey)
        .collect(Collectors.toSet());
```

---

### 10.7 Sort map by value (descending)

```java
Map<String, Integer> map = new HashMap<>(Map.of("apple", 30, "banana", 10, "mango", 20));
Map<String, Integer> sorted = map.entrySet().stream()
        .sorted(Map.Entry.<String, Integer>comparingByValue().reversed())
        .collect(Collectors.toMap(Map.Entry::getKey, Map.Entry::getValue,
                (e1, e2) -> e1, LinkedHashMap::new));
```

---

### 10.8 Invert map (swap keys and values)

```java
Map<String, Integer> map = new HashMap<>(Map.of("apple", 10, "banana", 20));
Map<Integer, String> inverted = map.entrySet().stream()
        .collect(Collectors.toMap(Map.Entry::getValue, Map.Entry::getKey));
```

---

### 10.9 Find key with maximum value

```java
Map<String, Integer> map = new HashMap<>(Map.of("apple", 30, "banana", 10, "mango", 20));
Optional<String> maxKey = map.entrySet().stream()
        .max(Map.Entry.comparingByValue())
        .map(Map.Entry::getKey);
```

---

### 10.10 Check if two maps are equal (ignoring order)

```java
Map<String, Integer> map1 = new HashMap<>(Map.of("a", 1, "b", 2));
Map<String, Integer> map2 = new HashMap<>(Map.of("b", 2, "a", 1));
boolean equal = map1.equals(map2);  // true
```

---

## 11. Quick reference table

| Operation | Method / Code |
|-----------|---------------|
| Insert | `map.put(key, value)` |
| Insert if absent | `map.putIfAbsent(key, value)` |
| Get | `map.get(key)` or `map.getOrDefault(key, defaultValue)` |
| Remove | `map.remove(key)` or `map.remove(key, value)` |
| Replace | `map.replace(key, value)` or `map.replace(key, oldValue, newValue)` |
| Replace all | `map.replaceAll((k, v) -> newValue)` |
| Contains | `map.containsKey(key)`, `map.containsValue(value)` |
| Transform values | `map.replaceAll((k, v) -> transform(v))` or stream |
| Filter entries | `map.entrySet().stream().filter(...).collect(...)` |
| Sort by key | `entrySet().stream().sorted(Map.Entry.comparingByKey())` |
| Sort by value | `entrySet().stream().sorted(Map.Entry.comparingByValue())` |
| Map → List (keys) | `new ArrayList<>(map.keySet())` |
| Map → List (values) | `new ArrayList<>(map.values())` |
| Map → List (entries) | `new ArrayList<>(map.entrySet())` |
| List → Map | `list.stream().collect(Collectors.toMap(...))` |
| Group by value | `entrySet().stream().collect(Collectors.groupingBy(...))` |

---

All examples use **Java 8** streams and collectors; Java 21 **SequencedMap** methods are noted where applicable.
