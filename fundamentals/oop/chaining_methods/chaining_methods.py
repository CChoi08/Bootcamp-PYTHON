#User class setup

class User:
    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age

        #default attributes

        self.is_rewards_member = False
        self.gold_card_points = 0

    #displays user's info on separate lines

    def display_info(self):
        print(self.first_name, self.last_name, self.email, self.age)
        return self

    #changing member status and points

    def enroll(self):
        if self.is_rewards_member == False and self.gold_card_points == 0:
            self.is_rewards_member = True
            self.gold_card_points = 200
            return self
        else:
            print('You are already a member')

    #spend points method

    def spend_points(self, amount):
        if amount > self.gold_card_points:
            return 'Sorry not enough points'
        else:
            self.gold_card_points = self.gold_card_points - amount
            return self.gold_card_points


user1 = User('Chris', 'Choi', 'email', 27)
user2 = User('Preston', 'Choi', 'email', 24)
user3 = User('Morgan', 'Choi', 'email', 21)

# print(User.display_info(user1))

# chaining methods

print(user1.enroll().display_info().spend_points(50))
print(user2.enroll().display_info().spend_points(80))
print(user3.display_info().spend_points(40))


# User.enroll(user2)
# User.spend_points(user2, 80)

# print(User.display_info(user1))
# print(user1.is_rewards_member)
# print(user1.gold_card_points)

# print(User.display_info(user2))
# print(user2.gold_card_points)

# print(User.display_info(user3))

# print(User.membership(user3))
# User.spend_points(user3, 40)