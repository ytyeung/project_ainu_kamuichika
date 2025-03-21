# LLM-assisted Translation project of Ainu shin'yoshu (アイヌ神謡集) collected by Chiri Yukie 知里幸惠 (1903 - 1922).

## Chinese Translation of

## Chironnup yaieyukar, “Haikunterke Haikoshitemturi” 狐が自ら歌った謡「ハイクンテレケ ハイコシテムトリ」

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

狐が自ら歌った謡
「ハイクンテレケ ハイコシテムトリ」

ハイクンテレケ ハイコシテムトリ
国の岬,神の岬の上に
私は坐して居りました.
ある日に外へ出て見ますと
海は凪なぎてひろびろとしていて,海の上に
オキキリムイとシュプンラムカとサマユンクルが
海猟に三人乗りで出かけています,それを見た私は
私の持ってる悪い心がむらむらと出て来ました.
この岬,国の岬,神の岬
の上をずーっと上へずーっと下へ
軽い足取りで腰やわらかにかけ出しました.
重い調子で木片をポキリポキリと折る様にパーウ,パウと叫び
この川の水源をにらみにらみ暴風の魔を
呼びました.すると,それにつれてこの川の
水源から烈しい風,つむじ風が
吹き出して海にはいると直ぐに
この海は,上の海が下になり
下の海が上になりました.オキキリムイたち
の漁舟は沖の人の海と,陸の人の海との
出会ったところ(海の中程)に,非常な急変に会って波の間を
クルリと廻りました.大きな浪が山の様に
舟の上へかぶさり寄ります.すると,
オキキリムイ,サマユンクル,シュプンラムカは
声をふるって,舟を漕ぎました.
この小さい舟は落葉の飛ぶ様に吹き飛ばされ
今にもくつがえりそうになるけれども
感心にも人間たちは力強くて
この小舟は風の中に
波の上をすべります.
それを見ると私の持っている悪い心がむらむらと出て来ました.
軽い足取りで腰やわらかにかけまわり,
重い調子で木片がポキリポキリと折れる様にパウ,パウと叫び
暴風の魔を声援するのみに精を出しました.
そうしてる中に,やっと,サマユンクルが
手の上から,手の下から血が流れて
疲れてたおれました.
そのさまを見て私はひそかに笑いを浮べました.
それからまた,精を出して
軽い足取りで腰やわらかにかけまわり
重い調子で木片をポキリポキリと折る様に叫び
暴風の魔を声援しました.
オキキリムイとシュプンラムカと二人で
励まし合いながら勇ましく舟を漕いで
居りましたが,と,ある時シュプンラムカは
手の上から手の下から血が流れて
疲れてたおれてしまいました,それを見て
ひそかに私は笑いました.
それからまた軽い足取りで腰やわらかに
飛びまわり重い調子でかたい木片を
ポキリポキリと折る様に叫び精を出しました.
けれども,オキキリムイは疲れた様子は少しも無い.
一枚の薄物を体にまとい,
舟を漕いでいます,そのうちに
手の下でその持っていた楫、が折れてしまいました.
すると,疲れ死んだサマユンクルに
躍りかかりその持っている楫、をもぎとってたった一人で
舟を漕ぎました.
私はそれを見ると,持前の悪い心がむらむらと出て来ました.
重い調子でかたい木片をポキリポキリと折る様に叫び
軽い足取りで腰やわらかにかけまわり
精を出して暴風の魔に声援しました.
そうしてるうちにサマユンクルの舵も
折れてしまいました.オキキリムイはシュプンラムカに
躍りかかりその楫をとって
勇ましく舟を漕ぎました.
けれども彼の楫も波に折られてしまいました.
そこで,オキキリムイは舟の中に
立ちつくして,烈しい風のうちに
まさか人間の彼が私を見つけようとは
思わなかったに,国の岬,神の岬の
上の,私の眼の央を見つめました.
今までやさしかった顔に怒りの色を
あらわして,鞄をいじっていたが
中から出したものを見ると,蓬よもぎの小弓と
蓬の小矢を取り出しました.
それを見てひそかに私は笑いました.
「人間なぞ何をしたって,恐い事があるものか,
あんな蓬の小矢は何に使うものだろう.」
と思ってこの岬
国の岬,神の岬の上を
ずーっと上へずーっと下へ軽い足取りで
腰やわらかにかけまわり,重い調子で
かたい木片をポキリポキリと折る様にパウ,パウと叫び
暴風の魔をほめたたえました.
その中にオキキリムイの射放した矢が飛んで来ましたが
ちょうど私の襟首えりくびのところへ突きささりました.
それっきりあとどうなったか解らなくなってしまいました.
ふと気がついて見ると
大そう好いお天気で,海の上は
広々として,オキキリムイの漁舟もなにもありません.
どうした事か私の頭のさきから
足のさきまで雁皮が燃え縮む様に痛みます.
まさか人間の射た小さな矢がこんなに私を苦しめ
ようとは思わなかったのに,それから手足をもがき苦しみ
この岬,国の岬,神の岬
の上を,ずーっと上へ,ずーっと下へ泣き叫びながら
もがき苦しみ,昼でも夜でも生きたり
死んだり,している中に,どうしたか
わからなくなりました.
ふと気がついて見ると,
大きな黒狐の耳と耳との間に私は居りました.
二日ほどたった時,オキキリムイが神様の様な様子で
やって来て,ニコニコ笑って言うことには,
「まあ見ばのよい事,国の岬,神の岬
の上を見守る黒狐の神様は,
善い心,神の心を持っていたから
死にざまの見ばのよい死方をしたのですね.」
言いながら私の頭を取って,
自分の家へ持って行き私の上顎の骨を
自分の便所のどだいとし,私の下顎を
その妻の便所の礎として,
私のからだはそのまま土と共に腐ってしまいました.
それから夜でも昼でも
悪い臭気に苦しんでいる中に私はつまらない死方,悪い
死方をしました.
ただの身分の軽い神でもなかったのですが
大変な悪い心を私は持っていた為なんにも
ならない,悪い死方を私はしたのですから
これからの狐たちよ,決して
悪い心を持ちなさるな.

と狐の神様が物語りました.
```

### Output
```
狐狸親自吟唱的歌謠
「ハイクンテレケ ハイコシテムトリ」

ハイクンテレケ ハイコシテムトリ
在國之岬，神之岬之上，
我曾端坐於此。
某日，我走出戶外，
只見海面風平浪靜，遼闊無垠，海面上，
オキキリムイ、シュプンラムカ和サマユンクル
三人乘船出海狩獵，見此情景，
我內心邪念頓生。
在這岬角，國之岬，神之岬，
之上，我輕盈地，腰肢柔軟地奔走。
以沉重的語調，如折斷木片般，啪嗚，啪嗚地叫喊，
怒視著這條河流的源頭，召喚暴風的魔力。
隨之而來，從這條河的
源頭湧出強烈的風，龍捲風，
一進入海面，立刻
海面翻騰，上下顛倒。オキキリムイ他們
的漁船在近海之人和遠海之人的
交匯之處（海的中央），遭遇突變，在波浪間
旋轉。巨大的浪濤如山一般
覆蓋船隻。於是，
オキキリムイ、サマユンクル、シュプンラムカ
奮力呼喊，划動船槳。
這艘小船如落葉般被吹飛，
眼看就要傾覆，
令人欽佩的是，人們充滿力量，
這艘小船在風中，
在波浪上滑行。
看到這些，我內心的邪念再次湧現。
我輕盈地，腰肢柔軟地奔走，
以沉重的語調，如折斷木片般，啪嗚，啪嗚地叫喊，
竭盡全力聲援暴風的魔力。
在這樣做的過程中，終於，サマユンクル
的手上，手下，鮮血直流，
疲憊地倒下了。
看到這情景，我暗自竊笑。
然後，我又竭盡全力，
輕盈地，腰肢柔軟地奔走，
以沉重的語調，如折斷木片般叫喊，
聲援暴風的魔力。
オキキリムイ和シュプンラムカ兩人
互相鼓勵，勇敢地划著船，
突然，某個時候，シュプンラムカ的
手上，手下，鮮血直流，
疲憊地倒下了，看到這些，
我暗自竊笑。
然後，我又輕盈地，腰肢柔軟地
跳躍奔走，以沉重的語調，如折斷堅硬的木片
般叫喊，竭盡全力。
但是，オキキリムイ卻沒有絲毫疲憊的樣子。
他身上披著一件薄衣，
划著船，不久，
他手中的船槳，斷裂了。
於是，他撲向疲憊而死的サマユンクル，
奪走他手中的船槳，獨自一人
划著船。
看到這些，我內心的邪念再次湧現。
以沉重的語調，如折斷堅硬的木片般叫喊，
輕盈地，腰肢柔軟地奔走，
竭盡全力聲援暴風的魔力。
在這樣做的過程中，サマユンクル的舵也
斷裂了。オキキリムイ撲向シュプンラムカ，
奪走他的船槳，
勇敢地划著船。
但是，他的船槳也被海浪折斷了。
於是，オキキリムイ在船中
站立著，在狂風中，
他萬萬沒想到身為人類的他會發現我，
他凝視著國之岬，神之岬
之上的，我的眼睛。
他原本溫柔的臉上顯露出憤怒之色，
擺弄著他的袋子，
從中取出的是，蓬草的小弓和
蓬草的小箭。
看到這些，我暗自竊笑。
「人類又能做什麼，有什麼可怕的，
那種蓬草的小箭有什麼用呢。」
我這樣想著，在這岬角，
國之岬，神之岬之上，
我一直向上，一直向下，輕盈地
腰肢柔軟地奔走，以沉重的語調，
如折斷堅硬的木片般，啪嗚，啪嗚地叫喊，
讚美暴風的魔力。
在其中，オキキリムイ射出的箭飛來，
正好刺中我的衣領。
從那以後，我就不知道發生了什麼。
突然回過神來，
天氣非常好，海面上
遼闊無垠，オキキリムイ的漁船什麼的都沒有了。
怎麼回事，我的頭頂
到腳底，都像雁皮燃燒收縮般疼痛。
萬萬沒想到人類射出的小箭會如此折磨我，於是我掙扎著，
在這岬角，國之岬，神之岬
之上，一直向上，一直向下，哭喊著
掙扎，白天黑夜，時而活著，
時而死去，在這樣做的過程中，我不知道
發生了什麼。
突然回過神來，
我身處於大黑狐的兩隻耳朵之間。
大約過了兩天，オキキリムイ以神靈般的姿態
前來，笑眯眯地說道，
「真是好看啊，守護國之岬，神之岬
之上的黑狐神，
因為擁有善良的心，神的心，
所以死得如此體面。」
說著，他取下我的頭，
帶回自己的家，將我的上顎骨
作為自己廁所的地基，將我的下顎
作為他妻子的廁所的基石，
我的身體就那樣與泥土一同腐爛了。
從那以後，無論白天黑夜，
我都飽受惡臭的折磨，我死得毫無價值，死得很慘。
我並非只是身份低微的神靈，
但因為我懷有極其邪惡的心，所以一無是處，
我死得很慘，
所以，從今以後的狐狸們啊，千萬
不要懷有邪惡的心。

狐狸神這樣講述著。
```
