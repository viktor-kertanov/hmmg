# from pyaxidraw import axidraw  
from axidraw_interactive.custom_method import CustomAxiDraw
import time
import numpy as np

ad = CustomAxiDraw()
ad.plot_setup("vpype/output/final_for_axi.svg")
output = ad.plot_run(True, sleep_timer_sec=10)

while output:
    ad.plot_setup(output)
    ad.options.mode = "res_home"
    output = ad.plot_run(True)
    time.sleep(5)
    print(f'Sleeping now 5')

    ad.plot_setup()
    ad.options.mode = "manual"
    ad.options.manual_cmd = "walk_mmx"
    clean_distance_x = 300 + np.random.randint(0, 30)
    ad.options.dist = clean_distance_x
    ad.plot_run()
    ad.options.manual_cmd = "walk_mmy"
    clean_distance_y = np.random.randint(0,30)
    ad.options.dist = clean_distance_y
    ad.plot_run()
    time.sleep(3)
    print(f'Sleeping now 3')


    for _ in range(3):
        ad.options.manual_cmd = "lower_pen"
        ad.options.pen_pos_down = 5
        ad.plot_run()
        time.sleep(1)
        ad.options.manual_cmd = "walk_x"
        ad.options.dist = 1
        ad.plot_run()
        ad.options.manual_cmd = "walk_x"
        ad.options.dist = -1
        ad.plot_run()
        ad.options.manual_cmd = "walk_y"
        ad.options.dist = 1
        ad.plot_run()
        ad.options.manual_cmd = "walk_y"
        ad.options.dist = -1
        ad.plot_run()
        ad.options.manual_cmd = "raise_pen"
        ad.options.pen_pos_up = 80
        ad.plot_run()
        time.sleep(1)


    ad.options.manual_cmd = "walk_mmx"
    ad.options.dist = -clean_distance_x
    ad.plot_run()
    ad.options.manual_cmd = "walk_mmy"
    ad.options.dist = -clean_distance_y
    ad.plot_run()
    time.sleep(5)
    print(f'Sleeping now 5')

    ad.plot_setup(output)
    ad.options.mode = "res_plot"
    output = ad.plot_run(True)
