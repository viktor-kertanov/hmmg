import numpy as np
from typing import Union

def get_circle_thetas(input_quarter: int, num_points_per_q=100) -> np.ndarray:
    '''Function that exclude a quarter from a circle points. 
    This is needed, in order to move a vector to a quartere, where the previous vector has not yet been.
    '''
    quarters = [1, 2, 3, 4]
    if input_quarter not in quarters:
        raise ValueError(f"{input_quarter} is not in [1, 2, 3, 4]")
    
    quarters.remove(input_quarter)
    points = np.array([])
    for q in quarters:
        start = (q-1)*np.pi/2
        end = start + np.pi/2 - np.pi/1000
        points = np.append(points, np.linspace(start, end, num_points_per_q))
    
    return points


def define_circle_quarter(angle_rad: float) -> int:
    '''Input is an angle in radians and it can be bigger thatn 2*pi.
    The output is a number of the circle quarter to which the angle belongs.
    '''
    fraction = angle_rad % (2*np.pi)

    if fraction >=0 and fraction < np.pi/2:
        return 1
    elif fraction >= np.pi/2 and fraction < np.pi:
        return 2
    elif fraction >= np.pi and fraction < 3*np.pi/2:
        return 3
    elif fraction >= 3*np.pi/2 and fraction < 2*np.pi:
        return 4
    else:
        raise ValueError(f'{angle_rad} return unexpected result. Fraction = {fraction}')

def get_opposit_quarter(input_angle_rad: float):
    '''Getting the opposite quarter'''
    input_q = define_circle_quarter(input_angle_rad)
    opposition = {1: 3, 2: 4, 3: 1, 4: 2}
    
    return opposition[input_q]

def random_walk_builder(
        num_vectors,
        vector_len,
        vector_len_mu,
        max_x = 100,
        max_y = 100
    ):
    
    cur_coord = (0,0)

    result_coords = [cur_coord]

    for vector_idx in range(num_vectors):
    
        level_x = cur_coord[0] / max_x # measure of leftness / rightness
        level_y = cur_coord[1] / max_y # measure of bottomness / topness
        
        # this is main trend which should be balanced by opposite motion
        mu_scale_x = (0.5 - np.abs(0.5-level_x))*2
        mu_scale_y = (0.5 - np.abs(0.5-level_y))*2

        # even vector_idx scenario
        if vector_idx % 2 ==0:

            if level_x <= 0.5:
                left_right = np.random.randn()*np.pi*mu_scale_x
            else:
                left_right = np.random.randn()*np.pi*mu_scale_x+np.pi
            
            if level_y <= .5:
                top_bottom = np.random.randn()*np.pi*mu_scale_y + np.pi/2
            else:
                top_bottom = np.random.randn()*np.pi*mu_scale_y - np.pi/2
            
            theta = np.random.choice([left_right, top_bottom, (top_bottom+left_right)/2])

        else:
            # odd_vector_idx scenario      
            input_quarter = define_circle_quarter(theta)      
            thetas = get_circle_thetas(input_quarter)  
            theta = np.random.choice(thetas)
        
        cur_coord = (
            cur_coord[0]+np.cos(theta)*vector_len*(1+np.random.rand()*vector_len_mu),
            cur_coord[1]+np.sin(theta)*vector_len*(1+np.random.rand()*vector_len_mu)
        )
        result_coords.append(cur_coord)
    
    return result_coords

def get_vector_chain_from_points(coordinate_chain: list[tuple]):
    vector_chain = []
    
    for idx, coordinate in enumerate(coordinate_chain[1:], start=1):
        vector_chain.append((coordinate_chain[idx-1], coordinate))
    
    return vector_chain
        

if __name__ == '__main__':
    print('Hello world!')