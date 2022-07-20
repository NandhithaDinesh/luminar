from functools import reduce
#map
# filter
# reduce
lst=[10,2,30,4]
gt_ten=list(filter(lambda n:n>10,lst))
print(gt_ten)

evens=list(filter(lambda n:n%2==0,lst))
print(evens)

squares=list(map(lambda n:n**2,lst))

cubes=list(map(lambda n:n**3,lst))

num_out=list(map(lambda n:n-1 if n<5 else n+1,lst ))
print(num_out)

sum=reduce(lambda n1,n2:n1+n2,lst)
print(sum)

product=reduce(lambda n1,n2:n1*n2,lst)
print(product)

max_num=reduce(lambda n1,n2:n1 if n1>n2 else n2,lst)
print(max_num)


minimum=reduce(lambda n1,n2:n1 if n1<n2 else n2,lst)
print(minimum)