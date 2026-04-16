##Projects

###task_00_basic_serialization.py

Create a basic serialization module that adds the functionality to serialize a Python dictionary to a JSON file and deserialize the JSON file to recreate the Python Dictionary.

- The function serialize_and_save_to_file take 2 parameters:

 - data: A Python Dictionary with data
 - filename: The filename of the output JSON file. If the output file already exists it should be replaced.
- The function load_and_deserialize take 1 parameters:

 - filename: The filename of the input JSON file This function returns a Python Dictionary with the deseialized JSON data from the file.

###task_01_pickle.py.

Create a custom Python class named CustomObject. This class should have the following attributes:

- name (a string)

- age (an integer)

- is_student (a boolean)

Implement two methods within this class:

- serialize(self, filename): This method will take a filename as its parameter. Using the pickle module, it will serialize the current instance of the object and save it to the provided filename.
- @classmethod deserialize(cls, filename): This class method will take a filename as its parameter. Using the pickle module, it will load and return an instance of the CustomObject from the provided filename.
