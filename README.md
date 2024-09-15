# Natural Camouflage Pattern Generator

This program generates natural camouflage patterns using L-systems (a formal grammar used to model tree-like structures) with randomness and recursion to simulate natural growth. The camouflage patterns resemble organic forms like trees, branches, and natural shapes. The randomness provides a more "organic" appearance by allowing variation in the angles, lengths, and starting points of each "tree." The program also uses a customizable color palette, line thickness, and recursion depth to generate diverse and unique patterns.

The program includes a graphical user interface (GUI) built using Tkinter, allowing users to easily configure parameters such as seed, number of colors, recursion depth, L-system rules, and more. Users can generate, save, and clear patterns within the GUI.

## Features

- **Customizable L-System Parameters**: Adjust axiom, rules, angle, and length for the L-system to create different types of growth patterns.
- **Randomness**: Vary the starting position, angle, and other properties to introduce a natural-looking randomness.
- **Torus Wrapping**: The pattern wraps around the screen like a torus, creating a seamless repeating effect.
- **Save as PNG**: Save your generated patterns as PNG files.
- **Clear/Exit Functionality**: Clear the canvas or exit the application easily.
- **Customizable GUI**: A Tkinter-based interface for easy control of parameters without needing to modify the code directly.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/natural-camo-generator.git
   cd natural-camo-generator
   ```

2. Install the required dependencies:
   ```bash
   pip install pillow
   ```

   Note: The program uses the built-in `turtle` and `tkinter` libraries, which are included with most standard Python installations.

## Usage

1. **Run the Program**: 
   ```bash
   python l-system-camo.py
   ```

2. **Graphical User Interface (GUI)**: 

   - Enter the desired parameters (seed, number of colors, recursion depth, L-system rules, etc.) in the GUI fields.
   - Click the **Draw Pattern** button to generate the pattern.
   - Use the **Save Pattern** button to save the image as a PNG file.
   - Use the **Clear Pattern** button to clear the current pattern.
   - Use the **Exit** button to close the application.

### Parameters

The following parameters can be set through the GUI:

- **Seed**: Controls the randomness; using the same seed will produce the same pattern.
- **Number of Colors**: Specifies how many colors to use from the natural color palette.
- **Number of Loops**: The number of tree-like structures to generate.
- **Recursion Depth**: Controls the depth of recursion for the L-system, which determines how detailed each structure will be.
- **Line Thickness**: Adjusts the thickness of the lines drawn by the turtle.
- **L-System Axiom**: The starting string for the L-system.
- **L-System Rules**: The rules that control how the L-system evolves at each recursion depth.
- **L-System Angle**: The base angle used for turns in the L-system.
- **L-System Length**: The length of each step taken by the turtle for each forward command in the L-system.
- **Random Deviation**: Controls the randomness applied to angles and lengths, creating more organic shapes.
  
### Example

Here’s an example of the parameters you can enter to generate a specific pattern:

- **Seed**: `42`
- **Number of Colors**: `5`
- **Number of Loops**: `15`
- **Recursion Depth**: `3`
- **Line Thickness**: `4`
- **L-System Axiom**: `F`
- **L-System Rules**: `{"F": "FF+[+F-F-F]-[-F+F+F]"}`
- **L-System Angle**: `25`
- **L-System Length**: `10`
- **Random Deviation**: `10`

These settings will generate a natural-looking camouflage pattern with various tree-like structures starting at random positions and angles.

## Natural Color Palette

The program uses a subdued natural color palette that mimics earthy tones, greens, and browns:

```python
COLOR_PALETTE = ['#4a7023', '#8b5a2b', '#3e442b', '#5b7553', '#6e4b26',
                 '#4b5320', '#2f4f2f', '#734f34', '#8c7853', '#5a4b3c']
```

## Saving the Patterns

The **Save Pattern** button allows you to save the current pattern as a PNG file. The program generates an EPS file first, then converts it to PNG using the Pillow library.

## Known Issues

- **White Background**: The background color on the generated image will turn to white when it's saved as a png. You may need to edit this in GIMP or another image editor. It is, however, convenient to have the white if you plan to make that part of the image transparent.

- **Torus Wrapping**: The patterns are designed to wrap around the screen edges, creating a seamless effect. Ensure the patterns don’t get cut off at the edges by experimenting with the number of loops and recursion depth.

  
## License

This project is licensed under the MIT License. Feel free to use, modify, and distribute the code.

---

Happy camouflage pattern generation!
