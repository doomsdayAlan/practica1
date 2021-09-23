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
    '''return  a, u0, v0'''
    return  a

def mcd_recur(a,b):
    if b == 0:
        return a
    return mcd_recur(b, a % b)

print("ingrese los valores aceptables para n,a, y b")
n=int(input("Dígame una cantidad para n: "))
a=int(input("Dígame una cantidad para a: "))
b=int(input("Dígame una cantidad para : "))
print(n,a,b)


if mcd_recur(a,n)==1:
    print(mcd_recur(a,n))
    print("es valido ")
    print(n,a,b)
else:
    print(mcd_recur(a,n))
    print("no es valido, ingrese otro valor")
    print(n,a,b)
