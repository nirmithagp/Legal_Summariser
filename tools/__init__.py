"""Tools package placeholders for IDE resolution.

These stubs provide minimal exported functions used by agents. Replace with
real implementations that integrate with your search/indexing logic.
"""
# tools/__init__.py

from .ipc_sections_search_tool import ipc_sections_search_tool
from .legal_precedent_search_tool import legal_precedent_search_tool


__all__ = ["ipc_sections_search_tool", "legal_precedent_search_tool"]