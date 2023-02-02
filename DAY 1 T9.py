def max_guests(E, L, T):
    guests = [0] * (T + 1)
    for i in range(len(E)):
        guests[E[i]] += 1
        guests[L[i]] -= 1
    
    max_guests = guests[0]
    for i in range(1, T+1):
        guests[i] += guests[i-1]
        max_guests = max(max_guests, guests[i])
    
    return max_guests

E=[1,5,9,10]
T=[-4]
L=[0,2,3,4]

print("Maximum number of guests present:", max_guests(E, L, T))
