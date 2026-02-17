"""
Pharmakon Product Recommender - Main Entry Point
A clean architecture application for pharmaceutical product recommendations.
"""
import sys
from pathlib import Path

# Add project root to Python path for imports
sys.path.insert(0, str(Path(__file__).parent))

from config.settings import Settings
from models.product import ProductDocument
from services.data_loader import DataLoader
from services.vector_store import VectorStoreManager
from services.recommendation import RecommendationService
from ui.streamlit_app import run_app


def initialize_application():
    """
    Initialize the application by setting up all required services.
    
    Returns:
        RecommendationService: Fully initialized recommendation service
    """
    # Validate configuration
    Settings.validate()
    
    # Load product data
    print("Loading product data...")
    products = DataLoader.load_products_from_json(Settings.PRODUCTS_JSON_PATH)
    DataLoader.validate_products(products)
    print(f"Loaded {len(products)} products.")
    
    # Convert products to documents
    documents = ProductDocument.from_products(products)
    
    # Initialize vector store
    print("Initializing vector store...")
    vector_store = VectorStoreManager()
    vector_store.initialize(documents)
    print(f"Vector store initialized with {vector_store.get_collection_count()} documents.")
    
    # Initialize recommendation service
    recommendation_service = RecommendationService(vector_store)
    
    return recommendation_service


def main():
    """Main application entry point."""
    try:
        # Initialize all services
        recommendation_service = initialize_application()
        
        # Run the Streamlit UI
        run_app(recommendation_service)
        
    except Exception as e:
        print(f"Error initializing application: {e}")
        raise


if __name__ == "__main__":
    main()


