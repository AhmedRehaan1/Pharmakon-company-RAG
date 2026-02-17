"""
Streamlit UI application.
Handles all user interface logic and presentation.
"""
import streamlit as st

from config.settings import Settings
from services.recommendation import RecommendationService


def render_header():
    """Render the application header with logo and title."""
    col1, col2 = st.columns([1, 5])
    
    with col1:
        # Display logo if it exists
        if Settings.LOGO_PATH.exists():
            st.image(str(Settings.LOGO_PATH), width=Settings.LOGO_WIDTH)
    
    with col2:
        st.title(Settings.APP_TITLE)


def render_sidebar():
    """Render the sidebar with company information."""
    with st.sidebar:
        st.header("About")
        st.write(f"**Address:** {Settings.COMPANY_INFO['address']}")
        st.write(f"**Mobile:** {Settings.COMPANY_INFO['mobile']}")
        st.write(f"**Email:** {Settings.COMPANY_INFO['email']}")


def render_search_interface(recommendation_service: RecommendationService):
    """
    Render the main search interface.
    
    Args:
        recommendation_service: Initialized RecommendationService instance
    """
    query = st.text_input("Enter your search query:")
    
    if query:
        with st.spinner("Searching for products..."):
            recommendation = recommendation_service.get_recommendations(query)
        
        if recommendation:
            st.write(recommendation)
        else:
            st.write("We have no products matching your query.")


def run_app(recommendation_service: RecommendationService):
    """
    Run the Streamlit application.
    
    This is the main entry point for the UI layer.
    
    Args:
        recommendation_service: Initialized RecommendationService instance
    """
    # Configure page
    st.set_page_config(
        page_title=Settings.APP_TITLE,
        page_icon="💊",
        layout="wide"
    )
    
    # Render UI components
    render_header()
    render_sidebar()
    render_search_interface(recommendation_service)
