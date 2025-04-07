# Assuming risk_funcs is a list of callable risk functions
risk_funcs = [
    lambda x: 0,
    lambda x: 2*x
    # Add other risk functions here
]

# Define operation_funcs where each function sums up risk_func(x) for all risk_funcs
operation_funcs = [
    lambda x: sum(risk_func(x) for risk_func in risk_funcs)
    # Add more lambda functions as needed
]

# Now you can use operation_funcs[i] to compute the sum of risk functions for a given x
result = operation_funcs[0](2)  # Compute the sum at x = -1
print(result)