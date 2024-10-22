#import libraries
import sympy as sp
import matplotlib.pyplot as plt
import numpy as np

def analyze_function(function):
    x = sp.symbols('x')
    f = sp.sympify(function)

    # Domain
    domain = sp.calculus.util.continuous_domain(f, x, sp.S.Reals)

    # Intercepts
    x_intercepts = sp.solve(f, x)
    y_intercept = f.subs(x, 0)

    # Derivatives
    f_prime = sp.diff(f, x)
    f_double_prime = sp.diff(f_prime, x)

    # Maxima and minima
    critical_points = sp.solve(f_prime, x)
    maxima_minima = [(p, f.subs(x, p)) for p in critical_points if domain.contains(p)]

    # Vertical asymptotes
    vertical_asymptotes = sp.solve(sp.denom(f), x)

    # Horizontal asymptotes
    limit_inf = sp.limit(f, x, -sp.oo)
    limit_sup = sp.limit(f, x, sp.oo)
    horizontal_asymptotes = []
    if limit_inf.is_finite:
        horizontal_asymptotes.append(limit_inf)
    if limit_sup.is_finite:
        horizontal_asymptotes.append(limit_sup)

    # Intervals of increase and decrease
    increasing_intervals = sp.solveset(f_prime > 0, x, domain)
    decreasing_intervals = sp.solveset(f_prime < 0, x, domain)

    # Concavity and convexity
    concave_intervals = sp.solveset(f_double_prime > 0, x, domain)
    convex_intervals = sp.solveset(f_double_prime < 0, x, domain)

    # Results
    results = {
        "Domain": domain,
        "X Intercepts": x_intercepts,
        "Y Intercept": y_intercept,
        "Maxima and Minima": maxima_minima,
        "Vertical Asymptotes": vertical_asymptotes,
        "Horizontal Asymptotes": horizontal_asymptotes,
        "Increasing Intervals": increasing_intervals,
        "Decreasing Intervals": decreasing_intervals,
        "Concave Intervals": concave_intervals,
        "Convex Intervals": convex_intervals
    }

    return results

def plot_function(function):
    x = sp.symbols('x')
    f = sp.lambdify(x, function, 'numpy')

    x_vals = np.linspace(-10, 10, 400)
    y_vals = f(x_vals)

    plt.plot(x_vals, y_vals, label=str(function))
    plt.axhline(0, color='black',linewidth=0.5)
    plt.axvline(0, color='black',linewidth=0.5)
    plt.grid(color = 'gray', linestyle = '--', linewidth = 0.5)
    plt.legend()
    plt.show()

# Ask the user for the function
function = input("Enter the function you want to analyze: ")

# Analyze the function
results = analyze_function(function)
for key, value in results.items():
    print(f"{key}: {value}")

# Plot the functionz
plot_function(function)