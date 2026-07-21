import sys

print('Python Will search importing Module in these PATH :-')
for e in sys.path :
    print(e)
print()
sys.path.append('/home/ndey/Python/Module_Packages')

print('Now Python Will search importing Module in these PATH :-')
for e in sys.path :
    print(e)

print()
import Package1.Module1

print(Package1.Module1.add(10,20))

