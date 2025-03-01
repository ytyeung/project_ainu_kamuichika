# LLM-assisted Translation project of Ainu shin'yoshu (アイヌ神謡集) collected by Chiri Yukie 知里幸惠 (1903 - 1922).

## Chinese Translation of

## Terkepi yaieyukar, “Tororo hanrok hanrok!” 蛙が自らを歌った謡「トーロロ ハンロク ハンロク!」

## This is translated from English translation.

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
Translate the following text from English to Chinese. The original text is translation from Japanese which is a Japanese translation of a Ainu chant, sung by Ainu god telling his story. 
Use story-telling and poetic tone. Keep the original meaning. Use modern Chinese. Display in Traditional Chinese. Only allow Chinese and English characters.
If a term cannot be translated, keep the original language.

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

### Output
```
青蛙之歌
「Toro ro hanroku hanroku!」

Toro ro hanroku hanroku!
一日，我在草原上跳躍嬉戲，
望見一間屋舍。我來到門前，
屋內，在一堆寶藏旁，
有一高臺。臺上，
一位年輕人正低頭雕刻刀鞘。
我心生惡作劇，便坐在門檻上，
唱道：「Toro ro hanroku hanroku!」
隨後，年輕人抬起握刀的手，
望著我，溫柔地笑了。
「這是你的歌嗎？你喜悅的歌？
我很想多聽一些，」他說。
我聽了很高興，再次唱道：「Toro ro hanroku hanroku!」
年輕人又說，
「這是你的 yukar？你的 sakehau？
我想更靠近地聽。」
聽了這話，我欣喜若狂，跳到
下方爐邊，
唱道：「Toro ro hanroku hanroku!」
年輕人說，
「這是你的 yukar？你的 sakehau？
我想更靠近地聽。」
聽了這話，我真是樂不可支，跳到
上方爐子的角落，
唱道：「Toro ro hanroku hanroku!」
突然！年輕人跳了起來，
我原以為是這樣，但他抓起一根巨大的燃燒木柴，
朝我扔來！那聲音彷彿我眼前的世界崩塌，之後，我便一無所知。
當我醒來時，我已在垃圾堆邊緣，
一隻腫脹的青蛙死了，而我正坐在它的兩耳之間。
仔細一看，我才意識到我原以為只是一間普通人家的屋舍，
實際上是 Okikirmui 的住所，一位擁有無窮力量的神。
而且我竟然在不知那是 Okikirmui 的情況下，
對他惡作劇。
如今，我將迎來如此毫無意義、可悲的死亡。
因此，未來的青蛙們，永遠、
永遠不要對人類惡作劇。」
說完這些話，腫脹的青蛙便死了。
```
