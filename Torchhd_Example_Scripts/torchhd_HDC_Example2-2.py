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
    vMap_records = torchhd.random(1,d)

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
    role_record = vMap_records[0]


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
    vectorMemory.add(role_record,'role_record')


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
    
    bundle_Theresa = torchhd.bundle(torchhd.bundle(torchhd.bundle(torchhd.bundle(bind_firstNameTheresa, bind_lastNameSobb), bind_genderFemale),bind_departmentDefence), bind_jobComputing)
    bundle_Andy = torchhd.bundle(torchhd.bundle(torchhd.bundle(torchhd.bundle(bind_firstNameAndrew, bind_lastNameDeHoog), bind_genderMale),bind_departmentDefence), bind_jobLogistics)
    bundle_Andrew = torchhd.bundle(torchhd.bundle(torchhd.bundle(torchhd.bundle(bind_firstNameAndrew, bind_lastNameSobb), bind_genderMale),bind_departmentTransport), bind_jobComputing)
    bundle_Dan = torchhd.bundle(torchhd.bundle(torchhd.bundle(torchhd.bundle(bind_firstNameDaniel, bind_lastNameSobb), bind_genderMale),bind_departmentEducation), bind_jobComputing)
    bundle_Beth = torchhd.bundle(torchhd.bundle(torchhd.bundle(torchhd.bundle(bind_firstNameBeth, bind_lastNameSobb), bind_genderFemale),bind_departmentEducation), bind_jobTeacher)
    bundle_Joe = torchhd.bundle(torchhd.bundle(torchhd.bundle(torchhd.bundle(bind_firstNameJoe, bind_lastNameBloggs), bind_genderUnspecified),bind_departmentFinance), bind_jobAccountant)

    # Add New Vectors to Memory
    vectorMemory.add(bundle_Theresa,'bundle_Theresa')
    vectorMemory.add(bundle_Andy,'bundle_Andy')
    vectorMemory.add(bundle_Andrew,'bundle_Andrew')
    vectorMemory.add(bundle_Dan,'bundle_Dan')
    vectorMemory.add(bundle_Beth,'bundle_Beth')
    vectorMemory.add(bundle_Joe,'bundle_Joe')

    # Bind bundles with record names
    bind_r1_Theresa = torchhd.bind(role_record, bundle_Theresa)
    bind_r2_Andy = torchhd.bind(role_record, bundle_Andy)
    bind_r3_Andrew = torchhd.bind(role_record, bundle_Andrew)
    bind_r4_Dan = torchhd.bind(role_record, bundle_Dan)
    bind_r5_Beth = torchhd.bind(role_record, bundle_Beth)
    bind_r6_Joe = torchhd.bind(role_record, bundle_Joe)

    # Add New Vectors to Memory
    vectorMemory.add(bind_r1_Theresa,'bind_r1_Theresa')
    vectorMemory.add(bind_r2_Andy,'bind_r2_Andy')
    vectorMemory.add(bind_r3_Andrew,'bind_r3_Andrew')
    vectorMemory.add(bind_r4_Dan,'bind_r4_Dan')
    vectorMemory.add(bind_r5_Beth,'bind_r5_Beth')
    vectorMemory.add(bind_r6_Joe,'bind_r6_Joe')

    # Bind and Bundle all data into one mega-hypervector
    bundle_AllRecords = torchhd.bundle(torchhd.bundle(torchhd.bundle(torchhd.bundle(torchhd.bundle(bind_r1_Theresa, bind_r2_Andy),bind_r3_Andrew),bind_r4_Dan),bind_r5_Beth),bind_r6_Joe)

    # Add New Vectors to Memory
    vectorMemory.add(bundle_AllRecords,'bundle_AllRecords')

    
    

    # Similarity Statistics
    tempVal = torchhd.cosine_similarity(bundle_Andy, bundle_Andrew)
    print(f'Bundle Similarity of Andy and Andrew: {tempVal}')

    tempVal = torchhd.cosine_similarity(bind_r2_Andy, bind_r3_Andrew)
    print(f'Bind Record Similarity of Andy and Andrew: {tempVal}')


    tempVal = torchhd.cosine_similarity(bundle_Theresa, bundle_Joe)
    print(f'BUndle Similarity of Tess and Joe: {tempVal}')

    tempVal = torchhd.cosine_similarity(bind_r1_Theresa, bind_r6_Joe)
    print(f'Bind record Similarity of Tess and Joe: {tempVal}')

    # Tests

    #1 Who is a teacher

    

    #tempVal = torchhd.bind((filler_teacher),bundle_AllRecords)
    #tempVal = vectorMemory.__getitem__(tempVal)
    #print(f'No Inverse?: {tempVal}')


    #tempVal = torchhd.bind(torchhd.inverse(filler_teacher),bundle_AllRecords)
    #tempVal = vectorMemory.__getitem__(tempVal)
    #print(f'Inverse?: {tempVal}')

    # up to here

    queryV = filler_teacher
    tempVal = torchhd.bind((queryV),bundle_AllRecords)
    printVal = vectorMemory.__getitem__(tempVal)
    print(f'Attempt: {printVal}')

    # get record fName:
    tempVal = torchhd.bind(role_record, tempVal)
    tempVal = vectorMemory.__getitem__(tempVal)
    print(f'GetRecord: {tempVal}')

    print("done!")

if __name__ == "__main__":
    main()



