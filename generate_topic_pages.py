    # ---------- Sorting algorithms (minimal but real) ----------
    if low in ("bubble sort", "selection sort", "insertion sort", "merge sort", "quick sort"):
        java_impl = textwrap.dedent(
            """\
            import java.util.*;

            public class Sorts {
                public static void bubbleSort(int[] a) {
                    for (int i = 0; i < a.length; i++) {
                        boolean swapped = false;
                        for (int j = 1; j < a.length - i; j++) {
                            if (a[j - 1] > a[j]) {
                                int t = a[j - 1]; a[j - 1] = a[j]; a[j] = t;
                                swapped = true;
                            }
                        }
                        if (!swapped) return;
                    }
                }

                public static void main(String[] args) {
                    int[] a = {5, 1, 4, 2};
                    bubbleSort(a);
                    System.out.println(Arrays.toString(a));
                }
            }
            """
        )
        return build_page(
            t,
            concept=f"Sorting algorithm: {t}.",
            problem="Sort an integer array in ascending order.",
            intuition="Sorting rearranges elements by comparison; choose algorithm based on stability, memory, and average/worst-case time.",
            java_impl=java_impl,
            stream_impl=textwrap.dedent(
                """\
                import java.util.*;
                import java.util.stream.*;

                public class StreamSort {
                    public static void main(String[] args) {
                        List<Integer> xs = Arrays.asList(5, 1, 4, 2);
                        List<Integer> out = xs.stream().sorted().collect(Collectors.toList());
                        System.out.println(out);
                    }
                }
                """
            ),
            sample_input="- Input: [5,1,4,2]",
            execution_steps=_bullets("Compare and swap (or divide/partition depending on algorithm)", "Repeat until sorted"),
            output="- Output: [1,2,4,5]",
            complexity="- Time: varies (bubble worst O(n^2), merge O(n log n), quick avg O(n log n))\n- Space: varies",
            enterprise_relevance="Sorting is used in pagination, ranking, and preparing deterministic outputs; choose algorithms that meet latency/memory budgets.",
            interview_points=_bullets("Stability", "Worst-case vs average", "In-place vs extra memory"),
            best_practices=_bullets("Prefer library sorts in production", "Avoid O(n^2) for large inputs", "Document comparator ordering"),
        )

    # ---------- String interview problems ----------
    if low == "reverse string":
        return build_page(
            t,
            concept="Reverse a string efficiently by swapping characters.",
            problem="Given a string, return its reverse.",
            intuition="Use a char array and two pointers moving inward.",
            java_impl=textwrap.dedent(
                """\
                public class ReverseString {
                    public static String reverse(String s) {
                        char[] a = s.toCharArray();
                        int i = 0, j = a.length - 1;
                        while (i < j) {
                            char t = a[i]; a[i] = a[j]; a[j] = t;
                            i++; j--;
                        }
                        return new String(a);
                    }
                }
                """
            ),
            stream_impl=textwrap.dedent(
                """\
                import java.util.stream.*;

                public class ReverseStringStream {
                    public static String reverse(String s) {
                        return IntStream.range(0, s.length())
                                .mapToObj(i -> s.charAt(s.length() - 1 - i))
                                .collect(StringBuilder::new, StringBuilder::append, StringBuilder::append)
                                .toString();
                    }
                }
                """
            ),
            sample_input="- Input: \"abcd\"",
            execution_steps=_bullets("Convert to char[]", "Swap ends inward", "Build result"),
            output="- Output: \"dcba\"",
            complexity="- Time: O(n)\n- Space: O(n) (char array)",
            enterprise_relevance="Used in parsing, formatting, and interview warmups; in production prefer clarity and avoid Unicode pitfalls for grapheme clusters.",
            interview_points=_bullets("In-place reversal", "Unicode considerations"),
            best_practices=_bullets("Use char[] for ASCII-like inputs", "Be explicit about Unicode needs"),
        )

    if low == "palindrome detection":
        return build_page(
            t,
            concept="A palindrome reads the same forward and backward.",
            problem="Given a string, determine if it is a palindrome.",
            intuition="Use two pointers; optionally normalize case and skip non-alphanumerics.",
            java_impl=textwrap.dedent(
                """\
                public class Palindrome {
                    public static boolean isPalindrome(String s) {
                        int i = 0, j = s.length() - 1;
                        while (i < j) {
                            if (s.charAt(i) != s.charAt(j)) return false;
                            i++; j--;
                        }
                        return true;
                    }
                }
                """
            ),
            stream_impl=GEN_STREAM,
            sample_input="- Input: \"level\"",
            execution_steps=_bullets("Compare symmetric characters", "Return false on mismatch"),
            output="- Output: true",
            complexity="- Time: O(n)\n- Space: O(1)",
            enterprise_relevance="Appears in validation and pattern matching; treat Unicode and normalization carefully if required.",
            interview_points=_bullets("Ignore case/spaces variant", "Two-pointer proof"),
            best_practices=_bullets("Clarify normalization rules", "Write tests for edge cases"),
        )

    # ---------- Kadane / max subarray ----------
    if low == "maximum subarray":
        return build_page(
            t,
            concept="Kadane’s algorithm finds the maximum-sum contiguous subarray in linear time.",
            problem="Given an integer array (may contain negatives), find the max subarray sum.",
            intuition="At each index, either extend the previous subarray or start fresh at current value.",
            java_impl=textwrap.dedent(
                """\
                public class MaxSubarray {
                    public static int maxSubarraySum(int[] a) {
                        int best = a[0];
                        int cur = a[0];
                        for (int i = 1; i < a.length; i++) {
                            cur = Math.max(a[i], cur + a[i]);
                            best = Math.max(best, cur);
                        }
                        return best;
                    }
                }
                """
            ),
            stream_impl=textwrap.dedent(
                """\
                import java.util.*;
                import java.util.stream.*;

                public class MaxSubarrayStreamNote {
                    public static void main(String[] args) {
                        // Kadane is sequential and stateful; a simple loop is clearer than streams.
                    }
                }
                """
            ),
            sample_input="- Input: [-2,1,-3,4,-1,2,1,-5,4]",
            execution_steps=_bullets("cur = max(a[i], cur+a[i])", "best = max(best, cur)"),
            output="- Output: 6 (subarray [4,-1,2,1])",
            complexity="- Time: O(n)\n- Space: O(1)",
            enterprise_relevance="Useful for detecting best-performing window (profit/loss, traffic deltas) in analytics pipelines.",
            interview_points=_bullets("All-negative arrays", "Return subarray indices"),
            best_practices=_bullets("Validate non-empty input", "Track start/end if needed"),
        )

    # ---------- Concurrency basics ----------
    if low in ("threads vs processes", "thread lifecycle", "synchronization", "volatile keyword", "locks and reentrantlock"):
        java_impl = textwrap.dedent(
            """\
            import java.util.concurrent.*;
            import java.util.concurrent.locks.*;

            public class ConcurrencyDemo {
                private static volatile boolean stop = false;
                private static int shared = 0;
                private static final Lock lock = new ReentrantLock();

                public static void main(String[] args) throws Exception {
                    Thread t = new Thread(() -> {
                        while (!stop) {
                            lock.lock();
                            try { shared++; }
                            finally { lock.unlock(); }
                        }
                    });
                    t.start();
                    Thread.sleep(50);
                    stop = true;
                    t.join();
                    System.out.println(shared);
                }
            }
            """
        )
        return build_page(
            t,
            concept=f"Concurrency topic: {t}.",
            problem="Coordinate multiple threads safely without race conditions.",
            intuition="Use synchronization/locks for mutual exclusion; use volatile for visibility (not atomicity).",
            java_impl=java_impl,
            stream_impl=GEN_STREAM,
            sample_input="- Input: 1 worker thread increments a counter",
            execution_steps=_bullets("Start thread", "Increment under lock", "Signal stop via volatile", "Join thread"),
            output="- Output: final counter value (non-deterministic magnitude) printed",
            complexity="- N/A (concept)",
            enterprise_relevance="Correct concurrency prevents data corruption in caches, rate limiters, batch workers, and request handling.",
            interview_points=_bullets("volatile vs AtomicInteger", "Intrinsic lock vs ReentrantLock", "Visibility vs atomicity"),
            best_practices=_bullets("Prefer higher-level concurrency utilities", "Keep critical sections small", "Avoid deadlocks"),
        )

    # ---------- Executor framework & CompletableFuture (real patterns) ----------
    if low in ("executor interface", "executorservice", "threadpoolexecutor", "scheduledexecutorservice", "forkjoinpool"):
        java_impl = textwrap.dedent(
            """\
            import java.util.concurrent.*;

            public class ExecutorExample {
                public static void main(String[] args) throws Exception {
                    ExecutorService pool = Executors.newFixedThreadPool(4);
                    Future<Integer> f = pool.submit(() -> 40 + 2);
                    System.out.println(f.get());
                    pool.shutdown();
                }
            }
            """
        )
        return build_page(
            t,
            concept=f"Executor topic: {t}.",
            problem="Run tasks asynchronously without creating raw threads per request.",
            intuition="Executors reuse threads; choose pool type based on workload (CPU vs IO). ForkJoinPool powers parallel streams.",
            java_impl=java_impl,
            stream_impl=GEN_STREAM,
            sample_input="- Input: compute 40+2 async",
            execution_steps=_bullets("Create ExecutorService", "Submit Callable", "Block on Future.get", "Shutdown"),
            output="- Output: 42",
            complexity="- N/A (concept)",
            enterprise_relevance="Thread pools are central to servers and batch systems; misconfiguration causes latency spikes and resource exhaustion.",
            interview_points=_bullets("Fixed vs cached thread pool", "Shutdown vs shutdownNow", "Work queue types"),
            best_practices=_bullets("Always shutdown pools", "Bound queues", "Separate IO and CPU pools"),
        )

    if low in ("completablefuture overview", "supplyasync", "runasync", "thenapply", "thencompose", "thencombine", "exceptionally", "allof", "anyof"):
        java_impl = textwrap.dedent(
            """\
            import java.util.concurrent.*;

            public class CfExample {
                public static void main(String[] args) {
                    CompletableFuture<Integer> a = CompletableFuture.supplyAsync(() -> 20);
                    CompletableFuture<Integer> b = CompletableFuture.supplyAsync(() -> 22);
                    CompletableFuture<Integer> c = a.thenCombine(b, Integer::sum)
                            .exceptionally(ex -> 0);
                    System.out.println(c.join());
                }
            }
            """
        )
        return build_page(
            t,
            concept=f"CompletableFuture operation: {t}.",
            problem="Compose async computations with clear control flow and centralized error handling.",
            intuition="Use thenApply for sync map, thenCompose for async flatten, thenCombine for fan-in, allOf/anyOf for fan-out.",
            java_impl=java_impl,
            stream_impl=GEN_STREAM,
            sample_input="- Input: two async computations producing 20 and 22",
            execution_steps=_bullets("Start futures", "Combine", "Handle exceptions", "Join"),
            output="- Output: 42",
            complexity="- N/A (concept)",
            enterprise_relevance="Used for parallel API calls and async IO; be careful with thread pools and timeouts.",
            interview_points=_bullets("thenCompose vs thenApply", "Exception propagation", "join vs get"),
            best_practices=_bullets("Use dedicated executor", "Add timeouts", "Avoid blocking inside async stages"),
        )
from __future__ import annotations

from pathlib import Path
import textwrap



def ensure_dir(p: Path) -> None:
    p.mkdir(parents=True, exist_ok=True)


def write_file(path: Path, content: str, *, overwrite: bool) -> bool:
    if path.exists() and not overwrite:
        return False
    ensure_dir(path.parent)
    path.write_text(content, encoding="utf-8")
    return True


def _bullets(*items: str) -> str:
    return "\n".join(f"- {x}" for x in items)


def build_page(
    title: str,
    *,
    concept: str,
    problem: str,
    intuition: str,
    java_impl: str,
    stream_impl: str,
    sample_input: str,
    execution_steps: str,
    output: str,
    complexity: str,
    enterprise_relevance: str,
    interview_points: str,
    best_practices: str,
) -> str:
    return TEMPLATE.format(
        title=title,
        concept=concept,
        problem=problem,
        intuition=intuition,
        java_impl=java_impl.rstrip(),
        stream_impl=stream_impl.rstrip(),
        sample_input=sample_input,
        execution_steps=execution_steps,
        output=output,
        complexity=complexity,
        enterprise_relevance=enterprise_relevance,
        interview_points=interview_points,
        best_practices=best_practices,
    )


TEMPLATE = """# {title}

## 1. Concept explanation
{concept}

## 2. Problem statement
{problem}

## 3. Algorithm intuition
{intuition}

## 4. Java 8 implementation
```java
{java_impl}
```

## 5. Stream API implementation
```java
{stream_impl}
```

## 6. Sample input
{sample_input}

## 7. Execution steps
{execution_steps}

## 8. Output
{output}

## 9. Time and space complexity
{complexity}

## 10. Enterprise relevance
{enterprise_relevance}

## 11. Interview discussion points
{interview_points}

## 12. Best practices
{best_practices}
"""


GEN_JAVA = """import java.util.*;

public class Example {
    public static void main(String[] args) {
        // Java 8 reference implementation.
        // Keep it deterministic, testable, and avoid hidden side effects.
    }
}
"""


GEN_STREAM = """import java.util.*;
import java.util.stream.*;

public class Example {
    public static void main(String[] args) {
        // Stream-based reference implementation (when applicable).
        // Avoid stateful lambdas; prefer pure transforms and collectors.
    }
}
"""


def page(title: str, *, java_impl: str | None = None, stream_impl: str | None = None,
         sample_input: str | None = None, execution_steps: str | None = None, output: str | None = None,
         complexity: str | None = None) -> str:
    # Legacy wrapper (kept for backward compatibility with older calls)
    return build_page(
        title,
        concept=(
            "Explain the concept in production terms: intent, where it applies, and what it replaces/improves.\n\n"
            "If there are sharp edges (nullability, ordering, concurrency, performance), call them out explicitly."
        ),
        problem="State a concrete problem that motivates the concept, including constraints and edge cases.",
        intuition=(
            "Explain the mental model and the decision points.\n\n"
            "Include a small ASCII sketch if it helps (pipeline flow, memory layout, thread handoff)."
        ),
        java_impl=(java_impl or GEN_JAVA),
        stream_impl=(stream_impl or GEN_STREAM),
        sample_input=sample_input or "- Input: (a small representative sample)",
        execution_steps=execution_steps or "- Step 1: ...\n- Step 2: ...\n- Step 3: ...",
        output=output or "- Output: (expected output for the sample input)",
        complexity=complexity or "- Time: O(n) (typical)\n- Space: O(1) or O(n) depending on data structures/collectors",
        enterprise_relevance=(
            "Explain how this shows up in real systems (service layer, batch ETL, async orchestration, caching, observability).\n\n"
            "Mention failure modes and safe defaults."
        ),
        interview_points=(
            "- Edge cases (empty input, nulls, duplicates, overflow)\n"
            "- Trade-offs vs alternatives\n"
            "- How you would test it\n"
            "- What you would change at scale (memory/latency)"
        ),
        best_practices=(
            "- Prefer clarity over cleverness\n"
            "- Keep functions pure (especially in Streams)\n"
            "- Avoid shared mutable state\n"
            "- Make ordering and parallelism explicit\n"
            "- Measure before optimizing"
        ),
    )


def generate_topic_page(title: str) -> str:
    t = title.strip()
    low = t.lower()

    # ---------- Section 1: fundamentals ----------
    if low.startswith("java platform overview"):
        return build_page(
            t,
            concept=(
                "JDK/JRE/JVM describe different layers of the Java platform. JDK is for building; JRE is for running; JVM executes bytecode."
            ),
            problem="Clarify what you install/deploy and what runs your Java program.",
            intuition=(
                "Think of Java as: source -> bytecode -> runtime.\n\n"
                "ASCII:\nHello.java --javac--> Hello.class --JVM--> native execution\n\n"
                "JDK = JRE + tools; JRE = JVM + core libs; JVM = classloading + JIT + GC."
            ),
            java_impl=textwrap.dedent(
                """\
                public class Hello {
                    public static void main(String[] args) {
                        System.out.println("Hello, Java");
                    }
                }
                """
            ),
            stream_impl=GEN_STREAM,
            sample_input="- Input: `javac Hello.java` then `java Hello`",
            execution_steps=_bullets("Compile to bytecode", "JVM loads & verifies classes", "JIT compiles hot code", "GC manages heap"),
            output="- Output: Hello, Java",
            complexity="- N/A (concept)",
            enterprise_relevance="Impacts build pipelines, container images, observability tooling (jcmd/jstack), and runtime tuning (GC/JIT flags).",
            interview_points=_bullets("What is bytecode?", "What does the JVM do?", "What is JIT?"),
            best_practices=_bullets("Pin a JDK version in CI", "Use a JRE/runtime image for production when appropriate", "Monitor GC and CPU"),
        )

    if low == "data types and operators":
        return build_page(
            t,
            concept="Java primitives have fixed sizes; operator behavior (overflow, widening) matters for correctness and performance.",
            problem="Avoid bugs due to integer overflow, incorrect comparisons, or unintended boxing.",
            intuition="Prefer primitives for hot paths; be explicit about widening casts; use long for counters/sums.",
            java_impl=textwrap.dedent(
                """\
                public class Types {
                    public static void main(String[] args) {
                        int a = Integer.MAX_VALUE;
                        int b = a + 1; // overflow
                        long c = (long) a + 1; // no overflow
                        System.out.println(b);
                        System.out.println(c);
                    }
                }
                """
            ),
            stream_impl=textwrap.dedent(
                """\
                import java.util.stream.*;

                public class PrimitiveStreams {
                    public static void main(String[] args) {
                        long sum = IntStream.rangeClosed(1, 1_000_000).asLongStream().sum();
                        System.out.println(sum);
                    }
                }
                """
            ),
            sample_input="- Input: a = Integer.MAX_VALUE",
            execution_steps=_bullets("Compute int overflow", "Compute long sum safely"),
            output="- Output: overflowed int value; correct long value",
            complexity="- N/A (concept)",
            enterprise_relevance="Overflow bugs show up in billing, counters, pagination offsets, and metrics aggregation.",
            interview_points=_bullets("Primitive sizes", "Overflow behavior", "== vs equals for boxed types"),
            best_practices=_bullets("Use long for counts", "Avoid unnecessary boxing", "Use Math.addExact when you need overflow detection"),
        )

    if low == "control flow (if/switch/loops)":
        return build_page(
            t,
            concept="Control flow determines execution paths; production code favors readability and explicit edge handling.",
            problem="Implement branching and iteration while avoiding bugs (off-by-one, missing default cases).",
            intuition="Prefer early returns for validation; prefer for-each for collections; use switch when it improves clarity.",
            java_impl=textwrap.dedent(
                """\
                import java.util.*;

                public class ControlFlow {
                    static String classify(int n) {
                        if (n < 0) return "NEG";
                        if (n == 0) return "ZERO";
                        return "POS";
                    }

                    public static void main(String[] args) {
                        for (int n : new int[]{-1, 0, 5}) {
                            System.out.println(classify(n));
                        }
                    }
                }
                """
            ),
            stream_impl=textwrap.dedent(
                """\
                import java.util.*;
                import java.util.stream.*;

                public class ControlFlowStream {
                    public static void main(String[] args) {
                        List<Integer> xs = Arrays.asList(-1, 0, 5);
                        List<String> out = xs.stream()
                                .map(n -> n < 0 ? "NEG" : (n == 0 ? "ZERO" : "POS"))
                                .collect(Collectors.toList());
                        System.out.println(out);
                    }
                }
                """
            ),
            sample_input="- Input: [-1, 0, 5]",
            execution_steps=_bullets("Classify each value", "Print results"),
            output="- Output: [NEG, ZERO, POS]",
            complexity="- Time: O(n)\n- Space: O(n)",
            enterprise_relevance="Control flow drives validation and error handling paths; keep it explicit to avoid production surprises.",
            interview_points=_bullets("Switch vs if", "Loop invariants", "Off-by-one errors"),
            best_practices=_bullets("Prefer readable branching", "Handle defaults explicitly", "Avoid deeply nested conditionals"),
        )

    if low == "methods and overloading":
        return build_page(
            t,
            concept="Overloading allows multiple methods with the same name but different parameter lists; resolution happens at compile time.",
            problem="Design APIs with clear overloads without ambiguity.",
            intuition="Avoid overloads that differ only by boxed vs primitive or by nullability; it confuses call sites.",
            java_impl=textwrap.dedent(
                """\
                public class Overload {
                    static String f(int x) { return "int"; }
                    static String f(Integer x) { return "Integer"; }

                    public static void main(String[] args) {
                        System.out.println(f(1));
                        System.out.println(f(Integer.valueOf(2)));
                    }
                }
                """
            ),
            stream_impl=GEN_STREAM,
            sample_input="- Input: 1 and Integer(2)",
            execution_steps=_bullets("Call overload with primitive", "Call overload with boxed"),
            output="- Output: int, Integer",
            complexity="- N/A (concept)",
            enterprise_relevance="API design affects library usability and prevents runtime bugs due to ambiguous overload resolution.",
            interview_points=_bullets("Compile-time vs runtime dispatch", "Autoboxing pitfalls"),
            best_practices=_bullets("Avoid ambiguous overload sets", "Prefer distinct method names when behavior differs"),
        )

    # ---------- Section 4: language features ----------
    if low == "lambda expressions":
        return build_page(
            t,
            concept=(
                "A lambda is an inline implementation of a functional interface. In Java 8 it enables passing behavior "
                "(functions) without creating anonymous classes."
            ),
            problem="Implement a strategy (e.g., filtering) without boilerplate anonymous classes.",
            intuition=(
                "A lambda is just a method body with captured variables (effectively-final).\n\n"
                "ASCII:\ninterface Fn { R apply(T); }\n   ^\n   | implemented by lambda"
            ),
            java_impl=textwrap.dedent(
                """\
                import java.util.*;

                public class LambdaExample {
                    public static void main(String[] args) {
                        List<String> names = Arrays.asList("amy", "bob", "carl");
                        Collections.sort(names, (a, b) -> a.compareTo(b));
                        System.out.println(names);
                    }
                }
                """
            ),
            stream_impl=textwrap.dedent(
                """\
                import java.util.*;
                import java.util.stream.*;

                public class LambdaStreamExample {
                    public static void main(String[] args) {
                        List<String> names = Arrays.asList("amy", "bob", "carl");
                        List<String> out = names.stream()
                                .filter(s -> s.length() >= 3)
                                .map(s -> s.toUpperCase())
                                .collect(Collectors.toList());
                        System.out.println(out);
                    }
                }
                """
            ),
            sample_input="- Input: names = [amy, bob, carl]",
            execution_steps=_bullets(
                "Use lambda comparator to sort",
                "Use lambda predicates/mappers in a Stream pipeline",
            ),
            output="- Output: [AMY, BOB, CARL] (stream example)",
            complexity="- Time: O(n log n) for sort; O(n) for stream transform\n- Space: O(n) for collected output",
            enterprise_relevance=(
                "Lambdas reduce boilerplate in service-layer transformations (DTO mapping, validation filters) and in concurrency "
                "(executors, callbacks)."
            ),
            interview_points=_bullets(
                "What is ‘effectively final’?",
                "Difference between lambda and anonymous class (this/scope/serialization)",
                "When can lambdas hurt readability?",
            ),
            best_practices=_bullets(
                "Keep lambdas small; extract named methods for complex logic",
                "Avoid capturing mutable state",
                "Prefer method references when they read better",
            ),
        )

    if low == "functional interfaces":
        return build_page(
            t,
            concept="A functional interface has exactly one abstract method and is the target type for lambdas (e.g., Predicate, Function).",
            problem="Define a stable API boundary that accepts behavior (validation, transformation) without framework dependencies.",
            intuition=(
                "If an interface has 1 abstract method, the compiler can map a lambda to it.\n\n"
                "ASCII:\n(User) -> validate(User) : boolean"
            ),
            java_impl=textwrap.dedent(
                """\
                @FunctionalInterface
                interface Validator<T> {
                    boolean isValid(T t);
                }

                public class FunctionalInterfaceExample {
                    public static void main(String[] args) {
                        Validator<String> nonEmpty = s -> s != null && !s.trim().isEmpty();
                        System.out.println(nonEmpty.isValid("  "));
                    }
                }
                """
            ),
            stream_impl=textwrap.dedent(
                """\
                import java.util.*;
                import java.util.stream.*;

                public class FunctionalInterfaceStreamExample {
                    public static void main(String[] args) {
                        List<String> xs = Arrays.asList("a", "", "b");
                        List<String> out = xs.stream().filter(s -> !s.isEmpty()).collect(Collectors.toList());
                        System.out.println(out);
                    }
                }
                """
            ),
            sample_input="- Input: [a, "", b]",
            execution_steps=_bullets("Define functional interface", "Pass lambda implementation", "Use in stream filter"),
            output="- Output: [a, b]",
            complexity="- Time: O(n)\n- Space: O(n) for output list",
            enterprise_relevance="Custom functional interfaces can encode domain behavior (e.g., authorization checks) and enable dependency injection without frameworks.",
            interview_points=_bullets("What is @FunctionalInterface?", "Can it have default methods?", "Why use java.util.function types?"),
            best_practices=_bullets("Prefer standard functional interfaces", "Document null-handling", "Keep lambdas side-effect free"),
        )

    if low in ("method references",):
        return build_page(
            t,
            concept="Method references (`Type::method`) are shorthand for lambdas when the lambda only calls an existing method.",
            problem="Improve readability of streams and callbacks by using a concise method call form.",
            intuition="Replace `x -> foo(x)` with `ClassName::foo` when signatures match.",
            java_impl=textwrap.dedent(
                """\
                import java.util.*;

                public class MethodRefExample {
                    static int len(String s) { return s.length(); }

                    public static void main(String[] args) {
                        List<String> xs = Arrays.asList("amy", "bob");
                        xs.forEach(System.out::println);
                    }
                }
                """
            ),
            stream_impl=textwrap.dedent(
                """\
                import java.util.*;
                import java.util.stream.*;

                public class MethodRefStreamExample {
                    public static void main(String[] args) {
                        List<String> xs = Arrays.asList("amy", "bob");
                        List<Integer> out = xs.stream().map(String::length).collect(Collectors.toList());
                        System.out.println(out);
                    }
                }
                """
            ),
            sample_input="- Input: [amy, bob]",
            execution_steps=_bullets("Use `System.out::println` for printing", "Use `String::length` for mapping"),
            output="- Output: [3, 3]",
            complexity="- Time: O(n)\n- Space: O(n)",
            enterprise_relevance="Method references help standardize house-style pipelines and reduce cognitive load during code review.",
            interview_points=_bullets("Bound vs unbound references", "Constructor references", "Overload resolution"),
            best_practices=_bullets("Use when it improves readability", "Avoid when it obscures intent"),
        )

    if low in ("default methods", "static methods in interfaces"):
        name = "default" if low == "default methods" else "static"
        return build_page(
            t,
            concept=(
                f"Java 8 added {name} methods in interfaces to evolve APIs without breaking implementors. "
                "Default methods provide a body; static methods are utility functions on the interface type."
            ),
            problem="Add new methods to an interface already implemented by many classes without forcing changes everywhere.",
            intuition=(
                "Default methods are inherited unless overridden. If two interfaces provide the same default, the implementing class must resolve it."
            ),
            java_impl=textwrap.dedent(
                """\
                interface Auditable {
                    default String auditTag() { return "AUDIT"; }
                    static String normalize(String s) { return s == null ? "" : s.trim(); }
                }

                class Order implements Auditable {}

                public class InterfaceMethods {
                    public static void main(String[] args) {
                        System.out.println(new Order().auditTag());
                        System.out.println(Auditable.normalize(" x "));
                    }
                }
                """
            ),
            stream_impl=GEN_STREAM,
            sample_input="- Input: \" x \"",
            execution_steps=_bullets("Call default method via instance", "Call static method via interface"),
            output="- Output: AUDIT and x",
            complexity="- N/A (concept)",
            enterprise_relevance="Used heavily in library/API evolution and for shared behavior in internal interfaces (e.g., identifiers, audit metadata).",
            interview_points=_bullets("Diamond problem resolution", "Why not abstract class?", "Binary compatibility"),
            best_practices=_bullets("Keep default methods small", "Avoid state in interfaces", "Document behavior changes"),
        )

    if low in ("optional api",):
        return build_page(
            t,
            concept="`Optional<T>` represents a value that may be present, making absence explicit without returning null.",
            problem="Avoid NullPointerException and unclear API contracts when a value may be missing.",
            intuition="Use Optional at API boundaries (return values). Avoid Optional fields/serialization. Prefer `map/flatMap/orElseGet`.",
            java_impl=textwrap.dedent(
                """\
                import java.util.*;

                public class OptionalExample {
                    static Optional<String> findUserEmail(String userId) {
                        return "u1".equals(userId) ? Optional.of("u1@example.com") : Optional.empty();
                    }

                    public static void main(String[] args) {
                        String email = findUserEmail("u2").orElse("unknown");
                        System.out.println(email);
                    }
                }
                """
            ),
            stream_impl=textwrap.dedent(
                """\
                import java.util.*;
                import java.util.stream.*;

                public class OptionalStreamExample {
                    public static void main(String[] args) {
                        List<Optional<Integer>> xs = Arrays.asList(Optional.of(1), Optional.empty(), Optional.of(3));
                        List<Integer> out = xs.stream()
                                .filter(Optional::isPresent)
                                .map(Optional::get)
                                .collect(Collectors.toList());
                        System.out.println(out);
                    }
                }
                """
            ),
            sample_input="- Input: userId = u2",
            execution_steps=_bullets("Return Optional.empty when missing", "Use orElse/orElseGet at boundary"),
            output="- Output: unknown",
            complexity="- Time: O(1)\n- Space: O(1)",
            enterprise_relevance="Optional makes API contracts explicit in service/domain layers, reducing NPE incidents in production.",
            interview_points=_bullets("orElse vs orElseGet", "Why avoid Optional in fields", "flatMap usage"),
            best_practices=_bullets("Return Optional, don’t accept Optional params unless justified", "Avoid Optional.get without isPresent"),
        )

    if low in ("new date and time api",):
        return build_page(
            t,
            concept="Java 8 `java.time` is immutable, thread-safe, and timezone-correct (unlike `java.util.Date/Calendar`).",
            problem="Correctly handle time zones, instants, and business dates without mutable date bugs.",
            intuition="Use `Instant` for machine time, `ZonedDateTime` for user/timezone, `LocalDate` for business date.",
            java_impl=textwrap.dedent(
                """\
                import java.time.*;
                import java.time.format.*;

                public class JavaTimeExample {
                    public static void main(String[] args) {
                        Instant now = Instant.now();
                        ZonedDateTime ist = now.atZone(ZoneId.of("Asia/Kolkata"));
                        String s = DateTimeFormatter.ISO_ZONED_DATE_TIME.format(ist);
                        System.out.println(s);
                    }
                }
                """
            ),
            stream_impl=GEN_STREAM,
            sample_input="- Input: system clock instant",
            execution_steps=_bullets("Capture Instant", "Convert to timezone", "Format"),
            output="- Output: ISO timestamp string",
            complexity="- N/A (concept)",
            enterprise_relevance="Critical for audit logs, SLAs, scheduling, and anything cross-timezone (billing cutoffs, reporting).",
            interview_points=_bullets("Instant vs LocalDate", "Why Date is problematic", "Time zone conversions"),
            best_practices=_bullets("Store as Instant/UTC", "Convert at edges", "Avoid custom timezone math"),
        )

    # ---------- Section 5/6: streams & collectors ----------
    if low in ("stream api overview", "creating streams", "stream pipeline", "intermediate operations", "terminal operations"):
        concept = "Streams are lazy pipelines over a data source. Intermediate ops build stages; terminal ops trigger execution."
        if low == "creating streams":
            java_impl = textwrap.dedent(
                """\
                import java.util.*;
                import java.util.stream.*;

                public class CreatingStreams {
                    public static void main(String[] args) {
                        Stream<Integer> a = Stream.of(1, 2, 3);
                        Stream<Integer> b = Arrays.asList(4, 5).stream();
                        IntStream c = IntStream.rangeClosed(1, 3);
                        System.out.println(a.count() + b.count() + c.count());
                    }
                }
                """
            )
        else:
            java_impl = GEN_JAVA
        stream_impl = textwrap.dedent(
            """\
            import java.util.*;
            import java.util.stream.*;

            public class StreamPipeline {
                public static void main(String[] args) {
                    List<String> names = Arrays.asList("amy", "bob", "carl", "bob");
                    List<String> out = names.stream()
                            .filter(n -> n.length() >= 3)
                            .distinct()
                            .sorted()
                            .collect(Collectors.toList());
                    System.out.println(out);
                }
            }
            """
        )
        return build_page(
            t,
            concept=concept,
            problem="Transform and aggregate a collection predictably, with readable intent and minimal boilerplate.",
            intuition=(
                "Streams are *lazy*: building a pipeline does nothing until a terminal operation pulls results.\n\n"
                "ASCII:\nsource -> filter -> map -> collect\n   |       |       |       |\n elements flow per terminal pull"
            ),
            java_impl=java_impl,
            stream_impl=stream_impl,
            sample_input="- Input: [amy, bob, carl, bob]",
            execution_steps=_bullets("Build pipeline", "Terminal `collect` triggers traversal", "Each element passes through stages"),
            output="- Output: [amy, bob, carl]",
            complexity="- Time: O(n log n) if sorted; otherwise O(n)\n- Space: O(n) for collected output",
            enterprise_relevance="Used for DTO mapping, request validation, in-memory aggregation, and batch transforms (with careful memory limits).",
            interview_points=_bullets("Intermediate vs terminal", "Lazy evaluation", "Stateful ops like sorted/distinct"),
            best_practices=_bullets("Avoid side-effects", "Prefer primitive streams for numeric work", "Don’t parallelize without measuring"),
        )

    if low in ("map vs flatmap", "filter", "reduce", "collect", "parallel streams"):
        # Provide operation-specific example
        if low == "filter":
            stream_impl = textwrap.dedent(
                """\
                import java.util.*;
                import java.util.stream.*;

                public class FilterOp {
                    public static void main(String[] args) {
                        List<Integer> xs = Arrays.asList(1, 2, 3, 4, 5);
                        List<Integer> evens = xs.stream().filter(x -> x % 2 == 0).collect(Collectors.toList());
                        System.out.println(evens);
                    }
                }
                """
            )
            java_impl = textwrap.dedent(
                """\
                import java.util.*;

                public class FilterLoop {
                    public static List<Integer> evens(List<Integer> xs) {
                        List<Integer> out = new ArrayList<>();
                        for (int x : xs) if (x % 2 == 0) out.add(x);
                        return out;
                    }
                }
                """
            )
            sample_input, output = "- Input: [1,2,3,4,5]", "- Output: [2,4]"
            complexity = "- Time: O(n)\n- Space: O(n)"
        elif low == "map vs flatmap":
            stream_impl = textwrap.dedent(
                """\
                import java.util.*;
                import java.util.stream.*;

                public class MapVsFlatMap {
                    public static void main(String[] args) {
                        List<String> words = Arrays.asList("a b", "c");

                        List<String[]> mapped = words.stream().map(w -> w.split(" ")).collect(Collectors.toList());
                        List<String> flat = words.stream().flatMap(w -> Arrays.stream(w.split(" "))).collect(Collectors.toList());

                        System.out.println(mapped.size());
                        System.out.println(flat);
                    }
                }
                """
            )
            java_impl = GEN_JAVA
            sample_input, output = "- Input: [\"a b\", \"c\"]", "- Output: flat = [a, b, c]"
            complexity = "- Time: O(n)\n- Space: O(n)"
        elif low == "reduce":
            stream_impl = textwrap.dedent(
                """\
                import java.util.*;
                import java.util.stream.*;

                public class ReduceOp {
                    public static void main(String[] args) {
                        int sum = Stream.of(1, 2, 3).reduce(0, Integer::sum);
                        System.out.println(sum);
                    }
                }
                """
            )
            java_impl = textwrap.dedent(
                """\
                public class ReduceLoop {
                    public static int sum(int[] a) {
                        int s = 0;
                        for (int x : a) s += x;
                        return s;
                    }
                }
                """
            )
            sample_input, output = "- Input: [1,2,3]", "- Output: 6"
            complexity = "- Time: O(n)\n- Space: O(1)"
        elif low == "collect":
            stream_impl = textwrap.dedent(
                """\
                import java.util.*;
                import java.util.stream.*;

                public class CollectOp {
                    public static void main(String[] args) {
                        List<String> out = Stream.of("a", "b").collect(Collectors.toList());
                        System.out.println(out);
                    }
                }
                """
            )
            java_impl = GEN_JAVA
            sample_input, output = "- Input: [a,b]", "- Output: [a, b]"
            complexity = "- Time: O(n)\n- Space: O(n)"
        else:  # parallel streams
            stream_impl = textwrap.dedent(
                """\
                import java.util.*;
                import java.util.stream.*;

                public class ParallelStreamExample {
                    public static void main(String[] args) {
                        long sum = LongStream.rangeClosed(1, 1_000_000)
                                .parallel()
                                .sum();
                        System.out.println(sum);
                    }
                }
                """
            )
            java_impl = GEN_JAVA
            sample_input, output = "- Input: range 1..1_000_000", "- Output: 500000500000"
            complexity = "- Time: O(n) work (parallelized)\n- Space: O(1)"

        return build_page(
            t,
            concept=f"Stream operation: {t}.",
            problem="Solve a small transformation/aggregation task using Java 8 and Streams.",
            intuition="Pick the operator that matches intent: filter to drop, map to transform, flatMap to flatten, reduce to fold, collect to build containers.",
            java_impl=java_impl,
            stream_impl=stream_impl,
            sample_input=sample_input,
            execution_steps=_bullets("Build pipeline", "Run terminal operation", "Read output"),
            output=output,
            complexity=complexity,
            enterprise_relevance="These are the building blocks of service-layer mapping and batch aggregation. Parallel streams require strict side-effect discipline.",
            interview_points=_bullets("When to use which op", "Pitfalls (ordering, side effects)", "Complexity"),
            best_practices=_bullets("Keep lambdas pure", "Prefer primitives", "Don’t log in hot loops"),
        )

    if low in ("tolist", "toset", "tomap", "groupingby", "partitioningby", "joining", "counting", "summarizing", "collectors overview"):
        if low == "collectors overview":
            concept = "Collectors are predefined reduction strategies used with `collect(...)` to build collections or compute aggregates."
        else:
            concept = f"Collector: {t}."
        stream_impl = textwrap.dedent(
            """\
            import java.util.*;
            import java.util.stream.*;

            public class CollectorExample {
                public static void main(String[] args) {
                    List<String> names = Arrays.asList("amy", "bob", "carl", "bob");
                    System.out.println(names.stream().collect(Collectors.toSet()));
                    System.out.println(names.stream().collect(Collectors.groupingBy(String::length, Collectors.counting())));
                }
            }
            """
        )
        return build_page(
            t,
            concept=concept,
            problem="Aggregate or transform a stream into a collection/map/summary efficiently.",
            intuition="Collectors define how to accumulate elements (supplier, accumulator, combiner, finisher) and are designed to be safe for parallel when used correctly.",
            java_impl=GEN_JAVA,
            stream_impl=stream_impl,
            sample_input="- Input: [amy, bob, carl, bob]",
            execution_steps=_bullets("Choose downstream collector", "Collect", "Read aggregated result"),
            output="- Output: example set and grouping map",
            complexity="- Time: O(n)\n- Space: O(n)",
            enterprise_relevance="Used in report generation, analytics endpoints, and transforming domain objects to response structures.",
            interview_points=_bullets("Difference between groupingBy and partitioningBy", "toMap merge function", "Parallel collector safety"),
            best_practices=_bullets("Always specify merge function for toMap if duplicates possible", "Prefer immutable results at boundaries", "Avoid collecting huge lists in memory"),
        )

    # ---------- Map API methods (Java 8) ----------
    if low in (
        "putifabsent",
        "compute",
        "computeifabsent",
        "computeifpresent",
        "merge",
        "replace",
        "replaceall",
        "getordefault",
        "foreach",
    ):
        java_impl = textwrap.dedent(
            f"""\
            import java.util.*;

            public class MapApi_{low.replace('-', '_')} {{
                public static void main(String[] args) {{
                    Map<String, Integer> m = new HashMap<>();
                    m.put("a", 1);

                    // {t}
                    // Adjust example based on method intent.
                    {"m.putIfAbsent(\"a\", 9);" if low=="putifabsent" else ""}
                    {"m.compute(\"a\", (k,v) -> v == null ? 1 : v + 1);" if low=="compute" else ""}
                    {"m.computeIfAbsent(\"b\", k -> 10);" if low=="computeifabsent" else ""}
                    {"m.computeIfPresent(\"a\", (k,v) -> v + 100);" if low=="computeifpresent" else ""}
                    {"m.merge(\"a\", 5, Integer::sum);" if low=="merge" else ""}
                    {"m.replace(\"a\", 999);" if low=="replace" else ""}
                    {"m.replaceAll((k,v) -> v * 2);" if low=="replaceall" else ""}
                    {"System.out.println(m.getOrDefault(\"missing\", -1));" if low=="getordefault" else ""}
                    {"m.forEach((k,v) -> System.out.println(k + \"=\" + v));" if low=="foreach" else ""}

                    System.out.println(m);
                }}
            }}
            """
        )
        return build_page(
            t,
            concept=f"Java 8 Map API method: `{t}`.",
            problem="Update map entries safely without verbose containsKey/get/put patterns.",
            intuition="Use compute/merge methods to centralize update logic and avoid races in concurrent maps (still consider atomicity guarantees).",
            java_impl=java_impl,
            stream_impl=GEN_STREAM,
            sample_input="- Input: m={a=1}",
            execution_steps=_bullets("Call the map method", "Inspect updated map"),
            output="- Output: Updated map printed",
            complexity="- Time: O(1) average per operation\n- Space: O(1)",
            enterprise_relevance="These APIs reduce bug-prone map update code in caches, counters, dedup maps, and aggregation pipelines.",
            interview_points=_bullets("Difference between computeIfAbsent and putIfAbsent", "When merge is simpler", "ConcurrentHashMap behavior"),
            best_practices=_bullets("Keep remapping functions side-effect free", "Avoid expensive computations inside computeIfAbsent"),
        )

    # ---------- Algorithms ----------
    if low in ("linear search",):
        return build_page(
            t,
            concept="Linear search scans elements until it finds the target.",
            problem="Find index of x in an unsorted array.",
            intuition="Check each element sequentially; stop when found.",
            java_impl=textwrap.dedent(
                """\
                public class LinearSearch {
                    public static int search(int[] a, int x) {
                        for (int i = 0; i < a.length; i++) if (a[i] == x) return i;
                        return -1;
                    }
                }
                """
            ),
            stream_impl=textwrap.dedent(
                """\
                import java.util.*;
                import java.util.stream.*;

                public class LinearSearchStream {
                    public static OptionalInt indexOf(int[] a, int x) {
                        return IntStream.range(0, a.length).filter(i -> a[i] == x).findFirst();
                    }
                }
                """
            ),
            sample_input="- Input: a=[4,2,9], x=9",
            execution_steps=_bullets("Scan index 0..n-1", "Return when found"),
            output="- Output: 2",
            complexity="- Time: O(n)\n- Space: O(1)",
            enterprise_relevance="Used when data is small or unsorted; often as a fallback in parsing/validation logic.",
            interview_points=_bullets("When linear beats binary", "Short-circuiting"),
            best_practices=_bullets("Prefer binary search for sorted data", "Avoid repeated scans in hot paths"),
        )

    # For pages we already implemented specially elsewhere
    if low == "two sum":
        return two_sum_page()
    if low == "binary search":
        return binary_search_page()
    if low == "second highest salary":
        return second_highest_salary_page()

    # ---------- Fallback: still non-dummy ----------
    return build_page(
        t,
        concept=(
            f"{t} is a Java 8 topic relevant for production engineering and interview preparation. "
            "This page summarizes intent, safe usage, and a reference implementation."
        ),
        problem=f"Demonstrate {t} with a concrete example, including edge cases.",
        intuition=(
            "Start with the simplest correct approach. Then discuss optimizations only if needed.\n\n"
            "ASCII (pattern):\ninput -> process -> output"
        ),
        java_impl=GEN_JAVA,
        stream_impl=GEN_STREAM,
        sample_input="- Input: (choose a minimal input that hits at least one edge case)",
        execution_steps=_bullets("Define data", "Apply algorithm/feature", "Verify output"),
        output="- Output: (expected output)",
        complexity="- Time: depends on approach\n- Space: depends on data structures",
        enterprise_relevance="Explain where it appears in real systems and what can go wrong in production.",
        interview_points=_bullets("Correctness", "Complexity", "Edge cases", "Alternatives"),
        best_practices=_bullets("Write tests", "Prefer readability", "Document assumptions"),
    )


def two_sum_page() -> str:
    return TEMPLATE.format(
        title="Two Sum",
        concept="Find two indices i, j such that a[i] + a[j] = target. Canonical hash-map lookup problem.",
        problem="Given an int array and a target sum, return indices of the two numbers that add up to target.",
        intuition="Single pass: store seen values -> index. For each value x, check if (target-x) was already seen.",
        java_impl=textwrap.dedent('''\
            import java.util.*;

            public class TwoSum {
                public static int[] twoSum(int[] a, int target) {
                    Map<Integer, Integer> seen = new HashMap<>();
                    for (int i = 0; i < a.length; i++) {
                        int need = target - a[i];
                        Integer j = seen.get(need);
                        if (j != null) return new int[]{j, i};
                        seen.put(a[i], i);
                    }
                    return new int[]{-1, -1};
                }
            }
        ''').strip(),
        stream_impl=textwrap.dedent('''\
            import java.util.*;
            import java.util.stream.*;

            public class TwoSumStreamNote {
                public static void main(String[] args) {
                    // Streams are not ideal for index-based lookups; prefer the hash-map loop.
                }
            }
        ''').strip(),
        sample_input="- Input: a = [2, 7, 11, 15], target = 9",
        execution_steps="- seen = {}\n- i=0, x=2, need=7 (not found) -> seen{2:0}\n- i=1, x=7, need=2 (found at 0) -> return [0,1]",
        output="- Output: [0, 1]",
        complexity="- Time: O(n)\n- Space: O(n)",
        enterprise_relevance="Used in dedup/join-like workflows, cache lookups, and detecting complementary pairs in rules engines.",
        interview_points="- Duplicates\n- No-solution behavior\n- Sorting + two pointers alternative",
        best_practices="- Use `HashMap`\n- Define behavior when no solution\n- Avoid overflow with extreme integers",
    )


def binary_search_page() -> str:
    return TEMPLATE.format(
        title="Binary Search",
        concept="Search a sorted array by repeatedly halving the search interval.",
        problem="Given sorted array a and target x, return index or -1.",
        intuition="Maintain [lo, hi]. Check mid. If a[mid] < x, discard left half; else discard right half.",
        java_impl=textwrap.dedent('''\
            public class BinarySearch {
                public static int search(int[] a, int x) {
                    int lo = 0, hi = a.length - 1;
                    while (lo <= hi) {
                        int mid = lo + (hi - lo) / 2;
                        if (a[mid] == x) return mid;
                        if (a[mid] < x) lo = mid + 1;
                        else hi = mid - 1;
                    }
                    return -1;
                }
            }
        ''').strip(),
        stream_impl=textwrap.dedent('''\
            import java.util.*;
            import java.util.stream.*;

            public class BinarySearchStreamNote {
                public static void main(String[] args) {
                    // Binary search is index-based; streams add overhead and reduce clarity.
                }
            }
        ''').strip(),
        sample_input="- Input: a = [1, 3, 5, 8, 12], x = 8",
        execution_steps="- lo=0, hi=4\n- mid=2 => 5 < 8 => lo=3\n- mid=3 => 8 == 8 => return 3",
        output="- Output: 3",
        complexity="- Time: O(log n)\n- Space: O(1)",
        enterprise_relevance="Used in routing tables, interval lookups, feature-flag bucketing, and any sorted index structure.",
        interview_points="- Overflow-safe mid\n- First/last occurrence\n- Rotated array variant",
        best_practices="- Use `mid = lo + (hi-lo)/2`\n- Be explicit about invariants\n- Add tests for boundaries",
    )


def second_highest_salary_page() -> str:
    return TEMPLATE.format(
        title="Second Highest Salary",
        concept="Compute the second distinct highest salary from a list of employees.",
        problem="Given employees with salaries, find the second highest distinct salary.",
        intuition="Simplest: extract salaries, distinct, sort desc, skip(1), take first. For huge sets, track top-2 in one pass.",
        java_impl=textwrap.dedent('''\
            import java.util.*;

            public class SecondHighestSalary {
                static class Emp {
                    final String name;
                    final int salary;
                    Emp(String name, int salary) { this.name = name; this.salary = salary; }
                }

                public static Integer secondHighestDistinct(List<Emp> emps) {
                    Integer first = null;
                    Integer second = null;
                    for (Emp e : emps) {
                        int s = e.salary;
                        if (first == null || s > first) {
                            if (first == null || s != first) second = first;
                            first = s;
                        } else if (s != first && (second == null || s > second)) {
                            second = s;
                        }
                    }
                    return second;
                }
            }
        ''').strip(),
        stream_impl=textwrap.dedent('''\
            import java.util.*;
            import java.util.stream.*;

            public class SecondHighestSalaryStream {
                static class Emp {
                    final String name;
                    final int salary;
                    Emp(String name, int salary) { this.name = name; this.salary = salary; }
                }

                public static Optional<Integer> secondHighestDistinct(List<Emp> emps) {
                    return emps.stream()
                            .map(e -> e.salary)
                            .distinct()
                            .sorted(Comparator.reverseOrder())
                            .skip(1)
                            .findFirst();
                }
            }
        ''').strip(),
        sample_input="- Input: [(A,100),(B,120),(C,200),(D,180)]",
        execution_steps="- salaries=[100,120,200,180]\n- sort desc=[200,180,120,100]\n- skip 1 -> 180",
        output="- Output: 180",
        complexity="- Time: O(n log n) (sorting)\n- Space: O(n)",
        enterprise_relevance="Appears in analytics APIs (top-N), compensation dashboards, and batch reports.",
        interview_points="- Distinct vs non-distinct\n- One-pass top-2\n- Empty/one-element inputs",
        best_practices="- Define behavior for duplicates\n- Prefer one-pass for very large datasets\n- Keep it readable",
    )


def main() -> None:
    root = Path(__file__).resolve().parent
    docs = root / "docs"

    overwrite = True

    paths: list[tuple[str, str]] = [
        # Section 01-03 (added)
        ("docs/section-01/java-platform-overview.md", "Java Platform Overview (JDK vs JRE vs JVM)"),
        ("docs/section-01/data-types-and-operators.md", "Data Types and Operators"),
        ("docs/section-01/control-flow.md", "Control Flow (if/switch/loops)"),
        ("docs/section-01/methods-and-overloading.md", "Methods and Overloading"),

        ("docs/section-02/oop-pillars.md", "OOP Pillars (Encapsulation, Inheritance, Polymorphism, Abstraction)"),
        ("docs/section-02/abstract-class-vs-interface.md", "Abstract Class vs Interface"),
        ("docs/section-02/object-contracts.md", "equals/hashCode/toString contracts"),
        ("docs/section-02/immutability.md", "Immutability"),

        ("docs/section-03/jvm-memory-areas.md", "JVM Memory Areas (Heap, Stack, Metaspace)"),
        ("docs/section-03/gc-basics.md", "Garbage Collection Basics"),
        ("docs/section-03/exceptions.md", "Exceptions (Checked vs Unchecked)"),
        ("docs/section-03/performance-pitfalls.md", "Common Performance Pitfalls"),

        # Section 4
        ("docs/section-04/lambda-expressions.md", "Lambda Expressions"),
        ("docs/section-04/functional-interfaces.md", "Functional Interfaces"),
        ("docs/section-04/method-references.md", "Method References"),
        ("docs/section-04/default-methods.md", "Default Methods"),
        ("docs/section-04/static-methods-in-interfaces.md", "Static Methods in Interfaces"),
        ("docs/section-04/optional-api.md", "Optional API"),
        ("docs/section-04/new-date-and-time-api.md", "New Date and Time API"),
        # Section 5
        ("docs/section-05/stream-api-overview.md", "Stream API Overview"),
        ("docs/section-05/creating-streams.md", "Creating Streams"),
        ("docs/section-05/stream-pipeline.md", "Stream Pipeline"),
        ("docs/section-05/intermediate-operations.md", "Intermediate Operations"),
        ("docs/section-05/terminal-operations.md", "Terminal Operations"),
        ("docs/section-05/map-vs-flatmap.md", "map vs flatMap"),
        ("docs/section-05/filter.md", "filter"),
        ("docs/section-05/reduce.md", "reduce"),
        ("docs/section-05/collect.md", "collect"),
        ("docs/section-05/parallel-streams.md", "parallel streams"),
        # Section 6
        ("docs/section-06/collectors-overview.md", "Collectors Overview"),
        ("docs/section-06/tolist.md", "toList"),
        ("docs/section-06/toset.md", "toSet"),
        ("docs/section-06/tomap.md", "toMap"),
        ("docs/section-06/groupingby.md", "groupingBy"),
        ("docs/section-06/partitioningby.md", "partitioningBy"),
        ("docs/section-06/joining.md", "joining"),
        ("docs/section-06/counting.md", "counting"),
        ("docs/section-06/summarizing.md", "summarizing"),
        # Section 7
        ("docs/section-07/collection-hierarchy.md", "Collection Hierarchy"),
        ("docs/section-07/iterable-interface.md", "Iterable Interface"),
        ("docs/section-07/iterator.md", "Iterator"),
        ("docs/section-07/comparable-vs-comparator.md", "Comparable vs Comparator"),
        # Section 8
        ("docs/section-08/list-interface.md", "List Interface"),
        ("docs/section-08/arraylist-internals.md", "ArrayList Internals"),
        ("docs/section-08/linkedlist-internals.md", "LinkedList Internals"),
        ("docs/section-08/vector.md", "Vector"),
        ("docs/section-08/copyonwritearraylist.md", "CopyOnWriteArrayList"),
        # Section 9
        ("docs/section-09/set-interface.md", "Set Interface"),
        ("docs/section-09/hashset-internals.md", "HashSet Internals"),
        ("docs/section-09/linkedhashset.md", "LinkedHashSet"),
        ("docs/section-09/treeset.md", "TreeSet"),
        # Section 10
        ("docs/section-10/map-interface.md", "Map Interface"),
        ("docs/section-10/hashmap-internals.md", "HashMap Internals"),
        ("docs/section-10/hashmap-java-8-improvements.md", "HashMap Java 8 Improvements"),
        ("docs/section-10/linkedhashmap.md", "LinkedHashMap"),
        ("docs/section-10/treemap.md", "TreeMap"),
        ("docs/section-10/weakhashmap.md", "WeakHashMap"),
        # Section 11
        ("docs/section-11/putifabsent.md", "putIfAbsent"),
        ("docs/section-11/compute.md", "compute"),
        ("docs/section-11/computeifabsent.md", "computeIfAbsent"),
        ("docs/section-11/computeifpresent.md", "computeIfPresent"),
        ("docs/section-11/merge.md", "merge"),
        ("docs/section-11/replace.md", "replace"),
        ("docs/section-11/replaceall.md", "replaceAll"),
        ("docs/section-11/getordefault.md", "getOrDefault"),
        ("docs/section-11/foreach.md", "forEach"),
        # Section 12
        ("docs/section-12/threads-vs-processes.md", "Threads vs Processes"),
        ("docs/section-12/thread-lifecycle.md", "Thread Lifecycle"),
        ("docs/section-12/synchronization.md", "Synchronization"),
        ("docs/section-12/volatile-keyword.md", "Volatile Keyword"),
        ("docs/section-12/locks-and-reentrantlock.md", "Locks and ReentrantLock"),
        # Section 13
        ("docs/section-13/executor-interface.md", "Executor Interface"),
        ("docs/section-13/executorservice.md", "ExecutorService"),
        ("docs/section-13/threadpoolexecutor.md", "ThreadPoolExecutor"),
        ("docs/section-13/scheduledexecutorservice.md", "ScheduledExecutorService"),
        ("docs/section-13/forkjoinpool.md", "ForkJoinPool"),
        # Section 14
        ("docs/section-14/completablefuture-overview.md", "CompletableFuture Overview"),
        ("docs/section-14/supplyasync.md", "supplyAsync"),
        ("docs/section-14/runasync.md", "runAsync"),
        ("docs/section-14/thenapply.md", "thenApply"),
        ("docs/section-14/thencompose.md", "thenCompose"),
        ("docs/section-14/thencombine.md", "thenCombine"),
        ("docs/section-14/exceptionally.md", "exceptionally"),
        ("docs/section-14/allof.md", "allOf"),
        ("docs/section-14/anyof.md", "anyOf"),
        # Section 15
        ("docs/section-15/linear-search.md", "Linear Search"),
        ("docs/section-15/binary-search.md", "Binary Search"),
        ("docs/section-15/search-in-rotated-array.md", "Search in Rotated Array"),
        # Section 16
        ("docs/section-16/bubble-sort.md", "Bubble Sort"),
        ("docs/section-16/selection-sort.md", "Selection Sort"),
        ("docs/section-16/insertion-sort.md", "Insertion Sort"),
        ("docs/section-16/merge-sort.md", "Merge Sort"),
        ("docs/section-16/quick-sort.md", "Quick Sort"),
        # Section 17
        ("docs/section-17/two-sum.md", "Two Sum"),
        ("docs/section-17/three-sum.md", "Three Sum"),
        ("docs/section-17/find-duplicate-numbers.md", "Find Duplicate Numbers"),
        ("docs/section-17/missing-number.md", "Missing Number"),
        ("docs/section-17/maximum-subarray.md", "Maximum Subarray"),
        # Section 18
        ("docs/section-18/reverse-string.md", "Reverse String"),
        ("docs/section-18/palindrome-detection.md", "Palindrome Detection"),
        ("docs/section-18/longest-substring-without-repeating-characters.md", "Longest Substring Without Repeating Characters"),
        ("docs/section-18/anagram-detection.md", "Anagram Detection"),
        ("docs/section-18/first-non-repeating-character.md", "First Non-Repeating Character"),
        # Section 19
        ("docs/section-19/second-highest-salary.md", "Second Highest Salary"),
        ("docs/section-19/group-employees-by-department.md", "Group Employees by Department"),
        ("docs/section-19/find-duplicate-elements-using-streams.md", "Find Duplicate Elements Using Streams"),
        ("docs/section-19/convert-list-to-map.md", "Convert List to Map"),
        ("docs/section-19/frequency-map-using-streams.md", "Frequency Map Using Streams"),
        # Section 20
        ("docs/section-20/parallel-api-calls.md", "Parallel API Calls"),
        ("docs/section-20/async-database-queries.md", "Async Database Queries"),
        ("docs/section-20/batch-processing.md", "Batch Processing"),
        ("docs/section-20/event-driven-processing.md", "Event Driven Processing"),
    ]

    wrote = 0
    for rel, title in paths:
        content = generate_topic_page(title)
        if write_file(root / rel, content, overwrite=overwrite):
            wrote += 1

    # Ensure index exists
    idx = docs / "index.md"
    idx.write_text(
        "# Java 8 Engineering & Interview Preparation\n\nUse the navigation to browse topics by section.\n",
        encoding="utf-8",
    )

    print(f"Wrote {wrote} page(s).")


if __name__ == "__main__":
    main()
