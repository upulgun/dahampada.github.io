import docx2txt
import re

section1 = docx2txt.process("./assets/doc/full_text.docx")



output_file = "./assets/doc/full_text.txt"

print(section1)

with open(output_file, 'w', encoding='utf-8') as fileo:
   fileo.write(section1)
