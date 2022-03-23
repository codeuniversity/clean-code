# Session 3
These are the code examples for the [Clean Code Quiz](https://docs.google.com/forms/d/e/1FAIpQLSe6-tVU769ID0wqwe2cELDEpXl7WW_Uk7JaruoEuPndiTPaEA/viewform)

## Example 1

```python
class Queue:
def __init__(self):

def is_empty(self):

def pop(self):

def push(self, elem):

def clear(self):

def peek(self):

def size(self):
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

```javascript
function createAButton(backgroundColor="red") {
    let button = document.createElement("button");
    button.innerHTML = "Do Something";
    let body = document.getElementsByTagName("body")[0];
    body.appendChild(button);

    button.style.background = backgroundColor;

    button.addEventListener ("click", function() {
        alert("did something");
    });
}
[...]

# Usage
if curUser.message == "Hello") {
    createAButton(user.customColor);
} else {
    createAButton();
}
```





