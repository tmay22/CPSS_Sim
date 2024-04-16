import Old_V1_Files.Setup_V1 as Setup_V1
import Old_V1_Files.Graph_V1 as Graph_V1

# Setup_v1 is the non HDC setup
def main_SetupV1():

    global personList_glob
    global edgeList_glob

    print("")
    setupOption= input("Choose Setup Option: \n 1. Default \n 2. Small (10 pers) \n...etc \n")
    
    

    print("You Selected " + setupOption)
    
    setupOutput = Setup_V1.build(setupOption)

    personList_glob = setupOutput[0]
    edgeList_glob = setupOutput[1]

    exportChoice= input("Would you like to export to graph? (Y/N) \n")
    if "Y" in exportChoice or "y" in exportChoice:
        #writtenFile = Graph.exportVNAGraph(personList_glob, edgeList_glob)
        writtenFile = Graph_V1.exportGexfGraph(personList_glob, edgeList_glob)
    
    print("hello")


def main():

    print("hello")



if __name__ == "__main__":
    main()