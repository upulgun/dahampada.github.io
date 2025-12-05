import re

def clean_text(text):
    # Remove spaces after opening parenthesis and closing parenthesis
    text = re.sub(r'\(\s+','(', text)
    # Ensure symbols ▲ and ▼ start on a new line and have at least one space after them
    text = re.sub(r'([^\n])([▲▼])', r'\1\n\2', text)
    text = re.sub(r'([▲▼])(?!\s)', r'\1 ', text)
    # Remove extra whitespace
    # text = re.sub(r'\s+', ' ', text).strip()
    return text

with open('fulltext-V2.txt', 'r', encoding='utf-8') as file:
    content = file.read()
    
# clean the text
cleaned_content = clean_text(content)

with open('fulltext-V2-clean.txt', 'w', encoding='utf-8') as file:
    file.write(cleaned_content)
