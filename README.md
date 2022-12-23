<<<<<<< HEAD
#  阿金不會忘記

## 動機
日常生活中有時會發生一些很令人生氣的事情要抱怨時想不起來，或是受到別人的幫忙怕忘記有點不好意思，所以就打算設計一個可以針對事件類型、對象進行分類的機器人將發生的事情記錄下來，在未來要想要回憶時可以想到更多細節。

## 加入帳號
掃描下方QR code即可加入

![](https://upload.cc/i1/2022/12/23/6YEhcW.jpg)

## 環境
- ubuntu 22.04
- python 3.6.15
- ngrok
- pipenv

## 環境設定
1. install 所需套件及開啟虛擬環境

```shell
$ pipenv install --three
$ pipenv install
$ pipenv shell
```
2. 安裝`graphviz`

```shell
$ sudo apt-get install graphviz graphviz-dev
```

3. 從`Line Developers`找到`LINE_CHANNEL_SECRET`及`INE_CHANNEL_ACCESS_TOKEN`，並填入至app.py及utils.py中

- Line
    - LINE_CHANNEL_SECRET
    - LINE_CHANNEL_ACCESS_TOKEN

- LINE_CHANNEL_SECRET:
![](https://upload.cc/i1/2022/12/23/cPMQvk.jpg)
- LINE_CHANNEL_ACCESS_TOKEN
![](https://upload.cc/i1/2022/12/23/YXR50w.jpg)

4. 利用 `ngrok` 產生https網址
```shell
$ ngrok http 8000
```

將ngrok中`Forwarding`內的網址複製至Line developers(須加上`/webhook`))
- Line Developers
![](https://upload.cc/i1/2022/12/23/jQbZm1.jpg)

5. 執行程式
```shell
$ python app.py
```

## 使用說明
- 開啟菜單：
    - 初次使用機器人時，可輸入menu開啟菜單（輸入任何文字軍會開啟菜單）
    - 當輸入不符合格式的文字時會跳回到菜單
	- 開啟菜單後可依據需求選擇新增、刪除、修改、及查看
- 錯誤格式：
	- 在刪除或修改時，輸入未紀錄的名字
	- 選擇事件時，輸入非阿拉伯數字或不在範圍內的數字
- 重新輸入：
	- 當因輸入錯誤格式回到menu時，可透過輸入`"返回 <正確名字/數字>"`來重新輸入名字或數字

## 使用示範
- 呼叫菜單：
	- ![](https://upload.cc/i1/2022/12/23/WM8qSz.jpg)

- 新增：
	- 新增壞事（點擊記仇- 再添一筆）: ![](https://upload.cc/i1/2022/12/23/9UlTxM.jpg)
	- 新增好事（點擊記恩- 再添一筆）: ![](https://upload.cc/i1/2022/12/23/CsgAOG.jpg)

- 查看：
	- 查看壞事（點擊翻小本本- 有仇報仇）:![](https://upload.cc/i1/2022/12/23/Jum7MC.jpg) 
	- 查看特定對象 （點擊翻小本本 接著輸入名字）：![](https://upload.cc/i1/2022/12/23/TUM3tS.jpg)

- 刪除：
	- 刪除特定事件 （點擊記仇/記功 接著輸入名字、數字）：![](https://upload.cc/i1/2022/12/23/38iPYU.jpg)

- 修改：
	- 修改特定事件 （點擊記仇/記功 接著輸入名字、數字 最後輸入要修改的內容）：![](https://upload.cc/i1/2022/12/23/tIE8eQ.jpg)


- 利用返回重新輸入：
	- 重新輸入數字
	![](https://upload.cc/i1/2022/12/23/92lqbA.jpg)
	![](https://upload.cc/i1/2022/12/23/34LWPF.jpg)
	- 重新輸入文字
	![](https://upload.cc/i1/2022/12/23/GTor07.jpg)
	![](https://upload.cc/i1/2022/12/23/u7pknm.jpg)


## FSM
![](https://upload.cc/i1/2022/12/23/DUGfwb.png)
### state說明
- user: 輸入menu開始呼叫菜單（輸入任何文字均會呼叫菜單）
- menu: 顯示菜單，提供使用者選擇操作類型及事件類型
- name: 輸入所要新增、刪除、查看、或修改的對象名字
- list: 顯示所指定名字有哪些事件
- Create_things: 紀錄使用者輸入的名字、讓使用者輸入所要新增事件的內容
- Update_choose: 紀錄使用者指定的事件、讓使用者輸入所要修改事件的內容
- Delete: 刪除指定的事件
- Update: 將指定事件的內容修改為輸入的內容
- Create: 將使用者、事件類型、名字、事件內容紀錄下來
- Read: 顯示所有與"name"時輸入的名字相同的事件
- things: 顯示所有與選擇事件類型相同的事件


## 參考圖源
![大頭照](https://www.youtube.com/watch?v=RdsWevZ3PpI)

![生氣狗狗](https://www.freepik.com/free-photo/angry-golden-retriever-dog_1254358.htm)

![開心狗狗](https://www.newsweek.com/golden-retriever-hectic-morning-routine-wakes-owners-viral-1741182)

![狗狗](https://www.doggiejogs.com/about-us)
=======
# linebot
>>>>>>> 12e52fdad6a8f55fad6c9a128b21bdd41a683fef
