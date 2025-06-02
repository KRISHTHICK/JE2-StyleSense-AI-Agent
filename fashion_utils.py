from PIL import Image
import random

def get_fashion_style(image):
    styles = ["Streetwear", "Bohemian", "Formal", "Casual", "Chic", "Sporty"]
    return random.choice(styles)

def generate_color_combos(image):
    color_suggestions = [
        ["Black", "Gold"],
        ["Navy Blue", "White"],
        ["Olive Green", "Beige"],
        ["Maroon", "Cream"],
        ["Grey", "Rust Orange"]
    ]
    return random.choice(color_suggestions)
