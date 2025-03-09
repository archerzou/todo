def print_heron_estimates(alpha, num_estimates):
    """
    Calculate and print the first num_estimates of the positive square root of alpha
    using Heron's method.

    Parameters:
    alpha (float): A positive real number to find the square root of.
    num_estimates (int): The number of estimates to calculate and print.
    """
    x = alpha / 2  # Initial estimate x1 = α / 2
    count = 0  # Initialize a counter

    while count < num_estimates:
        print(f"{x:.4f}")  # Print the current estimate to 4 decimal places
        x = 0.5 * (x + alpha / x)  # Calculate the next estimate using Heron's method
        count += 1  # Increment the counter

# Test the function
print_heron_estimates(3, 2)
print()  # Just for better readability in output
print_heron_estimates(3, 4)
print()
print_heron_estimates(121.0, 8)
print()
print_heron_estimates(23.0, 7)