DataViz 📊

Visualize Python data structures as beautiful ASCII mind maps and trees

https://img.shields.io/pypi/v/dataviz.svg
https://img.shields.io/pypi/pyversions/dataviz.svg
https://img.shields.io/badge/License-MIT-yellow.svg
https://img.shields.io/pypi/dm/dataviz.svg
https://img.shields.io/github/stars/GxDrogers/dataviz.svg
https://img.shields.io/github/forks/GxDrogers/dataviz.svg

DataViz is the ultimate Python module for visualizing complex data structures as intuitive ASCII mind maps. Debug APIs, understand JSON responses, and explore nested data with stunning visual clarity.

Created by Midhun Haridas
🚀 Quick Start
Installation
bash

pip install dataviz

Instant Visualization
python

from dataviz import viz

data = {
    'user': {
        'name': 'Alice', 
        'age': 30,
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
│   ├── 📛 name: 'Alice'
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

🌐 From Multiple Sources
python

from dataviz import MindMapFactory

# From JSON string, files, URLs, and more
mind_map = MindMapFactory.from_json('{"data": "value"}')
mind_map = MindMapFactory.from_file("data.json")
mind_map = MindMapFactory.from_url("https://api.github.com/users/octocat")

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
dataviz data.json --search "Alice"

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

Integration with Web Frameworks
python

# Flask example
from flask import Flask, jsonify
from dataviz import viz

app = Flask(__name__)

@app.route('/debug')
def debug_route():
    data = {"users": [], "settings": {}}
    viz(data)  # Visualize in console
    return jsonify(data)


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
