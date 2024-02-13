from solution import fourier_transform


def correct_fourier_transform(x):
    """
    This function computes the Fourier transform of the input signal x.
    Input: x - A list of N real numbers representing the input signal
    Output: A list of N real numbers (Rounded to 2 decimal places) representing the magnitude of the Fourier transform of the input signal
    """

    # Solve without any external libraries
    # Your code here

    # Solution

    # Import the math library
    import math

    # Initialize the result
    result = []

    # Get the length of the input signal
    N = len(x)

    # Loop through each frequency
    for k in range(N):
        # Initialize the real and imaginary parts of the result
        real = 0
        imag = 0

        # Loop through each point in the signal
        for n in range(N):
            # Compute the real and imaginary parts
            real += x[n] * math.cos(2 * math.pi * k * n / N)
            imag -= x[n] * math.sin(2 * math.pi * k * n / N)

        # Add the magnitude to the result
        result.append(round(math.sqrt(real**2 + imag**2), 2))

    # Return the result
    return result


inputs = [
    ([1, 2, 3, 4],),
    ([1, 2, 3, 4, 5],),
    ([1, 2, 3, 4, 5, 6],),
    ([1, 2, 3, 4, 5, 6, 7],),
    ([1, 2, 3, 4, 5, 6, 7, 8],),
]

passed = 0

for input in inputs:
    try:
        assert fourier_transform(*input) == correct_fourier_transform(*input)
        passed += 1
    except:
        pass

score = round(passed / len(inputs) * 100)
print(score)
