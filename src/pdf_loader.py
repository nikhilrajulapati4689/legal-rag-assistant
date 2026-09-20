import os
import fitz


DOCUMENTS_FOLDER = "documents"

CHUNK_SIZE = 1000
CHUNK_OVERLAP = 200


def load_pdf(pdf_path):

    document = fitz.open(pdf_path)

    pages = []

    for page_number, page in enumerate(document):

        text = page.get_text()

        if text.strip():

            pages.append({
                "text": text,
                "source": pdf_path,
                "page": page_number + 1
            })

    document.close()

    return pages


def load_all_pdfs():

    all_pages = []

    for filename in os.listdir(DOCUMENTS_FOLDER):

        if filename.lower().endswith(".pdf"):

            pdf_path = os.path.join(
                DOCUMENTS_FOLDER,
                filename
            )

            print(f"Loading: {pdf_path}")

            pages = load_pdf(pdf_path)

            all_pages.extend(pages)

    return all_pages


def create_chunks(pages):

    chunks = []

    for page in pages:

        text = page["text"]

        start = 0

        while start < len(text):

            end = start + CHUNK_SIZE

            chunk_text = text[start:end].strip()

            if chunk_text:

                chunks.append({
                    "text": chunk_text,
                    "source": page["source"],
                    "page": page["page"]
                })

            start += CHUNK_SIZE - CHUNK_OVERLAP

    return chunks


if __name__ == "__main__":

    pages = load_all_pdfs()

    print(f"\nTotal pages extracted: {len(pages)}")

    chunks = create_chunks(pages)

    print(f"Total chunks created: {len(chunks)}")