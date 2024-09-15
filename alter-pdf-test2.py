import fitz  # PyMuPDF
import json


def replace_placeholder(page, placeholder, replacement_text, fontsize=12, color=(0, 0, 0)):
    # Find all instances of the placeholder
    for inst in page.search_for(placeholder):
        # Draw a white rectangle over the old text (to hide it)
        page.draw_rect(inst, color=(1, 1, 1), fill=(1, 1, 1))

        # Replace with new text using default font
        page.insert_text(inst[:2], replacement_text, fontsize=fontsize, color=color)


def replace_text_in_pdf(input_pdf_path, output_pdf_path, names_list):
    # Open the original PDF
    pdf_document = fitz.open(input_pdf_path)

    for index, name_info in enumerate(names_list):
        # Create a new PDF to write the modified content
        new_pdf_document = fitz.open()

        for page_num in range(len(pdf_document)):
            original_page = pdf_document.load_page(page_num)
            new_page = new_pdf_document.new_page(width=original_page.rect.width, height=original_page.rect.height)

            # Copy content from the original page to the new page
            new_page.show_pdf_page(original_page.rect, pdf_document, page_num)

            # Replace placeholders with actual text
            replace_placeholder(new_page, f"First{index + 1}Bold", name_info['first_name'], fontsize=18)
            replace_placeholder(new_page, f"First{index + 1}Normal", name_info['first_name'], fontsize=11)
            replace_placeholder(new_page, f"Last{index + 1}", name_info['last_name'], fontsize=11)

        # Save the new PDF
        new_pdf_document.save(output_pdf_path)
        new_pdf_document.close()

    # Close the original PDF
    pdf_document.close()


if __name__ == "__main__":
    input_pdf_path = 'C:\\Users\\Owner\\PycharmProjects\\newPeoplePrintout\\sample.pdf'
    output_pdf_path = 'C:\\Users\\Owner\\PycharmProjects\\newPeoplePrintout\\output.pdf'
    json_file_path = 'C:\\Users\\Owner\\PycharmProjects\\newPeoplePrintout\\persons.json'

    with open(json_file_path, 'r') as json_file:
        names_list = json.load(json_file)

    replace_text_in_pdf(input_pdf_path, output_pdf_path, names_list)
