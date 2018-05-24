import __init__ as im

NZ_Holland = im.classes.classes.Stations()
NZ_Holland.stations("data/StationsHolland.csv")
NZ_Holland.railroads("data/ConnectiesHolland.csv")

# load data the Nederlands
Nederland = im.classes.classes.Stations()
Nederland.stations("data/StationsNationaal.csv")
Nederland.railroads("data/ConnectiesNationaal.csv")

# visualisation of possible trajectory
visual(NZ_Holland, "Visualisatie NZ Holland")
visual(Nederland, "Visualisatie Nederland")

max_t_n = 20
max_t_nz = 7
max_min_n = 180
max_min_nz = 120

# calculate score for random and cornerstart
random = []
corner = []
random_noreturn = []
corner_noreturn = []
hill_climber = []
greedy_alg = []

for i in range(2):
    random.append(random_sol(NZ_Holland, max_t_nz, max_min_nz).score())
    corner.append(cornerstart(NZ_Holland, max_t_nz, max_min_nz).score())
    random_noreturn.append(random_sol_noreturn(NZ_Holland, max_t_nz, max_min_nz).score())
    corner_noreturn.append(cornerstart_noreturn(NZ_Holland, max_t_nz, max_min_nz).score())
    hill_climber.append(hillclimber(NZ_Holland, random_sol, random_trajectory_noreturns, max_t_nz, max_min_nz).score())
    greedy_alg.append(greedy(NZ_Holland, max_t_nz, max_min_nz).score())

mean_random = sum(random)/len(random)
mean_corner = sum(corner)/len(corner)
mean_random_noreturn = sum(random_noreturn)/len(random_noreturn)
mean_corner_noreturn = sum(corner_noreturn)/len(corner_noreturn)
mean_hillclimber = sum(hill_climber)/len(hill_climber)
mean_greedy = sum(greedy_alg)/len(greedy_alg)

lijst = [mean_random, mean_random_noreturn, mean_corner, mean_corner_noreturn]
print(lijst)


print("RANDOM_SOL:")
print(mean_random)
print("UITHOEKSOL:")
print(mean_corner)
print("RANDOM_SOL NO RETURN:")
print(mean_random_noreturn)
print("UITHOEKSOL NO RETURN:")
print(mean_corner_noreturn)
print("HILLCLIMBER")
print(mean_hillclimber)
print("GREEDY")
print(mean_greedy)
print(max(greedy_alg))

visual_sol(NZ_Holland, random_sol_noreturn(NZ_Holland, max_t_nz, max_min_nz))

###################################################################
########## HOLLAND

n_random = []
n_corner = []
n_random_noreturn = []
n_corner_noreturn = []
n_hill_climber = []
n_greedy_alg = []

for i in range(2):
    n_random.append(random_sol(Nederland, max_t_n, max_min_n).score())
    n_corner.append(cornerstart(Nederland, max_t_n, max_min_n).score())
    n_random_noreturn.append(random_sol_noreturn(Nederland, max_t_n, max_min_n).score())
    n_corner_noreturn.append(cornerstart_noreturn(Nederland, max_t_n, max_min_n).score())
    n_hill_climber.append(hillclimber(Nederland, random_sol, random_trajectory_noreturns, max_t_n, max_min_n).score())
    n_greedy_alg.append(greedy(Nederland, max_t_n, max_min_n).score())

mean_n_random = sum(n_random)/len(n_random)
mean_n_corner = sum(n_corner)/len(n_corner)
mean_n_random_noreturn = sum(n_random_noreturn)/len(n_random_noreturn)
mean_n_corner_noreturn = sum(n_corner_noreturn)/len(n_corner_noreturn)
mean_n_hillclimber = sum(n_hill_climber)/len(n_hill_climber)
mean_n_greedy = sum(n_greedy_alg)/len(n_greedy_alg)

lijst = [mean_n_random, mean_n_random_noreturn, mean_n_corner, mean_n_corner_noreturn]
print(lijst)


print("RANDOM_SOL:")
print(mean_n_random)
print(max(n_random))
print("UITHOEKSOL:")
print(mean_n_corner)
print(max(n_corner))
print("RANDOM_SOL NO RETURN:")
print(mean_n_random_noreturn)
print(max(n_random_noreturn))
print("UITHOEKSOL NO RETURN:")
print(mean_n_corner_noreturn)
print(max(n_corner_noreturn))
print("HILLCLIMBER")
print(mean_n_hillclimber)
print(max(n_hill_climber))
print("GREEDY")
print(mean_n_greedy)
print(max(n_greedy_alg))

visual_sol(Nederland, random_sol_noreturn(Nederland, max_t_n, max_min_n))


######## VOORBEELD HISTOGRAM


greed = []
for i in range(100):
    greed.append(greedy(NZ_Holland, 7, 120).score())
hist(greed, "Histogram Greedy")


##### parser
import __init__ as im

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
    number of itterations
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
        hillclimber = im.hillclimber(Nederland, im.random_solution2, im.random_trajectory2, max_t_n, max_min_n, args.iterations)
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
        hillclimber = im.hillclimber(NZ_Holland, im.random_solution2, im.random_trajectory2, max_t_n, max_min_n, args.iterations)
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
