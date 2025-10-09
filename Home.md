# 🔍 MXRay Wiki

Welcome to the MXRay documentation! MXRay gives you X-ray vision for your Python data structures through beautiful ASCII mind maps and tree visualizations.

## 🎯 What is MXRay?

MXRay is a Python package that automatically converts complex nested data structures into intuitive ASCII visualizations with smart icons and multiple themes.

### Key Features
- 🎨 **Multiple Visualization Styles** - Tree, minimal, arrow, and boxed styles
- 🔍 **Smart Search & Highlight** - Find and highlight specific data
- 🎭 **Beautiful Themes** - Professional, colorful, and emoji themes
- 💾 **Export Formats** - HTML, Markdown, JSON exports
- 🖥️ **CLI Interface** - Use from command line
- 📊 **Metadata Display** - Data types and memory usage

### Quick Example
```python
from mxray import xray

data = {
    'user': {'name': 'Midhun', 'projects': ['MXRay']},
    'config': {'debug': True}
}

xray(data)
