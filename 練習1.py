class UserProfile:

    def __init__(self,name,level):
        self.name = name
        self.level = level

    def upgrade(self):
        self.level += 1
        print(f"恭喜 {self.name}！你升到了第 {self.level} 級！")

    def show_info(self):
        print(f"{self.name}目前的等級是{self.level}")

player_1 = UserProfile("OOO", 1)
player_2 = UserProfile("PPP", 50)

player_1.show_info()

player_1.upgrade()
player_1.upgrade()

player_1.show_info()
player_2.show_info()

player_2.upgrade()

player_2.show_info()