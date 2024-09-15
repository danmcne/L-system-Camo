import turtle
import random
import tkinter as tk
from tkinter import filedialog
from PIL import Image

# Default settings
DEFAULT_SEED = 42
DEFAULT_NUM_COLORS = 5
DEFAULT_NUM_LOOPS = 20
DEFAULT_RECURSION_DEPTH = 3
DEFAULT_LSYSTEM_AXIOM = "F"
DEFAULT_LSYSTEM_RULES = {"F": "FF+[+F-F-F]-[-F+F+F]"}
DEFAULT_LSYSTEM_ANGLE = 30
DEFAULT_LSYSTEM_LENGTH = 13
DEFAULT_RANDOM_DEVIATION = 8  # Degrees of randomness in direction

# Color palette resembling natural environments (greens, browns, earthy tones)
#COLOR_PALETTE = ['#556b2f', '#8fbc8f', '#6b8e23', '#a0522d', '#deb887',
#                 '#8b4513', '#228b22', '#2e8b57', '#daa520', '#cd853f']
# Subdued natural color palette (earthy tones, dark greens, browns, with subtle accents)
COLOR_PALETTE = ['#4b5320', '#2e3d26', '#6e4b3e', '#3a5f0b', '#4d4b3c',
                 '#5c4033', '#2f4f4f', '#556b2f', '#6b4226', '#3b3c36']


class NaturalCamoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Natural Camouflage Pattern Generator")
        self.root.geometry("400x500")

        # Initialize the turtle graphics
        self.t = turtle.Turtle()
        self.screen = turtle.Screen()
        self.screen.setup(width=600, height=600)
        self.t.speed(0)  # Fastest drawing speed
        self.screen.bgcolor("white")
        self.canvas = self.screen.getcanvas()

        # Create the UI elements
        self.create_widgets()

    def create_widgets(self):
        # Define font size
        font = ('Arial', 12)

        # Seed
        tk.Label(self.root, text="Seed:", font=font).grid(row=0, column=0, padx=10, pady=5)
        self.seed_entry = tk.Entry(self.root, font=font)
        self.seed_entry.insert(0, str(DEFAULT_SEED))
        self.seed_entry.grid(row=0, column=1, padx=10, pady=5)

        # Number of colors
        tk.Label(self.root, text="Number of Colors:", font=font).grid(row=1, column=0, padx=10, pady=5)
        self.num_colors_entry = tk.Entry(self.root, font=font)
        self.num_colors_entry.insert(0, str(DEFAULT_NUM_COLORS))
        self.num_colors_entry.grid(row=1, column=1, padx=10, pady=5)

        # Number of loops
        tk.Label(self.root, text="Number of Loops:", font=font).grid(row=2, column=0, padx=10, pady=5)
        self.num_loops_entry = tk.Entry(self.root, font=font)
        self.num_loops_entry.insert(0, str(DEFAULT_NUM_LOOPS))
        self.num_loops_entry.grid(row=2, column=1, padx=10, pady=5)

        # Recursion depth
        tk.Label(self.root, text="Recursion Depth:", font=font).grid(row=3, column=0, padx=10, pady=5)
        self.recursion_depth_entry = tk.Entry(self.root, font=font)
        self.recursion_depth_entry.insert(0, str(DEFAULT_RECURSION_DEPTH))
        self.recursion_depth_entry.grid(row=3, column=1, padx=10, pady=5)

        # Line thickness
        tk.Label(self.root, text="Line Thickness:", font=font).grid(row=4, column=0, padx=10, pady=5)
        self.line_thickness_entry = tk.Entry(self.root, font=font)
        self.line_thickness_entry.insert(0, str(DEFAULT_RANDOM_DEVIATION))
        self.line_thickness_entry.grid(row=4, column=1, padx=10, pady=5)

        # L-System Axiom
        tk.Label(self.root, text="L-System Axiom:", font=font).grid(row=5, column=0, padx=10, pady=5)
        self.lsystem_axiom_entry = tk.Entry(self.root, font=font)
        self.lsystem_axiom_entry.insert(0, DEFAULT_LSYSTEM_AXIOM)
        self.lsystem_axiom_entry.grid(row=5, column=1, padx=10, pady=5)

        # L-System Rules
        tk.Label(self.root, text="L-System Rules:", font=font).grid(row=6, column=0, padx=10, pady=5)
        self.lsystem_rules_entry = tk.Entry(self.root, font=font)
        self.lsystem_rules_entry.insert(0, str(DEFAULT_LSYSTEM_RULES))
        self.lsystem_rules_entry.grid(row=6, column=1, padx=10, pady=5)

        # L-System Angle
        tk.Label(self.root, text="L-System Angle:", font=font).grid(row=7, column=0, padx=10, pady=5)
        self.lsystem_angle_entry = tk.Entry(self.root, font=font)
        self.lsystem_angle_entry.insert(0, str(DEFAULT_LSYSTEM_ANGLE))
        self.lsystem_angle_entry.grid(row=7, column=1, padx=10, pady=5)

        # L-System Length
        tk.Label(self.root, text="L-System Length:", font=font).grid(row=8, column=0, padx=10, pady=5)
        self.lsystem_length_entry = tk.Entry(self.root, font=font)
        self.lsystem_length_entry.insert(0, str(DEFAULT_LSYSTEM_LENGTH))
        self.lsystem_length_entry.grid(row=8, column=1, padx=10, pady=5)

        # Random Deviation
        tk.Label(self.root, text="Random Deviation:", font=font).grid(row=9, column=0, padx=10, pady=5)
        self.random_deviation_entry = tk.Entry(self.root, font=font)
        self.random_deviation_entry.insert(0, str(DEFAULT_RANDOM_DEVIATION))
        self.random_deviation_entry.grid(row=9, column=1, padx=10, pady=5)

        # Buttons
        tk.Button(self.root, text="Draw Pattern", font=font, command=self.draw_pattern).grid(row=10, column=0, columnspan=2, padx=10, pady=5)
        tk.Button(self.root, text="Save Pattern", font=font, command=self.save_pattern).grid(row=11, column=0, columnspan=2, padx=10, pady=5)
        tk.Button(self.root, text="Clear Pattern", font=font, command=self.clear_pattern).grid(row=12, column=0, columnspan=2, padx=10, pady=5)
        tk.Button(self.root, text="Exit", font=font, command=self.root.quit).grid(row=13, column=0, columnspan=2, padx=10, pady=5)

    def setup(self):
        """Setup the random seed, background color, turtle colors, and line thickness."""
        random.seed(int(self.seed_entry.get()))
        
        # Pick a random background color and set it as screen background
        bg_color = random.choice(COLOR_PALETTE)
        self.screen.bgcolor(bg_color)
        
        # Remove the background color from the palette
        color_palette = COLOR_PALETTE.copy()
        color_palette.remove(bg_color)
        
        # Choose the colors for drawing from the remaining palette
        colors = random.sample(color_palette, int(self.num_colors_entry.get()))
        
        return colors

    def wrap_position(self, x, y):
        """Wrap the position to create a torus-like effect."""
        width = self.screen.window_width() // 2
        height = self.screen.window_height() // 2
        if x > width:
            x = -width + (x - width)
        elif x < -width:
            x = width + (x + width)
        
        if y > height:
            y = -height + (y - height)
        elif y < -height:
            y = height + (y + height)
        
        return x, y

    def generate_lsystem(self, axiom, rules, depth):
        """Generate the L-System string based on axiom and rules."""
        result = axiom
        for _ in range(depth):
            next_result = ""
            for char in result:
                next_result += rules.get(char, char)
            result = next_result
        return result

    def draw_lsystem(self, axiom, rules, angle, length, random_deviation, x, y, start_angle, thickness):
        """Draw the L-System using turtle graphics."""
        self.t.penup()
        self.t.goto(x, y)
        self.t.setheading(start_angle)
        self.t.pensize(thickness)
        self.t.pendown()
        
        lsystem_string = self.generate_lsystem(axiom, rules, int(self.recursion_depth_entry.get()))

        stack = []
        for char in lsystem_string:
            if char == 'F':
                # Move forward
                self.t.forward(length)
                # Get position after moving
                x, y = self.t.position()
                # If the position needs to be wrapped, pick up the pen
                wrapped_x, wrapped_y = self.wrap_position(x, y)
                if (wrapped_x, wrapped_y) != (x, y):
                    self.t.penup()
                    self.t.goto(wrapped_x, wrapped_y)
                    self.t.pendown()
            elif char == '+':
                self.t.right(angle + random.uniform(-random_deviation, random_deviation))
            elif char == '-':
                self.t.left(angle + random.uniform(-random_deviation, random_deviation))
            elif char == '[':
                stack.append((self.t.position(), self.t.heading()))
            elif char == ']':
                pos, head = stack.pop()
                self.t.penup()
                self.t.setposition(pos)
                self.t.setheading(head)
                self.t.pendown()

    def draw_pattern(self):
        """Draw the camouflage pattern with multiple L-System trees."""
        self.t.hideturtle()
        self.t.clear()
        self.screen.tracer(0)  # Turn off animation to draw faster
        
        colors = self.setup()
        
        num_loops = int(self.num_loops_entry.get())
        for _ in range(num_loops):
            # Random position
            x = random.randint(-self.screen.window_width() // 2, self.screen.window_width() // 2)
            y = random.randint(-self.screen.window_height() // 2, self.screen.window_height() // 2)
            
            # Random starting angle
            start_angle = random.uniform(0, 360)
            
            axiom = self.lsystem_axiom_entry.get()
            rules = eval(self.lsystem_rules_entry.get())
            base_angle = float(self.lsystem_angle_entry.get())
            base_length = float(self.lsystem_length_entry.get())
            random_deviation = float(self.random_deviation_entry.get())
            
            # Vary angle, length, and line thickness for each tree
            angle = base_angle + random.uniform(-random_deviation, random_deviation)
            length = base_length + random.uniform(-random_deviation, random_deviation)
            thickness = random.randint(2, 13)
            
            self.t.color(random.choice(colors))

            # Draw the tree with the specified parameters
            self.draw_lsystem(axiom, rules, angle, length, random_deviation, x, y, start_angle, thickness)

        # Hide turtle after drawing
        self.t.hideturtle()
        self.screen.update()

    def save_pattern(self):
        """Save the pattern to a file."""
        # Prompt user for file name
        file_name = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
        if not file_name:
            return

        # Ensure proper canvas initialization
        self.root.update()
        
        # Save the screen output to an EPS file
        self.canvas.postscript(file="temp_output.eps")

        # Convert EPS to PNG using Pillow
        img = Image.open("temp_output.eps")
        img.save(file_name, "png")

        print(f"Pattern saved as {file_name}.")

    def clear_pattern(self):
        """Clear the current pattern."""
        self.t.clear()  # Clear the drawing on the canvas
        self.screen.update()  # Update the screen to reflect changes

if __name__ == "__main__":
    root = tk.Tk()
    app = NaturalCamoApp(root)
    root.mainloop()

