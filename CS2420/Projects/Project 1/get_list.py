from random import seed, sample

def get_list(size):
    DATA_SIZE = size
    seed(7)
    data = sample(range(DATA_SIZE * 3), k=DATA_SIZE)
    data.sort()
    return data
