# shapes_module.py

### importing maodules ###########
import matplotlib.pyplot as plt
import numpy as np  # Import NumPy for mathematical operations
import matplotlib.patches as patches
import random


def setup_figure(title="Shape Playground"):
  # Define a list of random greeting messages
    greetings = [
        "Let's blast off into Python and shapes!",
        "You’ve got this — every coder starts with one line!",
        "Be curious, be creative, be awesome!",
        "Math + Code = Magic — let’s explore!",
        "Ready to think like a scientist?",
        "Keep going! Every shape you draw makes you smarter!",
        "Let’s solve some geometry puzzles together!",
        "Your imagination is the limit — create your world with code!",
        "Coding power activated — let’s build something cool!",
        "Make math colorful with Python shapes!",
        "Adventure time! Let’s discover what code can do!",
        "Every click is a step into the world of creators!",
        "Turn your ideas into reality — one line of code at a time!",
        "Let’s play with numbers and make them dance!",
        "Ready to unlock the secrets of shapes and patterns?",
        "Your brain is your superpower — let’s use it!",
        "Imagine it, code it, make it happen!",
        "Let’s turn math into art with Python!",
        "Curiosity leads to discovery — let’s start coding!",
        "Welcome to the coding playground — have fun exploring!"
     ]

    greeting = random.choice(greetings) # Randomly select one
    
    """Create and return a new figure and axis."""
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 5)
    # Turn on grid with light gray color
    ax.grid(True, color='lightgray')

    #ax.set_aspect('equal')
    ax.set_title(title,  fontsize=12, color='navy', weight='bold')
    #ax.axis('off')

    # Add the greeting message at the top of the figure
    fig.text(0.5, 0.97, greeting, ha='center', va='center', fontsize=10, color='gray', style='italic', weight='ultralight')
    
    return fig, ax

def setup_Flag(title="Shape Playground"):
  # Define a list of random greeting messages
    greetings = [
        "Let's blast off into Python and shapes!",
        "You’ve got this — every coder starts with one line!",
        "Be curious, be creative, be awesome!",
        "Math + Code = Magic — let’s explore!",
        "Ready to think like a scientist?",
        "Keep going! Every shape you draw makes you smarter!",
        "Let’s solve some geometry puzzles together!",
        "Your imagination is the limit — create your world with code!",
        "Coding power activated — let’s build something cool!",
        "Make math colorful with Python shapes!",
        "Adventure time! Let’s discover what code can do!",
        "Every click is a step into the world of creators!",
        "Turn your ideas into reality — one line of code at a time!",
        "Let’s play with numbers and make them dance!",
        "Ready to unlock the secrets of shapes and patterns?",
        "Your brain is your superpower — let’s use it!",
        "Imagine it, code it, make it happen!",
        "Let’s turn math into art with Python!",
        "Curiosity leads to discovery — let’s start coding!",
        "Welcome to the coding playground — have fun exploring!"
     ]

    greeting = random.choice(greetings) # Randomly select one
    
    """Create and return a new figure and axis."""
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 5)
    #ax.set_aspect('equal')
    ax.set_title(title,  fontsize=12, color='navy', weight='bold')
    ax.axis('off')

    # Add the greeting message at the top of the figure
    fig.text(0.5, 0.97, greeting, ha='center', va='center', fontsize=9, color='gray', style='italic', weight='ultralight')
    
    return fig, ax



def star_points(center, outer_radius=0.25, inner_radius=0.1, num_points=5):
    cx, cy = center
    points = []
    angle = np.pi / 2  # Start from top point
    for i in range(num_points * 2):
        r = outer_radius if i % 2 == 0 else inner_radius
        x = cx + r * np.cos(angle)
        y = cy + r * np.sin(angle)
        points.append((x, y))
        angle += np.pi / num_points
    return points