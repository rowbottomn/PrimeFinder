import time
#10ln10 ~ 23
hi = 10
lo = 20
iterations = 5
step = 10

primes = [2, 3, 5, 7, 11, 13, 17, 19]
for k in range(iterations):
  start = time.time()
  #I add 1 to low range as the lo range must not be prime as it was made by multiplying numbers
  for i in range(hi*(pow(step, k)+1),hi*(pow(step, k+1))):
    isPrime = True
    for j in range(len(primes)):
      if (primes[j]*2 > i):
        break
      if(i%primes[j]==0):
        #print("found {} is a factor of {}".format(primes[j], i))
        isPrime = False
        break
    if(isPrime):
      print("Found Prime:{}!".format(i))
      primes.append(i)

  end = time.time() - start

#display = input("Do you want to see the primes?)
#if display == "y" or "yes":
  #print(primes)
  print("Done! Found {} primes less than {}. completed in {} milliseconds".format(len(primes), hi*pow(step, k+1), end ))
print("Finally done")