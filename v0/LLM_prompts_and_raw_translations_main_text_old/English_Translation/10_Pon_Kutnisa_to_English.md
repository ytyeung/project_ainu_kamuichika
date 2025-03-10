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
Translate the following text from Japanese to English. The original text is a chant sung by god telling his story. Try to make the translation also look like a chant but keep the original meanings.

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
Okay, here's a translation of the Japanese text into English, attempting to maintain a chant-like quality while preserving the original meaning:

**The Chant of Little Okikirmui**
*"Kutsunisa Kutonkuton"*

Kutsunisa Kutonkuton,
One day I wandered, to the water's source I strayed,
There I saw a little man, his back in labor swayed.
Building a weir of walnut wood, hammering stakes with might,
He saw me then, and called to me, "Nephew, lend your light!"

"Who are you? Help me, nephew, your strength I implore!"
But the weir was walnut, the water stained and poor.
Walnut water flowed, a murky, bitter stream,
The salmon came, but turned away, their journey just a dream.
They wept and fled, repulsed by the tainted tide,
And in my heart, a burning rage, I could no longer hide.

I seized the mallet from his hand, the hammer he did wield,
And struck him hard, upon his back, his fate forever sealed.
A "pon" it echoed, through the air, a sound of breaking bone,
I broke his back, I took his life, and cast him down alone.
To hell I sent him, to the depths, where shadows twist and crawl,
His walnut stakes, I shook them hard, beyond hell's gates they fall.

Six hells away, the tremors spread, a darkness took its hold,
Then with my strength, my body's might, a story to be told.
I broke the stake, from root to tip, I shattered it in two,
And cast it down, to join the man, in hell's infernal stew.

From the source then flowed, a wind so pure and bright,
Clear water streamed, a cleansing force, banishing the blight.
The salmon turned, their spirits now restored,
They laughed and played, their joy outpoured.
They splashed and leaped, against the current strong,
Their journey onward, where they belonged.

I watched them rise, my heart at peace and ease,
And followed the stream, carried by the breeze.
Thus spoke Little Okikirmui, his tale now at an end,
Kutsunisa Kutonkuton, on this you can depend.

```
### Another prompt for matched meaning

```
Translate the following text from Japanese to English. The original text is a chant sung by god telling his story. Use a story telling tone. Keep the original meanings.
```

### Output of this prompt

```
This is the song of Okikirmui, sung by himself:
"Kutsunisa Kutonkuton"

Kutsunisa Kutonkuton

One day, I went to play near the source of the river. There, I saw a little man, hunched over, hammering stakes to build a weir of walnut wood.

He saw me and said, "Who are you? Nephew, please help me!"

I looked closer. It was a walnut weir, and the water flowing through it was murky with walnut. The salmon, trying to swim upstream, hated the walnut water and turned back, weeping.

I was furious. I snatched the hammer from the little man and struck him hard in the small of his back. *Pon!* The sound echoed. I broke his back, killed him, and kicked him down to hell.

I shook his walnut stake, and it seemed to reach all the way to the sixth level of hell.

Then, gathering all the strength in my back, all the power in my body, I broke the stake at its base and kicked it down to hell as well.

Clear wind and clear water began to flow from the source. The salmon, who had been weeping, were revived by the clear wind and water. They rejoiced, laughing and splashing as they swam upstream.

Seeing this, I was relieved and followed the flow of the river back home.

And that is the story told by little Okikirmui.

```