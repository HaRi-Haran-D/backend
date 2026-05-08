from pypdf import PdfReader

reader = PdfReader(r'C:\Users\Admin\Downloads\example.pdf')
page = reader.pages[0]
all_text = ""

for page in reader.pages:
    all_text += page.extract_text() + "\n"

print("Combined text from all pages:")
print(all_text)
