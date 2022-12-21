# Interactive quiz app
list_q=["Question 1:\n'OS' computer abbreviation usually means ? \n  A. Order of Significance \n  B. Open Software \n  C. Operating System \n  D. Optical Sensor",'"Question 2:\nWhich is a type of Electrically-Erasable Programmable Read-Only Memory? \n  A. Flash \n  B. Flange \n  C. Fury \n  D. FRAM"',"Question 3:\nA given signal's second harmonic is twice the given signal's __________ frequency...? \n  A. Fourier \n  B. Foundation \n  C. Fundamental \n  D. Field","Question 4:\nThe electromagnetic coils on the neck of the picture tube or tubes which pull the electron beam from side to side and up and down are called a...? \n  A. Transformer \n  B. Yoke \n  C. Capacitor \n  D. Diode"]
list_a=['C','A','C','B']
n=-1

for i in  list_q:
    print(i)
    a=input('Enter your choice: ')
    n+=1
    if a==list_a[n] or a==list_a[n].lower() :
      print('Correct!')
    else:
      print('No, the answer is: ',list_a[n])
    continue
