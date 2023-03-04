import stripe

# Set your Stripe API key
stripe.api_key = "sk_test_yourkeyhere"

# Define a function to block a transaction based on the transaction amount
def block_transaction_by_amount(amount):
    if amount > 1000: # Change the threshold amount to your desired value
        return True
    else:
        return False

# Define a function to block a transaction based on the transaction location
def block_transaction_by_location(location):
    if location == "high-risk-country": # Change the location to your desired value
        return True
    else:
        return False

# Define a function to block a transaction based on both amount and location
def block_transaction(amount, location):
    if block_transaction_by_amount(amount) or block_transaction_by_location(location):
        return True
    else:
        return False

# Process a transaction and block it if necessary
def process_transaction(user_id, amount, location):
    if block_transaction(amount, location):
        return "Transaction blocked"
    else:
        # Process the transaction using the Stripe API
        try:
            charge = stripe.Charge.create(
                amount=amount,
                currency="usd",
                customer=user_id
            )
            return "Transaction successful"
        except stripe.error.CardError as e:
            # The card has been declined
            return "Card declined"
