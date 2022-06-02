from collections import Counter 
 def word_count(apple): 
         with open(apple) as f: 
                 return Counter(f.read().split()) 
  
 print("Number of words in the file :",word_count("apple.txt"))
