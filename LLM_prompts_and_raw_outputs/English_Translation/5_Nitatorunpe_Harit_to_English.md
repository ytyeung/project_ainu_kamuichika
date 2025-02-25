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
Translate the following text from Japanese to English. The original text is a poem. Try to make the translation poetic but keep the original meanings.

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
Here's an English translation of the poem, aiming for a poetic feel while preserving the original meaning:

**The Marsh Demon's Own Ballad: "Haritsu Kunna"**

Haritsu Kunna,
One day, the weather fair and bright,
From my marsh, just eyes and mouth in sight,
I heard voices carried from the shore afar.
Two youths approached, as near as they are.

The first, a hero, bearing hero's grace,
A godlike beauty shone upon his face.
But the second, following close behind,
A sickly pallor, troubled in his mind.
They spoke in whispers, drawing ever near,
Until they stood before my marsh, so drear.

The sickly youth, he paused, and held his nose,
"Oh, what a stench! This marsh, how foul it grows!
So vile, so rank, what can this foulness be?"
He cried aloud, offensive unto me.

I heard his words, and rage consumed my soul,
I knew not if I lived, beyond control.
From the mud I burst, the earth began to crack,
With gnashing teeth, I charged upon their track.

The first, he saw, and with a fish's turn,
He darted back, his lesson quickly learned.
Beneath the sickly youth's arm, he swiftly fled,
And left him to my wrath, and rising dread.

The pallid youth, I chased him, two lengths, three,
And caught him quick, and swallowed him with glee.
Then, with all speed, I followed on the trail,
Toward a village, large beyond the vale.

There, from the village, came a fiery crone,
A goddess old, in robes of crimson stone.
Six layers of cloth, with sash tightly bound,
A crimson staff, she flew above the ground.

"What brings you here, to this Ainu land?
Begone, I say! Turn back, and understand!"
She raised her staff, of gold and fiery might,
And struck at me, with flames of burning light.

But I, unheeding, with a fearsome roar,
Pursued the youth, and sought to swallow more.
He ran in circles, through the village wide,
And where I followed, earth was torn aside.

The village panicked, chaos filled the air,
Some dragged their wives, some children, in despair.
They cried and fled, a scene of boiling dread,
But I cared not, as dust rose overhead.
The fiery crone, she ran beside my form,
And hurled great flames, a raging, fiery storm.

The youth, he darted to a house's door,
Then burst forth, running as he had before.
An arrow nocked, of mugwort, small and green,
He smiled at me, a deadly, mocking scene.

I laughed aloud, "Such tiny arrow's sting,
Can never harm a creature such as I, a thing!"
With gnashing teeth, I lunged to swallow whole,
But then, the arrow pierced my very soul.

All faded then, I knew not what became,
Until I woke, between a dragon's frame.
The villagers gathered, and the youth, so bold,
Commanded them, as I was lying cold.
They chopped my corpse, to pieces, small and fine,
And burned the fragments, in a pyre divine.
The ashes then, behind a mountain stone,
Were scattered there, my power overthrown.

Now I perceive, that he, the youth so fair,
Was not a mortal, but a god beyond compare.
Okikirmui, a hero, strong and true,
He saved his village, from a fiend like me, it's true.
He angered me, and let me chase him down,
Then slew me with the arrow, of renown.

The pallid youth, the one I swallowed whole,
Was not a man, but something to control.
Okikirmui's creation, foul and grim,
A decoy brought, to seal my fate within.

I was a demon, now condemned to hell,
No longer can I cast a wicked spell.
The human lands, are safe from me at last,
My reign of terror, forever in the past.

Though I was fearsome, mighty in my wrath,
A mortal's cunning, cut a deadly path.
A wretched death, a shameful end I meet,
Defeated by a hero's cunning feat.

Thus spoke the Marsh Demon, in his mournful lay.

```
### Another prompt for matched meaning

```
Translate the following text from Japanese to English. Keep the original meanings.
```

### Output of this prompt

```
The Bog Devil's Own Song: "Harits Kunna"

Harits Kunna

One day, as the weather was fine,
I was watching my bog with only my eyes and mouth showing,
When I heard voices coming from the direction of the beach.
Looking, I saw two young men walking together.
The one in front seemed a hero, possessing the qualities of a hero,
As beautiful as a god.
But when I looked at the one behind, he was in poor condition,
With a bad complexion. They were talking as they came,
And as they passed by my bog,
Just as they came in front of me, the man with the bad complexion
Stopped, stopped and covered his nose, saying,
"Oh, it stinks! A nasty bog! Passing by a bad bog,
How filthy! What is this awful smell?"
I only heard it, but I was so angry I didn't know if I was there or not.
I leaped out of the mud. When I jumped up,
The earth cracked and split. Gnashing my teeth,
I chased after them fiercely, but
The one in front, seeing that,
Turned back like a fish turning around, slipped under the arm of the man with the bad complexion,
And ran away.
I chased the blue man for two or three *ken* (間, a Japanese unit of length),
Quickly caught up and swallowed him whole.
Then, with all my speed, I chased after the other man,
And arrived behind a human village, a large village.
Looking, I saw coming from the other side
A fire old woman, a goddess old woman, in a red kimono, six kimonos,
With a sash, wearing six kimonos,
Leaning on a red staff, flying towards me.
"Well, well, what have you come to this Ainu village for?
Now go home, now go home!"
Saying this, she raised her red staff, a metal staff, and struck me,
And flames rained down on me
From the staff.
But I didn't care at all,
Gnashing my teeth, chasing after the man,
And the man ran around the village like a well-worn ring. Flying after him,
The earth cracked and split. The whole village was in an uproar,
Some pulling their wives' hands, some pulling their children's hands, crying and screaming,
Running away, a boiling scene, but
I didn't care at all, raising a dust storm. The fire old goddess ran beside me,
And tremendous flames flew over me.
In the midst of that, the man jumped into a house
And immediately jumped out again.
Looking, he was nocking a mugwort bow with a mugwort arrow,
Smiling at me from the other side, aiming at me.
Seeing that, I thought it was funny.
"How can such a small mugwort arrow hurt anyone?" I thought,
And as I gnashed my teeth,
And tried to swallow him whole,
At that moment, the man shot my neck
Hard. After that, I didn't know what happened.
When I came to,
I was between the ears of a large dragon.
The villagers gathered, and the young man I had chased
Was loudly giving instructions, and they all finely chopped up my corpse,
Carried it to one place, burned it, and threw the ashes
Behind the rocks of the mountain.
Now that I see it, I realize that the one I thought was just a human,
Just a young man,
Was Okikirmui, a divine hero.
A terrible evil god, a demon god, that's what I was,
And because I was near the human village,
Okikirmui, thinking of the village, angered me,
Made me chase him, and killed me with a mugwort arrow.
And the blue man I swallowed earlier,
I thought he was a human, but
He was a creation of Okikirmui's excrement,
And he had brought him along.
Because I was a devil, I have now been sent
To the terrible evil land of hell,
So from now on, there will be no danger
Or nuisance in the human land.
I was a terrible devil, but
I was defeated by the scheme of one human,
And now I am dying a meaningless death, a bad death.
So the bog devil told the story.

```