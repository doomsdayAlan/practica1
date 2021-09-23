import math
def xgcd(a, b):
    """(gcd)máximo común divisor de a y b.
        Utiliza el algoritmo extendido de Euclides.
    Args:
        a: mcd(a,b)=resultado
        b: mcd(a,b)=resultado
    Returns:
        Returns mcd(a,b) and (u0,v0)
    """
    if b == 0:
        return 0,1,0
    u0 = 1
    u1 = 0
    v0 = 0
    v1 = 1
    while b != 0:
        q = a//b
        r = a - b * q
        u = u0 - q * u1
        v = v0 - q * v1
        #Update a,b
        a = b
        b = r
        #Update for next iteration
        u0 = u1
        u1 = u
        v0 = v1
        v1 = v
    return  a, u0, v0
print(xgcd(393,267))

print("ingrese los valores aceptables para n,a, y b")
n=int(input("Dígame una cantidad para n: "))
a=int(input("Dígame una cantidad para a: "))
b=int(input("Dígame una cantidad para b: "))
print(n,a,b)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m



if b < n and b >=0 :
    print ("Betha es valido")
else: 
    print ("Betha se encuentra fuera de rango")

if (math.gcd(a,n)==1):
    print("alfa es valido")
    print(xgcd(a,n))
    Ek = (a + b) % n
    Dk = ((a - 1 ) * (-b)) % n
    print (Ek)
    print (Dk)
else: 
    print("Warning: Introduzca un valor de alpha valido") 
    a = int(input("Dígame una cantidad para a: ")) 




