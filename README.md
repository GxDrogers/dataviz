# DataViz 📊

**Visualize Python data structures as beautiful ASCII mind maps and trees**

[![PyPI version](https://img.shields.io/pypi/v/dataviz.svg)](https://pypi.org/project/dataviz/)
[![Python Versions](https://img.shields.io/pypi/pyversions/dataviz.svg)](https://pypi.org/project/dataviz/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Downloads](https://img.shields.io/pypi/dm/dataviz.svg)](https://pypi.org/project/dataviz/)

**DataViz** is the ultimate Python module for visualizing complex data structures as intuitive ASCII mind maps. Debug APIs, understand JSON responses, and explore nested data with stunning visual clarity.

Created by **Midhun Haridas**

---

## 🚀 Quick Start

### Installation
    ```bash
    pip install dataviz


### instant visualization


    from dataviz import viz
    
    data = {
        'user': {
            'name': 'Midhun', 
            'age': 25,
            'posts': [
                {'title': 'Hello World', 'tags': ['python', 'coding']},
                {'title': 'DataViz Launch!', 'tags': ['opensource']}
            ]
        }
    }

    viz(data)

### Output

    📦 root
    ├── 👤 user
    │   ├── 📛 name: 'Midhun'
    │   ├── 🔢 age: 25
    │   └── 📋 posts
    │       ├── 0
    │       │   ├── ✏️ title: 'Hello World'
    │       │   └── 🏷️ tags
    │       │       ├── 🐍 python
    │       │       └── 💻 coding
    │       └── 1
    │           ├── ✏️ title: 'DataViz Launch!'
    │           └── 🏷️ tags
    │               └── 📦 opensource

### ✨ Why DataViz?

#### Before DataViz

    print(json.dumps(complex_data, indent=2))
    # 😵 Hard to understand nested structure
    # 🔍 Difficult to spot relationships  
    # 📏 No visual hierarchy

#### With DataViz

    viz(complex_data)
    # 🎯 Instant visual understanding
    # 🔗 Clear parent-child relationships
    # 🎨 Beautiful, intuitive display

### 🎯 Key Features

#### 🎨 Multiple Visualization Styles
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

#### 🔍 Smart Search & Highlight
    mind_map = MindMap(complex_data)
    mind_map.search("Midhun")  # Highlights all occurrences
    print(mind_map.render())

### 📊 Advanced Metadata
    # Show data types and memory usage
    viz(data, show_types=True, show_memory=True)

#### Output:
    📦 root
    ├── 👤 user (dict) [48 bytes]
    │   ├── 📛 name: 'Midhun' (str) [54 bytes]
    │   └── 🔢 age: 25 (int) [28 bytes]
### 🎭 Beautiful Themes
    from dataviz import Themes
    
    viz(data, theme=Themes.PROFESSIONAL)
    viz(data, theme=Themes.COLORFUL) 
    viz(data, theme=Themes.EMOJI)
    
### 💾 Multiple Export Formats
    from dataviz import save_mind_map
    
    mind_map = MindMap(data)
    save_mind_map(mind_map, "structure.md")   # Markdown
    save_mind_map(mind_map, "structure.html") # Interactive HTML
    save_mind_map(mind_map, "structure.json") # JSON structure

### 🎯 Focus on Specific Paths
    # Zoom into specific data branches
    viz(data).focus_on("user.posts[0].tags")

### 📚 Comprehensive Usage

#### Basic Usage
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

### From Various Data Sources
    from dataviz import MindMapFactory
    
    # From JSON string
    json_str = '{"menu": {"file": "New"}}'
    mind_map = MindMapFactory.from_json(json_str)
    
    # From file
    mind_map = MindMapFactory.from_file("data.json")
    
    # From URL (requires requests)
    mind_map = MindMapFactory.from_url("https://api.github.com/users/MidhunHaridas")
    
    # From pandas DataFrame
    import pandas as pd
    df = pd.DataFrame({"A": [1, 2], "B": ["x", "y"]})
    viz(df.to_dict())

### Advanced Filtering
    # Filter nodes by custom conditions
    mind_map = MindMap(data)
    
    # Show only nodes with more than 3 children
    filtered = mind_map.filter(lambda node: len(node.children) > 3)
    
    # Show only string values
    filtered = mind_map.filter(lambda node: isinstance(node.value, str))

### Command Line Interface

#### Basic Usage
    # From JSON file
    dataviz data.json
    
    # From URL
    dataviz https://api.github.com/users/MidhunHaridas
    
    # From JSON string
    dataviz '{"name": "Midhun", "age": 25}'
    
    # From stdin
    echo '{"test": "data"}' | dataviz

#### Advanced CLI Options
    # Different styles and themes
    dataviz data.json --style minimal --theme colorful
    
    # Show types and memory
    dataviz data.json --show-types --show-memory
    
    # Search and highlight
    dataviz data.json --search "Midhun"
    
    # Export to file
    dataviz data.json --output structure.html --format html
    dataviz data.json --output structure.md --format md
    
#### Full CLI Help
    dataviz --help

### 🔧 Advanced Examples

#### API Response Visualization
    import requests
    from dataviz import viz
    
    response = requests.get('https://api.github.com/users/MidhunHaridas')
    viz(response.json(), show_types=True)

#### Configuration File Analysis
    import yaml
    from dataviz import viz
    
    with open('config.yaml') as f:
        config = yaml.safe_load(f)
        
    viz(config, style="minimal", show_memory=True)

#### Real-time Data Monitoring
    from dataviz import MindMap
    import time
    
    class LiveDataMonitor:
        def __init__(self):
            self.mind_map = None
        
        def update_data(self, new_data):
            self.mind_map = MindMap(new_data)
            print("\033[2J\033[H")  # Clear terminal
            print(self.mind_map.render())

### 🎨 Customization

#### Creating Custom Themes
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

### 📦 Installation

#### From PyPI (Recommended)
    pip install dataviz

#### From Source
    git clone https://github.com/GxDrogers/dataviz.git
    cd dataviz
    pip install -e .

#### For Development
    git clone https://github.com/GxDrogers/dataviz.git
    cd dataviz
    pip install -e ".[dev]"
    pytest  # Run tests

### 🤝 Contributing

We love contributions! Here's how to help:

 Fork the repository

 Create a feature branch: git checkout -b amazing-feature

 Commit your changes: git commit -m 'Add amazing feature'

 Push to the branch: git push origin amazing-feature

 Open a Pull Request
