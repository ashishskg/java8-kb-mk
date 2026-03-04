# Custom ArrayList — Implementation Cheat Sheet

## What you’re building

An array-backed, resizable, index-based list.

- **Storage**: `Object[] elementData`
- **Size** (logical): `int size`
- **Capacity** (physical): `elementData.length`

## Core invariants

- Valid element indices: `0 <= index < size`
- Valid add indices: `0 <= index <= size`
- Always null out freed slots (`elementData[size] = null`) to help GC.

## Complexity quick table

| Operation | Time |
|---|---|
| `get(i)` / `set(i,x)` | O(1) |
| `add(x)` (append) | Amortized O(1) |
| `add(i,x)` | O(n) (shift right) |
| `remove(i)` | O(n) (shift left) |
| `contains(x)` / `indexOf(x)` | O(n) |

## Resizing strategy (ensureCapacity)

```java
private void ensureCapacity(int minCapacity) {
    if (minCapacity > elementData.length) {
        int newCap = Math.max(elementData.length * 2, minCapacity);
        elementData = Arrays.copyOf(elementData, newCap);
    }
}
```

- Doubling gives amortized O(1) append.

## Bounds checks

```java
private void rangeCheck(int index) {
    if (index < 0 || index >= size) {
        throw new IndexOutOfBoundsException("Index: " + index + ", Size: " + size);
    }
}

private void rangeCheckForAdd(int index) {
    if (index < 0 || index > size) {
        throw new IndexOutOfBoundsException("Index: " + index + ", Size: " + size);
    }
}
```

## get / set

```java
@SuppressWarnings("unchecked")
public E get(int index) {
    rangeCheck(index);
    return (E) elementData[index];
}

@SuppressWarnings("unchecked")
public E set(int index, E e) {
    rangeCheck(index);
    E old = (E) elementData[index];
    elementData[index] = e;
    return old;
}
```

## add (append)

```java
public boolean add(E e) {
    ensureCapacity(size + 1);
    elementData[size++] = e;
    return true;
}
```

## add (insert)

```java
public void add(int index, E e) {
    rangeCheckForAdd(index);
    ensureCapacity(size + 1);
    System.arraycopy(elementData, index, elementData, index + 1, size - index);
    elementData[index] = e;
    size++;
}
```

## remove (by index)

```java
@SuppressWarnings("unchecked")
public E remove(int index) {
    rangeCheck(index);

    E old = (E) elementData[index];
    int numMoved = size - index - 1;

    if (numMoved > 0) {
        System.arraycopy(elementData, index + 1, elementData, index, numMoved);
    }

    elementData[--size] = null;
    return old;
}
```

## remove (by value)

```java
public boolean remove(Object o) {
    int idx = indexOf(o);
    if (idx >= 0) {
        remove(idx);
        return true;
    }
    return false;
}
```

## indexOf / lastIndexOf (handle null)

```java
public int indexOf(Object o) {
    if (o == null) {
        for (int i = 0; i < size; i++) if (elementData[i] == null) return i;
    } else {
        for (int i = 0; i < size; i++) if (o.equals(elementData[i])) return i;
    }
    return -1;
}

public int lastIndexOf(Object o) {
    if (o == null) {
        for (int i = size - 1; i >= 0; i--) if (elementData[i] == null) return i;
    } else {
        for (int i = size - 1; i >= 0; i--) if (o.equals(elementData[i])) return i;
    }
    return -1;
}
```

## Iterator (minimal)

- Track `cursor` and `lastRet`.
- `next()` returns `elementData[cursor++]`.
- `remove()` removes `lastRet` and adjusts `cursor`.

## Common pitfalls

- **Forgetting to grow capacity** before writes.
- **Confusing size vs capacity**.
- **Not nulling removed elements** (memory leak).
- **Broken index checks** (`index == size` is allowed only for add).

