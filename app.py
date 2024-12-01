import streamlit as st
import random
from PIL import Image, ImageDraw

# Function to generate a random color as an RGB tuple
def generate_random_color():
    return tuple(random.randint(0, 255) for _ in range(3))

# Function to create a color block image of given size and color
def create_color_block(color, size=(100, 100)):
    img = Image.new('RGB', size, color)
    return img

# Initialize session states
if 'game_initialized' not in st.session_state:
    st.session_state.game_initialized = False
    st.session_state.target_color = None
    st.session_state.options = []
    st.session_state.score = 0
    st.session_state.needs_new_round = True

def generate_new_round():
    """Generate new colors for the round"""
    target = generate_random_color()
    options = [target]
    
    while len(options) < 4:
        option = generate_random_color()
        if option not in options:  # Avoid duplicates
            options.append(option)
    
    random.shuffle(options)
    return target, options

def initialize_game():
    """Initialize or reset the game state"""
    if not st.session_state.game_initialized or st.session_state.needs_new_round:
        target, options = generate_new_round()
        st.session_state.target_color = target
        st.session_state.options = options
        st.session_state.game_initialized = True
        st.session_state.needs_new_round = False

# Streamlit app UI starts here
st.title("🎨 Color Match Game")
st.write("Welcome to the Color Match Game! Match the target color by selecting the correct option. A fun way to enhance cognitive skills!")

# Initialize game if needed
initialize_game()

# Display the target color block
st.subheader("Target Color:")
target_color_img = create_color_block(st.session_state.target_color)
st.image(target_color_img, caption="Match this color", width=150)

# Display color options
st.subheader("Choose the Matching Color:")
columns = st.columns(4)

# Handle button clicks and game logic
for i, color in enumerate(st.session_state.options):
    with columns[i]:
        color_img = create_color_block(color)
        st.image(color_img, width=100, caption=f"Option {i + 1}")
        
        if st.button(f"Select Option {i + 1}", key=f"color_option_{i}"):
            if color == st.session_state.target_color:
                st.session_state.score += 1
                st.session_state.needs_new_round = True
                # Generate new colors immediately
                target, options = generate_new_round()
                st.session_state.target_color = target
                st.session_state.options = options
                st.rerun()
            else:
                st.error("❌ Oops! Try again!")

# Reset game button
if st.button("Reset Game", key="reset_game"):
    st.session_state.score = 0
    st.session_state.needs_new_round = True
    target, options = generate_new_round()
    st.session_state.target_color = target
    st.session_state.options = options
    st.rerun()

# Footer message
st.write(f"##### 🎉 Success Score: {st.session_state.score}")
st.write("Enjoy and improve your visual cognitive skills!")