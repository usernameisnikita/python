# Write an algorithm to generate a password of
#  length n. The password should be randomly generated and must
#  include at least one uppercase letter, one lowercase letter, one digit,
#  and one special character.
#  Hint: Consider decomposing the problem into parts - generating an
#  uppercase letter, generating a lowercase letter, generating a digit,
#  generating a special character, and then combining these parts.

import random
import string

def password(n):

  assert(n>=4)

  passw = []
  passw.append(random.choice(string.ascii_uppercase))
  passw.append(random.choice(string.ascii_lowercase))
  passw.append(random.choice(string.digits))
  passw.append(random.choice(string.punctuation))
  
  for i in range(n-4):
    randomChoice=random.choice([0,1,2,3])
    if randomChoice==0:
      passw.append(random.choice(string.ascii_uppercase))
    elif randomChoice==1:
      passw.append(random.choice(string.ascii_lowercase))
    elif randomChoice==2:
      passw.append(random.choice(string.digits))
    else:
      passw.append(random.choice(string.punctuation))
  
  random.shuffle(passw)

  return''.join(passw)
    
res=password(10)
print(res)