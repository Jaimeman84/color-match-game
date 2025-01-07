# Color Match Game 🎨

A cognitive training game built with Streamlit where players match colors to improve their visual perception skills.

## Features

- 🎯 Random color generation with unique options
- 📊 Score tracking system
- 🔄 Instant feedback and round reset
- 🎮 Simple, intuitive interface
- ✨ Color similarity detection

## Requirements

- Python 3.8+
- Streamlit
- Pillow
- pytest (for development)

## Installation

1. **Clone the repository:**
```bash
git clone https://github.com/jaimeman84/color-match-game.git
cd color-match-game
```

2. **Set up a virtual environment:**
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/MacOS
python -m venv venv
source venv/bin/activate
```

3. **Install the package:**
```bash
# For playing the game
pip install -e .

# For development (includes testing tools)
pip install -e ".[dev]"
```

## Running the Game

```bash
streamlit run src/app/main.py
```

## Game Rules

1. A target color is displayed at the top
2. Four color options appear below
3. Click the option that matches the target color
4. Score points for correct matches
5. Try to achieve the highest score!

## Project Structure

```
color_match_game/
├── src/
│    ├── app.py        # Core game logic
│    ├── config.py      # Game settings
│    ├── types.py       # Type definitions
│    └── utils.py       # Helper functions
├── tests/                 # Test suite
├── requirements.txt       # Dependencies
├── CHANGELOG.md          # Version history
└── README.md             # This file
```

## Development

### Running Tests
```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=src

# Run specific test file
pytest tests/test_app.py
```

### Code Quality Tools
```bash
# Format code
black src/ tests/

# Sort imports
isort src/ tests/

# Type checking
mypy src/ tests/

# Lint code
flake8 src/ tests/
```

## Latest Changes

See [CHANGELOG.md](CHANGELOG.md) for detailed version history.

Recent updates:
- Added score tracking
- Improved color generation
- Fixed round reset issues
- Added unit tests

## Contributing

1. Fork the repository
2. Create your feature branch: `git checkout -b feature/new-feature`
3. Commit changes: `git commit -m 'Add new feature'`
4. Push to branch: `git push origin feature/new-feature`
5. Submit a pull request

## Known Issues

See the [Issues](https://github.com/jaimeman84/color-match-game/issues) page for current bugs and feature requests.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Streamlit for the awesome framework
- Testing tools: pytest, coverage
- Code quality: black, isort, flake8, mypy

## Support

If you have any questions or need help:
1. Check the [Issues](https://github.com/jaimeman84/color-match-game/issues) page
2. Create a new issue
3. Contact: your.email@example.com

---
Made with ❤️ by Jaime Mantilla + AI