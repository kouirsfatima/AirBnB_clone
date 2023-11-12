# AirBnB clone - The console
The AirBnB clone project starts now until… the end of the first year. The goal of the project is to deploy on your server a simple copy of the AirBnB website.
Steps:
- create your data model
- manage (create, update, destroy, etc) objects via a - - - - - console / command interpreter
store and persist objects to a file (JSON file)
The first piece is to manipulate a powerful storage system. This storage engine will give us an abstraction between “My object” and “How they are stored and persisted”. This means: from your console code (the command interpreter itself) and from the front-end and RestAPI you will build later, you won’t have to pay attention (take care) of how your objects are stored.

This abstraction will also allow you to change the type of storage easily without updating all of your codebase.

The console will be a tool to validate this storage engine
## File Description:
console.py: that contains the entry point of the command interpreter
quit and EOF to exit the program
create:  Creates a new instance of BaseModel, saves it (to the JSON file) and prints the id
show:Prints the string representation of an instance based on the class name and id
destroy:Deletes an instance based on the class name and id
all :Prints all string representation of all instances based or not on the class name
update:: Updates an instance based on the class name and id by adding or updating attribute
## the class: base_model.py .
base_model.py - The BaseModel class from which future classes will be derived
## the methode thas use in class base_model.py
def __init__(self, *args, **kwargs) - Initialization of the base model
def __str__(self) - String representation of the BaseModel class
def save(self) - Updates the attribute updated_at with the current datetime
def to_dict(self) - returns a dictionary containing all keys/values of the instance
## file_storage.py
file_storage.py - serializes instances to a JSON file & deserializes back to instances
## the methode thas use in file_storage.py
def all(self) - returns the dictionary __objects
def new(self, obj) - sets in __objects the obj with key .id
def save(self) - serializes __objects to the JSON file (path: __file_path)
 def reload(self) - deserializes the JSON file to __objects
 ## Classes inherited from Base Model:
    - amenity.py
    - city.py
    - place.py
    - review.py
    - state.py
    - user.py
## tests : this directory contains all tests
## test_BaseModel.py
- def test_BaseModel(self):  this methode test the  attributes existance and  Methodes existance  and 
type test
- def test_str(self): test correct output for str method
- def test_save(self): test for save method
## test_amenity.py
test_amenity.py - Contains the TestAmenityDocs class
- def test_amenity(self): this methode test existince and type test 
## test_city.py
- def test_city(self): this methode test existince and type test 
##  test_place.py
-  def test_place(self): this methode test existince and type test 
## test_review.py
-  def test_review(self): this methode test existince and type test 
## test_state
-  def test_state(self): this methode test existince and type test 
## test_user.py
-  def test_user(self): this methode test existince and type test 
