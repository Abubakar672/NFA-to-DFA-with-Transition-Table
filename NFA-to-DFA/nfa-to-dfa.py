import pandas as pd

nfa = {}                                 
nos = int(input("Enter the number of states : "))            
trans = int(input("Enter the number of transitions : "))       
for i in range(nos):  
    state = input("Enter the state name : ")          
    nfa[state] = {}
    for j in range(trans):
        path = input("Enter the path : ")              
        print("Enter end state from state {} passing through the path {} : ".format(state,path))
        destination_State = [x for x in input().split()]
        nfa[state][path] = destination_State     
print("\nNFA :- \n")
print(nfa)                                   
print("\nThe NFA Table :- ")

nfa_table = pd.DataFrame(nfa)
print(nfa_table.transpose())

print("Enter End state of NFA : ")
nfa_final_state = [x for x in input().split()]            
    
state_arrray = []                          
dfa = {}                                      
keys = list(list(nfa.keys())[0])                  
crossways = list(nfa[keys[0]].keys())    

dfa[keys[0]] = {}                        
for y in range(trans):
    var = "".join(nfa[keys[0]][crossways[y]])   
    dfa[keys[0]][crossways[y]] = var           
    if var not in keys:                         
        state_arrray.append(var)                  
        keys.append(var)                        
while len(state_arrray) != 0:                     
    dfa[state_arrray[0]] = {}                    
    for _ in range(len(state_arrray[0])):
        for i in range(len(crossways)):
            temporary_List = []                               
            for j in range(len(state_arrray[0])):
                temporary_List += nfa[state_arrray[0][j]][crossways[i]] 
            s = ""
            s = s.join(temporary_List)                        
            if s not in keys:                  
                state_arrray.append(s)            
                keys.append(s)                  
            dfa[state_arrray[0]][crossways[i]] = s  
        
    state_arrray.remove(state_arrray[0])    

print("\nDFA :- \n")    
print(dfa)                                       
print("\The DFA table :- ")
dfa_table = pd.DataFrame(dfa)
print(dfa_table.transpose())

dfa_states_list = list(dfa.keys())
dfa_final_states = []
for x in dfa_states_list:
    for i in x:
        if i in nfa_final_state:
            dfa_final_states.append(x)
            break
        
print("\End states of the DFA are : ",dfa_final_states)       

 
