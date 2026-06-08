# Create a decorator:

# checks whether user is logged in
# if logged in → run function
# otherwise print: Access denied
# Useful in banking or Soical media apps

def login_required(check_login):
    def wrapper(*args, **kwargs):
        if(args[0]=="snehil" and args[1]==12345 and args[2]=="fremont" ):
            print("Logged in\n")
            result = check_login(*args, **kwargs)
            return result
        else:
            print("Access denied")
    return wrapper
        
        

@login_required
def login_check(username, password, city, age):

    print(f"Hi {username} Welcome to the app. Your age is {age} and city is {city} ")

login_check("snehil",12345, "fremont" ,age=29)