# try:
#     file = open("customers.csv","r")
#     content = file.read()
#     print(content)

# except:
#     print("Memory Error")

def read_file(file_name):
    with open(file_name,"r") as f:
        for line in f:
            yield line

for line in read_file("customers.csv"):
    print(line)


    