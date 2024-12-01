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

# Function to start a new round and refresh target and options
def start_new_round():
    # Generate a new target color
    target_color = generate_random_color()
    st.session_state['target_color'] = target_color
    st.session_state['options'] = [target_color]

    # Generate 3 random distractor colors
    while len(st.session_state['options']) < 4:
        option = generate_random_color()
        if option not in st.session_state['options']:  # Avoid duplicates
            st.session_state['options'].append(option)

    # Shuffle the color options
    random.shuffle(st.session_state['options'])

# Streamlit app UI starts here
st.title("🎨 Color Match Game")
st.write("Welcome to the Color Match Game! Match the target color by selecting the correct option. A fun way to enhance cognitive skills!")

# Initialize session state for game variables
if 'target_color' not in st.session_state:
    start_new_round()

# Display the target color block
st.subheader("Target Color:")
target_color_img = create_color_block(st.session_state['target_color'])
st.image(target_color_img, caption="Match this color", width=150)

# Display color options
st.subheader("Choose the Matching Color:")
columns = st.columns(4)
for i, color in enumerate(st.session_state['options']):
    with columns[i]:  # Use columns for side-by-side display
        color_img = create_color_block(color)
        st.image(color_img, width=100, caption=f"Option {i + 1}")
        if st.button(f"Select Option {i + 1}", key=f"color_option_{i}"):  # Button for each color block
            if color == st.session_state['target_color']:
                st.success("🎉 Correct! Great job!")
                start_new_round()  # Start a new round on success
                st.experimental_rerun()  # Rerun the app to display new colors
            else:
                st.error("❌ Oops! Try again.")  # Feedback for incorrect choice

# Footer message
st.write("Enjoy and improve your visual cognitive skills!")