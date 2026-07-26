from app.ai.semantic_search import SemanticSearch

search = SemanticSearch()

documents = [
    "Python is a programming language.",
    "FastAPI is used for building APIs.",
    "Machine learning is a branch of AI.",
    "Gemini is Google's multimodal AI model.",
    "Cats are domestic animals.",
    "Dogs are loyal pets.",
    "Football is a popular sport.",
    "Paris is the capital of France.",
    "SQLAlchemy is an ORM for Python.",
    "Vector embeddings enable semantic search.",
]

search.add_documents(documents)

query = "How can I build APIs using Python?"

results = search.search(query)

for doc, score in results:
    print(f"{score:.4f} -> {doc}")