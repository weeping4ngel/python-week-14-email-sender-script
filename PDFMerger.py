from PyPDF2 import PdfMerger
import os

def merge_pdfs(pdf_paths, output_path):
    merger = PdfMerger()

    for path in pdf_paths:
        if not os.path.exists(path):
            print(f"Skipping (not found): {path}")
            continue
        if not path.lower().endswith(".pdf"):
            print(f"Skipping (not a PDF): {path}")
            continue

        merger.append(path)
        print(f"Added: {path}")

    merger.write(output_path)
    merger.close()
    print(f"\nDone! Merged PDF saved as: {output_path}")

def main():
    print("PDF Merger Tool")
    files = input("Enter PDF file paths separated by commas:\n").split(",")

    pdf_paths = [f.strip() for f in files if f.strip()]
    output_path = input("Enter output file name (e.g. merged.pdf): ").strip()

    if not output_path.lower().endswith(".pdf"):
        output_path += ".pdf"

    merge_pdfs(pdf_paths, output_path)

if __name__ == "__main__":
    main()
