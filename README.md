# FastAPI Student Authentication
***
## create a mysql database name "practice"
## create ".env" file
***
# Copy the following line to the .env file
##### SECRET_KEY=d0edcf1fe0b762a3a3eaf06d49a396f175b29ce3ecd680c61e3a0f94292e206c
##### ALGORITHM=HS256

##### DATABASE_URL=mysql+mysqlconnector://root<your database password>:@localhost:3306/practice
##### URL_ONE=http://localhost:3000
##### URL_TWO=https://localhost:3000
***
## clone the repo using "git clone https://github.com/mahadi025/FastAPI-Auth"
***
### ******** run the following command in the terminal(for linux)*********
### python3 -m venv env
### source env/bin/activate
### pip3 install -r requirements.txt
### cd src
### alembic upgrade head
### python3 main.py
***

### ******** run the following command in the Command Prompt(for windows)*********
### python -m venv env
### env\Scripts\activate
### pip install -r requirements.txt
### cd src
### alembic upgrade head
### python main.py
***
# Goto "http://127.0.0.3:8000" to access the server