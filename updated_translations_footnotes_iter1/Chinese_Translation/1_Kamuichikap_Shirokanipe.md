# LLM-assisted Translation project of Ainu shin'yoshu (アイヌ神謡集) collected by Chiri Yukie 知里幸惠 (1903 - 1922).

## Iterative 1 Updated Chinese Translation of

## Kamuichikap kamui yaieyukar, “Shirokanipe ranran pishkan” 梟の神の自ら歌った謡「銀の滴しずく降る降るまわりに」

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
You are translating the following Japanese text into Chinese. The original text is footnote. You already have a Chinese translation and an English translation.

Here are your tasks:

1. Criticise the Chinese translation based on the Japanese text. 
2. Compare the Chinese translation with the English translation.
3. Improve the Chinese translation, especially incoporating the pros of the English translation.

Keep the original meanings. For the text which are not in Japanese, keep the original form. Display in Traditional Chinese.

This is the Japanese text.
(1) 昔は男の子が少し大きくなると,小さい弓矢を作って与えます.子供はそれで樹木や鳥などを的に射て遊び,知らずしらずの中に弓矢の術に上達します.
ak......は弓術,shinot は遊戯,ponai は小矢.
(2) shiktumorke......眼つき.
人の素性を知ろうと思う時は,その眼を見ると一ばんよくわかると申しまして,少しキョロキョロしたりすると叱られます.
(3) achikara......「汚い」という意味.
(4) 鳥やけものが人に射落されるのは,人の作った矢が欲しいので,その矢を取るのだと言います.
(5) kotankorkamui......国または村を持つ神.
山には,nupurikorkamui......山を持つ神(熊)と nupuripakorkamui......山の東を持つ神(狼)などがあって,ふくろうは熊,狼の次におかれます.
kotankorkamui は山の神,山の東の神,の様に荒々しいあわて者ではありません.それでふだんは沈おち着いて,眼をつぶってばかりいて,よっぽど大変な事のある時でなければ眼を開かないと申します.
(6) eharkiso......左の座.
(7) eshiso......右の座.
家の央に囲炉裏いろりがあって,東側の※(「窗/心」、第3水準1-89-54)のある方が上座,上座から見て右が eshiso 左が harkiso.上座に坐るのは男子に限ります.お客様などで,家の主人よりも身分の卑しい人は上座につく事を遠慮します.右の座には主人夫婦がならんですわる事にきまっています.右座の次が左の座で,西側(戸口の方)の座が一ばん下座になっています.
(8) hayokpe 冑.
鳥でもけものでも山にいる時は,人間の目には見えないが,各々に人間の様な家があって,みんな人間と同じ姿で暮していて,人間の村へ出て来る時は冑を着けて出て来るのだと云います.そして鳥やけものの屍体は冑で本体は目には見えないけれども,屍体の耳と耳の間にいるのだと云います.
(9) otuipe......尻の切れた奴.
犬の尻尾の切れた様に短いのはあまり尊びません.
極くつまらない人間の事を wenpe......悪い奴,otuipe......尻尾の切れた奴と悪口をします.
(10) chikashnukar.神が大へん気に入った人間のある時,ちっとも思いがけない所へ,その人間に何か大きな幸を恵与すると,その人は ikashnukar an と云ってよろこびます.
(11) apehuchi......火の老女.火の神様は,家の中で最も尊い神様でおばあさんにきまっています.山の神や海の神,その他種々な神々がこのふくろうの様にお客様になって,家へ来た時は,この apehuchi が主になって,お客のお相手をして話をします.ただ kamuihuchi(神老女)と云ってもいい事になっています.
(12) neusar 語り合う事.
種々な世間話を語り合うのも neusar.普通 kamuiyukar(神謡)や uwepeker(昔譚)の様なものを neusar と云います.
(13) ashke a uk.ashke は指,手.a uk は取る.なにか祝いがあるとき人を招待する事を云います.
(14) kakkokhau......カッコウ鳥の声.
カッコウ鳥の声は,美しくハッキリと耳に響きますから,ハキハキとしてみんなによくわかるように物を云う人の事をカッコウ鳥の様だと申します.
(15) chisekorkamui......家を持つ神.
火の神が主婦で,家の神が主人の様なものです.男性で chisekorekashi......家を持つおじいさんとも申します.
(16) nusakorkamui......御幣棚を持つ神,老女.
御幣棚の神も女性にきまっています.何か変事の場合人間にあらわれる事がありますが,その時は蛇の形をかりてあらわれると云います.それで御幣棚の近所に,または東の方の窗の近所に,蛇が出て来たりすると,「きっと御幣棚のおばあさんが用事があって外出したのだろう」と言って,決してその蛇を殺しません.殺すと罰が当りますと云います.

This is the Chinese translation.
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


This is the English translation.
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
(1) 過去，男孩稍長，便會為其製作小弓箭。孩子們以此射樹木、鳥雀為戲，在不知不覺中熟習了弓箭技藝。ak......是弓術, shinot 是遊戯, ponai 是小矢.
(2) shiktumorke......眼神。欲知其人，觀其眼神最為真切。若眼神不定，左顧右盼，則會受到訓斥。
(3) achikara......意為「骯髒」。
(4) 據說鳥獸為人射落，乃是想要人所製之箭，故取之。
(5) kotankorkamui......掌管國家或村莊之神。山中，有nupurikorkamui......掌管山嶽之神（熊），以及nupuripakorkamui......掌管山之東方的神（狼）等。貓頭鷹之位，次於熊與狼。kotankorkamui不像山神或山之東方之神那般粗魯急躁。因此，平時沉穩平靜，總是閉目養神，據說除非有極為重大的事情才會睜開眼睛。
(6) eharkiso......左座。
(7) eshiso......右座。家之中央設有爐灶，東側有窗戶之處為上座。從上座望去，右側為eshiso，左側為harkiso。上座僅限男子。若來客身份低於主人，則會謙讓，不坐上座。右座通常為主夫婦並坐。右座之後為左座，西側（靠近門口）之座則為末座。
(8) hayokpe......頭盔。據說鳥獸居於山中時，人眼不可見，各自擁有如人類般的家宅，生活亦如人類。當其前往人類村落時，則會戴上頭盔。鳥獸之屍骸即為頭盔，本體雖不可見，然位於屍骸之雙耳之間。
(9) otuipe......斷尾之人。如犬般斷尾之短尾，不為人所重。常以wenpe......壞傢伙，otuipe......斷尾之人等語，詈罵無用之人。
(10) chikashnukar......神若甚喜某人，於其不意之處，賜予莫大幸福，此人便會高呼ikashnukar an，以示欣喜。
(11) apehuchi......火之老嫗。火神乃家中至尊之神，必為老嫗。山神、海神及諸多神祇若如貓頭鷹般來訪，則由apehuchi主持，負責款待與交談。亦可逕稱kamuihuchi（神老嫗）。
(12) neusar......相互傾談。相互傾談各種世間瑣事，亦可稱neusar。通常，如kamuiyukar（神謠）或uwepeker（昔譚）之類，皆可稱neusar。
(13) ashke a uk......ashke指手指、手，a uk指拿取。意指有慶典時邀請他人。
(14) kakkokhau......杜鵑之鳴。杜鵑之聲清亮悅耳，故常以杜鵑鳥比喻言辭清晰、易於理解之人。
(15) chisekorkamui......掌管家宅之神。火神如主婦，家神則如主人。男性則稱chisekorekashi......掌管家宅之老爺爺。
(16) nusakorkamui......掌管御幣棚之神，老嫗。御幣棚之神必為女性。遇有變故之時，或會顯靈於人，據說此時會借用蛇形。因此，若御幣棚附近或東側窗邊出現蛇，便會認為「定是御幣棚之老嫗有事外出」，絕不殺之。據說殺之將受懲罰。

Okay, let's analyze and improve the Chinese translation based on the Japanese original and the English translation.

**General Observations:**

*   The existing Chinese translation is generally accurate but sometimes lacks nuance and could benefit from incorporating the clarity and flow of the English translation.
*   Some sentences are a bit too literal and could be made more natural in Chinese.
*   The English translation often provides a more accessible and understandable rendering of the original Japanese, which can guide improvements to the Chinese.

**Specific Improvements and Rationale:**

I will go through each section, pointing out areas for improvement and providing a revised Chinese translation.

**(1) 昔は男の子が少し大きくなると,小さい弓矢を作って与えます.子供はそれで樹木や鳥などを的に射て遊び,知らずしらずの中に弓矢の術に上達します. ak......は弓術,shinot は遊戯,ponai は小矢.**

*   **Current Chinese:** 以前男孩子稍微長大一點,就會製作小弓箭給他。孩子們就用它來射樹木或鳥類等作為目標來玩耍,不知不覺中就精通了弓箭的技術。ak......是弓術, shinot 是遊戯, ponai 是小矢.
*   **Critique:** The Chinese translation is good. However, the English translation's phrasing "when a boy got a little older, they would make and give him a small bow and arrow" is more natural. The phrase "不知不覺中就精通了弓箭的技術" is a bit lengthy. We can shorten it.
*   **Improved Chinese:** 過去，男孩稍長，便會為其製作小弓箭。孩子們以此射樹木、鳥雀為戲，在不知不覺中熟習了弓箭技藝。ak......是弓術, shinot 是遊戯, ponai 是小矢.

**(2) shiktumorke......眼つき. 人の素性を知ろうと思う時は,その眼を見ると一ばんよくわかると申しまして,少しキョロキョロしたりすると叱られます.**

*   **Current Chinese:** shiktumorke......眼神。想了解一個人的本性時,看他的眼神最清楚,如果稍微左顧右盼,就會被訓斥。
*   **Critique:** The Chinese translation is accurate. The English translation is more descriptive: "the look in one's eyes". "左顧右盼" is okay, but we can use a more vivid word.
*   **Improved Chinese:** shiktumorke......眼神。欲知其人，觀其眼神最為真切。若眼神不定，左顧右盼，則會受到訓斥。

**(3) achikara......「汚い」という意味.**

*   **Current Chinese:** achikara......「骯髒」的意思。
*   **Critique:** Okay.
*   **Improved Chinese:** achikara......意為「骯髒」。

**(4) 鳥やけものが人に射落されるのは,人の作った矢が欲しいので,その矢を取るのだと言います.**

*   **Current Chinese:** 鳥或野獸被人射落,是因為想要人製作的箭,說是為了取箭。
*   **Critique:** The Chinese translation is accurate. The English translation is more concise.
*   **Improved Chinese:** 據說鳥獸為人射落，乃是想要人所製之箭，故取之。

**(5) kotankorkamui......国または村を持つ神. 山には,nupurikorkamui......山を持つ神(熊)と nupuripakorkamui......山の東を持つ神(狼)などがあって,ふくろうは熊,狼の次におかれます. kotankorkamui は山の神,山の東の神,の様に荒々しいあわて者ではありません.それでふだんは沈おち着いて,眼をつぶってばかりいて,よっぽど大変な事のある時でなければ眼を開かないと申します.**

*   **Current Chinese:** kotankorkamui......擁有國家或村莊的神。山裡有 nupurikorkamui......擁有山的神(熊)和 nupuripakorkamui......擁有山東方的神(狼)等,貓頭鷹的地位僅次於熊和狼。kotankorkamui 不像山神、山東方的神那樣粗暴慌張。因此平時總是沉著冷靜,總是閉著眼睛,除非有非常重大的事情才會睜開眼睛。
*   **Critique:** The Chinese translation is accurate. The English translation is more descriptive: "a god who possesses a country or village". "擁有山東方的神" is a bit awkward. We can rephrase it. "粗暴慌張" is okay, but we can use a more vivid word.
*   **Improved Chinese:** kotankorkamui......掌管國家或村莊之神。山中，有nupurikorkamui......掌管山嶽之神（熊），以及nupuripakorkamui......掌管山之東方的神（狼）等。貓頭鷹之位，次於熊與狼。kotankorkamui不像山神或山之東方之神那般粗魯急躁。因此，平時沉穩平靜，總是閉目養神，據說除非有極為重大的事情才會睜開眼睛。

**(6) eharkiso......左の座.**

*   **Current Chinese:** eharkiso......左邊的座位。
*   **Critique:** Okay.
*   **Improved Chinese:** eharkiso......左座。

**(7) eshiso......右の座. 家の央に囲炉裏いろりがあって,東側の※(「窗/心」、第3水準1-89-54)のある方が上座,上座から見て右が eshiso 左が harkiso.上座に坐るのは男子に限ります.お客様などで,家の主人よりも身分の卑しい人は上座につく事を遠慮します.右の座には主人夫婦がならんですわる事にきまっています.右座の次が左の座で,西側(戸口の方)の座が一ばん下座になっています.**

*   **Current Chinese:** eshiso......右邊的座位。家中央有爐灶,有窗戶的那一側是上座,從上座看過去,右邊是 eshiso,左邊是 harkiso。坐在上座的僅限男子。如果是客人等,身份比主人低的人會避免坐在上座。右邊的座位一定是主人夫婦並排坐著。右座的下一個是左座,西側(靠近門口)的座位是末座。
*   **Critique:** The Chinese translation is accurate. The English translation is more descriptive. "一定是主人夫婦並排坐著" is a bit too assertive. We can soften it.
*   **Improved Chinese:** eshiso......右座。家之中央設有爐灶，東側有窗戶之處為上座。從上座望去，右側為eshiso，左側為harkiso。上座僅限男子。若來客身份低於主人，則會謙讓，不坐上座。右座通常為主夫婦並坐。右座之後為左座，西側（靠近門口）之座則為末座。

**(8) hayokpe 冑. 鳥でもけものでも山にいる時は,人間の目には見えないが,各々に人間の様な家があって,みんな人間と同じ姿で暮していて,人間の村へ出て来る時は冑を着けて出て来るのだと云います.そして鳥やけものの屍体は冑で本体は目には見えないけれども,屍体の耳と耳の間にいるのだと云います.**

*   **Current Chinese:** hayokpe 冑(頭盔)。鳥或野獸在山裡的時候,人類的眼睛看不見,但各自都有像人類一樣的家,大家都過著和人類一樣的生活,到人類的村莊來的時候,會戴上頭盔。鳥或野獸的屍體是頭盔,本體是眼睛看不見的,但在屍體的耳朵和耳朵之間。
*   **Critique:** The Chinese translation is accurate. The English translation is more concise. "大家都過著和人類一樣的生活" is a bit lengthy. We can shorten it.
*   **Improved Chinese:** hayokpe......頭盔。據說鳥獸居於山中時，人眼不可見，各自擁有如人類般的家宅，生活亦如人類。當其前往人類村落時，則會戴上頭盔。鳥獸之屍骸即為頭盔，本體雖不可見，然位於屍骸之雙耳之間。

**(9) otuipe......尻の切れた奴. 犬の尻尾の切れた様に短いのはあまり尊びません. 極くつまらない人間の事を wenpe......悪い奴,otuipe......尻尾の切れた奴と悪口をします.**

*   **Current Chinese:** otuipe......斷了尾巴的傢伙。像狗一樣斷了尾巴的短尾巴不太受重視。會用 wenpe......壞傢伙, otuipe......斷了尾巴的傢伙來辱罵極其無用的人。
*   **Critique:** The Chinese translation is accurate. The English translation is more descriptive: "a guy with a cut-off butt". "極其無用的人" is okay, but we can use a more vivid word.
*   **Improved Chinese:** otuipe......斷尾之人。如犬般斷尾之短尾，不為人所重。常以wenpe......壞傢伙，otuipe......斷尾之人等語，詈罵無用之人。

**(10) chikashnukar. 神が大へん気に入った人間のある時,ちっとも思いがけない所へ,その人間に何か大きな幸を恵与すると,その人は ikashnukar an と云ってよろこびます.**

*   **Current Chinese:** chikashnukar. 神非常喜歡某個人的時候,在完全意想不到的地方,賜予這個人很大的幸福,這個人就會說 ikashnukar an 來表達喜悅。
*   **Critique:** The Chinese translation is accurate. The English translation is more concise. "表達喜悅" is redundant.
*   **Improved Chinese:** chikashnukar......神若甚喜某人，於其不意之處，賜予莫大幸福，此人便會高呼ikashnukar an，以示欣喜。

**(11) apehuchi......火の老女.火の神様は,家の中で最も尊い神様でおばあさんにきまっています.山の神や海の神,その他種々な神々がこのふくろうの様にお客様になって,家へ来た時は,この apehuchi が主になって,お客のお相手をして話をします.ただ kamuihuchi(神老女)と云ってもいい事になっています.**

*   **Current Chinese:** apehuchi......火的老婦。火神是家中最尊貴的神,一定是老奶奶。山神或海神,以及其他各種神明像貓頭鷹一樣成為客人來到家裡時,由這位 apehuchi 主持,負責招待客人和談話。也可以直接稱呼為 kamuihuchi(神老婦)。
*   **Critique:** The Chinese translation is accurate. The English translation is more descriptive: "old woman of fire". "負責招待客人和談話" is a bit lengthy. We can shorten it.
*   **Improved Chinese:** apehuchi......火之老嫗。火神乃家中至尊之神，必為老嫗。山神、海神及諸多神祇若如貓頭鷹般來訪，則由apehuchi主持，負責款待與交談。亦可逕稱kamuihuchi（神老嫗）。

**(12) neusar 語り合う事. 種々な世間話を語り合うのも neusar. 普通 kamuiyukar(神謡)や uwepeker(昔譚)の様なものを neusar と云います.**

*   **Current Chinese:** neusar 互相交談。互相交談各種世間閒話也稱為 neusar。一般來說,像 kamuiyukar(神謠)或 uwepeker(昔話)之類的東西稱為 neusar。
*   **Critique:** The Chinese translation is accurate. The English translation is more concise. "互相交談" is redundant.
*   **Improved Chinese:** neusar......相互傾談。相互傾談各種世間瑣事，亦可稱neusar。通常，如kamuiyukar（神謠）或uwepeker（昔譚）之類，皆可稱neusar。

**(13) ashke a uk.ashke は指,手.a uk は取る.なにか祝いがあるとき人を招待する事を云います.**

*   **Current Chinese:** ashke a uk. ashke 是手指、手。a uk 是拿取。指有慶祝活動時邀請人。
*   **Critique:** The Chinese translation is accurate. The English translation is more descriptive: "ashke is finger, hand. a uk is to take". "指有慶祝活動時邀請人" is a bit too direct. We can rephrase it.
*   **Improved Chinese:** ashke a uk......ashke指手指、手，a uk指拿取。意指有慶典時邀請他人。

**(14) kakkokhau......カッコウ鳥の声. カッコウ鳥の声は,美しくハッキリと耳に響きますから,ハキハキとしてみんなによくわかるように物を云う人の事をカッコウ鳥の様だと申します.**

*   **Current Chinese:** kakkokhau......杜鵑鳥的叫聲。杜鵑鳥的叫聲清晰響亮,因此會用杜鵑鳥來形容說話清楚明瞭,大家都聽得懂的人。
*   **Critique:** The Chinese translation is accurate. The English translation is more concise. "說話清楚明瞭,大家都聽得懂的人" is a bit lengthy. We can shorten it.
*   **Improved Chinese:** kakkokhau......杜鵑之鳴。杜鵑之聲清亮悅耳，故常以杜鵑鳥比喻言辭清晰、易於理解之人。

**(15) chisekorkamui......家を持つ神. 火の神が主婦で,家の神が主人の様なものです.男性で chisekorekashi......家を持つおじいさんとも申します.**

*   **Current Chinese:** chisekorkamui......擁有房子的神。火神是主婦,家神就像是主人。男性則稱為 chisekorekashi......擁有房子的老爺爺。
*   **Critique:** The Chinese translation is accurate. The English translation is more descriptive: "a god who possesses a house". "擁有房子的老爺爺" is a bit too direct. We can rephrase it.
*   **Improved Chinese:** chisekorkamui......掌管家宅之神。火神如主婦，家神則如主人。男性則稱chisekorekashi......掌管家宅之老爺爺。

**(16) nusakorkamui......御幣棚を持つ神,老女. 御幣棚の神も女性にきまっています. 何か変事の場合人間にあらわれる事がありますが,その時は蛇の形をかりてあらわれると云います. それで御幣棚の近所に,または東の方の窗の近所に,蛇が出て来たりすると,「きっと御幣棚のおばあさんが用事があって外出したのだろう」と言って,決してその蛇を殺しません.殺すと罰が当りますと云います.**

*   **Current Chinese:** nusakorkamui......擁有御幣棚的神,老婦。御幣棚的神一定是女性。有變故時會顯靈給人類看,據說那時會借用蛇的形狀顯靈。因此在御幣棚附近,或是在東邊窗戶附近,如果出現蛇,就會說「一定是御幣棚的老奶奶有事外出」,絕對不會殺死那條蛇。據說殺了會受到懲罰。
*   **Critique:** The Chinese translation is accurate. The English translation is more descriptive: "a god who possesses a sacred shelf, an old woman". "顯靈給人類看" is a bit lengthy. We can shorten it.
*   **Improved Chinese:** nusakorkamui......掌管御幣棚之神，老嫗。御幣棚之神必為女性。遇有變故之時，或會顯靈於人，據說此時會借用蛇形。因此，若御幣棚附近或東側窗邊出現蛇，便會認為「定是御幣棚之老嫗有事外出」，絕不殺之。據說殺之將受懲罰。
```

