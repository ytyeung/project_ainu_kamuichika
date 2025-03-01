# LLM-assisted Translation project of Ainu shin'yoshu (アイヌ神謡集) collected by Chiri Yukie 知里幸惠 (1903 - 1922).

## English Translation of

## Pon Horkeukamui yaieyukar, “Hotenao” 小狼の神が自ら歌った謡「ホテナオ」

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

小狼の神が自ら歌った謡
「ホテナオ」

ホテナオ
ある日に退屈なので浜辺へ出て,
遊んでいたら一人の小男が
来ていたから,川下へ下ると
私も川下へ下り,
川上へ来ると私も川上へ行き道をさえぎった.
すると川下へ六回
川上へ六回になった時小男は
持前の癇癪かんしゃくを顔に表して言うことには,
「ピイピイ
この小僧め悪い小僧め,そんな事をするなら
この岬の,昔の名と今の名を
言い解いて見ろ」
私は聞いて笑いながらいうこと
には,
「誰がこの岬の昔の名と
今の名を知らないものか!
昔は,尊いえらい神様や人間が居ったから
この岬を神の岬と
言ったものだが,今は時代が衰えたから
御幣の岬とよんでいるのさ!」
云うと,小男の云うことには,
「ピイトン,ピイトン
この小僧め本当にお前はそういうなら
この川の前の名と今の名を
云って見ろ.」
聞くと,私の云うことには,
「誰がこの川の前の名
今の名を知らないものか!
昔,えらかった時代にはこの川を
流れの早い川と云っていたのだが
今は世が衰えているので流れの遅い川と
云っているのさ.」
云うと小男の云うことには,
「ピイトントン,ピイトントン
本当にお前そんな事を云うなら
お互の素性の解き合いをやろう.」
聞いて私の云うことには,
「誰がお前の素性を知らないものか!
大昔,オキキリムイが山へ行って
狩猟小舎を建てた時榛はしばみの木の炉縁ろぶちを作ったら
その炉縁が火に当ってからからに乾いてしまった.
オキキリムイが片方を踏むと片一方が
上る,それをオキキリムイが怒って
その炉縁を川へ持って下り
捨ててしまったのだ.
それからその炉縁は流れに沿うて流れていって
海へ出で,彼方かなたの海波,此方こなたの海波
に打ちつけられる様を神様たちが御覧になって,
敬うべきえらいオキキリムイの手作りの物がその様に
何の役にもたたず迷い流れて海水と共に腐ってしまうのは
勿体もったいない事だから神様たちから
その炉縁は魚にされて,
炉縁魚と
名づけられたのだ.
ところがその炉縁魚は,自分の素性が
わからないので,人にばけてうろついている.
その炉縁魚がお前なのさ.」
云うと,小男は顔色を
変え変え聞いていたが
「ピイトントン,ピイトントン!
お前は,小さい,狼の子なの
さ.」
云い終ると直ぐに海へパチャンと飛び込んだ.
あと見送ると一つの赤い魚が
尾鰭おびれを動かしてずーっと沖へ
行ってしまった.
と,幼い狼の神様が物語りました.
```

### Output
```
The Song of the Little Wolf God, Sung by Himself
"Hotenao"

Hotenao,
One day, feeling bored, I went to the beach,
As I was playing, a little man appeared.
When I went downstream, he followed me downstream,
When I went upstream, he also went upstream, blocking my path.
This happened six times downstream,
And six times upstream. The little man,
His inherent temper flaring on his face, said,
"Pii pii!
You little brat, you bad little brat! If you do such things,
Tell me the old name and the current name
Of this cape!"
I listened and, laughing, replied,
"Who doesn't know the old name and the current name
Of this cape!
In the old days, because there were revered and great gods and people,
This cape was called the Cape of the Gods,
But now that the times have declined,
It is called the Cape of Nusa (御幣の岬)!"
Upon hearing this, the little man said,
"Piiton, piiton!
You little brat, if you really know,
Tell me the old name and the current name
Of this river!"
Listening, I said,
"Who doesn't know the old name
And the current name of this river!
In the old, great times, this river
Was called the River with the Swift Current,
But now that the world is declining, it is called the River with the Slow Current."
Upon hearing this, the little man said,
"Piitonton, piitonton!
If you really say such things,
Let us reveal each other's true nature."
Listening, I said,
"Who doesn't know your true nature!
Long ago, when Okikirmui went to the mountains
And built a hunting hut, he made a hearth frame of hazel wood.
When that hearth frame was exposed to the fire, it dried out completely.
When Okikirmui stepped on one side, the other side
Rose up. Okikirmui, angered by this,
Took the hearth frame down to the river
And threw it away.
From there, that hearth frame flowed along the current,
Went out to sea, and the gods watched
As it was struck by the waves from afar and the waves from here.
They thought, 'It is a waste that something handmade by the revered and great Okikirmui
Is pointlessly drifting and decaying with the seawater,
So the gods
Turned that hearth frame into a fish,
And it was named Robuchi fish (炉縁魚).'
However, that Robuchi fish doesn't know its own origin,
So it disguises itself as a person and wanders around.
That Robuchi fish is you!"
As I said this, the little man's face
Changed color as he listened,
"Piitonton, piitonton!
You are a small, wolf cub."
As soon as he finished speaking, he splashed into the sea.
Looking after him, a single red fish
Moved its tail fin and went far offshore.
So, the young wolf god told his story.
```
