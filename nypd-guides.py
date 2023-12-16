import fitz  # imports the pymupdf library
import os


def extract_text_from_pdf(pdf_file_path) -> str:
    pdf_text = ""
    with fitz.open(pdf_file_path) as doc:  # open a document
        for page in doc:  # iterate the document pages
            pdf_text = pdf_text + page.get_text()  # get plain text encoded as UTF-8

    pdf_text = pdf_text.replace("NEW  YORK  CITY  POLICE  DEPARTMENT", "")
    pdf_text = pdf_text.replace("\t", "")
    pdf_text = pdf_text.replace("\r", "")
    pdf_text = pdf_text.replace("\r\n", "")
    pdf_text = pdf_text.strip()
    return pdf_text


def list_files(directory) -> list:
    for root, dirs, files in os.walk(directory):
        pass
        # for file in files:
        #     print(os.path.join(root, file))
    return files


def save_text_to_file(directory, file_name, text) -> None:
    with open(directory + file_name[:-3] + "txt", "w") as f:
        f.write(text)


if __name__ == "__main__":
    pdf_directory = "./pdf-manuals/"
    text_directory = "./txt-manuals/"

    list_of_files = list_files(pdf_directory)

    for file in list_of_files:
        file_text = extract_text_from_pdf(pdf_directory + file)
        save_text_to_file(text_directory, file, file_text)
