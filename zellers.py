f_name=raw_input('Enter your first name:')
l_name=raw_input('Enter your last name:')
print('Enter your date of birth:')
print('NB. Year starts from March i.e March=1, April=2....February=12')
A=input('Month?')
B=input('Day?')
C=input('Year? [please enter last 2 digits only]')
D=input('Century?')
if A==11 or A==12:
    C=C-1
W = (13*A-1)/5
Y=D/4
X=C/4
Z = W + X + Y + B + C - 2*D
R = Z%7
if R<0:
    R+7
elif R==0:
   print'sunday'
elif R==1:
   print'monday'
elif R==2:
   print'tuesday'
elif R==3:
   print'wednesday'
elif R==4:
   print'thursday'
elif R==5:
   print'friday'
elif R==6:
   print'saturday'
