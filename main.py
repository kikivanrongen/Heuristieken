import __init__ as im

# load data NZ Holland
NZ_Holland = im.classes.classes.Stations()
NZ_Holland.stations("data/StationsHolland.csv")
NZ_Holland.railroads("data/ConnectiesHolland.csv")

# load data the Nederlands
Nederland = im.classes.classes.Stations()
Nederland.stations("data/StationsNationaal.csv")
Nederland.railroads("data/ConnectiesNationaal.csv")

parser = im.argparse.ArgumentParser(
    description = """
    This project generates train routes with different algorithms.
    """
    )

parser.add_argument(
    "-hillclimber",
    type = str,
    default = None,
    action = "store_true",
    help = """
    description of the hillclimber with example
    """
    )

parser.add_argument(
    "-greedy",
    type = str,
    default = None,
    action = "store_true",
    help = """
    description of the greedy with example
    """
    )

parser.add_argument(
    "-dijkstra",
    type = str,
    default = None,
    action = "store_true",
    help = """
    description of the dijkstra with example
    """
    )

parser.add_argument(
    "-iterations",
    type = int,
    default = "1000",
    action = "store_true",
    help = """
    number of iterations
    """
    )

parser.add_argument(
    "-noordzuid",
    type = str,
    default = None,
    action = "store_true",
    help = """
    data of noord-zuid holland
    """
    )

parser.add_argument(
    "-nederland",
    type = str,
    default = None,
    action = "store_true",
    help = """
    data of netherlands
    """
    )

args = parser.parse_args()


if args.nederland:
    max_t_n = 20
    max_min_n = 180
    if args.hillclimber:
        hillclimber = im.hillclimber(Nederland, im.random_solution, im.random_trajectory, max_t_n, max_min_n, args.iterations)
        im.visual_sol(Nederland, hillclimber)
    elif args.greedy:
        score = 0
        greed = []
        for i in range(args.iterations):
            option = im.greedy(Nederland, max_t_n, max_min_n)
            new_score = option.score()
            greed.append(new_score)
            if new_score > score:
                score = new_score
                best_option = option
        im.visual_sol(Nederland, best_option)
    elif args.dijkstra:
        score = 0
        dijks = []
        for i in range(args.iterations):
            option = im.dijkstra(Nederland, max_t_n, max_min_n)
            new_score = option.score()
            dijks.append(new_score)
            if new_score > score:
                score = new_score
                best_option = option
        im.visual_sol(Nederland, best_option)

elif args.noordzuid:
    max_t_nz = 7
    max_min_nz = 120
    if args.hillclimber:
        hillclimber = im.hillclimber(NZ_Holland, im.random_solution, im.random_trajectory, max_t_n, max_min_n, args.iterations)
        im.visual_sol(NZ_Holland, hillclimber)
    elif args.greedy:
        score = 0
        greed = []
        for i in range(args.iterations):
            option = im.greedy(NZ_Holland, max_t_n, max_min_n)
            new_score = option.score()
            greed.append(new_score)
            if new_score > score:
                score = new_score
                best_option = option
        im.visual_sol(NZ_Holland, best_option)
    elif args.dijkstra:
        score = 0
        dijks = []
        for i in range(args.iterations):
            option = im.dijkstra(NZ_Holland, max_t_n, max_min_n)
            new_score = option.score()
            dijks.append(new_score)
            if new_score > score:
                score = new_score
                best_option = option
        im.visual_sol(NZ_Holland, best_option)
