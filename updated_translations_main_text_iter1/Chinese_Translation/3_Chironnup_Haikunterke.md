# LLM-assisted Translation project of Ainu shin'yoshu (アイヌ神謡集) collected by Chiri Yukie 知里幸惠 (1903 - 1922).

## Iterative 1 Updated Chinese Translation of

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
You are translating the following Japanese text into Chinese. The original text is a chant sung by god telling his story. You already have a Chinese translation and an English translation.

Here are your tasks:

1. Criticise the Chinese translation based on the Japanese text. 
2. Compare the Chinese translation with the English translation.
3. Improve the Chinese translation, especially incoporating the pros of the English translation.

Keep the original meanings. Display in Traditional Chinese. If a term cannot be translated, keep the original language.

This is the Japanese text.
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
手の下でその持っていた楫、第3水準1-86-21)が折れてしまいました.
すると,疲れ死んだサマユンクルに
躍りかかりその持っている楫、第3水準1-86-21)をもぎとってたった一人で
舟を漕ぎました.
私はそれを見ると,持前の悪い心がむらむらと出て来ました.
重い調子でかたい木片をポキリポキリと折る様に叫び
軽い足取りで腰やわらかにかけまわり
精を出して暴風の魔に声援しました.
そうしてるうちにサマユンクルの舵も
折れてしまいました.オキキリムイはシュプンラムカに
躍りかかりその※(「楫+戈」、第3水準1-86-21)をとって
勇ましく舟を漕ぎました.
けれども彼の※(「楫+戈」、第3水準1-86-21)も波に折られてしまいました.
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

This is the Chinese translation.
狐狸親自吟唱的歌謠
「Haikunteleke Haikoshitemutori」

Haikunteleke Haikoshitemutori
在國家的海岬,神明的海岬之上
我靜靜地坐著。
某天我走到外面一看
海面風平浪靜,遼闊無垠,在海上
奧基基穆伊、舒彭拉姆卡和薩馬雲庫爾
三人乘船出海捕魚,看到這一幕,
我內心邪惡的念頭蠢蠢欲動。
這個海岬,國家的海岬,神明的海岬
之上,我輕盈地,腰肢柔軟地來回奔跑。
用沉重的語調,像折斷木片一樣,啪嗚,啪嗚地叫喊,
我怒視著這條河的源頭,召喚暴風的魔力。
隨之而來的是,從這條河的
源頭吹來猛烈的風,龍捲風,
一進入海面,立刻
這片海域,上面的海變成了下面,
下面的海變成了上面。奧基基穆伊他們
的漁船在近海的人的海和遠海的人的海
交匯之處(海的中央),遭遇了突如其來的巨變,在波浪間
旋轉。巨大的浪濤像山一樣
覆蓋到船上。於是,
奧基基穆伊、薩馬雲庫爾、舒彭拉姆卡
聲嘶力竭地划槳。
這艘小船像飛舞的落葉般被吹走,
眼看就要傾覆,
但令人欽佩的是,人們非常有力氣,
這艘小船在風中
在波浪上滑行。
看到這一幕,我內心邪惡的念頭再次蠢蠢欲動。
我輕盈地,腰肢柔軟地來回奔跑,
用沉重的語調,像折斷木片一樣,啪嗚,啪嗚地叫喊,
我竭盡全力地聲援暴風的魔力。
在這樣做的過程中,終於,薩馬雲庫爾
的手上,手下,都流出了鮮血,
疲憊地倒下了。
看到他的樣子,我暗自竊笑。
然後我又更加賣力地
輕盈地,腰肢柔軟地來回奔跑,
用沉重的語調,像折斷木片一樣叫喊,
聲援暴風的魔力。
奧基基穆伊和舒彭拉姆卡兩人
互相鼓勵,勇敢地划著船,
但是,突然有一天,舒彭拉姆卡
的手上,手下,都流出了鮮血,
疲憊地倒下了,看到這一幕,
我暗自竊笑。
然後我又輕盈地,腰肢柔軟地
跳躍奔跑,用沉重的語調,像折斷堅硬的木片
一樣叫喊,竭盡全力。
但是,奧基基穆伊卻沒有絲毫疲憊的樣子。
他身上披著一件薄薄的衣物,
划著船,在這過程中,
他手中的槳折斷了。
於是,他跳到已經疲憊死去的薩馬雲庫爾身上,
奪走了他手中的槳,獨自一人
划著船。
我看到這一幕,內心固有的邪惡念頭再次蠢蠢欲動。
用沉重的語調,像折斷堅硬的木片一樣叫喊,
輕盈地,腰肢柔軟地來回奔跑,
竭盡全力地聲援暴風的魔力。
在這樣做的過程中,薩馬雲庫爾的舵也
折斷了。奧基基穆伊跳到舒彭拉姆卡身上,
奪走了他的楫,
勇敢地划著船。
但是他的楫也被海浪折斷了。
於是,奧基基穆伊在船中
站立著,在猛烈的風中,
他萬萬沒想到身為人類的他會發現我,
他凝視著國家的海岬,神明的海岬
之上的,我的眼睛中央。
他原本溫柔的臉上露出了憤怒的神色,
擺弄著他的袋子,
從中取出的是,蓬草的小弓和
蓬草的小箭。
看到這一幕,我暗自竊笑。
「人類又能做什麼,有什麼可怕的,
那種蓬草的小箭有什麼用呢?」
我這樣想著,在這個海岬
國家的海岬,神明的海岬之上
我一直向上,一直向下,輕盈地
腰肢柔軟地來回奔跑,用沉重的語調
像折斷堅硬的木片一樣,啪嗚,啪嗚地叫喊,
讚美暴風的魔力。
在其中,奧基基穆伊射出的箭飛了過來,
正好刺穿了我的衣領。
從那以後,我就不知道發生了什麼。
突然回過神來,
天氣非常好,海面上
遼闊無垠,奧基基穆伊的漁船什麼的都不見了。
怎麼回事,我的頭頂
到腳尖,都像雁皮燃燒收縮一樣疼痛。
萬萬沒想到人類射出的小箭會如此折磨我,於是我掙扎著,
在這個海岬,國家的海岬,神明的海岬
之上,一直向上,一直向下,哭喊著
掙扎,白天黑夜,時而活著,
時而死去,在這樣的過程中,我不知道
發生了什麼。
突然回過神來,
我身處於一隻巨大的黑狐的耳朵和耳朵之間。
過了兩天左右,奧基基穆伊像神明一樣
走了過來,笑眯眯地說道,
「真是好看啊,守護著國家的海岬,神明的海岬
之上的黑狐神明,
因為擁有善良的心,神明的心,
所以死相也很好看啊。」
說著,他拿走了我的頭,
帶回了自己的家,把我的上顎骨
當作自己廁所的地基,把我的下顎
當作他妻子的廁所的基石,
我的身體就那樣和泥土一起腐爛了。
從那以後,無論白天黑夜,
我都飽受惡臭的折磨,我死得毫無價值,死得很慘。
我雖然不是地位低微的神明,
但因為我懷有非常邪惡的心,所以一無是處,
我死得很慘,
所以從今以後的狐狸們啊,千萬
不要懷有邪惡的心。

狐狸神明這樣講述道。


This is the English translation.
Listen closely, for I shall tell you a tale, a song sung by a fox-god of old:

"Haikunteleke Haikoshitemutori"

Haikunteleke Haikoshitemutori,
Upon the cape of the land, the cape of the gods,
I sat in my divine repose.
One day, I ventured forth to gaze upon the world,
The sea was calm, stretching far and wide, and upon it,
Okikirmui, Shupunkamka, and Samayunkur,
Ventured out on a sea hunt, three souls in a single boat.
And as I watched them, a wicked impulse stirred within my heart.

Across the cape, the cape of the land, the cape of the gods,
Up and down, with nimble feet and swaying hips, I darted.
With a heavy voice, like the snapping of dry twigs, I cried, "Pau, Pau!"
And I glared at the source of the river, summoning the demon of the storm.
And as I did, from the river's source, a fierce wind, a whirlwind,
Burst forth and rushed into the sea, and in an instant,
The sea above became the sea below,
And the sea below rose to become the sea above.
Okikirmui and his companions,
Their fishing boat, caught between the sea of men offshore and the sea of men on land,
Met with a sudden and violent change, spinning wildly amidst the waves.
A great wave, like a mountain,
Crashed down upon their boat.
Then Okikirmui, Samayunkur, and Shupunkamka,
Raised their voices and rowed with all their might.
The small boat was tossed about like a falling leaf,
On the verge of capsizing, yet,
Remarkably, the humans were strong,
And the little boat danced upon the waves,
Riding the wind.
Seeing this, the wicked impulse stirred within my heart once more.
With nimble feet and swaying hips, I darted about,
With a heavy voice, like the snapping of dry twigs, I cried, "Pau, Pau!"
And I devoted myself to cheering on the demon of the storm.
And as I did, at last, Samayunkur,
Blood flowing from his hands, above and below,
Collapsed in exhaustion.
Seeing this, I secretly smiled.
Then, once more, I exerted myself,
With nimble feet and swaying hips, I darted about,
With a heavy voice, like the snapping of dry twigs, I cried,
And cheered on the demon of the storm.
Okikirmui and Shupunkamka, the two of them,
Encouraged each other and rowed bravely on,
But then, at last, Shupunkamka,
Blood flowing from his hands, above and below,
Collapsed in exhaustion. Seeing this,
I secretly smiled.
Then, once more, with nimble feet and swaying hips,
I leaped about, with a heavy voice, like the snapping of dry twigs,
I cried out and exerted myself.
But Okikirmui showed no sign of fatigue.
With only a thin garment wrapped around his body,
He continued to row, until,
The oar in his hand snapped.
Then, he leaped upon the exhausted Samayunkur,
And snatched the oar from his grasp, and rowed on alone.

Seeing this, the wicked impulse stirred within my heart once more.
With a heavy voice, like the snapping of dry twigs, I cried,
With nimble feet and swaying hips, I darted about,
And devoted myself to cheering on the demon of the storm.
And as I did, Samayunkur's rudder, too,
Snapped. Okikirmui leaped upon Shupunkamka,
And took his oar,
And rowed bravely on.
But his oar, too, was broken by the waves.
Then, Okikirmui stood in the boat,
Amidst the raging storm,
Never imagining that a mere human could see me,
He gazed into the center of my eyes, upon the cape of the land, the cape of the gods.
His gentle face now filled with anger,
He rummaged in his bag,
And from within, he drew forth a small bow of mugwort,
And a small arrow of mugwort.
Seeing this, I secretly smiled.
"What could a human possibly do to frighten me?
What use could such a mugwort arrow possibly be?"
And so, across the cape,
The cape of the land, the cape of the gods,
Up and down, with nimble feet,
I darted about, with a heavy voice,
Like the snapping of dry twigs, I cried, "Pau, Pau!"
And praised the demon of the storm.
Then, the arrow shot by Okikirmui flew,
And struck me right in the nape of my neck.
And from that moment on, I knew nothing more.
When I awoke,
The weather was fair, and the sea was
Vast and calm, and Okikirmui's fishing boat was nowhere to be seen.
What had happened? From the tip of my head
To the tip of my toes, I felt a burning pain, as if the bark of a birch tree were shrinking.
Never did I imagine that a small arrow shot by a human could cause me such torment.
And so, I writhed in agony,
Across the cape, the cape of the land, the cape of the gods,
Up and down, crying out in pain,
Writhing in agony, living and dying,
Day and night, until, I knew nothing more.
When I awoke,
I was between the ears of a great black fox.
Two days later, Okikirmui arrived, looking like a god,
And said with a smile,
"What a fine sight! The black fox god, watching over
The cape of the land, the cape of the gods,
Possessed a good heart, a divine heart,
And so, he died a beautiful death."
As he spoke, he took my head,
And carried it to his home, and used my upper jawbone
As the foundation of his toilet, and my lower jawbone
As the foundation of his wife's toilet,
And my body rotted away with the earth.
And so, day and night,
Tormented by a foul stench, I died a meaningless, wretched death.
Though I was no mere low-ranking god,
Because I possessed such a wicked heart, I died a useless, wretched death.
Therefore, you foxes of the future, never, ever,
Harbor a wicked heart.

Thus spoke the fox-god, in his tale.


```

### Output
```
狐狸親自吟唱的歌謠
「ハイクンテレケ ハイコシテムトリ」

「ハイクンテレケ ハイコシテムトリ」
於國之岬，神之岬之上，
我踞坐於神聖的靜謐之中。
某日，我走出洞穴，放眼望去，
海面風平浪靜，遼闊無垠。只見海上，
奧基基穆伊、舒彭拉姆卡和薩馬雲庫爾，
三人同舟，出海狩獵。目睹此景，
我內心頓時湧起一股邪惡的衝動。

越過海岬，國之岬，神之岬，
我足履輕盈，腰肢款擺，來回奔馳。
以沉重之聲，如斷裂枯枝，我呼喊：「啪嗚，啪嗚！」
我怒視河之源頭，召喚暴風之魔。
隨之而來，自河之源頭，狂風怒號，旋風驟起，
直撲入海，頃刻之間，
上海變為下海，
下海升為上海。奧基基穆伊一行人，
他們的漁船，被夾在近岸之人和遠海之人之間，
遭遇突如其來的巨變，在波濤中瘋狂旋轉。
巨浪如山，
傾覆而下，壓向小舟。
於是，奧基基穆伊、薩馬雲庫爾、舒彭拉姆卡，
聲嘶力竭，奮力划槳。
小船如落葉般被狂風吹拂，
岌岌可危，眼看就要傾覆，
但令人欽佩的是，這些人何其堅韌，
小船在風中，
於波浪之上，如履平地。
見此情景，我內心邪惡的念頭再次蠢蠢欲動。
我足履輕盈，腰肢款擺，四處奔走，
以沉重之聲，如斷裂枯枝，我呼喊：「啪嗚，啪嗚！」
我竭盡全力，為暴風之魔搖旗吶喊。
如此這般，終於，薩馬雲庫爾，
雙手之上，鮮血淋漓，
精疲力竭，轟然倒下。
見此慘狀，我暗自竊笑。
而後，我更加賣力，
足履輕盈，腰肢款擺，四處奔走，
以沉重之聲，如斷裂枯枝，我呼喊，
為暴風之魔搖旗吶喊。
奧基基穆伊和舒彭拉姆卡二人，
互相鼓勵，勇敢地划著船，
然而，就在此時，舒彭拉姆卡，
雙手之上，鮮血淋漓，
精疲力竭，轟然倒下。見此情景，
我暗自竊笑。
而後，我又足履輕盈，腰肢款擺，
跳躍奔馳，以沉重之聲，如斷裂堅硬的木片，
我呼喊，竭盡全力。
然而，奧基基穆伊卻毫無疲憊之色。
他僅以單薄衣衫蔽體，
奮力划槳，直至，
他手中的槳，應聲折斷。
於是，他躍至已然力竭而死的薩馬雲庫爾身旁，
奪走他手中的槳，獨自一人
划著船。

目睹此景，我內心固有的邪惡念頭再次蠢蠢欲動。
以沉重之聲，如斷裂堅硬的木片，我呼喊，
足履輕盈，腰肢款擺，四處奔走，
竭盡全力，為暴風之魔搖旗吶喊。
如此這般，薩馬雲庫爾的舵，也
斷裂了。奧基基穆伊躍至舒彭拉姆卡身旁，
奪走他的楫，
勇敢地划著船。
然而，他的楫也被海浪無情折斷。
於是，奧基基穆伊在船中
孑然而立，於狂風暴雨之中，
他萬萬沒想到，身為凡人的他，竟能看見我，
他凝視著國之岬，神之岬
之上的，我的雙眼。
他原本溫和的面容，此刻充滿了憤怒，
他翻找著他的袋子，
從中取出的是，蓬草製成的小弓，
以及蓬草製成的小箭。
見此情景，我暗自竊笑。
「凡人又能奈我何？有何可懼？
那蓬草小箭，又有何用？」
我如是想，於此海岬，
國之岬，神之岬之上，
我上下奔走，足履輕盈，
以沉重之聲，如斷裂堅硬的木片，我呼喊：「啪嗚，啪嗚！」
讚頌暴風之魔。
就在此時，奧基基穆伊射出的箭矢飛來，
正中我的後頸。
自那之後，我便一無所知。
猛然醒來，
天氣晴朗，海面
遼闊無垠，奧基基穆伊的漁船早已無影無蹤。
究竟發生了何事？自我的頭頂
至我的腳尖，都如雁皮燃燒般劇痛。
萬萬沒想到，凡人射出的小箭，竟能如此折磨我。
於是我痛苦掙扎，
於此海岬，國之岬，神之岬
之上，上下翻滾，哭喊哀嚎，
在痛苦中掙扎，日夜不息，
時而生，時而死，就在這般煎熬之中，我失去了意識。
再次醒來，
我身處於一隻巨大的黑狐的雙耳之間。
約莫兩日之後，奧基基穆伊如神祇般降臨，
笑意盈盈地說道：
「真是美麗的景象啊！守護著國之岬，神之岬
之上的黑狐神明，
因為擁有一顆善良的心，一顆神明之心，
所以死相也如此安詳。」
說著，他取走了我的頭顱，
帶回了他的家，將我的上顎骨
作為他廁所的地基，將我的下顎骨
作為他妻子的廁所的基石，
而我的身軀，則與泥土一同腐爛殆盡。
自那之後，無論白晝黑夜，
我都飽受惡臭的折磨，我的死亡毫無價值，極其悲慘。
我雖非地位卑微的神明，
但因我懷有極其邪惡的內心，故而一無是處，
我的死亡極其悲慘。
所以，未來的狐狸們啊，切記，
永遠不要懷有邪惡的內心。

狐狸神明如是講述。

The Chinese translation is generally accurate but lacks the poetic and rhythmic qualities of the original Japanese and the English translation. It tends to be more literal, which makes it sound less engaging. The English translation captures the storytelling aspect and the emotional tone more effectively. For example, the repetition of "cape of the land, cape of the gods" is beautifully rendered in English, emphasizing the location's significance, while the Chinese translation is functional but less evocative. The phrase "nimble feet and swaying hips" is also more vividly translated into English than its Chinese counterpart. The onomatopoeic "Pau, Pau!" is kept as is, which is good, but the description of the sound could be improved in Chinese. The English translation also adds some phrases to make the story more readable, such as "Listen closely, for I shall tell you a tale, a song sung by a fox-god of old:", which is missing in the Chinese translation. The description of the fox god's death is also more vivid in English.

Comparing the Chinese and English translations, the English version is more descriptive and interpretive, while the Chinese version is more direct and literal. The English translation often expands on the original text to enhance the narrative flow and emotional impact, while the Chinese translation sticks closer to the literal meaning of the Japanese. For example, the English translation uses phrases like "divine repose" and "wicked impulse stirred within my heart" to add depth to the character's emotions, which are not as explicitly conveyed in the Chinese translation.

To improve the Chinese translation, I will focus on incorporating more descriptive language, enhancing the rhythmic flow, and capturing the emotional nuances of the original Japanese text, drawing inspiration from the English translation where appropriate. I will also try to make the language more vivid and engaging, while maintaining accuracy.
```

