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

```
### instant visualization
```bash

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
```
### Output
```
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
```
### ✨ Why DataViz?

### Before DataViz
```
print(json.dumps(complex_data, indent=2))
# 😵 Hard to understand nested structure
# 🔍 Difficult to spot relationships  
# 📏 No visual hierarchy
```
### With DataViz
```
viz(complex_data)
# 🎯 Instant visual understanding
# 🔗 Clear parent-child relationships
# 🎨 Beautiful, intuitive display
```



