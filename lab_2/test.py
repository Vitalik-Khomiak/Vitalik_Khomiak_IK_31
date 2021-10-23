#2.1
print("First_constant: ", True)
print("Thirs_constant: ", None)
print("Second_constant: ", False)

#2.2
x = 2
print(f"x + 2 = {eval('x+2')}")
print(f"4 в квадраті = {pow(4,2)}")
print("Максимальне число з чисел 5,8,9,3,45 :",max(5,8,9,3,45))

#2.3
#a
x=10
if x==10:
    print ('x=10')

else:
    print ('x!=10')

#b
for x in "ArtLab":
  print(x)

#2.4
x = '5'
try:
    x += 7
except TypeError as error:
    print(f"Error: {error}, occured !!!check your code")
finally:
    print("x = {x}({type(x)})")

#2.5
with open("1.txt", 'r') as readme_file:
    first_str = readme_file.readline()
    print(first_str)

#2.6
aor = lambda x, y: print(f"Площа: {x*y}")
aor(8,5)
