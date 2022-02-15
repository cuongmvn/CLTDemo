#CLT
import numpy as np
import matplotlib.pyplot as plt


def sampling(L,sample_size):
    return sum([L[np.random.randint(len(L))] for i in range(sample_size)])


def N_sampling(L, sample_size, number_of_sample):
    return [sampling(L, sample_size) for i in range(number_of_sample)]


def distribution(L, sample_size):
    return [L.count(i) for i in range(sample_size)]


def main():
    print("Please enter number of coin toss simulation:")
    n = int(input())
    print("How fair do you want the coin to be? \n"
          "Let's say P is the chance of getting Head,\n"
          "Please put 0 < p < 1:")
    p = float(input())
    L1 = np.random.binomial(1, p, n)
    print("Please enter number of sample size: (20 is a good number)")
    sample_size = int(input())
    print("Please enter number of sample set:")
    N = int(input())
# I decided to draw barchart because it is better in this case.
# Histogram deal with continuous distribution when we have here discrete distribution
# My modification is just small change for the code to show the distribution of increasing sample by color
    # and allow user to input biased coin
    # If there is more time I would like to do more visualization but for now,
    # I want to keep it simple and I don't want to make complicated code with complex library
    layer = 10
    for i in range(layer):
        L2 = N_sampling(L1, sample_size, N//layer*(layer-i))
        L3 = distribution(L2, sample_size)
        plt.bar([i for i in range(sample_size)], L3, color='g', alpha = 1/(layer+1)*(i+1))
    plt.show()


if __name__ == '__main__':
    main()
