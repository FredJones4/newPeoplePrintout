import json
"""
Counts the number of items in the given json. 
Note that the complete json file path needs to be added to the variable json_file_path.
"""
# Path to your JSON file
json_file_path = 'C:\\Users\\Owner\\PycharmProjects\\newPeoplePrintout\\persons.json'


def count_json_objects(file_path):
    """Count the number of objects in a JSON file."""
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)

            # Assuming the JSON file contains a list of objects
            if isinstance(data, list):
                return len(data)
            else:
                print("JSON file does not contain a list of objects.")
                return 0

    except FileNotFoundError:
        print("The specified file was not found.")
        return 0
    except json.JSONDecodeError:
        print("Error decoding JSON.")
        return 0


# Count and print the number of objects
num_objects = count_json_objects(json_file_path)
print(f"Number of objects in {json_file_path}: {num_objects}")
