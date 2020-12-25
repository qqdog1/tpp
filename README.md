# tpp
trading platform python practice  

----------
### 啟動前設定
於./config資料夾內編輯binance.config  
在裡面填上api key及secret(config為json格式)  

### 啟動方式  
main class 為 trading_platform.py  
執行後  
輸入start strategy name可開始    
輸入stop strategy name可停止  
輸入exit離開程式   

目前支援的strategy name 如下  
https://github.com/qqdog1/tpp/blob/main/strategy/supported_strategy.py

log位於root  
名稱為log.txt


### 實作新交易所  
exchange_connector  
詳細內容待補  

### 實作新策略  
strategy  
詳細內容待補  
