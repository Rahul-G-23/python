import random
n= random.randint(1,10)
print(' Name: Rahul G \n USN: 1AY24AI088 \n Section: O')
user = int(input('Eanter a number between 1 to 9: '))
print('computer guess: '+str(n))
if (user==n):
    print(' Your choice is correct')
else:
    print('Your choice is incorrect! Try again')
