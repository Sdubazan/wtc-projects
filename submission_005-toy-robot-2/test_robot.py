import unittest
import sys
from unittest.mock import patch
from io import StringIO
from contextlib import contextmanager
import robot

@contextmanager
def output_capture(stdin):
    new_out,new_err,new_input = StringIO(),StringIO(),stdin
    try:
        sys.stdout,sys.stderr,sys.stdin = new_out,new_err,new_input
        yield sys.stdout,sys.stderr
    finally:
        pass


class my_robot_unittest(unittest.TestCase):
    @patch('sys.stdin',StringIO('HAL'))
    def test_01_robot_name(self):
        self.assertEqual(robot.robot_name(),'HAL')
    
    def test_02_robot_off_command_test(self):
        with output_capture(StringIO('HAL\noff\n')) as (out,err):
            robot.robot_start()

            result = out.getvalue().strip()
            expected = """What do you want to name your robot? HAL: Hello kiddo!
HAL: What must I do next? HAL: Shutting down.."""
        self.assertEqual(result,expected)

    def test_03_robot_valid_command_test(self):
        with output_capture(StringIO('HAL\nroll down\noff\n')) as (out,err):
            robot.robot_start()

            result = out.getvalue().strip()
            expected = """What do you want to name your robot? HAL: Hello kiddo!
HAL: What must I do next? HAL: Sorry, I did not understand 'roll down'.
HAL: What must I do next? HAL: Shutting down.."""
        self.assertEqual(result,expected)
    
    def test_04_robot_help_command_test(self):
        with output_capture(StringIO('HAL\nhelp\noff\n')) as (out,err):
            robot.robot_start()

            result = out.getvalue().strip()
            expected = """What do you want to name your robot? HAL: Hello kiddo!
HAL: What must I do next? I can understand these commands:
OFF  - Shut down robot
HELP - provide information about commands 

 > HAL now at position (0,0).
HAL: What must I do next? HAL: Shutting down.."""
        self.assertEqual(result,expected)
    
    def test_05_robot_forward_command_test(self):
        with output_capture(StringIO('HAL\nforward 10\noff\n')) as (out,err):
            robot.robot_start()

            result = out.getvalue().strip()
            expected = """What do you want to name your robot? HAL: Hello kiddo!
HAL: What must I do next?  > HAL moved forward by 10 steps.
 > HAL now at position (0,10).
HAL: What must I do next? HAL: Shutting down.."""
        self.assertEqual(result,expected)
    
    def test_06_robot_back_command_test(self):
        with output_capture(StringIO('HAL\nback 10\noff\n')) as (out,err):
            robot.robot_start()

            result = out.getvalue().strip()
            expected = """What do you want to name your robot? HAL: Hello kiddo!
HAL: What must I do next?  > HAL moved back by 10 steps.
 > HAL now at position (0,-10).
HAL: What must I do next? HAL: Shutting down.."""
        self.assertEqual(result,expected)

    def test_07_robot_right_forward_10_command_test(self):
        with output_capture(StringIO('HAL\nright\nforward 10\noff\n')) as (out,err):
            robot.robot_start()

            result = out.getvalue().strip()
            expected = """What do you want to name your robot? HAL: Hello kiddo!
HAL: What must I do next?  > HAL turned right.
 > HAL now at position (0,0).
HAL: What must I do next?  > HAL moved forward by 10 steps.
 > HAL now at position (10,0).
HAL: What must I do next? HAL: Shutting down.."""
        self.assertEqual(result,expected)

    def test_08_robot_left_forward_10_command_test(self):
        with output_capture(StringIO('HAL\nleft\nforward 10\noff\n')) as (out,err):
            robot.robot_start()

            result = out.getvalue().strip()
            expected = """What do you want to name your robot? HAL: Hello kiddo!
HAL: What must I do next?  > HAL turned left.
 > HAL now at position (0,0).
HAL: What must I do next?  > HAL moved forward by 10 steps.
 > HAL now at position (-10,0).
HAL: What must I do next? HAL: Shutting down.."""
        self.assertEqual(result,expected)
    
    def test_09_robot_right_back_10_command_test(self):
        with output_capture(StringIO('HAL\nright\nback 10\noff\n')) as (out,err):
            robot.robot_start()

            result = out.getvalue().strip()
            expected = """What do you want to name your robot? HAL: Hello kiddo!
HAL: What must I do next?  > HAL turned right.
 > HAL now at position (0,0).
HAL: What must I do next?  > HAL moved back by 10 steps.
 > HAL now at position (-10,0).
HAL: What must I do next? HAL: Shutting down.."""
        self.assertEqual(result,expected)
    
    def test_10_robot_left_back_10_command_test(self):
        with output_capture(StringIO('HAL\nleft\nback 10\noff\n')) as (out,err):
            robot.robot_start()

            result = out.getvalue().strip()
            expected = """What do you want to name your robot? HAL: Hello kiddo!
HAL: What must I do next?  > HAL turned left.
 > HAL now at position (0,0).
HAL: What must I do next?  > HAL moved back by 10 steps.
 > HAL now at position (10,0).
HAL: What must I do next? HAL: Shutting down.."""
        self.assertEqual(result,expected)
    
    def test_11_robot_track_position_test(self):
        with output_capture(StringIO('HAL\nforward 10\nright\nforward 10\nright\nforward 10\nright\nforward 10\noff\n')) as (out,err):
            robot.robot_start()

            result = out.getvalue().strip()
            expected = """What do you want to name your robot? HAL: Hello kiddo!
HAL: What must I do next?  > HAL moved forward by 10 steps.
 > HAL now at position (0,10).
HAL: What must I do next?  > HAL turned right.
 > HAL now at position (0,10).
HAL: What must I do next?  > HAL moved forward by 10 steps.
 > HAL now at position (10,10).
HAL: What must I do next?  > HAL turned right.
 > HAL now at position (10,10).
HAL: What must I do next?  > HAL moved forward by 10 steps.
 > HAL now at position (10,0).
HAL: What must I do next?  > HAL turned right.
 > HAL now at position (10,0).
HAL: What must I do next?  > HAL moved forward by 10 steps.
 > HAL now at position (0,0).
HAL: What must I do next? HAL: Shutting down.."""
        self.assertEqual(result,expected)
    
    def test_12_robot_y_forward_area_limit_test(self):
        with output_capture(StringIO('HAL\nforward 250\nforward 100\noff\n')) as (out,err):
            robot.robot_start()

            result = out.getvalue().strip()
            expected = """What do you want to name your robot? HAL: Hello kiddo!
HAL: What must I do next? HAL: Sorry, I cannot go outside my safe zone.
 > HAL now at position (0,0).
HAL: What must I do next?  > HAL moved forward by 100 steps.
 > HAL now at position (0,100).
HAL: What must I do next? HAL: Shutting down.."""
        self.assertEqual(result,expected)
    
    def test_13_robot_y_back_area_limit_test(self):
        with output_capture(StringIO('HAL\nback 130\nback 70\noff\n')) as (out,err):
            robot.robot_start()

            result = out.getvalue().strip()
            expected = """What do you want to name your robot? HAL: Hello kiddo!
HAL: What must I do next? HAL: Sorry, I cannot go outside my safe zone.
 > HAL now at position (0,0).
HAL: What must I do next?  > HAL moved back by 70 steps.
 > HAL now at position (0,-70).
HAL: What must I do next? HAL: Shutting down.."""
        self.assertEqual(result,expected)
    
    def test_14_robot_x_forward_area_limit_test(self):
        with output_capture(StringIO('HAL\nright\nfoward 230\nforward 70\noff\n')) as (out,err):
            robot.robot_start()

            result = out.getvalue().strip()
            expected = """What do you want to name your robot? HAL: Hello kiddo!
HAL: What must I do next?  > HAL turned right.
 > HAL now at position (0,0).
HAL: What must I do next? 
 > HAL now at position (0,0).
HAL: What must I do next?  > HAL moved forward by 70 steps.
 > HAL now at position (70,0).
HAL: What must I do next? HAL: Shutting down.."""
        self.assertEqual(result,expected)
    
    def test_15_robot_x_back_area_limit_test(self):
        with output_capture(StringIO('HAL\nright\nback 130\nback 90\noff\n')) as (out,err):
            robot.robot_start()

            result = out.getvalue().strip()
            expected = """What do you want to name your robot? HAL: Hello kiddo!
HAL: What must I do next?  > HAL turned right.
 > HAL now at position (0,0).
HAL: What must I do next? HAL: Sorry, I cannot go outside my safe zone.
 > HAL now at position (0,0).
HAL: What must I do next?  > HAL moved back by 90 steps.
 > HAL now at position (-90,0).
HAL: What must I do next? HAL: Shutting down.."""
        self.assertEqual(result,expected)
    
    def test_16_robot_sprint_command_test(self):
        with output_capture(StringIO('HAL\nsprint 5\noff\n')) as (out,err):
            robot.robot_start()

            result = out.getvalue().strip()
            expected = """What do you want to name your robot? HAL: Hello kiddo!
HAL: What must I do next?  > HAL moved forward by 5 steps.
 > HAL moved forward by 4 steps.
 > HAL moved forward by 3 steps.
 > HAL moved forward by 2 steps.
 > HAL moved forward by 1 steps.
 > HAL now at position (0,15).
HAL: What must I do next? HAL: Shutting down.."""
        self.assertEqual(result,expected)
    
if __name__ == '__main__':
    unittest.main()