from experta import *

class Symptom(Fact):
    name = Field(str)
    isExist = Field(str)


class Disease(Fact):
    name = Field(str)


class DiseasesKnowledgeEngine(KnowledgeEngine):

    @Rule(Disease(name = MATCH.name))
    def result(self,name):
        print(name)

    @Rule(NOT(Symptom()))
    # def symptom_1(self):
    #     self.declare(Symptom(name ='headache', isExist = input('Do you have a headache? (yes/no)\n')))

    # @Rule(Symptom(name='headache', isExist = 'yes'))
    # def symptom_2(self):
    #     self.declare(Symptom(name ='symptom_2', isExist = input('Do you have a symptom_2? (yes/no)\n')))

    # @Rule(Symptom(name='headache', isExist = 'no'))
    # def symptom_3(self):
    #     self.declare(Symptom(name ='symptom_3', isExist = input('Do you have a symptom_3? (yes/no)\n')))


    @Rule(NOT(Symptom()))
    def symptom_1(self):
        self.declare(Symptom(name ='headache', isExist = input('Do you have a headache? (yes/no)\n')))
        
    @Rule(Symptom(name='Gait disturance', isExist = 'no')) 
    def askForInvoluntaryMovement(self):
        self.declare(Symptom(name ='Involuntary movement', isExist = input('Do you have a involuntary movement? (yes/no)\n')))

    @Rule(Symptom(name='Involuntary movement', isExist = 'yes'))
    def askForShiver(self):
         self.declare(Symptom(name ='Shiver', isExist = input('Do you have a Shiver? (yes/no)\n')))
    
    @Rule(Symptom(name='Shiver', isExist = 'yes')) 
    def askForSmooth(self):
        self.declare(Symptom(name ='Smooth', isExist = input('Do you have a Smooth? (yes/no)\n')))

    @Rule(Symptom(name='shiver', isExist = 'no'))
    def askForCanonMovements(self):
         self.declare(Symptom(name ='Canon movements', isExist = input('Do you have a Canon Movements? (yes/no)\n')))

    @Rule(Symptom(name='Smooth', isExist = 'yes'))
    def printHyperthyroidism(self):
        self.declare(Disease(name ='Hyperthyroidism'))

    @Rule(Symptom(name='Smooth', isExist = 'no'))
    def askForRough(self):
        self.declare(Symptom(name ='Rough', isExist = input('Do you have a Rough? (yes/no)\n')))

    @Rule(Symptom(name='Rough', isExist = 'yes'))
    def printDrugStopping(self):
        self.declare(Disease(name ='A Drug Stopping'))

    @Rule(Symptom(name='Rough', isExist = 'no'))
    def askForIntentionally(self):
        self.declare(Symptom(name ='Intentionally', isExist = input('Do you have a Intentionally? (yes/no)\n')))

    @Rule(Symptom(name='Intentionally', isExist = 'no'))
    def askForSpontaneous(self):
        self.declare(Symptom(name ='Spontaneous', isExist = input('Do you have a Spontaneous? (yes/no)\n')))

    @Rule(Symptom(name='Intentionally', isExist = 'yes'))
    def printCereblellumInjury(self):
        self.declare(Disease(name ='Cerebellum injury'))

    @Rule(Symptom(name='Spontaneous', isExist = 'yes'))
    def printParkinsonDisease(self):
        self.declare(Disease(name ='Parkinson disease'))

    @Rule(Symptom(name='Spontaneous', isExist = 'no'))
    def printNull(self):
        self.declare(Disease(name ='Spontaneous'))

    @Rule(Symptom(name='Canon movements', isExist = 'yes')) 
    def printOtriped(self):
        self.declare(Disease(name ='Otriped body injury'))

    @Rule(Symptom(name='Canon movements', isExist = 'no')) 
    def askForDancingMoving(self):
        self.declare(Symptom(name ='Dancing moving', isExist = input('Do you have a Dancing moving? (yes/no)\n')))

    @Rule(Symptom(name='Dancing moving', isExist = 'yes')) 
    def askForAcute(self):
        self.declare(Symptom(name ='Acute', isExist = input('Do you have a Acute? (yes/no)\n')))

    @Rule(Symptom(name='Dancing moving', isExist = 'no')) 
    def printNull(self):
        self.declare(Disease(name ='NULL'))

    @Rule(Symptom(name='Acute', isExist = 'yes')) 
    def printSydenham(self):
        self.declare(Disease(name ='Sydenham'))

    @Rule(Symptom(name='Acute', isExist = 'no')) 
    def askForChronic(self):
        self.declare(Symptom(name ='Chronic', isExist = input('Do you have a Chronic? (yes/no)\n')))

    @Rule(Symptom(name='Chronic', isExist = 'yes')) 
    def printHuntigton(self):
        self.declare(Disease(name ='Huntigton'))

    @Rule(Symptom(name='Chronic', isExist = 'no')) 
    def printNULL(self):
        self.declare(Disease(name ='NULL'))

    @Rule(Symptom(name='involuntary movement', isExist = 'no'))
    def askForInjuryInNerves(self):
         self.declare(Symptom(name ='Injury in nerves', isExist = input('Do you have a Injury in nerves? (yes/no)\n')))

    @Rule(Symptom(name='Injury in nerves', isExist = 'yes'))
    def askForSeeingDifficulty(self):
         self.declare(Symptom(name ='Seeing Difficulty', isExist = input('Do you have a Seeing Difficulty ? (yes/no)\n')))

    @Rule(Symptom(name='Injury in nerves', isExist = 'no'))
    def printNULL(self):
         self.declare(Disease(name ='NULL'))

    @Rule(Symptom(name='Seeing Difficulty', isExist = 'yes'))
    def PRintOpticalNerve(self):
        self.declare(Disease(name ='Injury in optical nerve'))

    @Rule(Symptom(name='Seeing Difficulty', isExist = 'no'))
    def askForSmellingDifficulty(self):
        self.declare(Symptom(name ='Smelling Difficulty', isExist = input('Do you have a Smelling Difficulty? (yes/no)\n')))

    @Rule(Symptom(name='Smelling Difficulty', isExist = 'yes'))
    def printAlfactoryNerve(self):
        self.declare(Disease(name ='Injury in alfactory nerve'))

    @Rule(Symptom(name='Smelling Difficulty', isExist = 'no'))
    def askForMovingEyeDifficulty(self):
        self.declare(Symptom(name ='Moving eye Difficulty', isExist = input('Do you have a Moving eye Difficulty ? (yes/no)\n')))

    @Rule(Symptom(name='Moving eye Difficultye', isExist = 'yes'))
    def printOcularNerve(self):
        self.declare(Disease(name ='Injury in ocular nerve'))

    @Rule(Symptom(name='Moving eye Difficulty', isExist = 'no'))
    def askForDifficultyInAbducenteye(self):
        self.declare(Symptom(name ='Difficulty in abducenteye', isExist = input('Do you have a Difficulty in abducenteye? (yes/no)\n')))

    @Rule(Symptom(name='Difficulty in abducenteye', isExist = 'yes'))
    def printAbducentNerve(self):
        self.declare(Disease(name ='Injury in abducent nerve'))

    @Rule(Symptom(name='Difficulty in abducenteye', isExist = 'no'))
    def askForDifficultyInMovingFaceMuscler(self):
        self.declare(Symptom(name ='Difficulty in moving face muscle', isExist = input('Do you have a Difficulty in moving face muscle? (yes/no)\n')))

    @Rule(Symptom(name='Difficulty in moving face muscle', isExist = 'yes'))
    def printFacialNerve(self):
        self.declare(Disease(name ='Injury in facial nerve'))

    @Rule(Symptom(name='Difficulty in moving face muscle', isExist = 'no'))
    def askForLossOfTaste(self):
        self.declare(Symptom(name ='Loss of taste sense in the posterior third', isExist = input('Do you have a Loss of taste sense in the posterior third? (yes/no)\n')))

    @Rule(Symptom(name='Loss of taste sense in the posterior third', isExist = 'yes'))
    def askForGlossopharyngeal(self):
        self.declare(Disease(name ='Injury in glossopharyngeal nerve'))

    @Rule(Symptom(name='Loss of taste sense in the posterior third', isExist = 'no'))
    def askForUvulaDeviation(self):
        self.declare(Symptom(name ='Uvula deviation', isExist = input('Do you have a Uvula deviation? (yes/no)\n')))

    @Rule(Symptom(name='Uvula deviation', isExist = 'yes'))
    def printVegal(self):
        self.declare(Disease(name ='Injury in vegal nerve'))

    @Rule(Symptom(name='Uvula deviation', isExist = 'no'))
    def askForSternocleidomastoid(self):
        self.declare(Symptom(name ='Weakness of the Sternocleidomastoid', isExist = input('Do you have a Weakness of the Sternocleidomastoid? (yes/no)\n')))

    @Rule(Symptom(name='Weakness of the Sternocleidomastoid', isExist = 'yes'))
    def printAccesory(self):
        self.declare(Disease(name ='Injury in accesory nerve'))

    @Rule(Symptom(name='Weakness of the Sternocleidomastoid', isExist = 'no'))
    def printNULL(self):
        self.declare(Disease(name ='NULL'))

