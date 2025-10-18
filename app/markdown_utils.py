"""
Markdown processing utilities for safe HTML rendering.
"""
import markdown
from bleach import clean


def markdown_to_html(text: str) -> str:
    """
    Convert markdown text to safe HTML.
    
    Args:
        text: Raw markdown text from the user
        
    Returns:
        Safe HTML string ready for display
    """
    if not text:
        return ""
    
    # Convert markdown to HTML
    html = markdown.markdown(
        text,
        extensions=[
            'markdown.extensions.fenced_code',
            'markdown.extensions.tables',
            'markdown.extensions.nl2br',
            'markdown.extensions.sane_lists',
        ]
    )
    
    # Define allowed HTML tags and attributes for safety
    allowed_tags = [
        'p', 'br', 'strong', 'em', 'u', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6',
        'blockquote', 'code', 'pre', 'ul', 'ol', 'li', 'a', 'img', 'table',
        'thead', 'tbody', 'tr', 'th', 'td', 'hr', 'div', 'span',
    ]
    
    allowed_attributes = {
        'a': ['href', 'title'],
        'img': ['src', 'alt', 'title'],
        'code': ['class'],
        'pre': ['class'],
    }
    
    # Clean and sanitize HTML
    safe_html = clean(
        html,
        tags=allowed_tags,
        attributes=allowed_attributes,
        strip=True
    )
    
    return safe_html
