## Note for Coding Python

1. The difference when read **bytes file with 'rb'**  between *Python2* and *Python3*

   Noted that when you read a binary file in Python2

   ```python
   file = open('/path/to/binary/file','rb')
   head = file.readline()
   type(head) # is string
   ```

    But in Python3

   ```python
   file = open('/path/to/binary/file','rb')
   head = file.readline()
   type(head) # is bytes
   ```

   So, when you need to turn it to ***string***, you can refer to the codes bellow to **add encoding**

   ```python
   # bytes object
   b = b"example"
   
   # str object
   s = "example"
    
   # str to bytes
   bytes(s, encoding = "utf8")
    
   # bytes to str
   str(b, encoding = "utf-8")
    
   # an alternative method
   # str to bytes
   str.encode(s)
    
   # bytes to str
   bytes.decode(b)
   ```

   

2.  

3.  

4. 