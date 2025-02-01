class Filter:
    def prime(self, n):
        if n <= 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True
    def fil(self, numbers):
        return list(filter(lambda x: self.prime(x), numbers))
prime_filter = Filter()
num = [10, 13, 7, 4, 11, 16, 23, 8]
prime_numbers = prime_filter.fil(num)
print(prime_numbers)
