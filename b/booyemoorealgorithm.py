# booye moore algorithm 
def generate_combinations(s):
    n = len(s)
    combinations = []
    
    for i in range(n):
        for j in range(i+1, n+1):
            combinations.append(s[i:j])
    print(1)
    return combinations
'''def booyemoore_algorithm(s , k):    
    k_splited = k.split()
    s_splited = s.split()
    listed = []
    len_s = len(s_splited)
    for i in len(k_splited):
        if s_splited[:-1] == k_splited[i-1]:
            if len_s<=i:
                if s_splited[0] == k_splited[i-len_s]:
                    proved = 0
                    for j in range(0,len_s-1):
                        if k_splitted[i-len_s +j]==s_splited[j]:
                            proved+=1
                    if proved == s_len-1:  
                        listed.append((s , (i-s_len+1 , i) , s_len))'''
def splited(sequ):
    list_seq = []
    for k in sequ:
        list_seq.append(k)
    return list_seq     
def booyemoore_algorithm(s, k):
    k_splitted = splited(k)
    
    s_splitted = splited(s)
    
    len_s = len(s_splitted)
    listed = []
    
    for i in range(len(k_splitted)):
        if s_splitted[-1] == k_splitted[i-1]:
            if len_s<=i:
                if s_splitted[0] == k_splitted[i-len_s]:
                    proved = 0
                    for j in range(0,len_s-1):
                        if k_splitted[i-len_s +j]==s_splitted[j]:
                            proved+=1
                    if proved == len_s-1:  
                        listed.append((s , (i-len_s+1 , i) , len_s))

                          
    return listed    
def checker(string_input, Dna_sequence):
    
    combi = generate_combinations(string_input)
    real_list = []
    
    for keys in combi:
        listed = booyemoore_algorithm(keys, Dna_sequence)
        if len(listed) != 0:
            for (a,b,c) in listed:
                real_list.append((a,b,c))
           
           
    try:
        if len(real_list) != 0:
            
            sorted_list = sorted(real_list, key=lambda x: x[2], reverse=False) 
            for i in sorted_list:
                print(f"{i}")
             
    except Exception as err:
        print(err)
        
        
string_input = "ACGTGTCAGGCTAGTC"
Dna_sequence = "ACGTGTCAGGCTAGTC"
print(f" the demo string is : {string_input}")
print(f" the real string is : {string_input} ")
checker(string_input , Dna_sequence)
