#####################################################################################################
#                                                                                                   #
#   Project by JSD Dev Laboratories                                                                 #
#   Programmer: Ivan Karpov                                                                         #
#   Tested with PyCharm Community Edition by JetBrains                                              #
#   Debugged with PyCharm Community Edition by JetBrains                                            #
#   Re-Tested with PyCharm Community Edition by JetBrains                                           #
#   Download PyCharm Community Edition https://www.jetbrains.com/pycharm/download/?section=windows  #
#                                                                                                   #
#####################################################################################################

"""
Main entry file
This is what you run to start the program
All variable names explained in `variables.md` file. Located at root/configs/variables.md
"""
##
 # Import configs
##
from configs.word import AllSupported
from configs.general import Step2
from configs.general import Step1
from configs.general import RecSteps
from configs.general import RecSteps2
from configs.word import Male
from configs.word import Male2
from configs.word import Female
from configs.word import Female2

##
 # Variables
##

GenderInput = str(input("Enter your gender: "))

##
 # Main code - Gender Checker
##
while GenderInput != Male or GenderInput != Male2 or GenderInput != Female or GenderInput != Female2:
    if GenderInput != Male or GenderInput != Male2 or GenderInput != Female or GenderInput != Female2:
        print(f"There was an error reading the gender.")
        print(f"Supported: {AllSupported}")
        GenderInput = str(input("Your gender: "))


##
 # Main Code - Variables
##

    if GenderInput == Male or GenderInput == Male2 or GenderInput == Female or GenderInput == Female2:
        StepCounter = int(input("Enter steps count: "))

##
 # ALU - Arithmetic Logic Unit
 # Converting and Output
##
        if GenderInput == Male or Male2:
            ALU_Input = Step1 * StepCounter
            ALU_Km = ALU_Input / 10000
            print("---------------------------")
            print("    Statistics    ")
            print(f"Steps: {StepCounter}")
            print(f"Distance {ALU_Input}m | {ALU_Km} km")
            if StepCounter < RecSteps:
                print("You have covered a distance")
                print("that is less than the norm.")
                print(f"{StepCounter} / {RecSteps}")
            elif StepCounter > RecSteps:
                print("You have covered a distance")
                print("that is greater than the norm.")
                print(f"{StepCounter} / {RecSteps}")
            else:
                print("You have covered a distance")
                print("that is equal to the norm")
                print(f"{StepCounter} = {RecSteps}")
        else:
            ALU_Input2 = Step2 * StepCounter
            ALU_Km2 = ALU_Input2 / 10000
            print("---------------------------")
            print("    Statistics    ")
            print(f"Steps: {StepCounter}")
            print(f"Distance {ALU_Input2}m | {ALU_Km2}km")
            if StepCounter < RecSteps:
                print("You have covered a distance")
                print("that is less than the norm.")
                print(f"{StepCounter} / {RecSteps2}")
            elif StepCounter > RecSteps:
                print("You have covered a distance")
                print("that is greater than the norm.")
                print(f"{StepCounter} / {RecSteps2}")
            else:
                print("You have covered a distance")
                print("that is equal to the norm")
                print(f"{StepCounter} = {RecSteps2}")
        break
