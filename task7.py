import random
from collections import Counter


def roll_two_dice():
    return random.randint(1, 6) + random.randint(1, 6)


def monte_carlo_simulation(num_trials):
    probabilities = Counter([roll_two_dice() for _ in range(num_trials)])
    percents = {}

    for outcome, count in probabilities.items():
        percents[outcome] = count / num_trials * 100

    return percents


def analytical_probabilities():
    analytical_prob = {
        2: 1 / 36 * 100,
        3: 2 / 36 * 100,
        4: 3 / 36 * 100,
        5: 4 / 36 * 100,
        6: 5 / 36 * 100,
        7: 6 / 36 * 100,
        8: 5 / 36 * 100,
        9: 4 / 36 * 100,
        10: 3 / 36 * 100,
        11: 2 / 36 * 100,
        12: 1 / 36 * 100,
    }

    return analytical_prob


def compare_results(simulation_prob, analytical_prob):
    print("\nПорівняння імовірностей:")
    for outcome, prob in analytical_prob.items():
        simulation_prob_percentage = simulation_prob[outcome]
        print(
            f"Сума {outcome}: Метод Монте-Карло - {simulation_prob_percentage:.2f}%, Аналітичний розрахунок - {prob:.2f}%"
        )


def main():
    num_trials = 1_000_000
    simulation_probabilities = monte_carlo_simulation(num_trials)
    analytical_probabilities_dict = analytical_probabilities()
    compare_results(simulation_probabilities, analytical_probabilities_dict)


if __name__ == "__main__":
    main()
