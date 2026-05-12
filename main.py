import finlab
from finlab import data
import os
import pandas as pd

def run_crawler():
    # 1. 登入 (從 GitHub Secrets 讀取 Token)
    token = os.getenv('FINLAB_TOKEN')
    if not token:
        print("❌ 錯誤: 找不到 FINLAB_TOKEN，請檢查 GitHub Secrets 設定。")
        return
    
    finlab.login(token)

    try:
        print("🚀 正在抓取集保股權分散資料...")
        # 抓取資料
        df = data.get('inventory')

        # 2. 定義分級對照表 (根據你的截圖內容)
        level_map = {
            1: '1-999', 2: '1,000-5,000', 3: '5,001-10,000', 4: '10,001-15,000',
            5: '15,001-20,000', 6: '20,001-30,000', 7: '30,001-40,000', 8: '40,001-50,000',
            9: '50,001-100,000', 10: '100,001-200,000', 11: '200,001-400,000',
            12: '400,001-600,000', 13: '600,001-800,000', 14: '800,001-1,000,000',
            15: '1,000,001以上', 17: '合計'
        }

        # 3. 資料整理
        # 將 '持股分級' 數字轉成文字說明
        if '持股分級' in df.columns:
            df['分級說明'] = df['持股分級'].map(level_map)

        # 找出最新的一天 (免費用戶目前可能是 2018)
        latest_date = df['date'].max()
        print(f"📅 偵測到可抓取的最新日期為: {latest_date}")

        # 4. 儲存檔案
        os.makedirs('data', exist_ok=True)
        file_path = 'data/inventory_latest.csv'
        
        # 只存最近一期的資料，避免檔案太大
        latest_df = df[df['date'] == latest_date]
        latest_df.to_csv(file_path, index=False, encoding='utf-8-sig')
        
        print(f"✅ 成功存檔至: {file_path}")
        print(latest_df.head())

    except Exception as e:
        print(f"❌ 執行失敗: {e}")

if __name__ == "__main__":
    run_crawler()
