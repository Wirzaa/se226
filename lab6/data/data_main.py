from simple_package import cleaner
from simple_package import analyzer

userString = str(input("Enter your list in one string: "))

stringList = userString.split(',')

cleanList = cleaner.strip_whitespaces(stringList)
cleanList = cleaner.remove_duplicates(cleanList)

cleanIntList = [int(num) for num in cleanList]

print(analyzer.calculate_mean(cleanIntList))
print(analyzer.find_max(cleanIntList))
print(analyzer.find_min(cleanIntList))
