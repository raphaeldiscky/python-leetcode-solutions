class Solution:
    def countPrimes(self, n: int) -> int:
        """
            Sieve if Eratosthenes
                Time: O(nlog(logn))
                Space: O(n)
            1. Create a 1D boolean array prime [] of size N.
            2. Initially we presume that all numbers are prime numbers. So we will initialize the array with true.
            3. Starting from 2, we check if prime [i] is true, if so, we update every multiple of i to false.
            4. In the end, we check prime [] from index = 2 and print the count of cells containing the value true.
            5. Note: 1 is not a prime number which is why we start iterating from 2.
        """
        if n == 0:
            return 0
        prime = [True]*n
        i = 2
        while i*i < n:
            if prime[i]:
                # update all multiples of i to False
                for j in range(i*i, n, i):
                    prime[j] = False
            i += 1
        total = 0
        list = []
        for i in range(2, n):
            if prime[i]:
                total += 1
                list.append(i)
        print(list)
        return total


ob1 = Solution()
print(ob1.countPrimes(10))
