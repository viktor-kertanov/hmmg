import numpy as np
import matplotlib.pyplot as plt

class Square:
    def __init__(self, init_coordinate: tuple[int], side_len: int):
        A = [init_coordinate[0], init_coordinate[1]]
        B = [A[0], ]
