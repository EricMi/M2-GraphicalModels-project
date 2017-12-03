import numpy as np
import matplotlib.pyplot as plt
# %matplotlib inline
from getPatternsUPCA import getPatternsUPCA

# prepare the black-white patterns for each symbol
patterns = getPatternsUPCA()

# the digits that will be encoded in the barcode
code = [0,1,2,3,4,5,6,7,8,9,0]

# Checksum computation
chksum = (10 - (3*sum(code[0::2])+sum(code[1::2]))%10) % 10
code.append(chksum)
# python : code[start:end:interval]
# matlab : code(start:interval:end)

# generate the 1D barcode
stripes = patterns[0] + patterns[0]    # initial white space
stripes = stripes + patterns[2]    # initial guard
for i in range(6):
    stripes = stripes + patterns[code[i] + 5]    # get the code for the corresponding left digit
stripes = stripes + patterns[4]    # middle guard
for i in range(6,12):
    stripes = stripes + patterns[code[i] + 15]    # get the code for the corresponding right digit
stripes = stripes + patterns[3]    # end guard
stripes = stripes + patterns[1] + patterns[1]
len(stripes)

# Generate the scanline
obs_noise = 0    # you can play with 'obs_noise'
# obs is the observed scanline (x_n in the document)
obs = 255 * np.asarray(stripes)
obs = obs + obs_noise * np.random.randn(obs.size)
obs[obs<0] = 0
obs[obs>255] = 255

# generate the image
plt.figure()
bc_image = 255 - np.tile(obs, (50,1))
plt.axis("off")
plt.imshow(bc_image, cmap='gray',vmin=0,vmax=255)
# cmap = 'gray'  : 0-black   1-white
# cmap = 'Grays' : 0-white   1-black
plt.title(str(np.asarray(code)))
plt.show()