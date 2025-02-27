# LLM-assisted Translation project of Ainu shin'yoshu (アイヌ神謡集) collected by Chiri Yukie 知里幸惠 (1903 - 1922).

## Iterative 1 Updated Chinese Translation of

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
You are translating the following Japanese text into English. The original text is a chant sung by god telling his story. You already have an initial English translation.

Here are your tasks:

1. Criticise the English translation based on the Japanese text. 
2. Improve the English translation.

Keep the original meanings.

This is the Japanese text.
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

This is the English translation.
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

### Output
```
This is Little Okikirmui's song, sung by himself:

"This sand is red, so red."

It goes like this:

One day, playing upstream, I met a demon's child. Always beautiful, with a lovely face, he wore black and carried a walnut bow and arrows. Seeing me, he grinned and said:

"Little Okikirmui, let's play! I'll stop the salmon run!"

He nocked a walnut arrow and shot it toward the source. Walnut water, foul and murky, poured forth. The salmon, struggling upstream, cried, hating the water, and fled back down. The demon child just grinned.

Angered, I took my silver bow, nocked a silver arrow, and shot it at the source. Silver water, pure and clear, flowed out. The salmon, revived by the clean water, laughed and played, splashing joyfully upstream.

Then, the demon child, temper flaring, scowled, "If you do that, I'll stop the deer!"

He nocked a walnut arrow, shot it into the sky. From the mountain forests came a walnut wind, a twisting gale, separating the bucks from the does, blowing them in a beautiful line into the heavens. The demon child grinned.

Enraged, I nocked a silver arrow to my silver bow and shot it after the deer. From the heavens fell a silver wind, a cleansing breeze, blowing the bucks and does back down to the mountain forests.

Then, the demon child, his temper plain, said, "You're getting on my nerves! Let's test our strength!"

He stripped off his coat. I, too, in a thin garment, grappled him. He grabbed me, I grabbed him. We wrestled, throwing and lifting, but I was surprised by his strength. Finally, I gathered all my strength, lifted him onto my shoulders, and slammed him onto a mountain rock with a resounding crash! I killed him, cast him to hell, and silence fell.

When that was done, I returned along the river. The salmon laughed and played, their voices a joyful clamor. In the mountain forests, the deer laughed and played, their voices filling the air as they grazed. Relieved, I returned home.

So, Little Okikirmui told his story.

The initial translation is generally good but can be improved by:

*   Being more concise and direct, reflecting the original's straightforward narrative style.
*   Enhancing the poetic elements, especially in describing the natural phenomena (winds, water).
*   Clarifying certain phrases for better understanding and flow.
*   Maintaining consistency in terminology (e.g., 'nock' vs. '番える').
*   Improving the rhythm and cadence of the chant-like sections.
*   Adding some cultural context if possible to enhance the reader's understanding.
*   Using stronger verbs and imagery to amplify the impact of key actions.
*   Ensuring the tone remains consistent with a god telling his story.
```

