"""Question 1: Implement a function is_balanced(expression) that takes a string 
containing parentheses, curly braces, and square brackets,and determines whether 
the expression is balanced. 

An expression is considered balanced if each opening bracket has a corresponding closing 
bracket in the correct order.

sample input = 

expression1 = "([]{})"
expression2 = "([)]"
print(is_balanced(expression1))  # Output: True
print(is_balanced(expression2))  # Output: False 
"""


def is_balanced(string):
   
    if  string=="":
        return True
    
    for x in string:
        string=string.replace("()","")
        string=string.replace("[]","")
        string=string.replace("{}","")

    return True if string=="" else False
    
print(is_balanced("(){}[]"))    #true
print(is_balanced("([{}])"))    #true
print(is_balanced("(}"))        #false
print(is_balanced("[(])"))      #false
print(is_balanced("[({})](]"))  #false


"""Question 2: Write a function remove_duplicates(sequence) that takes a 
sequence (list or tuple) and returns a new sequence with duplicates 
removed while maintaining the original order of elements. 

sample input = 

input_sequence = [2, 3, 2, 4, 5, 3, 6, 7, 5]
result = remove_duplicates(input_sequence)
print(result)  # Output: [2, 3, 4, 5, 6, 7] 
"""



def remove_duplicates(array):
   
   buffer=[]
   for x in array:
       if x not in buffer:
           buffer.append(x)

   return buffer


print(remove_duplicates([2, 3, 2, 4, 5, 3, 6, 7, 5]))


"""
Question 3: Implement a function word_frequency(sentence) that takes 
a sentence and returns a dictionary containing the frequency of each 
word in the sentence. 

Ignore punctuation and consider words in a case-insensitive manner. 

sample input = 

sentence = "This is a test sentence. This sentence is a test."
result = word_frequency(sentence)
print(result)"""


def word_frequency(sentence):

    sentence=sentence.lower()
    sentence=sentence.strip(",'\"")
    sentence=sentence.replace('.', '')
    
    array=sentence.split()

    my_dict={}

    while array !=[]:
        j=array[0]
        my_dict.update({j:array.count(j)})
        array=list(filter(lambda a: a !=j, array))

    return my_dict

example="This is a test sentence. This sentence is a test."
print(word_frequency(example))
        





    

    
  
         
         
         
    
    
              



