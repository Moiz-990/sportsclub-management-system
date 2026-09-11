
# Sports Club Management System - Version 1.0
# Features: member registration and membership details

def register_member(member_id, name, sport):
    print("Member", name, "registered for", sport)

def show_membership(member_id, name, sport):
    print("Member ID:", member_id)
    print("Name:", name)
    print("Sport:", sport)
 
def calculate_fee(months, monthly_fee=500):
    fee = months * monthly_fee
    print("Membership Fee = Rs.", fee)
    return fee
sports_schedule = {
    "Football": "Monday and Wednesday - 5 PM",
    "Cricket": "Tuesday and Thursday - 6 PM",
    "Badminton": "Friday and Saturday - 4 PM"
}
