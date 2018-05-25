import __init__ as im

# load data NZ Holland
NZ_Holland = im.pythoncode.classes.classes.Stations()
NZ_Holland.stations("data/StationsHolland.csv")
NZ_Holland.railroads("data/ConnectiesHolland.csv")

# load data the Nederlands
Nederland = im.pythoncode.classes.classes.Stations()
Nederland.stations("data/StationsNationaal.csv")
Nederland.railroads("data/ConnectiesNationaal.csv")

parser = im.argparse.ArgumentParser(
    description = """
    This project generates train routes through Noord/Zuid Holland and
    Netherlands with different algorithms. The purpose of this project is to
    optimize the score function and determine the corresponding solution.

    The programm starts with executing the following command:

        python main.py

    and additional arguments can be implemented. The user can choose the
    algortihm, the number iterations and the environment.
    """
    )

parser.add_argument(
    "-hillclimber",
    default = None,
    action = "store_true",
    help = """
    This argument ensures the usage of the hillclimber algorithm.

    Example:

        python main.py -hillclimber -noordzuid -iterations 100

    """
    )

parser.add_argument(
    "-greedy",
    default = None,
    action = "store_true",
    help = """
    This argument ensures the usage of the greedy algorithm.

    Example:

        python main.py -greedy -nederland -iterations 100

    """
    )

parser.add_argument(
    "-dijkstra",
    default = None,
    action = "store_true",
    help = """
    This argument ensures the usage of the dijkstra algorithm.

    Example:

        python main.py -dijkstra -noordzuid

    """
    )

parser.add_argument(
    "-iterations",
    type = int,
    default = "1000",
    help = """
    This argument is optional and determines the number of iterations used for a
    particular algorithm. The default value is set at 1000 iterations.

    Example:

        python main.py -dijkstra -nederland -iterations 200

    """
    )

parser.add_argument(
    "-noordzuid",
    default = None,
    action = "store_true",
    help = """
    This argument specifies the area where the stations are located, in this
    case Noord/Zuid Holland. Noord/Zuid-Holland are two provinces in the Netherlands.
    Multiple trajectories will be chosen in this environment.

    Example:

        python main.py -hillclimber -noordzuid

    """
    )

parser.add_argument(
    "-nederland",
    default = None,
    action = "store_true",
    help = """
    This argument specifies the area where the stations are located, in this
    case the Netherlands as a whole. Multiple trajectories will be chosen in
    this environment.

    Example:

        python main.py -greedy -nederland

    """
    )

args = parser.parse_args()


if args.nederland == True:
    max_t_n = 20
    max_min_n = 180
    if args.hillclimber == True:
        hillclimber = im.hillclimber(Nederland, im.random_solution, im.random_trajectory, max_t_n, max_min_n, args.iterations)
        print("Best score:")
        print(hillclimber.score())
        im.visual_solution(Nederland, hillclimber, "Hillclimber solution (Nederland)")
    elif args.greedy == True:
        score = 0
        greed = []
        for i in range(args.iterations):
            option = im.greedy(Nederland, max_t_n, max_min_n)
            new_score = option.score()
            greed.append(new_score)
            if new_score > score:
                score = new_score
                best_option = option
        print("Best score:")
        print(score)
        im.visual_solution(Nederland, best_option, "Greedy solution (Nederland)")
    elif args.dijkstra == True:
        score = 0
        dijks = []
        for i in range(args.iterations):
            option = im.dijkstra(Nederland, max_t_n, max_min_n)
            new_score = option.score()
            dijks.append(new_score)
            if new_score > score:
                score = new_score
                best_option = option
        print("Best score:")
        print(score)
        im.visual_solution(Nederland, best_option, "Dijkstra solution (Nederland)")

elif args.noordzuid == True:
    max_t_nz = 7
    max_min_nz = 120
    if args.hillclimber == True:
        hillclimber = im.hillclimber(NZ_Holland, im.random_solution, im.random_trajectory, max_t_nz, max_min_nz, args.iterations)
        print("Best score:")
        print(hillclimber.score())
        im.visual_solution(NZ_Holland, hillclimber, "Hillclimber solution (NZ Holland)")
    elif args.greedy == True:
        score = 0
        greed = []
        for i in range(args.iterations):
            option = im.greedy(NZ_Holland, max_t_nz, max_min_nz)
            new_score = option.score()
            greed.append(new_score)
            if new_score > score:
                score = new_score
                best_option = option
        print("Best score:")
        print(score)
        im.visual_solution(NZ_Holland, best_option, "Greedy solution (NZ Holland)")
    elif args.dijkstra == True:
        score = 0
        dijks = []
        for i in range(args.iterations):
            option = im.dijkstra(NZ_Holland, max_t_nz, max_min_nz)
            new_score = option.score()
            dijks.append(new_score)
            if new_score > score:
                score = new_score
                best_option = option
        print("Best score:")
        print(score)
        im.visual_solution(NZ_Holland, best_option, "Dijkstra solution (NZ Holland)")
