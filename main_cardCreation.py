import json
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import matplotlib.patches as patches

# Define paper size in centimeters (landscape mode)
PAGE_WIDTH = 29.7  # A4 landscape mode width
PAGE_HEIGHT = 21  # A4 landscape mode height
CARD_WIDTH = 7.5  # Card width in cm
CARD_HEIGHT = 10  # Card height in cm

# Define font sizes
LARGE_FONT_SIZE = 40  # Increased size for first name text
SMALL_FONT_SIZE = 16
CORNER_TEXT_SIZE = 10  # Small text size for "BYU 19th Ward"

# Convert from cm to inches for matplotlib
CM_TO_INCH = 0.393701
PAGE_WIDTH_INCH = PAGE_WIDTH * CM_TO_INCH
PAGE_HEIGHT_INCH = PAGE_HEIGHT * CM_TO_INCH
CARD_WIDTH_INCH = CARD_WIDTH * CM_TO_INCH
CARD_HEIGHT_INCH = CARD_HEIGHT * CM_TO_INCH

def load_persons_from_json(json_file):
    """Loads persons from a JSON file and returns a list of (first_name, last_name) tuples."""
    with open(json_file, 'r') as f:
        persons = json.load(f)
    return [(person['first_name'], person['last_name']) for person in persons]

def create_name_card(first_name, full_name, ax):
    """Creates a single name card on a given axis (ax) with a cardboard-cutout outline and "BYU 19th Ward" text"""
    ax.set_xlim(0, CARD_WIDTH)
    ax.set_ylim(0, CARD_HEIGHT)

    # Add a rectangular outline (cardboard-cutout)
    rect = patches.Rectangle((0, 0), CARD_WIDTH, CARD_HEIGHT, linewidth=2, edgecolor='black', facecolor='none', linestyle='dashed')
    ax.add_patch(rect)

    # Add small "BYU 19th Ward" text in the top left corner
    ax.text(
        0.5, CARD_HEIGHT - 0.5, "BYU 19th Ward",
        fontsize=CORNER_TEXT_SIZE,
        ha='left', va='top'
    )

    # Centered first name in large bold font, slightly lower
    ax.text(
        CARD_WIDTH / 2, CARD_HEIGHT / 1.7, first_name,  # Lowered by adjusting CARD_HEIGHT ratio
        fontsize=LARGE_FONT_SIZE, fontweight='bold',
        ha='center', va='center'
    )

    # Full name printed below in smaller font
    ax.text(
        CARD_WIDTH / 2, CARD_HEIGHT / 4, full_name,
        fontsize=SMALL_FONT_SIZE,
        ha='center', va='center'
    )

    ax.axis('off')  # Hide axis

def create_printable_page(persons, file_name):
    """Creates a multi-card PDF for printout, with 2 rows and 2 columns of cards per page"""
    rows_per_page = 2  # Manually set number of rows
    cols_per_page = 2  # Manually set number of columns
    cards_per_page = rows_per_page * cols_per_page

    total_cards = len(persons)
    total_pages = (total_cards + cards_per_page - 1) // cards_per_page  # Calculate number of pages

    # Prepare PDF
    pdf = PdfPages(file_name)

    for page in range(total_pages):
        fig, axes = plt.subplots(
            rows_per_page, cols_per_page,
            figsize=(PAGE_WIDTH_INCH, PAGE_HEIGHT_INCH)
        )

        # Flatten the axes array for easy indexing
        axes = axes.flatten()

        # Reduce the margins between the cards
        fig.subplots_adjust(hspace=0.05, wspace=0.05)  # Small space between cards

        for idx in range(cards_per_page):
            card_idx = page * cards_per_page + idx
            if card_idx >= total_cards:
                # Remove empty axes if no more cards to display
                axes[idx].remove()
                continue

            first_name, last_name = persons[card_idx]
            full_name = f"{first_name} {last_name}"

            create_name_card(first_name, full_name, axes[idx])

        # Save the page to the PDF
        pdf.savefig(fig)
        plt.close(fig)

    pdf.close()

if __name__ == "__main__":
    # Load persons from a JSON file
    persons_file = 'persons.json'
    persons = load_persons_from_json(persons_file)

    # Create the PDF with name cards using 2 rows and 2 columns layout
    create_printable_page(persons, "name_cards_with_larger_first_name.pdf")

    print(f"PDF created with names from '{persons_file}', with larger first name text and 'BYU 19th Ward' text in the top left corner.")
