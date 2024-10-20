
# Name to Nametags

This project automates the creation of name tags by converting names listed in a JSON file into a PDF format suitable for printing. Specifically, it is designed to work with pre-cut papers following our pdf format requirements. Alternative pdf printouts are given in '''alternate_printout_1''' and '''alternate_printout_2'''.

## Features

- **Custom PDF Generation**: Converts names from a JSON file into a formatted PDF designed to align with Sister Parkin's pre-cut nametag papers.
- **Flexible Data Input**: Supports names with or without titles through different JSON structures.
- **Output Customization**: Generates `output.pdf` which is stored in the current directory and can be directly printed.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

What things you need to install the software and how to install them:

- Python 3.x
- Required Python libraries: [list any libraries that your script depends on, e.g., `PyPDF2`, `reportlab`]

```bash
pip install PyPDF2 reportlab
```

### Installation

Clone the repository to your local machine:

```bash
git clone https://github.com/FredJones4/newPeoplePrintout.git
cd newPeoplePrintout
```

### Setup

Before running the script, make sure to update the paths to `input.pdf`, `output.pdf`, and the JSON files in `main.py` to correspond with the file locations on your computer.

### Usage

1. **Prepare your JSON file**:
   - Use `persons.json` to list names without titles.
   - Use `persons_and_title.json` for names with titles. Generate this file using `create-persons-with-name-json.py` if necessary.

2. **Run the Script**:
   ```bash
   python main.py
   ```
   This command will generate `output.pdf` in the current directory.

3. **Print `output.pdf`**:
   Ensure your printer is set up with Sister Parkin's pre-cut papers and print `output.pdf`.

## File Descriptions

- **main.py**: The main script that reads the names, formats them, and outputs the `output.pdf`.
- **persons.json**: JSON file where names are stored for conversion to name tags.
- **persons_and_title.json**: Alternative JSON file that includes titles along with names.
- **create-persons-with-name-json.py**: Utility script to create `persons_and_title.json` from `persons.json`.

## Versioning

We use [Git](https://git-scm.com/) for version control. For the versions available, see the [tags on this repository](https://github.com/yourusername/nametotags/tags).

## Authors

- **Christian Hales** - *Initial work* - [FredJones4](https://github.com/FredJones4)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE) file for details

## Acknowledgments

- Thanks to Sister Parkin for her specific format requirements which guided the design of this software.

---

Make sure to adjust the installation commands, repository URL, and other details according to your actual project setup. This `README.md` provides a complete overview and should be helpful to anyone looking to use or contribute to your project.
