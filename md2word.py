# pip install python-docx markdown 
import markdown
from docx import Document

def convert_markdown_to_word(md, word):

    with open(md, 'r') as file:
        file_contents = file.read()
        
    # Convert Markdown to HTML
    html_text = markdown.markdown(file_contents)

    # Create a new Word document
    doc = Document()

    # Add the converted HTML text to the Word document
    doc.add_paragraph(html_text)

    # Save the Word document
    doc.save(word)

convert_markdown_to_word('synopsis.md','synopsis.docx')
