import math

leivis = (float)(input("Pistä leivisköjen määrä: "))

naula = (float)(input("Pistä naulojen määrä: "))

luoti = (float)(input("Pistä luotien määrä: "))
grammat = naula * 32 + luoti * 13.3 * 32 + leivis / 32 * 13.3 * 20

print("Massa nykymittojen mukaan: "(grammat))
