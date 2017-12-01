# Part 4: Compute the filtering distribution via Forward recursion
eps = np.finfo(float).eps
p_init[p_init < eps] = eps

log_alpha = np.zeros(NumStates, T)
log_alpha_predict = np.zeros((NumStates, T))
for t in range(T):
    if t == 0:
        log_alpha_predict[:, t] = log(p_init)
    else:
        mx = np.max(log_alpha[:, t - 1])
        p = np.exp(log_alpha[:, t - 1] - mx)
        log_alpha_predict[:, t] = np.log(A.dot(p)) + mx
    log_alpha[:, t] = log_alpha_predict[:, t] + logObs[:, t]

d_filtering = np.zeros((NumStates, T))
for t in range(T):
    d_filtering[:, t] = log_alpha[:, t] / np.sum(log_alpha[:, t])
