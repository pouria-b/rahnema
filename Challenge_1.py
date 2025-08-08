def sum_even_vowels(used_chars)->bool:
    e_v=['a' ,'e' ,'u' ,'i' ,'o']
    summ=0
    for v in e_v:
        if v in used_chars:
            summ +=1
    
    return (summ % 2==0) and (summ > 0)
    
def longest_valid_unique_substring(s):
    vowels = set('aeiou')
    n = len(s)
    max_len = 0
    max_substring = ""
    used_chars = set()

    if n == 0 or n == 1:
        return 0

    i1=0
    i2=0
    used_chars.add(s[i1])
    while (True):
        
        if (s[i2+1] not in used_chars) and (i2+1<=n):
            i2 += 1 
            used_chars.add(s[i2])
            ls = len(used_chars)    
            if sum_even_vowels(used_chars) and (max_len<ls):
                max_len = ls
            
        else:
            ls = len(used_chars)    
            if sum_even_vowels(used_chars) and (max_len<ls):
                max_len = ls
            
            while(True):
                used_chars.remove(s[i1])
                i1 += 1 
                if s[i2+1] not in used_chars:               
                    break
            if (s[i2+1] not in used_chars) and (i2+1<=n):
                i2 += 1 
                used_chars.add(s[i2])
            # print('i1:',i1,'i2:',i2,'s',s)  
            # print(used_chars)  

        if i2+1 >= n:
            ls = len(used_chars)    
            if sum_even_vowels(used_chars) and (max_len<ls):
                max_len = ls
            break


    return max_len

def l_v_u_s(s):
    ans = max(longest_valid_unique_substring(s),longest_valid_unique_substring(s[::-1]))
    return ans 

print(l_v_u_s("abciiidef")) 
print(l_v_u_s("abcabcbb"))        
print(l_v_u_s("aeiouxyz"))    
