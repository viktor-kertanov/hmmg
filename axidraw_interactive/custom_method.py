from pyaxidraw import axidraw
from pyaxidraw.axidraw import AxiDraw
import logging
import threading

logger = logging.getLogger(__name__)

class CustomAxiDraw(AxiDraw):
    def plot_run(self, output=False, sleep_timer_sec=30):
        '''Python module plot context: Plot document'''

        self.set_up_pause_transmitter()

        if self.document is None:
            logger.error("No SVG input provided.")
            logger.error("Use plot_setup(svg_input) before plot_run().")
            raise RuntimeError("No SVG input provided.")
        
        self.set_defaults() # Re-initialize some items normally set at __init__
        self.set_up_pause_receiver(self.software_initiated_pause_event)
        self.effect()
        self.clear_pause_request()
        #self.fw_version_string is a public string made available to Python API:
        self.fw_version_string = self.plot_status.fw_version

        self.handle_errors()

        if self.options.mode in ("plot", "layers", "res_plot"):
            ''' Timing & distance variables only available in modes that plot '''
            # Set up a timer to trigger the pause after 10 minutes (600 seconds)
            pause_timer = threading.Timer(sleep_timer_sec, self.software_initiated_pause_event.set)
            pause_timer.start()
            logger.info('Currently after pause timer in plot or res_plot or layers mode.')
            if self.options.preview:
                self.time_estimate = self.plot_status.stats.pt_estimate / 1000.0
            else:
                self.time_estimate = self.time_elapsed
            self.distance_pendown = 0.0254 * self.plot_status.stats.down_travel_tot
            self.distance_total = self.distance_pendown +\
                0.0254 * self.plot_status.stats.up_travel_tot
            self.pen_lifts = self.pen.status.lifts

        for warning_message in self.warnings.return_text_list():
            self.user_message_fun(warning_message)
        if output:
            return self.get_output()
        return None