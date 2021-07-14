"""
Module containing test cases for the objective_1.py
Author: Shilpaj Bhalerao
Date: July 11, 2021
"""
# Standard Library Imports
import pytest

# Local Imports
from objective_1 import *


def test_polygon_repr():
    """
    Test case to check if proper documentation is printed by the object of a class
    """
    # Create an object of the class
    _object = Polygon(3, 4)

    # Check if __repr__ method is present
    assert hasattr(_object, '__repr__')


def test_polygon_eq():
    """
    Test case to check if __eq__ method is implemented correctly
    """
    # Create an object of the class
    _object = Polygon(3, 4)

    # Check if __repr__ method is present
    assert hasattr(_object, '__eq__')


def test_polygon_gt():
    """
    Test case to check if __gt__ method is implemented correctly
    """
    # Create an object of the class
    _object = Polygon(3, 4)

    # Check if __repr__ method is present
    assert hasattr(_object, '__gt__')


def test_polygon_getitem():
    """
    Test case to check if __getitem__ method is implemented correctly
    """
    # Create an object of the class
    _object = Polygon(3, 4)

    # Check if __repr__ method is present
    assert hasattr(_object, '__getitem__')


def test_polygon_wrong_input_for_comparison():
    """
    Test case to check if errors is raised when incorrect type of object is passed for comparison
    """
    # Create an object of the class
    triangle = Polygon(3, 4)

    class Test:
        def __init__(self):
            pass

    _object = Test()

    # Check if error is raised when different types of objects are compared
    with pytest.raises(TypeError):
        assert triangle == _object
        assert triangle > _object
        assert triangle < _object
        assert triangle >= _object
        assert triangle <= _object


def test_polygon_wrong_input_for_getitem():
    """
    Test case to check if errors is raised when incorrect string is passed to __getitem__
    """
    # Create an object of the class
    triangle = Polygon(3, 4)

    with pytest.raises(IndexError):
        assert triangle['any_string']


def test_polygon_getitem_output():
    """
    Test case to check if the int values are returned for edges and vertices while float values are returned for
    other indexes when __getitem__ method is called
    """
    # Acceptable keys for __getitem__
    int_keys = ['edges', 'vertices']
    float_keys = ['interior_angle', 'edge_length', 'apothem', 'area', 'perimeter']

    # Create an object of the class
    triangle = Polygon(3, 4)

    int_conditions = [type(triangle[key]) == int for key in int_keys]
    float_conditions = [type(triangle[key]) == float for key in float_keys]
    assert all(int_conditions)
    assert all(float_conditions)


def test_polygon_equality():
    """
    Test case to check if __eq__ method is working properly for same type of polygons
    """
    # Create an object of the class
    _triangle_1 = Polygon(3, 4)
    _triangle_2 = Polygon(3, 4)
    _triangle_3 = Polygon(3, 5)

    assert _triangle_1 == _triangle_2
    assert _triangle_1 != _triangle_3


def test_polygon_equality_polygon():
    """
    Test case to check if __eq__ method is working properly for different type of polygons
    """
    # Create an object of the class
    _triangle = Polygon(3, 4)
    _square = Polygon(4, 4)

    assert _triangle != _square


def test_polygon_comparison():
    """
    Test case to check if __gt__ method is working properly
    """
    # Create an object of the class
    _triangle = Polygon(3, 4)
    _square = Polygon(4, 5)
    _pentagon = Polygon(5, 5)
    _pentagon_2 = Polygon(5, 6)

    assert _pentagon > _square > _triangle
    assert not _pentagon_2 > _pentagon


def test_polygon_inputs():
    """
    Test case to check valid values of edges and circumradius
    """
    with pytest.raises(ValueError):
        _polygon_1_4 = Polygon(1, 4)

    with pytest.raises(ValueError):
        _polygon_1_0 = Polygon(3.5, 4)

    with pytest.raises(ValueError):
        _polygon_1_0 = Polygon(3, 0)

    with pytest.raises(ValueError):
        _polygon_1_0 = Polygon(3, 4.5)
