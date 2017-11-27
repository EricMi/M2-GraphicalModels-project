## Part2: Compute the inital probability

p_init = zeros(NumStates)

# to be filled

# the barcode *must* start with the "starting quite zone", with s_n=1. Other
# states are not possible. Fill the initial probability accordingly. 

# Suppose that the initial probability is a uniform distribution over the
# states with s_n = 0
mask_support_init = States[:, 1] == 0
cnt_support_init = sum(mask_support_init)

p_init[mask_support_init] = 1. / cnt_support_init
