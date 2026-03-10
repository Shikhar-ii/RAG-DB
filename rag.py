import os
import pickle
import faiss
import numpy as np
from pypdf import PdfReader
from sentence_transformers import SentenceTransformer


class RagEngine:

    def __init__(self):
        os.makedirs("vector_store", exist_ok=True)

        self.model = SentenceTransformer("all-MiniLM-L6-v2")

        self.index_file = "vector_store/index.faiss"
        self.meta_file = "vector_store/meta.pkl"

        if os.path.exists(self.index_file):

            self.index = faiss.read_index(self.index_file)

            with open(self.meta_file, "rb") as f:
                self.meta = pickle.load(f)

        else:

            self.index = faiss.IndexFlatL2(384)
            self.meta = []

    def save(self):

        faiss.write_index(self.index, self.index_file)

        with open(self.meta_file, "wb") as f:
            pickle.dump(self.meta, f)

    def extract_pdf(self, path):

        reader = PdfReader(path)
        text = ""

        for p in reader.pages:
            text += p.extract_text() or ""

        return text

    def chunk(self, text):

        size = 700
        overlap = 100

        chunks = []

        i = 0

        while i < len(text):

            chunks.append(text[i:i+size])

            i += size - overlap

        return chunks

    def add_document(self, path, name):

        text = self.extract_pdf(path)

        chunks = self.chunk(text)

        embeddings = self.model.encode(chunks)

        self.index.add(np.array(embeddings).astype("float32"))

        for i,c in enumerate(chunks):

            self.meta.append({
                "file": name,
                "text": c
            })

        self.save()

        return len(chunks)

    def search(self, query):

        q = self.model.encode([query])

        dist, ids = self.index.search(np.array(q).astype("float32"),4)

        results = []

        for i in ids[0]:

            if i < len(self.meta):

                results.append(self.meta[i])

        return results
