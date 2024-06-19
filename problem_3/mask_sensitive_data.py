import PyPDF2
import re
import spacy
import en_core_web_sm

def chunk_and_mask_pdf(pdf_path, chunk_size, mask_symbol="***"):
  """
  Chunks text from a PDF, masks specified words and named entities, and returns a list of strings.

  Args:
      pdf_path: Path to the PDF file.
      chunk_size: Number of words per chunk.
      mask_symbol: Symbol to replace masked words (default="***").

  Returns:
      List of strings containing chunked and masked text.
  """
  chunks = []
  nlp = en_core_web_sm.load()
  

  with open(pdf_path, 'rb') as pdf_file:
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    for page_num in range(len(pdf_reader.pages)):
      page = pdf_reader.pages[page_num]
      text = page.extract_text()

      # Split text into words
      doc = nlp(text)  # Apply NER with spaCy

      words = []
      for token in doc:
        words.append(token.text)

      for i in range(0, len(words), chunk_size):
        chunk = words[i:i+chunk_size]

        # Mask pre-defined words and named entities
        masked_chunk = [re.sub(rf"\b(named entity recognition|regular expressions|rule based logic)\b", mask_symbol, word) for word in chunk]
        for entity in doc.ents:
          if entity.text.lower() in chunk:
            masked_chunk = [mask_symbol if word == entity.text else word for word in masked_chunk]
        chunks.append(" ".join(masked_chunk))
  return chunks

# Example usage
pdf_path = "ner-sample.pdf"
chunk_size = 50  # Adjust chunk size as needed
masked_chunks = chunk_and_mask_pdf(pdf_path, chunk_size)

# Print or process the masked chunks
for chunk in masked_chunks:
  print(chunk)
