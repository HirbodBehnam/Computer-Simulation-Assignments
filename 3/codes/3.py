import math
COST = 0.001
ROUND_DIGITS = 3
l = int(input("lambda: "))
m = int(input("mu: "))
c = int(input("server count: "))
# Main calc
rho = l / (c * m)
p0 = ((l / m) ** c) * (1 / math.factorial(c)) * (c * m / (c * m - l))
for n in range(0, c):
    p0 += (l / m) ** n / math.factorial(n)
p0 = 1 / p0
L = c * rho + ((c * rho)**(c+1) * p0) / (c * math.factorial(c) * (1 - rho) ** 2)
w = L / l
wq = w - 1 / m
annualCost = wq * l * 3600 * 24 * 365 * COST
# Round everything
rho = round(rho, ROUND_DIGITS)
p0 = round(p0, ROUND_DIGITS)
L = round(L, ROUND_DIGITS)
w = round(w, ROUND_DIGITS)
wq = round(wq, ROUND_DIGITS)
annualCost = round(annualCost, ROUND_DIGITS)
# Print latex
print("\\begin{gather*}")
print(f"\\rho = \\frac{{\lambda}}{{c \mu}} = \\frac{{{l}}}{{{c} \\times {m}}} = {rho}\\\\")
print(f"P_0 = \\Bigl(\sum_{{n=0}}^{{{c}-1}} \\frac{{(\\frac{{{l}}}{{{m}}})^n}}{{n!}} + (\\frac{{{l}}}{{{m}}}^{{{c}}} \\times \\frac{{1}}{{{c}!}} \\times \\frac{{{c} \\times {m}}}{{{c} \\times {m} - {l}}}\\Bigr)^{{-1}} = {p0}\\\\")
print(f"L = {c} \\times {rho} + \\frac{{({c} \\times {rho})^{{{c}+1}} \\times {p0}}}{{{c} \\times {c}! \\times (1 - {rho})^2}} = {L}\\\\")
print(f"w = \\frac{{{L}}}{{{l}}} = {w}\\\\")
print(f"w_q = w - \\frac{{1}}{{\mu}} = {w} - {1 / m} = {wq}\\\\")
print(f"\\text{{\\lr{{annual cost}}}} = {wq} \\times {l} \\times 3600 \\times 24 \\times 365 \\times {COST} = {annualCost}\\$")
print("\\end{gather*}")
