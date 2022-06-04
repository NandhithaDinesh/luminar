# sum=0
# for i in range(1,10):
#     sum+=i
# print(sum)
#.........................................................
# total=sum(range(1,10))
# print(total)
#.........................................................
# def add_numbers(n1,n2):
#     return n1+n2
# print(add_numbers(12,12))
#.........................................................
# def sub_numbers(n1,n2):
#     return n1-n2
# print(sub_numbers(24,12))
#.........................................................
# def smart_sum(n1,n2):
#     return n1-n2 if n1>n1 else n2-n1
# print(smart_sum(2,8))
#.........................................................
# def num_check(n1):
#     return "even" if n1%2==0 else "odd"
# print(num_check(9))
#.........................................................
# def is_starts_witha(name):
#     return name.startswith("a")
# print(is_starts_witha("maya"))
#...........................................................
# def validate_email(email):
#     return email.endswith("@gmail.com")
# print(validate_email("nandhitha@gmail.com"))
#...........................................................
# def factorial(num):
#     fact=1
#     for i in range(1,(num+1)):
#         fact=fact*i
#     return fact
# print(factorial(5))
#............................................................
def is_prime(num):
    flag=0
    for i in range(2,num):
        if(num%i==0):
            flag=1
            break
    return True if flag==0 else False
    # if flag==0:
    #     print("prime")
    # else:
    #     print("not prime")
#print(is_prime(4))
def prime_range(low,upp):
    for num in range(low,(upp+1)):
        if is_prime(num):
            print(num)
prime_range(10,50)

#.................................................................
