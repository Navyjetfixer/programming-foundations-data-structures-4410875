user_preferences = {
    "timezone": "GMT",
    "language": "English",
    "notifications": None,
    "currency": "USD",
    "theme": None
}


def update_preferences(user_pref):
    new_user_prefs = {}
    for key, value in user_pref.items():
        if value != None:
            new_user_prefs[key] = value
           
   
    return new_user_prefs


print(update_preferences(user_preferences))
