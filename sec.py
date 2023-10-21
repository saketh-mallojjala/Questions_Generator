from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from io import StringIO


def extract_text_from_pdf(pdf_path, page_numbers=None):
    resource_manager = PDFResourceManager()
    text_output = StringIO()
    laparams = LAParams()
    converter = TextConverter(resource_manager, text_output, laparams=laparams)
    interpreter = PDFPageInterpreter(resource_manager, converter)

    with open(pdf_path, 'rb') as pdf_file:
        for page in PDFPage.get_pages(pdf_file, page_numbers, check_extractable=True):
            interpreter.process_page(page)

        extracted_text = text_output.getvalue()

    converter.close()
    text_output.close()

    return extracted_text


def save_text_to_file(text, file_path):
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(text)


pdf_path = 'Big Mac Index.pdf'

extracted_text = extract_text_from_pdf(pdf_path)
print('Extracted Text:', extracted_text)
output_file_path = 'Big Mac Index.txt'
save_text_to_file(extracted_text, output_file_path)
