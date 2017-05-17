import random
import numpy as np

#CPT
probablity_w=0.3
probablity_c=0.8
probablity_i=0.5
probablity_ts=np.array([0.2,0.4,0.1,0.7])
probablity_o=np.array([0.2,0.5,0.3,0.6])
probablity_r=np.array([0.9,0.5,0.3,0.1])


def check_probability_independent(value,probablity_element):
    if value<=probablity_element:
        return 1
    else:
        return 0
def check_probability_dependent(value,probablity_element,first_dependent_element,sec__dependent_element):
    if first_dependent_element==1 and sec__dependent_element==1:
        a = probablity_element[3]
        if value<=a:
            return 1
        else:
            return 0
    elif first_dependent_element==1 and sec__dependent_element==0:
        a = probablity_element[2]
        if value<=a:
            return 1
        else:
            return 0
    elif first_dependent_element==0 and sec__dependent_element==1:
        a = probablity_element[1]
        if value<=a:
            return 1
        else:
            return 0
    elif first_dependent_element==0 and sec__dependent_element==0:
        a = probablity_element[0]
        if value<=a:
            return 1
        else:
            return 0

needed_result = [1,1,1,1,1,1]
sample_numbers=int(input("Enter a number of samples: "))
i=0
for x in range (sample_numbers):
    states=6
    sample_list=[]
    for y in range(states):
        ran_number = random.uniform(0, 1)
        sample_list.append(ran_number)
    #print(len(sample_list))
    one_element=check_probability_independent(sample_list[0],probablity_i)
    sec_element = check_probability_independent(sample_list[1], probablity_c)
    thi_element = check_probability_independent(sample_list[2], probablity_w)
    fou_element = check_probability_dependent(sample_list[3], probablity_o,one_element,sec_element)
    fif_element = check_probability_dependent(sample_list[4], probablity_ts,sec_element,thi_element)
    six_element = check_probability_dependent(sample_list[5], probablity_r,fou_element,fif_element)
    sample_result=np.array([one_element,sec_element,thi_element,fou_element,fif_element,six_element])
    print(sample_result)
    if(needed_result==sample_result).all():
        i=i+1
    else:
        i=i
query=i/sample_numbers
print(query)
