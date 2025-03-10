# LLM-assisted Translation project of Ainu shin'yoshu (アイヌ神謡集) collected by Chiri Yukie 知里幸惠 (1903 - 1922).

## English Translation of

## Kamuichikap kamui yaieyukar, “Shirokanipe ranran pishkan” 梟の神の自ら歌った謡「銀の滴しずく降る降るまわりに」

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
Translate the following text from Japanese to English. The original text is a chant sung by god telling his story. Try to make the translation also look like a chant but keep the original meanings.

梟の神の自ら歌った謡
「銀の滴しずく降る降るまわりに」

「銀の滴降る降るまわりに,金の滴
降る降るまわりに.」という歌を私は歌いながら
流に沿って下り,人間の村の上を
通りながら下を眺めると
昔の貧乏人が今お金持になっていて,昔のお金持が
今の貧乏人になっている様です.
海辺に人間の子供たちがおもちゃの小弓に
おもちゃの小矢をもってあそんで居ります.
「銀の滴降る降るまわりに
金の滴降る降るまわりに.」という歌を
歌いながら子供等の上を
通りますと,(子供等は)私の下を走りながら
云うことには,
「美しい鳥! 神様の鳥!
さあ,矢を射てあの鳥
神様の鳥を射当てたものは,一ばんさきに取った者は
ほんとうの勇者,ほんとうの強者だぞ.」
云いながら,昔貧乏人で今お金持になってる者の
子供等は,金の小弓に金の小矢を
番つがえて私を射ますと,金の小矢を
私は下を通したり上を通したりしました.
その中に,子供等の中に
一人の子供がただの(木製の)小弓にただの小矢
を持って仲間にはいっています.私はそれを見ると
貧乏人の子らしく,着物でも
それがわかります.けれどもその眼色を
よく見ると,えらい人の子孫らしく,一人変り
者になって仲間入りをしています.自分もただの小弓に
ただの小矢を番えて私をねらいますと,
昔貧乏人で今お金持の子供等は大笑いをして
云うには,
「あらおかしや貧乏の子
あの鳥,神様の鳥は私たちの
金の小矢でもお取りにならないものを,お前の様な
貧乏な子のただの矢腐れ木の矢を
あの鳥,神様の鳥がよくよく
取るだろうよ.」
と云って,貧しい子を足蹴にしたり
たたいたりします.けれども貧乏な子は
ちっとも構わず私をねらっています.
私はそのさまを見ると,大層不憫に思いました.
「銀の滴降る降るまわりに,
金の滴降る降るまわりに.」という歌を
歌いながらゆっくりと大空に
私は輪をえがいていました.貧乏な子は
片足を遠く立て片足を近くたてて,
下唇をグッと噛みしめて,ねらっていて
ひょうと射放しました.小さい矢は美しく飛んで
私の方へ来ました,それで私は手を
差しのべてその小さい矢を取りました.
クルクルまわりながら私は
風をきって舞い下りました.
すると,彼かの子供たちは走って
砂吹雪をたてながら競争しました.
土の上に私が落ちると一しょに,一等先に
貧乏な子がかけついて私を取りました.
すると,昔貧乏人で今は金持になってる者の
子供たちは後から走って来て
二十も三十も悪口をついて
貧乏な子を押したりたたいたり
「にくらしい子,貧乏人の子
私たちが先にしようとする事を先がけしやがって.」
と云うと,貧乏な子は,私の上に
おおいかぶさって,自分の腹にしっかりと私を押えていました.
もがいてもがいてやっとの事,人の隙から
飛び出しますと,それから,どんどんかけ出しました.
昔は貧乏人で今は金持の子供等が
石や木片を投げつけるけれど
貧乏な子はちっとも構わず
砂吹雪をたてながらかけて来て一軒の小屋の
表へ着きました.子供は
第一の窗から私を入れて,それに
言葉を添え,斯々かくかくのありさまを物語りました.
家の中から老夫婦が
眼の上に手をかざしながらやって来て
見ると,大へんな貧乏人ではあるけれども
紳士らしい淑女らしい品をそなえています,
私を見ると,腰の央なかをギックリ屈めて,ビックリしました.
老人はキチンと帯をしめ直して,
私を拝し
「ふくろうの神様,大神様,
貧しい私たちの粗末な家へ
お出で下さいました事,有難う御座います.
昔は,お金持に自分を数え入れるほどの者で
御座いましたが今はもうこの様に
つまらない貧乏人になりまして,国の神様
大神様をお泊め申すも
畏れ多い事ながら今日はもう
日も暮れましたから,今宵は大神様を
お泊め申し上げ,明日は,ただイナウだけでも
大神様をお送り申し上げましょう.」という事を
申しながら何遍も何遍も礼拝を重ねました.
老婦人は,東の窗の下に
敷物をしいて私をそこへ置きました.
それからみんな寝ると直ぐに高いびきで
寝入ってしまいました.
私は私の体の耳と耳の間に坐って
いましたがやがて,ちょうど,真夜中時分に
起き上りました.
「銀の滴降る降るまわりに,
金の滴降る降るまわりに.」
という歌を静かにうたいながら
この家の左の座へ右の座へ
美しい音をたてて飛びました.
私が羽ばたきをすると,私のまわりに
美しい宝物,神の宝物が美しい音をたてて
落ち散りました.
一寸のうちに,この小さい家を,りっぱな宝物
神の宝物で一ぱいにしました.
「銀の滴降る降るまわりに,
金の滴降る降るまわりに.」
という歌をうたいながらこの小さい家を
一寸の間にかねの家,大きな家に
作りかえてしまいました,家の中は,りっぱな宝物の積場
を作り,りっぱな着物の美しいのを
早つくりして家の中を飾りつけました.
富豪の家よりももっとりっぱにこの大きな家の
中を飾りつけました.私はそれを終ると
もとのままに私の冑の
耳と耳の間に坐っていました.
家の人たちに夢を見せて
アイヌのニシパが運が悪くて貧乏人になって
昔貧乏人で今お金持になっている者たちに
ばかにされたりいじめられたりしてるさまを私が見て
不憫に思ったので,私は身分の卑しいただの神では
ないのだが,人間の家
に泊って,恵んでやったのだという事を
知らせました.
それが済んで少したって夜が明けますと
家の人々が一しょに起きて
目をこすりこすり家の中を見るとみんな
床の上に腰を抜かしてしまいました.老婦人は
声を上げて泣き,老人は
大粒の涙をポロポロこぼして
いましたが,やがて,老人は起き上り
私の処へ来て,二十も三十も礼拝
を重ねて,そして云う事には,
「ただの夢ただの眠りをしたのだと
思ったのに,ほんとうに,こうしていただいた事.
つまらないつまらない,私共の粗末な家に
お出で下さるだけでも有難く存じますものを
国の神様,大神様,私たちの不運な
事を哀れんで下さいまして
お恵みのうちにも最も大きいお恵みをいただき
ました事.」と云う事を泣きながら
申しました.
それから,老人はイナウの木をきり
りっぱなイナウを美しく作って私を飾りました.
老婦人は身仕度をして
小さい子を手伝わせ,薪をとったり
水を汲んだりして,酒を造る仕度をして,一寸の間に
六つの酒樽を上座にならべました.
それから私は火の老女,老女神と
種々な神の話を語り合いました.
二日程たつと,神様の好物ですから
はや,家の中に酒の香が
漂いました.
そこで,あの小さい子に態わざと
古い衣物を着せて,村中の
昔貧乏人で今お金持になっている人々を
招待するため使いに出してやりました.ので
後見送ると,子供は家毎に
入って使いの口上を述べますと
昔貧乏人で今お金持になっている人々は
大笑いをして
「これはふしぎ,貧乏人どもが
どんな酒を造ってどんな
御馳走があってそのため人を招待するのだろう,
行ってどんな事があるか見物して
笑ってやりましょう.」と
言い合いながら大勢打ち連れて
やって来て,ずーっと遠くから,ただ家を見ただけで
驚いてはずかしがり,そのまま帰る者もあります,
家の前まで来て腰を抜かしているのもあります.
すると,家の夫人が外へ出て
人皆の手を取って家へ入れますと,
みんないざり這いよって
顔を上げる者もありません.
すると,家の主人は起き上って
カッコウ鳥の様な美しい声で物を言いました.
斯々かくかくの訳を物語り
「この様に,貧乏人でへだてなく
互に往来も出来なかったのだが
大神様があわれんで下され,何の悪い考えも
私どもは持っていませんのでしたのでこの様に
お恵みをいただきましたのですから
今から村中,私共は一族の者
なんですから,仲善くして
互に往来をしたいという事を皆様に
望む次第であります.」という事を
申し述べると,人々は
何度も何度も手をすりあわせて
家の主人に罪を謝し,これからは
仲よくする事を話し合いました.
私もみんなに拝されました.
それが済むと,人はみな,心が柔らいで
盛んな酒宴を開きました.
私は,火の神様や家の神様や
御幣ごへい棚の神様と話し合いながら
人間たちの舞を舞ったり躍りをしたりするさまを
眺めて深く興がりました.そして
二日三日たつと酒宴は終りました.
人間たちが仲の善いありさまを
見て,私は安心をして
火の神,家の神
御幣棚の神に別れを告げました.
それが済むと私は自分の家へ帰りました.
私の来る前に,私の家は美しい御幣
美酒が一ぱいになっていました.
それで近い神,遠い神に
使者をたてて招待し,盛んな酒宴を
張りました,席上,神様たちへ
私は物語り,人間の村を訪問した時の
その村の状況,その出来事を詳しく話しますと
神様たちは大そう私をほめたてました.
神様たちが帰る時に美しい御幣を
二つやり三つやりしました.
彼かのアイヌ村の方を見ると,
今はもう平穏で,人間たちは
みんな仲よく,彼のニシパが
村に頭になっています,
彼の子供は,今はもう,成人
して,妻ももち子も持って
父や母に孝行をしています,
何時でも何時でも,酒を造った時は
酒宴のはじめに,御幣やお酒を私に送ってよこします.
私も人間たちの後に坐して
何時でも
人間の国を守護まもっています.
と,ふくろうの神様が物語りました.
```

### Output
```
Here is the translation of the text, attempting to maintain the chant-like quality and original meaning:

**The Owl God's Own Song**

"Silver drops fall, fall around,
Silver drops fall, fall around, golden drops
Fall, fall around." So I sang,
Down the river I flowed, above the villages of men,
Looking down, I saw,
The once poor now rich, the once rich now poor, it seems.
By the shore, children of men, with toy bows,
With toy arrows, they play.

"Silver drops fall, fall around,
Golden drops fall, fall around." So I sang,
Passing above the children,
They ran beneath me, saying,
"A beautiful bird! A god's bird!
Come, shoot the arrow!
He who hits the god's bird first,
He is the true hero, the true strong one!"

Saying this, the children of the once poor, now rich,
With golden bows and golden arrows,
They aimed and shot at me, the golden arrows
I let pass above, I let pass below.
Among them, among the children,
One child with a simple (wooden) bow, a simple arrow,
Joined the group. Seeing him,
Like a child of the poor, his clothes
Revealed it. But looking closely at his eyes,
Like a descendant of the great, a singular
Being, he joined the group. He too, with a simple bow,
A simple arrow, aimed at me,
The children of the once poor, now rich, laughed loudly,
Saying,

"How funny, child of the poor!
That bird, the god's bird, will not take
Our golden arrows,
Will that bird, the god's bird, ever
Take your simple, rotten-wood arrow,
Child of the poor?"
And they kicked and struck the poor child. But the poor child,
Unfazed, aimed at me.
Seeing this, I felt great pity.
"Silver drops fall, fall around,
Golden drops fall, fall around." So I sang,
Slowly in the great sky,
I drew a circle. The poor child,
One foot far, one foot near,
Biting his lower lip, aiming,
He let fly! The small arrow flew beautifully,
Coming toward me, so I reached out my hand,
And took the small arrow.
Spinning, I
Cut through the wind, descending.
Then, the children ran,
Raising sandstorms as they raced.
As I fell to the earth, together, first,
The poor child rushed and took me.
Then, the children of the once poor, now rich,
Ran up from behind,
Twenty, thirty insults they hurled,
Pushing and striking the poor child,
"Hateful child, child of the poor!
You took what we were going to take!"
The poor child, covering me,
Pressed me firmly to his belly.
Struggling, struggling, finally, from the gaps between people,
He burst out, then ran and ran.
The children of the once poor, now rich,
Threw stones and pieces of wood, but
The poor child, unfazed,
Ran, raising sandstorms, to the front of a small hut. The child
Put me through the first window, and with
Words, told the story of what had happened.
From inside the house, an old couple,
Shading their eyes, came out,
Though very poor,
They possessed the grace of a gentleman and lady.
Seeing me, they bent low at the waist, surprised.
The old man straightened his belt,
And worshipped me,
"Owl God, Great God,
Thank you for coming to our humble home.
Once, we counted ourselves among the rich,
But now we are such insignificant poor,
To lodge the country's god,
The Great God, is a daunting thing, but tonight,
Since the day is already done, tonight we will
Lodge the Great God, and tomorrow, with just inau,
We will send the Great God on his way."
Saying this, he bowed again and again.
The old woman, beneath the east window,
Laid a mat and placed me there.
Then everyone went to sleep, immediately snoring
Loudly.
I, sitting between my body's ears,
Soon, around midnight,
Arose.
"Silver drops fall, fall around,
Golden drops fall, fall around."
Singing quietly,
To the left of this house, to the right,
I flew, making beautiful sounds.
As I flapped my wings, around me,
Beautiful treasures, god's treasures, fell,
Scattering with beautiful sounds.
In an instant, this small house, with magnificent treasures,
God's treasures, I filled it.
"Silver drops fall, fall around,
Golden drops fall, fall around."
Singing, this small house,
In an instant, into a house of gold, a large house,
I transformed it, inside the house, a storehouse of magnificent treasures
I created, and beautiful, magnificent clothes
I quickly made, decorating the house.
More magnificent than a rich man's house, this large house
I decorated inside. When I finished,
As before, between my helmet's
Ears, I sat.
To the people of the house, I showed a dream,
That the Ainu Nishpa, unlucky and poor,
Was scorned and bullied by those who were once poor and now rich,
And seeing this, I felt pity, so I, a humble, simple god,
Not a great one, stayed in a human house,
And bestowed blessings, I let them know.
When that was done, after a while, as the night turned to dawn,
The people of the house woke together,
Rubbing their eyes, looking inside the house, everyone
Collapsed onto the floor. The old woman
Cried out, and the old man
Shed large tears,
But soon, the old man rose,
Came to me, bowed twenty, thirty times,
And then said,
"I thought it was just a dream, just sleep,
But it really happened.
Insignificant, insignificant, just coming to our humble home
Is something we are grateful for,
Country's god, Great God, pitying
Our misfortune,
You have given us the greatest of blessings."
Saying this, he spoke while crying.
Then, the old man cut inau wood,
Made magnificent inau beautifully, and decorated me.
The old woman dressed,
Helped by the small child, gathering firewood,
Drawing water, preparing to make sake, in an instant
Six sake barrels she lined up in the upper seat.
Then I spoke with the old woman of fire, the old goddess, and
Various gods.
After two days, because it is the gods' favorite,
Soon, the scent of sake
Filled the house.
So, to that small child, I deliberately
Put old clothes on, and to the village,
To invite the people who were once poor and now rich,
I sent him as a messenger.
Seeing him off, the child, house by house,
Entered and delivered the message,
The people who were once poor and now rich
Laughed loudly,
"This is strange, what kind of sake
Will the poor make, what kind of
Feast will there be, that they invite people?
Let's go see what's happening, and
Laugh at them."
Saying this, many came together,
And from far away, just seeing the house,
They were surprised and ashamed, some even returned,
Some came to the front of the house and collapsed.
Then, the woman of the house came outside,
Took everyone's hand and brought them into the house,
Everyone crawled in,
Some didn't even raise their faces.
Then, the master of the house rose,
And spoke in a beautiful voice like a cuckoo bird.
He told the story of what had happened,
"Like this, as poor people, we could not
Visit each other freely,
But the Great God pitied us, and because we had no bad thoughts,
We received this blessing,
So from now on, in the village, we are all family,
So I wish for everyone to be friendly
And visit each other."
Saying this,
The people rubbed their hands together again and again,
Apologized to the master of the house, and from now on
They talked about being friendly.
I too was worshipped by everyone.
When that was done, everyone's hearts softened,
And they held a grand sake feast.
I, talking with the fire god, the house god, and
The gods of the gohei shelf,
Watched the humans dance and leap,
And was deeply delighted. And
After two or three days, the sake feast ended.
Seeing the humans being friendly,
I felt relieved,
And bid farewell to the fire god, the house god,
And the gods of the gohei shelf.
When that was done, I returned to my own house.
Before I came, my house was filled with beautiful gohei,
And fine sake.
So, to the near gods, the far gods,
I sent messengers to invite them, and held a grand sake feast.
At the feast, to the gods,
I told the story, of when I visited the human village,
The situation of that village, the events that happened, in detail,
And the gods praised me greatly.
When the gods returned, beautiful gohei
Two or three I gave them.
Looking toward that Ainu village,
Now it is peaceful, and the humans
Are all friendly, and that Nishpa
Is the head of the village.
His child, now grown,
Has a wife and children,
And is filial to his father and mother.
Whenever, whenever, when they make sake,
At the beginning of the sake feast, gohei and sake
They send to me.
I too, sitting behind the humans,
Always
Protect the human country.
So, the owl god told the story.

```
### Another prompt for matched meaning

```
Translate the following text from Japanese to English. The original text is a chant sung by god telling his story. Use a story telling tone. Keep the original meanings.
```

### Output of this prompt

```
This is the song of the Owl God, sung by himself:

"Silver drops fall, fall all around,
Golden drops fall, fall all around."

Singing this song, I descended along the river, passing over a human village. Looking down, I saw that the poor of old had become rich, and the rich of old had become poor.

By the seaside, human children were playing with toy bows and arrows.

"Silver drops fall, fall all around,
Golden drops fall, fall all around."

As I passed over the children, they ran beneath me, shouting,

"A beautiful bird! A god's bird!
Come, shoot it with arrows!
Whoever shoots down that bird, that god's bird, and takes it first, is a true hero, a true strong one!"

The children of those who were once poor but now rich nocked golden arrows to golden bows and shot at me. I let the golden arrows pass above and below me.

Among the children, one held only a simple wooden bow and arrow, joining the others. I could tell he was the child of a poor man by his clothes. But looking closely at his eyes, I saw the bearing of a noble descendant, a lone wolf among the group. He, too, nocked his simple arrow to his simple bow and aimed at me.

The children of those who were once poor but now rich laughed loudly, saying,

"How funny, the poor man's child!
That bird, that god's bird, wouldn't even take notice of our golden arrows. Why would it ever take notice of your rotten wooden arrow, you poor child?"

They kicked and hit the poor child. But he paid them no mind, continuing to aim at me.

Seeing this, I felt great pity for him.

"Silver drops fall, fall all around,
Golden drops fall, fall all around."

Singing this song, I slowly circled in the vast sky. The poor child stood with one foot far back and one foot close, biting his lower lip, and released his arrow. The small arrow flew beautifully towards me, and I reached out my hand and caught it.

Spinning and twirling, I cut through the wind and descended.

The children ran, kicking up a sandstorm as they raced. As I landed on the ground, the poor child was the first to reach me and take hold of me.

Then, the children of those who were once poor but now rich ran up, hurling insults by the score, pushing and hitting the poor child.

"Hateful child, poor man's child! You dared to take what we were going to take!"

The poor child covered me with his body, holding me tightly against his stomach.

Struggling and wriggling, he finally broke free from the crowd and ran as fast as he could.

The children of those who were once poor but now rich threw stones and pieces of wood at him, but the poor child paid them no mind, running through the sandstorm until he reached the front of a small hut. The child slipped me through the first window, adding words to me, telling the story of what had happened.

From inside the house, an old couple came out, shading their eyes with their hands. They were terribly poor, but possessed the grace of a gentleman and a lady. When they saw me, they bowed deeply at the waist, startled.

The old man straightened his belt and bowed to me, saying,

"Owl God, Great God, thank you for coming to our humble home. We were once wealthy enough to count ourselves among the rich, but now we are mere paupers. It is presumptuous to offer lodging to the god of the land, the Great God, but as the day is already done, we will offer you lodging for tonight. Tomorrow, we will send you off with only inau."

He repeated his bows many times.

The old woman laid a mat beneath the east window and placed me there.

Soon, everyone went to sleep, snoring loudly.

I sat between the ears on my head, and then, right around midnight, I awoke.

"Silver drops fall, fall all around,
Golden drops fall, fall all around."

Singing this song softly, I flew with a beautiful sound from the left side of the house to the right.

As I flapped my wings, beautiful treasures, divine treasures, fell and scattered around me with a beautiful sound.

In an instant, I filled the small house with magnificent treasures, divine treasures.

"Silver drops fall, fall all around,
Golden drops fall, fall all around."

Singing this song, I transformed the small house into a house of gold, a grand house, in an instant. I created a storehouse of magnificent treasures inside, and quickly fashioned beautiful, splendid clothes to decorate the house.

I decorated the inside of this grand house even more splendidly than a wealthy man's home. When I was finished, I returned to my place between the ears on my helmet.

I showed the people in a dream how the Ainu Nishpa had been unlucky and become poor, and how I had seen him being ridiculed and bullied by those who were once poor but now rich, and felt pity for him. I let them know that I was not just any god, but a god of high status, and that I had stayed in their human home and bestowed blessings upon them.

After that, as dawn approached, the people woke up together. Rubbing their eyes, they looked around the house and all collapsed onto the floor. The old woman cried out, and the old man shed large tears. But then, the old man stood up and came to me, bowing twenty or thirty times, and said,

"We thought it was just a dream, just sleep, but it really happened. It is too much, too much. We are grateful just for you coming to our humble home, but the god of the land, the Great God, has taken pity on our misfortune and bestowed upon us the greatest of blessings."

He said this while weeping.

Then, the old man cut down a tree for inau and made beautiful, splendid inau to decorate me.

The old woman dressed herself and had the small child help her gather firewood and draw water, preparing to make sake. In an instant, she lined up six sake barrels in the upper seat.

Then, I talked with the old woman of fire, the old goddess, and various other gods.

After two days, the scent of sake filled the house, as it is a favorite of the gods.

So, they deliberately dressed the small child in old clothes and sent him out to invite the people in the village who were once poor but now rich.

As they watched him go, the child entered each house and delivered his message. The people who were once poor but now rich laughed loudly, saying,

"This is strange. What kind of sake and what kind of feast could those poor people be making that they would invite people? Let's go see what's going on and laugh at them."

They gathered together and came to the house. From far away, just seeing the house, some were surprised and ashamed, and went home. Others came to the front of the house and collapsed in shock.

Then, the woman of the house came outside, took everyone's hand, and led them into the house. Everyone crawled in, unable to lift their faces.

Then, the master of the house stood up and spoke in a beautiful voice like a cuckoo bird. He told the story of what had happened, saying,

"Like this, we were poor and unable to visit each other freely, but the Great God took pity on us. We had no bad intentions, so we received these blessings. From now on, we are all members of the same family in this village, so I hope that we can be friendly and visit each other."

The people rubbed their hands together many times and apologized to the master of the house for their sins, and discussed becoming friends from now on.

I was also worshipped by everyone.

When that was done, everyone's hearts softened and they held a grand feast.

I talked with the god of fire, the god of the house, and the god of the sacred shelf, watching the humans dance and leap, and was deeply amused. And after two or three days, the feast ended.

Seeing the humans being friendly with each other, I felt relieved and said goodbye to the god of fire, the god of the house, and the god of the sacred shelf.

When that was done, I returned to my own home.

Before I arrived, my house was filled with beautiful sacred treasures and fine sake.

So, I sent messengers to the gods near and far, inviting them to a grand feast. At the feast, I told the gods in detail about the situation in the human village when I visited it, and the events that had occurred. The gods praised me greatly.

When the gods left, I gave them two or three beautiful sacred treasures each.

Looking towards that Ainu village, it is now peaceful, and the humans are all friendly. That Nishpa is now the head of the village.

His child has now grown up, has a wife and children, and is filial to his parents.

Whenever they make sake, they always send me sacred treasures and sake at the beginning of the feast.

I sit behind the humans and always protect the human country.

So, the Owl God told his story.

```