import re

html_head_1 = """<!DOCTYPE html>
<html lang="en">

<head>

        <!-- Google tag (gtag.js) -->
        <script async src="https://www.googletagmanager.com/gtag/js?id=G-KZ8V4HEJQM"></script>
        <script>
        window.dataLayer = window.dataLayer || [];
        function gtag(){dataLayer.push(arguments);}
        gtag('js', new Date());

        gtag('config', 'G-KZ8V4HEJQM');
        </script>
        <script async src="https://cse.google.com/cse.js?cx=f1665ce0444e24639"></script>
    
        <!-- Required meta tags -->
        <meta charset="utf-8" />
        <meta name="viewport"
            content="width=device-width, initial-scale=1, shrink-to-fit=no"     />

        <!-- Bootstrap CSS v5.2.1 -->
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css"
            rel="stylesheet"
            integrity="sha384-T3c6CoIi6uLrA9TneNEoa7RxnatzjcDSCmG1MXxSR1GAsXEV/Dwwykc2MPK8M2HN"
            crossorigin="anonymous"/>

            <link rel="apple-touch-icon" sizes="180x180" href="/assets/favicon/apple-touch-icon.png">
            <link rel="icon" type="image/png" sizes="32x32" href="/assets/favicon//favicon-32x32.png">
            <link rel="icon" type="image/png" sizes="16x16" href="/assets/favicon//favicon-16x16.png">
            <link rel="manifest" href="/assets/favicon//site.webmanifest">

            <style>
            .btn {
                background-color: rgb(76, 243, 10);
                font-size: 18px;
                font-weight: bolder;
                color: rgb(44, 10, 235);
                border-radius: 5000px;
                transition: all 0.3s;
                /*
                text-transform: uppercase;
                */
                box-shadow: 0 6px 23px rgba(0,0,0,0.45);
                animation: fade-up 0.5s 0.4s backwards;
            }

            .btn:hover {
                transform: scale(1.15);
                background-color: #93f0f7;
            }

            .navbar a:hover, .dropdown:hover .dropbtn {
                background-color: #555;
                color: white;
            }
            .bolded {
                font-size: 4pc;
                font-weight: 900;
            }
        

    
        .subheading {
            font-weight: bold;
            margin-left: 10px;
            font-size: large;
            color: blue;
        }
        .heading {
            font-weight: bold;
            font-size: larger;
        }
        .keyword {
            font-weight: bold;
        }
        .keywordseg {
            margin-left: 10px;
        }
        .subkeyword {
            margin-left: 20px;
        }
    </style>
    """
html_head_2 = """
</head>
<body>
    <header>
        <nav
            class="navbar fixed-top navbar-expand-md navbar-dark bg-secondary">
            <div class="container-fluid">
                <a class="navbar-brand" href="/"><img src="/assets/img/dpm_logo-removebg.png" width="30"></a>
                <button  class="navbar-toggler d-lg-none"
                    type="button"
                    data-bs-toggle="collapse"
                    data-bs-target="#collapsibleNavId"
                    aria-controls="collapsibleNavId"
                    aria-expanded="false"
                    aria-label="Toggle navigation">
                    <span class="navbar-toggler-icon"></span>
                </button>
                <div class="collapse navbar-collapse" id="collapsibleNavId">
                    <ul class="navbar-nav me-auto mt-2 mt-lg-0">

                        <li class="nav-item">
                            <a class="nav-link active" href="/index.html#foreword">පෙරවදන</a>
                        </li>
                        <li class="nav-item">
                            <a class="nav-link active" href="/index.html#intro">හැදින්වීම</a>
                        </li>
                        <li class="nav-item">
                            <a class="nav-link active" href="/index.html#vishaya_karunu">විෂය කරුණු</a>
                        </li>
                        <li class="nav-item">
                            <a class="nav-link active" href="/index.html#download">Download</a>
                        </li>

                        <li class="nav-item dropdown">
                            <a  class="nav-link dropdown-toggle active"
                                href="#"
                                id="dropdownId"
                                data-bs-toggle="dropdown"
                                aria-haspopup="true"
                                aria-expanded="false">පොතේ කොටස්</a>
                            <div  class="dropdown-menu"      aria-labelledby="dropdownId">
                                <a href="/sections/a_section.html" class="dropdown-item">අ කොටස</a>
                                <a href="/sections/e_section.html" class="dropdown-item">ඉ කොටස</a>
                                <a href="/sections/u_to_o_sections.html" class="dropdown-item">උ, ඍ, එ සහ ඔ කොටස්</a>
                                <a href="/sections/ka_kha_section.html" class="dropdown-item">ක සහ ඛ කොටස්</a>
                                <a href="/sections/ga_gha_section.html" class="dropdown-item">ග සහ ඝ කොටස්</a>
                                <a href="/sections/cha_chha_section.html" class="dropdown-item"> ච සහ ඡ කොටස්</a>
                                <a href="/sections/ja_section.html" class="dropdown-item">ජ කොටස</a>
                                <a href="/sections/kgna_gna_taa_section.html" class="dropdown-item">ඤ, ඥ සහ ඨ කොටස්</a>
                                <a href="/sections/tha_thha_section.html" class="dropdown-item">ත සහ ථ කොටස්</a>
                                <a href="/sections/da_dha_section.html" class="dropdown-item">ද සහ ධ කොටස්</a>
                                <a href="/sections/na_nha_section.html" class="dropdown-item">න සහ ණ කොටස්</a>
                                <a href="/sections/pa_pha_section.html" class="dropdown-item">ප සහ ඵ කොටස්</a>
                                <a href="/sections/ba_bha_section.html" class="dropdown-item">බ සහ භ කොටස්</a>
                                <a href="/sections/ma_section.html" class="dropdown-item">ම කොටස</a>
                                <a href="/sections/ya_section.html" class="dropdown-item">ය කොටස</a>
                                <a href="/sections/ra_la_section.html" class="dropdown-item">ර සහ ල කොටස්</a>
                                <a href="/sections/wa_section.html" class="dropdown-item">ව කොටස</a>
                                <a href="/sections/sa_section.html" class="dropdown-item">ස කොටස</a>
                                <a href="/sections/sha_shha_section.html" class="dropdown-item">ශ සහ ෂ කොටස්</a>
                                <a href="/sections/ha_section.html" class="dropdown-item">හ කොටස</a>
                                <a href="assets/pdfs/pages_969_1017.pdf" class="dropdown-item">සුචිය</a>
                                <a href="assets/pdfs/pages_1018_1244.pdf" class="dropdown-item">උපග්‍රන්ථ</a>
                                <a href="assets/pdfs/pages_1245_end.pdf" class="dropdown-item">සිතියම්</a>
                            </div>
                        </li>
                        
                    </ul>
                    <form class="form-inline my-2 my-lg-0">
                        <!-- Google Custom Search Element -->
                        <div class="gcse-searchbox-only"></div>
                    </form>
                </div>
            </div>
        </nav>

    </header>
    <main>

"""

html_tail = """
</main>
        <footer>
            <!-- place footer here -->
        </footer>
        <!-- Bootstrap JavaScript Libraries -->
        <script
            src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.11.8/dist/umd/popper.min.js"
            integrity="sha384-I7E8VVD/ismYTF4hNIPjVp/Zjvgyol6VFvRkX/vR+Vc4jQkC+hVqc2pM8ODewa9r"
            crossorigin="anonymous"></script>

        <script
            src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.min.js"
            integrity="sha384-BBtl+eGJRgqQAUMxJ7pMwbEyER4l1g+O15P+16Ep7Q9Q+zqX6gSbd85u4mG4QzX+"
            crossorigin="anonymous"></script>
</body>
</html>"""

def process_file_first_pass(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    
    processed_lines = []

    for line in lines:
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

def process_file(input_file, output_file, section_name):
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
                segment = f'<div class="subkeyword">{segment}</div>'
            
            # Check if the line starts with the ▲ character
            if segment.startswith('▲'):
                inside_subheading = False
            
            # Apply subheading class if inside subheading block
            if inside_subheading and not segment.startswith('<span class="subkeyword">'):
                segment = f'<div class="subkeyword">{segment}</div>'
            
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
            
            if '▲' in segment:
                segment = f'<div class="keywordseg">{segment}</div>'
            
            # Only append non-empty segments
            if segment.strip():
                processed_lines.append(f'<p>{segment}</p>')
    
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(html_head_1)
        file.write(f'<title>{section_name}</title>')
        file.write(html_head_2)
        file.write(f'<br><br><br>\n<h1>{section_name}</h1>\n')
        for line in processed_lines:
            file.write(line + '\n')
        file.write(html_tail)



##########################

def process_section(section_filename, section_name):
    input_file = f'sections/{section_filename}.txt'
    im_file = f'sections/{section_filename}_im.txt'
    output_file = f'sections/{section_filename}.html'
    process_file_first_pass(input_file, im_file)
    process_file(im_file, output_file, section_name)


section_names = ['අ කොටස','ඉ කොටස', 'උ කොටස, ඍ කොටස, එ කොටස සහ ඔ කොටස',
                  'ක සහ ඛ කොටස්', 'ග සහ ඝ කොටස්', 'ච සහ ඡ කොටස්', 'ජ කොටස',
                  'ඤ, ඥ සහ ඨ කොටස්', 'ත සහ ථ කොටස්', 'ද සහ ධ කොටස්',
                  'න සහ ණ කොටස්', 'ප සහ ඵ කොටස්', 'බ සහ භ කොටස්',
                  'ම කොටස', 'ය කොටස', 'ර සහ ල කොටස්', 
                  'ව කොටස', 'ස කොටස', 'ශ සහ ෂ කොටස්', 'හ කොටස']

section_filenames = ['a_section', 'e_section', 'u_to_o_sections',
                     'ka_kha_section', 'ga_gha_section', 'cha_chha_section', 'ja_section',
                     'kgna_gna_taa_section', 'tha_thha_section', 'da_dha_section',
                     'na_nha_section','pa_pha_section', 'ba_bha_section',
                     'ma_section', 'ya_section', 'ra_la_section',
                     'wa_section', 'sa_section', 'sha_shha_section', 'ha_section']

""" input_file = 'sections/a_section.txt'   
output_file = 'sections/a_section1.txt' 
process_file_first_pass(input_file, output_file)


input_file = 'sections/a_section1.txt'   
output_file = 'sections/a_section.html' 
process_file(input_file, output_file, section_name) """

N = len(section_names)

for n in range(1, N+1):
    section_filename  = section_filenames[n-1]
    section_name = section_names[n-1]
    print(f'{n} {section_filenames[n-1]}  {section_name}')

    process_section(section_filename, section_name)

