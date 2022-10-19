    # def functionName():
    #     #Instrucciones de la función

#Fucntions

# def print_message():
#     print("Special Message")
#     print("I'm learnign with new ways as python")

# print_message()

def conversation(message):
    print('hi')
    print('how are you')
    print(message)
    print('bye')

option = input('Choose an option (1, 2, 3): ')
if option == 1:
    conversation('Choose option 1')
elif option == 2:
    conversation('Choose option 2')
elif option == 3:
    conversation('Choose option 3')
else: 
    print('Choose other option')