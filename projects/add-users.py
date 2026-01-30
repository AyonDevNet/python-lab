

def addUsers():
    userers= []
    username = input("Enter username: ").strip()
    role = input("Enter role (admin/user): ").strip()
    status = input("Enter status (active/inactive): ").strip()

    userDetails = {

    "username": username,
    "role" : role,
    "status": status

    }

    if userDetails == True:
        print("❌ This user already exists")
    else:
        userers.append(userDetails)
        print("✅ User added successfully")
addUsers()