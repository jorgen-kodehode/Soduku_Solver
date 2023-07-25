#!/env/usr/bin/
import soduku_solver
import time

start_time = time.time()
def main():
    soduku_solver.animate_ascii_board(board=soduku_solver.static_board)
    soduku_solver.solve_board(board=soduku_solver.static_board)
    print("_______________________")
    print("Solved in:")
    print("----%s seconds----" % (time.time() - start_time))
    soduku_solver.animate_ascii_board(board=soduku_solver.static_board)







if __name__ == "__main__":
    main()


