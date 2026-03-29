# CORRECTION person.py

## 1. def get_age
- ERROR:
    > NameError: name 'datetime' is not defined

- FIXED:
    ```python
    import datetime
    ```
    ***

- FAIL:
    > AssertionError: -24 != 24
    ```python
    return self.yob - now.year
    ```
- FIXED:
    ```python
    return now.year - self.yob
    ```
***
***

## 2. def get_name
- OK
***
***

## 3. def set_name
- FAIL:
    > AssertionError: 'Boby' != None
    ```python
    self.name = self.name
    ```
    > Присваивается старое значение атрибута name, а не переданное значение name
- FIXED:
    ```python
    self.name = name
    ```
***
***

## 4. def set_address
- FAIL:
    > AssertionError: '17 Baker str.' != '101 Miracle Ave.'
    ```python
    self.address == address
    ```
    > Используется оператор сравнения '==', а не присваивания '='
- FIXED:
    ```python
    self.address = address
    ```
***
***

## 5. def get_address
- OK
***
***

## 6. def is_homeless
- ERROR:
    > NameError: name 'address' is not defined
    ```python
    return address is None
    ```
    >Используется переменная address, но должен использоваться атрибут self.address
- FIXED:
    ```python
    return self.address is None or self.address == ''
    ```

