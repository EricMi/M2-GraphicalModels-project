# Part 4: Compute the filtering distribution via Forward recursion
# For numerical stability
eps = np.finfo(float).eps
p_init[p_init < eps] = eps

# log_alpha: update message in forward pass 
# log_alpha_predict: predict message in forward pass
log_alpha = np.zeros((NumStates, T))
log_alpha_predict = np.zeros((NumStates, T))
for t in range(T):
    if t == 0:
        log_alpha_predict[:, t] = np.log(p_init)
    else:
        mx = np.max(log_alpha[:, t - 1])
        p = np.exp(log_alpha[:, t - 1] - mx)
        log_alpha_predict[:, t] = np.log(A.dot(p)) + mx
    log_alpha[:, t] = log_alpha_predict[:, t] + logObs[:, t]

# d_filtering: filtering distribution
d_filtering = np.zeros((NumStates, T))
for t in range(T):
    alpha = np.exp(log_alpha[:, t])
    d_filtering[:, t] = alpha / np.sum(alpha)

# d_marginal_filtering_s: marginal filtering distribution of s
# d_marginal_filtering_c: marginal filtering distribution of c
# d_marginal_filtering_m: marginal filtering distribution of m
d_marginal_filtering_s = np.zeros((S, T))
d_marginal_filtering_c = np.zeros((C, T))
d_marginal_filtering_m = np.zeros((M, T))
for t in range(T):
    for s in range(S):
        mask_s = [States[:, 1] == s]
        d_marginal_filtering_s[s, T] = np.sum(d_filtering[mask_s])
    for c in range(C):
        mask_c = [States[:, 0] == c+1]
        d_marginal_filtering_c[c, T] = np.sum(d_filtering[mask_c])
    for m in range(M):
        mask_m = [States[:, 2] == m+1]
        d_marginal_filtering_m[m, T] = np.sum(d_filtering[mask_m])
