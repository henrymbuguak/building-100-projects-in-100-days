import turtle
import colorsys
import os

def draw_star(t):
    """
    Draws a star of the specified size.
    
    Args:
        t (turtle.Turtle): The turtle object used for drawing.
    """
    t.color("gold")
    t.begin_fill()
    for _ in range(5):
        t.forward(100)
        t.right(144)
        t.forward(100)
        t.left(72)
    t.end_fill()

def draw_spiral(t):
    """
    Draws a spiral pattern.
    
    Args:
        t (turtle.Turtle): The turtle object used for drawing.
    """
    t.speed(0)
    t.color("cyan")
    for i in range(200):
        t.forward(i * 2)
        t.right(121)

def draw_rainbow_circles(t):
    """
    Draws rainbow-colored circles.
    
    Args:
        t (turtle.Turtle): The turtle object used for drawing.
    """
    t.speed(0)
    num_circles = 36
    hue = 0
    for i in range(num_circles):
        color = colorsys.hsv_to_rgb(hue, 1.0, 1.0)
        t.color(color)
        t.circle(100)
        t.right(10)
        hue += 1 / num_circles

def draw_fractal_tree(t):
    """
    Draws a fractal tree.
    
    Args:
        t (turtle.Turtle): The turtle object used for drawing.
    """
    def draw_branch(branch_length):
        if branch_length > 5:
            t.forward(branch_length)
            t.right(20)
            draw_branch(branch_length - 15)
            t.left(40)
            draw_branch(branch_length - 15)
            t.right(20)
            t.backward(branch_length)

    t.color("green")
    t.left(90)
    t.penup()
    t.goto(0, -250)
    t.pendown()
    t.backward(100)
    draw_branch(100)

def draw_spirograph(t):
    """
    Draws a spirograph.
    
    Args:
        t (turtle.Turtle): The turtle object used for drawing.
    """
    t.speed(0)
    t.color("blue")
    for i in range(36):
        t.circle(100)
        t.right(10)

def clear_terminal():
    """
    Clears the terminal screen.
    """
    os.system('cls' if os.name == 'nt' else 'clear')

def prompt_user_choice():
    """
    Prompts the user to select a drawing or exit.
    
    Returns:
        str: The user's choice.
    """
    clear_terminal()
    print("Choose a drawing to run:")
    print("1. Star")
    print("2. Spiral Design")
    print("3. Rainbow Circles")
    print("4. Fractal Tree")
    print("5. Spirograph")
    print("6. Exit")

    choice = input("Enter the number of your choice: ")

    return choice

def main():
    """
    Main function to run the turtle drawings. Prompts the user to choose a drawing and executes the chosen drawing.
    """
    screen = turtle.Screen()
    screen.bgcolor("black")
    t = turtle.Turtle()
    
    options = {
        '1': draw_star,
        '2': draw_spiral,
        '3': draw_rainbow_circles,
        '4': draw_fractal_tree,
        '5': draw_spirograph
    }

    while True:
        choice = prompt_user_choice()

        if not choice.isdigit():
            print("Invalid input. Please enter a number corresponding to your choice.")
            input("Press Enter to continue...")
            continue

        if choice == '6':
            print("Exiting...")
            break

        if choice in options:
            t.clear()
            t.reset()
            options[choice](t)
            input("Press Enter to continue...")
        else:
            print("Invalid choice. Please choose a valid option.")
            input("Press Enter to continue...")

if __name__ == "__main__":
    main()
    turtle.done()
