# Session 3: Group Challenge 
These are the code examples for the [Clean Code Social_Media_Platform_Challenge](https://docs.google.com/forms/d/e/1FAIpQLSfWlOHMUhS9XW1XHYC569p7mibWcv91iB5EBf1Bt-Vv8pwRxw/viewform)

## Example 1 (Social Media Platform)

```python
import datetime
import post_database
from PIL import Image

class Post:
    def __init__(self, author: str, text: str, image: Image.Image, date: datetime.date):
        self.author = author
        self.text = text
        self.date = date
        self.image = image

        db_connection = post_database.get_connector() # returns a MySQL connection
        mycursor = db_connection.cursor()
        sql = "INSERT INTO posts (author, text, date) VALUES (%s, %s, %s)"
        val = (self.author, self.text, self.date.isoformat())
        mycursor.execute(sql, val)
        db_connection.commit()

    def get_author(self) -> str:
        return self.author

    def get_text(self) -> str:
        return self.text

    def get_image(self) -> Image.Image:
        return self.image

    def get_date(self) -> datetime.date:
        return self.date
```


## Bonus: State Machine

```python
import subprocess
import os

    from typing import List

class StateMachine:
def __init__(self):
self.__states = {}


def add_state(self, name: str, transitions: List[str]):
if name in self.__states:
raise Exception("StateMachine: Duplicate state " + name + ".")
if not self.__states:
self.__cur_state = name
self.__states[name] = transitions

def change_state(self, new_state: str):
self.__do_sanity_check()

if not self.__is_state(new_state):
raise Exception('StateMachine: Attempt to change to nonexistent state ' +
    new_state + '.')
if not new_state in self.__states[self.__cur_state]:
raise Exception('StateMachine: State change from ' + self.__cur_state + ' to ' +
    new_state + ' not allowed.')
self.__cur_state = new_state

def get_state(self):
return self.__cur_state

def dump(self):
for state, transitions in self.__states.items():
print(state)
for transition in transitions:
print("  -->", transition)
print("Current state:", self.__cur_state)

def make_diagram(self, file_name: str, title: str):
def write_state(state_name):
dot_file.write('	"' + state_name + '" [label=<' + state_name + '>];\n')

def write_transition(orig_state, dest_state):
dot_file.write('	"' + orig_state + '" -> "' + dest_state + '"')
dot_file.write(";\n")

dot_file = open("tmp.dot", "w")
dot_file.write('digraph "' + title + '" {\n')
dot_file.write('	node [fontsize=12, shape=box, style=rounded];\n')
dot_file.write('	startstate [shape=point, height=0.2, width=0.2, label=""];\n')
dot_file.write('	{ rank=source; "startstate" };\n')
for state, transitions in self.__states.items():
write_state(state)
for dest_state in transitions:
write_transition(state, dest_state)
dot_file.write('	"' + self.__cur_state + '" [style="rounded,bold"];\n')
dot_file.write('}\n')
dot_file.close()
try:
subprocess.call(["dot", "tmp.dot", "-Tpng", "-o" + file_name])
except FileNotFoundError:
    raise Exception(
    "dot executable not found. graphviz needs to be installed for StateMachine.makeDiagram to work.")
os.remove("tmp.dot")

def __is_state(self, state: str):
return state in self.__states

def __do_sanity_check(self):
for state, transitions in self.__states.items():
for transition in transitions:
if not (self.__is_state(transition)):
raise Exception("StateMachine: transition " + state + " -> " +
    transition + " has an unknown destination state.")


# Usage example
machine = StateMachine()
machine.add_state("A", ["B", "C"])
machine.add_state("B", ["D"])
machine.add_state("C", ["A"])
machine.add_state("D", [])

machine.change_state("B")
machine.dump()

machine.make_diagram("diagram.png", "TestMachine")
```



