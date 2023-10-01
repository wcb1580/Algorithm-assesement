import itertools
import math
import utm # Coordinates are converted to UTM format for analysis in metres (assume they are in same zone)
import numpy as np
# Take a list of lat/lon coords and extract out the easting and northing vectors (in m)
# NOTE: For the purposes of this exercise we can ignore differing zone letters and numbers

def convert_to_utm_xy(coordinates):
    return [utm.from_latlon(*c)[:2] for c in coordinates]

def calc_total_distance(coordinates_xy, indices):
    total_distance = 0
    for i in range(1, len(indices)):
        dx = coordinates_xy[indices[i]][0] - coordinates_xy[indices[i-1]][0]
        dy = coordinates_xy[indices[i]][1] - coordinates_xy[indices[i-1]][1]
        total_distance += math.sqrt(dx*dx + dy*dy)

    return total_distance
def calc_distance(coordinates_xy,A,B):
    x = coordinates_xy[A][0]-coordinates_xy[B][0]
    y = coordinates_xy[A][1]-coordinates_xy[B][1]
    distance = math.sqrt(x*x+y*y)
    return distance

def nearest_neighbour(coordinates_xy,start):
    n = len(coordinates_xy)
    visited = [False]*n
    visited[start]=[True]
    Start = [start]
    for k in range(n-1):
        best = float('inf')
        Current = Start[-1]
        for i in range(n):
            if not visited[i]:
                distance = calc_distance(coordinates_xy,i,Current)
                if distance<best:
                    best = distance
                    predecessor = i
        Start.append(predecessor)
        visited[predecessor] = True
    return Start


def optimise_travel_order(coordinates):
    coordinates_xy = convert_to_utm_xy(coordinates)
    indices = list(range(len(coordinates_xy)))
    # TODO Devise an algorithm to optimise the order
    best = float('Inf')
    for t in range(len(indices)):
        order = nearest_neighbour(coordinates_xy,t)
        distance = calc_total_distance(coordinates_xy,order)
        if distance < best:
            best = distance
            indices = order


    return indices
