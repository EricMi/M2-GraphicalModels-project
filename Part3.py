## Part3: Compute the log-likelihood

T = len(obs);

logObs = np.zeros((NumStates, T))

mu= np.array([250, 20])
sigma = np.array([sqrt(5), sqrt(5)])

p_state = p_init 

for t in range(0, T):
    # to be filled
    # you can use the variable f_kst here
    logObs = np.log(p_state) + [norm.pdf(obs[t], mu[i], sigma[i]) for i in
            f_kst]
    p_state = A.dot(p_state)
