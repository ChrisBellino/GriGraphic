from graphics import *
from random import randint, shuffle

def grid(win, rows, columns, width, height):
    grid_width = width / columns
    grid_height = height / rows


    for i in range(1, columns):
        x = i * grid_width
        vert_line = Line(Point(x, 0), Point(x, height))
        if i % 3 == 0:
            vert_line.setWidth(3)
        vert_line.draw(win)


    for i in range(1, rows):
        y = i * grid_height
        horiz_line = Line(Point(0, y), Point(width, y))
        if i % 3 == 0:
            horiz_line.setWidth(3)
        horiz_line.draw(win)
def num_grid(rows, columns, min_num, max_num, gen_num):
    grid = [[None for _ in range(columns)] for _ in range(rows)]

    def is_valid(grid, row, col, value):
        if value in grid[row]:
            return False

        if value in [grid[i][col] for i in range(rows)]:
            return False

        start_row = 3 * (row // 3)
        start_col = 3 * (col // 3)
        for i in range(3):
            for j in range(3):
                if grid[start_row + i][start_col + j] == value:
                    return False

        return True


    def fill_grid(grid):
        for row in range(rows):
            for col in range(columns):
                if grid[row][col] is None:
                    numbers = list(range(min_num, max_num + 1))
                    shuffle(numbers)

                    for number in numbers:
                        if is_valid(grid, row, col, number):
                            grid[row][col] = number
                            if fill_grid(grid):
                                return True
                            grid[row][col] = None
                    return False
        return True

    fill_grid(grid)


    def create_puzzle(grid, fill_percentage):
        puzzle = [row.copy() for row in grid]
        total_cells = rows * columns
        cells_to_remove = int((1 - (fill_percentage / 100)) * total_cells)

        for _ in range(cells_to_remove):
            while True:
                row = randint(0, rows - 1)
                col = randint(0, columns - 1)
                if puzzle[row][col] is not None:
                    puzzle[row][col] = None
                    break

        return puzzle

    return create_puzzle(grid, gen_num)


def textboxes(win, grid, width, height):
    rows = len(grid)
    columns = len(grid[0])
    box_width = width / columns
    box_height = height / rows

    for row_position, row in enumerate(grid):
        for column_position, value in enumerate(row):
            x = (column_position + 0.5) * box_width
            y = (row_position + 0.5) * box_height
            if value is not None:
                text_obj = Text(Point(x, y), str(value))
                text_obj.draw(win)
            else:
                input_box = Entry(Point(x, y), 2)
                input_box.draw(win)

# Function to create a "Quit" button
def ButtonQuit(win, text, command):
    button_rect = Rectangle(Point(320, 600), Point(420, 640))
    button_rect.setFill("grey")
    button_rect.draw(win)
    button_text = Text(Point(370, 620), text)
    button_text.draw(win)

    click_point = win.getMouse()
    x_click, y_click = click_point.getX(), click_point.getY()

    # Correct bounds for click detection
    if 320 <= x_click <= 420 and 600 <= y_click <= 640:
        command()  # Call the command to quit the application

# Function to check if the Sudoku solution is valid
def check_solution(grid):
    def is_valid(row, col, num):
        # Check the row and column for duplicate numbers
        for i in range(9):
            if grid[row][i] == num or grid[i][col] == num:
                return False

        # Check the 3x3 subgrid for duplicates
        start_row, start_col = 3 * (row // 3), 3 * (col // 3)
        for i in range(3):
            for j in range(3):
                if grid[start_row + i][start_col + j] == num:
                    return False
        return True

    # Check all rows, columns, and subgrids for validity
    for row in range(9):
        for column in range(9):
            if grid[row][column] is None or not is_valid(row, column, grid[row][column]):
                return False
    return True


def ButtonCheck(win, text, grid):
    button_rect = Rectangle(Point(120, 600), Point(220, 640))
    button_rect.setFill("grey")
    button_rect.draw(win)
    button_text = Text(Point(170, 620), text)
    button_text.draw(win)

    click_point = win.getMouse()
    x_click, y_click = click_point.getX(), click_point.getY()

    # Correct bounds for click detection
    if 120 <= x_click <= 220 and 600 <= 640:
        if check_solution(grid):
            msg = Text(Point(win.getWidth() / 2, win.getHeight() - 20), "Sudoku solution is correct!")
            msg.setTextColor("green")
            msg.draw(win)
        else:
            msg = Text(Point(win.getWidth() / 2, win.getHeight() - 20), "Sudoku solution is incorrect!")
            msg.setTextColor("red")
            msg.draw(win)

# Main function to set up the Sudoku game
def main():
    difficulty = input("Choose a difficulty (Easy, Medium, Hard): ").capitalize()

    if difficulty == "Easy":
        percentage = 60
    elif difficulty == "Medium":
        percentage = 40
    elif difficulty == "Hard":
        percentage = 20

    win = GraphWin("Sudoku", 640, 640)
    win.setBackground("white")
    random_grid = num_grid(9, 9, 1, 9, percentage)
    grid(win, 9, 9, win.getWidth(), 440)
    textboxes(win, random_grid, win.getWidth(), 440)


    ButtonQuit(win, "Quit", win.quit)
    ButtonCheck(win, "Check", random_grid)


    win.getMouse()
    win.close()

if __name__ == "__main__":
    main()
