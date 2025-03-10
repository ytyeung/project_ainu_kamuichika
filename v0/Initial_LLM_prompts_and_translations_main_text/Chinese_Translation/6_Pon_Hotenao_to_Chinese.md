# LLM-assisted Translation project of Ainu shin'yoshu (アイヌ神謡集) collected by Chiri Yukie 知里幸惠 (1903 - 1922).

## Chinese Translation of

## Pon Horkeukamui yaieyukar, “Hotenao” 小狼の神が自ら歌った謡「ホテナオ」

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

小狼の神が自ら歌った謡
「ホテナオ」

ホテナオ
ある日に退屈なので浜辺へ出て,
遊んでいたら一人の小男が
来ていたから,川下へ下ると
私も川下へ下り,
川上へ来ると私も川上へ行き道をさえぎった.
すると川下へ六回
川上へ六回になった時小男は
持前の癇癪かんしゃくを顔に表して言うことには,
「ピイピイ
この小僧め悪い小僧め,そんな事をするなら
この岬の,昔の名と今の名を
言い解いて見ろ」
私は聞いて笑いながらいうこと
には,
「誰がこの岬の昔の名と
今の名を知らないものか!
昔は,尊いえらい神様や人間が居ったから
この岬を神の岬と
言ったものだが,今は時代が衰えたから
御幣の岬とよんでいるのさ!」
云うと,小男の云うことには,
「ピイトン,ピイトン
この小僧め本当にお前はそういうなら
この川の前の名と今の名を
云って見ろ.」
聞くと,私の云うことには,
「誰がこの川の前の名
今の名を知らないものか!
昔,えらかった時代にはこの川を
流れの早い川と云っていたのだが
今は世が衰えているので流れの遅い川と
云っているのさ.」
云うと小男の云うことには,
「ピイトントン,ピイトントン
本当にお前そんな事を云うなら
お互の素性の解き合いをやろう.」
聞いて私の云うことには,
「誰がお前の素性を知らないものか!
大昔,オキキリムイが山へ行って
狩猟小舎を建てた時榛はしばみの木の炉縁ろぶちを作ったら
その炉縁が火に当ってからからに乾いてしまった.
オキキリムイが片方を踏むと片一方が
上る,それをオキキリムイが怒って
その炉縁を川へ持って下り
捨ててしまったのだ.
それからその炉縁は流れに沿うて流れていって
海へ出で,彼方かなたの海波,此方こなたの海波
に打ちつけられる様を神様たちが御覧になって,
敬うべきえらいオキキリムイの手作りの物がその様に
何の役にもたたず迷い流れて海水と共に腐ってしまうのは
勿体もったいない事だから神様たちから
その炉縁は魚にされて,
炉縁魚と
名づけられたのだ.
ところがその炉縁魚は,自分の素性が
わからないので,人にばけてうろついている.
その炉縁魚がお前なのさ.」
云うと,小男は顔色を
変え変え聞いていたが
「ピイトントン,ピイトントン!
お前は,小さい,狼の子なの
さ.」
云い終ると直ぐに海へパチャンと飛び込んだ.
あと見送ると一つの赤い魚が
尾鰭おびれを動かしてずーっと沖へ
行ってしまった.
と,幼い狼の神様が物語りました.
```

### Output
```
小狼之神親自吟唱的歌謠
「ホテナオ」

ホテナオ
某日，我百般無聊，便來到海邊，
正當我玩耍之際，一個小矮人
走了過來，我往河下游走去，
他也跟著往河下游走，
我往河上游去，他也往河上游走，擋住了我的去路。
如此在河下游來回六次，
河上游來回六次後，小矮人
面露他那與生俱來的急躁，說道：
「匹伊匹伊
你這小鬼，壞小鬼，你要是再這樣，
就說說看這海岬，過去和現在的名字！」
我聽了，笑著回答說：
「誰會不知道這海岬過去和
現在的名字呢！
從前，因為有尊貴偉大的神明和人類居住於此，
所以這海岬被稱為神之岬，
但如今時代衰退，
便被稱作御幣之岬！」
聽我說完，小矮人說道：
「匹伊頓，匹伊頓
你這小鬼，你若真這麼厲害，
就說說看這條河，過去和現在的名字。」
我聽了，回答說：
「誰會不知道這條河過去和
現在的名字呢！
從前，在那個偉大的時代，這條河被稱為
水流湍急之河，
但如今世道衰敗，便被稱作水流緩慢之河。」
聽我說完，小矮人說道：
「匹伊頓頓，匹伊頓頓
你若真這麼厲害，
不如我們來互相揭露彼此的底細。」
我聽了，回答說：
「誰會不知道你的底細呢！
很久以前，オキキリムイ去山裡
建造狩獵小屋時，用榛木做了爐緣，
那爐緣被火烤得乾燥。
オキキリムイ一踩爐緣的一端，另一端
就會翹起來，オキキリムイ對此感到惱火，
便把那爐緣拿到河邊
丟棄了。
之後，那爐緣便順著河流漂流，
流向大海，神明們看見它被遠方的海浪，近方的海浪
拍打的樣子，
心想，值得尊敬的偉大オキキリムイ親手製作的東西，竟然如此
毫無用處地迷失漂流，與海水一同腐爛，
實在太可惜了，於是神明們便
將那爐緣變成了魚，
並命名為爐緣魚。
然而，那爐緣魚，因為不知道自己的身世，
便化為人形四處遊蕩。
你就是那爐緣魚。」
聽我說完，小矮人面色
數變，
「匹伊頓頓，匹伊頓頓！
你，是隻小小的，狼之子啊。」
話一說完，立刻撲通一聲跳入海中。
我目送著他，只見一條紅色的魚
擺動著尾鰭，一直往遠方游去。
這就是，年幼的狼神所講述的故事。
```
