"""
Result formatting utilities.
Handles formatting of search results for display and LLM processing.
"""
from typing import List, Tuple

from langchain.schema import Document

from config.settings import Settings


class ResultFormatter:
    """Utility class for formatting search results."""
    
    @staticmethod
    def format_search_results(
        results: List[Tuple[Document, float]]
    ) -> str:
        """
        Format similarity search results into a readable string.
        
        This format is used as context for the LLM to generate recommendations.
        
        Args:
            results: List of (Document, similarity_score) tuples
            
        Returns:
            Formatted string with product details and confidence scores
        """
        if not results:
            return "No results found above the threshold."
        
        output = ""
        for i, (doc, score) in enumerate(results, 1):
            output += f"""Result {i} (Confidence: {score:.2f})

Product Name: {doc.metadata["name"]}
Link: {doc.metadata["link"]}
Price: {doc.metadata["price"]}
Description: {doc.page_content[:Settings.DESCRIPTION_PREVIEW_LENGTH]}

"""
        
        return output
    
    @staticmethod
    def format_single_result(doc: Document, score: float = None) -> str:
        """
        Format a single search result.
        
        Args:
            doc: Document object with product metadata
            score: Optional similarity score
            
        Returns:
            Formatted string for a single product
        """
        result = f"Product Name: {doc.metadata['name']}\n"
        result += f"Link: {doc.metadata['link']}\n"
        result += f"Price: {doc.metadata['price']}\n"
        
        if score is not None:
            result += f"Confidence: {score:.2f}\n"
        
        result += f"Description: {doc.page_content[:Settings.DESCRIPTION_PREVIEW_LENGTH]}"
        
        return result
    
    @staticmethod
    def format_for_display(results: List[Tuple[Document, float]]) -> str:
        """
        Format results for user-friendly display in UI.
        
        Args:
            results: List of (Document, similarity_score) tuples
            
        Returns:
            Formatted string ready for UI display
        """
        if not results:
            return "No products found matching your query."
        
        output = "### Recommended Products\n\n"
        
        for i, (doc, score) in enumerate(results, 1):
            confidence_percent = score * 100
            output += f"**{i}. {doc.metadata['name']}** (Match: {confidence_percent:.0f}%)\n\n"
            output += f"- **Price:** {doc.metadata['price']}\n"
            output += f"- **Link:** [{doc.metadata['link']}]({doc.metadata['link']})\n"
            output += f"- **Description:** {doc.page_content[:200]}...\n\n"
            output += "---\n\n"
        
        return output
