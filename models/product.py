"""
Product data models and schemas.
Defines the structure for product data throughout the application.
"""
from typing import Dict, Any
from dataclasses import dataclass
from langchain.schema import Document


@dataclass
class Product:
    """Represents a pharmaceutical product with its details."""
    
    product_name: str
    product_price: str
    product_description: str
    product_link: str
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'Product':
        """
        Create a Product instance from a dictionary.
        
        Args:
            data: Dictionary containing product data
            
        Returns:
            Product instance
        """
        return cls(
            product_name=data.get("product_name", ""),
            product_price=data.get("product_price", ""),
            product_description=data.get("product_description", ""),
            product_link=data.get("product_link", "")
        )
    
    def to_dict(self) -> Dict[str, Any]:
        """
        Convert Product to dictionary.
        
        Returns:
            Dictionary representation of the product
        """
        return {
            "product_name": self.product_name,
            "product_price": self.product_price,
            "product_description": self.product_description,
            "product_link": self.product_link
        }
    
    def to_document(self) -> Document:
        """
        Convert Product to a LangChain Document for vector storage.
        The description is used as page_content, metadata contains other fields.
        
        Returns:
            LangChain Document object
        """
        return Document(
            page_content=self.product_description,
            metadata={
                "name": self.product_name,
                "link": self.product_link,
                "price": self.product_price
            }
        )


class ProductDocument:
    """Helper class for working with product documents."""
    
    @staticmethod
    def from_products(products: list[Product]) -> list[Document]:
        """
        Convert a list of Product objects to LangChain Documents.
        
        Args:
            products: List of Product instances
            
        Returns:
            List of Document objects ready for vector embedding
        """
        return [product.to_document() for product in products]
