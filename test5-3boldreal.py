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
        text_width = get_text_width(replacement_text, fontsize, fontname)

        x_center = inst.x0 + (inst.width / 2) - (text_width / 2)
        y_position = inst.y0 + (inst.height / 2) + (fontsize / 2)

        if bold:
            # Draw text twice with slight offset to simulate bold
            page.insert_text((x_center - 0.5, y_position - 0.5), replacement_text, fontsize=fontsize, fontname=fontname,
                             color=color)
            page.insert_text((x_center + 0.5, y_position + 0.5), replacement_text, fontsize=fontsize, fontname=fontname,
                             color=color)
        else:
            page.insert_text((x_center, y_position), replacement_text, fontsize=fontsize, fontname=fontname,
                             color=color)


def replace_text_in_pdf(input_pdf_path, output_pdf_path, names_list):
    pdf_document = fitz.open(input_pdf_path)
    new_pdf_document = fitz.open()

    for page_num in range(len(pdf_document)):
        original_page = pdf_document.load_page(page_num)
        new_page = new_pdf_document.new_page(width=original_page.rect.width, height=original_page.rect.height)
        new_page.show_pdf_page(original_page.rect, pdf_document, page_num)

        for index, name_info in enumerate(names_list):
            replace_placeholder(new_page, f"First{index + 1}Bold", name_info['first_name'], fontsize=18, bold=True)

            full_name = f"{name_info['first_name']} {name_info['last_name']}"
            replace_placeholder(new_page, f"First{index + 1}Normal Last{index + 1}", full_name, fontsize=11)

        if index < len(names_list) - 1 and (index + 1) % 6 == 0:
            new_pdf_document.new_page(width=original_page.rect.width, height=original_page.rect.height)

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