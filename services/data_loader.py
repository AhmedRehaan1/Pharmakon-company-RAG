"""
Data loading service.
Handles loading and parsing product data from JSON files.
"""
import json
from pathlib import Path
from typing import List

from models.product import Product


class DataLoader:
    """Service for loading product data from JSON files."""
    
    @staticmethod
    def load_products_from_json(json_path: Path | str) -> List[Product]:
        """
        Load products from a JSON file.
        
        Args:
            json_path: Path to the JSON file containing product data
            
        Returns:
            List of Product objects
            
        Raises:
            FileNotFoundError: If the JSON file doesn't exist
            json.JSONDecodeError: If the JSON file is malformed
        """
        json_path = Path(json_path)
        
        if not json_path.exists():
            raise FileNotFoundError(f"Product data file not found: {json_path}")
        
        with open(json_path, "r", encoding="utf-8") as f:
            raw_products = json.load(f)
        
        products = [Product.from_dict(product_data) for product_data in raw_products]
        
        return products
    
    @staticmethod
    def validate_products(products: List[Product]) -> bool:
        """
        Validate loaded products for completeness.
        
        Args:
            products: List of Product objects to validate
            
        Returns:
            True if all products are valid
            
        Raises:
            ValueError: If any product is missing required fields
        """
        if not products:
            raise ValueError("No products loaded")
        
        for idx, product in enumerate(products):
            if not product.product_name:
                raise ValueError(f"Product at index {idx} missing product_name")
            if not product.product_link:
                raise ValueError(f"Product at index {idx} missing product_link")
        
        return True
