





class TestClass:


    def __init__(self):
        return;

    def EnterInfo(self,input1):
        self.stored = input1;
        return;

    def DisplayInfo(self):
        print("(" + str( self.stored) + ")");
        return;



# create objects
object1 = TestClass();
object2 = TestClass();
object3 = TestClass();
object4 = TestClass();
object5 = TestClass();


# set objects data
object1.EnterInfo("Hello");
object2.EnterInfo("World");
object3.EnterInfo(True);
object4.EnterInfo(12);
object5.EnterInfo(5.3);

# Add to list
list1 = [object1,object2,object3,object4,object5];


for object in list1:
    object.DisplayInfo();
