from scipy.optimize import minimize

# Define the objective function
def objective(x, c):
    return sum(c[i]*x[i] for i in range(len(x)))

# Define the constraint functions
def constraint1(x):
    return x[0]**2 + x[1]**2 - 25

def constraint2(x):
    return 7*x[0] + 8*x[1] - 56

# Define the Lagrangian function
def lagrangian(x, c, lambdas):
    return objective(x, c) - sum(lambdas[i]*f(x) for i, f in enumerate([constraint1, constraint2]))

# Define a function to solve the problem
def solve_NLPP():
    # Get the coefficients from user input
    n = int(input("Enter the number of variables: "))
    c = [float(input(f"Enter the coefficient for x{i}: ")) for i in range(n)]
    
    # Get the constraint functions from user input
    m = int(input("Enter the number of constraints: "))
    constraints = []
    for i in range(m):
        c = [float(input(f"Enter the coefficient for x{i}: ")) for i in range(n)]
        b = float(input("Enter the constant: "))
        constraints.append((c, b))
    
    # Define the initial point for the optimizer
    x0 = [1]*n
    
    # Solve the problem using the SLSQP method
    sol = minimize(lagrangian, x0, args=(c, [0]*m), method='SLSQP', constraints=[{'type': 'ineq', 'fun': f} for f in [constraint1, constraint2]])

    # Print the solution
    print("Solution:")
    print(f"Z = {sol.fun}")
    print(f"x = {sol.x}")

# Call the function to solve the problem
solve_NLPP()
