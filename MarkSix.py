import sys
import random

def MarkSixLottery(n):
    """
    :param n: The total number of balls.
    :return:
    """
    draws = 6
    balls = range(1, n+1)
    drawn = []
    for i in range(draws):
        random.shuffle(balls)
        pos = random.randint(0,len(balls)-1)
        drawn.append(balls.pop(pos))
    drawn.sort()
    print drawn

def main():
    trials = sys.argv[1]
    for i in range(trials):
        MarkSixLottery(49)

if __name__ == '__main__':
    main()
