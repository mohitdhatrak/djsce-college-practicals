import random

# this is not necessary, directly assume 10 candidates with name and rank in each object, no need to calculate the rank
candidates = [
    {"name": "Alice", "experience": 3, "prev_salary": 10000, "projects": 2},
    {"name": "Bob", "experience": 5, "prev_salary": 12000, "projects": 4},
    {"name": "Charlie", "experience": 2, "prev_salary": 8500, "projects": 1},
    {"name": "David", "experience": 4, "prev_salary": 11000, "projects": 3},
    {"name": "Eva", "experience": 6, "prev_salary": 13500, "projects": 5},
    {"name": "Frank", "experience": 1, "prev_salary": 7500, "projects": 0},
    {"name": "Grace", "experience": 3, "prev_salary": 10500, "projects": 2},
    {"name": "Hannah", "experience": 2, "prev_salary": 9000, "projects": 1},
    {"name": "Ian", "experience": 4, "prev_salary": 11500, "projects": 3},
    {"name": "Julia", "experience": 5, "prev_salary": 15000, "projects": 8},
]

def sort_data(obj):
    return (
        3 * obj["experience"] + 2 * obj["projects"] + obj["prev_salary"],
        obj["name"],
    )

sorted_by_rank = sorted(candidates, key=sort_data, reverse=True)

for i, candidate in enumerate(sorted_by_rank, start=1):
    candidate["rank"] = i
    print(f"Rank {candidate['rank']}: {candidate['name']}")

def hiring_process(candidates_order):
    interview_cost = 1000  # fixed cost per interview for company
    hiring_cost = 0  # cost of hiring new employee + cost of firing prev employee
    # cost of hiring new employee -> 1000 fixed
    # firingCost -> days_worked * pay_per_day
    # total_cost = interview_cost + hiring_cost --> total cost for company per employee
    pay_per_day = 2000
    days_worked = 0
    employee_rank = 100  # random high int value
    company_cost = 0
    formula_cost = 0
    n = len(candidates)
    m = 0  # number of hired employees
    hiring_cost_sum = 0

    print("Rank Interview Hiring TotalCost")
    for i in range(len(candidates_order)):
        position = candidates_order[i] - 1
        if sorted_by_rank[position]["rank"] < employee_rank:
            m += 1
            employee_rank = sorted_by_rank[position]["rank"]
            hiring_cost = 1000 + pay_per_day * days_worked
            hiring_cost_sum += hiring_cost
            days_worked = 1
        else:
            days_worked += 1
            hiring_cost = 0

        total_cost = interview_cost + hiring_cost
        company_cost += total_cost

        print(
            f"{sorted_by_rank[position]['rank']}\t{interview_cost}\t{hiring_cost}\t{total_cost}"
        )

    print("Number of candidates hired:", m)
    print("Total cost of company:", company_cost)

    formula_cost = n * interview_cost + hiring_cost_sum # hiring_cost_sum --> m * hiring_cost i.e. hiring cost of each hired candidate
    print("Total cost of company as per formula:", formula_cost)

# best candidate is rank 1
worst_order = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
print("\nWorst case rank order:", worst_order)
hiring_process(worst_order)

# random_order = random.sample(range(1, 11), 10)
random.shuffle(worst_order) # shuffles the array in place, does not return new array
random_order = worst_order
print("\nRandom rank order:", random_order)
hiring_process(random_order)