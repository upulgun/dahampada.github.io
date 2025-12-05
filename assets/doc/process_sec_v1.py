

def process_file(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    
    processed_lines = []
    
    for line in lines:
        # Add newlines before ▼ or ▲ while keeping the symbols
        line = line.replace("මූලාශ්‍රය:", "<b>මූලාශ්‍රය:</b>")
        line = line.replace("සටහන:", "<b>සටහන:</b>")

        new_line = line.replace('▼', '\n▼').replace('▲', '\n▲')
        
        # Split the line into segments by newlines introduced above
        segments = new_line.split('\n')
        
        for segment in segments:
            if '▲' in segment and ':' in segment:
                start = segment.index('▲')
                end = segment.index(':') + 1
                segment = f'{segment[:start]}<span class="keyword">{segment[start:end]}</span>{segment[end:]}'
            
            processed_lines.append(f'<p>{segment}</p>')
    
    with open(output_file, 'w', encoding='utf-8') as file:
        for line in processed_lines:
            file.write(line + '\n')

# Example usage
input_file = 'section1.txt'   # Replace with your input file name
output_file = 'section1_processed.txt' # Replace with your desired output file name
process_file(input_file, output_file)