# LLM-assisted Translation project of Ainu shin'yoshu (アイヌ神謡集) collected by Chiri Yukie 知里幸惠 (1903 - 1922).

## English Translation of

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
Translate the following text from Japanese to English. The original text is a poem. Try to make the translation poetic but keep the original meanings.

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
```

### Output
```
Here is an English translation of the poem, aiming for a poetic feel while preserving the original meaning:

**The Song of the Sea God: Atoika**

*Atoika tomatomaki kuntoteashi hum hum!*

Atoika tomatomaki kuntoteashi hum hum!
Long elder brothers, six in all, long elder sisters, six in all,
Short younger brothers, six in all, short younger sisters, six in all,
Raised me as their own, but I,
Beside the treasure hoard, built a raised platform, and upon it
Sat carving scabbards, engraving scabbards,
That alone
Was my life's pursuit.
Each day, as morning broke, my brothers
Shouldered their quivers, went forth with my sisters,
And as evening fell, returned with weary faces,
Empty-handed. My sisters, though tired,
Prepared the meals, set my place,
Ate themselves when done, and as the dishes cleared,
My brothers busied themselves crafting arrows.
When the quivers overflowed, weary as they were,
They slept, their loud snores echoing through the night.
The next day, before dawn's first light,
They rose again, my sisters preparing the meal, setting my place,
And when all had eaten, they shouldered their quivers once more
And departed. Again, as evening fell,
They returned with weary faces, empty-handed,
My sisters preparing the meal, my brothers crafting arrows,
Always, always, the same routine.
One day, again, my brothers and sisters
Shouldered their quivers and went forth.
I was carving treasures, but soon
Rose from my platform, took up a golden bow
And golden arrows, went outside, and saw
The sea, vast and calm,
And whales, to the east and to the west,
Playing with splashes. Then,
To the east of the sea, the long elder sisters, six in all, joined hands to form a ring,
The short younger sisters, six in all, drove the whales into the ring,
The long elder brothers, six in all, the short younger brothers, six in all,
Aimed and shot at the whales within the ring, their arrows
Passing beneath and above.
Every day, they did this.
Then I saw, in the center of the sea,
A great whale, a whale and its calf, playing
With splashes, rising and falling.
From afar, I nocked a golden arrow to my golden bow,
Aimed, and shot, and with a single arrow
Pierced both whale and calf at once.
Then I cut the great whale in half,
And threw one half into the sisters' ring.
Then, with the whale and a half beneath its tail,
I headed toward the land of humans,
Arrived at the village of Otasutsu,
And pushed the whale and a half
Onto the village shore.
Then, slowly, I swam back
Across the sea, when someone
Came running, breathless, beside me.
It was the sea sprite.
Gasping for breath, it said,
"Tomin karikuru kamui karikuru isoyankekuru,
Brave god, great god,
Why have you given such a great sea bounty to the lowly humans, the wicked humans?
The lowly humans, the wicked humans, with axes
And sickles, are hacking and poking and scraping
At the great sea bounty. Brave god,
Great god, take back the great sea bounty at once!
Even though you have given them so much, the lowly humans, the wicked humans,
Do not appreciate it, and do such things!"
Hearing this, I laughed and said,
"I gave it to the humans,
It is theirs now, so let them
Poke at it with sickles, hack at it with axes,
Eat it as they please,
What does it matter?"
The sea sprite looked disconsolate, but
I paid it no mind, and slowly swam
Across the sea,
And as the sun was setting, I arrived at my sea.
There I saw
The twelve brothers, the twelve
Sisters, unable to carry the half-whale,
All struggling together, shouting,
Stuck in the east of the sea.
I was truly astonished.
I ignored them and returned home,
And sat upon my platform.
Then, looking back toward the world of humans,
I saw that around the whale
And a half that I had beached, fine men and
Fine women, dressed in finery,
Were rejoicing and dancing over the sea bounty, and on the dunes behind,
A fine mat had been spread,
And upon it, the village chief of Otasutsu,
Wearing six robes, his sash bound tight, six robes
Draped over his shoulders, a fine divine crown, the crown of his ancestors,
Upon his head, a divinely granted sword at his waist,
Looking beautiful as a god, raising his hands high
In worship. The humans were weeping,
Rejoicing over the sea bounty.
The sprite had said that the humans
Were poking at the whale I had beached with
Axes and sickles, but
The village chief and the
Villagers, since ancient times,
Had taken out the divine sword, which they held as the most precious treasure,
And were using it to cut the meat and carry it away.
And my brothers and sisters showed no sign of returning.
Two or three days passed, and then, in the window,
Something seemed to appear.
Turning to look, I saw in the window
A golden cup overflowing
With sake, and upon it
Chopsticks adorned with *gohei*,
Moving back and forth, delivering a message:
"I am from the village of Otasutsu, and
Though it is presumptuous, I offer you this sake."
The village chief of Otasutsu, representing
All the villagers, spoke in detail of his gratitude,
"Tomin karikuru kamui karikuru isoyankekuru,
Great god, brave god, who else
Would have pitied our village, when famine struck
And we were so desperately
Lacking food?
Thank you truly for giving life to our village.
Rejoicing over the sea bounty,
We have made a little sake,
Added a small *nusa*,
And offer our thanks to the great god."
This was what the *gohei*-adorned chopsticks conveyed, moving back and forth.
Then I rose, took the golden cup,
And raised it to my forehead,
Opened the lids of the six sake barrels on the upper seat,
Poured a little of the fine sake into each,
And placed the golden cup in the window.
When that was done, I sat back down on the platform,
And saw that the cup and chopsticks
Were gone. Then, carving
Scabbards, engraving scabbards,
I suddenly looked up,
And the house was filled with beautiful *gohei*,
And white clouds drifted through the house, and white lightning
Flashed and flickered. I thought, "Ah, how beautiful."
Then, two or three days later,
At last, I heard my brothers and
Sisters outside the house, shouting as they
Pulled the whale. I was astonished.
Watching them enter the house,
I saw that my brothers and sisters
Were terribly tired, their faces pale and withered.
They all came in, and seeing the many *gohei*,
Were amazed, and bowed again and again.
Meanwhile, the six sake barrels on the eastern seat
Overflowed, and the scent of the gods' favorite
Sake filled the house.
Then I decorated the house with beautiful *gohei*,
Invited the gods of far and near,
And held a grand feast. My sisters
Boiled the whale, and offered it to the gods,
Who smacked their lips and rejoiced.
As the feast reached its height, I rose
And told in detail how famine had struck the human world,
And how, taking pity, I had beached the sea bounty,
And how, when I had done good to the humans, the wicked gods
Had envied me, and the sea sprite had slandered me,
And how the village chief of Otasutsu had spoken words of gratitude to me,
And how the *gohei*-adorned chopsticks had come as messengers.
Hearing this, the gods
All nodded in unison,
And praised me.
Then, holding another grand feast,
The sounds of the gods
Dancing and leaping here and there
Made a beautiful harmony, and my sisters
Carried *chōshi* and poured sake between the seats,
And sang with the goddesses
In beautiful voices.
Two or three days later, the feast ended.
Giving the gods two or three beautiful *gohei* each,
The gods bent low at the waist,
Bowing again and again,
And all returned to their homes.
After that, always, the long elder brothers, six in all,
The long elder sisters, six in all, the short younger sisters, six in all,
The short younger brothers, six in all, together,
Whenever the humans made sake, they sent sake to me,
And sent *gohei* to my place.
Now, the humans have no lack of food,
No troubles, and live in peace,
So I am at ease.

```
### Another prompt for matched meaning

```
Translate the following text from Japanese to English. Keep the original meanings.
```

### Output of this prompt

```
The sea god himself sang this song, "Atoika Tomatomaki Kuntoteashi Fumu Fumu!"

Atoika Tomatomaki Kuntoteashi Fumu Fumu
Long elder brothers, six elder brothers, long elder sisters, six elder sisters,
Short elder brothers, six elder brothers, short elder sisters, six elder sisters,
Were raising me, but I,
Next to the pile of treasures, built a raised platform, and on that platform
Sat carving scabbards, engraving scabbards,
And that alone
Was my occupation.
Every day, when morning came, my elder brothers
Would shoulder their quivers and go out with my elder sisters,
And when evening came, with tired faces,
They would return empty-handed, and my elder sisters,
Though tired, would prepare the meal, set a tray for me,
And after they themselves had eaten and the meal was cleared away,
Then my elder brothers would busily make arrows.
When the quivers were full, because everyone was tired,
They would sleep, snoring loudly.
The next day, while it was still dark,
Everyone would get up, my elder sisters would prepare the meal and set a tray for me,
And when everyone had finished eating, they would again shoulder their quivers
And go away. Again, in the evening,
With tired faces, they would return empty-handed,
My elder sisters would prepare the meal, my elder brothers would make arrows,
Always doing the same thing.
One day, again, my elder brothers and elder sisters
Shouldered their quivers and went away.
I was carving treasures, but eventually
I got up on the raised platform, took a golden bow
And golden arrows, went outside,
And saw the sea was wide and calm,
And whales were playing, splashing, to the east of the sea and to the west of the sea. Then,
To the east of the sea, the long elder sisters, six elder sisters, joined hands and made a ring,
The short elder sisters, six elder sisters, drove the whales into the ring,
The long elder brothers, six elder brothers, the short elder brothers, six elder brothers,
Aimed and shot at the whales in the ring, and the arrows
Passed under and over the whales.
Every day they did this. Looking, in the center of the sea,
I saw a large whale and its calf playing, splashing, up and down,
So from a distance, I nocked a golden arrow to my golden bow,
Aimed and shot, and with one arrow
Pierced both the whale and its calf at once.
Then I cut the middle of one whale,
And threw half of it into the ring of my elder sisters. Then, with the one and a half whales,
I put them under their tails and headed towards the land of humans,
Arrived at Otasutsu Village,
And pushed the one and a half whales
Up onto the village beach.
Then I slowly
Swam back over the sea,
When someone came running breathlessly beside me,
And I saw it was the sea gull.
Gasping for breath, it said,
"Tominkarukur Kamuykarukur Isoyankekur
Brave god, great god,
Why did you give such a great bounty of the sea to the lowly humans, the bad humans?
The lowly humans, the bad humans, are using axes
And sickles to cut, poke, and
Whittle away at the great bounty of the sea. Brave god,
Great god, please quickly take back
The great bounty of the sea. Even though you gave them so much bounty of the sea,
The lowly humans, the bad humans,
Don't appreciate it and are doing such things."
So I laughed and said,
"I gave it to the humans, so
Now it is theirs. Whether the humans
Poke at their possessions with sickles or
Whittle them away with axes, isn't it fine if they
Eat them as they please?
What's wrong with that?" Then
The sea gull looked lost, but
I didn't mind it at all and slowly swam over the sea,
And when it was almost sunset, I arrived at my sea. Looking,
The twelve elder brothers, the twelve
Elder sisters, were carrying that half whale,
Unable to carry it, all together, shouting loudly,
Struggling in the east of the sea.
I was truly amazed.
I didn't mind them and went home,
And sat on the raised platform.
Then, looking back towards the world of humans,
I saw that around the one and a half
Whales that I had beached, splendid men and
Splendid women were dressed in finery,
Joyfully dancing for the bounty of the sea, rejoicing and leaping, and on the dunes behind,
A splendid mat was spread,
And on it, the village chief of Otasutsu Village,
With six kimonos and a bundled sash, wearing six kimonos,
Wearing a splendid god's crown, an ancestral crown,
On his head, wearing a divinely granted sword at his waist,
Looking as beautiful as a god, raising his hands high,
Worshipping. The humans were crying,
Rejoicing at the bounty of the sea.
What the gull said, that the humans were
Poking at the whale I had beached with axes and sickles,
Was not true. The village chief and
The villagers, since long ago,
Took out the divine sword, which they considered the most precious of treasures,
And used it to cut the meat and carry it.
And then, my elder brothers and elder sisters showed no sign of returning.
Two or three days passed, and something seemed to be visible in the window, so
I turned around and looked, and on the window,
There was a golden cup overflowing
With sake, and on top of it,
There were sake chopsticks with gohei attached,
Going back and forth, stating their message as envoys, saying,
"I am a person from Otasutsu Village, and
Though it is presumptuous, I offer you sake." And
The village chief of Otasutsu Village, representing
All the villagers, spoke in detail about the circumstances of offering thanks to me,
"Tominkarukur Kamuykarukur Isoyankekur
Great god, brave god, who else but you
Would have pitied our village, where there was a famine
And we were so desperately
Lacking food?
Thank you very much for giving life to our village.
Rejoicing at the bounty of the sea, we have made a little sake,
Added a small nusa,
And are offering our thanks to the great god."
The sake chopsticks with gohei attached stated this, going back and forth.
So I got up, took the golden cup,
Humbly received it,
Opened the lids of the six sake barrels on the upper seat,
Poured a little fine sake into each,
And placed the golden cup on the window.
When that was done, I sat down on the raised platform,
And saw that the cup had disappeared, along with the chopsticks. Then, carving scabbards,
Engraving scabbards, and eventually,
Suddenly raising my face,
I saw that the house was full of beautiful gohei,
And white clouds were drifting in the house, and white lightning
Was flashing. I thought, "Ah, how beautiful."
Then again, two or three days passed,
And at that time, finally, outside the house, my elder brothers and
Elder sisters began to be heard, shouting loudly, pulling
The whale. I was amazed.
Looking at how they entered the house,
My elder brothers and elder sisters were
Very tired, and their faces were withered.
Everyone came in, and when they saw the many gohei,
They were surprised and bowed many times.
Meanwhile, the six sake barrels on the eastern seat
Were overflowing, and the scent of the god's favorite
Sake drifted through the house.
Then I decorated the house with beautiful gohei,
Invited the gods of distant places and the gods of nearby places,
And held a grand banquet. My elder sisters
Boiled the whale and offered it to the gods,
And the gods smacked their lips and rejoiced.
When the banquet was at its height, I got up
And told in detail how there was a famine in the human world,
And feeling pity, I had beached the bounty of the sea,
And how the bad gods, envying me for treating the humans well,
Had slandered me through the sea gull, and how the
Village chief of Otasutsu Village had taken those words and offered thanks to me,
And how the sake chopsticks with gohei attached had come as envoys.
The gods all nodded in unison,
Praising me.
Then again, we held a grand banquet,
And the sounds of the gods
Dancing and leaping here and there
Made a beautiful sound, and my elder sisters
Carried choshi and went around pouring sake between the seats,
And sang with beautiful voices along with the goddesses.
Two or three days passed, and the banquet closed.
When I gave the gods two or three beautiful gohei each,
The gods bent their waists
With a creak and bowed many times,
And everyone returned to their own homes.
After that, as always, the long elder brothers, six elder brothers,
The long elder sisters, six elder sisters, the short elder sisters, six elder sisters,
The short elder brothers, six elder brothers, together,
Whenever the humans made sake, they would
Send sake to me and send gohei to my place.
Now, the humans no longer lack food
And have no troubles, living in peace,
So I am at ease.

```