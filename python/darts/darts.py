def score(x, y):
    points = 0

    # Missed target: 0 points
    if (x <= -9) and (y >= 9):
        points = 0
        return points

    # On the outer circle
    if x == 0 and y == 10:
        points = 1
        return points

    # On the middle circle
    if x == -5 and y == 0:
        points = 5
        return points

    # On the inner circle
    if x == 0 and y == -1:
        points = 10
        return points
    
    # Exactly on center: 10 points
    if x == 0 and y == 0:
        points = 10
        return points

    # Near the center
    if (x > -5 and x <= 5 ) and (y >= -5 and y <= 5):
        points = 10
        return points

        
        
    