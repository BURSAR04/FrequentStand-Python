import math

# Function to calculate the mean
def calculate_mean(data):
    return sum(data) / len(data)

# Function to calculate the variance
def calculate_variance(data):
    mean = calculate_mean(data)
    temp = 0
    for value in data:
        temp += (value - mean) ** 2
    return temp / len(data)

# Function to calculate the standard deviation
def calculate_std_dev(data):
    return math.sqrt(calculate_variance(data))

# Function to calculate the frequency of each value in the dataset
def calculate_frequency(data):
    frequency = {}
    for value in data:
        if value in frequency:
            frequency[value] += 1
        else:
            frequency[value] = 1
    return frequency

# Collect dataset from user input
data = []
print()
while True:
    value = input("Enter a value (or 'q' to quit): ")
    if value.lower() == 'q':
        break
    data.append(float(value))

# Calculate and display results
mean = calculate_mean(data)
variance = calculate_variance(data)
std_dev = calculate_std_dev(data)
frequency = calculate_frequency(data)

print("Mean:", mean)
print("Variance:", variance)
print("Standard Deviation:", std_dev)
print("Frequency:")
for value, count in frequency.items():
    print(f"{value}: {count}")

