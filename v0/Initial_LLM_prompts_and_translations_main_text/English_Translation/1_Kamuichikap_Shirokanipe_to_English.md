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
Translate the following text from Japanese to English. The original text is a Japanese translation of a Ainu chant, sung by Ainu god telling his story. 
Use story-telling and poetic tone. Keep the original Japanese meaning accurately. Use modern and simple English.
If a term cannot be translated, keep the original language.

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
The Owl God's Own Song:
"Silver drops fall, fall around me."

Singing the song, "Silver drops fall, fall around me, golden drops fall, fall around me," I descended along the river, passing over a human village. Looking down, I saw the once poor now rich, and the once rich now poor.

Children played on the beach with toy bows and arrows. As I passed over them, singing, "Silver drops fall, fall around me, golden drops fall, fall around me," they ran beneath me, crying out:

"A beautiful bird! A god's bird! Come, shoot it down! Whoever hits the god's bird first is the true hero, the true strong one!"

The children of the newly rich, with golden bows and golden arrows, aimed at me. I dodged their golden arrows, flying above and below. Among them, one child stood apart, with a simple wooden bow and arrow. I could see he was poor, even in his clothes. Yet, in his eyes, I saw the lineage of greatness, a unique spirit among them. He, too, aimed his simple bow and arrow at me.

The children of the newly rich laughed, saying, "How foolish, poor child! The bird, the god's bird, won't even take notice of our golden arrows. Why would it ever care for your rotten wooden arrow?"

They kicked and shoved the poor child, but he paid them no mind, focusing on me. Seeing this, I felt a deep pity.

Singing, "Silver drops fall, fall around me, golden drops fall, fall around me," I slowly circled in the sky. The poor child stood with one foot forward and one back, biting his lip in concentration, and released his arrow. The small arrow flew beautifully towards me, and I reached out and caught it.

Spinning, I danced on the wind and descended. The children raced, kicking up dust in their wake. As I landed on the ground, the poor child reached me first and took me in his hands.

The children of the newly rich ran up, showering him with insults, pushing and hitting him. "Hateful child, poor child! You dared to take what we wanted first!" The poor child shielded me with his body, holding me tightly to his chest.

Struggling, he finally broke free and ran, the children of the newly rich throwing stones and wood after him. He didn't falter, running through the dust to a small hut. He slipped me through the first window, telling the story of what had happened.

From inside, an old couple came, shading their eyes. Though they were poor, they carried themselves with the grace of a gentleman and lady. Seeing me, they bowed deeply in surprise. The old man straightened his belt and prayed to me.

"Owl God, Great God, thank you for visiting our humble home. We were once counted among the wealthy, but now we are poor. It is an honor to host you, but as night has fallen, we offer you shelter for tonight. Tomorrow, we will send you off with only inaw, though it is not enough."

He repeated his prayers many times. The old woman laid a mat beneath the east window and placed me there. Soon, they were all asleep, snoring loudly.

I sat between my ears, on my head, and awoke near midnight. Singing softly, "Silver drops fall, fall around me, golden drops fall, fall around me," I flew from the left side of the house to the right, making beautiful sounds.

As I flapped my wings, beautiful treasures, god's treasures, fell around me with a melodious sound. In an instant, I filled the small house with magnificent treasures, god's treasures.

Singing, "Silver drops fall, fall around me, golden drops fall, fall around me," I transformed the small house into a house of gold, a grand mansion. I created a storehouse of magnificent treasures and adorned the house with beautiful, newly made clothes.

I decorated the grand mansion even more splendidly than the homes of the wealthy. When I was finished, I returned to my place between my ears, on my head.

I showed the family a dream, revealing that I had seen the Ainu nishpa, unlucky and poor, being mocked and bullied by the newly rich. I pitied him, and though I am not a god of high status, I stayed in their human home and bestowed blessings upon them.

As dawn approached, the family awoke together. Rubbing their eyes, they looked around the house and were stunned. The old woman cried out, and the old man shed large tears. Finally, the old man rose and came to me, offering many prayers. He said,

"We thought it was just a dream, but it is real! It is already an honor for you to visit our humble home, Great God. You have pitied our misfortune and bestowed upon us the greatest of blessings!" He spoke through his tears.

Then, the old man cut inaw wood and crafted beautiful inaw to adorn me. The old woman prepared herself and had the young child help her gather firewood and water, preparing to brew sake. In an instant, six sake barrels were lined up in the place of honor.

I spoke with the old woman of fire, the old goddess, and various other gods.

After two days, the scent of sake filled the house, a favorite of the gods. The child, dressed in old clothes, was sent to invite the newly rich from the village. As they watched him go, the child entered each house and delivered the message.

The newly rich laughed, saying, "How strange! What kind of sake and feast could the poor have to offer? Let's go see what's happening and have a laugh!"

They came in a large group, but some were so shocked and ashamed by the sight of the house that they turned back. Others came to the front of the house and were too stunned to move.

The woman of the house came out and took each of their hands, inviting them inside. They crawled in, unable to lift their faces.

The master of the house rose and spoke with a voice as beautiful as a cuckoo bird. He told them the story, saying, "We were poor and unable to associate with each other, but the Great God has pitied us. We had no ill intentions, and so we have received these blessings. From now on, we are all family in this village, and I hope we can all be friends and visit each other."

The people repeatedly clasped their hands together and apologized to the master of the house, promising to be friends from now on. They also prayed to me.

With softened hearts, they began a grand feast. I watched the humans dance and sing, conversing with the fire god, the house god, and the god of the altar, and I was deeply pleased. After two or three days, the feast ended.

Seeing the humans living in harmony, I felt at peace. I bid farewell to the fire god, the house god, and the god of the altar. Then, I returned to my home.

Before I arrived, my house was filled with beautiful gohei and fine sake. I sent messengers to the near and far gods, inviting them to a grand feast. At the feast, I told the gods about my visit to the human village and the events that had transpired. The gods praised me greatly.

As the gods departed, I gave them two or three beautiful gohei each.

Looking towards the Ainu village, I saw that it was now peaceful, and the humans were all friends. The nishpa was now the head of the village.

His child had grown into an adult, with a wife and children, and was devoted to his parents. Whenever they brewed sake, they would send gohei and sake to me at the beginning of the feast.

I sit behind the humans, always protecting the human land.

So, the Owl God told his story.
```
