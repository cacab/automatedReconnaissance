from googlesearch import search

#user menu
print("What would you like to do?")
print("Please enter a number")
print("1 to search by name")
print("2 to search by ip address")
print("3 to search by specific file extension")
choice = input("Enter your choice: ")

if choice == 1:
    query = input('Enter the name enclosed in double quotes like so: "name" ')
    stopNum = input("How many results would you like to see? ")
    f = open("companyNames.txt", "w+")
    print("Results will be written to companyNames.txt")
    for url in search(query, stop=stopNum):
        print(url)
        f.write(url + "\n")


if choice == 2:
    query = input('Enter the ip address enclosed in double quotes like so: "000.000.000" ')
    stopNum = input("How many results would you like to see? ")
    f = open("ipAddresses.txt", "w+")
    print("Results will be written to ipAddresses.txt")
    for url in search(query, stop=stopNum):
        print(url)
        f.write(url + "\n")


if choice == 3:
    targetSite = input('Enter the target site ex: "redhat.com" ')
    query = input('Enter the specific file extension ex: "txt" ')
    stopNum = input("How many results would you like to see? ")
    f = open("fileExtensions.txt", "w+")
    print("Results will be written to fileExtensions.txt")
    for url in search("site: <"+targetSite+"> inurl:php."+query+" filetype:" + query, stop=stopNum):
        print(url)
        f.write(url + "\n")


