import finlab
from finlab import data
import os

# 1. 取得秘密金鑰並登入
token = os.getenv('FINLAB_TOKEN')
finlab.login(token)

# 2. 抓取資料並印出來測試
try:
    print("🚀 正在連線 FinLab 抓取集保分散資料...")
    df = data.get('inventory')
    
    print("\n✅ 抓取成功！資料預覽：")
    # 顯示最後 5 筆，讓我們看看最新的日期
    print(df.tail())
    
    print("\n📊 欄位名稱：", df.columns.tolist())
except Exception as e:
    print(f"❌ 發生錯誤：{e}")
