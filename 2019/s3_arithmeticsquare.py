


"""
get all of the inital square scenarios
- one single unit
    - fill every cell with the single unit -> arithmetic sequence
- two units in a row (a b x)
    - x = b-a -> arithmetic sequence for the given row
    - if no other rows are filled out then duplicate the first one
        a b c
        a b c
        a b c
- first row completely filled + 2 rows empty
    - just duplicate the first row twice just like above

- first row filled and one unit in the second row
    a b c
    d x x
    x x x
    - take first row (a b c) and increment everything by (d-a) then just put it all in the second row
        second row = (a+(d-a)), (b+(d-a)), (c+(d-a))
        example:
        1 2 3    1 2 3                    1 2 3
        4 x x -> 4 (2+(4-1)) (3+(4-1)) -> 4 5 6
        x x x    x x x                    x x x
    
do the same thing but for columns rotated 90 degrees or something

"""

# getting the input inital grid
# probably better to get each row as it's own variable instead of one 2d grid
# so that its easier to work with