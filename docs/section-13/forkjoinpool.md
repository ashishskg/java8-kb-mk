# ForkJoinPool

## 1. Concept explanation
`ForkJoinPool` is a work-stealing pool optimized for many small CPU-bound tasks (used by parallel streams).

## 2. Problem statement
Run a small recursive task and get deterministic result.

## 3. Algorithm intuition
Split work into subtasks (fork) and combine results (join).

## 4. Java 8 implementation
```java
import java.util.concurrent.*;

public class ForkJoinDemo {
    static class SumTask extends RecursiveTask<Integer> {
        final int lo, hi;
        SumTask(int lo, int hi) { this.lo = lo; this.hi = hi; }
        protected Integer compute() {
            if (hi - lo <= 2) {
                int s = 0;
                for (int i = lo; i <= hi; i++) s += i;
                return s;
            }
            int mid = (lo + hi) / 2;
            SumTask left = new SumTask(lo, mid);
            SumTask right = new SumTask(mid + 1, hi);
            left.fork();
            int r = right.compute();
            return left.join() + r;
        }
    }

    public static void main(String[] args) {
        ForkJoinPool p = new ForkJoinPool(2);
        int sum = p.invoke(new SumTask(1, 5));
        System.out.println(sum);
        p.shutdown();
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
- Input: sum range 1..5

## 7. Execution steps
- Split task
- Fork/join
- Combine sums

## 8. Output
- Output: 15

## 9. Time and space complexity
- Work: O(n)
- Span: O(log n) splits

## 10. Enterprise relevance
ForkJoin excels for CPU-bound divide-and-conquer; avoid for IO-bound tasks.

## 11. Interview discussion points
- Work stealing
- RecursiveTask vs RecursiveAction
- Common pool

## 12. Best practices
- Keep tasks small but not tiny
- Avoid blocking inside FJ threads
- Prefer explicit pools in servers
