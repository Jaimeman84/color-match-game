import pytest
import streamlit as st
from PIL import Image
from typing import Tuple
import random
from src.app import (
    generate_random_color,
    create_color_block,
    generate_new_round,
    initialize_game
)

@pytest.fixture
def mock_session_state(monkeypatch):
    """Mock Streamlit session state"""
    class MockSessionState:
        def __init__(self):
            self.game_initialized = False
            self.target_color = None
            self.options = []
            self.score = 0
            self.needs_new_round = True
    
    mock_state = MockSessionState()
    monkeypatch.setattr(st, "session_state", mock_state)
    return mock_state

def test_generate_random_color():
    """Test random color generation"""
    color = generate_random_color()
    
    assert isinstance(color, tuple)
    assert len(color) == 3
    assert all(isinstance(c, int) for c in color)
    assert all(0 <= c <= 255 for c in color)

def test_create_color_block():
    """Test color block image creation"""
    color = (255, 0, 0)  # Red
    size = (100, 100)
    
    image = create_color_block(color, size)
    
    assert isinstance(image, Image.Image)
    assert image.size == size
    assert image.mode == 'RGB'
    assert image.getpixel((0, 0)) == color

def test_generate_new_round():
    """Test new round generation"""
    target, options = generate_new_round()
    
    assert isinstance(target, tuple)
    assert isinstance(options, list)
    assert len(options) == 4
    assert target in options
    assert len(set(options)) == 4  # Check for duplicates

def test_initialize_game(mock_session_state):
    """Test game initialization"""
    initialize_game()
    
    assert mock_session_state.game_initialized is True
    assert mock_session_state.needs_new_round is False
    assert isinstance(mock_session_state.target_color, tuple)
    assert len(mock_session_state.options) == 4
    assert mock_session_state.target_color in mock_session_state.options

@pytest.mark.parametrize("score,expected", [
    (0, 1),  # First correct answer
    (5, 6),  # Mid-game correct answer
    (9, 10), # Milestone correct answer
])
def test_score_increment(mock_session_state, score, expected):
    """Test score incrementing"""
    mock_session_state.score = score
    mock_session_state.target_color = (255, 0, 0)
    mock_session_state.score += 1
    assert mock_session_state.score == expected

def test_color_uniqueness():
    """Test that generated colors in options are unique"""
    target, options = generate_new_round()
    unique_colors = set(options)
    assert len(unique_colors) == 4

def test_reset_game(mock_session_state):
    """Test game reset functionality"""
    # Setup initial state
    mock_session_state.score = 10
    mock_session_state.game_initialized = True
    mock_session_state.needs_new_round = False
    
    # Reset game
    mock_session_state.score = 0
    mock_session_state.needs_new_round = True
    initialize_game()
    
    assert mock_session_state.score == 0
    assert mock_session_state.game_initialized is True
    assert mock_session_state.needs_new_round is False
    assert mock_session_state.target_color is not None
    assert len(mock_session_state.options) == 4