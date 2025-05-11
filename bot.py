from sentence_transformers import SentenceTransformer
import faiss
import numpy as np


class QAChatBot:
    def __init__(self, model_path="qachatbot/models/all-MiniLM-L6-v2"):
        # Initialize the model
        self.model = SentenceTransformer(model_path)
        self.index = None
        self.sentences = []

    def load_sentences(self, file_path):
        """Load sentences from the provided text file."""
        with open(file_path, "r") as file:
            self.sentences = file.readlines()
        self.sentences = [
            sentence.strip() for sentence in self.sentences
        ]  # Remove extra spaces/newlines
        self._create_index()

    def _create_index(self):
        """Create FAISS index for fast nearest-neighbor search."""
        embeddings = self.model.encode(self.sentences)
        embeddings = np.array(embeddings).astype("float32")
        self.index = faiss.IndexFlatL2(embeddings.shape[1])  # L2 distance metric
        self.index.add(embeddings)

    def ask_question(self, question):
        """Ask a question and get the most relevant sentence."""
        input_vector = self.model.encode([question], convert_to_tensor=False)[0]
        input_vector = np.array(input_vector).astype("float32").reshape(1, -1)
        distances, indices = self.index.search(input_vector, 1)
        return self.sentences[indices[0][0]]
