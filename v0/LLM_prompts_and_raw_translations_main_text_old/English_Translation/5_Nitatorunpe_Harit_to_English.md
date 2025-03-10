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
Translate the following text from Japanese to English. The original text is a chant sung by god telling his story. Try to make the translation also look like a chant but keep the original meanings.

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
Here's a translation of the Japanese text into English, attempting to maintain a chant-like quality while preserving the original meaning:

**The Mire Demon's Own Sung Ballad: "Haritsu Kunna"**

Haritsu Kunna, hear my tale,
On a day of sunlit vale.
From my mire, just eyes and mouth,
I watched the world, from north to south.

Voices came upon the breeze,
From the shore, beneath the trees.
Two young men, I saw them stride,
Toward my mire, side by side.

The first, a hero, strong and bright,
A godlike beauty, filled with light.
The second, sickly, pale of face,
A wretched air, a foul disgrace.

They spoke in whispers, drawing near,
Until my mire was crystal clear.
The sickly one, he stopped and cried,
His nose he pinched, his face he hide.

"Oh, the stench! This mire is cursed!
A foulness here, the very worst!"
I heard his words, a burning sting,
My rage arose, on furious wing.

From the mud, I burst and flew,
The earth it cracked, the ground it knew.
With gnashing teeth, I gave them chase,
To banish them from this sacred place.

The hero saw, and turned with speed,
Like fish that twist, to plant a seed.
Beneath the wretch's arm he flew,
And fled away, from me and you.

The sickly man, I chased him down,
Two steps, three steps, then wore the crown.
I caught him quick, and swallowed whole,
His wretched life, I took his soul.

Then turned my wrath, with all my might,
To chase the hero, out of sight.
He fled toward a village grand,
A human place, in this fair land.

Then from the village, drawing near,
A fiery crone, dispelled all fear.
In robes of red, six layers deep,
A staff of fire, secrets to keep.

"What brings you here, to Ainu land?
Begone, foul beast, I command!"
She raised her staff, a fiery brand,
And struck at me, with burning hand.

Flames like rain, upon me fell,
But still I chased, with savage yell.
He ran in circles, round and round,
While earth did crack, with awful sound.

The village screamed, in wild dismay,
As parents fled, and children stray.
A boiling chaos, fear took hold,
But still I chased, so brave and bold.

The fiery crone, she ran beside,
With flames that danced, a burning tide.
The hero dove, into a home,
Then out again, no longer prone.

A bow of wormwood, in his hand,
An arrow notched, at my command.
He smiled at me, with steady gaze,
And aimed his shot, in cunning ways.

I laughed aloud, "A puny dart!
How can such weakness pierce my heart?"
I gnashed my teeth, prepared to feast,
To swallow him, both man and beast.

But then he struck, with deadly aim,
The arrow pierced, my vital frame.
I knew no more, my senses fled,
And darkness fell, upon my head.

I woke to find, a gruesome sight,
Between the ears, of dragon might.
The villagers, they gathered near,
The hero spoke, for all to hear.

He ordered them, with voice so strong,
To cut my corpse, where I was wrong.
They chopped me small, with blade and stone,
And burned my flesh, to leave me prone.

My ashes cast, behind the stone,
My reign of terror, overthrown.
I see it now, with fading breath,
He was no man, but faced with death.

Okikirmui, the hero bright,
Who saved his village, from my blight.
He angered me, and made me chase,
Then killed me swift, in this vile place.

The sickly man, I swallowed whole,
Was not a man, but took its toll.
Okikirmui, with cunning art,
Had made a thing, to play its part.

A demon I, now doomed to dwell,
In hellish realms, where shadows fell.
No more I'll haunt, the human land,
No more I'll threaten, with my hand.

A fearsome demon, I have been,
But tricked by man, a mortal sin.
A wretched death, a shameful end,
This is the tale, the mire did send.

```
### Another prompt for matched meaning

```
Translate the following text from Japanese to English. The original text is a chant sung by god telling his story. Use a story telling tone. Keep the original meanings.
```

### Output of this prompt

```
This is the song of Haritsu Kunna, sung by the demon of the valley himself:

Haritsu Kunna...

One day, the weather was fine, so I peeked out from my valley, just my eyes and mouth visible.
From the direction of the shore, I heard the voices of men.
Looking closer, I saw two young men approaching together.
The first seemed a hero, possessing the bearing of a brave warrior, beautiful as a god.
But the second man looked unwell, his complexion poor.
They were talking as they walked, and as they passed by my valley, right in front of me, the sickly man stopped.
He covered his nose and said, "Oh, how foul! This wretched valley! Passing by this awful place, what is that disgusting stench?"

I only heard his words, but I was so enraged I forgot myself.
I burst from the mud! As I leaped, the earth cracked and split.
Gnashing my teeth, I gave chase with all my might.
The first man, seeing this, turned back as swiftly as a fish, darted under the sickly man's arm, and fled far away.
I pursued the pale man for only a few steps before I caught him and swallowed him whole.

Then, with all the speed I could muster, I chased after the other man, following him to a large human village.
There, coming towards me, was an old woman of fire, a goddess, wearing six red robes, belted and layered.
Leaning on a red staff, she flew to my side.
"Well, well," she said, "what brings you to this Ainu village? Now, be gone! Be gone!"
As she spoke, she raised her red, golden staff and struck me.
Flames rained down upon me from the staff.

But I paid them no mind, gnashing my teeth as I pursued the man.
He ran through the village like a wheel turning, and I flew after him, splitting and cracking the earth.
The village was in chaos! People grabbed their wives and children, crying and fleeing in terror, a scene of utter turmoil.
But I cared not. I kicked up a storm of dust. The old fire goddess ran beside me, and a torrent of flames flew over me.

In the midst of this, the man darted into a house, only to emerge again immediately.
I saw him nocking a small arrow of mugwort to a small bow of mugwort, aiming at me with a smile.
I found this amusing.
"How could such a tiny arrow of mugwort cause any harm?" I thought.
Gnashing my teeth, I lunged to swallow him whole.
But at that moment, the man struck me hard in the neck with his arrow.
After that, I knew nothing.

When I came to, I found myself between the enormous ears of a dragon.
The villagers had gathered, and the young man I had chased was shouting orders.
They chopped my corpse into tiny pieces, gathered them together, burned them, and scattered the ashes behind a mountain rock.

Only now do I realize that the man I thought was just a human, just a young man, was actually Okikirmui, a hero of the gods.
I was a terrible, evil god, a demon, and because I was near the human village, Okikirmui, thinking of the village's safety, angered me, made me chase him, and killed me with his arrow of mugwort.
And the pale man I swallowed earlier, whom I thought was human, was actually a creation of Okikirmui's excrement, brought along for that purpose.

I was a demon, and now I have been cast into the terrible, evil land of hell.
From now on, the land of humans will be free from danger, free from trouble.
I was a fearsome demon, but I was defeated by the cunning of a single human.
Now I face a meaningless, wretched death.

So spoke the demon of the valley.

```