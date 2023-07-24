class Workout:
    def __init__(self, name, description):
        self.name = name
        self.description = description


class Activity:
    def __init__(self, customer, coach, workout, workout_date, start_time, end_time):
        self.customer = customer
        self.coach = coach
        self.workout = workout
        self.workout_date = workout_date
        self.start_time = start_time
        self.end_time = end_time


def add_coach(manager, name, age, email, phone_number, address, sport):
    coach = Coach(name, age, email, phone_number, address, sport)
    manager.add_coach(coach)
    print("Coach added successfully")


def remove_coach(manager, name):
    for coach in manager.coaches:
        if coach.name == name:
            manager.remove_coach(coach)
            print("Coach removed successfully")
            break
    else:
        print("Coach not found")


def add_membership(manager, customer_name, start_date, end_date, price):
    for customer in manager.customers:
        if customer.name == customer_name:
            membership = Membership(customer, start_date, end_date, price)
            manager.add_membership(membership)
            print("Membership added successfully")
            break
    else:
        print("Customer not found")


def remove_membership(manager, customer_name):
    for membership in manager.memberships:
        if membership.customer.name == customer_name:
            manager.remove_membership(membership)
            print("Membership removed successfully")
            break
    else:
        print("Membership not found")


def add_workout(manager, name, description):
    workout = Workout(name, description)
    manager.add_workout(workout)
    print("Workout added successfully")


def remove_workout(manager, name):
    for workout in manager.workouts:
        if workout.name == name:
            manager.remove_workout(workout)
            print("Workout removed successfully")
            break
    else:
        print("Workout not found")


def add_activity(manager, customer_name, coach_name, workout_name, workout_date, start_time, end_time):
    customer = next(
        (customer for customer in manager.customers if customer.name == customer_name), None)
    coach = next(
        (coach for coach in manager.coaches if coach.name == coach_name), None)
    workout = next(
        (workout for workout in manager.workouts if workout.name == workout_name), None)
    if customer and coach and workout:
        activity = Activity(customer, coach, workout,
                            workout_date, start_time, end_time)
        manager.add_activity(activity)
        customer.add_activity(activity)
        coach.add_activity(activity)
        print("Activity added successfully")
    else:
        print("Invalid input")


def remove_activity(manager, customer_name, coach_name, workout_date, start_time):
    for activity in manager.activities:
        if activity.customer.name == customer_name and activity.coach.name == coach_name and activity.workout_date == workout_date and activity.start_time == start_time:
            manager.remove_activity(activity)
            activity.customer.remove_activity(activity)
            activity.coach.remove_activity(activity)
            print("Activity removed successfully")
            break
    else:
        print("Activity not found")


def search_coach(manager, sport):
    coaches = manager.search_coach(sport)
    if coaches:
        for coach in coaches:
            print(coach)
    else:
        print("No coach found")


def search_history(manager, name):
    activities = manager.search_history(name)
    if activities:
        for activity in activities:
            print(activity.workout_date,
                  activity.start_time, activity.workout.name)
    else:
        print("No activity found")


class User:
    def __init__(self, side, name, userName, password, age, email, phone_number, address):
        self.side = side
        self.name = name
        self.userName = userName
        self.password = password
        self.age = age
        self.email = email
        self.phone_number = phone_number
        self.address = address


class Admin(User):
    def __init__(self, name, userName, password, age, email, phone_number, address):
        super().__init__("Admin", name, userName, password,
                       age, email, phone_number, address)


class Membership(User):
    def __init__(self, name, userName, password, age, email, phone_number, address, Amount):
        super().__init__("Membership", name, userName, password,
                       age, email, phone_number, address)
        self.amount = Amount
        self.coaches = []
        self.customers = []
        self.workouts = []
        self.activities = []

    def add_coach(self, coach):
        self.coaches.append(coach)

    def remove_coach(self, coach):
        self.coaches.remove(coach)

    def add_workout(self, workout):
        self.workouts.append(workout)

    def remove_workout(self, workout):
        self.workouts.remove(workout)

    def add_activity(self, activity):
        self.activities.append(activity)

    def remove_activity(self, activity):
        self.activities.remove(activity)

    def search_coach(self, sport):
        return [coach for coach in self.coaches if coach.sport == sport]

    def search_history(self, name):
        customer = next(
            (customer for customer in self.customers if customer.name == name), None)
        if customer:
            return customer.activities
        return None


class Coach(User):
    def __init__(self, name, userName, password, age, email, phone_number, address, sport):
        super().__init__("Coach", name, userName, password,
                       age, email, phone_number, address)
        self.sport = sport
        self.activities = []

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, Email: {self.email}, Phone Number: {self.phone_number}, Address: {self.address}, Sport: {self.sport}"

    def add_activity(self, activity):
        self.activities.append(activity)

    def remove_activity(self, activity):
        self.activities.remove(activity)

def remove_User(Username):
    global Users
    for user in Users:
        if user.name == Username:
            Users.remove(user)

admin = Admin("admin" ,"admin","admin" , 19 , None, None ,None)
Users = [admin]
def main():
    global Users
    user_SignIn = None

    print("\n\nWelcome to the Sports Management System!\n")

    while True:
        userName = input("Enter User Name : ")
        password = input("Enter Password : ")

        for user in Users:
            if userName == user.name and password == user.password:
                user_SignIn = user
                print(f"\nhello {user.name}")
                print("Welcome Back")

        if user_SignIn != None and user_SignIn.side == "Admin":

            while True:
                print("Please choose an option:")
                print("1. Add User")
                print("2. Remove User")
                print("3. Exit\n")

                choice = input("Enter your choice: ")

                if choice == "1":
                    print("-"*10, "Add User", "-"*10)
                    item = input("""
                    1 => Add Admin 
                    2 => Add Coah
                    3 => Add Membership
                      => """)
                    name = input("Enter Name : ")
                    userName = input("Enter User Name : ")
                    password = input("Enter Passsword : ")
                    age = input("Enter Age : ")
                    try:
                        age = int(age)
                    except:
                        print("format Age Not Valid")

                    email = input("Enter email : ")
                    phone_number = input("Enter Phone Number : ")
                    address = input("Enter Address : ")
                    match item:
                        case "1":

                            new_user = Admin(name, userName, password,
                                            age, email, phone_number, address)
                            Users.append(new_user)
                        case "2":

                            sport = input("Enter Sport : ")
                            new_user = Coach(name, userName, password,
                                            age, email, phone_number, address, sport)
                            Users.append(new_user)
                        case "3":
                            try:

                                amount = int(input("Enter Amount Of MemberShip : "))
                            except:
                                print("Format Amount not Valid! ")
                            new_user = Membership(name, userName, password,
                                            age, email, phone_number, address, amount)
                            Users.append(new_user)

                elif choice == "2":
                    UserName = input("Enter User Name : ")
                    remove_User(UserName)

                elif choice == "3":
                    print("Goodbye!")
                    break

                else:
                    print("Invalid choice, please try again.\n")

        if user_SignIn != None and user_SignIn.side == "Membership":

            while True:
                print("1. Add coach")
                print("2. Remove coach")
                print("7. Add workout")
                print("8. Remove workout")
                print("9. Add activity")
                print("10. Remove activity")
                print("11. Search coach by sport")
                print("12. Search customer activity history")

                choice = input("Enter your choice: ")

                if choice == "1":
                    name = input("Enter coach name: ")
                    age = int(input("Enter coach age: "))
                    email = input("Enter coach email: ")
                    phone_number = input("Enter coach phone number: ")
                    address = input("Enter coach address: ")
                    sport = input("Enter coach sport: ")
                    add_coach(user_SignIn, name, age, email,
                            phone_number, address, sport)

                elif choice == "2":
                    name = input("Enter coach name: ")
                    remove_coach(user_SignIn, name)

                elif choice == "7":
                    name = input("Enter workout name: ")
                    description = input("Enter workout description: ")
                    add_workout(user_SignIn, name, description)

                elif choice == "8":
                    name = input("Enter workout name: ")
                    remove_workout(user_SignIn, name)

                elif choice == "9":
                    customer_name = input("Enter customer name: ")
                    coach_name = input("Enter coach name: ")
                    workout_name = input("Enter workout name: ")
                    workout_date = input("Enter workout date (YYYY-MM-DD): ")
                    start_time = input("Enter start time (HH:MM): ")
                    end_time = input("Enter end time (HH:MM): ")
                    add_activity(user_SignIn, customer_name, coach_name,
                                workout_name, workout_date, start_time, end_time)

                elif choice == "10":
                    customer_name = input("Enter customer name: ")
                    coach_name = input("Enter coach name: ")
                    workout_date = input("Enter workout date (YYYY-MM-DD): ")
                    start_time = input("Enter start time (HH:MM): ")
                    remove_activity(user_SignIn, customer_name,
                                    coach_name, workout_date, start_time)

                elif choice == "11":
                    sport = input("Enter sport: ")
                    search_coach(user_SignIn, sport)

                elif choice == "12":
                    name = input("Enter customer name: ")
                    search_history(user_SignIn, name)

                elif choice == "13":
                    print("Goodbye!")
                    break

                else:
                    print("Invalid choice, please try again.\n")

main()
