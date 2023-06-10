#!/usr/bin/python3

#changing the color of banner and text
banner = '\033[1;32m' + '''
⠀⠀⠀⢀⣴⣾⣿⣿⣿⡶⢦⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⠴⢾⣿⣿⣿⣷⣦⡀⠀⠀⠀
⠀⠀⣰⣿⣿⣿⣿⣿⣿⣿⣷⣦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣡⣴⣾⣿⣿⣿⣿⣿⣿⣿⡄⠀⠀
⠀⠀⠉⠀⠀⠀⠀⠈⠙⠻⣿⣿⣿⣷⡄⠀⠀⠀⠀⠀⣰⣿⣿⣿⡿⠛⠉⠁⠀⠀⠀⠈⠉⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⣯⠁⠀⠀⠀⠀⠀⢈⣿⠟⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢀⡴⢖⣛⣧⣴⣶⣤⣄⠹⡆⡀⠀⠀⠀⠀⡼⢃⣤⣴⣶⣧⣽⣛⡲⣤⠀⠀⠀⠀⠀
⠀⢱⣄⣴⣟⠾⣿⣿⣿⣿⣿⣿⣿⡇⠀⡇⠀⠀⠀⡇⠀⣿⣿⣿⣿⣿⣿⣿⣿⣞⣷⣄⣴⠃⠀
⢠⠟⠉⠉⠉⠛⠓⠿⠏⠸⠟⠛⠉⠀⢠⡇⠀⠀⠀⣿⠀⠀⠉⠛⠻⠇⠿⠟⠛⠋⠉⠉⠙⠻⡀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⡇⠀⠀⠀⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡾⢿⡇⠀⠀⠀⢿⠿⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⡄⠀⠀⠀⠀⠀⠀⠀⣀⣤⢴⠏⠀⣸⠁⠀⠀⠀⢸⡆⠈⢳⡀⣤⡀⠀⠀⠀⠀⠀⠀⠀⡄⠀
⠀⢹⣶⢤⣤⡤⠴⠶⠛⠉⠀⠸⠀⣄⢻⣄⠀⠀⢀⣸⢃⣀⠰⠃⠈⠙⠓⠶⠤⣤⣤⢤⣾⠃⠀
⠀⠈⢿⣆⠻⣿⣄⠀⠀⠀⠀⠀⠀⠉⣱⣬⣍⣉⣯⣥⡉⠁⠀⠀⠀⠀⠀⠀⣴⣿⢃⣾⡏⠀⠀
⠀⠀⠈⢿⣆⠹⣿⣧⣀⣀⣀⣀⣤⣴⣿⣿⠟⠙⢿⣿⣿⣦⣄⣀⣀⣀⣠⣾⡿⠁⣼⠟⠀⠀⠀
⠀⠀⠀⠈⢿⣦⡈⠻⠿⠿⠿⠿⢿⣿⣿⣋⣀⣀⣀⣻⣿⣿⠿⠿⠿⠿⠿⠛⣠⣾⠏⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠻⣎⠓⢤⣀⠀⠀⠀⠉⠉⠉⠉⠉⠉⠉⠉⠁⠀⠀⠀⣀⠴⢊⡿⠋⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠘⢧⠀⠀⠀⠀⠀⠀⠀⢤⣄⣀⣠⡄⠀⠀⠀⠀⠀⠀⢠⠞⠁⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠱⣄⠀⠀⠀⠀⠀⠀⣿⣿⡏⠀⠀⠀⠀⠀⠀⡠⠃⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⠀⠀⠀⠀⠀⣿⣿⣷⠀⠀⠀⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⠇
\033[1;31mM4573R TOOL\033[1;31m⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀''' + '\033[0m'


#printing the banner
print(banner)

#menu to choose between scan port or scam ip
print("\nChoose an option:\n1. Scan port\n2. Scam IP\n")
option = input("Enter your option: ")

if option == "1":
    #importing libraries
    import socket # Required to make socket connections
    import subprocess # Required to run system commands

    #setting the target
    alvo = input('\033[1;36mEnter the IP address or host you want to scan:\033[0m')

    #Setting the port range from 1 to 1024
    for port in range(1, 1025):  
        #Creating a socket to establish connection
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #Setting timeout
        sock.settimeout(1)
        #Trying to connect port
        resultado = sock.connect_ex((alvo, port))
        #If the connection is successful
        if resultado == 0:
            print("\033[1;31mThe door {} it's open\033[0m".format(port))

        #closing the connection
        sock.close()

elif option == "2":
    #import the necessary libraries
    import socket 
    from urllib.parse import urlparse 
     
    Site_url=input('Enter website link: ') 
     
    # Extract the domain from the website 
    parsed_uri = urlparse(Site_url) 
    domain = parsed_uri.netloc 
     
    # Gets the IP address
    ip_address = socket.gethostbyname(domain) 
    print("The IP address of the website is ", ip_address)

else:
    print("Invalid option. Please try again.")