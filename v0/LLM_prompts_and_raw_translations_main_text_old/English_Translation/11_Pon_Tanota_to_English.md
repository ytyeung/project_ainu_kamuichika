# LLM-assisted Translation project of Ainu shin'yoshu (アイヌ神謡集) collected by Chiri Yukie 知里幸惠 (1903 - 1922).

## English Translation of

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
Translate the following text from Japanese to English. The original text is a chant sung by god telling his story. Try to make the translation also look like a chant but keep the original meanings.

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
Okay, here's my attempt at translating the Ainu chant into English, trying to maintain a chant-like feel and preserve the original meaning:

**The Song of Little Okikirmui**
*"This sand, red, so red."*

This sand, red, so red,
One day I wandered, upstream I sped.
There I met a demon's child,
Whose beauty was beguiling, mild.
Face so fair, a sight to see,
Clothed in black, eternally.
A walnut bow, a walnut dart,
He smiled at me, and spoke his heart:

"Little Okikirmui, let us play,
Let's banish the fish from this waterway!"
He notched his bow, the walnut string,
And shot an arrow toward the spring.
From the source, a walnut tide,
Murky waters, far and wide.
The salmon came, with silver gleam,
But the walnut water, a waking dream.
They wept and turned, their journey done,
The demon child, he watched, amused, the fun.

My anger rose, a burning fire,
I notched my bow, of silver wire.
A silver arrow, swift and true,
I shot it forth, the spring anew.
From the source, a silver stream,
Pure and bright, a waking dream.
The salmon returned, their spirits high,
With laughter loud, they leaped to the sky.
They splashed and played, with joyful sound,
Upstream they surged, on sacred ground.

The demon child, his face contorted,
His temper flared, his joy aborted.
"If you do this, then you shall see,
I'll banish the deer, eternally!"
He notched his bow, the walnut string,
And shot an arrow toward the sky's wing.
From the mountains, a walnut gale,
A whirlwind rose, a mournful wail.
The stags were lifted, one by one,
The does as well, their race was run.
To the heavens high, they soared and flew,
The demon child, he watched, amused, anew.

My anger surged, a tidal wave,
I notched my bow, my soul to save.
A silver arrow, aimed with care,
I shot it forth, into the air.
From the heavens, a silver breeze,
A gentle wind, through the ancient trees.
The stags descended, safe and sound,
The does as well, on hallowed ground.
Back to the mountains, they gently fell,
The demon child, his face a living hell.

The demon child, his rage unbound,
"You arrogant fool, on sacred ground!
If you do this, then you shall know,
A test of strength, before you go!"
He shed his cloak, with wicked glee,
I shed my robe, for all to see.
We grappled close, with might and main,
He held me down, then up again.
We wrestled hard, with sweat and strain,
The demon's strength, a hurricane.
But in the end, with all my might,
I lifted him, into the light.
Above my head, I held him high,
And slammed him down, against the sky.
Upon the rocks, a crashing sound,
I killed him there, on sacred ground.
To hell he fell, his spirit gone,
The silence reigned, the battle won.

I turned and walked, along the stream,
The salmon's laughter, a waking dream.
They splashed and played, with joyful sound,
On sacred ground, forever bound.
In the mountains high, the deer did roam,
The stags and does, returning home.
They grazed and played, with hearts so light,
Banishing darkness, with all their might.
I saw their joy, and felt relief,
And journeyed home, beyond belief.

Thus spoke Little Okikirmui,
Of battles fought, beneath the sky.
*"This sand, red, so red."*

```
### Another prompt for matched meaning

```
Translate the following text from Japanese to English. The original text is a chant sung by god telling his story. Use a story telling tone. Keep the original meanings.
```

### Output of this prompt

```
This is the song of Little Okikirmui, sung by himself:

"This sand is red, red."

It goes like this:

One day, I was playing, going upstream, when I met the child of a demon. Always, this demon child was beautiful to behold, with a beautiful face. He wore black clothes and carried a small bow of walnut wood and arrows of walnut wood. When he saw me, he smiled and said,

"Little Okikirmui, let's play! I'll show you how to cut off the salmon's path!"

And with that, he nocked a walnut arrow to his walnut bow and shot it towards the source of the river. From the source flowed walnut water, murky and foul. The salmon, trying to swim upstream, hated the walnut water and, crying, turned back and fled downstream. The demon child just smiled and smiled.

Seeing this, I was angered. I took my silver bow and nocked a silver arrow, shooting it towards the source of the river. From the source flowed silver water, pure and clean. The salmon, who had been crying, regained their strength in the clear water, laughing and playing, splashing and swimming upstream.

Then, the demon child, his temper flaring, showed his anger on his face and said, "If you're really going to do that, I'll show you how to cut off the deer's path!"

He nocked a walnut arrow to his walnut bow and shot it into the sky. From the mountain forests came a walnut wind, a whirlwind, and from the mountain forests, the male deer and the female deer were separated and blown upwards, rising in a beautiful line into the sky. The demon child just smiled and smiled.

Seeing this, I was enraged! I nocked a silver arrow to my silver bow and shot it after the deer. From the heavens came a silver wind, a pure wind, and the male deer and the female deer were separated and blown down, back to the mountain forests.

Then, the demon child, his temper plain on his face, said, "You're getting on my nerves! If you're really going to do that, let's have a contest of strength!"

And with that, he took off his coat. I, too, stripped down to a thin garment, and we grappled. He grabbed me, and I grabbed him. We wrestled, throwing each other down and lifting each other up, but I was surprised by how strong the demon child was. But finally, at a certain moment, I gathered all the strength in my waist and body, lifted the demon child onto my shoulders, and slammed him onto a mountain rock with a resounding crash! I killed him and cast him down to hell, and then all was silent.

When that was done, I returned along the river, and in the river, I could hear the salmon laughing and playing, their voices rising in a joyful clamor. In the mountain forests, the male deer and the female deer were laughing and playing, their voices filling the air as they ate here and there. Seeing this, I was relieved and returned to my home.

So, Little Okikirmui told his story.

```