import fractions

x = int(input())
while x > 0:
    (a, b, c) = [int(p) for p in input().split(" ")]
    f = fractions.Fraction(a, b)
    print(f ** fractions.Fraction(1,1))






    x += -1