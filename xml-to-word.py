import zipfile
import os


def create_docx_from_xml(xml_file, output_docx):
    # Create a new zip file with a .docx extension
    with zipfile.ZipFile(output_docx, 'w') as docx_zip:
        # Add the XML file to the ZIP archive
        docx_zip.write(xml_file, 'word/theme/theme1.xml')

        # Add minimal required content to make it a valid .docx file
        # Note: This is a minimal example, and a real .docx file has several required components.
        # The full structure can be complex and should be replicated properly.

        # Create word directory and add other necessary files
        docx_zip.writestr('word/document.xml', '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
                                               '<w:document xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">'
                                               '<w:body><w:p><w:r><w:t>Hello World</w:t></w:r></w:p></w:body></w:document>')

        docx_zip.writestr('word/_rels/document.xml.rels', '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
                                                          '<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">'
                                                          '</Relationships>')

        docx_zip.writestr('[Content_Types].xml', '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
                                                 '<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">'
                                                 '<Default Extension="xml" ContentType="application/xml"/>'
                                                 '<Override PartName="/word/document.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.document.main+xml"/>'
                                                 '<Override PartName="/word/theme/theme1.xml" ContentType="application/vnd.openxmlformats-officedocument.theme+xml"/>'
                                                 '</Types>')


if __name__ == "__main__":
    xml_file = 'sample.docx'
    output_docx = 'output.docx'
    create_docx_from_xml(xml_file, output_docx)
