n=int(input("enter +ve number:"))
if n < 0:
    print("Please enter a positive number.")
else:
    i=1
    while(i!=11):
        print(f"{n}*{i}={n*i}")
        i=i+1
