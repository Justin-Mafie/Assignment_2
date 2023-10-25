import statistics


def is_outlier(data, test_value):
    # Calculate the mean and standard deviation of the data
    mean = statistics.mean(data)
    std_dev = statistics.stdev(data)

    # Define the outlier range (μ - 3σ, μ + 3σ)
    lower_limit = mean - 3 * std_dev
    upper_limit = mean + 3 * std_dev

    # Check if the test value is an outlier
    if test_value < lower_limit or test_value > upper_limit:
        print(f"{test_value} is an outlier.")
    else:
        print(f"{test_value} is not an outlier.")


# Example usage
data = [10, 15, 20, 25, 30, 100]  # Sample data
test_value = 1000  # Test value

is_outlier(data, test_value)
