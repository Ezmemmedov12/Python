#####   REVENUE CALCULATOR   #####


# g---gelir
# x---xerc
# k---kateqoriya

# mv---menfeet vergisi
# xg---xalis gelir
# vm---verginin meblegi
# ak--- alt kategoriya

g=int(input('Gelirinizi daxil edin: '))
x=int(input('Xercinizi daxil edin: '))
k=str(input('Fiziki və ya Huquqi şəxs olduğunuzu daxil edin: '))
if k=='Huquqi':
  if g<=x:
    print('Menfeet vergisi: 0')
    print('Xalis gelir:', g)
  else:
    mv=(g-x)*20/100
    xg=g-mv
    print('Menfeet vergisi:',mv)
    print('Xalis gelir:',xg)
elif k=='Fiziki':
  ak=str(input('Dovlet ve ya Ozel müəssisədə islediyinizi daxil edin: '))
  if ak=='Dovlet':
   if g<=x:
    print('Verginin meblegi: 0')
    print('Xalis gelir:', g)
   elif g<=2500:
     if g<=200:
       print('Verginin meblegi: 0')
       print('Xalis gelir:', g)
     else:  
       vm=(g-200)*14/100
       xg=g-vm
       print('Verginin meblegi:',vm)
       print('Xalis gelir:',xg)
   else:
       vm=350+(g-2500)*25/100
       xg=g-vm
       print('Verginin meblegi:',vm)
       print('Xalis gelir:',xg)
  elif ak=='Ozel':
    if g<=x:
      print('Verginin meblegi: 0')
      print('Xalis gelir:', g)
    elif g<=8000:
       print('Verginin meblegi: 0')
       print('Xalis gelir:', g)
    else:
       vm=350+(g-2500)*25/100
       xg=g-vm
       print('Verginin meblegi:',vm)
       print('Xalis gelir:',xg)
  else:
     print('Melumat duzgun daxil olunmayib.Programi yeniden ise salin.')
else:
  print('Melumat duzgun daxil olunmayib.Programi yeniden ise salin.')

