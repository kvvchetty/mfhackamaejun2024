import PyPDF2
import re
import spacy
import en_core_web_sm

def read_pdf(pdf_path):
    with open(pdf_path, 'rb') as pdf_file:
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        text = ''
        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            text += page.extract_text()
        return text

def split_text_into_words(text):
    nlp = en_core_web_sm.load()
    doc = nlp(text)
    words = [token.text for token in doc]
    return words

def apply_ner_and_mask_words(words, mask_symbol):
    nlp = en_core_web_sm.load()
    doc = nlp(' '.join(words))
    masked_words = [re.sub(r"\b(named entity recognition|regular expressions|rule based logic)\b", mask_symbol, word) for word in words]
    for entity in doc.ents:
        if entity.text.lower() in words:
            masked_words = [mask_symbol if word == entity.text else word for word in masked_words]
    return masked_words

def chunk_and_mask_pdf(pdf_path, chunk_size, mask_symbol="***"):
    chunks = []
    text = read_pdf(pdf_path)
    words = split_text_into_words(text)
    for i in range(0, len(words), chunk_size):
        chunk = words[i:i+chunk_size]
        masked_chunk = apply_ner_and_mask_words(chunk, mask_symbol)
        chunks.append(" ".join(masked_chunk))
    return chunks
  
def mask_text_in_pdf(pdf_path, regex_pattern, replacement):
    with open(pdf_path, 'rb') as pdf_file:
        pdf_reader = PyPDF2.PdfFileReader(pdf_file)

        # Extract text from the PDF
        pdf_text = ''
        for page_num in range(pdf_reader.numPages):
            page = pdf_reader.getPage(page_num)
            pdf_text += page.extractText()

        # Mask the text based on the regular expression
        masked_text = re.sub(regex_pattern, replacement, pdf_text)

        return masked_text

# Example usage
pdf_path = "ner-sample.pdf"
chunk_size = 50  # Adjust chunk size as needed
masked_chunks = chunk_and_mask_pdf(pdf_path, chunk_size)

# Print or process the masked chunks
for chunk in masked_chunks:
  print(chunk)


regex_pattern = r'\d{3}-\d{2}-\d{4}'  # Regular expression pattern for SSN
replacement = '***-**-****'

masked_pdf_text = mask_text_in_pdf(pdf_path, regex_pattern, replacement)
print(masked_pdf_text)
