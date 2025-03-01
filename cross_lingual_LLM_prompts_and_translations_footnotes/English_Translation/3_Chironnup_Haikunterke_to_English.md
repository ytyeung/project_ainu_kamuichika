# LLM-assisted Translation project of Ainu shin'yoshu (アイヌ神謡集) collected by Chiri Yukie 知里幸惠 (1903 - 1922).

## English Translation of

## Chironnup yaieyukar, “Haikunterke Haikoshitemturi” 狐が自ら歌った謡「ハイクンテレケ ハイコシテムトリ」

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
Translate the following text from Chinese to English. The original text is translation from Japanese which is a footnotes of Ainu chants. 
Keep the original meaning. Use modern and simple English.
If a term cannot be translated, keep the original language.

(1) pau. 狐狸叫聲的擬聲詞。
(2) pushtotta......形狀像袋子的東西,出海打獵時用來裝火具、藥品和其他零碎必需品。用途相同的還有 piuchiop, karop 等,但因為是用蒲草、厚司織等製作,所以在陸地上使用。pushtotta 是用熊皮、海豹皮或其他毛皮製成,因此不透水,所以帶到海上去。
(3) noya ai......蓬蒿之箭。蓬蒿是愛努人尊崇的草。據說被蓬蒿之箭射中,會無法漂浮,因此是惡魔最害怕的東西,所以遠行時會將其視為必需品之一。
(4) 原本男廁和女廁是分開的。ashinru 和 eosineru 都是廁所的意思。
在狐狸之中,黑狐被認為是最尊貴的。突出於海中的海岬大多是黑狐的領地,據說除非發生非常重大的事情,否則黑狐不會讓人聽到它的聲音。
Okikurumi (Okikirmui) 和 Samayunkur 和 Shupunramka 是表兄弟,Shupunramka 年紀最大,Okikirmui 年紀最小。Shupunramka 性格溫和內向,所以沒有什麼故事,但 Samayunkur 性格暴躁,缺乏智慧,是個冒失鬼,性格惡劣的膽小鬼,Okikirmui 則像神一樣充滿智慧,富有同情心,是個勇敢偉大的人,因此關於他的故事多到數不清。

```

### Output
```
(1) pau: An onomatopoeia for the sound a fox makes.
(2) pushtotta: A bag-like item used during sea hunting to store fire-making tools, medicine, and other small necessities. Similar items include piuchiop and karop, but these are made from reeds or attush and used on land. pushtotta is made from bear skin, seal skin, or other fur, making it waterproof and suitable for use at sea.
(3) noya ai: An arrow made of mugwort. Mugwort is a sacred grass to the Ainu. It is said that being shot by a mugwort arrow prevents one from floating, making it the thing that demons fear most. Therefore, it is considered an essential item for long journeys.
(4) Originally, men's and women's toilets were separate. ashinru and eosineru both mean toilet.
Among foxes, the black fox is considered the most noble. Capes protruding into the sea are often the territory of black foxes, and it is said that a black fox will not allow its voice to be heard unless something very significant is happening.
Okikurumi (Okikirmui), Samayunkur, and Shupunramka are cousins. Shupunramka is the oldest, and Okikirmui is the youngest. Shupunramka is gentle and introverted, so there are not many stories about him. Samayunkur is hot-tempered, lacks wisdom, and is reckless, cowardly, and has a bad personality. Okikirmui, on the other hand, is wise like a god, compassionate, brave, and great, so there are countless stories about him.
```
