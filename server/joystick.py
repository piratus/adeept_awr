from pyPS4Controller.controller import Controller
import move


class MyController(Controller):

    def __init__(self, interface, **kwargs):
        Controller.__init__(
            self,
            interface,
            connecting_using_ds4drv=False,
            **kwargs,
        )
        move.setup()

        self.speed = 75
        self.move_direction = 'no'
        self.rotate_direction = 'no'

    def _update(self):
        move.move(self.speed, self.move_direction, self.rotate_direction)

    def destroy(self):
        move.destroy()

    def on_up_arrow_press(self):
        self.move_direction = 'forward'
        self._update()

    def on_down_arrow_press(self):
        self.move_direction = 'backward'
        self._update()

    def on_up_down_arrow_release(self):
        self.move_direction = 'no'
        self._update()

    def on_left_arrow_press(self):
        self.rotate_direction = 'left'
        self._update()

    def on_right_arrow_press(self):
        self.rotate_direction = 'right'
        self._update()

    def on_left_right_arrow_release(self):
        self.rotate_direction = 'no'
        self._update()

    def on_L3_up(self, value):
        self._update()

    def on_L3_down(self, value):
        self._update()

    def on_L3_left(self, value):
        self._update()

    def on_L3_right(self, value):
        self._update()

    def on_L3_y_at_rest(self):
        self._update()

    def on_L3_x_at_rest(self):
        self._update()


if __name__ == '__main__':
    controller = MyController('/dev/input/js1')
    try:
        controller.listen()
    finally:
        print('Cleaning up...')
        controller.destroy()
