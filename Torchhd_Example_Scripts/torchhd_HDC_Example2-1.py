import torchhd
import torch

def main():

    # num dimensions
    d = 10000

    global vectorMemory
    vectorMemory = torchhd.structures.Memory(0.0)
    
    # Generate hypervectors for the atomic units unassigned to labels
    vMap_roles = torchhd.random(5,d)
    vMap_firstNames = torchhd.random(5,d)
    vMap_lastNames = torchhd.random(3,d)
    vMap_genders = torchhd.random(3,d)
    vMap_departments = torchhd.random(4,d)
    vMap_jobs = torchhd.random(4,d)

    # Assign hypervectors to python variables for atomic units
    role_firstName = vMap_roles[0]
    role_lastName = vMap_roles[1]
    role_gender = vMap_roles[2]
    role_department = vMap_roles[3]
    role_job = vMap_roles[4]
    filler_female= vMap_genders[0]
    filler_male = vMap_genders[1]
    filler_genUnspecified = vMap_genders[2]
    filler_andrew = vMap_firstNames[0]
    filler_theresa = vMap_firstNames[1]
    filler_daniel = vMap_firstNames[2]
    filler_beth = vMap_firstNames[0]
    filler_joe = vMap_firstNames[4]
    filler_sobb = vMap_lastNames[0]
    filler_bloggs = vMap_lastNames[1]
    filler_deHoog = vMap_lastNames[2]
    filler_education = vMap_departments[0]
    filler_defence = vMap_departments[1]
    filler_transport = vMap_departments[2]
    filler_finance = vMap_departments[3]
    filler_teacher = vMap_jobs[0]
    filler_computing = vMap_jobs[1]
    filler_logistics = vMap_jobs[2]
    filler_accountant = vMap_jobs[3]


    # Add Vectors to Memory
    vectorMemory.add(role_firstName,'role_firstName')
    vectorMemory.add(role_lastName,'role_lastName')
    vectorMemory.add(role_gender,'role_gender')
    vectorMemory.add(role_department,'role_department')
    vectorMemory.add(role_job,'role_job')
    vectorMemory.add(filler_female,'filler_female')
    vectorMemory.add(filler_male,'filler_male')
    vectorMemory.add(filler_genUnspecified,'filler_genUnspecified')
    vectorMemory.add(filler_andrew,'filler_andrew')
    vectorMemory.add(filler_theresa,'filler_theresa')
    vectorMemory.add(filler_daniel,'filler_daniel')
    vectorMemory.add(filler_beth,'filler_beth')
    vectorMemory.add(filler_joe,'filler_joe')
    vectorMemory.add(filler_sobb,'filler_sobb')
    vectorMemory.add(filler_bloggs,'filler_bloggs')
    vectorMemory.add(filler_deHoog,'filler_deHoog')
    vectorMemory.add(filler_education,'filler_education')
    vectorMemory.add(filler_defence,'filler_defence')
    vectorMemory.add(filler_transport,'filler_transport')
    vectorMemory.add(filler_finance,'filler_finance')
    vectorMemory.add(filler_teacher,'filler_teacher')
    vectorMemory.add(filler_computing,'filler_computing')
    vectorMemory.add(filler_logistics,'filler_logistics')
    vectorMemory.add(filler_accountant,'filler_accountant')


    # Bind label-content pair hypervectors (makes like a dictionary)
    bind_genderFemale = torchhd.bind(role_gender, filler_female)
    bind_genderMale = torchhd.bind(role_gender, filler_male)
    bind_genderUnspecified = torchhd.bind(role_gender, filler_genUnspecified)
    bind_firstNameAndrew = torchhd.bind(role_firstName, filler_andrew)
    bind_firstNameTheresa = torchhd.bind(role_firstName, filler_theresa)
    bind_firstNameDaniel = torchhd.bind(role_firstName, filler_daniel)
    bind_firstNameBeth = torchhd.bind(role_firstName, filler_beth)
    bind_firstNameJoe = torchhd.bind(role_firstName, filler_joe)
    bind_lastNameSobb = torchhd.bind(role_lastName, filler_sobb)
    bind_lastNameBloggs = torchhd.bind(role_lastName, filler_bloggs)
    bind_lastNameDeHoog = torchhd.bind(role_lastName, filler_deHoog)
    bind_departmentEducation = torchhd.bind(role_department, filler_education)
    bind_departmentDefence = torchhd.bind(role_department, filler_defence)
    bind_departmentTransport = torchhd.bind(role_department, filler_transport)
    bind_departmentFinance = torchhd.bind(role_department, filler_finance)
    bind_jobTeacher = torchhd.bind(role_job, filler_teacher)
    bind_jobComputing = torchhd.bind(role_job, filler_computing)
    bind_jobLogistics = torchhd.bind(role_job, filler_logistics)
    bind_jobAccountant = torchhd.bind(role_job, filler_accountant)


    # Add New Vectors to Memory
    vectorMemory.add(bind_genderFemale,'bind_genderFemale')
    vectorMemory.add(bind_genderMale,'bind_genderMale')
    vectorMemory.add(bind_genderUnspecified,'bind_genderUnspecified')
    vectorMemory.add(bind_firstNameAndrew,'bind_firstNameAndrew')
    vectorMemory.add(bind_firstNameTheresa,'bind_firstNameTheresa')
    vectorMemory.add(bind_firstNameDaniel,'bind_firstNameDaniel')
    vectorMemory.add(bind_firstNameBeth,'bind_firstNameBeth')
    vectorMemory.add(bind_firstNameJoe,'bind_firstNameJoe')
    vectorMemory.add(bind_lastNameSobb,'bind_lastNameSobb')
    vectorMemory.add(bind_lastNameBloggs,'bind_lastNameBloggs')
    vectorMemory.add(bind_lastNameDeHoog,'bind_lastNameDeHoog')
    vectorMemory.add(bind_departmentEducation,'bind_departmentEducation')
    vectorMemory.add(bind_departmentDefence,'bind_departmentDefence')
    vectorMemory.add(bind_departmentTransport,'bind_departmentTransport')
    vectorMemory.add(bind_departmentFinance,'bind_departmentFinance')
    vectorMemory.add(bind_jobTeacher,'bind_jobTeacher')
    vectorMemory.add(bind_jobComputing,'bind_jobComputing')
    vectorMemory.add(bind_jobLogistics,'bind_jobLogistics')
    vectorMemory.add(bind_jobAccountant,'bind_jobAccountant')


    # Bundle Records/People together

    # make records - up to here #
    
    bundle_r1_Theresa = torchhd.bundle(torchhd.bundle(torchhd.bundle(torchhd.bundle(bind_firstNameTheresa, bind_lastNameSobb), bind_genderFemale),bind_departmentDefence), bind_jobComputing)
    bundle_r2_Andy = torchhd.bundle(torchhd.bundle(torchhd.bundle(torchhd.bundle(bind_firstNameAndrew, bind_lastNameDeHoog), bind_genderMale),bind_departmentDefence), bind_jobLogistics)
    bundle_r3_Andrew = torchhd.bundle(torchhd.bundle(torchhd.bundle(torchhd.bundle(bind_firstNameAndrew, bind_lastNameSobb), bind_genderMale),bind_departmentTransport), bind_jobComputing)
    bundle_r4_Dan = torchhd.bundle(torchhd.bundle(torchhd.bundle(torchhd.bundle(bind_firstNameDaniel, bind_lastNameSobb), bind_genderMale),bind_departmentEducation), bind_jobComputing)
    bundle_r5_Beth = torchhd.bundle(torchhd.bundle(torchhd.bundle(torchhd.bundle(bind_firstNameBeth, bind_lastNameSobb), bind_genderFemale),bind_departmentEducation), bind_jobTeacher)
    bundle_r6_Joe = torchhd.bundle(torchhd.bundle(torchhd.bundle(torchhd.bundle(bind_firstNameJoe, bind_lastNameBloggs), bind_genderUnspecified),bind_departmentFinance), bind_jobAccountant)

    # Add New Vectors to Memory
    vectorMemory.add(bundle_r1_Theresa,'bundle_r1_Theresa')
    vectorMemory.add(bundle_r2_Andy,'bundle_r2_Andy')
    vectorMemory.add(bundle_r3_Andrew,'bundle_r3_Andrew')
    vectorMemory.add(bundle_r4_Dan,'bundle_r4_Dan')
    vectorMemory.add(bundle_r5_Beth,'bundle_r5_Beth')
    vectorMemory.add(bundle_r6_Joe,'bundle_r6_Joe')

    # Bind and Bundle all data into one mega-hypervector
    bind_AllRecords = torchhd.bind(torchhd.bind(torchhd.bind(torchhd.bind(torchhd.bind(bundle_r1_Theresa, bundle_r2_Andy),bundle_r3_Andrew),bundle_r4_Dan),bundle_r5_Beth),bundle_r6_Joe)
    bundle_AllRecords = torchhd.bundle(torchhd.bundle(torchhd.bundle(torchhd.bundle(torchhd.bundle(bundle_r1_Theresa, bundle_r2_Andy),bundle_r3_Andrew),bundle_r4_Dan),bundle_r5_Beth),bundle_r6_Joe)

    # Add New Vectors to Memory
    

    vectorMemory.add(bind_AllRecords,'bind_AllRecords')
    vectorMemory.add(bundle_AllRecords,'bundle_AllRecords')

    # Create negative and positive vectors
    tempV =  torchhd.random(1,d)
    tempV = tempV[0]
    negOneVector = torchhd.bind(torchhd.negative(tempV), tempV)
    posOneVector = torchhd.negative(negOneVector)

    vectorMemory.add(negOneVector, 'negOneVector')
    vectorMemory.add(posOneVector, 'posOneVector')

    print("configuration complete")

    # Similarity Statistics
    
    #tempVal = torchhd.cosine_similarity(bundle_r1_Theresa, bundle_r6_Joe)
    #print(f'Similarity of Tess and Joe: {tempVal}')

    #  --------------------------------------------------------------------
    # Tests
    #  ---------------------------------------------------------------------

    print(f'----------------------------------- \nTests \n -----------------------------------')


    # Test 01
    # Difference between two bundles - i.e. Difference between 'bundle_r2_Andy and bundle_r3_Andrew'
    tempVal = torchhd.cosine_similarity(bundle_r2_Andy, bundle_r3_Andrew)
    print(f'Test One \nSimilarity of two bundles - Andy and Andrew: {tempVal} \n -----------------------------------')



    # Test  02
    # Return value pairings for two different pair values - i.e. windows*injection and injection*process. 
    ### NOT TESTED AND APPLICABLE TO THIS SCENARIO
    

    #tempVal = torchhd.bind((filler_teacher),bundle_AllRecords)
    #tempVal = vectorMemory.__getitem__(tempVal)
    #print(f'No Inverse?: {tempVal}')


    #tempVal = torchhd.bind(torchhd.inverse(filler_teacher),bundle_AllRecords)
    #tempVal = vectorMemory.__getitem__(tempVal)
    #print(f'Inverse?: {tempVal}')

    # up to here

    #does mum-bundle contain job*teacher?
    tempVal = torchhd.bind(bundle_r5_Beth, torchhd.negative(bind_jobTeacher))
    tempCos = torchhd.cosine_similarity(tempVal, negOneVector)
    tempMem = vectorMemory.__getitem__(tempVal)
    if tempMem[1] == 'negOneVector' or tempMem[1] == 'posOneVector':
        print("mum-bundle contains job-teacher")
    else:
        print("mum-bundle DOES NOT contain job-teacher")


    #is there someone who is a teacher?
    tempVal = torchhd.bind(bundle_AllRecords, torchhd.negative(bind_jobTeacher))
    tempCos = torchhd.cosine_similarity(tempVal, negOneVector)
    tempMem = vectorMemory.__getitem__(tempVal)
    if tempMem[1] == 'negOneVector' or tempMem[1] == 'posOneVector':
        print("all-bundle contains job-teacher")
    else:
        print("all-bundle DOES NOT contain job-teacher")

        

    # if there are multiple people who work in computing, then how many?
    # could you get the average vector value after you times it, then use that as an approx

    tempVal = torchhd.bind(bundle_AllRecords, torchhd.negative(bind_jobComputing))
    aveVal = torch.mean(tempVal)
    tempMem = vectorMemory.__getitem__(tempVal)
    if tempMem[1] == 'negOneVector' or tempMem[1] == 'posOneVector':
        if aveVal <-0.5:
            aveVal = torchhd.negative(aveVal)
        print(f'all-bundle contains {aveVal} job-computer (not inc strength / separates multiples)')
    else:
        print("all-bundle DOES NOT contain job-computer")
    



    queryV = torchhd.bind((bind_jobTeacher), bundle_r5_Beth)
    print(f'r5 beth: \n{bundle_r5_Beth}')
    print(f'bind job_teacher: \n{bind_jobTeacher}')
    print(f'queryV: \n{queryV}')
    #tempVal = torchhd.bind((queryV),bundle_AllRecuncle
    minus_queryV = torchhd.negative(queryV)
    print(f'minus_queryV: \n{minus_queryV}')
    searchVal = torchhd.bundle(bundle_r5_Beth, minus_queryV)
    print(f'SearchVal: \n{searchVal}')
    tempVal = vectorMemory.__getitem__(searchVal)
    print(f'Attempt search from mem: \n{tempVal}')

    print("Cosine of Attempt")
    cosineOut = torchhd.cosine_similarity(bind_jobTeacher,searchVal)
    print(cosineOut)

    print("done")

if __name__ == "__main__":
    main()



