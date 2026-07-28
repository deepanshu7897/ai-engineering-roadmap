from app.rag.document_loader import DocumentLoader

loader = DocumentLoader()

documents = loader.load("sample_docs/sample.pdf")

print(f"Total Documents: {len(documents)}")

print()

for doc in documents:
    print("=" * 60)
    print(doc.metadata)
    print()
    print(doc.content[:300])
    print()