import fitz  # PyMuPDF


def replace_text_in_pdf(input_pdf, output_pdf, target_name, replacement_name):
    # Open the input PDF
    pdf_document = fitz.open(input_pdf)

    # Iterate through each page of the PDF
    for page_num in range(len(pdf_document)):
        page = pdf_document[page_num]
        text_instances = page.search_for(target_name)

        # Iterate through all instances where the target name is found
        for inst in text_instances:
            # Convert tuple to list for color
            white_fill = [1, 1, 1]  # RGB color values between 0 and 1 for white

            # Redact the old text (replace with a white rectangle)
            page.add_redact_annot(inst, fill=white_fill)
            page.apply_redactions()

            # Insert the new text at the same location
            page.insert_text(inst[:2], replacement_name, fontsize=12, color=(0, 0, 0))  # Insert new text in black

    # Save the modified PDF
    pdf_document.save(output_pdf)
    pdf_document.close()


if __name__ == "__main__":
    input_pdf_path = r"C:\Users\Owner\Downloads\Avery5392NameBadgesInsertRefills.pdf"
    output_pdf_path = r"C:\Users\Owner\Downloads\Updated_Avery5392NameBadgesInsertRefills.pdf"

    replace_text_in_pdf(input_pdf_path, output_pdf_path, "John", "Jane")
