

# Loop 5 times
for i in [0,1,2,3,4]:
    print(i);

for i in range(0,5):
    print(i);


list2 = ["Hello","World","12345678","Testing","Learning"];


for name in ["tristan","amos","Hello","world"]:
    print(name)


# loop until stop is true
stop = True;
while stop == True:
    print("Looping until stop is true")
    stop = False; # loops once because we set stop to true

# loop forever
while 1:
    print("Looping Forever")

# loop forever
while True:
    print("Looping Forever")


for filename in os.listdir("./"):
    print(" File or Folder -> " + filename)
