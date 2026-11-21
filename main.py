# Importing individual modules
import graphics.rectangle
graphics.rectangle.area(10, 5)
graphics.rectangle.perimeter(10, 5)

# Importing a module using alias
import graphics.circle as c
c.area(7)
c.perimeter(7)

# Importing specific functions
from three_d_graphics.cuboid import area, perimeter
area(5, 4, 3)
perimeter(5, 4, 3)

# Importing a module
from three_d_graphics import sphere
sphere.area(7)
