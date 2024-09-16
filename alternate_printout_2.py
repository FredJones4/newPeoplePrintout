from reportlab.lib.pagesizes import letter, landscape
from reportlab.lib import colors
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
import json

# Load the persons.json file
with open('persons.json') as f:
    persons = json.load(f)

def draw_card(c, x, y, first_name, full_name):
    """Draw a single card on the canvas."""
    card_width = 4 * inch  # 4 inches wide in landscape mode
    card_height = 3 * inch  # 3 inches tall

    # Draw card outline
    c.setStrokeColor(colors.black)
    c.rect(x, y, card_width, card_height)

    # Add the small text in the top left
    c.setFont("Helvetica", 8)
    c.drawString(x + 0.1 * inch, y + card_height - 0.3 * inch, "BYU 19th Ward")

    # Add the first name in the center, lowered by a character space
    c.setFont("Helvetica-Bold", 50)  # Double the original size
    first_name_width = c.stringWidth(first_name, "Helvetica-Bold", 50)
    c.drawString(x + (card_width - first_name_width) / 2, y + 2 * inch, first_name)

    # Add the full name below
    c.setFont("Helvetica", 16)
    full_name_width = c.stringWidth(full_name, "Helvetica", 16)
    c.drawString(x + (card_width - full_name_width) / 2, y + 0.5 * inch, full_name)

def create_name_card_pdf(persons):
    """Generate a PDF with name cards for the given persons in landscape mode."""
    c = canvas.Canvas("name_cards_landscape.pdf", pagesize=landscape(letter))

    # Define the number of rows and columns (2x2 layout)
    cols = 2
    rows = 2
    card_width = 4 * inch
    card_height = 3 * inch
    margin_x = 0.5 * inch  # Adjust margins if necessary
    margin_y = 0.75 * inch

    # Track the current card position
    page_cards = 0

    for i, person in enumerate(persons):
        col = page_cards % cols
        row = page_cards // cols

        # If we need to start a new page after 4 cards
        if page_cards >= rows * cols:
            c.showPage()
            page_cards = 0  # Reset the page card counter
            col = 0
            row = 0

        # Calculate the position of the card
        x = margin_x + col * (card_width + margin_x)
        y = landscape(letter)[1] - margin_y - (row + 1) * (card_height + margin_y)

        # Draw the card
        first_name = person['first_name']
        full_name = f"{person['first_name']} {person['last_name']}"
        draw_card(c, x, y, first_name, full_name)

        page_cards += 1  # Move to the next card

    c.save()

# Call the function to create the PDF
create_name_card_pdf(persons)
