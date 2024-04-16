import torchhd
import torch

def main():

    # num dimensions
    d = 10000

    global vectorMemory
    vectorMemory = torchhd.structures.Memory(0.0)
    
    # Generate hypervectors for the atomic units
    labelV = torchhd.random(3,d)
    nameV = torchhd.random(2,d)
    currencyV = torchhd.random(2,d)
    capitalV = torchhd.random(2,d)

    

    # Assign hypervectors to python variables
    label_Name = labelV[0]
    label_Capital = labelV[1]
    label_Money = labelV[2]
    content_USA = nameV[0]
    content_Mexico = nameV[1]
    content_WashingtonDC = capitalV[0]
    content_MexicoCity = capitalV[1]
    content_Dollar = currencyV[0]
    content_Peso = currencyV[1]

    # Add Vectors to Memory
    vectorMemory.add(label_Name,'label_Name')
    vectorMemory.add(label_Capital,'label_Capital')
    vectorMemory.add(label_Money,'label_Currency')
    vectorMemory.add(content_USA,'content_USA')
    vectorMemory.add(content_Mexico,'content_Mexico')
    vectorMemory.add(content_WashingtonDC,'content_WashingtonDC')
    vectorMemory.add(content_MexicoCity,'content_MexicoCity')
    vectorMemory.add(content_Dollar,'content_Dollar')
    vectorMemory.add(content_Peso,'content_Peso')

    # Bind label-content pair hypervectors (makes like a dictionary)
    bind_NameUSA = torchhd.bind(label_Name, content_USA)
    bind_NameMexico = torchhd.bind(label_Name, content_Mexico)
    bind_CapitalWashingtonDC = torchhd.bind(label_Capital, content_WashingtonDC)
    bind_CapitalMexicoCity = torchhd.bind(label_Capital, content_MexicoCity)
    bind_CurrencyDollar = torchhd.bind(label_Money, content_Dollar)
    bind_CurrencyPeso = torchhd.bind(label_Money, content_Peso)

    # Add New Vectors to Memory
    vectorMemory.add(bind_NameUSA,'bind_NameUSA')
    vectorMemory.add(bind_NameMexico,'bind_NameMexico')
    vectorMemory.add(bind_CapitalWashingtonDC,'bind_CapitalWashingtonDC')
    vectorMemory.add(bind_CapitalMexicoCity,'bind_CapitalMexicoCity')
    vectorMemory.add(bind_CurrencyDollar,'bind_CurrencyDollar')
    vectorMemory.add(bind_CurrencyPeso,'bind_CurrencyPeso')

    # Bundle all US and all Mexico hypervectors together
    bundle_USA = torchhd.bundle(torchhd.bundle(bind_NameUSA, bind_CapitalWashingtonDC), bind_CurrencyDollar)
    bundle_Mexico = torchhd.bundle(torchhd.bundle(bind_NameMexico, bind_CapitalMexicoCity), bind_CurrencyPeso)
    
    # Add New Vectors to Memory
    vectorMemory.add(bundle_USA,'bundle_USA')
    vectorMemory.add(bundle_Mexico,'bundle_Mexico')

    # Bind all data into one mega-hypervector
    bind_AllCountries = torchhd.bind(bundle_USA, bundle_Mexico)

    # Add New Vectors to Memory
    vectorMemory.add(bind_AllCountries,'bind_AllCountries')



    # can you find the hypervector that is the name value of USA?
    
    compute_LabelNameForBundleUSA = torchhd.bind(torchhd.inverse(label_Name),bundle_USA)
    
    intReturn = vectorMemory.__getitem__(compute_LabelNameForBundleUSA)
    print("Name value of USA:")
    print(intReturn)
    print("---------------------------------------")
    

        
     # What is the Dollar of Mexico OG?

    compute_valueOfDollarOfMexico = torchhd.bind(torchhd.inverse(content_Dollar),bind_AllCountries)
    intReturn = vectorMemory.__getitem__(compute_valueOfDollarOfMexico)
    print("Dollar of Mexico OG Way):")
    print(intReturn)
    print("---------------------------------------")

     # What is the Dollar of Mexico try 2?

    compute_valueOfDollarOfMexico = torchhd.bind(label_Money,bind_AllCountries)
    compute_valueOfDollarOfMexico = torchhd.bind(content_Dollar,compute_valueOfDollarOfMexico)
    
    intReturn = vectorMemory.__getitem__(compute_valueOfDollarOfMexico)
    print("Dollar of Mexico (double inverse):")
    print(intReturn)
    print("---------------------------------------")


    # What is the Currency of Mexico? - big / wrong? way
    compute_valueCurrOfMexico = torchhd.bind(bundle_USA,bind_AllCountries)
    compute_valueCurrOfMexico = torchhd.bind(torchhd.inverse(label_Money),compute_valueCurrOfMexico)
    intReturn = vectorMemory.__getitem__(compute_valueCurrOfMexico)
    print("Currency of Mexico (big/worng)")
    print(intReturn)
    print("---------------------------------------")
    print("hello")  

if __name__ == "__main__":
    main()



