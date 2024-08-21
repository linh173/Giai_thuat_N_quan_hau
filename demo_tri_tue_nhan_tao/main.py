import tkinter as tk
class n_quan_hau:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("N Quân Hậu")
        self.window.resizable(width=False, height=False)
        self.canvas = tk.Canvas(self.window, width=400, height=400, background= "Silver")
        self.canvas.pack()
        self.label = tk.Label(self.window,  text="Nhập số lượng quân hậu:", fg="Silver",font=("Arial", 13))
        self.label.pack(side="left", padx=13, pady=10)
        self.entry = tk.Entry(self.window, width=20)
        self.entry.pack(side="left", pady=10)
        self.button = tk.Button(self.window, text="Giải Quyết", fg="blue",background="Silver", font=("Arial", 13), command=self.solve_n_queens)
        self.button.pack(padx=10, side= "top", pady=10)
        self.window.mainloop()
    def print_board(self, board):
        for row in board:
            print(" ".join(row))
    def is_safe(self, board, row, col, n):
        for i in range(n):
            if board[row][i] == "Q" or board[i][col] == "Q":
                return False
        for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
            if board[i][j] == "Q":
                return False
        for i, j in zip(range(row, n, 1), range(col, -1, -1)):
            if board[i][j] == "Q":
                return False
        return True

    def solve(self, board, col, n):
        if col >= n:
            return True
        for i in range(n):
            if self.is_safe(board, i, col, n):
                board[i][col] = "Q"
                self.draw_board(board)
                self.canvas.update()
                self.canvas.after(100)
                if self.solve(board, col + 1, n):
                    return True
                board[i][col] = "."
                self.draw_board(board)
                self.canvas.update()
                self.canvas.after(100)
        return False

    def solve_n_queens(self):
        n = int(self.entry.get())
        board = [["." for i in range(n)] for j in range(n)]
        if self.solve(board, 0, n) == False:
            print("Không tìm thấy giải pháp")
        else:
            self.print_board(board)
    def draw_board(self, board):
        n = len(board)
        cell_size = min(400 // n, 400 // n)
        offset_x = (400 - n * cell_size) // 2
        offset_y = (400 - n * cell_size) // 2
        for row in range(n):
            for col in range(n):
                x1 = col * cell_size
                y1 = row * cell_size
                x2 = x1 + cell_size
                y2 = y1 + cell_size
                color = "white" if (row + col) % 2 == 0 else "gray"
                self.canvas.create_rectangle(x1, y1, x2, y2, fill=color)
                if board[row][col] == "Q":
                    self.canvas.create_oval(x1, y1, x2, y2, fill="red")
gui = n_quan_hau()

