# JetBot Mega

Jetson nano搭載のメガローバー「JetBot Mega」用のプロジェクトです。  
基本的な使用方法は通常のJetBotと同様ですが、ドライバー等のプログラムがVS-WRC021仕様になっています。  

<img src="https://www.vstone.co.jp/products/wheelrobot/img/jetbot_01.jpg" height="256">

環境構築、動作方法については下記のJetBotのwikiに従ってください。  
[JetBot Wiki](https://github.com/NVIDIA-AI-IOT/jetbot/wiki)  

ただし、使用するOSイメージは、[jetbot_image_v0p3p2.zip](https://drive.google.com/file/d/1GF2D814hkViwluZ5SgNKW56cQu_5Ekt5/view)を使用してください。  
また、下記の２点についてはコマンドに変更が必要です。  
* Software setupのStep 5、項目4について  
 プログラムはJetBot Mega用の物を使用する必要があるため、gitのコマンドを下記のように修正してください。
 ```
 $ git clone https://github.com/vstoneofficial/jetbot-mega.git jetbot
 ```
* Software setupのStep 5、項目5について  
 rsyncコマンドは、下記のようにrオプションを追加して実行してください。
 ```
 $ rsync -r jetbot/notebooks ~/Notebooks  
 ```

なお、このプログラムはメガローバーVer.2.1用になります。  
メガローバーVer.2.0で使用する場合、Arduinoライブラリおよびサンプルスケッチmegarover_commonの改造が必要となります。  
改造する場合はメガローバーVer.2.1用のライブラリ、サンプルスケッチを参考にしてください。  
ただし、具体的な改造方法についてはサポートの対象外とさせて頂いております。何卒ご了承ください。
