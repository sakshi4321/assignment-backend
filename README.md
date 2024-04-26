# assignment-backend


To run the assignment :

Run the following commands in a terminal:
`psql`
`CREATE ROLE newuser WITH LOGIN PASSWORD 'password';`
`CREATE DATABASE postgres;`
`GRANT ALL PRIVILEGES ON DATABASE postgres TO newuser;`

Open a Terminal and run the following commands(runs on port 8000):

`pip install -r requirements.txt`

`python3 manage.py makemigrations`

`python3 manage.py migrate`

`python3 manage.py runserver`


You can access the documentation at 

`http://127.0.0.1:8000/swagger/`