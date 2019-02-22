print("Hello, my name is Alan!")
name = input("What's your name? ")
print("Hey, "+ name + "! " + "I'd love to learn some more about you.")
fun_fact = input("Would you like to tell me a fun fact about yourself? ")
if(fun_fact == "yes"):
    yes = input("Awesome, let's hear it! ")
elif(fun_fact == "no"):
    no = input("Aw, okay. How about you tell me your favorite thing to do? ")  
input("That's really cool! (press enter) ")   
age = input("How old are you? ")
print("I'm 423 years old, so that makes me " + str(423 - int(age)) + " years older than you!") 
difference = 423 - int(age)
# print(difference)
print("Let's count together to " + str(difference) + "!")
input("Are you ready? ")
for num in range(0, 25):
    print(num)
print("Just kidding, I wouldn't put us both through that torture!")    
print("I've really enjoyed speaking with you today " + name + "!") 