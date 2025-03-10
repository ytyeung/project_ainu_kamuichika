# LLM-assisted Translation project of Ainu shin'yoshu (アイヌ神謡集) collected by Chiri Yukie 知里幸惠 (1903 - 1922).

## English Translation of

## Chironnup yaieyukar, “Towa towa to” 狐が自ら歌った謡「トワトワト」

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

狐が自ら歌った謡「トワトワト」

トワトワト
ある日に海辺へ食物を拾いに
出かけました.
石の中ちゃらちゃら
木片の中ちゃらちゃら
行きながら自分の行手を見たところが
海辺に鯨が寄り上って
人間たちがみんな盛装して
海幸をば喜び舞い海幸をば喜び躍り肉を切る者運ぶ者が
行き交かって重立った人たちは海幸をば謝し拝む者
刀をとぐ者など浜一ぱいに黒く見えます.
私はそれを見ると大層喜びました.
「ああ早くあそこへ着いて
少しでもいいから貰いたいものだ」と
思って「ばんざーい! ばんざーい」と
叫びながら
石の中ちゃらちゃら
木片の中ちゃらちゃら
行って行って近くへ行って見ましたら
ちっとも思いがけなかったのに
鯨が上ったのだとばかり思ったのは
浜辺に犬どもの便所があって
大きな糞の山があります,
それを鯨だと私は思ったので
ありました.
人間たちが海幸をば喜んで躍り海幸をば喜び舞い
肉を切ったりはこんだりしているのだと
私が思ったのはからすどもが
糞をつっつき糞を散らし散らし
その方へ飛びこの方へ飛びしているのでした.
私は腹が立ちました.
「眼の曇ったつまらない奴
眼の曇った悪い奴
尻尾の下の臭い奴
尻尾の下の腐った奴
お尻からやにの出る奴
お尻から汚い水の出る奴
なんという物の見方をしたのだろう.」
それからまた
石の中ちゃらちゃら
木片の中ちゃらちゃら
海のそばから走りながら
見たところが私の行手に
舟があってその舟の中で
人間が二人互いにお悔みをのべています,
「おや,何の急変が
あるのでああいう事をしているのだろう,もしや
舟と一しょに引繰ひっくりかえった人でもあるのではないかしら,
おお早くずっと近くへ行って
人の話を聞きたいものだ.」
と思うのでフオホホーイと
高く叫んで
石の中ちゃらちゃら
木片の中ちゃらちゃら
飛ぶようにして行って見たら
舟だと思ったのは浜辺にある
岩であって,人だと思ったのは
二羽の大きな鵜であったのでした.
二羽の大きな鵜が長い首をのばしたり縮めたり
しているのを悔みを言い合っている様に
私は見たのでありました.
「眼の曇ったつまらない奴
眼の曇った悪い奴
尻尾の下の臭い奴
尻尾の下の腐った奴
お尻からやにの出る奴
お尻から汚い水の出る奴
なんという物の見方をしたのだろう.」
それからまた
石の中ちゃらちゃら
木片の中ちゃらちゃら
飛ぶ様にして川をのぼって行きましたところが
ずーっと川上に女が二人
浅瀬に立っていて泣き合っています.
私はそれを見てビックリして
「おや,なんの悪い事があって
なんの凶報が来てあんなに泣き合って
いるのだろう?
ああ早く着いて人の話を
聞きたいものだ.」
と思って
石の中ちゃらちゃら
木片の中ちゃらちゃら
飛ぶ様にして行って見たら
川の中程に二つの簗やながあって
二つの簗の杭くいが流れにあたってグラグラ動いているのを
二人の女がうつむいたり仰むいたりして
泣き合っているのだと私は思ったの
でありました.
「眼の曇ったつまらぬ奴
眼の曇った悪い奴
尻尾の下の臭い奴
尻尾の下の腐った奴
お尻からやにの出る奴
お尻から汚い水の出る奴
なんという物の見方をしたのだろう.」
それからまた,川をのぼって
石の中ちゃらちゃら
木片の中ちゃらちゃら
飛ぶようにして帰って来ました.
自分の行手を見ましたところが
どうしたのだか
私の家が燃えあがって
大空へ立ちのぼる煙は
立ちこめた雲の様です.それを見た私は
ビックリして気を失うほど
驚きました.女の声で叫びながら
飛び上りますと,むこうから誰かが
大きな声でホーイと叫びながら私のそばへ
飛んで来ました.見るとそれは私の妻で
ビックリした顔色で息せききって,
「旦那様どうしたのですか?」
と云うので,見ると
火事の様に見えたのに
私の家はもとのまま
たっています.火もなし,煙もありません.
それは,私の妻が搗物つきものをしていると
その時に風が強く吹いて簸ている粟の
糠ぬかが吹き飛ばされるさまを
煙の様に私は見たのでありました.
食物を探しに出かけても食物も見付からず,その上に
また,私が大声を上げたので私の妻が
それに驚いて簸ていた粟をも
簸と一しょに放り飛ばしてしまったので
今夜は食べる事も出来ません
私は腹立たしくて床の底へ
身を投げて寝てしまいました.
「眼の曇ったつまらぬ奴
眼の曇った悪い奴
尻尾の下の臭い奴
尻尾の下の腐った奴
お尻からやにの出る奴
お尻から汚い水の出る奴
なんという物の見方をしたのだろう.」
  と
狐の頭かしらが物語りました.
```

### Output
```
The Fox's Own Song: "Towatowato"

Towatowato,
One day, I went to the shore to gather food.
Among the stones, chara-chara,
Among the driftwood, chara-chara.
As I went, I looked ahead and saw
A whale had washed ashore.
The people were all dressed in finery,
Rejoicing in the bounty of the sea, dancing in celebration,
Some cutting the meat, others carrying it away.
The important ones offered thanks and prayers to the sea.
Some sharpened their knives; the beach was black with people.
Seeing this, I was overjoyed.
"Ah, I must hurry and get there,
I want to receive even a little bit!" I thought,
And shouting, "Banzai! Banzai!"
Among the stones, chara-chara,
Among the driftwood, chara-chara.
I went closer and closer, but then,
Unexpectedly,
What I thought was a beached whale
Was just a pile of dog feces on the shore,
A great mountain of dung.
That is what I had mistaken for a whale.
And what I thought were people dancing and rejoicing in the sea's bounty,
Cutting and carrying the meat,
Were just crows pecking at the dung,
Scattering it this way and that,
Flying here and there.
I was furious.
"Blind, worthless fool!
Blind, wicked fool!
Stinky one beneath the tail!
Rotten one beneath the tail!
One whose rear oozes resin!
One whose rear drips foul water!
What a way to see things!"
Then again,
Among the stones, chara-chara,
Among the driftwood, chara-chara.
Running from the seaside,
I saw in the distance
A boat, and in the boat,
Two people were exchanging condolences.
"Oh, what sudden event
Could cause them to do such a thing? Perhaps
Someone has capsized with their boat.
Ah, I must go closer and
Listen to what they are saying!"
So, shouting "Hoo-hoo-hoi!"
Among the stones, chara-chara,
Among the driftwood, chara-chara.
I flew as if on wings to see,
But what I thought was a boat
Was just a rock on the shore,
And what I thought were people
Were just two large cormorants.
Two large cormorants stretching and retracting
Their long necks, which I mistook
For people exchanging condolences.
"Blind, worthless fool!
Blind, wicked fool!
Stinky one beneath the tail!
Rotten one beneath the tail!
One whose rear oozes resin!
One whose rear drips foul water!
What a way to see things!"
Then again,
Among the stones, chara-chara,
Among the driftwood, chara-chara.
I flew up the river,
And far upstream,
Two women stood in the shallows, weeping together.
I was startled to see this.
"Oh, what misfortune has befallen them?
What ill tidings have arrived that they weep so?
Ah, I must hurry and
Listen to what they are saying!"
So,
Among the stones, chara-chara,
Among the driftwood, chara-chara.
I flew as if on wings to see,
But in the middle of the river were two yana (fish weirs),
And the posts of the two yana
Were swaying in the current,
Which I mistook for two women
Looking down and then up,
Weeping together.
"Blind, worthless fool!
Blind, wicked fool!
Stinky one beneath the tail!
Rotten one beneath the tail!
One whose rear oozes resin!
One whose rear drips foul water!
What a way to see things!"
Then again, I went up the river,
Among the stones, chara-chara,
Among the driftwood, chara-chara.
I flew as if on wings back home.
Looking ahead,
I saw that, somehow,
My house was ablaze,
The smoke rising into the sky
Like gathering clouds. Seeing this, I
Was so startled I nearly fainted.
I leaped up, shouting in a woman's voice,
And from the other side, someone
Came flying towards me, shouting "Hoi!" in a loud voice.
It was my wife, her face pale with shock, breathless.
"Husband, what is it?" she asked.
I looked, and what had seemed like a fire,
My house stood as before.
No fire, no smoke.
It was just that my wife was hulling grain (tsukimono),
And at that moment, a strong wind blew,
Scattering the winnowed rice bran (nuka)
Which I had mistaken for smoke.
I had gone out in search of food but found none, and on top of that,
Because I had shouted so loudly, my wife
Was so startled that she threw the winnowing basket
And the rice bran into the air.
So tonight, we will have nothing to eat.
I was furious and threw myself
Onto the floor and went to sleep.
"Blind, worthless fool!
Blind, wicked fool!
Stinky one beneath the tail!
Rotten one beneath the tail!
One whose rear oozes resin!
One whose rear drips foul water!
What a way to see things!"
So spoke the head of the fox.
```
