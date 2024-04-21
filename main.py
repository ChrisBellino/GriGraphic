from graphics import *


def draw_grid(win, grid_rows, grid_columns, width, height):
    # Calculate width and height of the grid by taking the total width and height of the window and dividing it by the number of rows and colums
    grid_width = width / grid_columns
    grid_height = height / grid_rows


    for i in range(grid_columns):
        x = i * grid_width
        #Draws a bold line every 3 columns
        if i % 3 == 0 and i != 0:
            bold_line = Line(Point(x, 0), Point(x, height))
            bold_line.setWidth(3)
            bold_line.draw(win)
        else:
            line = Line(Point(x, 0), Point(x, height))
            line.draw(win)

    # Drawing horizontal lines
    for i in range(grid_rows):
        y = i * grid_height
        # Draw bold lines every 3 rows
        if i % 3 == 0 and i != 0:
            bold_line = Line(Point(0, y), Point(width, y))
            bold_line.setWidth(3)
            bold_line.draw(win)
        else:
            line = Line(Point(0, y), Point(width, y))
            line.draw(win)

# Function to create text entry boxes
def textboxes(win, rows, columns, width, height):
    # Calculate width and height of each box
    Box_width = width / columns
    Box_height = height / rows

    # Textboxes for each box in grid
    for row in range(rows):
        for column in range(columns):
            x = column * Box_width + Box_width / 2
            y = row * 47 + Box_height / 2  #if you know how to get the box to place in the center without having
            #to put the 47 in manually I think that would be better
            entry = Entry(Point(x, y), 1)
            entry.draw(win)


def ButtonQuit(win, text, command):
    button_rect = Rectangle(Point(320, 600), Point(420, 640))
    button_rect.setFill("grey")
    button_rect.draw(win)
    button_text = Text(Point(370, 620), text)
    button_text.draw(win)
    click_point = win.getMouse()
    x_click, y_click = click_point.getX(), click_point.getY()

    if 320 <= x_click <= 420 and 600 <= y_click <= 640:
        command()

def ButtonCheck(win, text, command):
    #Button check not working idk why I think its the coorundates of the box placement
    #Also the button does not have a function yet
    button_rect = Rectangle(Point(120, 600), Point(420, 640))
    button_rect.setFill("grey")
    button_rect.draw(win)
    button_text = Text(Point(270, 620), text)
    button_text.draw(win)
    click_point = win.getMouse()
    x_click, y_click = click_point.getX(), click_point.getY()

    if 120 <= x_click <= 420 and 600 <= y_click <= 640:
        command()


def main():
    win = GraphWin("Sudoku", 640, 640)
    win.setBackground("white")

    grid_rows = 9
    grid_columns = 9

    draw_grid(win, grid_rows, grid_columns, win.getWidth(), 440)  # Draw the Sudoku grid
    textboxes(win, grid_rows, grid_columns, win.getWidth(), win.getHeight())  # Create text entry boxes

    # Create Quit button
    closeButton = ButtonQuit(win, "Quit", win.quit)
    closeButton.draw(win)

    # Create Check button
    checkButton = ButtonCheck(win, "Check")
    checkButton.draw(win)

    win.getMouse()
    win.close()

if __name__ == "__main__":
    main()
