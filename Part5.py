# Part 5: Compute the smoothing distribution via Forward-Backward recursion

# log_beta: update message in backward pass
# log_beta_postdict: postdict message in backward pass
log_beta = np.zeros((NumStates, T))
log_beta_postdict = np.zeros((NumStates, T))
for t in range(T-1:-1:-1):
    if t == T-1:
        log_beta_postdict[:, t] = np.zeros(NumStates)
    else:
        mx = np.max(log_beta[:, t + 1])
        p = np.exp(log_beta[:, t + 1] - mx)
        log_beta_postdict[:, t] = log(A.T.dot(p)) + mx
    log_beta[:, t] = log_beta_postdict[:, t] + logObs[:, t]

# d_smoothing: smoothing distribution
d_smoothing = np.zeros((NumStates, T))
for t in range(T):
    gamma = np.exp(log_alpha[:, t] + log_beta_postdict[:, t])
    d_smoothing = gamma / np.sum(gamma)

# d_marginal_smoothing_s: marginal smoothing distribution of s
# d_marginal_smoothing_c: marginal smoothing distribution of c
# d_marginal_smoothing_m: marginal smoothing distribution of m
d_marginal_smoothing_s = np.zeros((S, T))
d_marginal_smoothing_c = np.zeros((C, T))
d_marginal_smoothing_m = np.zeros((M, T))
for t in range(T):
    for s in range(S):
        mask_s = [States[:, 1] == s]
        d_marginal_smoothing_s[s, T] = np.sum(d_smoothing[mask_s])
    for c in range(C):
        mask_c = [States[:, 0] == c+1]
        d_marginal_smoothing_c[c, T] = np.sum(d_smoothing[mask_c])
    for m in range(M):
        mask_m = [States[:, 2] == m+1]
        d_marginal_smoothing_m[m, T] = np.sum(d_smoothing[mask_m])
