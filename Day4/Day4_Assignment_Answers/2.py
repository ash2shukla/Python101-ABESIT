import sys
def python101_print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False):
    """Prints string representation of all the objects passed to system's standard output.
    
    Keyword Arguments:
    objects (arbitrary argument) -- objects to print  
    sep (str) -- seperator between objects  
    end (str) -- ending of objects
    file (file_stream) -- file_stream to which it should print
    flush (bool) -- whether to flush stream or not
    """
    # intialize a list to store string representation of all objects
    stringified_objects = []
    for _object in objects:
        # convert all objects to string and append them to list
        stringified_objects.append(str(_object))
    # join all of the objects' string representation with seperator and concatenate end
    file.write(sep.join(stringified_objects) + end)
    # if flush is True then flush the stream
    if flush:
        file.flush()

python101_print(1,2,3,4,5,6, sep='SEP', end='END')
