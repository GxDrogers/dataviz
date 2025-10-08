from typing import Dict, Any

class Styles:
    TREE = "tree"
    BOXED = "boxed"
    MINIMAL = "minimal"
    ARROW = "arrow"
    PROFESSIONAL = "professional"
    COLORFUL = "colorful"

class Themes:
    """Pre-defined themes for different use cases"""
    
    DEFAULT = {
        "name": "default",
        "icons": {}
    }
    
    PROFESSIONAL = {
        "name": "professional",
        "icons": {
            "dict": "📊", "list": "📑", "tuple": "📄",
            "str": "🔤", "int": "#", "float": "##",
            "bool": "✓" if True else "✗", "none": "∅"
        }
    }
    
    COLORFUL = {
        "name": "colorful", 
        "icons": {
            "dict": "🌈", "list": "🎨", "tuple": "📚",
            "str": "🎯", "int": "🔢", "float": "💯",
            "bool": "💚" if True else "💔", "none": "⚫"
        }
    }
    
    EMOJI = {
        "name": "emoji",
        "icons": {
            "dict": "📦", "list": "📋", "tuple": "📑",
            "str": "🔤", "int": "🔢", "float": "🔢", 
            "bool": "✅" if True else "❌", "none": "🚫"
        }
    }

def get_theme(theme_name: str) -> Dict[str, Any]:
    """Get theme by name"""
    themes = {
        "default": Themes.DEFAULT,
        "professional": Themes.PROFESSIONAL, 
        "colorful": Themes.COLORFUL,
        "emoji": Themes.EMOJI
    }
    return themes.get(theme_name, Themes.DEFAULT)