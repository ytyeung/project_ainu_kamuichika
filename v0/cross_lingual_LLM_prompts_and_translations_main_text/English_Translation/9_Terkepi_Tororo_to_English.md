# LLM-assisted Translation project of Ainu shin'yoshu (アイヌ神謡集) collected by Chiri Yukie 知里幸惠 (1903 - 1922).

## English Translation of

## Terkepi yaieyukar, “Tororo hanrok hanrok!” 蛙が自らを歌った謡「トーロロ ハンロク ハンロク!」

## This is translated from Chinese translation.

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
Translate the following text from Chinese to English. The original text is translation from Japanese which is a Japanese translation of a Ainu chant, sung by Ainu god telling his story. 
Use story-telling and poetic tone. Keep the original meaning. Use modern and simple English.
If a term cannot be translated, keep the original language.

青蛙自歌之謠
「托羅羅 漢羅庫 漢羅庫！」

托羅羅 漢羅庫 漢羅庫！
「某日，我於草原間跳躍嬉戲，
忽見一戶人家，遂至門前探望。
但見屋內堆滿寶藏，旁有一高床。
一少年郎於高床之上，埋首雕琢刀鞘。
我心生惡作劇，便坐於門檻之上，
鳴叫：「托羅羅 漢羅庫 漢羅庫！」
那少年聞聲，抬起持刀之手，
望向我，粲然一笑，問道：
「此乃汝之歌謠？汝之喜悅之歌？
吾甚想再聞。」
我欣喜若狂，再次鳴叫：「托羅羅 漢羅庫 漢羅庫！」
少年又道：
「此乃汝之ユーカラ？汝之サケハウ？
吾欲更近聆聽。」
聞此言，我心花怒放，一躍至下座之爐緣，
鳴叫：「托羅羅 漢羅庫 漢羅庫！」
少年仍道：
「此乃汝之ユーカラ？汝之サケハウ？
吾欲更近聆聽。」
聽罷此語，我真乃喜不自勝，遂躍至上座之爐緣角落，
高聲鳴叫：「托羅羅 漢羅庫 漢羅庫！」

突如其來！少年猛然起身，
迅如疾風，抄起巨大之燃燒薪柴，
向我擲來，只覺眼前一黑，
隨後便人事不省。

再次醒來，
卻發現自己身處垃圾堆末端，化作一隻腹部鼓脹之青蛙，
已然死去，而我正坐於其雙耳之間。

仔細一看，原以為只是一介凡人之家，
實乃オキキリムイ，神祇般強大之存在所居之所。
而我竟不知其乃オキキリムイ，
貿然前去惡作劇。

如今我將以如此微不足道、如此糟糕之方式死去，
故告誡未來之青蛙們，切莫再對人類惡作劇。
」

鼓脹之青蛙如是說著，氣絕身亡。
```

### Output
```
The Frog's Self-Sung Ballad:
"Tororo Hanroku Hanroku!"

Tororo Hanroku Hanroku!
"One day, as I hopped and played in the meadow,
I spied a dwelling and went to its door to peek.
Inside, treasures piled high, beside a raised bed.
A young man sat upon it, head bent, carving a knife sheath.
A mischievous thought struck me, so I sat upon the threshold,
And sang: "Tororo Hanroku Hanroku!"
The young man, hearing my voice, raised his knife-holding hand,
Looked at me, smiled brightly, and asked:
"Is this your song? Your joyful tune?
I long to hear it again."
Overjoyed, I sang once more: "Tororo Hanroku Hanroku!"
The young man then said:
"Is this your yukar? Your sakehau?
I wish to hear it closer."
At these words, my heart bloomed, and I leaped to the lower hearth's edge,
Singing: "Tororo Hanroku Hanroku!"
The young man persisted:
"Is this your yukar? Your sakehau?
I wish to hear it closer still."
Hearing this, I was beside myself with glee, and hopped to the corner of the upper hearth,
Singing loudly: "Tororo Hanroku Hanroku!"

Suddenly! The young man rose with a start,
Swift as the wind, he seized a massive, burning log,
And hurled it at me, and all went black,
And I knew no more.

When I awoke again,
I found myself at the edge of a garbage heap, transformed into a frog with a swollen belly,
Already dead, and I was sitting between its ears.

Looking closely, what I thought was a mere mortal's home,
Was in truth the dwelling of Okikirmui, a being of godlike power.
And I, not knowing him as Okikirmui,
Went there to play a prank.

Now I shall die in this insignificant, wretched way,
So I warn all future frogs, never again play tricks on humans."

Thus spoke the swollen frog, and breathed its last.
```
