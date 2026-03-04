# New Date and Time API

## 1. Concept explanation
java.time is immutable, thread-safe, and timezone-correct (unlike java.util.Date/Calendar).

Use:
- Instant for machine time
- LocalDate for business dates
- ZonedDateTime for user/timezone

## 2. Problem statement
Convert and format a timestamp for a user-facing timezone without losing correctness.

## 3. Algorithm intuition
Store timestamps as UTC `Instant` in systems of record, then convert to `ZonedDateTime` at the boundary (UI/API response).

Use `Duration` for machine-time differences; use `Period` for date-based differences.

## 4. Java 8 implementation
```java
import java.time.*;
import java.time.format.*;

public class TimeDemo {
    public static void main(String[] args) {
        Instant fixed = Instant.parse("2020-01-02T03:04:05Z");
        ZonedDateTime ist = fixed.atZone(ZoneId.of("Asia/Kolkata"));
        System.out.println(DateTimeFormatter.ISO_ZONED_DATE_TIME.format(ist));
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
- Input: 2020-01-02T03:04:05Z

## 7. Execution steps
- Parse Instant
- Convert to Asia/Kolkata
- Format ISO string

## 8. Output
- Output: 2020-01-02T08:34:05+05:30[Asia/Kolkata]

## 9. Time and space complexity
- N/A (concept)

## 10. Enterprise relevance
Critical for audit logs, SLAs, scheduling, and cross-timezone correctness.

## 11. Interview discussion points
- Instant vs LocalDate
- Duration vs Period
- Zone conversions (DST)

## 12. Best practices
- Store UTC instants
- Convert at edges
- Avoid legacy Date/Calendar
