# LLM-assisted Translation project of Ainu shin'yoshu (アイヌ神謡集) collected by Chiri Yukie 知里幸惠 (1903 - 1922).

## English Translation of

## Pon Okikirmui yaieyukar, “Kutnisa kutunkutun” 小オキキリムイが自ら歌った謡「クツニサ クトンクトン」

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
「クツニサ クトンクトン」

クツニサ クトンクトン
ある日に水源の方へ遊びに
出かけたら,水源に一人の小男が
胡桃くるみの木の簗やなをたてるため杭を打つのに
腰を曲げ曲げしている.
私を見ると,いう事には,
「誰だ? 私の甥よ,私に手伝ってお呉れ.」
という.見ると,胡桃の簗
なものだから,胡桃の水,濁った水
が流れて来て鮭どもが
上って来ると胡桃の水が嫌なので
泣きながら帰ってゆく.私は腹が立ったので
小男の持っている杭を打つ槌を
引ったくり小男の腰の央を
私がたたく音がポンと響いた.小男の
腰の央を折ってしまって殺してしまい
地獄へ踏み落してやった.彼の胡桃の杭を
揺り動かして見ると六つの地獄の
彼方まで届いている様だ.
それから,私は腰の力,からだ中の力を
出して,その杭を根本から
折ってしまい,地獄へ踏み落してしまった.
水源から清い風,清い水が
流れて来て,泣きながら帰って行った.
鮭どもは清い風,清い水に
気を恢復して,大さわぎ大笑いして遊び
ながら,パチャパチャと
上って来た.私はそれを見て,安心をし
流れに沿うて帰って来た.と
小さいオキキリムイが物語った.
```

### Output
```
Here's a poetic translation of the Japanese poem into English, aiming to preserve the original meaning and tone:

**Little Okikirmui's Own Song**
*"Kutsunisa Kutonkuton"*

Kutsunisa Kutonkuton,
One day, I wandered to the spring,
And there I saw a tiny man,
Bent low, building a weir of walnut wood.
He hammered stakes, his back a bow,
And when he saw me, thus he spoke:
"Who's there? My nephew, lend a hand!"
But then I saw the walnut weir,
And walnut water, muddied, flowed.
The salmon came, but hated so
The walnut water, turned and wept,
And fled away. My anger rose!
I snatched the mallet from his hand,
And struck him hard, right in the back,
A hollow *pon* the sound that rang.
I broke his back, and slew the wretch,
And kicked him down to deepest hell.
I shook his walnut stakes and saw
They reached beyond six hells or more.

Then, gathering strength from all my limbs,
I broke the stakes right from the root,
And kicked them down to deepest hell.
From the spring, a pure wind blew,
And crystal water flowed anew.
The salmon, who had wept and fled,
Revived by wind and water clear,
With joyful shouts and splashing play,
Leapt up the stream in happy throngs.
I watched them, and my heart found peace,
And followed the stream, returning home.

So spoke the little Okikirmui.

```
### Another prompt for matched meaning

```
Translate the following text from Japanese to English. Keep the original meanings.
```

### Output of this prompt

```
Here's the English translation of the Japanese text, aiming to preserve the original meaning and tone:

A Song Sung by Little Okikirmui Himself
"Kutsunisa Kutonkuton"

Kutsunisa Kutonkuton
One day, I went to play towards the source of the water.
There at the source, I found a little man
Hunched over, driving stakes to build a weir of walnut wood.
When he saw me, he said,
"Who's there? My nephew, please help me."
I looked and saw it was a weir of walnuts,
So walnut water, muddy water,
Was flowing, and the salmon
Trying to swim upstream hated the walnut water
And went back crying. I was furious, so
I snatched the mallet the little man was using to drive the stakes
And struck the little man's lower back.
The sound "pon" echoed. I broke the little man's
Lower back, killed him,
And kicked him down to hell. I shook his walnut stake
And it seemed to reach beyond six hells.
Then, I put all the strength in my back, all the strength in my body,
And broke that stake off at the root,
And kicked it down to hell.
Clear wind, clear water,
Flowed from the source, and the salmon who had gone back crying
Recovered their spirits in the clear wind, clear water,
And frolicked with great commotion and laughter,
Splashing and swimming upstream.
Seeing that, I was relieved
And returned along the stream.
So told little Okikirmui.

```