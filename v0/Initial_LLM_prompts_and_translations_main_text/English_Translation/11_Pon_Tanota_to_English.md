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
Translate the following text from Japanese to English. The original text is a Japanese translation of a Ainu chant, sung by Ainu god telling his story. 
Use story-telling and poetic tone. Keep the original Japanese meaning accurately. Use modern and simple English.
If a term cannot be translated, keep the original language.

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
A song sung by Little Okikirmui himself:
"This sand, red, so red."

This sand, red, so red,
One day, venturing upstream for play,
I encountered a child of the devil.
Always, the devil's child possessed a beautiful air,
A beautiful face, adorned in black robes,
A small bow of walnut, with arrows of walnut he held.
Seeing me, he grinned,
saying,
"Little Okikirmui, let us play.
Now, I shall show you how to cut off the fish's roots."
So saying, with his walnut bow and walnut arrow,
He aimed and shot towards the water source.
From the source, walnut water, turbid water flowed,
And the salmon, as they tried to ascend,
Loathing the walnut water, cried and retreated with the flow.
The devil's child, he grinned at this.
Seeing this, I was angered,
And with my silver bow and silver arrow,
I aimed and shot towards the water source.
From the source, silver water, pure water flowed,
And the salmon, who had cried as they retreated,
Regained their vigor in the pure water,
Laughing and frolicking,
Splashing and ascending the river.
Then, the devil's child,
His inherent temper showing on his face,
said,
"If you truly do such a thing, I shall show you how to cut off the deer's roots."
And saying so, with his walnut bow and walnut arrow,
He shot into the vast sky.
From the mountain's fields,
Walnut wind, a whirlwind, blew forth,
And from the mountain's fields,
The stags in one group,
The does in another,
Were blown upwards by the wind,
Ascending neatly into the sky.
The devil's child, he grinned.
Seeing this, I was enraged,
And with my silver bow and silver arrow,
I aimed and shot after the deer.
From the heavens,
Silver wind, pure wind, blew down,
The stags in one group,
The does in another,
Were blown down upon the mountain's fields.
Then, the devil's child,
His inherent temper showing on his face,
said,
"Insolent one, if you truly
do such a thing, let us have a contest of strength."
And saying so, he removed his outer garment.
I, too, in a thin robe,
Grappled with him. He grappled with me. From then on,
We wrestled, sometimes below, sometimes above,
But I was astonished by the devil's child's great strength.
Yet, finally, at a certain moment,
I gathered all the strength in my waist, in my body,
And lifted the devil's child
Up to my shoulders,
And the sound of me slamming him upon the mountain rocks
Resounded with a clang. After killing him and
kicking him down to hell, all became silent.
That done, as I returned along the stream,
From within the river, the voices of salmon laughing,
The sounds of play, rose clamorously,
Splashing and echoing. In the mountain's fields,
The voices of stags and does laughing,
The sounds of play, filled the air,
Eating here and there. Seeing this, I was relieved,
And returned to my home.
So, Little Okikirmui told his story.
```
