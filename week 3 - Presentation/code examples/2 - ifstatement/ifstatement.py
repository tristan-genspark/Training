



if 1 == 1:
    print("1 eaquals 1");


if FileExsists() == True:
    DeleteFile();

if 1 == True:
    print("1 is not False");


# if 4 is greater than or eaqual to  >=
if 4 >= 2:
    print("4 is greater than or eaqual to 2");


#  in python there is no != syntax You must use "not"
if not 4 == 2:
    print("4 does not eaqual 2");
elif 4 == 5:
    print("4 eaquals 2 ");
else:
    print("None of the if statements above are valid")




value = FileLocatedin("C:\\Users\\Name\\.AppDir");
if value:
    UpdateFile();

if not FileLocatedin("C:\\Users\\Name\\.AppDir"):
    UpdateFile();
elif FileLocatedin("C:\\Users\\Name\\Storage") == True:
    UpdateFile();
else:
    MakeFile();


# elif statements "else if" can be useful to prevent
# if statements from being called if another stement was already called
# This example shows how only one if statement is called

var1 = 7;
if var1 == 7:
    var1 = var1 + 1;
elif var1 == 8:
    var1 = var1 + 2;



var1 = 7;

if var1 == 7:
    var1 = var1 + 1;
    print("Adding one to var1")

elif var1 == 8:
    var1 = var1 + 2;
    print("Adding two to var1")

print(var1)



'''

A simple scenerio

If the temperature is above 76  F
      turn on the AC Unit

'''

maxtemp = 76;
temperature = 82;

if temperature > maxtemp:
    print("Tuning on AC Unit")















#
