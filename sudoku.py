
import random


if __name__ == "__main__":

    # Set the number of iterations and the number of numbers to select each time
    iterations = 302575350
    num_numbers = 5

    # Create a dictionary to store the count for each number
    counts = {}

    # Iterate over the range of iterations
    for i in range(iterations):
      # Select the numbers using the randint function
      numbers = [random.randint(1, 70) for _ in range(num_numbers)]

      # Increment the count for each number in the list
      for number in numbers:
        if number in counts:
          counts[number] += 1
        else:
          counts[number] = 1

    # Sort the counts in descending order
    sorted_counts = sorted(counts.items(), key=lambda x: x[1], reverse=True)

    # Print the top 5 most repeated numbers
    print(sorted_counts[:5])
