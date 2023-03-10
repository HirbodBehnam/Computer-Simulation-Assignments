import random

def array_to_latex_cell(array: list[int]) -> str:
    result = "\\makecell{"
    for (index, element) in enumerate(array):
        if index != 0 and index % 5 == 0:
            result += "\\\\"
        result += str(element)
        result += ","
    return result[:-1]  + "}"

def array_to_latex_cell_f(array: list[float]) -> str:
    result = "\\makecell{"
    for (index, element) in enumerate(array):
        if index != 0 and index % 5 == 0:
            result += "\\\\"
        temp = element + 0.5
        result += f'{temp:.{2}f}'
        result += ","
    return result[:-1]  + "}"

def get_random_element(a: list[tuple[int, int, int]]) -> tuple[int, float]:
    """
    Gets a random element from the list based on probabilities.
    Returns the number and the generated random number as the result
    """
    rng = random.random()
    for elem in a:
        if elem[1] < rng and elem[2] > rng:
            return (elem[0], rng)
    raise Exception("hmmm")


CUSTOMERS: list[tuple[int, int, int]] = [(14, 0, 0.2), (16, 0.2, 0.48), (18, 0.48, 0.78), (20, 0.78, 1)]
BREAD_BOUGHT: list[tuple[int, int, int]] = [(1, 0, 0.5), (2, 0.5, 0.65), (3, 0.65, 0.75), (4, 0.75, 1)]

print("\\begin{latin}\\centering\\begin{tabular}{|c|c|c|c|c|c|}")
print("\\hline")
print("Day & Customer RNG & No. Customers & Bread RNG & No. Breads & Total Breads \\\\")
for day in range(10): # for each day...
    customers_in_this_day, customers_in_this_day_rng = get_random_element(CUSTOMERS)
    breads_bought: list[int] = []
    breads_bought_rng: list[float] = []
    for _ in range(customers_in_this_day):
        b_b, b_b_r = get_random_element(BREAD_BOUGHT)
        breads_bought.append(b_b)
        breads_bought_rng.append(b_b_r)
    print("\\hline")
    print(f"{day} & {customers_in_this_day_rng:.{4}f} & {customers_in_this_day} & {array_to_latex_cell_f(breads_bought_rng)} & {array_to_latex_cell(breads_bought)} & {sum(breads_bought)} \\\\")
print("\\hline")
print("\\end{tabular}\\end{latin}")


