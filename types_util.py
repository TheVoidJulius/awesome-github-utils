"""A collection of shared type definitions and utilities for the project."""
from typing import Dict, List, Tuple, Optional


# Type aliases for common patterns used across utilities
FileStats = Dict[str, int]
RGBColor = Tuple[int, int, int]
HSLColor = Tuple[int, int, int]
OrganizedFiles = Dict[str, List[str]]
