
# set the limit to be checked 
limit = int(input('what is the upper bound of numbers? '))

#create the loop
for i in range(limit + 1):

"""there are several approaches here, but this is the most basic. This problem set can also be solved by having additional variables 
to be checked instead of hard coded values """


  if i % 3 == 0 and i % 5 == 0:
    print('FizzBuzz')
  elif i % 5 == 0:
    print('Buzz')
  elif i % 3 == 0:
    print('Fizz')
  else:
    print(i)
