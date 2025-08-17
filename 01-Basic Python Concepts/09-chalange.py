'''
#Celcius ------> Faranheit.

c = input("Enter Celcius: ")
c = float(c);
f = (c * 9/5) + 32;

print("Ferenheit: ",f)
'''

'''
#Faranheit ------> Celcius.
f = input("Enter Faranheit: ");
f = float(f)
c = (f-32) * 5/9 
print("Celcus : ",c)
'''

#Simple Interest (SI)
P = float(input("Enter Principal Amount: "));
N = float(input("Enter Number of years / Time period: "));
R = float(input("Rate of Interest: "));

SI = (P * N * R) / 100;

print(f"You earn ₹{SI} interest after 2 years.")