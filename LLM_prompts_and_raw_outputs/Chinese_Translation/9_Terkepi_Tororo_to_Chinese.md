# LLM-assisted Translation project of Ainu shin'yoshu (アイヌ神謡集) collected by Chiri Yukie 知里幸惠 (1903 - 1922).

## Chinese Translation of

## Terkepi yaieyukar, “Tororo hanrok hanrok!” 蛙が自らを歌った謡「トーロロ ハンロク ハンロク!」

### Model
gemini-2.0-flash-001

### Setting
```
generate_content_config = types.GenerateContentConfig(
    temperature = 0,
    top_p = 0,
    max_output_tokens = 8192,
    response_modalities = ["TEXT"],
    safety_settings = [types.SafetySetting(
      category="HARM_CATEGORY_HATE_SPEECH",
      threshold="OFF"
    ),types.SafetySetting(
      category="HARM_CATEGORY_DANGEROUS_CONTENT",
      threshold="OFF"
    ),types.SafetySetting(
      category="HARM_CATEGORY_SEXUALLY_EXPLICIT",
      threshold="OFF"
    ),types.SafetySetting(
      category="HARM_CATEGORY_HARASSMENT",
      threshold="OFF"
    )],
    system_instruction=[types.Part.from_text(text=si_text1)],
  )
```

### System prompt
```
You are a professional translator. You know Japanese, English and Chinese. You can translate Japanese into either Chinese or English.
```

### Prompt
```
Translate the following text from Japanese to Chinese. The original text is a poem. Try to make the translation poetic but keep the original meanings. Display in Traditional Chinese.

蛙が自らを歌った謡
「トーロロ ハンロク ハンロク!」

トーロロ ハンロク ハンロク!
「ある日に,草原を飛び廻って
遊んでいるうちに見ると,
一軒の家があるので戸口へ行って
見ると,家の内に宝の積んである側に
高床がある.その高床の上に
一人の若者が鞘を刻んでうつむいて
いたので,私は悪戯をしかけようと思って敷居の上に
坐って,「トーロロ ハンロク ハンロク!」と
鳴いた,ところが,彼の若者は刀持つ手を上げ
私を見ると,ニッコリ笑って,
「それはお前の謡かえ? お前の喜びの歌かえ?
もっと聞きたいね.」というので
私はよろこんで「トーロロ ハンロク ハンロク!」と
鳴くと,彼の若者のいう事には,
「それはお前のユーカラかえ? サケハウかえ?
もっと近くで聞きたいね.」
私はそれをきいて嬉しく思い下座の方の
炉縁の上へピョンと飛んで
「トーロロ ハンロク ハンロク!」と鳴くと
彼の若者のいうことには,
「それはお前のユーカラかえ? サケハウかえ?
もっと近くで聞きたいね.」それを聞くと私は,
本当に嬉しくなって,上座の方の炉縁の
隅のところへピョンと飛んで
「トーロロ ハンロク ハンロク!」と鳴いたら
突然!彼の若者がパッと起ち
上ったかと思うと,大きな薪の燃えさしを
取り上げて私の上へ投げつけた音は
体の前がふさがったように思われて,それっきり
どうなったかわからなくなってしまった.
ふと気がついて見たら
芥捨あくすて場の末に,一つの腹のふくれた蛙が
死んでいて,その耳と耳との間に私はすわっていた.
よく見ると,ただの人間の家
だと思ったのは,オキキリムイ,神の様に
強い方の家なのであった,そして
オキキリムイだという事も知らずに
私が悪戯をしたのであった.
私はもう今この様につまらない死方,悪い死方
をするのだから,これからの
蛙たちよ,決して,人間たちに悪戯をするのではないよ.
と,ふくれた蛙が云いながら死んでしまった.
```

### Output
```
好的，這是一份將日文詩歌翻譯成繁體中文的譯文，我會盡力保持詩意和原文的含義：

**蛙自歌謠**

「托洛洛，漢洛克，漢洛克！」

托洛洛，漢洛克，漢洛克！
某日，躍於草原之上，
嬉戲之間，忽見一戶人家。
趨步至門前，探首望之，
屋內珍寶堆疊，高臺聳立。
臺上一少年，俯首刻鞘。
吾欲戲之，踞於門檻之上，
高唱：「托洛洛，漢洛克，漢洛克！」
少年聞聲，抬刀之手微頓，
望吾，粲然一笑，問曰：
「此乃汝之歌謠？汝之喜悅之歌？
願聞其詳。」
吾欣喜，復唱：「托洛洛，漢洛克，漢洛克！」
少年又曰：
「此乃汝之敘事詩？汝之祝禱？
願近而聆聽。」
吾聞之，心喜，躍至下座爐邊，
再唱：「托洛洛，漢洛克，漢洛克！」
少年仍曰：
「此乃汝之敘事詩？汝之祝禱？
願更近而聆聽。」
吾聞之，益喜，躍至上座爐邊一隅，
高歌：「托洛洛，漢洛克，漢洛克！」
忽而！少年驟起，
似飛身而上，取巨木燃燒之殘骸，
擲向吾身，如泰山壓頂，
頓失知覺，不知所終。
醒來之時，
身處垃圾堆之末，一腹脹之蛙，
氣絕身亡，吾立於其耳間。
細觀之，原以為尋常人家，
實乃神祇奧奇奇里穆伊，
神力無邊之居所。
吾竟不知其身份，冒然戲弄。
如今落得如此卑微之死，惡劣之死，
告誡後世之蛙，切記，
莫要戲弄人類。
腹脹之蛙如是說罷，溘然長逝。

```
### Another prompt for matched meaning

```
Translate the following text from Japanese to Chinese. Keep the original meanings. Display in Traditional Chinese.
```

### Output of this prompt

```
以下是將日文文本翻譯成繁體中文的結果：

青蛙自歌的謠曲
「托羅羅 漢羅庫 漢羅庫！」

托羅羅 漢羅庫 漢羅庫！
「有一天，在草原上飛來飛去
玩耍的時候，看到
一間房子，就走到門口
一看，屋內堆滿了寶物，旁邊
有個高台。在那高台上
有個年輕人正在刻刀鞘，低著頭
我想要惡作劇，就坐在門檻上
鳴叫「托羅羅 漢羅庫 漢羅庫！」
沒想到，那個年輕人舉起拿刀的手
看著我，微微一笑，
「那是你的歌謠嗎？是你的喜悅之歌嗎？
還想多聽聽呢。」於是我
高興地鳴叫「托羅羅 漢羅庫 漢羅庫！」
那個年輕人說道，
「那是你的尤喀拉嗎？薩凱豪嗎？
還想更靠近地聽聽呢。」
我聽了很高興，就跳到下座的
爐緣上
鳴叫「托羅羅 漢羅庫 漢羅庫！」
那個年輕人說道，
「那是你的尤喀拉嗎？薩凱豪嗎？
還想更靠近地聽聽呢。」聽到這話，我
真的很高興，就跳到上座的爐緣的
角落
鳴叫「托羅羅 漢羅庫 漢羅庫！」
突然！那個年輕人猛然站起
好像跳了起來，拿起一根巨大的燃燒的木柴
朝我扔了過來，那聲音
好像身體前面被堵住了一樣，之後
發生了什麼就不知道了。
突然回過神來，發現
在垃圾堆的末端，有一隻肚子鼓脹的青蛙
死了，我正坐在牠的兩耳之間。
仔細一看，我以為
只是一般的人家，其實是奧基基里穆伊，像神一樣
強大的人的家，而且
我竟然不知道那是奧基基里穆伊，就
惡作劇了。
我現在就要這樣無聊地死去，可悲地死去
所以，從今以後的
青蛙們啊，千萬不要對人類惡作劇啊。
」
肚子鼓脹的青蛙這樣說著，就死去了。

```