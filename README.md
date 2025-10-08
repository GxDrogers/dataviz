DataViz 📊

Visualize Python data structures as beautiful ASCII mind maps and trees

https://img.shields.io/pypi/v/dataviz.svg
https://img.shields.io/pypi/pyversions/dataviz.svg
https://img.shields.io/badge/License-MIT-yellow.svg
https://img.shields.io/pypi/dm/dataviz.svg

DataViz is the ultimate Python module for visualizing complex data structures as intuitive ASCII mind maps. Debug APIs, understand JSON responses, and explore nested data with stunning visual clarity.
🚀 Quick Start
Installation
bash

pip install dataviz

Instant Visualization
python

from dataviz import viz

data = {
    'user': {
        'name': 'Midhun', 
        'age': 23,
        'posts': [
            {'title': 'Hello World', 'tags': ['python', 'coding']},
            {'title': 'DataViz Rocks!', 'tags': ['opensource']}
        ]
    }
}

viz(data)

Output:
text

📦 root
├── 👤 user
│   ├── 📛 name: 'Midhun'
│   ├── 🔢 age: 30
│   └── 📋 posts
│       ├── 0
│       │   ├── ✏️ title: 'Hello World'
│       │   └── 🏷️ tags
│       │       ├── 🐍 python
│       │       └── 💻 coding
│       └── 1
│           ├── ✏️ title: 'DataViz Rocks!'
│           └── 🏷️ tags
│               └── 📦 opensource

✨ Why DataViz?
Before DataViz
python

print(json.dumps(complex_data, indent=2))
# 😵 Hard to understand nested structure
# 🔍 Difficult to spot relationships  
# 📏 No visual hierarchy

With DataViz
python

viz(complex_data)
# 🎯 Instant visual understanding
# 🔗 Clear parent-child relationships
# 🎨 Beautiful, intuitive display

🎯 Key Features
🎨 Multiple Visualization Styles
python

from dataviz import MindMap, Styles

data = {'api': {'users': [], 'settings': {}}}

# Tree style (default)
viz(data, style=Styles.TREE)

# Minimal style
viz(data, style=Styles.MINIMAL)

# Arrow style  
viz(data, style=Styles.ARROW)

# Boxed style
viz(data, style=Styles.BOXED)

🔍 Smart Search & Highlight
python

mind_map = MindMap(complex_data)
mind_map.search("Midhun")  # Highlights all occurrences
print(mind_map.render())

📊 Advanced Metadata
python

# Show data types and memory usage
viz(data, show_types=True, show_memory=True)

Output:
text

📦 root
├── 👤 user (dict) [48 bytes]
│   ├── 📛 name: 'Midhun' (str) [54 bytes]
│   └── 🔢 age: 30 (int) [28 bytes]

🎭 Beautiful Themes
python

from dataviz import Themes

viz(data, theme=Themes.PROFESSIONAL)
viz(data, theme=Themes.COLORFUL) 
viz(data, theme=Themes.EMOJI)

💾 Multiple Export Formats
python

from dataviz import save_mind_map

mind_map = MindMap(data)
save_mind_map(mind_map, "structure.md")   # Markdown
save_mind_map(mind_map, "structure.html") # Interactive HTML
save_mind_map(mind_map, "structure.json") # JSON structure

🎯 Focus on Specific Paths
python

# Zoom into specific data branches
viz(data).focus_on("user.posts[0].tags")

📚 Comprehensive Usage
Basic Usage
python

from dataviz import viz, MindMap

# One-liner magic
viz(your_data)

# Full control
mind_map = MindMap(
    data=your_data,
    style="tree",           # tree, minimal, arrow, boxed
    show_icons=True,        # Enable smart icons
    show_types=False,       # Show data types
    show_memory=False,      # Show memory usage
    max_depth=None          # Limit visualization depth
)
print(mind_map.render())

From Various Data Sources
python

from dataviz import MindMapFactory

# From JSON string
json_str = '{"menu": {"file": "New"}}'
mind_map = MindMapFactory.from_json(json_str)

# From file
mind_map = MindMapFactory.from_file("data.json")

# From URL (requires requests)
mind_map = MindMapFactory.from_url("https://api.github.com/users/octocat")

# From pandas DataFrame
import pandas as pd
df = pd.DataFrame({"A": [1, 2], "B": ["x", "y"]})
viz(df.to_dict())

Advanced Filtering
python

# Filter nodes by custom conditions
mind_map = MindMap(data)

# Show only nodes with more than 3 children
filtered = mind_map.filter(lambda node: len(node.children) > 3)

# Show only string values
filtered = mind_map.filter(lambda node: isinstance(node.value, str))

🛠️ Command Line Interface
Basic Usage
bash

# From JSON file
dataviz data.json

# From URL
dataviz https://api.github.com/users/octocat

# From JSON string
dataviz '{"name": "John", "age": 30}'

# From stdin
echo '{"test": "data"}' | dataviz

Advanced CLI Options
bash

# Different styles and themes
dataviz data.json --style minimal --theme colorful

# Show types and memory
dataviz data.json --show-types --show-memory

# Search and highlight
dataviz data.json --search "Midhun"

# Export to file
dataviz data.json --output structure.html --format html
dataviz data.json --output structure.md --format md

Full CLI Help
bash

dataviz --help

usage: dataviz [-h] [--style {tree,minimal,arrow,boxed}] [--theme {default,professional,colorful,emoji}]
               [--output OUTPUT] [--format {txt,md,html,json}] [--search SEARCH] [--show-types] [--show-memory] [--no-icons]
               [input]

Visualize data structures as ASCII mind maps

positional arguments:
  input                 Input file, URL, or JSON string

options:
  -h, --help            show this help message and exit
  --style {tree,minimal,arrow,boxed}
                        Visualization style
  --theme {default,professional,colorful,emoji}
                        Icon theme
  --output OUTPUT, -o OUTPUT
                        Output file
  --format {txt,md,html,json}
                        Output format
  --search SEARCH, -s SEARCH
                        Search and highlight text
  --show-types          Show data types
  --show-memory         Show memory usage
  --no-icons            Hide icons

🔧 Advanced Examples
API Response Visualization
python

import requests
from dataviz import viz

response = requests.get('https://api.github.com/users/octocat')
viz(response.json(), show_types=True)

Configuration File Analysis
python

import yaml
from dataviz import viz

with open('config.yaml') as f:
    config = yaml.safe_load(f)
    
viz(config, style="minimal", show_memory=True)

Database Schema Visualization
python

# With SQLAlchemy
from dataviz import viz
from my_app.models import User

viz(User.__dict__, style="professional")

Real-time Data Monitoring
python

from dataviz import MindMap
import time

class LiveDataMonitor:
    def __init__(self):
        self.mind_map = None
    
    def update_data(self, new_data):
        self.mind_map = MindMap(new_data)
        print("\033[2J\033[H")  # Clear terminal
        print(self.mind_map.render())

🎨 Customization
Creating Custom Themes
python

from dataviz import MindMap

custom_theme = {
    "name": "my_theme",
    "icons": {
        "user": "👨💻",
        "email": "📨", 
        "created_at": "🕒",
        "dict": "🗂️",
        "list": "📜",
        "str": "🔤",
        "int": "🔟"
    }
}

viz(data, theme=custom_theme)

Custom Connector Styles
python

# Extend the MindMap class for custom rendering
class CustomMindMap(MindMap):
    def _get_connectors(self, is_last: bool):
        return {
            "node": "→ " if is_last else "├ ",
            "child_prefix": "  " if is_last else "│ "
        }

📦 Installation Options
From PyPI (Recommended)
bash

pip install dataviz

From Source
bash

git clone https://github.com/GxDrogers/dataviz.git
cd dataviz
pip install -e .

For Development
bash

git clone https://github.com/GxDrogers/dataviz.git
cd dataviz
pip install -e ".[dev]"
pytest  # Run tests

🔗 Integration Examples
Jupyter Notebooks
python

from dataviz import viz
from IPython.display import display, HTML

# Inline visualization
viz(complex_data)

# Export to HTML in notebook
from dataviz import save_mind_map
save_mind_map(MindMap(data), "notebook_output.html")
display(HTML("notebook_output.html"))

Django Debug Toolbar
python

# In settings.py
def show_context_data(request):
    from dataviz import viz
    viz(request.__dict__)

Pytest Debugging
python

# In tests/conftest.py
import pytest
from dataviz import viz

@pytest.fixture(autouse=True)
def debug_data(request):
    def print_data(data, description=""):
        if request.config.getoption("verbose") > 0:
            print(f"\n=== {description} ===")
            viz(data)
    return print_data

FastAPI Documentation
python

from fastapi import FastAPI
from dataviz import save_mind_map
import json

app = FastAPI()

@app.on_event("startup")
async def generate_docs():
    schema = json.loads(app.openapi())
    save_mind_map(MindMap(schema), "api_schema.html")

🤝 Contributing

We love contributions! Here's how to help:

    Fork the repository

    Create a feature branch: git checkout -b amazing-feature

    Commit your changes: git commit -m 'Add amazing feature'

    Push to the branch: git push origin amazing-feature

    Open a Pull Request

Development Setup
bash

git clone https://github.com/GxDrogers/dataviz.git
cd dataviz
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -e ".[dev]"
pre-commit install

Running Tests
bash

pytest tests/ -v
pytest tests/ --cov=dataviz --cov-report=html

📄 License

This project is licensed under the MIT License - see the LICENSE file for details.
🙏 Acknowledgments

    Author: Midhun Haridas

    Inspiration: Every developer who struggled with complex JSON structures

    Special Thanks: The Python community for amazing tooling and support

📞 Support

    Documentation: GitHub Wiki

    Issues: GitHub Issues

    Email: midhunharidas0@gmail.com

🚀 Ready to Visualize?

bash

pip install dataviz

Star the repo ⭐ if you find DataViz useful!

https://img.shields.io/github/stars/GxDrogers/dataviz.svg?style=social
https://img.shields.io/github/forks/GxDrogers/dataviz.svg?style=social

DataViz: See your data structures, don't just read them. 🎯
