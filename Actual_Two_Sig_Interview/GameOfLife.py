# ## Conway's Game Of Life
# ## -- Write a function to compute a board after n generations given initial board state
#
# ## Rules
# # If a cell has more than 3 neighbors -- dies due to overcrowding
# # If a cell has less than 2 neighbors -- dies due to loneliness
# # If a dead cell has exactly 2 neighbors -- it will be born
#
#
# # Given
# # 0 0 1 0 1
# # 1 0 0 0 0
# # 0 0 0 1 0
# # 0 0 1 0 0
#
# # after 1st generation
# # 0 0 0 0 0
# # 0 0 0 0 0
# # 0 1 1 0 0
# # 0 0 0 1 0
#
#
# class GameOfLife:
#
#     def __init__(board):
#         self.board = board
#         self.temp_board = board
#         self.row_length = len(board[0])
#         self.column_length = len(board)
#
#     def pass_generations(self, n: int):
#         # for every cell in self.board
#
#         counter = 0
#
#         while counter < n:
#             for j in range(self.column_length):
#                 for i in range(self.row_length):
#                     neighbors = []
#                     # get cell direct to right
#                     right = self.board[i][j + 1]
#                     # get cell direct to left
#                     left = self.board[i][j - 1]
#                     # get cell direct to bottom
#                     bottom = self.board[i + 1][j]
#                     # get cell direct to up
#                     up = self.board[i - 1][j]
#                     # get northeast
#                     northeast = self.board[i - 1][j + 1]
#                     # get northwest
#                     northwest = self.board[i - 1][j - 1]
#                     # get southeast
#                     southeast = self.board[i + 1][j + 1]
#                     # get southwest
#                     southwest = self.board[i + 1][j - 1]
#
#                     neighbors = [right, left, bottom, up, northeast, northwest, southeast, southwest]
#
#                     value_to_place = self.evaluate_life(neighbors, self.board[i][j])
#                     self.temp_board[i][j] = value_to_place
#
#             self.board = self.temp_board
#
#         return self.board
#
#     def handle_wrapping():
#
#     def evaluate_life(self, neighbors: list, curr_life: int):
#         if sum(neighbors) == 3:
#             return curr_life
#         if sum(neighbors) > 3:
#             return 0
#         elif sum(neighbors) < 2:
#             return 0
#         else:
#             return 1
