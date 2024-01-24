from pypdf import PdfMerger
import os

pdfToAppend = "append.pdf"
pdfDirectory = ".\\input"
outputDirectoryPrefix = ".\\output"

# check if input folder exists
if not os.path.exists(pdfDirectory):
    print("input folder does not exist. Exiting...")
    exit(1)

# create output directory
outputDirectory = outputDirectoryPrefix
suffix = 1
while os.path.exists(outputDirectory):
    suffix += 1
    outputDirectory = outputDirectoryPrefix + "-" + str(suffix)
os.mkdir(outputDirectory)


def get_long_path(dirpath, filename):
    path = os.path.abspath(os.path.join(dirpath, filename))
    if path.startswith("\\\\"):
        path = "\\\\?\\UNC\\" + path[2:]
    else:
        path = "\\\\?\\" + path
    return path


pathPdfToAppend = get_long_path(".\\", pdfToAppend)

# merge pdfs
for dirpath, dirnames, filenames in os.walk(pdfDirectory):
    for filename in filenames:
        if filename.endswith(".pdf"):
            print("Appending a page to " + filename)
            input_file_path = get_long_path(dirpath, filename)
            output_file_path = get_long_path(outputDirectory, filename)
            merger = PdfMerger()
            merger.append(input_file_path)
            merger.append(pathPdfToAppend)
            merger.write(output_file_path)
            merger.close()
