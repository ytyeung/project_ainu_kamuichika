# LLM-assisted Translation project of Ainu shin'yoshu (アイヌ神謡集) collected by Chiri Yukie 知里幸惠 (1903 - 1922).

## English Translation of Chiri's footnotes on

## Chironnup yaieyukar, “Haikunterke Haikoshitemturi” 狐が自ら歌った謡「ハイクンテレケ ハイコシテムトリ」

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

(1) pau.狐の鳴声の擬声詞.
(2) pushtotta......鞄の様な形のもので,海猟に出かける時に火道具,薬類,その他細々の必要品を入れて持ってゆくもの.同じ用途のもので piuchiop,karop などがありますが,蒲がま,アツシ織などで作りますから,陸で使用します.pushtotta は熊の皮,あざらしの皮,その他の毛皮で製しますから水がとおらないので,海へ持って行くのです.
(3) noya ai......蓬の矢.蓬はアイヌの尊ぶ草です.蓬の矢で打たれると,浮ぶ事が出来ないから悪魔の最も恐れるものだと云うので,遠出するとき必要品の一つに数えられます.
(4) もとは男の便所と女の便所は別になっていました.ashinru も eosineru も同じく便所の事.
狐の中で黒狐は最も尊いものだとしています.海の中に突き出ている岬は大概黒狐の所領で,黒狐はよっぽどの大へんがなければ,人に声をきかせないと申します.
Okikurumi(Okikirmui)と Samayunkur と Shupunramka とはいとこ同士で,Shupunramka は一ばん年上で Okikirmui は一ばん年下だと云います.Shupunramka は温和な人で内気ですからなにも話がありませんが,Samayunkur は短気で,智恵が浅く,あわて者で,根性が悪い弱虫で,Okikirmui は神の様に智恵があり,情深く,勇気のあるえらい人だと云うので,その物語りは無限というほど沢山あります.
```

### Output
```
Okay, here's the translation of the footnotes from Japanese to English, preserving the original meanings and keeping non-Japanese terms as they are:

(1) pau: Onomatopoeia for the sound of a fox's cry.

(2) pushtotta: A bag-like item used when going sea hunting, to carry fire-making tools, medicines, and other small necessities. Similar items for the same purpose include *piuchiop* and *karop*, but these are made from cattail matting (*gama*) or *attush* woven fabric, so they are used on land. *pushtotta* are made from bear skin, seal skin, or other fur, making them waterproof and suitable for taking to sea.

(3) noya ai: Arrow made of mugwort. Mugwort is a plant revered by the Ainu. It is said that demons fear being struck by a mugwort arrow because it prevents them from floating away, making it an essential item for long journeys.

(4) Originally, men's and women's toilets were separate. *ashinru* and *eosineru* both refer to toilets.

Among foxes, the black fox is considered the most revered. Capes jutting out into the sea are generally considered the territory of black foxes, and it is said that a black fox will not make its presence known to humans unless something very serious is happening.

*Okikurumi (Okikirmui)*, *Samayunkur*, and *Shupunramka* are cousins, with *Shupunramka* being the oldest and *Okikirmui* the youngest. *Shupunramka* is a gentle and timid person, so there are no stories about him. *Samayunkur* is short-tempered, lacks wisdom, is hasty, has a bad nature, and is a coward. *Okikirmui*, on the other hand, is wise like a god, compassionate, courageous, and a great person, so there are countless stories about him.

```