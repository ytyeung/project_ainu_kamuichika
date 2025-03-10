# LLM-assisted Translation project of Ainu shin'yoshu (アイヌ神謡集) collected by Chiri Yukie 知里幸惠 (1903 - 1922).

## English Translation of

## Esaman yaieyukar, “Kappa reureu kappa” 獺かわうそが自ら歌った謡「カッパ レウレウ カッパ」

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

獺かわうそが自ら歌った謡
「カッパ レウレウ カッパ」

カッパ レウレウ カッパ
ある日に,流れに沿うて遊びながら
泳いで下りサマユンクルの
水汲路のところに来ると,
サマユンクルの妹が神の様な美しい容子で
片手に手桶を持ち片手に
蒲の束を持って来ているので
川の縁に私は頭だけ出し,
「お父様をお持ちですか?
お母様をお持ちですか?」と云うと,
娘さんは驚いて眼をきょろきょろさせ
私を見つけると,怒の色を顔に
現して,
「まあ,にくらしい扁平頭,悪い扁平頭が
人をばかにして.犬たちよ,ココ......」
と言うと,大きな犬どもが
駈け出して来て,私を見ると牙を鳴ら
している.私はビックリして川の底へ
潜り込んで直ぐそのまま川底を通って
逃げ下った.
そうして,オキキリムイの水汲路の
川口へ頭だけだして
見ると,オキキリムイの妹が
神の様に美しい様子で片手に手桶を持ち
片手に蒲の束を持って
来たので私のいうことには,
「御父様をお持ちですか?
御母様をお持ちですか?」というと,
娘さんは驚いて眼をきょろきょろさせ
私を見ると,怒りの色を顔に
表して,
「まあ,にくらしい扁平頭,悪い扁平頭が
人をばかにして.犬たちよ,ココ......」
と言うと大きな犬どもが駈け出して来た.
それを見て私は先刻の事を思い出し
可笑しく思いながら川の底へ
潜りこんで逃げようとしたら,
まさか犬たちがそんな事をしようとは
思わなかったのに,牙を鳴らしながら
川の底まで私に飛び付き
陸へ私を引き摺り上げ,私の頭も私の体も
噛みつかれ噛みむしられて,しまいに
どうなったかわからなくなってしまった.
ふと気が付いて見ると,
大きな獺の耳と耳の間に私はすわって
いた.
サマユンクルもオキキリムイも
父もなく母もないのを私は知って
あんな悪戯をしたので罰を当てられ
オキキリムイの犬どもに殺され
つまらない死方,悪い死方をするのです.
これからの獺たちよ,決して悪戯をしなさるな.
と,獺が物語った.
```

### Output
```
The Otter's Own Song:
"Kappa Reureu Kappa"

Kappa Reureu Kappa,
One day, as I played along the stream,
Swimming down, I came to Samayunkuru's
Water-drawing path.
Samayunkuru's sister, beautiful as a goddess,
Carried a bucket in one hand and
A bundle of reeds in the other.
I poked my head out of the river's edge and asked,
"Do you have a father?
Do you have a mother?"
The maiden, startled, looked around,
And finding me, her face filled with anger,
"Oh, you hateful flathead, you wicked flathead,
Making fun of people! Dogs, here!"
At her call, large dogs came rushing,
Baring their fangs at me. Startled, I dove
To the river bottom and fled downstream.

Then, at the mouth of Okikirmui's water-drawing path,
I peeked out again. Okikirmui's sister,
Beautiful as a goddess, carried a bucket
In one hand and a bundle of reeds in the other.
I said to her,
"Do you have a father?
Do you have a mother?"
The maiden, startled, looked around,
And finding me, her face filled with anger,
"Oh, you hateful flathead, you wicked flathead,
Making fun of people! Dogs, here!"
Large dogs came rushing at her call.
Remembering what happened before, I found it funny,
And as I dove to the river bottom to escape,
Though I never imagined the dogs would do such a thing,
They leaped into the river, fangs bared,
Dragging me ashore, biting and tearing
At my head and body, until I lost consciousness.

When I awoke, I found myself
Sitting between the ears of a great otter.
I knew that neither Samayunkuru nor Okikirmui
Had father or mother, and I played that prank,
So I was punished, killed by Okikirmui's dogs,
A meaningless, wretched death.

Future otters, never play such pranks.
So, the otter told his tale.
```
