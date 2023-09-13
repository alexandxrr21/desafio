def celcius_a_fahrenheit(celsius):
    return (celsius *9/5) + 32

def celcius_a_kelvin(celcius):
    return celcius + 273.15

if __name__=="__main__":
    celsius =25
    fahrenheit =celcius_a_fahrenheit(celsius)
    print(f"{celsius} grados celcius son equivalentes a {fahrenheit} grados fahrenheit")