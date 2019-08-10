# person-finder-server

The backend server and image processor for my academic project kodona which is an application to find missing peson.

# Get it running

1. install dependencies
  * ```pip3 install -r requirments.txt```


2. install postgres database
  * create a database named kodona_db
  * create a user named kodona_user password as `password`


3. create the database tables 
  * ```python3 manage.py migrate```


4. run the server 
  * ```python3 manage.py runserver```


5. hit the server at localhost:8000/
