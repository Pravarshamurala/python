# Define the input string
bitwise_expr = "1A0B0C1"

# Replace the characters with their respective bitwise operators
bitwise_expr = bitwise_expr.replace('A', ' & ').replace('B', ' | ').replace('C', ' ^ ')

# Evaluate the expression
result = eval(bitwise_expr)

# Print the result
print("Result:", result)
