accounts = {
    'checking': 1957.00,
    'savings': 36980
}
def add_balance(amount: float, name: str = 'checking') -> float: #returns float; name: str = 'checking' => set's the default value of parameter
    #or name = 'checking')
    #default argument should be AFTER non-default argument
    """Function to update the balance of an account and return the new balance""" #this is doc string
    accounts[name] += amount
    return accounts[name]

add_balance(500.00, 'savings')
add_balance(100.00)
print(accounts['savings'])
print(accounts['checking'])