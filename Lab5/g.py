# Function to convert decimal to binary
def decimal_to_binary(n):
    if n == 0:
        return "0b0"
    else:
        binary = ""
        while n > 0:
            binary = str(n % 2) + binary
            n = n // 2
        return "0b" + binary

# Function to convert decimal to octal
def decimal_to_octal(n):
    if n == 0:
        return "0o0"
    else:
        octal = ""
        while n > 0:
            octal = str(n % 8) + octal
            n = n // 8
        return "0o" + octal

# Function to convert decimal to hexadecimal
def decimal_to_hexadecimal(n):
    if n == 0:
        return "0x0"
    else:
        hexadecimal = ""
        while n > 0:
            remainder = n % 16
            if remainder < 10:
                hexadecimal = str(remainder) + hexadecimal
            else:
                hexadecimal = chr(remainder - 10 + ord('A')) + hexadecimal
            n = n // 16
        return "0x" + hexadecimal

# Example usage
n= int(input("Enter a decimal number: "))
print(decimal_to_binary(n))
print(decimal_to_octal(n))
print(decimal_to_hexadecimal(n))
