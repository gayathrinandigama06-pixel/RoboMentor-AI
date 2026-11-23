"""Simple 2D circular-obstacle geometry utilities."""
import math

def point_is_clear(point, center, radius):
    if radius < 0:
        raise ValueError("radius cannot be negative")
    return math.dist(point, center) > radius

def path_is_clear(start, goal, center, radius):
    """Check whether a segment clears a circular obstacle (touching counts as collision)."""
    if radius < 0:
        raise ValueError("radius cannot be negative")
    sx, sy = start
    gx, gy = goal
    cx, cy = center
    dx, dy = gx-sx, gy-sy
    denom = dx*dx + dy*dy
    if denom == 0:
        return point_is_clear(start, center, radius)
    t = max(0.0, min(1.0, ((cx-sx)*dx + (cy-sy)*dy)/denom))
    closest = (sx+t*dx, sy+t*dy)
    return math.dist(closest, center) > radius
