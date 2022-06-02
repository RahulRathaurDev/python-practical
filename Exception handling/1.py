try: 
     fp=open("apple.txt","a") 
     try: 
         fp.write("This is my test file") 
     finally: 
         print("Closing the file") 
         fp.close() 
 except IOError as e: 
     print("Error:",e) 
 o=open("apple.txt","r") 
 print(o.read())
