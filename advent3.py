file_input = open("input3.1", "r")
lines = file_input.read().splitlines()
file_input.close()
wires = []
for line in lines:
    wires.append(line.split(','))
def createCorners(corners):
    # Run through the list of directions and build the wire's path.
    # Also build dicts of horizontal / vertical segments.
    # createCorner[0] = List of corners (in order)
    # createCorner[1] = List of horiztonal segments
    #
    #   horizontals[y] = [(x, x), (x, x)]
    #
    # createCorners[2] = List of vertical segments
    #
    #   verticals[x] = [(y, y), (y, y)]
    x = 0
    y = 0
    corner = (x, y)
    line = []
    line.append(corner)
    horizontals = {}
    verticals = {}
    
    for segment in corners:
        direction = segment[0]
        length = int(segment[1:])
        if direction == 'R':
            # Go right
            if not horizontals.has_key(y):
                horizontals[y] = [(x, x+length)]
            else:
                horizontals[y].append((x,x+length))
            x += length
        elif direction == 'D':
            # Go down
            if not verticals.has_key(x):
                verticals[x] = [(y, y-length)]
            else:
                verticals[x].append((y,y-length))
            y -= length
        elif direction == 'L':
            # Go left
            if not horizontals.has_key(y):
                horizontals[y] = [(x-length, x)]
            else:
                horizontals[y].append((x-length,x))
            x -= length
        elif direction == 'U':
            # Go up
            if not verticals.has_key(x):
                verticals[x] = [(y+length, y)]
            else:
                verticals[x].append((y+length,y))
            y += length

        else:
            print "Wrong direction!"
            break
        
        corner = (x, y)
        line.append(corner)
    return line, horizontals, verticals

def intersects(point, segment):
    # Returns a boolean for if the segment intersects the point
    # point (x, y)
    # segment ((x, y), (x, y))
    if 
    


def findIntersects(lines):
    # Return a list of segments that intersect each other.

    # An intersection occurs when the y coordinate of a horizontal lies between the y coordinates of a vertical.
    # For each line segment in the line, check the other line for segments that might intersect.

    wire1 = createCorners(lines[0])
    wire2 = createCorners(lines[1])
    intersects = []

    # look at all the horizontal segments in wire1, see if they intersect any vertical segments in wire2
    horizontals = wire1[1].viewitems()
    verticals = wire2[2].viewitems()

    for row, columns in horizontals:
        left = columns[0][0]
        right = columns[0][1]
        for column, rows in verticals:
            top = rows[0][0]
            bottom = rows[0][1]

            if row < top and row > bottom and column > left and column < right:
                print column, row
                intersects.append((column,row))
   
    del horizontals, verticals

    # Look at all the vertical segments in wire1, see if they intersect any horizontal segments in wire2
    horizontals = wire2[1].viewitems()
    verticals = wire1[2].viewitems()
    
    for column, rows in verticals:
        top = rows[0][0]
        bottom = rows[0][1]
        for row, columns in horizontals:
            left = columns[0][0]
            right = columns[0][1]

            if column < right and column > left and row > bottom and row < top:
                print column, row
                intersects.append((column, row))

    return intersects

test = [['R8','U5','L5','D3'],['U7','R6','D4','L4']]
test1 = [['R75','D30','R83','U83','L12','D49','R71','U7','L72'], ['U62','R66','U55','R34','D71','R55','D58','R83']]
test2 = [['R98','U47','R26','D63','R33','U87','L62','D20','R33','U53','R51'],['U98','R91','D20','R16','D67','R40','U7','R15','U6','R7']]

#print createCorners(test[0])
#print createCorners(test1[0])
#print createCorners(test2[0])

# Part 1: Find the intersection closest to the origin.
low = None
intersects = findIntersects(wires)
for intersect in intersects:

    dist = abs(intersect[0])+ abs(intersect[1])
    if not low:
        low = dist
    elif dist < low:
        low = dist

print low
    

# Part 2: Find the intersection where the sum of the distance the wires takes is lowest.

# Trace the path the wire takes, couting up the steps. Stop when we reach the intersection.
for intersect in intersects:
