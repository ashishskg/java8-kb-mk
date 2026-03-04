# Java Platform Overview (JDK vs JRE vs JVM)

## 1. Concept explanation
JDK is the developer kit, JRE is the runtime environment, JVM executes bytecode. These layers matter for build vs run decisions.

## 2. Problem statement
Explain what runs your Java code and what you need installed in dev vs prod.

## 3. Algorithm intuition
Think: source -> bytecode -> JVM runtime.

ASCII:
Hello.java --javac--> Hello.class --JVM--> native

JDK = JRE + tools; JRE = JVM + core libs.

## 4. Java 8 implementation
```java
public class Hello {
    public static void main(String[] args) {
        System.out.println("Hello, Java");
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
- Input: `javac Hello.java` then `java Hello`

## 7. Execution steps
- Compile
- Load/verify classes
- Execute main

## 8. Output
- Output: Hello, Java

## 9. Time and space complexity
- N/A (concept)

## 10. Enterprise relevance
Affects container images, CI toolchains, and runtime tuning (GC/JIT flags).

## 11. Interview discussion points
- What is bytecode?
- What is JIT?
- What is the classloader?

## 12. Best practices
- Pin JDK version
- Monitor GC
- Use minimal runtime images where appropriate
