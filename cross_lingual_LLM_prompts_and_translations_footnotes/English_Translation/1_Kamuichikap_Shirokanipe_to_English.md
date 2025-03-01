# LLM-assisted Translation project of Ainu shin'yoshu (アイヌ神謡集) collected by Chiri Yukie 知里幸惠 (1903 - 1922).

## English Translation of

## Kamuichikap kamui yaieyukar, “Shirokanipe ranran pishkan” 梟の神の自ら歌った謡「銀の滴しずく降る降るまわりに」

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

(1) 以前男孩子稍微長大一點,就會製作小弓箭給他。孩子們就用它來射樹木或鳥類等作為目標來玩耍,不知不覺中就精通了弓箭的技術。
ak......是弓術, shinot 是遊戯, ponai 是小矢.

(2) shiktumorke......眼神。
想了解一個人的本性時,看他的眼神最清楚,如果稍微左顧右盼,就會被訓斥。

(3) achikara......「骯髒」的意思。

(4) 鳥或野獸被人射落,是因為想要人製作的箭,說是為了取箭。

(5) kotankorkamui......擁有國家或村莊的神。
山裡有 nupurikorkamui......擁有山的神(熊)和 nupuripakorkamui......擁有山東方的神(狼)等,貓頭鷹的地位僅次於熊和狼。
kotankorkamui 不像山神、山東方的神那樣粗暴慌張。因此平時總是沉著冷靜,總是閉著眼睛,除非有非常重大的事情才會睜開眼睛。

(6) eharkiso......左邊的座位。

(7) eshiso......右邊的座位。
家中央有爐灶,有窗戶的那一側是上座,從上座看過去,右邊是 eshiso,左邊是 harkiso。坐在上座的僅限男子。如果是客人等,身份比主人低的人會避免坐在上座。右邊的座位一定是主人夫婦並排坐著。右座的下一個是左座,西側(靠近門口)的座位是末座。

(8) hayokpe 冑(頭盔)。
鳥或野獸在山裡的時候,人類的眼睛看不見,但各自都有像人類一樣的家,大家都過著和人類一樣的生活,到人類的村莊來的時候,會戴上頭盔。鳥或野獸的屍體是頭盔,本體是眼睛看不見的,但在屍體的耳朵和耳朵之間。

(9) otuipe......斷了尾巴的傢伙。
像狗一樣斷了尾巴的短尾巴不太受重視。
會用 wenpe......壞傢伙, otuipe......斷了尾巴的傢伙來辱罵極其無用的人。

(10) chikashnukar. 神非常喜歡某個人的時候,在完全意想不到的地方,賜予這個人很大的幸福,這個人就會說 ikashnukar an 來表達喜悅。

(11) apehuchi......火的老婦。火神是家中最尊貴的神,一定是老奶奶。山神或海神,以及其他各種神明像貓頭鷹一樣成為客人來到家裡時,由這位 apehuchi 主持,負責招待客人和談話。也可以直接稱呼為 kamuihuchi(神老婦)。

(12) neusar 互相交談。
互相交談各種世間閒話也稱為 neusar。一般來說,像 kamuiyukar(神謠)或 uwepeker(昔話)之類的東西稱為 neusar。

(13) ashke a uk. ashke 是手指、手。a uk 是拿取。指有慶祝活動時邀請人。

(14) kakkokhau......杜鵑鳥的叫聲。
杜鵑鳥的叫聲清晰響亮,因此會用杜鵑鳥來形容說話清楚明瞭,大家都聽得懂的人。

(15) chisekorkamui......擁有房子的神。
火神是主婦,家神就像是主人。男性則稱為 chisekorekashi......擁有房子的老爺爺。

(16) nusakorkamui......擁有御幣棚的神,老婦。
御幣棚的神一定是女性。有變故時會顯靈給人類看,據說那時會借用蛇的形狀顯靈。因此在御幣棚附近,或是在東邊窗戶附近,如果出現蛇,就會說「一定是御幣棚的老奶奶有事外出」,絕對不會殺死那條蛇。據說殺了會受到懲罰。

```

### Output
```
(1) In the past, when boys grew up a little, they would be given small bows and arrows. The children would use them to shoot at trees or birds as targets for play, and unknowingly master the art of archery. ak... is archery, shinot is play, ponai is a small arrow.

(2) shiktumorke... eyes. When you want to understand a person's nature, looking at their eyes is the clearest way. If they glance around too much, they would be scolded.

(3) achikara... means 'dirty'.

(4) A bird or beast is shot down because it wanted a person to make an arrow for it, saying it was to retrieve the arrow.

(5) kotankorkamui... a god who owns a country or village. In the mountains, there is nupurikorkamui... a god who owns the mountain (bear), and nupuripakorkamui... a god who owns the east side of the mountain (wolf), etc. The owl's position is second only to the bear and wolf. kotankorkamui is not as rough and flustered as the mountain gods or the gods of the east side of the mountain. Therefore, they are usually calm and composed, always with their eyes closed, and only open them when there is something very important.

(6) eharkiso... the left seat.

(7) eshiso... the right seat. There is a hearth in the center of the house, and the side with the window is the seat of honor. Looking from the seat of honor, the right side is eshiso, and the left side is harkiso. Only men can sit in the seat of honor. If it is a guest, someone of lower status than the host will avoid sitting in the seat of honor. The host and his wife always sit side by side in the right seat. Next to the right seat is the left seat, and the seat on the west side (near the entrance) is the lowest seat.

(8) hayokpe helmet. When birds or beasts are in the mountains, they are invisible to human eyes, but they each have houses like humans, and they all live the same lives as humans. When they come to human villages, they wear helmets. The corpses of birds or beasts are helmets, and the main body is invisible, but it is between the ears and ears of the corpse.

(9) otuipe... a guy with a broken tail. Short tails, like dogs with broken tails, are not highly valued. wenpe... bad guy, otuipe... a guy with a broken tail, are used to insult extremely useless people.

(10) chikashnukar. When a god likes someone very much, they bestow great happiness on that person in a completely unexpected place, and that person will say ikashnukar an to express their joy.

(11) apehuchi... the old woman of fire. The fire god is the most honorable god in the house and must be an old woman. When mountain gods, sea gods, and other various gods come to the house as guests like owls, this apehuchi presides over the reception and conversation. She can also be called kamuihuchi (god old woman) directly.

(12) neusar talking to each other. Talking to each other about various worldly matters is also called neusar. Generally speaking, things like kamuiyukar (god tales) or uwepeker (old tales) are called neusar.

(13) ashke a uk. ashke is finger, hand. a uk is to take. It refers to inviting people when there is a celebration.

(14) kakkokhau... the call of the cuckoo. The call of the cuckoo is clear and loud, so the cuckoo is used to describe someone who speaks clearly and understandably to everyone.

(15) chisekorkamui... a god who owns the house. The fire god is the housewife, and the house god is like the master of the house. Men are called chisekorekashi... the old man who owns the house.

(16) nusakorkamui... a god who owns the altar, an old woman. The god of the altar must be female. When something happens, she will appear to humans, and it is said that she will borrow the shape of a snake to appear. Therefore, if a snake appears near the altar or near the east window, people will say, "The old woman of the altar must have gone out on business," and they will never kill the snake. It is said that killing it will be punished.
```
