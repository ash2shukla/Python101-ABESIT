def python101_range(start, stop="NOT_GIVEN", step=1):
    """Returns a generator that produces a sequence starting from start to stop with step.
    
    Keyword Arguments:
    start (int) -- The sequence's start 
    stop (int) -- The sequence's end
    step (int) -- The sequence's step
    """
    if stop == "NOT_GIVEN":
        stop=start
        start=0
    while start < stop:
        yield start
        start+=step

for i in python101_range(1,10,2):
    print(i)
