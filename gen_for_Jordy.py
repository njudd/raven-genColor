import raven_gen
from raven_gen import Matrix, MatrixType, Ruleset, RuleType
import matplotlib.pyplot as plt
from PIL import Image
import os
import numpy as np


#raven_gen.attribute.SIZE_VALUES
#raven_gen.attribute.COLOR_VALUES

raven_gen.attribute.SIZE_VALUES = (.3, .5, .7, .9) # maybe do 4? .25, .5, .75 1
raven_gen.attribute.SIZE_MAX = 3 # need to tell it the length of the new vector when it changes

#### There is a google doc called "MatrixStimuliNotes" as well

# Where is the noise attribute can you chanage that?
# ^^^ you can't making noise is possible (specifically by adding a rule in rule.py)
# yet... making alternatives with noise would require entirely different logic,
# because right now all of the alternatives "work"; so they can be subsitutited
# yet with noise, you can't pick another rule of the atribute (as the rule is NO rule)
#
# with "rulset" it will just pick four rules at random; not ideal behaviour?
# ^^^ this does not happen; the thing is 'number' and 'position' are linked they form 'configuration'
# while the others (color, sizzze, shape) are a different class (see the SI of paper)
# therefore the function does not allow non-constant rules to occur on both of the attributes
#
# Also importantly they exclude the arthmetic rule on Type, since it makes no sense
# since our function is no using color this is also the case with color (gray scale can increment)
# we have not yet hardcoded the function to not allow it; also distribute 3 is very hard in color
#
# I would fool around up the alternatives count;
# The alternatives by definition don't follow the rule set;
# so you might have to figure out a way to make reasonable(ish) alternatives?
# ^^^ we have decided to make 8 and manually pick 3; this is something we should expand if we get the OSF grant



# all constant
ruleset_1_constant = Ruleset(size_rules=[RuleType.CONSTANT],
                  shape_rules=[RuleType.CONSTANT],
                  color_rules=[RuleType.CONSTANT],
                  number_rules=[RuleType.CONSTANT], # if you only do single stimulis this isn't an issue
                  position_rules=[RuleType.CONSTANT])

ruleset_2_sizeProgression = Ruleset(size_rules=[RuleType.PROGRESSION],
                  shape_rules=[RuleType.CONSTANT],
                  color_rules=[RuleType.CONSTANT],
                  number_rules=[RuleType.CONSTANT], # if you only do single stimulis this isn't an issue
                  position_rules=[RuleType.CONSTANT])

ruleset_3_sizeDist3 = Ruleset(size_rules=[RuleType.DISTRIBUTE_THREE],
                  shape_rules=[RuleType.CONSTANT],
                  color_rules=[RuleType.CONSTANT],
                  number_rules=[RuleType.CONSTANT], # if you only do single stimulis this isn't an issue
                  position_rules=[RuleType.CONSTANT])

ruleset_4_sizeArith = Ruleset(size_rules=[RuleType.ARITHMETIC],
                  shape_rules=[RuleType.CONSTANT],
                  color_rules=[RuleType.CONSTANT],
                  number_rules=[RuleType.CONSTANT], # if you only do single stimulis this isn't an issue
                  position_rules=[RuleType.CONSTANT])

ruleset_5_shapeProgression = Ruleset(size_rules=[RuleType.CONSTANT],
                  shape_rules=[RuleType.PROGRESSION],
                  color_rules=[RuleType.CONSTANT],
                  number_rules=[RuleType.CONSTANT], # if you only do single stimulis this isn't an issue
                  position_rules=[RuleType.CONSTANT])

ruleset_6_shapeDist3 = Ruleset(size_rules=[RuleType.CONSTANT],
                  shape_rules=[RuleType.DISTRIBUTE_THREE],
                  color_rules=[RuleType.CONSTANT],
                  number_rules=[RuleType.CONSTANT], # if you only do single stimulis this isn't an issue
                  position_rules=[RuleType.CONSTANT])

# advanced for the other layouts

ruleset_7_numProg = Ruleset(size_rules=[RuleType.CONSTANT],
                  shape_rules=[RuleType.CONSTANT],
                  color_rules=[RuleType.CONSTANT], # you have too many color options & not enough blocks for this too work
                  number_rules=[RuleType.PROGRESSION], # if you only do single stimulis this isn't an issue
                  position_rules=[RuleType.CONSTANT])


ruleset_8_numDist3 = Ruleset(size_rules=[RuleType.CONSTANT],
                  shape_rules=[RuleType.CONSTANT],
                  color_rules=[RuleType.CONSTANT], # you have too many color options & not enough blocks for this too work
                  number_rules=[RuleType.DISTRIBUTE_THREE], # if you only do single stimulis this isn't an issue
                  position_rules=[RuleType.CONSTANT])

ruleset_9_numArith = Ruleset(size_rules=[RuleType.CONSTANT],
                  shape_rules=[RuleType.CONSTANT],
                  color_rules=[RuleType.CONSTANT], # you have too many color options & not enough blocks for this too work
                  number_rules=[RuleType.ARITHMETIC], # if you only do single stimulis this isn't an issue
                  position_rules=[RuleType.CONSTANT])

ruleset_10_positionProg = Ruleset(size_rules=[RuleType.CONSTANT],
                  shape_rules=[RuleType.CONSTANT],
                  color_rules=[RuleType.CONSTANT], # you have too many color options & not enough blocks for this too work
                  number_rules=[RuleType.CONSTANT], # if you only do single stimulis this isn't an issue
                  position_rules=[RuleType.PROGRESSION])

ruleset_11_positionDist3 = Ruleset(size_rules=[RuleType.CONSTANT],
                  shape_rules=[RuleType.CONSTANT],
                  color_rules=[RuleType.CONSTANT], # you have too many color options & not enough blocks for this too work
                  number_rules=[RuleType.CONSTANT], # if you only do single stimulis this isn't an issue
                  position_rules=[RuleType.DISTRIBUTE_THREE])

ruleset_12_mix_sizeProg_shapeDist3 = Ruleset(size_rules=[RuleType.PROGRESSION],
                                             shape_rules=[RuleType.DISTRIBUTE_THREE])
ruleset_13_mix_numArith_shapeProg = Ruleset(number_rules=[RuleType.ARITHMETIC],
                                             shape_rules=[RuleType.PROGRESSION])
ruleset_14_mix_sizeArith_shapeConst = Ruleset(size_rules=[RuleType.ARITHMETIC],
                                             shape_rules=[RuleType.CONSTANT])


#### playspace ####
# import raven_gen
# from raven_gen import Matrix, MatrixType, Ruleset, RuleType, AttributeType
# import os
# import numpy as np
#
# #AttributeType.UNIFORMITY = (True)
#
# # Uniformity
# raven_gen.attribute.UNI_VALUES = (False, False, False)
# raven_gen.attribute.UNI_MIN = 0
# raven_gen.attribute.UNI_MAX = len(raven_gen.attribute.UNI_VALUES) - 1
#
#
# #raven_gen.component.Uniformity
#
#
# # I think you need to get into the ComponentType (import this)
# # there you should have component.uniformity.value...?
#
# #from raven_gen import Matrix, MatrixType, Ruleset, RuleType, ComponentType, LayoutType
# #Matrix.attribute_bounds[MatrixType.FOUR_SHAPE][(ComponentType.NONE, LayoutType.GRID_FOUR)]
#
# os.chdir('/Users/njudd/Desktop/ct_ravGen')
# ruleset_ct = Ruleset(number_rules=[RuleType.CONSTANT],
#                      position_rules=[RuleType.CONSTANT], # called configuration?
#                      shape_rules=[RuleType.CONSTANT],
#                      size_rules=[RuleType.CONSTANT],
#                      color_rules=[RuleType.CONSTANT]
#                      )
#
# rpm_ct = Matrix.make(list(MatrixType)[1], ruleset=ruleset_ct) #, n_alternatives=5
# rpm_ct.save(path = ".", puzzle_name="ct_rav")
# print(rpm_ct.rules)
# #print(rpm_ct.rules, file="rules.txt")
# print(rpm_ct)

# there is some error depending on a certian combination...
# remember they do special things for position & number (you should only rand the attribute table)
#### playspace ####



# https://stackoverflow.com/questions/4326658/how-to-index-into-a-dictionary
# first_key = list(rules)[0]
# first_val = list(rules.values())[0]

# using dicts instead of lists
rules = {'ruleset_1_constant':ruleset_1_constant,
         'ruleset_2_sizeProgression':ruleset_2_sizeProgression, 'ruleset_3_sizeDist3':ruleset_3_sizeDist3,
         'ruleset_4_sizeArith':ruleset_4_sizeArith, 'ruleset_5_shapeProgression':ruleset_5_shapeProgression, 'ruleset_6_shapeDist3':ruleset_6_shapeDist3}

rules_extra = {'ruleset_1_constant':ruleset_1_constant,
         'ruleset_2_sizeProgression':ruleset_2_sizeProgression, 'ruleset_3_sizeDist3':ruleset_3_sizeDist3,
         'ruleset_4_sizeArith':ruleset_4_sizeArith, 'ruleset_5_shapeProgression':ruleset_5_shapeProgression, 'ruleset_6_shapeDist3':ruleset_6_shapeDist3,
               'ruleset_7_numProg':ruleset_7_numProg, 'ruleset_8_numDist3':ruleset_8_numDist3, 'ruleset_9_numArith':ruleset_9_numArith,
               'ruleset_10_positionProg':ruleset_10_positionProg, 'ruleset_11_positionDist3':ruleset_11_positionDist3}

# new try's
rules_new = {'ruleset_12_mix_sizeProg_shapeDist3':ruleset_12_mix_sizeProg_shapeDist3,
             'ruleset_13_mix_numArith_shapeProg':ruleset_13_mix_numArith_shapeProg,
             'ruleset_14_mix_sizeArith_shapeConst':ruleset_14_mix_sizeArith_shapeConst}
rules = rules_new
rules_extra = rules_new


# because its only single pieces (i.e., list(MatrixType)[0])
# you can't change position

os.getcwd()
os.chdir('/Users/njudd/surfdrive/Shared/ravenStim/rpms_new_CT')


# I could do a for look with 3 but I want different rule sets so I will just hardcode
os.mkdir('/Users/njudd/surfdrive/Shared/ravenStim/rpms_new_CT/layout1')
os.chdir('/Users/njudd/surfdrive/Shared/ravenStim/rpms_new_CT/layout1')

for w in range(len(rules)):
    os.mkdir("rpm_" + list(rules)[w])
    os.chdir("rpm_" + list(rules)[w])
    #print(w)
    for i in range(10):
        loopname = ("rpm_prob_" + list(rules)[w])
        loopname += str(i)
        #print("innerloop")
        #print(i)
        rpm = Matrix.make(list(MatrixType)[0], ruleset=list(rules.values())[w], n_alternatives=3)
        os.mkdir(loopname)  # making a dir for the rpm stuff
        rpm.save(loopname + "/.", loopname)  # going in that dir, also naming the stimuli by the loopname

        with open(loopname + "/" + loopname + "output.txt",
                  "a") as f:  # going into the folder and making an output per item
            print(rpm.rules, file=f)

        with open("Global_output.txt", "a") as f:  # going into the folder and making an output per item
            print(rpm.rules, file=f)
    os.chdir("..")

    # barf rules
    with open("Global_rules.txt", "a") as f:  # going into the folder and making an output per item
        print(list(rules)[w], file=f)



os.mkdir('/Users/njudd/surfdrive/Shared/ravenStim/rpms_new_CT/layout2')
os.chdir('/Users/njudd/surfdrive/Shared/ravenStim/rpms_new_CT/layout2')

for w in range(len(rules_extra)):
    os.mkdir("rpm_" + list(rules_extra)[w])
    os.chdir("rpm_" + list(rules_extra)[w])
    #print(w)
    for i in range(10):
        loopname = ("rpm_prob_" + list(rules_extra)[w])
        loopname += str(i)
        #print("innerloop")
        #print(i)
        rpm = Matrix.make(list(MatrixType)[1], ruleset=list(rules_extra.values())[w], n_alternatives=3)
        os.mkdir(loopname)  # making a dir for the rpm stuff
        rpm.save(loopname + "/.", loopname)  # going in that dir, also naming the stimuli by the loopname

        with open(loopname + "/" + loopname + "output.txt",
                  "a") as f:  # going into the folder and making an output per item
            print(rpm.rules, file=f)

        with open("Global_output.txt", "a") as f:  # going into the folder and making an output per item
            print(rpm.rules, file=f)
    os.chdir("..")

    # barf rules
    with open("Global_rules.txt", "a") as f:  # going into the folder and making an output per item
        print(list(rules_extra)[w], file=f)


os.mkdir('/Users/njudd/surfdrive/Shared/ravenStim/rpms_new_CT/layout3')
os.chdir('/Users/njudd/surfdrive/Shared/ravenStim/rpms_new_CT/layout3')

for w in range(len(rules_extra)):
    os.mkdir("rpm_" + list(rules_extra)[w])
    os.chdir("rpm_" + list(rules_extra)[w])
    #print(w)
    for i in range(10):
        loopname = ("rpm_prob_" + list(rules_extra)[w])
        loopname += str(i)
        #print("innerloop")
        #print(i)
        rpm = Matrix.make(list(MatrixType)[2], ruleset=list(rules_extra.values())[w], n_alternatives=3)
        os.mkdir(loopname)  # making a dir for the rpm stuff
        rpm.save(loopname + "/.", loopname)  # going in that dir, also naming the stimuli by the loopname

        with open(loopname + "/" + loopname + "output.txt",
                  "a") as f:  # going into the folder and making an output per item
            print(rpm.rules, file=f)

        with open("Global_output.txt", "a") as f:  # going into the folder and making an output per item
            print(rpm.rules, file=f)
    os.chdir("..")

    # barf rules
    with open("Global_rules.txt", "a") as f:  # going into the folder and making an output per item
        print(list(rules_extra)[w], file=f)






















os.getcwd()


os.chdir("/Users/njudd/Desktop/rpms_100rand")
# just making 100 randomly sampled
for i in range(100):
    loopname = "rpm_ct_"
    loopname += str(i)
    # print("innerloop")
    # print(i)
    rpm = Matrix.make(list(MatrixType)[0], n_alternatives=3)
    os.mkdir(loopname)  # making a dir for the rpm stuff
    rpm.save(loopname + "/.", loopname)  # going in that dir, also naming the stimuli by the loopname

    with open(loopname + "/" + loopname + "output.txt",
              "a") as f:  # going into the folder and making an output per item
        print(rpm.rules, file=f)

    with open("Global_output.txt", "a") as f:  # going into the folder and making an output per item
        print(rpm.rules, file=f)





# maybe make a panda's dataframe of the rules as well?


# only doing gimme so I can take a look at it without saving
#rpm.gimme()
#plt.imshow(Image.fromarray(rpm.ans_img), cmap='gray')
#plt.axis('off')
#plt.show()
print(rpm.rules)
#print(rpm)

with open("output.txt", "a") as f: # a is for append
  print("start")
  print(rpm.rules, file=f)
  print("end")




