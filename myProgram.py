import os
import random
import datetime
import statistics

random.seed(1)

inputOntology = "datasets/web.owl"
inputSubclassStatements = "datasets/subClasses.nt"
forgetOntology = "datasets/web.owl"
method = "3"
signature = "datasets/signature.txt"


def CreateForgetOrder(forget_input):
    forget_file = open(forget_input, "r")

    forget_order = []
    for line in forget_file:
        forget_order.append(line)
    return forget_order


def main():
    global forgetOntology
    NUM_REPEATS = 10
    forget_file = "./forget_this_web_forward.txt"
    forget_order = CreateForgetOrder(forget_file)

    times = []
    for i in range(NUM_REPEATS):
        print('\t\t\tREPEAT', i+1)
        # random.shuffle(forget_order)
        forgetOntology = "datasets/web.owl"
        start = datetime.datetime.now()

        for concept in forget_order:
            with open(signature, 'w') as f:  # overwrites file every time
                f.write(concept)

            os.system(
                'java -cp lethe-standalone.jar uk.ac.man.cs.lethe.internal.application.ForgettingConsoleApplication --owlFile '
                + forgetOntology + ' --method ' + method + ' --signature ' + signature)

            forgetOntology = './result.owl'
        end = datetime.datetime.now()
        diff = end - start
        times.append(diff.total_seconds() * 1000)

        print('\n\t\t\tDONE WITH REPEAT', i+1, '\n\t\t\t', diff.total_seconds() * 1000,'\n')

    print('DONE\nAVERAGE:\t', statistics.mean(times), '\nSD:\t\t\t', statistics.stdev(times), '\nMIN:\t\t', min(times),
          '\nMAX:\t\t', max(times))


# This is an example puython programme which shows how to use the different stand-alone versions of OWL reasoners and forgetting programme

# # Choose the ontology (in the OWL format) for which you want to explain the entailed subsumption relations.
# inputOntology = "datasets/pizza.owl"

# # Choose the set of subclass for which you want to find an explanation.
# # this file can be generated using the second command (saveAllSubClasses)
# inputSubclassStatements = "datasets/subClasses.nt"

# # Choose the ontology to which you want to apply forgetting. This can be the inputOntology, but in practise
# # should be a smaller ontology, e.g. created as a justification for a subsumption
# forgetOntology = "datasets/pizza.owl"

# # Decide on a method for the forgetter (check the papers of LETHE to understand the different options).
# # The default is 1, I believe.
# # 1 - ALCHTBoxForgetter
# # 2 - SHQTBoxForgetter
# # 3 - ALCOntologyForgetter
# method = "3"  #

# # Choose the symbols which you want to forget.
# signature = "datasets/signature.txt"


# 1. PRINT ALL SUBCLASSES (inputOntology):
# print all subClass statements (explicit and inferred) in the inputOntology
# --> uncomment the following line to run this function
# os.system('java -jar kr_functions.jar ' + 'printAllSubClasses' + " " + inputOntology)

# 2. SAVE ALL SUBCLASSES (inputOntology):
# save all subClass statements (explicit and inferred) in the inputOntology to file datasets/subClasses.nt
# --> uncomment the following line to run this function
# os.system('java -jar kr_functions.jar ' + 'saveAllSubClasses' + " " + inputOntology)

# 3. PRINT ALL EXPLANATIONS (inputOntology, inputSubclassStatements):
# print explanations for each subClass statement in the inputSubclassStatements
# --> uncomment the following line to run this function
# os.system('java -jar kr_functions.jar ' + 'printAllExplanations' + " " + inputOntology + " " + inputSubclassStatements)

# 4. SAVE ALL EXPLANATIONS (inputOntology, inputSubclassStatements):
# save explanations for each subClass statement in the inputSubclassStatements to file datasets/exp-#.owl
# --> uncomment the following line to run this function
# os.system('java -jar kr_functions.jar ' + 'saveAllExplanations' + " " + inputOntology + " " + inputSubclassStatements)


# For running LETHE forget command:
# --> uncomment the following line to run this function
# os.system(
#     'java -cp lethe-standalone.jar uk.ac.man.cs.lethe.internal.application.ForgettingConsoleApplication --owlFile ' + forgetOntology + ' --method ' + method + ' --signature ' + signature)

main()
