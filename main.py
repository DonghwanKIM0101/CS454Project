import sys
import getopt
import csv
import GA
import PGA
import random
from tester import Tester


def main():
    pga = False

    try:
        opts, args = getopt.getopt(sys.argv[1:],'p:m:f:')
    except getopt.GetoptError as err:
        print(str(err))
        help()
        sys.exit(1)

    for opt, arg in opts:
        if (opt == '-p'):
            pga = arg
        elif (opt == '-m'):
            mutation_rate = float(arg)
        elif (opt == '-f'):
            fun_name = arg

    f = open('./InitialPopulations/' + fun_name + '_population.csv', 'r')
    rdr = csv.reader(f)
    for line in rdr:
        population = line
    new_population = []
    for parameter in population:
        new_population.append(eval(parameter))
    population = new_population

    population = []
    for _ in range(10):
        sequence = []
        for _ in range(5):
            gene = []
            for _ in range(3):
                gene.append(random.randint(0,20))
            sequence.append(gene)
        population.append(sequence)

    evaluator = Tester()
    evaluator.reset(argnum=3, max_value=20, condition_range=5, error_rate=0.3, correction_range=[])

    if pga == "True":
        best_input, best_value, fitness_step, total_population_size, running_time = PGA.main(population, mutation_rate, fun_name, 2, 1, 30, evaluator) # n, m, k hyperparamter
    else:
        best_input, best_value, fitness_step, total_population_size, running_time = GA.main(population, mutation_rate, fun_name, evaluator)
    print(best_value, fitness_step, total_population_size, running_time)

if __name__ == '__main__':
    main()