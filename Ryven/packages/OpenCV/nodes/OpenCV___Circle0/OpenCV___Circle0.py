from NENV import *

import cv2

# API METHODS

# self.main_widget()        <- access to main widget


# Ports
# self.input(index)                   <- access to input data
# set_output_val(self, index, val)    <- set output data port value
# self.exec_output(index)             <- executes an execution output

# self.create_input(type_, label, widget_name=None, widget_pos='under', pos=-1)
# self.delete_input(index or input)
# self.create_output(type_, label, pos=-1)
# self.delete_output(index or output)


# Logging
# mylog = self.new_log('Example Log')
# mylog.log('I\'m alive!!')
# self.log_message('hello global!', 'global')
# self.log_message('that\'s not good', 'error')

# ------------------------------------------------------------------------------


class Circle_Node(Node):
    def __init__(self, params):
        super(Circle_Node, self).__init__(params)

        # self.special_actions['action name'] = {'method': M(self.action_method)}
        # ...

    # don't call self.update_event() directly, use self.update() instead
    def update_event(self, input_called=-1):
        img = self.input(0).copy()
        result = cv2.circle(img, self.input(1), self.input(2), self.input(3), 3)
        self.main_widget().show_image(result)
        self.set_output_val(0, result)


    def get_state(self):
        data = {}
        # ...
        return data

    def set_state(self, data):
        pass # ...


    def remove_event(self):
        pass