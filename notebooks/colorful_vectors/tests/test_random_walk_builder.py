from notebooks.colorful_vectors.random_walk_builder import define_circle_quarter
import numpy as np

def test_define_circle_quarter():
    angles = [0, np.pi/2, np.pi, 3*np.pi/2, 2*np.pi-0.1, np.pi/4, np.pi/2 + np.pi/4, 12*np.pi]
    answers = [1, 2, 3, 4, 4, 1, 2, 1]
    for idx, angle in enumerate(angles):
        assert define_circle_quarter(angle) == answers[idx]


if __name__ == '__main__':
    test_define_circle_quarter()