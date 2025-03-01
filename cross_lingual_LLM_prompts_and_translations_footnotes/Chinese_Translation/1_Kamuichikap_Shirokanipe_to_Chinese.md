# LLM-assisted Translation project of Ainu shin'yoshu (アイヌ神謡集) collected by Chiri Yukie 知里幸惠 (1903 - 1922).

## Chinese Translation of

## Kamuichikap kamui yaieyukar, “Shirokanipe ranran pishkan” 梟の神の自ら歌った謡「銀の滴しずく降る降るまわりに」

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
Translate the following text from English to Chinese. The original text is translation from Japanese which is footnotes of Ainu chant. 
Keep the original meaning. Use modern Chinese. Display in Traditional Chinese. Only allow Chinese and English characters.
If a term cannot be translated, keep the original language.

1.  In the old days, when a boy got a little older, they would make and give him a small bow and arrow. The child would play by shooting at trees and birds, unknowingly becoming skilled in archery.
ak...... archery, shinot is play, ponai is small arrow.

2.  shiktumorke...... the look in one's eyes.
It is said that if you want to know a person's true nature, the best way is to look at their eyes, and they would be scolded if they looked around restlessly.

3.  achikara...... means "dirty."

4.  It is said that birds and animals are shot down by people because they want the arrows made by people, and they are taking the arrows.

5.  kotankorkamui...... a god who possesses a country or village.
In the mountains, there are nupurikorkamui...... a god who possesses a mountain (bear) and nupuripakorkamui...... a god who possesses the east of the mountain (wolf), and the owl is ranked after the bear and wolf.
kotankorkamui is not a rough and hasty person like the mountain god or the god of the east of the mountain. Therefore, they are usually calm and always have their eyes closed, and it is said that they only open their eyes when something very serious happens.

6.  eharkiso...... the left seat.

7.  eshiso...... the right seat.
In the center of the house is a hearth, and the side with the ※(「窗/心」) on the east side is the upper seat. Looking from the upper seat, the right is eshiso and the left is harkiso. Only men can sit in the upper seat. Guests who are of lower status than the head of the house will refrain from taking the upper seat. It is customary for the master and mistress of the house to sit side by side in the right seat. The left seat is next to the right seat, and the seat on the west side (towards the doorway) is the lowest seat.

8.  hayokpe helmet.
It is said that when birds and animals are in the mountains, they are invisible to human eyes, but each has a house like a human, and they all live in the same form as humans, and when they come to human villages, they wear helmets. And it is said that the corpses of birds and animals are helmets, and the main body is invisible, but it is between the ears of the corpse.

9.  otuipe...... a guy with a cut-off butt.
A tail that is short like a dog's cut-off tail is not highly valued.
They use abusive language to describe extremely insignificant people as wenpe...... a bad guy, otuipe...... a guy with a cut-off tail.

10. chikashnukar. When a god is very pleased with a human, and bestows some great fortune on that person in a completely unexpected place, that person rejoices, saying ikashnukar an.

11. apehuchi...... old woman of fire. The fire goddess is the most revered goddess in the house and is always an old woman. When mountain gods, sea gods, and other various gods come to the house as guests like this owl, this apehuchi takes the lead in entertaining and talking to the guests. It is also acceptable to simply say kamuihuchi (god old woman).

12. neusar talking to each other.
Talking about various worldly matters is also neusar. Usually, things like kamuiyukar (god song) and uwepeker (old tales) are called neusar.

13. ashke a uk. ashke is finger, hand. a uk is to take. It means inviting people when there is a celebration.

14. kakkokhau...... the voice of the cuckoo bird.
Because the voice of the cuckoo bird is beautiful and clear, people who speak clearly and understandably to everyone are said to be like cuckoo birds.

15. chisekorkamui...... a god who possesses a house.
The fire god is like the housewife, and the house god is like the master of the house. He is also called chisekorekashi...... an old man who owns a house.

16. nusakorkamui...... a god who possesses a sacred shelf, an old woman.
The god of the sacred shelf is also always a woman. In the event of an emergency, she may appear to humans, but at that time, she appears in the form of a snake. Therefore, if a snake appears near the sacred shelf or near the east window, they say, "The old woman of the sacred shelf must have gone out on business," and they never kill the snake. It is said that if you kill it, you will be punished.

```

### Output
```
1. 在過去，當男孩稍微長大一點，他們會製作並給他一個小弓箭。孩子會通過射擊樹木和鳥類來玩耍，不知不覺地變得擅長射箭。
ak...... archery（射箭）, shinot 是玩耍, ponai 是小箭。

2. shiktumorke...... 眼神。
據說，如果你想了解一個人的真實本性，最好的方法是看他們的眼睛，如果他們不安地四處張望，就會受到責罵。

3. achikara...... 意思是「骯髒」。

4. 據說鳥類和動物被人類射下來，是因為它們想要人類製作的箭，並且它們正在拿走箭。

5. kotankorkamui...... 擁有國家或村莊的神。
在山裡，有 nupurikorkamui...... 擁有山的神（熊）和 nupuripakorkamui...... 擁有山東邊的神（狼），貓頭鷹的地位排在熊和狼之後。
kotankorkamui 不像山神或山東邊的神那樣粗魯和倉促。因此，他們通常很平靜，總是閉著眼睛，據說只有在非常嚴重的事情發生時才會睜開眼睛。

6. eharkiso...... 左座。

7. eshiso...... 右座。
在房子的中央是一個爐灶，東側有※(「窗/心」)的那一側是上座。從上座看，右邊是 eshiso，左邊是 harkiso。只有男人才能坐在上座。地位低於戶主的客人會避免坐在上座。房子的主人和女主人習慣並排坐在右座。左座在右座旁邊，西側（朝向門口）的座位是最低的座位。

8. hayokpe 頭盔。
據說，當鳥類和動物在山裡時，人類的眼睛是看不見它們的，但它們每個都像人類一樣有一個房子，它們都以與人類相同的形式生活，當它們來到人類的村莊時，它們會戴上頭盔。據說鳥類和動物的屍體是頭盔，主體是看不見的，但在屍體的耳朵之間。

9. otuipe...... 一個屁股被切掉的傢伙。
像狗的斷尾一樣短的尾巴是不受重視的。
他們使用辱罵性的語言來形容極其微不足道的人，如 wenpe...... 一個壞傢伙，otuipe...... 一個斷尾的傢伙。

10. chikashnukar. 當神非常高興人類，並在一個完全意想不到的地方給予那個人一些巨大的財富時，那個人會高興地說 ikashnukar an。

11. apehuchi...... 火的老婦人。火女神是房子裡最受尊敬的女神，而且總是一位老婦人。當山神、海神和其他各種神像這隻貓頭鷹一樣來到房子裡做客時，這位 apehuchi 會帶頭招待和與客人交談。也可以簡單地說 kamuihuchi（神老婦人）。

12. neusar 互相交談。
談論各種世俗的事情也是 neusar。通常，像 kamuiyukar（神之歌）和 uwepeker（古老的故事）之類的事情被稱為 neusar。

13. ashke a uk. ashke 是手指，手。a uk 是拿取。意思是當有慶祝活動時邀請人們。

14. kakkokhau...... 杜鵑鳥的聲音。
因為杜鵑鳥的聲音優美而清晰，所以說話清晰且大家都能理解的人被說成像杜鵑鳥一樣。

15. chisekorkamui...... 擁有房子的神。
火神就像家庭主婦，而房屋神就像房子的主人。他也被稱為 chisekorekashi...... 擁有房子的老人。

16. nusakorkamui...... 擁有神聖架子的神，一位老婦人。
神聖架子的神也總是一位女性。在緊急情況下，她可能會出現在人類面前，但在那時，她會以蛇的形式出現。因此，如果一條蛇出現在神聖架子附近或東窗附近，他們會說：「神聖架子的老婦人一定是出去辦事了」，他們永遠不會殺死蛇。據說如果你殺了它，你將受到懲罰。
```
