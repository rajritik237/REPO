def c_to_f (temp):
    return(temp*9/5)+32
celsius_temp=[0.0,10.0,20.0,30.0,40.0,98.0,100.0]
fahrenhight_tem = list(map(c_to_f,celsius_temp))
print(fahrenhight_tem)