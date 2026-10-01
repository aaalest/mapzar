from __future__ import annotations
from dataclasses import dataclass, field


@dataclass
class Category:
    id: str
    name: str  # Raw localized name (e.g., "Свіжі овочі")
    children: list[Category] = field(default_factory=list)  # Subcategories

    @property
    def is_leaf(self) -> bool:
        """Returns True if this category has no subcategories (it's a checkable item)."""
        return len(self.children) == 0
