# LLM-assisted Translation project of Ainu shin'yoshu (アイヌ神謡集) collected by Chiri Yukie 知里幸惠 (1903 - 1922).

## English Translation of

## Nitatorunpe yaieyukar, “Harit kunna” 谷地の魔神が自ら歌った謡「ハリツ クンナ」

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

谷地の魔神が自ら歌った謡「ハリツ クンナ」

ハリツ クンナ
ある日に好いお天気なので
私の谷地に眼と口とだけ
出して見ていたところが
ずっと浜の方から人の話し声がきこえて来た.
見ると,二人の若者が連れだって来た.
先に来た者は勇者らしく勇者の品を
そなえて,神の様に美しいが
後から来た者を見ると,様子の悪い
顔色の悪い男で,何か話し合いながら
やって来たが私の谷地の側を通り
ちょうど私の前へ来ると,あとから来た顔色の悪い男が
立ち止り立ち止り自分の鼻をおおい
「おお臭い,いやな谷地,悪い谷地の前を通ったら
まあ汚い,何だろうこんなに臭いのは.」
と言った.
私はただ聞いたばかりだけれど自分の居るか居ないかも
わからぬほど腹が立った.
泥の中から飛び出した.私が飛び上ると
地が裂け地が破れる.牙を
鳴らしながら,彼等を強く追っかけたところが
先に来た者は,それと見るや
魚がクルリとあとへかえる様に引っかえして顔色の悪い男の
わきの下をくぐりずーっと逃げてしまった.
青い男を二間三間追っかけると
直ぐ追いついて頭から呑んでしまった.
そこで今度は彼かの男をありったけの速力で追っかけて来て
人間の村,大きな村の後へ着いた.
見るとむこうから
火の老女,神の老女があかい着物,六枚の着物に
帯をしめ,六枚の着物を羽織って
あかい杖をついて私の側へ飛んで来た.
「これはこれは,お前は何しにこのアイヌ村へ
来るのか,さあお帰り,さあお帰り.」
言いながら,あかい杖,かねの杖をふり上げて私を
たたくと,杖から焔が
私の上へ雨の様に降って来る.
けれども私はちっとも構わず,
牙打ち鳴らしながら彼の男を
追っかけると,彼の男は村の中を
よくまわる環の様に走って行く.そのあとを飛んで
行くと,大地が裂け大地が破れる.村中は大さわぎ
妻の手を引く者,子の手を引く者,泣き叫び
逃げゆくもの,煮えくりかえるようなありさま,けれども
私は少しも構わず,土吹雪
をたてる,火の老女神は私の側を走って来ると
大へんな焔が,私の上に飛び交う.
その中に,彼の男は一軒の家に
飛び込むと直ぐにまた飛び出した.
見ると,蓬の小弓に蓬の小矢をつがえて
むこうから,ニコニコして,私をねらっている.
それを見て私は可笑しく思った.
「あんな小さな蓬の矢,何で人が苦しむものか.」と
思いながら私は牙を打ち鳴らして,
頭から呑もうとしたら
その時彼の男は私の首ッ玉を
したたかに射た.それっきりどうしたか
わからなくなってしまった.
ふと気がついて見たところが
大きな竜の耳と耳の間に私はいた.
村の人々が集って,彼かの私が追っかけた若者が
大声で指図さしずをして,私の屍体をみんな細かに刻み
一つ所へ運んで焼いてその灰を
山の岩の岩の後へ捨ててしまった.
今になってはじめて見ると,それは,ただの人間
ただの若者だと思ったのは
オキキリムイ,神の勇者であった.
恐しい悪い神,悪魔神,私はそれであって
人間の村の近くにいるので,
オキキリムイは村の為を思って,私をおこらせ
自分を追いかけさせて,蓬の矢で私を殺したので
あった.それから,先に私が呑んでしまった
青い男は,人間だと思ったのだったが
それは,オキキリムイがその放糞を人に作り,
それを連れて来たのであった.
私は魔神であったから今はもう
地獄のおそろしい悪い国にやられたのだから
これからは,人間の国には,なんの危険も
ない,邪魔ものもないであろう.
私は恐しい魔神であったけれども,
一人の人間の計略にまけて
今はもう,つまらない死方,悪い死方をするのです.
と谷地の魔神が物語りました.
```

### Output
```
The bog demon himself sang this song, "Harits Kunna":

Harits Kunna

One day, the weather was fine,
So I peeked out from my bog,
Just my eyes and mouth showing.
From the direction of the shore,
I heard the voices of men.
I saw two young men approaching together.

The first seemed a hero,
Possessing the qualities of a brave warrior,
Beautiful as a god.
But the one who followed behind,
He looked unwell,
Pale of face.
They came along discussing something,
And as they passed by my bog,
Right in front of me,
The pale-faced man stopped.
He covered his nose and said,
"Oh, how foul! This wretched bog!
Passing by this awful place,
It's so filthy! What is that stench?"

I only heard his words,
But I was enraged beyond measure,
Unsure if I even existed anymore.
I burst forth from the mud!
The earth split and cracked as I leaped.
Gnashing my teeth,
I fiercely pursued them.

The first man, seeing this,
Turned back like a fish darting around,
Slipped under the pale man's arm,
And fled far away.
I chased the blue-faced man for a few steps,
Quickly caught up,
And swallowed him whole, head first.

Then, with all my might, I chased after the other man,
Reaching a human village,
A large settlement.
I saw coming towards me,
The Fire Old Woman, the Divine Old Woman,
In red robes, six layers of them,
With a sash tied, wearing all six layers,
And leaning on a red staff, she flew to my side.

"Well, well," she said,
"Why have you come to this Ainu village?
Now, go back! Go back!"
As she spoke, she raised her red staff, her metal staff,
And struck me.
Flames rained down from the staff,
Like a downpour upon me.

But I paid no heed,
Gnashing my teeth,
I chased after the man.
He ran through the village,
Like a ring spinning around.
I flew after him,
And the earth split and cracked.
The village was in uproar,
Some pulling their wives by the hand,
Others dragging their children,
Crying and screaming,
Fleeing in a boiling frenzy.

But I cared not,
Raising a storm of dust.
The Fire Old Goddess ran beside me,
And tremendous flames flew over me.

In the midst of this,
The man darted into a house,
And immediately burst out again.
I saw him nocking a small arrow of artemisia to a small bow of artemisia,
Smiling at me from afar, aiming.
Seeing this, I found it amusing.
"How can such a tiny artemisia arrow cause harm?"
I thought, gnashing my teeth,
And tried to swallow him head first.

At that moment, the man shot me square in the neck.
After that, I knew no more.
When I came to my senses,
I was between the ears of a great dragon.

The villagers gathered,
And the young man I had chased,
Gave loud instructions.
They meticulously cut up my corpse,
Carried it to one place, burned it,
And scattered the ashes
Behind a rock on the mountain.

Only now do I realize,
That the one I thought was just a human,
Just a young man,
Was Okikirmui, a divine hero.
I was a terrible, evil god, a demon god,
And because I was near the human village,
Okikirmui, thinking of the village's safety,
Provoked me,
Made me chase him,
And killed me with an artemisia arrow.

And the blue-faced man I swallowed,
I thought he was human,
But it was Okikirmui who created a being from his own excrement,
And brought it along.

Because I was a demon,
I have now been cast into
The terrible, evil land of hell.
From now on, there will be no danger,
No disturbance,
In the land of humans.

I was a fearsome demon,
But I was defeated by the scheme of a single human,
And now I face a meaningless death, a wretched end."

So spoke the bog demon.
```
