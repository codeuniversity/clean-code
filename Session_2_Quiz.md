# Session 2
These are the code examples for the [Clean Code Quiz](https://docs.google.com/forms/d/1mgwag0RiKLELmxFwQkzuxUDyMZ0QVKZWWnBi9Eo5Tqg/viewform). 

For each example, look at the code and list bad smells. If you have an idea, describe how you would improve the code as well. Most - but not all - smells are listed in the Refactoring book. If you can, use Fowler's names for the smells.

## Example 1

```javascript
var d; // elapsed time in days
```


## Example 2

```python
// Subtract discount from price.
finalPrice = (numItems * itemPrice) - min(5, numItems) * itemPrice * 0.1
```

## Example 3

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


## Example 4

```javascript
function calculateTotal(priceA, priceB, taxRate) {
    let total = priceA
    total += priceB
    total *= taxRate
    return total
}
```


## Example 5

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
   server.starttls(context = context)  # Secure the connection
   server.login(sender_email, password)
   server.sendmail(sender_email, email_address, email_message)
```


## Example 6

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
response = server.Call(request)
 
if response.GetStatus() == RPC.OK:
  if response.GetAuthorizedUser():
    if response.GetEnc() == 'utf-8':
      if response.GetRows():
        vals = [ParseRow(r) for r in response.GetRows()]
        avg = sum(vals) / len(vals)
        return avg, vals
      else:
        raise EmptyError()
    else:
      raise AuthError('unauthorized')
  else:
    raise ValueError('wrong encoding')
else:
  raise RpcError(response.GetStatus())
```


## Example 8: Bonus

Is this code clean? Why/why not?

[Explanation of what this code does](https://betterexplained.com/articles/understanding-quakes-fast-inverse-square-root/)

```C
float InvSqrt(float x){
    float xhalf = 0.5f * x;
    int i = *(int*)&x;            // store floating-point bits in integer
    i = 0x5f3759df - (i >> 1);    // initial guess for Newton's method
    x = *(float*)&i;              // convert new bits into float
    x = x*(1.5f - xhalf*x*x);     // One round of Newton's method
    return x;
}
