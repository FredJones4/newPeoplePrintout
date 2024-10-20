import json


def update_persons_with_title(input_file, output_file):
    """
    This function is designed to take persons.json, which has firstname and lastname, and add a title for those in leadership.
    This function specifically is only for
    :param input_file: persons.json
    :param output_file: persons_and_tile.json
    :return:
    """
    # Read the original JSON data
    with open(input_file, 'r') as file:
        persons = json.load(file)

    # Define a list of titles to cycle through or any other logic for title assignment
    titles = ['', '']
    for index, person in enumerate(persons):
        # Example logic: Assign titles alternately, can be changed as needed
        title_index = index % len(titles)
        person['title'] = titles[title_index]

    # Write the updated data to a new JSON file
    with open(output_file, 'w') as file:
        json.dump(persons, file, indent=4)


# Usage
input_file = 'persons.json'
output_file = 'persons_and_title.json'
update_persons_with_title(input_file, output_file)
