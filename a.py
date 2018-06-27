#take a file name as an arguement. This function should attempt to open file, catch error. Read line by line. Each line appended to a list and return list. Each element will be a string of each element.

#It is implied by the example in the project that unsupported operators are those other than + and - so this is how it has been programed.

def readFile(L,fileName):
  with open(fileName,"r") as f:
    data = f.read().split('\n')
  return data

def openFile():
  fileName = ""
  nest = ""
  flag = 1
  while flag is 1:
   try:
      fileName = input("Input file name: ")
      f = open(fileName, "r")
      flag = 0
   except:
        print("Filename invalid, please try again!")
        flag = 1
  if flag is 0:
    nest = readFile(nest,fileName)

  return nest


def doMath(L):
    finalOutput = []
    K = L
    flag = 0
    for c in range(0,len(K)):
        curStr = K[c]
        curStr.split(" ")
        for i in range(0,len(curStr)):
            if curStr[i] is " " or curStr[i] is "\n":
                i += 1
            elif curStr[i].isdigit() is False:
                if curStr[i] == "+" or curStr[i] == "-" or curStr[i] == "*" or curStr[i] == "/" :
                   flag = 0
                else:
                   flag = 1
                   break
                
            else:
               flag = 0

        if flag is 0:
            a = eval(curStr)
            finalOutput.append(a)
        if flag is 1:
            print("invalid chracter in input")
            return -1
    return finalOutput

def outputFile(vals):
    try:
        outputfile = open("outputfile.txt","w")
        print("File created successfully")
    except IOError:
        print("there was an error creating output file!")

    for i in range(0,len(vals)):
        outputfile.write(str(vals[i] )+ "\n")


def main():
  T = openFile()
  ans = doMath(T)
  if ans != -1:
      outputFile(ans)

main()