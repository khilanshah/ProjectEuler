
product = 600851475143

def factors(number):
    factor_list = [x for x in range(1,int(number**0.5),1) if number%x ==0]
    factor_complement = [number/x for x in factor_list]
    factor_list = factor_list + factor_complement
    return factor_list

def is_prime(number):
    if number > 3:
        i=5

        while i*i <= number:
            if number%i==0 or number%(i+2)==0:
                return 0
            else:
                i = i + 6

        return 1

    else:
        return number>1

          

fact_list=factors(product)
print(fact_list)

primes = [x for x in fact_list if is_prime(x)==1]
print(primes)

print('largest prime = ', max(primes))

