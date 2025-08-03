import getpass

username = input("Enter your username: ")
password = getpass.getpass("Enter your password: ")

print("\nLogging in...")
print("Username: ", username)
print("Password: [hidden for security]")
