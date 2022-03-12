# Session 2
These are the code examples for the [Clean Code Quiz](https://docs.google.com/forms/d/1mgwag0RiKLELmxFwQkzuxUDyMZ0QVKZWWnBi9Eo5Tqg/edit)

## Example 1

```javascript
var d; // elapsed time in days
```

## Example 2

```python
def check_user_array(user):
   if user['data']['name']['first']:
       first_name = user['data']['name']['first']
   else:
       if user['data']['name']['last']:
           return user['data']['name']['last']
   if user['data']['name']['last']:
       last_name = user['data']['name']['last']
       if user['data']['name']['first']:
           return first_name + ' ' + last_name
   else:
       if user['data']['name']['first']:
           return first_name
       else:
           return ''
```

## Example 3

```javascript
function calculateTotal(priceA, priceB, taxRate) {
    let total = priceA
    total += priceB
    total *= taxRate
    return total
}
```


## Example 4

```python
class Rectangle:
   height: float
   width: float

def calc_area(rectangle: Rectangle):
   return rectangle.height * rectangle.width
```


## Example 5

```python
def calc_dot_product(x1, y1, z1, x2, y2, z2):
   return x1*x2 + y1*y2 + z1*z2

def are_orthogonal(x1, y1, z1, x2, y2, z2):
   return calc_dot_product(x1, y1, z1, x2, y2, z2) == 0
```


## Example 6

```python
def log_items_and_send_receipts(items, email_address):
   total_price = 0
   for item in items:
       price = item.price * 1.16
       total_price += price
   
   for item in items:
       print('Item ID:', item.id)
       print('Item Name:', item.name)
       print('Item price:', item.price)
   print('Email: ' + email_address)
   print('Total', total_price)

   email_message = 'New Order! Total price' + str(total_price)
   server = smtplib.SMTP(smtp_server, port)
   server.starttls(context=context)  # Secure the connection
   server.login(sender_email, password)
   server.sendmail(sender_email, email_address, email_message)
```


## Example 7

```python
GAME_BOARD = [...] # list of cells, each cell is a dict

def get_flagged_cells() -> List[any]:
   flagged_cells = []
   for cell in GAME_BOARD:
       if cell['STATUS_VALUE'] == FLAGGED:
           flagged_cells.append(cell)

   return flagged_cells
```

## Example 7

```python
GAME_BOARD = [...] # list of cells, each cell is a dict

def get_flagged_cells() -> List[any]:
   flagged_cells = []
   for cell in GAME_BOARD:
       if cell['STATUS_VALUE'] == FLAGGED:
           flagged_cells.append(cell)

   return flagged_cells
```


## Example 8

```javascript
function checkIfUserExists(userinput) {
    if (userinput === null) {
        return false;
    }

    checkUser(userinput);
    calculateProfileStyles();

    const profileData = new FormData();
    const profileField = document.querySelector('input[type="file"]');

    profileData.append('username', userinput.name);
    profileData.append('avatar', profileField.files[0]);
    return profileData;
}
```

