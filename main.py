import fitz  # PyMuPDF
import json

def get_text_width(text, fontsize, fontname):
    temp_doc = fitz.open()
    temp_page = temp_doc.new_page()
    font = fitz.Font(fontname)
    text_width = font.text_length(text, fontsize)
    temp_doc.close()
    return text_width

def replace_placeholder(page, placeholder, replacement_text, fontsize=12, color=(0, 0, 0), bold=False):
    for inst in page.search_for(placeholder):
        page.draw_rect(inst, color=(1, 1, 1), fill=(1, 1, 1))

        fontname = "helv"

        if bold:
            bold_fontsize = fontsize * 2
            text_width = get_text_width(replacement_text, bold_fontsize, fontname)
            x_center = inst.x0 + (inst.width / 2) - (text_width / 2)
            y_position = inst.y0 + (inst.height / 2) + (bold_fontsize / 4)
            page.insert_text((x_center, y_position), replacement_text, fontsize=bold_fontsize, fontname=fontname, color=color)
        else:
            text_width = get_text_width(replacement_text, fontsize, fontname)
            x_center = inst.x0 + (inst.width / 2) - (text_width / 2)
            y_position = inst.y0 + (inst.height / 2) + (fontsize / 2)
            page.insert_text((x_center, y_position), replacement_text, fontsize=fontsize, fontname=fontname, color=color)

def replace_text_in_pdf(input_pdf_path, output_pdf_path, names_list):
    pdf_document = fitz.open(input_pdf_path)
    new_pdf_document = fitz.open()

    original_page = pdf_document.load_page(0)  # Assuming sample.pdf has only one page

    for i in range(0, len(names_list), 6):
        # Create a new page that's an exact copy of the original
        new_page = new_pdf_document.new_page(width=original_page.rect.width, height=original_page.rect.height)
        new_page.show_pdf_page(new_page.rect, pdf_document, 0)  # 0 is the page number of the original

        # Process up to 6 names for this page
        for j in range(6):
            if i + j < len(names_list):
                name_info = names_list[i + j]
                replace_placeholder(new_page, f"First{j + 1}Bold", name_info['first_name'], fontsize=18, bold=True)
                full_name = f"{name_info['first_name']} {name_info['last_name']}"
                replace_placeholder(new_page, f"First{j + 1}Normal Last{j + 1}", full_name, fontsize=11)

    new_pdf_document.save(output_pdf_path)
    new_pdf_document.close()
    pdf_document.close()

if __name__ == "__main__":
    input_pdf_path = 'C:\\Users\\Owner\\PycharmProjects\\newPeoplePrintout\\sample.pdf'
    output_pdf_path = 'C:\\Users\\Owner\\PycharmProjects\\newPeoplePrintout\\output.pdf'
    json_file_path = 'C:\\Users\\Owner\\PycharmProjects\\newPeoplePrintout\\persons.json'

    with open(json_file_path, 'r') as json_file:
        names_list = json.load(json_file)

    replace_text_in_pdf(input_pdf_path, output_pdf_path, names_list)