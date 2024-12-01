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
if 'game_started' not in st.session_state:
    st.session_state.game_started = False
if 'target_color' not in st.session_state:
    st.session_state.target_color = generate_random_color()
if 'options' not in st.session_state:
    st.session_state.options = []
if 'score' not in st.session_state:
    st.session_state.score = 0
if 'show_success' not in st.session_state:
    st.session_state.show_success = False

# Function to start a new round and refresh target and options
def start_new_round():
    # Generate a new target color
    st.session_state.target_color = generate_random_color()
    st.session_state.options = [st.session_state.target_color]
    st.session_state.show_success = False

    # Generate 3 random distractor colors
    while len(st.session_state.options) < 4:
        option = generate_random_color()
        if option not in st.session_state.options:  # Avoid duplicates
            st.session_state.options.append(option)

    # Shuffle the color options
    random.shuffle(st.session_state.options)
    st.session_state.game_started = True

# Handle game initialization
if not st.session_state.game_started:
    start_new_round()

# Streamlit app UI starts here
st.title("🎨 Color Match Game")
st.write("Welcome to the Color Match Game! Match the target color by selecting the correct option. A fun way to enhance cognitive skills!")

# Display score
# st.sidebar.markdown(f"### Score: {st.session_state.score}")

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
        
        # Create a unique key for each button
        button_key = f"color_option_{i}_{st.session_state.target_color}"
        if st.button(f"Select Option {i + 1}", key=button_key):
            if color == st.session_state.target_color:
                st.session_state.score += 1
                st.session_state.show_success = True
                start_new_round()
            else:
                st.error("❌ Oops! Try again.")

# Show success message if needed
if st.session_state.show_success:
    st.success("🎉 Correct! Great job!")

# Reset game button
if st.button("Reset Game", key="reset_game"):
    st.session_state.score = 0
    start_new_round()

# Footer message
st.write("Enjoy and improve your visual cognitive skills!")

# Debug section (optional, comment out in production)
# st.sidebar.write("Debug Info:")
# st.sidebar.write(st.session_state)