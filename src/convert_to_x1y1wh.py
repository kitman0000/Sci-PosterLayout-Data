# This script convert the npy from xcycwh to x1y1wh
import numpy as np

import sys


def convert(input, output):
    data = np.load(input)
    print(f'File shape: {data.shape}')
    for poster in data:
        for panel in poster:
            xc = panel[1]
            yc = panel[2]
            w = panel[3]
            h = panel[4]

            x1 = xc - w / 2
            x2 = yc - h / 2

            panel[1] = x1
            panel[2] = x2
            

    np.save(output,data,allow_pickle=True)
    print(f'x1y1wh file saved to {output}')

if __name__ == '__main__':
    input = sys.argv[1]
    output = sys.argv[2]

    convert(input,output)