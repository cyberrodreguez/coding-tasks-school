def lower(inf,outf):
    file=open(inf,"r")
    output=open(outf,"w")
    a=file.readlines()
    for i in a:
        if not i[0] in "abcdefghijklmnopqrstuvwxyz":
            output.write(i)
    output.close()
    file.close()
lower("yo.txt","outfile.txt")

    
