# LLM-assisted Translation project of Ainu shin'yoshu (アイヌ神謡集) collected by Chiri Yukie 知里幸惠 (1903 - 1922).

## English Translation of

## Terkepi yaieyukar, “Tororo hanrok hanrok!” 蛙が自らを歌った謡「トーロロ ハンロク ハンロク!」

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

蛙が自らを歌った謡
「トーロロ ハンロク ハンロク!」

トーロロ ハンロク ハンロク!
「ある日に,草原を飛び廻って
遊んでいるうちに見ると,
一軒の家があるので戸口へ行って
見ると,家の内に宝の積んである側に
高床がある.その高床の上に
一人の若者が鞘を刻んでうつむいて
いたので,私は悪戯をしかけようと思って敷居の上に
坐って,「トーロロ ハンロク ハンロク!」と
鳴いた,ところが,彼の若者は刀持つ手を上げ
私を見ると,ニッコリ笑って,
「それはお前の謡かえ? お前の喜びの歌かえ?
もっと聞きたいね.」というので
私はよろこんで「トーロロ ハンロク ハンロク!」と
鳴くと,彼の若者のいう事には,
「それはお前のユーカラかえ? サケハウかえ?
もっと近くで聞きたいね.」
私はそれをきいて嬉しく思い下座の方の
炉縁の上へピョンと飛んで
「トーロロ ハンロク ハンロク!」と鳴くと
彼の若者のいうことには,
「それはお前のユーカラかえ? サケハウかえ?
もっと近くで聞きたいね.」それを聞くと私は,
本当に嬉しくなって,上座の方の炉縁の
隅のところへピョンと飛んで
「トーロロ ハンロク ハンロク!」と鳴いたら
突然!彼の若者がパッと起ち
上ったかと思うと,大きな薪の燃えさしを
取り上げて私の上へ投げつけた音は
体の前がふさがったように思われて,それっきり
どうなったかわからなくなってしまった.
ふと気がついて見たら
芥捨あくすて場の末に,一つの腹のふくれた蛙が
死んでいて,その耳と耳との間に私はすわっていた.
よく見ると,ただの人間の家
だと思ったのは,オキキリムイ,神の様に
強い方の家なのであった,そして
オキキリムイだという事も知らずに
私が悪戯をしたのであった.
私はもう今この様につまらない死方,悪い死方
をするのだから,これからの
蛙たちよ,決して,人間たちに悪戯をするのではないよ.
と,ふくれた蛙が云いながら死んでしまった.
```

### Output
```
The Frog's Own Song
"Toro ro hanroku hanroku!"

Toro ro hanroku hanroku!
One day, as I hopped and played in the meadow,
I saw a house. I went to the doorway,
and inside, beside a pile of treasures,
was a raised platform. On that platform,
a young man was carving a sheath, his head bowed.
I thought to play a trick, so I sat on the threshold
and sang, "Toro ro hanroku hanroku!"
Then, the young man raised the hand that held his knife,
looked at me, and smiled gently.
"Is that your song? Your song of joy?
I'd like to hear more," he said.
Pleased, I sang again, "Toro ro hanroku hanroku!"
And the young man said,
"Is that your yukar? Your sakehau?
I'd like to hear it closer."
Hearing this, I was delighted and hopped down
to the hearth's edge on the lower side,
and sang, "Toro ro hanroku hanroku!"
The young man said,
"Is that your yukar? Your sakehau?
I'd like to hear it closer."
Hearing this, I was truly happy, and hopped
to the corner of the hearth on the upper side,
and sang, "Toro ro hanroku hanroku!"
Suddenly! The young man leaped up,
or so I thought, and grabbed a large, burning log,
hurling it at me! The sound was as if the world in front of me collapsed, and after that, I knew nothing.
When I came to, I was at the edge of the refuse heap,
a bloated frog lay dead, and I was sitting between its ears.
Looking closely, I realized that what I thought was a mere human's house
was actually the home of Okikirmui, a god of immense power.
And without knowing it was Okikirmui,
I had played a trick.
Now, I am to die such a meaningless, wretched death.
Therefore, frogs of the future, never,
ever play tricks on humans."
And with those words, the bloated frog died.
```
