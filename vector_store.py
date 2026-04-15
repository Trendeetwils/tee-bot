"""
STEP 4 — Vector Database Builder
===================================
Run this ONCE to embed your documents and save them to ChromaDB.
After that, the bot loads from the saved database automatically.

Run: python vector_store.py
"""

from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
from knowledge_loader import load_documents, split_documents
from config import CHROMA_DB_PATH
import os


EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"


def get_embeddings():
    print("Loading embedding model (downloads once ~80MB)...")
    return HuggingFaceEmbeddings(
        model_name=EMBEDDING_MODEL,
        model_kwargs={"device": "cpu"},
        encode_kwargs={"normalize_embeddings": True}
    )


def build_vector_store():
    """Build the vector store from scratch. Run this once."""
    print("\n=== Building Vector Database ===\n")

    docs = load_documents()
    chunks = split_documents(docs)

    if not chunks:
        print("\n[WARNING] No documents found!")
        print("Place PDF/text files in books/ and texts/ folders first.")
        print("The bot will still work using its trained knowledge only.\n")
        return None

    print(f"\nEmbedding {len(chunks)} chunks into ChromaDB...")
    embeddings = get_embeddings()

    vectorstore = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory=CHROMA_DB_PATH
    )
    vectorstore.persist()
    print(f"\n[DONE] Vector store saved to: {CHROMA_DB_PATH}")
    print("Now run: python telegram_bot.py\n")
    return vectorstore


def load_vector_store():
    """Load an existing vector store from disk."""
    if not os.path.exists(CHROMA_DB_PATH):
        print("[INFO] No vector store found. Bot will use base knowledge only.")
        return None
    embeddings = get_embeddings()
    return Chroma(
        persist_directory=CHROMA_DB_PATH,
        embedding_function=embeddings
    )


if __name__ == "__main__":
    build_vector_store()
