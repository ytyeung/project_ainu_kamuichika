# LLM-assisted Translation project of Ainu shin'yoshu (アイヌ神謡集) collected by Chiri Yukie 知里幸惠 (1903 - 1922).

## Iterative 1 Updated Chinese Translation of

## Repun Kamui yaieyukar, “Atuika tomatomaki kuntuteashi hm hm!” 海の神が自ら歌った謡「アトイカ トマトマキ クントテアシ フム フム!」

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
海の神が自ら歌った謡「アトイカ
トマトマキ クントテアシ フム フム!」

アトイカ トマトマキ クントテアシ フムフム
長い兄様,六人の兄様,長い姉様,六人の姉様
短い兄様,六人の兄様,短い姉様,六人の姉様が
私を育てて居たが,私は
宝物の積んである傍に高床をしつらえ,その高床の上に
すわって鞘さや刻み鞘彫り
それのみを
事として暮していた.
毎日,朝になると兄様たちは
矢筒を背負って姉様たちと一しょに出て行って
暮方になると疲れた顔色で
何も持たずに帰って来て姉様たちは
疲れているのに食事拵こしらえをし,私にお膳を出して
自分たちも食事をして食事のあとが片附くと,
それから兄様たちは矢を作るのに忙しく手を動かす.
矢筒が一ぱいになると,みんな疲れているものだから
寝ると高鼾たかいびきを響かせてねむってしまう.
その次の日になるとまだ暗い中に
みんな起きて姉様たちが食事拵えをして私に膳を出し
みんな食事が済むと,また矢筒を背負って
行ってしまう.また夕方になると
疲れた顔色で何も持たずに帰って来て
姉様たちは食事拵え,兄様たちは矢を作って,
何時いつでも同じ事をしていた.
ある日にまた兄様たち姉様たちは
矢筒を背負って出て行ってしまった.
宝物の彫刻を私はしていたがやがて
高床の上に起き上り金の小弓に
金の小矢を持って外へ出て
見ると海はひろびろと凪なぎて
海の東へ海の西へ鯨たちが
パチャパチャと遊んで居る.すると
海の東に長い姉様,六人の姉様が手をつらねて輪をつくると,
短い姉様,六人の姉様が,輪の中へ鯨を追い込む,
長い兄様,六人の兄様,短い兄様,六人の兄様が
輪の中へ鯨をねらい射つと,その鯨の
下を矢が通り上を矢が通る.
毎日毎日彼等はこんな事をして
いたのであった.見ると海の中央に
大きな鯨が親子の鯨が上へ下へ
パチャパチャと遊んで居るのが見えたので
遠い所から金の小弓に金の小矢を
番つがえてねらい射ったところ,一本の矢で
一度に親子の鯨を射貫いてしまった.
そこで一つの鯨のまんなかを斬って
その半分を姉様たちの輪の中へ
ほうりこんだ.それから鯨一ツ半の鯨を
尾の下にいれて人間の国に
むかって行きオタシュツ村に
着いて一ツ半の鯨を
村の浜へ押し上げてやった.
それから海の上にゆっくりと
游いで帰って
来たところが,誰かが
息を切らしてその側をはしるものがあるので
見ると,海のごめであった.
息をきらしながら云うことには,
「トミンカリクル カムイカリクル イソヤンケクル
勇マシイ神様,大神様,
あなたはなんの為に,卑しい人間共,悪い人間共に
大きな海幸をおやりになったのです.
卑しい人間共,悪い人間共は,斧もて
鎌をもて大きな海幸をブツブツ切ったり突っついたり
削り取っています,勇ましい神様
大神様さあ早く大海幸を
お取り返しなさいませ.あんなに沢山,海幸をおやりに
なっても卑しい人間たち悪い人間たちは
有難いとも思わずこんな事をします.」
と云うので私は笑って云う
ことには,
「私は人間たちに呉れてやったものだから
今はもう自分の物だから,人間たちが
自分の持物を鎌でつつこうが斧で
削ろうがどうでも
自分たちの自由に食べたらいいではないか
それがどうなのだ.」と云うと
海のごめは所在無げにしているけれども
私はそれを少しも構わず海の上を
ゆっくりとおよいで
もう日が暮れようとしている時に,私の海へ
着いた.見ると
十二人の兄様,十二人の
姉様は,彼の半分の鯨をはこび
きれなくてみんなで掛声高く
海の東に,グズグズしている.
私は実にあきれてしまった.
私はそれに構わずに家へ
帰り,高床の上にすわった.
そこで後ふりかえって人間の世界の方を
見ると,私が打ち上げた一ツ
半の鯨のまわりをとりまいてりっぱな男たちや
りっぱな女たちが盛装して
海幸をば喜び舞い海幸をば歓び躍り,後の砂丘
の上にはりっぱな敷物が敷かれて
その上にオタシュツ村の村長が
六枚の着物に帯を束たばね,六枚の着物を
羽織って,りっぱな神の冠,先祖の冠を
頭に冠り,神授の剣を腰に佩はき
神の様に美しい様子で手を高くさし上げ
礼拝をしている.人間たちは泣いて
海幸をよろこんでいる.
何をごめが人間たちが
斧で鎌で私の押し上げた鯨を
突っついていると云ったが,
村長をはじめ
村民は,昔から
宝物の最も尊いものとしている神剣を取り出して
それで肉を斬って搬はこんでいる.
それから,私の兄様たち姉様たちは帰って来る
様子もない.
二日三日たった時,窗の方に
何か見える様だ,それで
振りかえって見て見ると,窗の上に
かねの盃にあふれる程
酒がはいっていてその上に
御幣を取りつけた酒箸が載っていて,
行きつ戻りつ,使者としての口上を述べて云うには,
「私はオタシュツ村の人で
畏れ多い事ながらおみきを差し上げます.」と
オタシュツ村の村長が村民
一同を代表して私に礼をのべる
次第をくわしく話し,
「トミンカリクル カムイカリクル イソヤンケクル
大神様,勇ましい神様でなくて誰が,
この様に私たちの村に饑饉があって
もう,どうにも仕様がない程
食物に窮している時に哀れんで下されましょう.
私たちの村に生命を与えて下さいました事,
誠に有難う御座います,海幸をよろこび
少しの酒を作りまして,小さな幣ぬさを
添え,大神様に謝礼
申し上げる次第であります.」という事を
幣つきの酒箸が行きつ戻りつ申し立てた.
それで私は起き上って,かねの盃を
取り,押しいただいて
上の座の六つの酒樽の蓋ふたを開き
美酒を少しずつ入れて
かねの盃を窗の上にのせた.
それが済むと,高床の上に腰を下し
見ると彼の盃は箸と共に
なくなっていた.それから,鞘を刻み
鞘を彫り,していてやがて
ふと面をあげて見ると,
家の中は美しい幣で一ぱいになっていて
家の中は白い雲がたなびき白いいなびかりが
ピカピカ光っている.私はああ美しいと思った.
それからまた,二日三日たつと,
その時やっと,家のそとで,兄様たちや
姉様たちが掛声高く彼の鯨を
引っ張って来たのがきこえだした.私はあきれて
しまった.家の中へはいる様子を
眺めると,兄様たちや姉様たちは
たいへん疲れて,顔色も萎しおれている.
みんなはいって来て,沢山の幣を見ると,
驚いてみんななん遍もなん遍も拝した.
そのうちに,東の座の六つの酒樽は
溢れるばかりになって,神の好物の
酒の香が家の中に漂うた.
それから私は,美しい幣で家の中を飾りつけ,
遠方の神,近所の神を招待し
盛んな酒宴を張った.姉様たちは
鯨を煮て,神たちに出すと,
神たちは,舌鼓を打ってよろこんだ.
宴酣たけなわの頃私は起き上り
斯々かくかく,人間世界に饑饉があって
あわれに思い,海幸を打ち上げた次第や
人間たちをよくしてやると,悪い神々が
それをねたみ,海のごめが私に中
傷した事や,オタシュツ村の
村長が斯々の言葉をとって私に礼をのべ
幣つきの酒箸が使者になって来た事など
詳しく物語ると,神たちは
一度に揃って打ちうなずきつつ,
私をほめたたえた.
それからまた,盛な宴をはり
神たちの,そこに
ここに舞う音,躍る音は
美しき響をなし,姉様たちは
提子ちょうしを持って席の間を酌して
まわるもあり,女神たち
と共に美しい声で歌うもある.
二日三日たって宴を閉じた.
神々に美しい幣を二つ三つずつ
上げると神々は腰の央なかを
ギックリ屈めてなん遍もなん遍も礼をして,
みんな自分の家に立ち帰った.
そのあと,何時でも同じく長い兄様,六人の兄様
長い姉様,六人の姉様,短い姉様,六人の姉様
短い兄様,六人の兄様と一しょにい,
人間たちが酒を造るとその度毎に
私に酒を送り私のところへ幣をよこす.
今はもう,人間たちも食物の不足も
なんの困る事も無く平穏に
暮しているので,私は安心をしています.

This is the Chinese translation.
海神親自吟唱的歌謠「アトイカ トマトマキ クントテアシ フム フム!」

アトイカ トマトマキ クントテアシ フムフム
長兄大人,六位兄長大人,長姊大人,六位姊姊大人,
短兄大人,六位兄長大人,短姊大人,六位姊姊大人,
養育著我,而我卻
在堆滿寶物的地方搭建高床,在那高床上
坐著雕刻刀鞘,
只以此為
事度日。
每天,早上兄長們
背著箭筒與姊姊們一同出門,
傍晚時分,帶著疲憊的神色
空手而歸,姊姊們
明明也很疲憊,卻還是準備餐點,為我擺上膳食,
自己也用餐,餐後收拾完畢,
之後,兄長們便忙著製作箭矢。
箭筒裝滿後,大家都累了,
睡覺時便發出高亢的鼾聲。
隔天,天還沒亮,
大家就起身,姊姊們準備餐點,為我擺上膳食,
大家用完餐後,又背起箭筒
出門去了。傍晚時分,又
帶著疲憊的神色空手而歸,
姊姊們準備餐點,兄長們製作箭矢,
無論何時都做著相同的事情。
某天,兄長們和姊姊們又
背著箭筒出門去了。
我原本在雕刻寶物,不久後
便從高床上起身,拿著金製小弓和
金製小箭走到外面,
看見大海遼闊平靜,
鯨魚們在海的東邊和西邊
嬉戲玩耍。接著,
海的東邊,長姊大人,六位姊姊大人手牽著手圍成一圈,
短姊大人,六位姊姊大人,將鯨魚趕入圈中,
長兄大人,六位兄長大人,短兄大人,六位兄長大人
瞄準圈中的鯨魚射箭,箭矢
從鯨魚下方穿過,從上方掠過。
他們每天每天都做著這樣的事情。看見海的中央,
一隻巨大的鯨魚和牠的孩子鯨魚正在上下
嬉戲玩耍,
我便從遠處用金製小弓
搭上金製小箭瞄準射去,一箭
同時貫穿了母子鯨魚。
於是,我將其中一隻鯨魚從中間斬斷,
將一半拋入姊姊們的圈中。然後,將一隻半的鯨魚
放在尾巴下方,朝著人類的國度
前進,抵達オタシュツ村,
將一隻半的鯨魚
推到村子的海灘上。
之後,我悠閒地在海上
游了回去,
這時,有人
氣喘吁吁地從旁邊跑過,
一看,原來是海のごめ(海神使者)。
牠氣喘吁吁地說道:
「トミンカリクル カムイカリクル イソヤンケクル
勇猛的神明大人,偉大的神明大人,
您為何要將如此豐盛的海產賜給卑賤的人類,邪惡的人類呢?
卑賤的人類,邪惡的人類,用斧頭
用鐮刀將豐盛的海產切得亂七八糟,又戳又
削,勇猛的神明大人,
偉大的神明大人,請快點將豐盛的海產
收回去吧。賜給他們這麼多海產,
卑賤的人類,邪惡的人類卻
不心懷感激,還做出這種事。」
聽了牠的話,我笑著說:
「我既然已經賜給人類了,
現在就是他們的東西了,人類
要用鐮刀戳,還是用斧頭
削,都隨他們的便,讓他們自由地吃就好,
那又怎麼樣呢?」
海のごめ雖然有些不知所措,
我卻毫不在意,悠閒地在海上
游著,
在快要日落的時候,抵達了我的海域。看見
十二位兄長大人,十二位
姊姊大人,因為搬不動那半隻鯨魚,
大家一起大聲呼喊著,
在海的東邊,慢吞吞地搬運著。
我實在是感到無語。
我沒有理會他們,直接回家,
坐在高床上。
於是我回頭看向人類的世界,
看見我推上去的那一隻
半的鯨魚周圍,聚集了許多出色的男人和
出色的女人,盛裝打扮,
歡欣鼓舞地慶祝海產,後方的沙丘
上鋪著華麗的墊子,
オタシュツ村的村長
穿著六件和服,束著腰帶,披著六件和服,
頭戴華麗的神之冠,祖先之冠,
腰佩神授之劍,
以如神般美麗的姿態高舉雙手
禮拜著。人類們哭著
喜悅著海產。
雖然海のごめ說人類們
用斧頭和鐮刀戳著我推上去的鯨魚,
但村長和
村民們,從以前就
將寶物中最珍貴的神劍取出,
用它來切割肉並搬運著。
而且,我的兄長們和姊姊們也沒有回來的
跡象。
過了兩三天,窗戶邊
好像有什麼東西,
於是我回頭看去,看見窗戶上
放著裝滿
酒的金盃,上面
放著裝飾著御幣的酒箸,
來回移動著,以使者的身分陳述道:
「我是オタシュツ村的人,
雖然非常惶恐,但還是要獻上御神酒。」
オタシュツ村的村長代表
全體村民向我表達感謝之意,
詳細地說明了事情的經過,
「トミンカリクル カムイカリクル イソヤンケクル
不是偉大的神明大人,勇猛的神明大人,還會有誰
在我們村子發生饑荒,
已經到了走投無路的地步,
食物匱乏的時候,憐憫我們呢?
您賜給我們村子生命,
實在非常感謝,我們用海產釀造了
少許的酒,並附上小小的幣束,
向大神大人表達謝意。」
裝飾著御幣的酒箸來回移動著陳述道。
於是我起身,將金盃
拿起,恭敬地接過,
打開上方座位的六個酒桶的蓋子,
將美酒一點一點地倒入,
將金盃放在窗戶上。
做完這些後,我便坐在高床上,
看見那金盃連同酒箸
都消失了。之後,我繼續雕刻刀鞘,
雕刻著,不知不覺地
抬頭一看,
家裡已經擺滿了美麗的幣束,
家裡瀰漫著白色的雲霧,白色的閃電
閃爍著。我覺得啊,真美。
之後,又過了兩三天,
這時,終於聽見家裡外面,兄長們和
姊姊們大聲呼喊著,
拉著那隻鯨魚回來了。我感到無語。
我望著他們進入家裡的樣子,
兄長們和姊姊們
非常疲憊,臉色也憔悴不堪。
大家都進來後,看見這麼多的幣束,
驚訝地拜了又拜。
不久,東邊座位的六個酒桶
都滿溢了出來,神明喜愛的
酒香瀰漫在屋內。
之後,我用美麗的幣束裝飾家裡,
邀請遠方的神明,附近的神明,
舉辦盛大的酒宴。姊姊們
煮了鯨魚,獻給神明們,
神明們都讚不絕口,非常高興。
宴會正酣時,我起身,
詳細地說明了人類世界發生饑荒,
我憐憫他們,將海產推上去的經過,
以及我善待人類,卻被邪惡的神明
嫉妒,海のごめ中傷我的事情,
還有オタシュツ村的
村長以如此這般的言語向我表達感謝,
裝飾著幣束的酒箸成為使者前來的事情等等,
神明們聽了,
一致點頭,
稱讚我。
之後,又舉辦了盛大的宴會,
神明們的,在那裡
這裡跳舞的聲音,躍動的聲音,
發出美妙的聲響,姊姊們
拿著提壺在席間斟酒,
也有人與女神們
一同用美妙的聲音歌唱。
過了兩三天,宴會結束了。
我將兩三個美麗的幣束
獻給神明們,神明們都彎著腰
恭敬地行了無數次的禮,
大家都回到自己的家裡。
在那之後,無論何時都一樣,長兄大人,六位兄長大人,
長姊大人,六位姊姊大人,短姊大人,六位姊姊大人,
短兄大人,六位兄長大人都一起,
只要人類們釀酒,每次都會
送酒給我,並將幣束送到我這裡。
現在,人類們也不再為食物不足所
困擾,過著平穩的
生活,我感到很安心。


This is the English translation.
Atoika Tomatomaki Kuntoteashi Fumu Fumu!
Long brothers, six in number, long sisters, six in number,
Short brothers, six in number, short sisters, six in number,
They raised me, but I,
Beside the treasures piled high, built a raised platform, and upon that platform,
I sat, carving sheaths, engraving sheaths,
That alone
Was my life's pursuit.
Each day, as morning broke, my brothers,
Shouldering quivers, went out with my sisters,
And as evening fell, with weary faces,
They returned empty-handed, while my sisters,
Though weary, prepared the meal, set my place,
And after they ate and cleared away the dishes,
Then my brothers busied themselves, crafting arrows.
When the quivers were full, for they were all weary,
They slept, their loud snores echoing in the night.
The next day, while still dark,
They all arose, my sisters preparing the meal, setting my place,
And when all had eaten, they shouldered their quivers once more,
And departed. Again, as evening fell,
With weary faces, they returned empty-handed,
My sisters preparing the meal, my brothers crafting arrows,
Ever and always, they did the same.
One day, again, my brothers and sisters,
Shouldered their quivers and went away.
I was carving treasures, but soon,
I rose upon the raised platform, and with a golden bow,
And golden arrows, I went outside,
And saw the sea, vast and calm,
And to the east of the sea, to the west of the sea, whales,
Splashed and played. Then,
To the east of the sea, long sisters, six in number, joined hands, forming a ring,
Short sisters, six in number, drove the whales into the ring,
Long brothers, six in number, short brothers, six in number,
Aimed and shot at the whales within the ring, the arrows
Passing beneath, the arrows passing above.
Day after day, they did this,
So I saw in the center of the sea,
A great whale, a whale and its calf, rising and falling,
Splashing and playing.
From afar, with my golden bow, and golden arrows,
I aimed and shot, and with a single arrow,
I pierced both whale and calf at once.
Then, I cut the whale in half,
And threw half into the ring of my sisters. Then, with one and a half whales,
I placed them beneath their tails and headed towards the land of humans,
Arriving at Otasutsu village,
I pushed the one and a half whales
Onto the village beach.
Then, slowly, upon the sea,
I swam back,
When someone,
Breathless, ran beside me,
And I saw it was the sea grebe.
Gasping for breath, it said,
"Tominkarukur Kamuykarukur Isoyankekur
Brave God, Great God,
Why have you given such great sea bounty to the lowly humans, the wicked humans?
The lowly humans, the wicked humans, with axes,
With sickles, hack and poke,
And carve away at the great sea bounty, Brave God,
Great God, quickly, take back the great sea bounty!
Though you give them so much sea bounty, the lowly humans, the wicked humans,
Do not appreciate it, and do such things!"
So I laughed and said,
"I have given it to the humans,
Now it is theirs, let the humans
Poke at their possessions with sickles, or
Carve them with axes, let them eat as they please,
What does it matter?" And the sea grebe was discomfited,
But I paid it no mind, and upon the sea,
I swam slowly,
And as the day was ending, I arrived at my sea. And I saw,
Twelve brothers, twelve
Sisters, unable to carry
The half whale, all together, with loud cries,
Were struggling to the east of the sea.
I was truly astonished.
I paid them no mind and returned home,
And sat upon the raised platform.
Then, looking back towards the world of humans,
I saw that around the one and a half
Whales I had cast ashore, splendid men and
Splendid women, in their finest attire,
Rejoiced and danced over the sea bounty, celebrated and leaped, and upon the dunes behind,
A splendid mat was spread,
And upon it, the village chief of Otasutsu village,
With six robes and a bundled sash, wearing six robes,
And a splendid god's crown, an ancestral crown,
Upon his head, and a god-given sword at his waist,
In a godlike, beautiful manner, raised his hands high,
And offered prayers. The humans wept,
Rejoicing in the sea bounty.
What the grebe said, that the humans
Were poking at the whale I had cast ashore with axes and sickles,
Was not true, for the village chief and
The villagers, from ancient times,
Took out the god sword, which they considered the most precious of treasures,
And with it, they cut the meat and carried it away.
And then, my brothers and sisters showed no sign of returning.
Two or three days passed, and then, something
Appeared in the window, so
I turned and looked, and upon the window,
A golden cup, overflowing
With sake, and upon it,
Sacred paper streamers attached to sake chopsticks,
Going back and forth, delivering a message as an envoy, saying,
"I am from Otasutsu village, and
Though it is presumptuous, I offer this sake." And
The village chief of Otasutsu village, representing
All the villagers, spoke in detail of their gratitude,
"Tominkarukur Kamuykarukur Isoyankekur
Great God, Brave God, who else,
When our village was in famine,
And we were so desperately
Lacking food, would have had pity on us?
We are truly grateful that you have given life to our village,
Rejoicing in the sea bounty,
We have made a little sake, and added
Small sacred paper streamers, to offer our thanks
To the Great God." This
The sake chopsticks with streamers declared, going back and forth.
So I rose, and took the golden cup,
And reverently received it,
Opened the lids of the six sake barrels in the upper seat,
Poured a little of the fine sake,
And placed the golden cup upon the window.
When that was done, I sat down upon the raised platform,
And saw that the cup, along with the chopsticks,
Had disappeared. Then, carving sheaths,
Engraving sheaths, and soon,
I suddenly raised my face,
And the house was filled with beautiful streamers,
And the house was filled with white clouds, and white lightning
Flashed brightly. I thought, "Ah, how beautiful."
Then again, two or three days passed,
And at that time, at last, outside the house, my brothers and
Sisters, with loud cries,
Began to drag the whale. I was astonished.
Watching them enter the house,
My brothers and sisters were
Very weary, their faces pale.
When they all entered, seeing the many streamers,
They were amazed, and bowed many times.
Meanwhile, the six sake barrels in the eastern seat
Were overflowing, and the scent of the god's favorite
Sake filled the house.
Then I decorated the house with beautiful streamers,
Invited the gods of afar, the gods of near,
And held a grand feast. My sisters
Cooked the whale, and when they offered it to the gods,
The gods smacked their lips and rejoiced.
As the feast reached its height, I rose,
And told in detail how there was a famine in the human world,
And feeling pity, I had cast ashore the sea bounty,
And how the wicked gods, envying this,
And how the sea grebe had slandered me,
And how the village chief of Otasutsu village had expressed his gratitude in such words,
And how the sake chopsticks with streamers had come as envoys,
And as I told the story in detail, the gods
All nodded in unison,
And praised me.
Then again, we held a grand feast,
And the sounds of the gods,
Dancing here and there, leaping,
Made a beautiful sound, and my sisters,
Carrying sake pitchers, went around pouring sake
Between the seats, and sang with beautiful voices
Together with the goddesses.
Two or three days passed, and the feast ended.
I gave the gods two or three beautiful streamers each,
And the gods bent low at the waist,
And bowed many times,
And all returned to their homes.
After that, as always, long brothers, six in number,
Long sisters, six in number, short sisters, six in number,
Short brothers, six in number, were with me,
And whenever the humans made sake,
They sent sake to me, and sent streamers to my place.
Now, the humans have no shortage of food
And no troubles, and they live in peace,
So I am at ease.


```

### Output
```
海神親自吟唱的歌謠「アトイカ トマトマキ クントテアシ フム フム!」

アトイカ トマトマキ クントテアシ フムフム
有長兄六人，有長姊六人，
有短兄六人，有短姊六人，
他們養育著我。而我呢？
在堆滿寶物之處，築起高台，
我便端坐其上，
雕琢刀鞘，精描細繪，
以此為業，度日。

每日清晨，兄長們
背負箭筒，與姊姊們一同出門，
黃昏時分，面帶倦色，
空手而歸。姊姊們雖也疲憊，
仍舊準備餐食，為我擺上，
她們也用膳，餐後收拾完畢，
兄長們便忙碌起來，製作箭矢。
箭筒裝滿，眾人皆已疲乏，
沉沉睡去，鼾聲如雷。

次日，天色未明，
眾人起身，姊姊們備餐，為我擺膳，
大家用完餐，又再背起箭筒，
出門而去。傍晚時分，依舊
面帶倦容，空手而回。
姊姊們準備餐食，兄長們製作箭矢，
日復一日，年復一年，皆是如此。

某日，兄長姊姊們又
背起箭筒，出門遠去。
我本在雕琢寶物，不久
起身，走下高台，手持金弓，
金箭在手，來到戶外。
只見大海遼闊，風平浪靜，
鯨魚們在海之東，海之西，
嬉戲玩耍，濺起浪花。忽見
海之東，長姊六人，手牽著手，圍成一圈，
短姊六人，將鯨魚驅趕入圈，
長兄六人，短兄六人，
瞄準圈中鯨魚，引弓射箭，
箭矢從鯨身下穿過，從鯨背上掠過。

他們日日如此。
我望向海的中央，
一隻巨鯨，帶著小鯨，正在上下
嬉戲玩耍，濺起浪花。
我從遠處，以金弓，
搭上金箭，瞄準射去，一箭
竟同時貫穿母子二鯨。

我將其中一隻鯨魚從中斬斷，
把一半拋入姊姊們的圈內，而將另一隻半鯨魚
置於尾下，朝人類的國度
而去，抵達オタシュツ村，
將這隻半鯨
推上了村子的海灘。

之後，我悠然自得地在海上
游了回去。
這時，有人
氣喘吁吁地從我身旁跑過，
定睛一看，原來是海のごめ(海神使者)。
牠上氣不接下氣地說道：
「トミンカリクル カムイカリクル イソヤンケクル
勇猛的神明啊，偉大的神明啊！
您為何要將如此豐饒的海產，賜予卑賤的人類，邪惡的人類？
這些卑賤的人類，邪惡的人類，竟用斧頭，
用鐮刀，將這豐盛的海產，亂砍亂戳，
削割殆盡！勇猛的神明啊，
偉大的神明啊，請您趕快將這海產
收回去吧！您賜予他們如此多的海產，
這些卑賤的人類，邪惡的人類，
不但不知感恩，還做出這等惡行！」

聽了牠的話，我笑道：
「我既已將之賜予人類，
現在便是他們的了。人類
要用鐮刀戳，還是用斧頭
削，悉聽尊便，任他們自由食用，
又有何妨？」
海のごめ聽了，有些不知所措，
我卻毫不在意，依舊悠然自得地在海上
游著。

夕陽西下之時，我回到了自己的海域，
只見十二位兄長，十二位
姊姊，搬不動那半隻鯨魚，
眾人齊聲呼喊，
在海的東邊，慢吞吞地拖著。
我實在無語。

我沒有理會他們，徑自回家，
端坐於高台之上。
回首望向人類世界，
只見我推上岸的那隻
半鯨周圍，聚集了盛裝打扮的
俊男美女，
歡欣鼓舞地慶祝這海的恩賜，後方的沙丘
上，鋪著華麗的墊子，
オタシュツ村的村長，
身穿六件和服，束緊腰帶，
頭戴華麗的神之冠冕，祖先之冠，
腰佩神授之劍，
以如神祇般莊嚴美麗的姿態，高舉雙手，
虔誠禮拜。人類們喜極而泣，
歡慶這海的饋贈。

海のごめ說人類
用斧頭和鐮刀戳著我推上岸的鯨魚，
並非事實。村長與
村民們，自古以來，
便取出視為至寶的神劍，
用它來切割鯨肉，並搬運著。

我的兄長姊姊們，卻遲遲不見歸來。

過了兩三天，窗邊
似乎出現了什麼，
回頭一看，只見窗戶上
放著一個滿溢
美酒的金盃，上面
橫著裝飾著御幣的酒箸，
來回移動，以使者的身分傳達訊息：
「我是オタシュツ村的人，
冒昧前來，敬獻御神酒。」
オタシュツ村的村長，代表
全體村民，向我表達由衷的感謝，
並詳細地說明了事情的經過：
「トミンカリクル カムイカリクル イソヤンケクル
若非偉大的神明，勇猛的神明，
在我們村莊遭受饑荒，
走投無路，
糧食匱乏之時，又有誰會憐憫我們呢？
您賜予我們村莊生命，
實在感激不盡。我們用海產釀造了
些許薄酒，並附上小小的幣束，
向大神大人表達謝意。」
裝飾著御幣的酒箸，來回移動，陳述著。

於是我起身，拿起金盃，
恭敬地接過，
打開上方六個酒桶的蓋子，
將美酒一點一滴地倒入，
再將金盃放回窗戶上。

做完這些，我便坐回高台，
只見那金盃連同酒箸，
都已消失不見。之後，我繼續雕琢刀鞘，
不知不覺地
抬頭一看，
屋內已擺滿了美麗的幣束，
白色的雲霧繚繞，白色的閃電
閃爍耀眼。我心想，啊，真美啊！

又過了兩三天，
終於聽到屋外，兄長姊姊們
齊聲呼喊，
拖著那隻鯨魚回來了。我感到十分驚訝。
看著他們進入屋內的樣子，
個個疲憊不堪，面容憔悴。

眾人進屋，看見如此多的幣束，
驚訝不已，連忙拜了又拜。
不久，東邊的六個酒桶
都滿溢了出來，神明喜愛的
酒香瀰漫在屋內。

我用美麗的幣束裝飾屋內，
邀請遠方的神明，近處的神明，
舉辦盛大的酒宴。姊姊們
烹煮鯨肉，獻給神明們，
神明們讚不絕口，歡欣鼓舞。

宴會正酣時，我起身，
詳細地講述了人間發生饑荒，
我心生憐憫，將海產推上岸的經過，
以及我善待人類，卻被邪惡的神明
嫉妒，海のごめ中傷我的事情，
還有オタシュツ村的
村長以如此這般的言語向我表達感謝，
裝飾著幣束的酒箸前來致謝等等。
神明們聽了，
一致點頭，
稱讚我。

之後，我們再次舉辦盛大的宴會，
神明們的
舞蹈聲，跳躍聲，
交織成美妙的樂章。姊姊們
手持酒壺，在席間斟酒，
也有人與女神們
一同高歌，歌聲婉轉動聽。

過了兩三天，宴會結束。
我將兩三個美麗的幣束
贈予神明們，神明們彎腰鞠躬，
再三拜謝，
各自返回自己的居所。

從此以後，無論何時，長兄六人，
長姊六人，短姊六人，
短兄六人，都與我同在。
只要人類釀酒，每次都會
送酒給我，並將幣束送到我這裡。
如今，人類不再為糧食短缺所
困擾，過著安穩的
生活，我也感到安心了。

The Chinese translation is generally accurate but lacks the poetic and rhythmic qualities of the original Japanese and the English translation. It tends to be overly literal, especially in the repetition of '大人' after each title, which sounds unnatural in Chinese. The English translation captures the storytelling tone and rhythm better. It also makes better choices in translating certain terms, such as avoiding honorifics like '大人'.

Comparing the Chinese and English translations, the English version flows more smoothly and reads more like a story. It avoids unnecessary repetition and uses more natural phrasing. For example, the English translation of the whale hunting scene is more vivid and engaging than the Chinese translation.

To improve the Chinese translation, I will focus on making it more idiomatic, removing unnecessary honorifics, and incorporating the strengths of the English translation in terms of rhythm and storytelling.
```

