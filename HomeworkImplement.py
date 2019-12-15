import time
import HomeworkClass as HomeworkImplement

## Environment Setting ## 
#############################################################################################
### Choose Platform ###
CheckPlatform = HomeworkImplement.Platform();
CheckPlatform.setup_method_Chrome();

### Get Website URL ###
NickTest = HomeworkImplement.TestList(CheckPlatform);
NickTest.get_site()


## Test Item ## 
#############################################################################################
### Test 1 ~ 10 units with one random number ###
# NickTest.ImputNumberRandom_FirstElement()
# NickTest.teardown_method()

### Test 1 ~ 10 units with two random number ###
NickTest.InputNumberRandom_TwoElement()
NickTest.teardown_method()

### Input English / Chinese Character ###
# NickTest.InputCharacter()
# NickTest.teardown_method()

### Open and Close app ###
# i = 1
# while i < 10: 
# 	NickTest.teardown_method()
# 	CheckPlatform = HomeworkImplement.Platform();
# 	CheckPlatform.setup_method_Chrome();
# 	NickTest = HomeworkImplement.TestList(CheckPlatform);
# 	NickTest.get_site()
# 	i = i + 1

### Test Load Performance ###
# NickTest.Load_Performance()
# NickTest.teardown_method()

### Test Press Propine Marker Link ###
# NickTest.PressLink()
# NickTest.teardown_method()



