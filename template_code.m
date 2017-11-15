generate_barcode;

S = length(patterns);

patternLengths = zeros(S,1);
for s = 1:S
    patternLengths(s) = length(patterns{s});
end

M = 6;
C = max(patternLengths);
NumStates = C*S*M;

%Enumerate all the states
States = zeros(NumStates,3) -1 ;
StatesInv = zeros(C,S,M) -1;

ix = 1;
for c = 1:C
    for s = 1:S
        for m = 1:M
            if( (s > 5) || (s <=5 && m ==1) )
                if( c<=patternLengths(s))
                    States(ix,:) = [c s m];
                    StatesInv(c,s,m) = ix;
                    ix = ix+1;
                end
            end
        end
    end
end

NumStates = ix -1;
States = States(1:NumStates,:);

%warning: NumStates will be less than S*M*C, because not all possible
%[s,m,c] triples are valid. 


%% Part1: Fill the transition matrix A

%mapping states to binary numbers, which will be useful for computing the
%likelihood
f_kst = zeros(NumStates,1); 


A = zeros(NumStates);

for i = 1:NumStates
    
    c = States(i,1);
    s = States(i,2);
    m = States(i,3);
    
    patternLen = patternLengths(s);
    f_kst(i) = patterns{s}(c); %determines if this state is black or white
    
    %example:
    if(s == 1) %starting quiet zone
        
        if(c == patternLen)
            
            for ss = [1 3] %the next states can only be either starting quiet zone, or the starting guard
                s_next = ss;
                c_next = 1;
                m_next = 1;
                
                nextStateIx = StatesInv(c_next,s_next,m_next);
                A(nextStateIx,i) = (1/2);
            end
            
        else
            c_next = c+1;
            s_next = s;
            m_next = m;
            
            nextStateIx = StatesInv(c_next,s_next,m_next);
            A(nextStateIx,i) = 1;
        end
        
        
    elseif(s == 2) %ending quiet zone
        
        %to be filled
        
    elseif(s== 3) %starting guard
        
        %to be filled
        
    elseif(s== 4) %ending guard
        
        %to be filled
        
    elseif(s== 5) %middle guard
        
        %to be filled
        
    elseif(s>= 6 && s<=15) %left symbols
        
        %to be filled
            
    elseif(s>= 16 && s<=25) %right symbols
        
        %to be filled
        
    else
        error('Unknown State!');
    end
end

%% Part2: Compute the inital probability

p_init = zeros(NumStates);

%to be filled

%the barcode *must* start with the "starting quite zone", with s_n=1. Other
%states are not possible. Fill the initial probability accordingly. 



%% Part3: Compute the log-likelihood

T = length(obs);

logObs = zeros(NumStates,T);

mu= [mu0 mu1]';
sigma = ...;

for t=1:T
    % to be filled
    % you can use the variable f_kst here
end

%% Part 4: Compute the filtering distribution via Forward recursion

%to be filled

%% Part 5: Compute the smoothing distribution via Forward-Backward recursion

%to be filled

%% Part 6: Compute the most-likely path via Viterbi algorithm

%to be filled

%% Part 7: Obtain the barcode string from the decoded states

best_cn = ... (this will be obtained via Viterbi)
best_sn = ... (this will be obtained via Viterbi)

%find the place where a new symbol starts
ix = find(best_cn ==1);

s_ix = BestStates(ix,2);
decoded_code = [];
for i = 1:length(best_sn)
    tmp = s_ix(i);
    %consider only the symbols that correspond to digits
    if(tmp>=6)
        chr = mod(tmp-6,10);
        decoded_code = [decoded_code, chr];
    end
    
end

fprintf('Real code:\t');
fprintf('%d',code);
fprintf('\n');
fprintf('Decoded code:\t');
fprintf('%d',decoded_code);
fprintf('\n');
