from pypdf import PdfMerger
import os

pdfToAppend = "./append.pdf"
pdfDirectory = "./input"
outputDirectoryPrefix = "./output"

# check if input folder exists
if (not os.path.exists(pdfDirectory)):
    print("input folder does not exist. Exiting...")
    exit(1)

# create output directory
outputDirectory = outputDirectoryPrefix
suffix = 1
while os.path.exists(outputDirectory):
    suffix += 1
    outputDirectory = outputDirectoryPrefix + "-" + str(suffix)
os.mkdir(outputDirectory)

# merge pdfs
for dirpath, dirnames, filenames in os.walk(pdfDirectory):
    for filename in filenames:
        if (filename.endswith(".pdf")):
            print("Appending a page to " + filename)
            merger = PdfMerger()
            merger.append(pdfDirectory + "/" + filename)
            merger.append(pdfToAppend)
            merger.write(outputDirectory + "/" + filename)
            merger.close()
