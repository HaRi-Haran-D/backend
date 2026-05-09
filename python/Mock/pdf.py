# from pypdf import PdfReader
#
# reader = PdfReader(r'C:\Users\Admin\Downloads\example.pdf')
# page = reader.pages[0]
# all_text = ""
#
# for page in reader.pages:
#     all_text += page.extract_text() + "\n"
#
# print("Combined text from all pages:")
# print(all_text)


n = 6
print(n, end="")

while n != 1:
    if n % 2 == 0:
        n = n // 2
    else:
        n = (3 * n) + 1
    print(f", {n}", end="")