#Getting the email address from the user
email = input("Enter Your Email: ").strip()

#calculating the input
username = email[:email.index("@")]
domain_name = email[email.index("@")+1:]

#Formating the result
format_ = (f"Your user name is '{username}' and your domain is '{domain_name}'")
print(format_)