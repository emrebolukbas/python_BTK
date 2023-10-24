def topla():
    global a #yerelde bu sekilde de kullanılabilir fakat a'ya değer atanamaz
    global b
    a=5 #yerel
    b=9
    return(a+b)
#a=5
#b=9   #global
print(topla())
print(a)
print(b)
