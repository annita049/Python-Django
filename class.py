# 1 + 2 + 3 + ... + 10 = (10 * 11)/2

def SeriesSum(n=1):
    return (n*(n+1))//2

terms_no = int(input("Enter the number of terms: "))
print(SeriesSum(n=terms_no))