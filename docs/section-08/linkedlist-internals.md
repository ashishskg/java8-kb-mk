# LinkedList Internals

## 1. Concept explanation
`LinkedList` is a doubly-linked list. Each node stores prev/next pointers and the item.

Costs:
- get(i): O(n) traversal
- add/remove at ends: O(1)
- high memory overhead due to node objects

## 2. Problem statement
Understand why LinkedList is rarely faster than ArrayList in real services.

## 3. Algorithm intuition
Pointer chasing defeats CPU cache locality; only use when you truly need deque semantics and can’t use ArrayDeque.

## 4. Java 8 implementation
```java
import java.util.*;

public class LinkedListDemo {
    public static void main(String[] args) {
        Deque<Integer> dq = new LinkedList<>();
        dq.addFirst(2);
        dq.addFirst(1);
        dq.addLast(3);
        System.out.println(dq.removeFirst());
        System.out.println(dq);
    }
}
```

## 5. Stream API implementation
```java
import java.util.*;
import java.util.stream.*;

public class Example {
    public static void main(String[] args) {
        List<Integer> xs = Arrays.asList(1, 2, 3, 4, 5);
        int sumOfEvens = xs.stream().filter(x -> x % 2 == 0).mapToInt(x -> x).sum();
        System.out.println(sumOfEvens);
    }
}
```

## 6. Sample input
- Input: addFirst(2), addFirst(1), addLast(3)

## 7. Execution steps
- Use as Deque
- Remove from front
- Inspect remaining

## 8. Output
- Output: 1
- Output: [2, 3]

## 9. Time and space complexity
- addFirst/addLast/removeFirst: O(1)
- get(i): O(n)

## 10. Enterprise relevance
Prefer ArrayDeque for queues/stacks. LinkedList adds allocation overhead and GC pressure.

## 11. Interview discussion points
- Why get(i) is O(n)
- Memory overhead
- LinkedList vs ArrayDeque

## 12. Best practices
- Use Deque interface
- Prefer ArrayDeque
- Avoid LinkedList for random access
