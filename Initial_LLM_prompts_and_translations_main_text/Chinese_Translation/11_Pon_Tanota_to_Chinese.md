# LLM-assisted Translation project of Ainu shin'yoshu (アイヌ神謡集) collected by Chiri Yukie 知里幸惠 (1903 - 1922).

## Chinese Translation of

## Pon Okikirmui yaieyukar, “Tanota hurehure” 小オキキリムイが自ら歌った謡「この砂赤い赤い」

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

小オキキリムイが自ら歌った謡
「この砂赤い赤い」

〔この砂赤い赤い〕
ある日に流れをさかのぼって遊びに
出かけたら,悪魔の子に出会った.
いつでも悪魔の子は様子が美しい
顔が美しい.黒い衣を着けて
胡桃くるみの小弓に胡桃の小矢を持っていて
私を見ると,ニコニコして
いうことには,
「小オキキリムイ,遊ぼう.
さあこれから,魚の根を絶やして見せよう.」
と言って,胡桃の小弓に胡桃の小矢を
番つがえ水源の方へ矢を射放すと,
水源から胡桃の水,濁った水が
流れ出し,鮭どもが上って来ると
胡桃の水が厭なので泣きながら
引き返して流れて行く.悪魔の子は
それをニコニコしている.
私はそれを見て腹が立ったので
私の持っていた,銀の小弓に銀の小矢を
番え水源へ矢を射はなすと
水源から銀の水,清い水が
流れ出し,泣きながら流れて行った
鮭どもは清い水に元気を恢復し
大笑いをして遊びさわいで
パチャパチャ川を上って行った.
すると,悪魔の子は,持前の癇癪かんしゃくを
顔に表して,
「本当にお前そんな事をするなら,鹿の根を
絶やして見せよう.」と云って,
胡桃の小弓に胡桃の小矢を番え
大空を射ると,山の木原から
胡桃の風,つむじ風が吹いて来て
山の木原から,牡鹿の群は別に
牝鹿の群はまた別に,風に吹き上げられ
ずーっと天空へきれいにならんで上って行く.
悪魔の子はニコニコしている.
それを見た私はかっと癪にさわったので
銀の小弓に銀の小矢を
番えて,鹿の群のあとへ矢を射放すと,
天上から,銀の風,清い風が
吹き降り,牡鹿の群は
別に,牝鹿の群はまた別に,
山の木原の上へ吹き下された.
すると,悪魔の子は
持前の癇癪を顔に現し,
「生意気な,本当に
お前そんな事をするなら,力競べをやろう.」
と云いながら上衣を脱いだ.
私も薄衣一枚になって
組み付いた.彼も私に組み付いた.それからは
互に下にしたり上にしあったり相撲をとったが,
大へんに悪魔の子が力のある事には
驚いた.けれども,とうとう,ある時間に,
私は腰の力,からだの力を
みんな出して,悪魔の子を
肩の上まで引っ担ぎ,
山の岩の上へ彼を打ちつけた音が
がんと響いた.殺してしまって地獄へ
踏み落したあとはしんと静まり返った.
それが済んで,私は流れに沿って帰って来ると,
川の中では鮭どもが笑う声
遊ぶ声がかまびすしくのぼって来るのが
パチャパチャきこえる.山の木原では,
牡鹿ども,牝鹿どもが笑う声
遊ぶ声がそこら一ぱいになって
そこにここに物を
食べている.私はそれを見て
安心をし,私の家へ
帰って来た.
と,小さいオキキリムイが物語った.
```

### Output
```
小オキキリムイ親自吟唱的歌謠
「這砂，紅豔豔的」

〔這砂，紅豔豔的〕
某日，我溯流而上，前去遊玩，
遇見了惡魔之子。
惡魔之子總是那般俊美，
容貌秀麗。身著黑色衣裳，
手持胡桃木的小弓，胡桃木的小箭。
他看見我，笑嘻嘻地說：
「小オキキリムイ，來玩吧！
我這就讓你看看，如何斷絕魚的生路。」
說著，他將胡桃木的小弓搭上胡桃木的小箭，
朝水源方向射去。
水源湧出胡桃木色的水，混濁不堪，
鮭魚們溯游而上，
卻因厭惡胡桃木水，哭泣著
退回下游。惡魔之子
見此情景，只是得意地笑。
我見狀，怒火中燒，
便拿出我的銀製小弓，搭上銀製小箭，
朝水源射去。
水源湧出銀色的水，清澈甘甜，
哭泣著離去的鮭魚們
在清澈的水中恢復了活力，
歡笑著，嬉鬧著，
啪嚓啪嚓地逆流而上。
惡魔之子頓時
面露他那與生俱來的怒容，
「你若真要如此，我就讓你看看，如何斷絕鹿的生路！」
說著，他將胡桃木的小弓搭上胡桃木的小箭，
射向天空，
山林的樹木間，颳起了
胡桃木之風，龍捲風。
從山林的樹木間，雄鹿群各自一方，
雌鹿群又在另一方，被風吹向天空，
整整齊齊地排列著，升向天際。
惡魔之子見此，得意地笑著。
我見狀，怒不可遏，
便拿起銀製小弓，搭上銀製小箭，
朝著鹿群離去的方向射去。
從天上，吹落下銀色的風，清新的風，
雄鹿群各自一方，
雌鹿群又在另一方，
被吹回山林的樹木間。
惡魔之子頓時
面露他那與生俱來的怒容，
「狂妄之徒，你若
真要如此，我們就來比試力氣！」
說著，他脫下了上衣。
我也只剩一件薄衣，
與他扭打在一起。他也緊緊抱住我。
從那以後，我們互相壓制，互相角力，
但惡魔之子的力氣之大，
實在令我驚訝。然而，終於，在某一刻，
我使出腰部的力量，全身的力量，
將惡魔之子
扛到肩上，
將他狠狠摔在山岩上，
發出轟然巨響。殺死了他，將他踢入地獄之後，
四周一片寂靜。
事情結束後，我沿著河流返回，
只聽見河中鮭魚們的歡笑聲，
嬉戲聲，熱鬧地傳來，
啪嚓啪嚓地響著。山林的樹木間，
雄鹿們，雌鹿們的歡笑聲，
嬉戲聲，充滿四處，
牠們在那裡，在這裡，
吃著東西。我見此情景，
感到安心，便回到
我的家。
小オキキリムイ如此講述著。
```
