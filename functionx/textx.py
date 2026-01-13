import functionx.namex
def file(result,output1,output2):
    with open(result, "w") as fo:
        fo.write(output1+output2)