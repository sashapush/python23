class User:
    def __init__(self, name, engagement):
        self.name = name
        self.engagement_metrics = engagement
        self.score = 0

    def __repr__(self):
        return f'<User {self.name}>'

def email_engaged_user(user):
    try:
        user.score = perform_calculation(user.engagement_metrics) #defined in init method as well, as good practice
    except KeyError:
        print('Incorrect values provided to our calculation function.')
        #raise #to reraise the exception to show stacktrace of error. Must be inside 'except' block
    else: #if nothing above provides error; ie on success
        if user.score > 500:
            send_engagement_notification(user)

def perform_calculation(metrics):
    return metrics['clicks'] * 5 + metrics['hits'] * 2

def send_engagement_notification(user):
    print(f'Notification sent to {user}.')

# def email_engaged_user(user):
#     try:
#         user.score = perform_calculation(user.engagement_metrics)
#     except KeyError:
#         print('Incorrect values provided to our calculation function.')
#     else: #if exception doesn't occure - this block of code executes
#         if user.score > 500:
#             send_engagement_notification(user)
#my_user = User('Rolf', {'click': 61, 'hits': 100}) #will return error due to Key (click) error name (not clicks, as expected by code)
my_user = User('Rolf', {'clicks': 61, 'hits': 100})
email_engaged_user(my_user)