class StarCookie:
    milk = 0.5  #class attribute
    def __init__(self, weight, colour):
        print("Cookie is ready!")
        self.colour = colour
        self.weight = weight

star_cookie1 = StarCookie(10,'red')
print(star_cookie1)
print(star_cookie1.weight, star_cookie1.colour,star_cookie1.milk)
star_cookie2 = StarCookie(15,'blue')
print(star_cookie2)
print(star_cookie2.weight, star_cookie2.colour, star_cookie2.milk)

print(star_cookie1.__dict__)
print(star_cookie2.__dict__)
print(StarCookie.__dict__)

class Youtube:
    def __init__(self, username, subscribers=0, subscriptions = 0):
        self.username = username
        self.subscribers = subscribers
        self.subscriptions = subscriptions

    def subscribe(self, user):
        user.subscribers += 1
        self.subscriptions += 1

user1 = Youtube("Rana", 5, 1)
user2 = Youtube("Sam")
user1.subscribe(user2)
print(user1.subscribers,user1.username, user1.subscriptions)
print(user2.subscribers,user2.username)
