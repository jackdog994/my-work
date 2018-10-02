"""
Logic problem from https://www.reddit.com/r/dailyprogrammer_ideas/comments/96et5l/intermediaterobogarden/

A gardener with a passion for technology decides to use a swarm of robots to irrigate the flower beds in his garden.
He wishes to use water from the spring situated at the end of the main path which crosses the garden. Each garden bed
has its own robot, and each robot must water a single garden bed. All the robots start from the spring to water the
garden beds at the same time in the morning (for example, at 5:00:00) and work in parallel, without stopping, for a
given amount of time. They go through the main path until reaching their flower bed, which they water and then return
to the spring to refill their water supply. When time runs out, all the robots stop immediately, regardless of their
current state. Initially, there is a single tap available at the spring. The gardener notices delays in the watering
schedule due to the robots having to wait in line for refilling their water supply. As such, he considers that the best
solution is to install additional water taps. Each morning, all robots start the day with a full water supply.
Two robots cannot fill their water supply from the same tap at the same time.
"""

from collections import defaultdict


def taps_calculator(time, distance, watering):
    """
    :param time: Integer, time frame to measure for watering to occur
    :param distance: List of distances to each flower bed
    :param watering: List of time to water each flower bed
    :return: The minimum number of extra taps required to ensure no queues to water.
    """

    steps = defaultdict(int)

    if len(distance) != len(watering):
        print('Please ensure the distance and watering times have the same amount of values!')
        return

    for i in range(0, len(distance)):
        trip = 0
        while trip <= time:
            trip += (distance[i]*2 + watering[i] + 1)
            steps[trip] += 1
            trip += 1

    print(f"A minimum of {max(steps.values())} extra taps are required.")


taps_calculator(32, [1, 2, 1, 2, 1], [1, 3, 2, 1, 3])
