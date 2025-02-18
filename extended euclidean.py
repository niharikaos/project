def extended_euclid(a, m):
    # Initialize values
    r1, r2 = a, m
    t1, t2 = 1, 0
    step = 1

    # Print the table headers
    print(f"{'q':<4} {'r1':<4} {'r2':<4} {'r':<4} {'t1':<4} {'t2':<4} {'t':<4}")
    print("-" * 40)

    while r2 != 0:
        q = r1 // r2  # Quotient
        r = r1 % r2   # Remainder
        t = t1 - q * t2  # New t value

        # Print the current state in the table format
        print(f"{q:<4} {r1:<4} {r2:<4} {r:<4} {t1:<4} {t2:<4} {t:<4}")

        # Update values for next iteration
        r1, r2 = r2, r
        t1, t2 = t2, t

    # The GCD will be r1 when the loop ends
    gcd = r1

    # Check if modular inverse exists
    if gcd != 1:
        print(f"No modular inverse exists for {a} mod {m}")
    else:
        # Ensure the result is positive
        mod_inverse = (t1 % m + m) % m
        print(f"The modular inverse of {a} mod {m} is: {mod_inverse}")

def main():
    # User input for the number and modulus
    a = int(input("Enter a number to find its modular inverse: "))
    m = int(input("Enter the modulus (m): "))
    
    # Call the extended Euclidean function
    extended_euclid(a, m)

if _name_ == "_main_":
    main()



# Enter a number to find its modular inverse: 7
# Enter the modulus (m): 26
# q    r1   r2   r    t1   t2   t   
# ----------------------------------------
# 0    7    26   7    1    0    1
# 3    26   7    5    0    1   -3
# 1    7    5    2    1   -3    4
# 2    5    2    1   -3    4   -11
# 2    2    1    0    4   -11   26
# The modular inverse of 7 mod 26 is: 4
