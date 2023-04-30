from fastapi import FastAPI, Path, Query

app = FastAPI() #creating an instance of the fast api object so it can be used later

students = {
    1:{
    "name": "john",
    "age": 17,
    "class": "year 12"
    }
}

@app.get("/") #create an endpoint- one end of a communication channel - the path e.g. amazon.com/(CREATE-USER), there are GET (Get information), POST (Create something new), PUT (update data) and DELETE (delete data)
def index():
    return {"name": "First Data"}

#To run the program: this is what you do: uvicorn myapi:app --reload  #If you do /docs you can test the API
#The path parameter (e.g. google.com/get-student) is a parameter that the user can input 1 for id of 1 in the dictionary

@app.get("/get-student/{student_id}")#The endpoint path parameter will be what the user entered in the url, so if they input 1, it will return the student with key 1
def get_student(student_id: int = Path(description="The ID of the student you would like to view", gt=0, lt=3 )):#You have to define the data type #The none is so that it is empty incase the user doesn't add any data #We can specify what we want the integar we are collecting to be greater than 0
    return students[student_id]

#gt = greater than, lt = less than, ge = greater than or equal to, le = less than or equal to