import os
import zipfile
import shutil
from bs4 import BeautifulSoup
import html

input = './epubs/karamazov.epub'
output = './output/karamazovBOLD.epub'

def bolder(epub_path, output_path):
# Step 1: Extract EPUB Content using zipfile module
    output_folder = 'temp_extracted_folder'
    with zipfile.ZipFile(epub_path, 'r') as epub_zip:
        epub_zip.extractall(output_folder)

    # Step 2: Process HTML Files
    html_files = []
    for root, _, files in os.walk(os.path.join(output_folder, 'OEBPS')):
        html_files.extend([os.path.join(root, file) for file in files if file.endswith('.html')])

    for html_file in html_files:
        with open(html_file, 'r', encoding='utf-8') as file:
            content = file.read()

            # Decode HTML-encoded entities
            decoded_content = html.unescape(content)

            soup = BeautifulSoup(decoded_content, 'html.parser')

        # Step 3: Modify Content
        for text_node in soup.find_all(string=True):
            words = text_node.split()
            modified_words = ['<b>' + word[:len(word) // 2] + '</b>' + word[len(word) // 2:] for word in words]
            text_node.replace_with(' '.join(modified_words))

        # Step 4: Replace encoded span tags
        modified_content = str(soup).replace('&lt;b&gt;', '<b>').replace('&lt;/b&gt;', '</b>')

        # Save the modified content back to the file
        with open(html_file, 'w', encoding='utf-8') as file:
            file.write(modified_content)

    # Step 5: Repackage EPUB
    with zipfile.ZipFile(output_path, 'w') as output_zip:
        for root, _, files in os.walk(output_folder):
            for file in files:
                output_zip.write(os.path.join(root, file), os.path.relpath(os.path.join(root, file), output_folder))

    # Step 6: Clean up temporary files
    shutil.rmtree('temp_extracted_folder')

    print("EPUB modification and repackaging completed.")

# bolder(input, output)
