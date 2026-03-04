# Conversions (object <-> primitive)

## Stream -> IntStream/LongStream/DoubleStream
```java
List<String> names = Arrays.asList("amy", "bob", "carl");

IntStream len = names.stream().mapToInt(String::length);
LongStream ids = Stream.of("10", "11").mapToLong(Long::parseLong);
DoubleStream ds = Stream.of("1.5", "2.0").mapToDouble(Double::parseDouble);
```
Input: `names=["amy","bob","carl"]`, ids strings `["10","11"]`, doubles strings `["1.5","2.0"]`

Output: `len=[3,3,4]`, `ids=[10,11]`, `ds=[1.5,2.0]`

Production note: Primitive streams avoid boxing costs when aggregating.

## Primitive -> Stream (boxed)
```java
Stream<Integer> boxed = IntStream.range(0, 3).boxed();
```
Input: `IntStream.range(0,3) => [0,1,2]`

Output: `Stream<Integer>` elements `[0,1,2]`

Production note: Boxing allocates; do it only at API boundaries.

## Stream<T> -> Stream<U> via `map` (DTO mapping pattern)
```java
class User { final String name; User(String n){ this.name = n; } }
class UserDto { final String name; UserDto(String n){ this.name = n; } }

List<User> users = Arrays.asList(new User("amy"), new User("bob"));
List<UserDto> dtos = users.stream().map(u -> new UserDto(u.name)).collect(Collectors.toList());
```
Input: `users=[User("amy"), User("bob")]`

Output: `dtos=[UserDto("amy"), UserDto("bob")]`

Production note: Keep mapping pure; avoid calling remote services inside `map`.

## Enterprise example: parse + validate + map at the API boundary
```java
class CreateUserRequest { final String name; CreateUserRequest(String name){ this.name = name; } }
class UserEntity { final String name; UserEntity(String name){ this.name = name; } }

List<CreateUserRequest> reqs = Arrays.asList(
    new CreateUserRequest("amy"),
    new CreateUserRequest(""),
    new CreateUserRequest("bob")
);

List<UserEntity> entities = reqs.stream()
    .map(r -> r.name)
    .map(String::trim)
    .filter(n -> !n.isEmpty())
    .map(UserEntity::new)
    .collect(Collectors.toList());
```
Input: `["amy", "", "bob"]`

Output: `[UserEntity("amy"), UserEntity("bob")]`

Production note: Validation in-stream is fine for simple checks; for complex validation collect errors explicitly.
