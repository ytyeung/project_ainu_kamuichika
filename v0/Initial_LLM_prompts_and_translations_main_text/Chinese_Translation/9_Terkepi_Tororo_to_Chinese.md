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
Translate the following text from Japanese to Chinese. The original text is a Japanese translation of a Ainu chant, sung by Ainu god telling his story. 
Use story-telling and poetic tone. Keep the original Japanese meaning accurately. Use modern Chinese. Display in Traditional Chinese.
If a term cannot be translated, keep the original language.

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
青蛙自歌之謠
「托羅羅 漢羅庫 漢羅庫！」

托羅羅 漢羅庫 漢羅庫！
「某日，我於草原間跳躍嬉戲，
忽見一戶人家，遂至門前探望。
但見屋內堆滿寶藏，旁有一高床。
一少年郎於高床之上，埋首雕琢刀鞘。
我心生惡作劇，便坐於門檻之上，
鳴叫：「托羅羅 漢羅庫 漢羅庫！」
那少年聞聲，抬起持刀之手，
望向我，粲然一笑，問道：
「此乃汝之歌謠？汝之喜悅之歌？
吾甚想再聞。」
我欣喜若狂，再次鳴叫：「托羅羅 漢羅庫 漢羅庫！」
少年又道：
「此乃汝之ユーカラ？汝之サケハウ？
吾欲更近聆聽。」
聞此言，我心花怒放，一躍至下座之爐緣，
鳴叫：「托羅羅 漢羅庫 漢羅庫！」
少年仍道：
「此乃汝之ユーカラ？汝之サケハウ？
吾欲更近聆聽。」
聽罷此語，我真乃喜不自勝，遂躍至上座之爐緣角落，
高聲鳴叫：「托羅羅 漢羅庫 漢羅庫！」

突如其來！少年猛然起身，
迅如疾風，抄起巨大之燃燒薪柴，
向我擲來，只覺眼前一黑，
隨後便人事不省。

再次醒來，
卻發現自己身處垃圾堆末端，化作一隻腹部鼓脹之青蛙，
已然死去，而我正坐於其雙耳之間。

仔細一看，原以為只是一介凡人之家，
實乃オキキリムイ，神祇般強大之存在所居之所。
而我竟不知其乃オキキリムイ，
貿然前去惡作劇。

如今我將以如此微不足道、如此糟糕之方式死去，
故告誡未來之青蛙們，切莫再對人類惡作劇。
」

鼓脹之青蛙如是說著，氣絕身亡。
```
