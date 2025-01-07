import random
from typing import List, Tuple
from .types import ColorRGB, ColorOptions
from .config import MIN_COLOR_VALUE, MAX_COLOR_VALUE, COLOR_CHANNELS, NUM_OPTIONS

def generate_random_color() -> ColorRGB:
    """Generate a random RGB color tuple"""
    return tuple(random.randint(MIN_COLOR_VALUE, MAX_COLOR_VALUE) 
                for _ in range(COLOR_CHANNELS))

def is_color_similar(color1: ColorRGB, color2: ColorRGB, threshold: int = 30) -> bool:
    """Check if two colors are too similar"""
    return all(abs(c1 - c2) <= threshold 
              for c1, c2 in zip(color1, color2))

def generate_distinct_colors(num_colors: int = NUM_OPTIONS) -> List[ColorRGB]:
    """Generate a list of distinct colors"""
    colors: List[ColorRGB] = []
    attempts = 0
    max_attempts = 100
    
    while len(colors) < num_colors and attempts < max_attempts:
        new_color = generate_random_color()
        if not any(is_color_similar(new_color, existing) 
                  for existing in colors):
            colors.append(new_color)
        attempts += 1
    
    return colors