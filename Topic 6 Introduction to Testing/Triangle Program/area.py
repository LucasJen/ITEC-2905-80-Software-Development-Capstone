def triange_area(height, base):
    if base < 0 or height < 0:
        raise ValueError('Base and height must be at least 0')
    return height * base * 0.5
