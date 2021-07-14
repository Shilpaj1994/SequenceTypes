"""
Module to return geometric properties of a regular strictly convex polygon
Author: Shilpaj Bhalerao
Date: July 11, 2021
"""
# Standard Library Imports
import math
from operator import sub, mul, truediv
from functools import total_ordering


@total_ordering
class Polygon:
    """
    Class containing methods for a regular polygon
    """

    def __init__(self, edges, circumradius) -> None:
        """
        Constructor
        :param edges: number_of_edges of a circumscribed polygon
        :param circumradius: radius of a circle in which polygon is inscribed
        """
        if not isinstance(edges, int) or edges <= 2:
            raise ValueError(f"Enter valid input for number of edges. It cannot be less than 3. Current value: {edges}")
        elif not isinstance(circumradius, int) or circumradius < 1:
            raise ValueError(f"Enter valid input for number of circumradius. It cannot be less than or equal to 1. "
                             f"Current value: {circumradius}")
        else:
            self.edges = edges
            self.circumradius = circumradius

            # Dictionary to keep the record of data and return when asked
            self._data = dict()

            # Expected indexes for the __getitem__ method
            self._keys = ['edges', 'vertices', 'interior_angle', 'edge_length', 'apothem', 'area', 'perimeter']

    def __getitem__(self, _property: str) -> float:
        """
        Method to calculate and return the geometric properties
        :param _property: edges, vertices, interior_angle, edge_length, apothem, area, perimeter
        :return: value of the property
        """
        if _property in self._keys:
            self._data['edges'] = self.edges
            self._data['vertices'] = self.edges
            self._data['interior_angle'] = truediv(mul(sub(self.edges, 2), 180), self.edges)
            self._data['edge_length'] = mul(mul(2, self.circumradius), math.sin(truediv(math.pi, self.edges)))
            self._data['apothem'] = mul(self.circumradius, math.cos(truediv(math.pi, self.edges)))
            self._data['area'] = mul(mul(0.5, self.edges), mul(self._data['edge_length'], self._data['apothem']))
            self._data['perimeter'] = mul(self.edges, self._data['edge_length'])
            return self._data[_property]
        raise IndexError(f"Please check the entered index. Accepted index: {self._keys}")

    def __repr__(self) -> str:
        """
        Method returning a string representation of a class object
        :return: String representation
        """
        return f"Polygon with {self.edges} edges and inscribed in a circle of radius {self.circumradius}"

    def __eq__(self, other: object) -> bool:
        """
        Method to implement the equal to operation for two objects
        :param other: object to be compared with
        :return: True/False
        """
        if isinstance(other, Polygon):
            if self.edges == other.edges and self.circumradius == other.circumradius:
                return True
            return False
        raise TypeError("Both are objects are not of same type")

    def __gt__(self, other: object) -> bool:
        """
        Method to implement the greater than operation for two objects
        :param other: object to be compared with
        :return: True/False
        """
        if isinstance(other, Polygon):
            if self.edges > other.edges:
                return True
            return False
        raise TypeError("Both are objects are not of same type")


if __name__ == '__main__':
    # Create an instance of a class
    triangle_1 = Polygon(3, 5)
    triangle_2 = Polygon(3, 5)
    square = Polygon(4, 6)

    # Test the __repr__ functionality
    print(triangle_1)

    # Test __eq__ functionality
    print(triangle_1 == triangle_2)

    # Test __gt__ functionality
    print(square > triangle_2)

    # Test the getitem functionality for 'edges', 'vertices', 'interior_angle', 'edge_length', 'apothem', 'area', 'perimeter'
    print(f"Property edges for square: {square['edges']}")
    print(f"Property vertices for square: {square['vertices']}")
    print(f"Property interior angle for square: {square['interior_angle']}")
    print(f"Property edge length for square: {square['edge_length']}")
    print(f"Property apothem for square: {square['apothem']}")
    print(f"Property area for square: {square['area']}")
    print(f"Property perimeter for square: {square['perimeter']}")
