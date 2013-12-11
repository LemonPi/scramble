line_starts = [] # list of original line number and start position
def descramble(in_filename, out_filename):
    """
    (str(in_filename), str(out_filename)) -> no return
    Read lines from in_filename and sort them, then write line content
    in order to out_filename.
    """
    
    start = 0
    with open(in_filename, 'r') as infile:
        for line in infile:
            line_num = int(line.split(":")[0])  # colon separates # from content
            line_starts.append((line_num, start))
            start += len(line)  # go to first char of next line
        with open(out_filename, 'w') as outfile:
            line_starts.sort()  # sort by first elem, ala line number
            for start in line_starts:
                infile.seek(start[1])
                line = infile.readline()
                outfile.write(line.split(":", 1)[1])  # skips line num and colon
            
            # gives the size of outfile, then gets rid of last \n
            size = outfile.tell()
            outfile.truncate(size - 1)
