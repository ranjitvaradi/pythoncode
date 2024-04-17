
def is_palindrome(word):
   l=[]
   for x in word:
      l.append(x)
   k=list(l[::-1])
   if k==l:
      return True
   else:
      return False
y=is_palindrome(input("enter a word: "))
print(y)
   







   
   
   
   
   

   
   
         

         
         
   
      

