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

