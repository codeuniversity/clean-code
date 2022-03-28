# Session 3 Code Examples

## Example 1

A queue is a data structure that allows elements to be retrieved in the order of insertion ('FIFO' - first in first out). The following example implements a queue in python.

```python
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


## Example 2

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


## Example 3



