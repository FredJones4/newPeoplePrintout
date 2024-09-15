import json
import PyPDF2
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from io import BytesIO

def load_persons(json_file):
    with open(json_file, 'r') as f:
        return json.load(f)

def modify_pdf(input_pdf, output_pdf, persons):
    # Read the PDF
    reader = PyPDF2.PdfReader(input_pdf)
    writer = PyPDF2.PdfWriter()

    # Assume we're working with the first page
    page = reader.pages[0]

    # Extract text from the page
    text = page.extract_text()

    # Split the text into lines
    lines = text.split('\n')

    # Modify the lines
    new_lines = []
    person_index = 0
    for i, line in enumerate(lines):
        if line.startswith('First') and line.endswith('Bold'):
            new_lines.append(line)
        elif line.startswith('First') and 'Normal' in line:
            if person_index < len(persons):
                person = persons[person_index]
                new_line = f"{person['first_name']} {person['last_name']}"
                new_lines.append(new_line)
                person_index += 1
            else:
                new_lines.append(line)
        else:
            new_lines.append(line)

    # Create a new PDF with the modified text
    packet = BytesIO()
    can = canvas.Canvas(packet, pagesize=letter)
    y = 750  # Start from top of the page
    for line in new_lines:
        can.drawString(100, y, line)
        y -= 20  # Move down for next line
    can.save()

    # Move to the beginning of the StringIO buffer
    packet.seek(0)
    new_pdf = PyPDF2.PdfReader(packet)

    # Add the new content to the existing page
    page.merge_page(new_pdf.pages[0])

    # Add the modified page to the writer
    writer.add_page(page)

    # Write the result to a new file
    with open(output_pdf, 'wb') as f:
        writer.write(f)

# Usage
persons = load_persons('persons.json')
modify_pdf('sample.pdf', 'modified_namebadges.pdf', persons)