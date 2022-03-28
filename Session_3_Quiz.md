# Session 3 Code Examples

## Example 1

```python
class Rectangle:
   height: float
   width: float

def calc_area(rectangle: Rectangle):
   return rectangle.height * rectangle.width
```

## Example 2

Hint: If you don't know what a dot product is, quickly google it.

```python
def calc_dot_product(x1, y1, z1, x2, y2, z2):
   return x1*x2 + y1*y2 + z1*z2

def are_orthogonal(x1, y1, z1, x2, y2, z2):
   return calc_dot_product(x1, y1, z1, x2, y2, z2) == 0
```

## Example 3

A queue is a data structure that allows elements to be retrieved in the order of insertion ('FIFO' - first in first out). The following example implements a queue in python.

```python
class Queue:
    def __init__(self):
        self.__elements = []

    def is_empty(self):
        return len(self.__elements) == 0

    def pop(self):
        return self.__elements.pop(0)

    def push(self, elem):
        self.__elements.append(elem)

    def clear(self):
        self.__elements = []

    def peek(self):
        return self.__elements[0]

    def size(self):
        return len(self.__elements)
```

## Example 4

```javascript
function createAButton(user) {
    let button = document.createElement("button");
    button.innerHTML = "Do Something";
    let body = document.getElementsByTagName("body")[0];
    body.appendChild(button);

    if(user.message == "Hello") {
        button.style.background = user.customColor;
    } else {
        button.style.background = "red";
    }

    button.addEventListener ("click", function() {
        alert("did something");
    });
}
[...]

# Usage
createAButton(curUser);
```


