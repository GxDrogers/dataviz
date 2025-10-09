from typing import Any, Dict, List, Optional, Union, Callable
from dataclasses import dataclass
import json
import sys
from pathlib import Path
from datetime import datetime

@dataclass
class Node:
    """Represents a node in the mind map"""
    key: str
    value: Any
    depth: int
    parent: Optional['Node'] = None
    children: List['Node'] = None
    path: str = ""
    data_type: str = ""
    memory_size: int = 0
    
    def __post_init__(self):
        if self.children is None:
            self.children = []
        self.data_type = type(self.value).__name__
        self.memory_size = self._calculate_memory()

    def _calculate_memory(self) -> int:
        """Calculate approximate memory usage"""
        try:
            return sys.getsizeof(self.value)
        except:
            return 0

class MindMap:
    """Main class for creating mind maps from data structures"""
    
    def __init__(self, data: Any, style: str = "tree", show_icons: bool = True, 
                 show_types: bool = False, show_memory: bool = False,
                 max_depth: Optional[int] = None, theme: Optional[Dict] = None):
        self.data = data
        self.style = style
        self.show_icons = show_icons
        self.show_types = show_types
        self.show_memory = show_memory
        self.max_depth = max_depth
        self.theme = theme or {}
        self.root = self._build_tree("root", data, 0)
        self._highlighted_nodes = set()
    
    def _build_tree(self, key: str, value: Any, depth: int, parent: Node = None, path: str = "") -> Node:
        """Recursively build tree structure from data"""
        if self.max_depth and depth > self.max_depth:
            return Node(key=key, value="...", depth=depth, parent=parent, path=path)
            
        node = Node(key=key, value=value, depth=depth, parent=parent, path=path)
        
        if isinstance(value, dict):
            for k, v in value.items():
                child_path = f"{path}.{k}" if path else k
                child = self._build_tree(k, v, depth + 1, node, child_path)
                node.children.append(child)
        elif isinstance(value, (list, tuple)):
            for i, item in enumerate(value):
                child_path = f"{path}[{i}]" if path else f"[{i}]"
                child = self._build_tree(str(i), item, depth + 1, node, child_path)
                node.children.append(child)
        
        return node
    
    def _get_icon(self, value: Any, key: str = "") -> str:
        """Get appropriate icon for data type"""
        if not self.show_icons:
            return ""
        
        # Custom theme icons
        if self.theme.get('icons'):
            custom_icons = self.theme['icons']
            if key in custom_icons:
                return custom_icons[key] + " "
        
        # Smart icon detection based on key names
        key_lower = key.lower()
        icon_rules = {
            'name': '📛', 'username': '👤', 'user': '👤', 'email': '📧',
            'age': '🎂', 'title': '✏️', 'description': '📝',
            'id': '🆔', 'url': '🌐', 'link': '🔗', 'website': '🌐',
            'phone': '📞', 'address': '🏠', 'location': '📍',
            'price': '💰', 'cost': '💰', 'amount': '💰',
            'date': '📅', 'time': '⏰', 'created': '📅', 'updated': '🔄',
            'status': '📊', 'active': '✅', 'enabled': '✅', 'disabled': '❌',
            'count': '🔢', 'total': '🔢', 'size': '📏',
            'file': '📄', 'image': '🖼️', 'photo': '🖼️',
            'password': '🔒', 'token': '🔑', 'key': '🔑',
            'tags': '🏷️', 'categories': '📑',
        }
        
        if key_lower in icon_rules:
            return icon_rules[key_lower] + " "
        
        # Type-based icons
        type_icons = {
            dict: "📦", list: "📋", tuple: "📑",
            str: "🔤", int: "🔢", float: "🔢",
            bool: "✅" if value else "❌", 
            type(None): "🚫"
        }
        
        for data_type, icon in type_icons.items():
            if isinstance(value, data_type):
                return icon + " "
        return "• "
    
    def _render_node(self, node: Node, prefix: str = "", is_last: bool = True) -> str:
        """Render a single node with proper connectors"""
        icon = self._get_icon(node.value, node.key)
        is_highlighted = node.path in self._highlighted_nodes
        
        # Apply highlighting
        highlight_prefix = "🔸 " if is_highlighted else ""
        
        if node.depth == 0:
            line = f"{highlight_prefix}{icon}{node.key}\n"
        else:
            connectors = self._get_connectors(is_last)
            line = f"{prefix}{connectors['node']}{highlight_prefix}{icon}{node.key}"
            
            # Add metadata
            metadata_parts = []
            if self.show_types and not isinstance(node.value, (dict, list, tuple)):
                metadata_parts.append(f"({node.data_type})")
            if self.show_memory and node.memory_size > 0:
                metadata_parts.append(f"[{node.memory_size} bytes]")
            
            metadata = " ".join(metadata_parts)
            if metadata:
                line += f" {metadata}"
            
            # Show primitive values inline
            if not isinstance(node.value, (dict, list, tuple)) and node.value is not None:
                line += f": {repr(node.value)}"
            line += "\n"
        
        # Build new prefix for children
        if node.depth > 0:
            new_prefix = prefix + connectors['child_prefix']
        else:
            new_prefix = ""
        
        # Render children
        for i, child in enumerate(node.children):
            is_last_child = i == len(node.children) - 1
            line += self._render_node(child, new_prefix, is_last_child)
        
        return line
    
    def _get_connectors(self, is_last: bool) -> Dict[str, str]:
        """Get connector characters based on style"""
        connectors = {
            "tree": {
                "node": "└── " if is_last else "├── ",
                "child_prefix": "    " if is_last else "│   "
            },
            "minimal": {
                "node": "╰─ " if is_last else "├─ ",
                "child_prefix": "   " if is_last else "│  "
            },
            "arrow": {
                "node": "➤ ",
                "child_prefix": "  "
            },
            "boxed": {
                "node": "└─ " if is_last else "├─ ",
                "child_prefix": "   " if is_last else "│  "
            }
        }
        return connectors.get(self.style, connectors["tree"])
    
    def render(self) -> str:
        """Render the complete mind map as ASCII art"""
        return self._render_node(self.root).rstrip()
    
    def __str__(self) -> str:
        return self.render()
    
    def search(self, query: str) -> 'MindMap':
        """Highlight nodes matching search query"""
        self._highlighted_nodes.clear()
        
        def search_node(node: Node, current_path: str = ""):
            path = f"{current_path}.{node.key}" if current_path else node.key
            query_lower = query.lower()
            
            # Search in keys and string values
            if query_lower in node.key.lower():
                self._highlighted_nodes.add(node.path)
            elif isinstance(node.value, str) and query_lower in node.value.lower():
                self._highlighted_nodes.add(node.path)
            elif isinstance(node.value, (int, float)) and query in str(node.value):
                self._highlighted_nodes.add(node.path)
            
            for child in node.children:
                search_node(child, path)
        
        search_node(self.root)
        return self
    
    def filter(self, predicate: Callable[[Node], bool]) -> 'MindMap':
        """Filter nodes based on predicate function"""
        def filter_node(node: Node) -> Optional[Node]:
            if predicate(node):
                filtered_node = Node(
                    key=node.key, value=node.value, depth=node.depth,
                    parent=node.parent, path=node.path
                )
                for child in node.children:
                    filtered_child = filter_node(child)
                    if filtered_child:
                        filtered_node.children.append(filtered_child)
                return filtered_node
            return None
        
        filtered_root = filter_node(self.root)
        if filtered_root:
            self.root = filtered_root
        return self
    
    def focus_on(self, path: str) -> 'MindMap':
        """Focus on a specific path in the data structure"""
        path_parts = path.split('.')
        current_node = self.root
        
        for part in path_parts:
            found = False
            for child in current_node.children:
                if child.key == part:
                    current_node = child
                    found = True
                    break
            if not found:
                # Try array access [index]
                if part.startswith('[') and part.endswith(']'):
                    try:
                        index = int(part[1:-1])
                        for child in current_node.children:
                            if child.key == str(index):
                                current_node = child
                                found = True
                                break
                    except ValueError:
                        pass
                if not found:
                    raise ValueError(f"Path not found: {path}")
        
        self.root = current_node
        self.root.depth = 0
        self.root.parent = None
        return self


def xray(data: Any, **kwargs) -> None:
    """One-liner function for quick data structure x-ray"""
    mind_map = MindMap(data, **kwargs)
    print(mind_map.render())
    
# Factory methods for different data sources
class MindMapFactory:
    @staticmethod
    def from_json(json_str: str, **kwargs) -> MindMap:
        data = json.loads(json_str)
        return MindMap(data, **kwargs)
    
    @staticmethod
    def from_file(file_path: Union[str, Path], **kwargs) -> MindMap:
        with open(file_path, 'r') as f:
            if file_path.endswith('.json'):
                data = json.load(f)
            else:
                data = f.read()
        return MindMap(data, **kwargs)
    
    @staticmethod
    def from_url(url: str, **kwargs) -> MindMap:
        try:
            import requests
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()
            return MindMap(data, **kwargs)
        except ImportError:
            raise ImportError("Requests library required for URL support")