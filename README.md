# ChitChatPY 

This is a unit test for python. It is a clone of the early version of the NodeJS version.

# Installation

In your terminal, please do:

``` bash
pip install ChitChatPY
```
When you've done that, you have installed ChitChatPY!

# Usage

In your code, at the top please put:

``` python
from ChitChatPY import TestCase
```

Then, put:

``` python
def add(num1, num2):
  return num1 + num2
myTest = TestCase('My first test', add(3, 4))
myTest.expectToBe(7)
```

And then your test should pass! While this test is easy, yours and be very long and complex!
