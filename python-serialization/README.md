##Projects

###task_00_basic_serialization.py

Create a basic serialization module that adds the functionality to serialize a Python dictionary to a JSON file and deserialize the JSON file to recreate the Python Dictionary.

- The function serialize_and_save_to_file take 2 parameters:

 - data: A Python Dictionary with data
 - filename: The filename of the output JSON file. If the output file already exists it should be replaced.
- The function load_and_deserialize take 1 parameters:

 - filename: The filename of the input JSON file This function returns a Python Dictionary with the deseialized JSON data from the file.