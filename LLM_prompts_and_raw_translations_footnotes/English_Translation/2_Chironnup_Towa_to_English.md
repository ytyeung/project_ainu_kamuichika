# LLM-assisted Translation project of Ainu shin'yoshu (アイヌ神謡集) collected by Chiri Yukie 知里幸惠 (1903 - 1922).

## English Translation of Chiri's footnotes on

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
Translate the following text from Japanese to English. The original text is footnote. Keep the original meanings. For the text which are not in Japanese, keep the original form.

(1) isoeonkami.iso は海幸,eonkami は......を謝す事.
鯨が岸で打ち上げられるのは,海の大神様が人間に下さる為に御自分で持って来て,岸へ打ち上げて下さるものだと信じて,その時は必ず重立った人が盛装して沖の方をむいて礼拝をします.
(2) ononno.これは海に山に猟に出た人が何か獲物を持って帰って来た時にそれを迎える人が口々に言う言葉です.
(3) uniwente......大水害のあと,火災のあと,火山の破裂のあと,その他種々な天災のあったあとなどに,または人が熊に喰われたり,海や川に落ちたり,その他なにによらず変った事で負傷したり,死んだりした場合に行う儀式の事.
その時は槍や刀のさきを互いに突き合せながらお悔みの言葉を交します.一つの村に罹災者が出来ると,近所の村々から沢山の代表者がその村に集ってその儀式を行いますが,一人と一人でも致します.
(4) hokokse......uniwente の時,また大へんな変り事が出来た時に神様に救いを求める時の男の叫び声.フオホホーイと,これは男に限ります.
(5) ashur は変った話,ek は来る.
......村から遠い所に旅に出た人が病気したとか死んだとかした時にその所からその人の故郷へ使者がその変事を知らせに来るとか,外の村で誰々が死にましたとか,何々の変った事がありましたとかと村へ人が知らせに来る事を云います.
その使者を ashurkorkur(変った話を持つ人)と云います.
ashurkorkur は村の近くへ来た時に先ず大声をあげて hokokse(フオホホーイ)をします.すると,それをききつけた村人は,やはり大声で叫びながら村はずれまで出迎えてその変り事をききます.
(6) uchishkar......泣き合う.これは女の挨拶,長く別れていて久しぶりで会った時,近親の者が死んだ時,誰かがなにか大変な危険にあって,やっと免れた時などに,女どうしで手を取り合ったり,頭や肩を抱き合ったりして泣く事.
(7) matrimimse(女の叫び声)......何か急変の場合または uniwente の場合,男は hokokse(フオホホーイ)と太い声を出しますが,女はほそくホーイと叫びます.
女の声は男の声よりも高く強くひびくので神々の耳にも先にはいると云います.それで急な変事が起った時には,男でも女の様にほそい声を出して,二声三声叫びます.
(8) peutanke......rimimse と同じ意ですが,これは普通よく用いられる言葉で,rimimse の方は少し難かしい言葉になっています.
```

### Output
```
Here are the translations of the footnotes from Japanese to English, preserving the original meanings:

(1) isoeonkami.iso refers to the sea, eonkami refers to the act of apologizing for something.
It is believed that when a whale washes ashore, the Great God of the Sea brings it himself to give to humans, and washes it ashore. At that time, important people dress up formally and worship facing the sea.

(2) ononno. This is a word that people say repeatedly when someone returns from hunting in the mountains or at sea with some game.

(3) uniwente...... A ritual performed after a major flood, fire, volcanic eruption, or other natural disasters, or when someone is eaten by a bear, falls into the sea or river, or is injured or dies due to any unusual event.
At that time, they exchange words of condolence while pointing the tips of spears and swords at each other. When a disaster victim appears in one village, many representatives from neighboring villages gather in that village to perform the ritual, but it can also be done between two people.

(4) hokokse...... A man's cry to ask for help from the gods during uniwente or when a terrible event has occurred. "Hohho-i," and this is limited to men.

(5) ashur means unusual news, ek means to come.
......When someone who has traveled far from the village becomes ill or dies, a messenger comes from that place to the person's hometown to report the unusual event, or when someone comes to the village to report that someone has died in another village, or that something unusual has happened.
That messenger is called ashurkorkur (person with unusual news).
When ashurkorkur comes near the village, he first shouts loudly hokokse (Hohho-i). Then, the villagers who hear it also shout loudly and go out to the edge of the village to greet him and hear the unusual news.

(6) uchishkar...... Crying together. This is a woman's greeting, when they meet after a long separation, when a close relative has died, or when someone has been in great danger and has finally escaped, women hold hands or hug each other's heads or shoulders and cry.

(7) matrimimse (woman's cry)...... In case of a sudden change or in the case of uniwente, men make a loud voice of hokokse (Hohho-i), but women shout in a thin voice, "Ho-i."
It is said that women's voices are higher and stronger than men's voices, so they reach the ears of the gods first. Therefore, when a sudden event occurs, even men make a thin voice like women and shout two or three times.

(8) peutanke...... Has the same meaning as rimimse, but this is a commonly used word, while rimimse is a slightly difficult word.

```