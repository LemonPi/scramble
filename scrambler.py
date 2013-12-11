import random
line_starts = [(1,0)] # line number 1 starting at 0
def scramble(in_filename, out_filename):
    """
    (str(in_filename), str(out_filename)) -> no return
    Write scrambled lines to out_filename from in_filename after prepending
    each line with original line numbers.
    """
    
    start = 0
    line_n = 1
    last_blank = True  # flag for if last line has trailing \n
    with open(in_filename, 'r') as infile:
        for line in infile:
            start += len(line)  # add one to go to first char of next line
            line_n += 1
            line_starts.append((line_n, start))
        with open(out_filename, 'w') as outfile:
            del line_starts[-1]  # last start value is EOF
            random.shuffle(line_starts)
            for start in line_starts:
                infile.seek(start[1])  # goes to first char of random line
                line = str(start[0]) + ":" + infile.readline()
                outfile.write(line)
                if line[-1] != '\n':
                    last_blank = False
                    outfile.write('\n')  # append \n to any line ending without
            # use the fact that last_blank can be 0 or 1
            outfile.write((str(len(line_starts) + 1) + ':\n') * last_blank)

