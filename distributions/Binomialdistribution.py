import math
import matplotlib.pyplot as plt
from .Generaldistribution import Distribution
import numpy as np


class Binomial(Distribution):
    """ Binomial distribution class for calculating and
    visualizing a Binomial distribution.

    Attributes:
        mean (float) representing the mean value of the distribution
        stdev (float) representing the standard deviation of the distribution
        data_list (list of floats) a list of floats to be extracted from the data file
        p (float) representing the probability of an event occurring
        n (int) the total number of trials

    """

    #       A binomial distribution is defined by two variables:
    #           the probability of getting a positive outcome
    #           the number of trials

    #       If you know these two values, you can calculate the mean and the standard deviation
    #
    #       For example, if you flip a fair coin 25 times, p = 0.5 and n = 25
    #       You can then calculate the mean and standard deviation with the following formula:
    #           mean = p * n
    #           standard deviation = sqrt(n * p * (1 - p))

    #

    def __init__(self, prob=.5, size=20):

        self.p = prob
        self.n = size

        mu = self.calculate_mean()
        sigma = self.calculate_stdev()

        Distribution.__init__(self, mu, sigma)

        #
        #       Then use the init function from the Distribution class to initialize the
        #       mean and the standard deviation of the distribution

    def calculate_mean(self):

        """Function to calculate the mean from p and n

        Args:
            None

        Returns:
            float: mean of the data set

        """

        mean = self.n * self.p
        self.mean = mean

        return mean

    def calculate_stdev(self):

        """Function to calculate the standard deviation from p and n.

        Args:
            None

        Returns:
            float: standard deviation of the data set

        """

        stdev = math.sqrt(self.mean * (1 - self.p))
        self.stdev = stdev

        return stdev

    def replace_stats_with_data(self):

        """Function to calculate p and n from the data set

        Args:
            None

        Returns:
            float: the p value
            float: the n value

        """

        #       updates the n attribute of the binomial distribution
        #       updates the p value of the binomial distribution by calculating the
        #               number of positive trials divided by the total trials

        n = len(self.data)
        p = np.count_nonzero(np.array(self.data) == 1)/len(self.data)

        self.n = n
        self.p = p

        return p, n

    def plot_bar(self):
        """Function to output a histogram of the instance variable data using
        matplotlib pyplot library.

        Args:
            None

        Returns:
            None
        """
        #       For example, say you have a coin where heads = 1 and tails = 0.
        #       If you flipped a coin 35 times, and the coin landed on
        #       heads 20 times and tails 15 times, the bar chart would have two bars:
        #       0 on the x-axis and 15 on the y-axis
        #       1 on the x-axis and 20 on the y-axis

        #       Make sure to label the chart with a title, x-axis label and y-axis label

        plt.bar([0, 1], self.data)
        plt.title('Bar')
        plt.xlabel('Success/Failure')
        plt.ylabel('Count')

    def pdf(self, k):
        """Probability density function calculator for the binomial distribution.

        Args:
            k (float): point for calculating the probability density function


        Returns:
            float: probability density function output
        """
        #   For example, if you flip a coin n = 60 times, with p = .5,
        #   what's the likelihood that the coin lands on heads 40 out of 60 times?

        binomial_coeff = math.factorial(self.n)/(math.factorial(k)*math.factorial(self.n - k))

        pdf = binomial_coeff * self.p**k * (1 - self.p)**(self.n - k)

        return pdf

    def plot_bar_pdf(self):

        """Function to plot the pdf of the binomial distribution

        Args:
            None

        Returns:
            list: x values for the pdf plot
            list: y values for the pdf plot

        """

        # TODO: Use a bar chart to plot the probability density function from
        # k = 0 to k = n

        #   Hint: You'll need to use the pdf() method defined above to calculate the
        #   density function for every value of k.

        #   Be sure to label the bar chart with a title, x label and y label

        #   This method should also return the x and y values used to make the chart
        #   The x and y values should be stored in separate lists

    def __add__(self, other):

        """Function to add together two Binomial distributions with equal p

        Args:
            other (Binomial): Binomial instance

        Returns:
            Binomial: Binomial distribution

        """

        try:
            assert self.p == other.p, 'p values are not equal'
        except AssertionError as error:
            raise

        result = Binomial()
        result.n = other.n + self.n
        result.p = self.p

        return result

    def __repr__(self):

        """Function to output the characteristics of the Binomial instance

        Args:
            None

        Returns:
            string: characteristics of the Gaussian

        """

        return "mean {}, standard deviation {}".format(self.mean, self.stdev)
