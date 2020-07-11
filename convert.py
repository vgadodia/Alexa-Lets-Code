import os

def get_python_code(TEXT):
    lines = [x.strip() for x in TEXT.split("new line")]
    
    word_to_num = {"one": 1, "two": 2, "three": 3, "four": 4,
               "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9, "ten": 10}
    for i in range(len(lines)):
        words = lines[i].split()
    
        if words[0] == "back" and words[1] == "tab":
            lines[i] = "\b"
        
        elif words[0] == "print" and words[1] == "string":
            lines[i] = "print(\"" + " ".join(words[2:]) + "\")"
        elif words[0] == "print":
        
            try:
                lines[i] = "print(" + str(word_to_num[words[1]]) + ")"
            except:
                lines[i] = "print(" + " ".join(words[1:]) + ")"
        elif (words[1] == "equals" or words[1] == "=") and words[2] == "string":
            lines[i] = words[0] + " = " + "'" + ' '.join(words[3:]) + "'"
        elif (words[1] == "equals" or words[1] == "=") and words[2] == "list":
            lines[i] = words[0] + " = ["
            j = 3
            while j < len(words):
                if words[j] == 'string':
                    lines[i] += "'" + words[j+1] + "', "
                    j += 2
                else:
                
                    lines[i] += words[j] + ", "
                
                    j += 1
            lines[i] = lines[i][:-2] + "]"

        elif words[1] == "equals" or words[1] == "=":
            try:
                lines[i] = words[0] + \
                    " = " + str(word_to_num[words[2]])
            except:
                lines[i] = words[0] + " = " + " ".join(words[2:])
        elif words[0] == "if" and (words[2] == "equals" or words[2] == "=") and words[3] == "string":
            words[2] = "=="
            lines[i] = " ".join(words[:3]) + " '" + ' '.join(words[4:]) + "'" + ":"
            

        elif words[0] == "if" and (words[2] == "equals" or words[2] == "="):
            words[2] = "=="
            lines[i] = " ".join(words) + ":"
            
        elif words[0] == "for" and words[3] == "range":
            lines[i] = " ".join(words[:4]) + "(" + ' '.join(words[4:]) + ")" + ":"
            
        elif words[0] == "for":
            lines[i] = " ".join(words) + ":"
            
        elif words[0] == "function" and len(words) == 2:
            lines[i] = "def " + words[1] +  "()" + ":"
            
        elif words[0] == "function" and len(words) > 2:
            lines[i] = "def " + words[1] +  "("
            for j in range(3, len(words)):
                lines[i] += words[j] + ", "
            lines[i] = lines[i][:-2] + "):"
        
        elif words[0] == "call" and len(words) == 2:
            lines[i] = words[1] +  "()"
        elif words[0] == "call" and len(words) > 2:
            lines[i] = words[1] +  "("
            for j in range(3, len(words)):
                lines[i] += words[j] + ", "
            lines[i] = lines[i][:-2] + ")"



    toParse = "\n".join([x for x in lines if x != ""])
    return toParse
import git
g = git.cmd.Git("C:/Users/Nand/Alexa-Lets-Code")
g.add(".")
g.commit("-m \"init\"")
g.push()