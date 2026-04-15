"""
STEP 3 — Knowledge Base Loader
================================
Place your source files in these folders:
  books/    → PDF books (God Delusion, God Is Not Great, etc.)
  texts/    → Plain .txt files with atheism content
  
Web sources are scraped automatically.
"""

import os
from langchain_community.document_loaders import PyPDFLoader, TextLoader, WebBaseLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from config import CHUNK_SIZE, CHUNK_OVERLAP


# ── PDF books to load ──────────────────────────────────────────────────────────
PDF_FILES = [
    "books/god_delusion.pdf",
    "books/god_is_not_great.pdf",
    "books/end_of_faith.pdf",
    "books/why_i_am_not_a_christian.pdf",
    "books/breaking_the_spell.pdf",
]

# ── Plain text files to load ───────────────────────────────────────────────────
TEXT_FILES = [
    "texts/atheism_arguments.txt",
    "texts/secular_ethics.txt",
    "texts/freethought_history.txt",
]

# ── Web sources to scrape ──────────────────────────────────────────────────────
WEB_URLS = [
    "https://plato.stanford.edu/entries/atheism-agnosticism/",
    "https://plato.stanford.edu/entries/evil/",
    "https://plato.stanford.edu/entries/divine-hiddenness/",
    "https://infidels.org/library/modern/why_atheism/",
]


def load_documents():
    all_docs = []

    # Load PDFs
    for path in PDF_FILES:
        if os.path.exists(path):
            try:
                loader = PyPDFLoader(path)
                docs = loader.load()
                all_docs.extend(docs)
                print(f"  [OK] Loaded PDF: {path} ({len(docs)} pages)")
            except Exception as e:
                print(f"  [SKIP] Could not load {path}: {e}")
        else:
            print(f"  [MISSING] {path} — place the file there to include it")

    # Load text files
    for path in TEXT_FILES:
        if os.path.exists(path):
            try:
                loader = TextLoader(path, encoding="utf-8")
                docs = loader.load()
                all_docs.extend(docs)
                print(f"  [OK] Loaded text: {path}")
            except Exception as e:
                print(f"  [SKIP] Could not load {path}: {e}")
        else:
            print(f"  [MISSING] {path} — place the file there to include it")

    # Scrape web pages
    for url in WEB_URLS:
        try:
            loader = WebBaseLoader(url)
            docs = loader.load()
            all_docs.extend(docs)
            print(f"  [OK] Scraped: {url}")
        except Exception as e:
            print(f"  [SKIP] Could not scrape {url}: {e}")

    print(f"\nTotal documents loaded: {len(all_docs)}")
    return all_docs


def split_documents(docs):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=CHUNK_SIZE,
        chunk_overlap=CHUNK_OVERLAP,
        separators=["\n\n", "\n", ". ", " "]
    )
    chunks = splitter.split_documents(docs)
    print(f"Total chunks after splitting: {len(chunks)}")
    return chunks


if __name__ == "__main__":
    print("\n=== Loading Knowledge Base ===\n")
    docs = load_documents()
    chunks = split_documents(docs)
    print("\nDone! Now run: python vector_store.py")
