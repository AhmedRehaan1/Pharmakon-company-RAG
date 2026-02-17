"""
Vector store service.
Manages Chroma vector database initialization, persistence, and querying.
"""
import os
from pathlib import Path
from typing import List, Tuple, Optional

from langchain.schema import Document
from langchain.vectorstores import Chroma
from langchain.embeddings import OpenAIEmbeddings

from config.settings import Settings


class VectorStoreManager:
    """
    Manages the Chroma vector database for product embeddings.
    Handles creation, persistence, and loading of the vector store.
    """
    
    def __init__(self):
        """Initialize the vector store manager with configuration settings."""
        self.persist_directory = Settings.PERSIST_DIRECTORY
        self.embedding_model = OpenAIEmbeddings(model=Settings.EMBEDDING_MODEL)
        self._vectordb: Optional[Chroma] = None
    
    def initialize(self, documents: List[Document], force_recreate: bool = False) -> None:
        """
        Initialize or load the vector database.
        
        Args:
            documents: List of Document objects to embed and store
            force_recreate: If True, recreate the database even if it exists
        """
        db_exists = os.path.exists(self.persist_directory)
        
        if force_recreate or not db_exists:
            self._create_vector_db(documents)
        else:
            self._load_vector_db()
    
    def _create_vector_db(self, documents: List[Document]) -> None:
        """
        Create a new vector database from documents.
        
        Args:
            documents: List of Document objects to embed and store
        """
        print("Creating new vector database...")
        
        self._vectordb = Chroma.from_documents(
            documents=documents,
            embedding=self.embedding_model,
            persist_directory=self.persist_directory
        )
        
        # Persist the database to disk
        self._vectordb.persist()
        
        print(f"Vector database created and persisted at {self.persist_directory}")
    
    def _load_vector_db(self) -> None:
        """Load an existing vector database from disk."""
        print("Loading existing vector database...")
        
        self._vectordb = Chroma(
            persist_directory=self.persist_directory,
            embedding_function=self.embedding_model
        )
        
        print("Vector database loaded successfully.")
    
    def similarity_search(
        self, 
        query: str, 
        k: int = Settings.DEFAULT_TOP_K,
        score_threshold: float = Settings.SIMILARITY_THRESHOLD
    ) -> List[Tuple[Document, float]]:
        """
        Perform similarity search on the vector database.
        
        Args:
            query: The search query string
            k: Number of top results to return
            score_threshold: Minimum similarity score threshold (0-1)
            
        Returns:
            List of tuples containing (Document, similarity_score)
            Only returns results above the threshold
            
        Raises:
            RuntimeError: If vector database is not initialized
        """
        if self._vectordb is None:
            raise RuntimeError(
                "Vector database not initialized. Call initialize() first."
            )
        
        # Get results with similarity scores
        results_with_score = self._vectordb.similarity_search_with_score(query, k=k)
        
        # Filter by threshold
        filtered_results = [
            (doc, score) 
            for doc, score in results_with_score 
            if score >= score_threshold
        ]
        
        return filtered_results
    
    @property
    def is_initialized(self) -> bool:
        """Check if the vector database is initialized."""
        return self._vectordb is not None
    
    def get_collection_count(self) -> int:
        """
        Get the number of documents in the vector store.
        
        Returns:
            Number of documents, or 0 if not initialized
        """
        if not self.is_initialized:
            return 0
        
        try:
            return self._vectordb._collection.count()
        except Exception:
            return 0
