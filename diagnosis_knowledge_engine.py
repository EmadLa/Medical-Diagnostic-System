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
    def askForHeadache(self):
        self.declare(Symptom(name ='headache', isExist = input('Do you have a headache? (yes/no)\n')))

    @Rule(Symptom(name='headache', isExist = 'yes')) 
    def askForPulsingHeadache(self):
        self.declare(Symptom(name ='Pulsing Headache', isExist = input('Do you have a Pulsing Headache (yes/no)\n')))

    @Rule(Symptom(name='headache', isExist = 'no')) 
    def askForSyncope(self):
        self.declare(Symptom(name ='Syncope', isExist = input('Do you have a Syncope (yes/no)\n')))

    @Rule(Symptom(name='Pulsing Headache', isExist = 'yes')) 
    def askForPainInTheUpperPartOfTheHead(self):
        self.declare(Symptom(name ='Pain in the upper part of the head', isExist = input('Do you have a Pain in the upper part of the head (yes/no)\n')))
        
    @Rule(Symptom(name='Pulsing Headache', isExist = 'no')) 
    def askForTightHeadache(self):    
        self.declare(Symptom(name ='Tight headache', isExist = input('Do you have a Tight headache (yes/no)\n')))

    @Rule(Symptom(name='Pain in the upper part of the head', isExist = 'yes')) 
    def printClusterHeadache(self):
        self.declare(Disease(name ='Cluster Headache'))
        
    @Rule(Symptom(name='Pain in the upper part of the head', isExist = 'no')) 
    def askForPainInPartOfTheHead(self):    
        self.declare(Symptom(name ='Pain in the right/left part of the head', isExist = input('Do you have a Pain in the right/left part of the head (yes/no)\n')))
    
    @Rule(Symptom(name='Pain in the right/left part of the head', isExist = 'yes')) 
    def printMigraine(self):
        self.declare(Disease(name ='Migraine'))
        
    @Rule(Symptom(name='Pain in the right/left part of the head', isExist = 'no')) 
    def printNotInLeftOfHead(self):    
        self.declare(Disease(name ='NULL'))

    @Rule(Symptom(name='Pulsing Headache', isExist = 'no')) 
    def askForTightHeadache(self):
        self.declare(Symptom(name ='Tight headache', isExist = input('Do you have a Tight headache (yes/no)\n')))

    @Rule(Symptom(name='Tight headache', isExist = 'yes')) 
    def askForSpasmHeadache(self):    
        self.declare(Symptom(name ='Spasm Headache', isExist = input('Do you have a Spasm Headache (yes/no)\n')))

    @Rule(Symptom(name='Tight headache', isExist = 'no')) 
    def askForMadeYouWakingUpFromSleeping(self):
        self.declare(Symptom(name ='Made you waking up from sleeping', isExist = input('Do you have a Made you waking up from sleeping (yes/no)\n')))

    @Rule(Symptom(name='Spasm Headache', isExist = 'no')) 
    def printPsychologicalDistress(self):    
        self.declare(Disease(name ='Psychological Distress'))

    @Rule(Symptom(name='Spasm Headache', isExist = 'yes')) 
    def printNotPsychologicalDistress(self):
        self.declare(Disease(name ='NULL'))

    @Rule(Symptom(name='Made you waking up from sleeping', isExist = 'no')) 
    def printNotFromSleeping(self):    
        self.declare(Disease(name ='NULL'))

    @Rule(Symptom(name='Made you waking up from sleeping', isExist = 'yes')) 
    def askForFountainVomit(self):
        self.declare(Symptom(name ='Fountain Vomit', isExist = input('Do you have a Fountain Vomit (yes/no)\n')))

    @Rule(Symptom(name='Fountain Vomit', isExist = 'yes')) 
    def printbrainTumor(self):    
        self.declare(Disease(name ='brain Tumor'))

    @Rule(Symptom(name='Fountain Vomit', isExist = 'no')) 
    def printNotbrainTumor(self):    
        self.declare(Disease(name ='NULL'))

    @Rule(Symptom(name='Syncope', isExist = 'yes')) 
    def askForHypotension(self):
        self.declare(Symptom(name ='Hypotension', isExist = input('Do you have a Hypotension (yes/no)\n')))
        
    @Rule(Symptom(name='Syncope', isExist = 'no')) 
    def askForVertigo(self):    
        self.declare(Symptom(name ='Vertigo', isExist = input('Do you have a Vertigo (yes/no)\n')))

    @Rule(Symptom(name='Hypotension', isExist = 'yes')) 
    def printOrthostaticHypotension(self):
        self.declare(Disease(name ='Orthostatic Hypotension'))
        
    @Rule(Symptom(name='Hypotension', isExist = 'no')) 
    def askForWhilePeeing(self):    
        self.declare(Symptom(name ='While Peeing', isExist = input('Do you have a While Peeing (yes/no)\n')))

    @Rule(Symptom(name='While Peeing', isExist = 'yes')) 
    def printPeeSyncope(self):
        self.declare(Disease(name ='Pee Syncope'))
        
    @Rule(Symptom(name='Hypotension', isExist = 'no')) 
    def askForWhileMakingANecktie(self):    
        self.declare(Symptom(name ='While making a Necktie', isExist = input('Do you have a While making a Necktie (yes/no)\n')))

    @Rule(Symptom(name='While making a Necktie', isExist = 'yes')) 
    def printVagalSyncope(self):
        self.declare(Disease(name ='Vagal Syncope'))
        
    @Rule(Symptom(name='While making a Necktie', isExist = 'no')) 
    def askForPeripheralVasodilation(self):    
        self.declare(Symptom(name ='Peripheral vasodilation', isExist = input('Do you have a Peripheral vasodilatione (yes/no)\n')))

    @Rule(Symptom(name='Peripheral vasodilation', isExist = 'yes')) 
    def printAnotherVasovagalSyncope(self):
        self.declare(Disease(name ='Vasovagal Syncope'))
        
    @Rule(Symptom(name='Peripheral vasodilation', isExist = 'no')) 
    def printNotVasovagalSyncope(self):    
        self.declare(Disease(name ='Vagal Syncope'))

    @Rule(Symptom(name='Vertigo', isExist = 'yes')) 
    def askForReal(self):
        self.declare(Symptom(name ='Real', isExist = input('Do you have a Real (yes/no)\n')))
        
    @Rule(Symptom(name='Real', isExist = 'yes')) 
    def printInnerEarInfection(self):
        self.declare(Disease(name ='Inner ear infection'))
        
    @Rule(Symptom(name='Real', isExist = 'no')) 
    def askForLie(self):    
        self.declare(Symptom(name ='Lie', isExist = input('Do you have a Lie (yes/no)\n')))    

    @Rule(Symptom(name='Real', isExist = 'yes')) 
    def printPsychologicalProblem (self):
        self.declare(Disease(name ='Psychological Problem'))

    @Rule(Symptom(name='Real', isExist = 'no')) 
    def printNotPsychologicalProblem (self):
        self.declare(Disease(name ='NULL'))

    @Rule(Symptom(name='Vertigo', isExist = 'no')) 
    def askForGaitDisturbance(self):    
        self.declare(Symptom(name ='Gait disturbance', isExist = input('Do you have a Gait disturbance (yes/no)\n')))

    @Rule(Symptom(name='Gait disturbance', isExist = 'yes'))
    def askForSpastic(self):
         self.declare(Symptom(name ='Spastic', isExist = input('Do you have a Spastic? (yes/no)\n')))

    @Rule(Symptom(name='Spastic', isExist = 'yes')) 
    def printPyramidalInjury(self):
        self.declare(Disease(name ='Pyramidal injury'))

    @Rule(Symptom(name='Spastic', isExist = 'no'))
    def askForStagger(self):
         self.declare(Symptom(name ='Stagger', isExist = input('Do you have a Stagger? (yes/no)\n')))

    @Rule(Symptom(name='Stagger', isExist = 'yes')) 
    def printCerebellumInjury(self):
        self.declare(Disease(name ='Cerebellum injury'))

    @Rule(Symptom(name='Stagger', isExist = 'no'))
    def askForGaitHemiphegiar(self):
         self.declare(Symptom(name ='Gait hemiphegia', isExist = input('Do you have a Gait hemiphegia? (yes/no)\n')))

    @Rule(Symptom(name='Gait hemiphegia', isExist = 'yes')) 
    def printHemiphegia(self):
        self.declare(Disease(name ='Hemiphegia'))

    @Rule(Symptom(name='Gait hemiphegia', isExist = 'no'))
    def askForMilitary(self):
         self.declare(Symptom(name ='Military', isExist = input('Do you have a Military? (yes/no)\n')))

    @Rule(Symptom(name='Military', isExist = 'yes')) 
    def printPosteriorCordInjury(self):
        self.declare(Disease(name ='Posterior cord injury'))

    @Rule(Symptom(name='Military', isExist = 'no'))
    def askForTrendlenburg(self):
         self.declare(Symptom(name ='trendlenburg', isExist = input('Do you have a trendlenburg? (yes/no)\n')))

    @Rule(Symptom(name='trendlenburg', isExist = 'yes')) 
    def printCongenitalHipDislocation(self):
        self.declare(Disease(name ='Congenital hip dislocation'))

    @Rule(Symptom(name='trendlenburg', isExist = 'no'))
    def askForGaitParkinson(self):
         self.declare(Symptom(name ='Gait parkinson', isExist = input('Do you have a Gait parkinson? (yes/no)\n')))

    @Rule(Symptom(name='Gait parkinson', isExist = 'yes')) 
    def printParkinsonDisease(self):
        self.declare(Disease(name ='Parkinson Disease'))

    @Rule(Symptom(name='Gait parkinson', isExist = 'no'))
    def askForNotParkinson(self):
        self.declare(Disease(name ='NULL'))

    @Rule(Symptom(name='Gait disturbance', isExist = 'no')) 
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
    def printSpontaneous(self):
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
    def printNotDancingMoving(self):
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
    def printChronic(self):
        self.declare(Disease(name ='NULL'))

    @Rule(Symptom(name='Involuntary movement', isExist = 'no'))
    def askForInjuryInNerves(self):
         self.declare(Symptom(name ='Injury in nerves', isExist = input('Do you have a Injury in nerves? (yes/no)\n')))

    @Rule(Symptom(name='Injury in nerves', isExist = 'yes'))
    def askForSeeingDifficulty(self):
         self.declare(Symptom(name ='Seeing Difficulty', isExist = input('Do you have a Seeing Difficulty ? (yes/no)\n')))

    @Rule(Symptom(name='Injury in nerves', isExist = 'no'))
    def printInjuryNerve(self):
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
    def printSternocleidomastoid(self):
        self.declare(Disease(name ='NULL'))

