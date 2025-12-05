import re

html_head = """"<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        .subheading {
            font-weight: bold;
            margin-left: 20px;
        }
        .heading {
            font-weight: bold;
            font-size: large;
        }
        .keyword {
            font-weight: bold;
        }
        .subkeyword {
            margin-left: 20px;
        }
    </style>
    <title>දහම් පද මාලාව</title>
</head>
<body>"""

html_tail = """</body>
</html>"""

def process_file_first_pass(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    
    processed_lines = []

    for line in lines:
        # Replace "මූලාශ්‍රය:" with <b>මූලාශ්‍රය:</b>
        # line = line.replace("මූලාශ්‍රය:", "<b>මූලාශ්‍රය:</b>")

        #match = re.search(r'(\s+)(\S{2})(\s+)▲', line)
        match = re.search(r'(\s+)([^\W\d_]{2})(\s+)▲', line, re.UNICODE)
        #match2 = re.search(r'(\s+)(\S{2})(\s+\n)▲', line)
        match2 = re.search(r'(\s+)([^\W\d_]{2})(\s+\n)▲', line, re.UNICODE)

        if match:
            two_char_word = match.group(2)
            # Split the line at the position of the two-character word
            start = match.start(2)
            end = match.end(2)
            line = f'{line[:start]}\n<span class="subheading">{two_char_word}</span>\n{line[end:]}'
        
        if match2:
            two_char_word = match2.group(2)
            # Split the line at the position of the two-character word
            start = match2.start(2)
            end = match2.end(2)
            line = f'{line[:start]}\n<span class="subheading">{two_char_word}</span>\n{line[end:]}'

        processed_lines.append(f'{line}')

    with open(output_file, 'w', encoding='utf-8') as file:
        for line in processed_lines:
            file.write(line + '\n')
    
import re

""" def process_file(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    
    processed_lines = []
    
    for line in lines:
        # Replace "මූලාශ්‍රය:" with <b>මූලාශ්‍රය:</b>
        line = line.replace("මූලාශ්‍රය:", "<b>මූලාශ්‍රය:</b>")
        line = line.replace("සටහන:", "<b>සටහන:</b>")
        
        # Add newlines before ▼ or ▲ while keeping the symbols
        new_line = line.replace('▼', '\n▼').replace('▲', '\n▲')
        
        # Split the line into segments by newlines introduced above
        segments = new_line.split('\n')
        
        for segment in segments:
            # Check for pattern: some spaces, a two-character UTF-8 word (excluding numbers), some spaces, followed by ▲
            match_subheading = re.search(r'(\s+)([^\W\d_]{2})(\s+)▲', segment, re.UNICODE)
            if match_subheading:
                two_char_word = match_subheading.group(2)
                # Split the line at the position of the two-character word
                start = match_subheading.start(2)
                end = match_subheading.end(2)
                segment = f'{segment[:start]}\n<span class="subheading">{two_char_word}</span>\n{segment[end:]}'
            
            # Check for pattern: UTF-8 character followed by space and "කොටස:"
            match_heading = re.search(r'([^\W\d_])\s+කොටස:', segment, re.UNICODE)
            if match_heading:
                start = match_heading.start()
                end = match_heading.end()
                segment = f'{segment[:start]}<span class="Fheading">{segment[start:end]}</span>{segment[end:]}'
            
            if '▲' in segment and ':' in segment:
                start = segment.index('▲')
                end = segment.index(':') + 1
                segment = f'{segment[:start]}<span class="keyword">{segment[start:end]}</span>{segment[end:]}'
            
            processed_lines.append(f'<p>{segment}</p>')
    
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(html_head)
        for line in processed_lines:
            file.write(line + '\n')
        file.write(html_tail)
 """

import re

def process_file_ok(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    
    processed_lines = []
    
    for line in lines:
        # Replace "මූලාශ්‍රය:" with <b>මූලාශ්‍රය:</b>
        line = line.replace("මූලාශ්‍රය:", "<b>මූලාශ්‍රය:</b>")
        line = line.replace("සටහන:", "<b>සටහන:</b>")

        # Add newlines before ▼ or ▲ while keeping the symbols
        new_line = line.replace('▼', '\n▼').replace('▲', '\n▲')
        
        # Split the line into segments by newlines introduced above
        segments = new_line.split('\n')
        
        for segment in segments:
            # Check if the line starts with the ▼ character
            if segment.startswith('▼'):
                segment = f'<span class="subkeyword">{segment}</span>'
            
            # Check for pattern: some spaces, a two-character UTF-8 word (excluding numbers), some spaces, followed by ▲
            match_subheading = re.search(r'(\s+)([^\W\d_]{2})(\s+)▲', segment, re.UNICODE)
            if match_subheading:
                two_char_word = match_subheading.group(2)
                # Split the line at the position of the two-character word
                start = match_subheading.start(2)
                end = match_subheading.end(2)
                segment = f'{segment[:start]}\n<span class="subheading">{two_char_word}</span>\n{segment[end:]}'
            
            # Check for pattern: UTF-8 character followed by space and "කොටස:"
            match_heading = re.search(r'([^\W\d_])\s+කොටස:', segment, re.UNICODE)
            if match_heading:
                start = match_heading.start()
                end = match_heading.end()
                heading_segment = f'<span class="heading">{segment[start:end]}</span>'
                # Append the heading segment separately to ensure it is on its own line
                processed_lines.append(f'<p>{heading_segment}</p>')
                # Remove the heading part from the original segment
                segment = segment[end:].strip()
            
            if '▲' in segment and ':' in segment:
                start = segment.index('▲')
                end = segment.index(':') + 1
                segment = f'{segment[:start]}<span class="keyword">{segment[start:end]}</span>{segment[end:]}'
            
            # Only append non-empty segments
            if segment.strip():
                processed_lines.append(f'<p>{segment}</p>')
    
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(html_head)
        for line in processed_lines:
            file.write(line + '\n')
        file.write(html_tail)

import re

def process_file(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    
    processed_lines = []
    inside_subheading = False
    
    for line in lines:
        # Replace "මූලාශ්‍රය:" with <b>මූලාශ්‍රය:</b>
        line = line.replace("මූලාශ්‍රය:", "<b>මූලාශ්‍රය:</b>")
        line = line.replace("සටහන:", "<b>සටහන:</b>")
        line = line.replace("මූලාශ්‍ර:", "<b>මූලාශ්‍ර:</b>")
        line = line.replace("බලන්න:", "<b>බලන්න:</b>")
        
        # Add newlines before ▼ or ▲ while keeping the symbols
        new_line = line.replace('▼', '\n▼').replace('▲', '\n▲')
        
        # Split the line into segments by newlines introduced above
        segments = new_line.split('\n')
        
        for segment in segments:
            # Check if the line starts with the ▼ character
            if segment.startswith('▼'):
                inside_subheading = True
                segment = f'<span class="subkeyword">{segment}</span>'
            
            # Check if the line starts with the ▲ character
            if segment.startswith('▲'):
                inside_subheading = False
            
            # Apply subheading class if inside subheading block
            if inside_subheading and not segment.startswith('<span class="subkeyword">'):
                segment = f'<span class="subkeyword">{segment}</span>'
            
            # Check for pattern: some spaces, a two-character UTF-8 word (excluding numbers), some spaces, followed by ▲
            match_subheading = re.search(r'(\s+)([^\W\d_]{2})(\s+)▲', segment, re.UNICODE)
            if match_subheading:
                two_char_word = match_subheading.group(2)
                # Split the line at the position of the two-character word
                start = match_subheading.start(2)
                end = match_subheading.end(2)
                segment = f'{segment[:start]}\n<span class="subheading">{two_char_word}</span>\n{segment[end:]}'
            
            # Check for pattern: UTF-8 character followed by space and "කොටස:"
            match_heading = re.search(r'([^\W\d_])\s+කොටස:', segment, re.UNICODE)
            if match_heading:
                start = match_heading.start()
                end = match_heading.end()
                heading_segment = f'<span class="heading">{segment[start:end]}</span>'
                # Append the heading segment separately to ensure it is on its own line
                processed_lines.append(f'<p>{heading_segment}</p>')
                # Remove the heading part from the original segment
                segment = segment[end:].strip()
            
            if '▲' in segment and ':' in segment:
                start = segment.index('▲')
                end = segment.index(':') + 1
                segment = f'{segment[:start]}<span class="keyword">{segment[start:end]}</span>{segment[end:]}'
            
            # Only append non-empty segments
            if segment.strip():
                processed_lines.append(f'<p>{segment}</p>')
    
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(html_head)
        for line in processed_lines:
            file.write(line + '\n')
        file.write(html_tail)



# Example usage

input_file = 'sections/a_section.txt'   # Replace with your input file name
output_file = 'sections/a_section1.txt' # Replace with your desired output file name
process_file_first_pass(input_file, output_file)


input_file = 'sections/a_section1.txt'   # Replace with your input file name
output_file = 'sections/a_section.html' # Replace with your desired output file name
process_file(input_file, output_file)

