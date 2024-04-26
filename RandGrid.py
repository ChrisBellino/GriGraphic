from graphics import *
from random import randint


# Function to draw the grid
def grid(win, rows, columns, width, height):
    grid_width = width / columns
    grid_height = height / rows

    # Draw vertical lines
    for i in range(1, columns):
        x = i * grid_width
        vert_line = Line(Point(x, 0), Point(x, height))
        if i % 3 == 0:
            vert_line.setWidth(3)
        (vert_line.draw(win))

    # Draw horizontal lines
    for i in range(1, rows):
        y = i * grid_height
        horiz_line = Line(Point(0, y), Point(width, y))
        if i % 3 == 0:
            horiz_line.setWidth(3)
        horiz_line.draw(win)

#creates a number grid
def num_grid(rows, columns, min_val, max_val, fill_percentage):
    grid = []
    for row in range(rows):
        row_list = []
        for _ in range(columns):
            if randint(1, 100) <= fill_percentage:
                row_list.append(randint(min_val, max_val))
            else:
                row_list.append(None)
        grid.append(row_list)
    return grid

# Function to create textboxes based on the grid
def textboxes(win, grid, width, height):
    rows = len(grid)
    columns = len(grid[0])
    box_width = width / columns
    box_height = height / rows

    for row_idx, row_list in enumerate(grid):
        for col_idx, value in enumerate(row_list):
            x = col_idx * box_width + box_width / 2
            y = row_idx * box_height + box_height / 2
            if value is not None:
                text_obj = Text(Point(x, y), str(value))
                text_obj.draw(win)
            else:
                input_box = Entry(Point(x, y), 2)  # Empty text box
                input_box.draw(win)
# Function to create a button that closes the window
def ButtonQuit(win, text, command):
    button_rect = Rectangle(Point(320, 600), Point(420, 640))
    button_rect.setFill("grey")
    button_rect.draw(win)
    button_text = Text(Point(370, 620), text)
    button_text.draw(win)

    click_point = win.getMouse()
    x_click, y_click = click_point.getX(), click_point.getY()

    if 320 <= x_click <= 420 and 600 <= 640:
        command()


def ButtonCheck(win, text, command):
    button_rect = Rectangle(Point(120, 600), Point(220, 640))
    button_rect.setFill("grey")
    button_rect.draw(win)
    button_text = Text(Point(170, 620), text)
    button_text.draw(win)

    click_point = win.getMouse()
    x_click, y_click = click_point.getX(), click_point.getY()

    if 120 <= x_click <= 220 and 600 <= 640:
        command()


def main():
    difficulty = input("Choose a difficulty Easy, Medium, Hard: ")
    if difficulty == "Easy":
        percentage = 40
    elif difficulty == "Medium":
        percentage = 25
    elif difficulty == "Hard":
        percentage = 15
    else:
        print("Enter Valid Difficulty")
        input("Choose a difficulty Easy, Medium, Hard: ")

    win = GraphWin("Sudoku", 640, 640)
    win.setBackground("white")

    #Generates the number grid
    random_grid = num_grid(9, 9, 1, 9, percentage)

    #draw Grid
    grid(win, 9, 9, win.getWidth(), 440)

    # Add textboxes to display random numbers and empty cells
    textboxes(win, random_grid, win.getWidth(), 440)

    # Create a "Quit" button
    ButtonQuit(win, "Quit", win.quit)
    ButtonCheck(win, "Check", ButtonCheck)


    win.getMouse()  # Wait for a final interaction before closing
    win.close()

if __name__:="__main__":
    main()
