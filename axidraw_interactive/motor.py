# from pyaxidraw import axidraw  
from axidraw_interactive.custom_method import CustomAxiDraw
import time
import numpy as np
import threading

def plot_thread():

    ad = CustomAxiDraw()
    ad.plot_setup("vpype/output/final_for_axi.svg")
    output = ad.plot_run(True, sleep_timer_sec=90)

    while True:
        ad.plot_setup(output)
        ad.options.mode = "res_home"
        output = ad.plot_run(True)
        time.sleep(1)

        ad.plot_setup()
        ad.options.mode = "manual"
        ad.options.manual_cmd = "walk_mmx"
        clean_distance_x = 300 + np.random.randint(0, 100)
        ad.options.dist = clean_distance_x
        ad.plot_run()
        ad.options.manual_cmd = "walk_mmy"
        clean_distance_y = 100 + np.random.randint(0,100)
        ad.options.dist = clean_distance_y
        ad.plot_run()
        # time.sleep(3)
        # print(f'Sleeping now 3')


        for _ in range(2):
            ad.options.manual_cmd = "lower_pen"
            ad.options.pen_pos_down = 20
            ad.plot_run()
            time.sleep(1)
            ad.options.manual_cmd = "walk_mmy"
            ad.options.dist = -clean_distance_y
            ad.plot_run()
            ad.options.manual_cmd = "walk_mmx"
            ad.options.dist = -10
            ad.plot_run()
            ad.options.manual_cmd = "walk_mmy"
            ad.options.dist = clean_distance_y
            ad.plot_run()
            ad.options.manual_cmd = "walk_mmx"
            ad.options.dist = 10
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
        time.sleep(1)
        print(f'Sleeping now 1')

        ad.plot_setup(output)
        ad.options.mode = "res_plot"
        output = ad.plot_run(True)
        if ad.plot_status.resume.old.pause_dist < 0:
            print('The plot has finished its work')
            break

    ad.plot_setup()
    ad.options.mode = "manual"
    ad.options.manual_cmd = "disable_xy"
    ad.plot_run()

t = threading.Thread(target=plot_thread)
t.start()

# Join the plotting thread to wait for its completion
t.join()

