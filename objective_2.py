"""
Module to return geometric parameters of a regular strictly convex polygon
Author: Shilpaj Bhalerao
Date: July 11, 2021
"""
# Standard Library Imports
import math
from operator import sub, mul, truediv
from functools import lru_cache
from collections import namedtuple
from typing import Union


class CustomPolygon:
    """
    Class containing methods for a regular polygon
    """

    def __init__(self, edges, circumradius) -> None:
        """
        Constructor
        :param edges: number_of_edges of largest circumscribed polygon
        :param circumradius: common radius of a circle in which polygon is inscribed
        """
        if not isinstance(edges, int) or edges <= 2:
            raise ValueError(f"Enter valid input for number of edges. It cannot be less than 3. Current value: {edges}")
        elif not isinstance(circumradius, int) or circumradius < 1:
            raise ValueError(f"Enter valid input for number of circumradius. It cannot be less than or equal to 1. "
                             f"Current value: {circumradius}")
        else:
            self.max_edges = edges
            self.circumradius = circumradius

            self._ratio_data = dict()
            self._records = []

            self._ratio_data = {edge: self._property_calculations(edge) for edge in range(3, edges + 1)}

    def __getitem__(self, index) -> Union[float, list]:
        """
        Method to return the ratio of area to perimeter for a regular polygon
        :param index: index number of a polygon considering polygon with 3 edges has 0 index
        :return: Ratio of area to perimeter for the polygon with number of vertices
        """
        # Length of sequence considering polygons starts from triangle(i.e. edges=3)
        length_of_sequence = self.max_edges - 2

        if isinstance(index, int):
            if index < 0:
                index = length_of_sequence + index
            if index < 0 or index > length_of_sequence:
                raise IndexError
            else:
                return self._ratio_data[index + 3]
        else:
            start, stop, step = index.indices(length_of_sequence)
            rng = range(start, stop, step)
            return [self._ratio_data[index + 3] for index in rng]

    @lru_cache(2 ** 10)
    def _property_calculations(self, edges):
        """
        Method to calculate all the property value for a regular polygon
        :param edges: Number of edges for a polygon
        :return: output of area:perimeter ratio
        """
        # NamedTuple to store the record of data
        PolygonData = namedtuple('PolygonData',
                                 "edges vertices interior_angle edge_length apothem area perimeter ratio")
        PolygonData.__doc__ = "Data associated with a regular polygon inscribed in a circle"
        PolygonData.edges.__doc__ = "Number of edges of a regular polygon"
        PolygonData.vertices.__doc__ = "Number of vertices of a regular polygon"
        PolygonData.interior_angle.__doc__ = "Interior angle of a regular polygon"
        PolygonData.edge_length.__doc__ = "Edge length of a regular polygon"
        PolygonData.apothem.__doc__ = "Apothem of a regular polygon"
        PolygonData.area.__doc__ = "Area of a regular polygon"
        PolygonData.perimeter.__doc__ = "Perimeter of a regular polygon"
        PolygonData.ratio.__doc__ = "Ratio of area to perimeter for a regular polygon"

        # Calculate all the properties of polygon
        _edges = edges
        _vertices = _edges
        _interior_angle = truediv(mul(sub(_edges, 2), 180), _edges)
        _edge_length = mul(mul(2, self.circumradius), math.sin(truediv(math.pi, _edges)))
        _apothem = mul(self.circumradius, math.cos(truediv(math.pi, _edges)))
        _area = mul(mul(0.5, _edges), mul(_edge_length, _apothem))
        _perimeter = mul(_edges, _edge_length)
        _ratio = truediv(_area, _perimeter)

        # Store all the data
        self._records.append(PolygonData(edges=_edges, vertices=_vertices, interior_angle=_interior_angle,
                                         edge_length=_edge_length, apothem=_apothem, area=_area, perimeter=_perimeter,
                                         ratio=_ratio))
        # Return the ratio of area:perimeter
        return _ratio

    def __repr__(self) -> str:
        """
        Method returning a string representation of a class object
        :return: String representation
        """
        return f"Regular Polygons with edges ranging from 3 to {self.max_edges} all inscribed in a circle of radius {self.circumradius}"

    def max_efficiency_polygon_edges(self) -> int:
        """
        Method to return the edges value of a polygon with maximum efficiency of area:perimeter ratio
        :return: number of edges of polygon with max efficiency
        """
        max_ratio = max(self._ratio_data.values())
        return list(self._ratio_data.keys())[list(self._ratio_data.values()).index(max_ratio)]

    def __len__(self) -> int:
        """
        Method to print total number of polygons in the sequence
        :return: Length of an object
        """
        return self.max_edges - 2

    def get_record(self):
        """
        Method to get all properties information in the sequence
        """
        return self._records


if __name__ == '__main__':
    # Create an instance of a class
    polygon_sequence = CustomPolygon(25, 5)

    # Test the polygon with maximum efficiency
    print(f"Maximum efficiency is for polygon with {polygon_sequence.max_efficiency_polygon_edges()} edges")

    # Test __getitem__ functionality
    print(f"Edges: Efficiency are as:")
    [print(f"Edges: {index + 3}  Efficiency: {polygon_sequence[i]}") for index, i in
     enumerate(range(len(polygon_sequence)))]

    # Test the __len__ functionality
    print(f"Length of the object: {len(polygon_sequence)}")

    # Test the __repr__ functionality
    print(polygon_sequence)

    # Test the record functionality
    for polygon in polygon_sequence.get_record():
        print(polygon)
