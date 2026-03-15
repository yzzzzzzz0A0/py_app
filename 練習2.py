class UserProfile:
    def __init__(self, name, level):
        self.name = name
        self.level = level

    def upgrade(self):
        self.level += 1
        print(f"恭喜 {self.name}！你升到了第 {self.level} 級！")

    def show_info(self):
        print(f"{self.name} 目前的等級是 {self.level}")

# ==========================================
# 主程式區
# ==========================================

# 模擬從伺服器抓下來的原始資料 (List 裡裝 Dict)
server_data = [
    {"user_id": "Alice", "lv": 10},
    {"user_id": "Bob", "lv": 5},
    {"user_id": "Charlie", "lv": 99}
]

# 準備一個空清單，用來裝「真實的物件」
active_users = []

# --- 請在下方開始寫你的迴圈邏輯 ---
# 1. 將 server_data 轉換成物件並裝進 active_users
for data in server_data:

    active_users.append(UserProfile(data["user_id"], data["lv"]))

# 2. 讓 active_users 裡的所有物件都秀出自己的資訊
active_users[].show_info()