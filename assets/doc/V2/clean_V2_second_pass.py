import re

def clean_text_first_pass(text):
    # Remove spaces after opening parenthesis and before closing parenthesis
    text = re.sub(r'\(\s+', '(', text)
    text = re.sub(r'\s+\)', ')', text)
    
    # Ensure ▲ or ▼ symbols start on a new line and have at least one space after them
    text = re.sub(r'([^\n])([▲▼])', r'\1\n\2', text)
    text = re.sub(r'([▲▼])(?!\s)', r'\1 ', text)
    
    return text

def clean_text_second_pass(text):
    # Handle " කොටස:" phrase
    text = re.sub(r'(.)( කොටස:)(.*)', r'\n\1\2\n\3', text)
    
    # Handle two-character words surrounded by many spaces
    text = re.sub(r'(\s{3,})(\S{2})(\s{3,})', r'\n\2\n', text)
    
    return text

def process_file(input_file, intermediate_file, output_file):
    # First pass
    with open(input_file, 'r', encoding='utf-8') as infile:
        content = infile.read()
    
    cleaned_content = clean_text_first_pass(content)
    
    with open(intermediate_file, 'w', encoding='utf-8') as outfile:
        outfile.write(cleaned_content)
    
    # Second pass
    with open(intermediate_file, 'r', encoding='utf-8') as infile:
        content = infile.read()
    
    final_content = clean_text_second_pass(content)
    
    with open(output_file, 'w', encoding='utf-8') as outfile:
        outfile.write(final_content)

# Main execution
input_file = 'fulltext-V2.txt'
intermediate_file = 'fulltext-V2-cleaned.txt'
output_file = 'fulltext-V2-second-pass.txt'

process_file(input_file, intermediate_file, output_file)
print(f"File cleaned and saved as {output_file}")