from mpmath import mp

def pi_upto_n_digit(n):
  mp.dps = n+1
  return str(mp.pi)

n = int(input("Enter n: "))
pi = pi_upto_n_digit(n)
print(pi)
