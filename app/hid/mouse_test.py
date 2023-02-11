import tempfile
import unittest

from hid import mouse


class MouseTest(unittest.TestCase):

    def test_sends_mouse_click_to_hid_interface(self):
        with tempfile.NamedTemporaryFile() as input_file:
            mouse.send_mouse_event(mouse_path=input_file.name,
                                   buttons=0x01,
                                   relative_x=0.5,
                                   relative_y=0.75,
                                   vertical_wheel_delta=0,
                                   horizontal_wheel_delta=0)
            input_file.seek(0)

            self.assertEqual(b'', input_file.read())

    def test_sends_mouse_move_to_hid_interface(self):
        with tempfile.NamedTemporaryFile() as input_file:
            mouse.send_mouse_event(mouse_path=input_file.name,
                                   buttons=0,
                                   relative_x=0.0,
                                   relative_y=1.0,
                                   vertical_wheel_delta=0,
                                   horizontal_wheel_delta=0)
            input_file.seek(0)

            self.assertEqual(b'', input_file.read())
