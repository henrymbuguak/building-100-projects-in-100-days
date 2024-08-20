# Turtle Graphics Color Extraction and Painting Program

Welcome to the Turtle Graphics Color Extraction and Painting Program! This project showcases how to extract colors from an image and create artistic dot paintings using [Python's Turtle graphics](https://realpython.com/beginners-guide-python-turtle/) module.

## Introduction

This program extracts colors from an image file and uses those colors to generate a 10 by 10 grid of colored dots. It highlights the synergy between image processing and Turtle graphics, offering a creative and visually appealing way to explore Python's capabilities.

## Prerequisites

- [Python 3.12](https://www.python.org/downloads/) installed on your system.
- The `colorgram.py` module installed, which you can get using pip:

    ```sh
    pip install colorgram.py
    ```

## Program Description

The program extracts colors from an image and uses the Turtle graphics module to create a grid of dots:

- **Color Extraction**: The program extracts 20 colors from the provided image (`hirst.jpeg`), returning them as RGB tuples.
- **Dot Painting**: It then uses these colors to draw a 10 by 10 grid of dots, each with a diameter of 20 units, and spaced 50 units apart.

## How the Code Works

- **Color Extraction**: The `colorgram` library extracts colors from an image. The extracted colors are converted into RGB tuples.
- **Turtle Graphics Setup**: The Turtle graphics environment is set up, and the Turtle is positioned to start painting the grid.
- **Dot Drawing**: The Turtle iteratively draws a series of dots, each colored randomly from the extracted palette.
- **Execution Flow**: The program automatically starts the painting process when run and waits for user interaction to close the Turtle graphics window.

## How to Run the Code

Follow these steps to run the Turtle Graphics Color Extraction and Painting Program:

1. Open your terminal or command prompt.
1. Download the code using the following command:

    ```sh
    git clone https://github.com/henrymbuguak/building-100-projects-in-100-days.git
    ```

1. Navigate to the directory `building-100-projects-in-100-days/12-painting-project` where `main.py` is saved.
1. Run the program by executing the command:

    ```sh
    python main.py
    ```

1. Watch as the Turtle creates a grid of colorful dots based on the extracted colors.

## Example Usage

When you run the program, it will extract colors from `hirst.jpeg` and create a vibrant dot painting using those colors. The Turtle graphics window will display the painting, and it will remain open until you click to close it.

This program is a fun and interactive way to combine image processing with Turtle graphics, allowing you to create beautiful dot paintings programmatically. Enjoy your artistic journey!

