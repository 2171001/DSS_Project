from flask import Flask, request

app = Flask(__name__)

# Define a dictionary to store the status of user accounts
user_status = {}

# Define a function to block a user's account
def block_account(user_id):
    user_status[user_id] = "Blocked"

# Define a function to unblock a user's account
def unblock_account(user_id):
    user_status[user_id] = "Active"

# Define a function to check if a user's account is blocked
def is_account_blocked(user_id):
    return user_status.get(user_id) == "Blocked"

# Define a decorator function to require a user's account to be active
def require_active_account(func):
    def wrapper(*args, **kwargs):
        user_id = request.headers.get("User-Id")
        
        if user_id:
            if is_account_blocked(user_id):
                return "Account blocked"
            else:
                return func(*args, **kwargs)
        else:
            return "User ID required"
    
    return wrapper

# Define a protected resource that requires an active account
@app.route("/protected-resource")
@require_active_account
def protected_resource():
    return "This is a protected resource that requires an active account"

if __name__ == "__main__":
    # Initialize user_status with some example values
    user_status = {"user1": "Active", "user2": "Blocked"}
    app.run()
