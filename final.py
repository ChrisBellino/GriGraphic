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


def num_grid(rows, columns, min_num, max_num, fill_percentage):

    grid = [[None for _ in range(columns)] for _ in range(rows)]

    def valid_grid(grid, row, col, value):
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
                        if valid_grid(grid, row, col, number):
                            grid[row][col] = number
                            if fill_grid(grid):
                                return True
                            grid[row][col] = None
                    return False
        return True


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

    fill_grid(grid)
    return create_puzzle(grid, fill_percentage)


input_boxes = []


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
                input_boxes.append((input_box, row_position, column_position))
                input_box.draw(win)

    return True
def rules_sudoku(sudoku):
    rows = len(sudoku)
    columns = len(sudoku[0])

    for row in sudoku:
        if len(set(row)) != rows:
            return False

    for column in range(columns):
        column_values = [sudoku[row][column] for row in range(rows)]
        if len(set(column_values)) != columns:
            return False
    for small_gric_row in range(0, rows, 3):
        for small_grid_column in range(0, columns, 3):
            small_grid_values = []
            for r in range(3):
                for c in range(3):
                    small_grid_values.append(sudoku[small_gric_row + r][small_grid_column + c])
            if len(set(small_grid_values)) != 9:
                return False
    return True



def ButtonCheck(win, text, sudoku_puzzle):
    button_rect = Rectangle(Point(220, 600), Point(320, 640))
    button_rect.setFill("grey")
    button_rect.draw(win)
    button_text = Text(Point(270, 620), text)
    button_text.draw(win)

    def Sudoku_check():
        filled_sudoku = []
        for row in range(9):
            complete_row = []
            for column in range(9):
                value = sudoku_puzzle[row][column]
                if value is None:
                    entry_obj = [entry for (entry, r, c) in input_boxes if r == row and c == column][0]
                    input_value = entry_obj.getText()
                    try:
                        complete_row.append(int(input_value))
                    except ValueError:
                        complete_row.append(None)
                else:
                    complete_row.append(value)
            filled_sudoku.append(complete_row)

        if rules_sudoku(filled_sudoku):
            message = "Sudoku is Correct!"
        else:
            message = "Sudoku is Incorrect!"

        result_text = Text(Point(370, 500), message)
        result_text.setTextColor("red")
        result_text.setSize(25)
        result_text.draw(win)


    click_point = win.getMouse()
    x_click, y_click = click_point.getX(), click_point.getY()

    if 220 <= x_click <= 320 and 600 <= 640:
        Sudoku_check()



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


def main():
    difficulty = input("Choose a difficulty (Easy, Medium, Hard): ")

    if difficulty == "Easy":
        percentage = 98
    elif difficulty == "Medium":
        percentage = 40
    elif difficulty == "Hard":
        percentage = 20


    win = GraphWin("Sudoku", 640, 640)
    win.setBackground("white")


    sudoku_puzzle = num_grid(9, 9, 1, 9, percentage)
    grid(win, 9, 9, win.getWidth(), 440)
    textboxes(win, sudoku_puzzle, win.getWidth(), 440)


    ButtonQuit(win, "Quit", win.quit)
    ButtonCheck(win, "Check", sudoku_puzzle)


    win.getMouse()
    win.close()


if __name__ == "__main__":
    main()
