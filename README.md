# Loja-Mercado
# Aprendi uzar o metodo 'with open', peguei um exemplo deste site (tem bons exemplos e esta bem explicado):
# https://www.freecodecamp.org/news/with-open-in-python-with-statement-syntax-example/
# Uzei este exemplo para fazer o programa:
                  with open("hello.txt", "w") as my_file:
                          my_file.write("Hello world \n")
                          my_file.write("I hope you're doing well today \n")
                          my_file.write("This is a text file \n")
                          my_file.write("Have a nice time \n")

                    with open("hello.txt") as my_file:
                    print(my_file.read())

   
   
   
     #Output: 
   Hello world 
   
   I hope you're doing well today
   
   This is a text file
   
   Have a nice time
