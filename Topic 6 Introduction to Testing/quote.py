
# return values depending on inputted lawn size
def lawn_quote(size, same_day):
    if size =='small':
        price = 10
    elif size == 'medium':
        price = 15
    elif size == 'large':
        price = 20
    else:
        return #can't calculate, return None
    
    # add 5 to value if same day is true
    if same_day:
        price +=5

    return price