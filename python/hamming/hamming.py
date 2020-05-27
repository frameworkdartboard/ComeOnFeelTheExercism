def distance(strand_a, strand_b):
    if (strand_a == "" and strand_b != ""):
        raise ValueError("strand_a is an empty string but not strand_b.")
    elif (strand_b == "" and strand_a != ""):
        raise ValueError("strand_b is the empty string but not strand_a.")
    
    lena = len(strand_a)
    lenb = len(strand_b)
    
    if (lena > lenb):
        raise ValueError("strand_a is longer than strand_b.")
    elif (lenb > lena):
        raise ValueError("strand_b is longer than strand_a.")
    
    numdiffs = 0
    for ii in range(lena):
        if (strand_a[ii] != strand_b[ii]):
            numdiffs = numdiffs + 1
    
    return(numdiffs)