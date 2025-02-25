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
Translate the following text from Japanese to English. The original text is a poem. Try to make the translation poetic but keep the original meanings.

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
**Little Okikirmui's Own Song:**
"This sand, red, so red."

(This sand, red, so red)
One day, I went to play, upstream I tread,
And met a demon child, beauty spread.
Forever fair, the demon child's guise,
A beautiful face, with darkness in his eyes.
Clad in black, a walnut bow he bore,
With walnut arrows, held evermore.
He saw me then, a smile upon his face,
And spoke to me, with wicked, playful grace:

"Little Okikirmui, let us play,
And from this river, fish we'll sweep away!"
He notched his arrow, walnut, dark, and deep,
And shot it forth, where river's secrets sleep.
From the source, a walnut water flowed,
A murky stream, where darkness sowed.
The salmon came, with silver scales so bright,
But turned away, from walnut's bitter blight.
They wept and fled, downstream they sadly went,
The demon child, with joy, his gaze he bent.

I watched him there, and anger filled my breast,
I drew my bow, of silver, purest, best.
A silver arrow, aimed with all my might,
I shot it forth, into the fading light.
From the source, a silver water sprung,
A crystal stream, where purity was sung.
The salmon turned, their spirits now restored,
With laughter bright, they played and then adored.
They splashed and leaped, upstream they bravely flew,
The demon child, his anger quickly grew.

"If you do this," he cried, with rising ire,
"The deer I'll banish, set their souls afire!"
He notched his bow, of walnut, dark, and grim,
And shot it high, beyond the forest's rim.
From the mountain's heart, a walnut wind did blow,
A swirling gale, where shadows start to grow.
The stags were swept, and does were torn apart,
And lifted high, a line against the heart.
They rose to heaven, in the swirling blast,
The demon child, his wicked joy held fast.

I saw it then, and rage consumed my soul,
I drew my bow, to make the creatures whole.
A silver arrow, aimed with steady hand,
I shot it forth, to heal the ravaged land.
From the heavens high, a silver wind descended,
A cleansing breeze, where hope was now extended.
The stags were freed, and does were gently cast,
Back to the earth, their mountain home at last.

The demon child, his fury now unleashed,
His face contorted, all his anger preached.
"You insolent one, if you dare defy,
Then let us fight, and see which one shall die!"
He shed his cloak, his challenge now declared,
And I, in thin clothes, for the battle bared.
We grappled close, our strength against each other,
He pushed me down, then I became the brother.
We wrestled hard, with all our might and main,
I marveled at his power, and felt the pain.
But in the end, with all my strength I strained,
I lifted him, his wicked power drained.
Upon my shoulders, high I held him fast,
And slammed him down, upon the rocks amassed.
The sound it made, a thunderous, echoing crack,
I killed him then, and sent him to the black.
The silence fell, where evil once had reigned,
The demon child, forever now enchained.

I turned and walked, downstream I made my way,
The salmon's laughter, filled the air with play.
Their joyful sounds, like music, filled the stream,
A vibrant chorus, in a waking dream.
Upon the hills, the deer began to graze,
Their happy voices, filled the forest maze.
They ate and played, their freedom now restored,
I watched them there, my heart with peace outpoured.
And then I knew, my task was truly done,
I turned and walked, towards the setting sun,
And made my way, back to my humble home,
Where peace and quiet, would forever roam.

So little Okikirmui, told her tale.

```
### Another prompt for matched meaning

```
Translate the following text from Japanese to English. Keep the original meanings.
```

### Output of this prompt

```
Little Okikirmui's Own Sung Ballad
"This Sand is Red, Red"

[This Sand is Red, Red]
One day, I went upstream to play,
And encountered the child of a demon.
Always, the child of a demon has a beautiful appearance,
A beautiful face. Wearing black clothes,
With a walnut bow and walnut arrows,
When he saw me, he smiled and
Said,
"Little Okikirmui, let's play.
Now, I'll show you how to cut off the fish's roots."
Saying that, he nocked a walnut arrow to his walnut bow,
And shot the arrow towards the source of the river.
From the source, walnut water, muddy water,
Flowed out, and when the salmon tried to swim upstream,
They hated the walnut water and, crying,
Turned back and flowed away. The child of a demon
Smiled at that.
I was angered by the sight, so
I nocked a silver arrow to my silver bow,
And shot the arrow towards the source of the river.
From the source, silver water, clear water,
Flowed out, and the salmon, who had been crying,
Regained their energy in the clear water,
And laughing loudly, playing and frolicking,
Splashing, went upstream.
Then, the child of a demon,
Showing his inherent temper on his face,
Said, "If you really do such things, I'll
Show you how to cut off the deer's roots."
Saying that, he nocked a walnut arrow to his walnut bow,
And shot it into the sky, and from the mountain forest,
Walnut wind, a whirlwind, blew,
And from the mountain forest, the male deer herds separately,
And the female deer herds separately, were blown up by the wind,
And rose neatly into the sky.
The child of a demon smiled.
Seeing that, I was enraged, so
I nocked a silver arrow to my silver bow,
And shot the arrow after the deer herds.
From the sky, silver wind, clear wind,
Blew down, and the male deer herds
Separately, and the female deer herds separately,
Were blown down onto the mountain forest.
Then, the child of a demon,
Showing his inherent temper on his face,
Said, "You impudent thing, if you really
Do such things, let's have a contest of strength."
Saying that, he took off his outer garment.
I also became just a thin garment,
And grappled with him. He also grappled with me. From then on,
We took turns being on top and on bottom, wrestling,
But I was surprised at how strong the child of a demon was.
However, finally, at a certain moment,
I used all the strength in my waist, all the strength in my body,
And lifted the child of a demon
Up to my shoulders,
And the sound of me slamming him onto the mountain rock
Resounded with a clang. After killing him and
Kicking him down to hell, everything became silent.
After that was done, I came back along the river,
And in the river, the voices of the salmon laughing,
The voices of them playing, noisily rising,
Could be heard splashing. In the mountain forest,
The voices of the male deer, the female deer laughing,
The voices of them playing, filled the area,
And they were eating things here and there. I saw that
And felt relieved, and
Returned to my home.
So, little Okikirmui narrated.

```