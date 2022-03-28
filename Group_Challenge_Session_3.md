# Session 3: Social Media Platform Example 
This is the code example for the [Clean Code Social_Media_Platform_Challenge](https://docs.google.com/forms/d/e/1FAIpQLSfWlOHMUhS9XW1XHYC569p7mibWcv91iB5EBf1Bt-Vv8pwRxw/viewform)

```python
import datetime
import post_database

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

