# Pybok

The Python library to remove all the boilerplate from your code — inspired in https://projectlombok.org/ 🔥

## Installation

```bash
pip install pybok
```

## Usage

There are multiple useful decorators.

### ArgsConstructor

```python
@ArgsConstructor
class Student:
    name: str
    age: int

student = Student("John", 21)

print(student._name) # John
print(student._age) # 21
```

### Getter

```python
@Getter
@ArgsConstructor
class Student:
    name: str
    age: int

student = Student("John", 21)

print(student.name) # John
print(student.age) # 21
```

### Setter

```python
@Setter
@ArgsConstructor
class Student:
    name: str
    age: int

student = Student("John", 21)

student.name = "Jane"
student.age = 19

print(student._name("Jane")) # Jane
print(student._age_(19)) # 19
```

### Data

```python
@Data
class Person:
    name: str
    age: int

p1 = Person("John", 21)

print(p1) # 'Person(name=John,age=21)'

print(p1.name) # John
print(p1.age) # 21

print((hash(p1), hash((p1._name, p1._age))) # True

p1.name = "Mike"
p1.age = 28

print(p1._name) # Mike
print(p1.get_age()) # 28
```

### Builder

```python
@Builder
@ArgsConstructor
class Person:
    name: str
    age: int

person = Person.builder().name("John").age(23).build()

print(person._name) # John
print(person._age # 23
```

### EqualsAndHashCode

```python
@EqualsAndHashCode
@ArgsConstructor
class Person:
    name: str
    age: int

p1 = Person("John", 21)

print(hash(p1) == hash((p1._name, p1._age))) # True

p2 = Person("Jane", 19)

print(p1 == p2) # False
print(p1 == p1) # True
```

### ToString

```python
@ToString
@ArgsConstructor
class Person:
    name: str
    age: int

person = Person("John", 21)

print(person) # Person(name=John,age=21)
```

### ToJSON

```python
@ToJSON
@ArgsConstructor
class Person:
    name: str
    age: int

person = Person("John", 21)

print(person.json()) # {"name": "John", "age": 21} but pretty
```

### Singleton

```python
@Singleton
@ArgsConstructor
class Person:
    name: str
    age: int

john = Person("John", 21)
jane = Person("Jane", 19)
empty = Person()

print(john == jane) # True
print(john == empty) # True
```

### UtilityClass

```python
@UtilityClass
class MyClass:
    def utility_method():
        # whatever you need

MyClass() # raises exception (cannot instantiate)
```

### With

```python
@With
@ArgsConstructor
class Person:
    name: str
    age: int

person = Person("Jane", 19)
same = person.with_name("Jane")
another = person.with_age(21)
        
print(person == same) # True
print(person == another) # False  
```

### Copy

```python
@ArgsConstructor
class Eyes:
    color: str

@Copy
@ArgsConstructor
class Person:
    name: str
    age: int
    eyes: Eyes  

person = Person("Jane", 19, Eyes("blue"))

shallow_copy = person.copy()
deep_copy = person.deepcopy()

print(person._name == shallow_copy._name) # True
print(person._age == shallow_copy._age) # True
print(person._eyes == shallow_copy._eyes) # True

print(person._name == deep_copy._name) # True
print(person._age == deep_copy._age) # True
print(person._eyes == deep_copy._eyes) # False
```

### Log

```python
@Log
@ArgsConstructor
class Person:
    name: str
    age: int

    def greet(self):
        self.logger.info("{name} greets")

@Log
@ArgsConstructor
class Cat:
    name: str
    age: int

    def meow(self):
        self.logger.warning(f"{name}" meows!)

person = Person("Jane", 19)

person.greet() # 2005-03-23 23:47:11,663 - pybok_app - INFO - Jane greets

cat = Cat("Tom", 8)

cat.meow() # 2005-03-23 23:47:11,663 - pybok_app - WARN - Tom meows

print(person.logger == cat.logger) # True
```

### ConfigurationProperties

Reads any environment variable that you require. Supports default values as well.

Also, you can make it a singleton to inject it wherever you want by using the `@Singleton`.

```python
os.environ[self.DAY] = "1"
os.environ[self.MONTH] = "10"

@Singleton
@ConfigurationProperties
class MyProps:
    day: str
    month: str
    year: str = '1991'

myprops = MyProps()

print(myprops._day) # 1
print(myprops._month) # 10
print(myprops._year) # 1991

my_other_props = MyProps()

print(myprops == my_other_props) # True
```

## Contribution

Please read [CONTRIBUTION.md](CONTRIBUTION.md).

## Code of Conduct

Please read the [Contributor Covenant Code of Conduct](CODE_OF_CONDUCT.md).

## License

This project is licensed under the [MIT License](LICENSE).