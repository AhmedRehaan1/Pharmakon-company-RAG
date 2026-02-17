"""
Recommendation service.
Handles product recommendation logic using LLM and vector search.
"""
from typing import List, Tuple, Optional

from langchain.schema import Document
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

from config.settings import Settings
from config.prompts import Prompts
from services.vector_store import VectorStoreManager
from utils.formatters import ResultFormatter


class RecommendationService:
    """
    Service for generating product recommendations.
    Combines vector search with LLM-based reasoning.
    """
    
    def __init__(self, vector_store: VectorStoreManager):
        """
        Initialize the recommendation service.
        
        Args:
            vector_store: Initialized VectorStoreManager instance
        """
        self.vector_store = vector_store
        self.llm = ChatOpenAI(
            model=Settings.LLM_MODEL,
            temperature=Settings.LLM_TEMPERATURE
        )
        self.prompt_template = ChatPromptTemplate.from_template(
            Prompts.RECOMMENDATION_PROMPT
        )
    
    def get_recommendations(
        self, 
        query: str, 
        k: int = Settings.DEFAULT_TOP_K
    ) -> Optional[str]:
        """
        Generate product recommendations based on user query.
        
        This method:
        1. Queries the vector database for similar products
        2. Formats the results
        3. Uses LLM to generate intelligent recommendations
        
        Args:
            query: User's query describing their needs/symptoms
            k: Number of top products to consider
            
        Returns:
            LLM-generated recommendation text, or None if no results found
        """
        # Step 1: Query vector database
        search_results = self.vector_store.similarity_search(query, k=k)
        
        if not search_results:
            return None
        
        # Step 2: Format search results as context
        formatted_context = ResultFormatter.format_search_results(search_results)
        
        # Step 3: Generate LLM recommendation
        final_prompt = self.prompt_template.format(
            context=formatted_context,
            input=query
        )
        
        response = self.llm.invoke(final_prompt)
        
        return response.content
    
    def get_raw_search_results(
        self, 
        query: str, 
        k: int = Settings.DEFAULT_TOP_K
    ) -> List[Tuple[Document, float]]:
        """
        Get raw search results without LLM processing.
        Useful for debugging or when direct results are needed.
        
        Args:
            query: Search query string
            k: Number of top results to return
            
        Returns:
            List of (Document, score) tuples
        """
        return self.vector_store.similarity_search(query, k=k)
