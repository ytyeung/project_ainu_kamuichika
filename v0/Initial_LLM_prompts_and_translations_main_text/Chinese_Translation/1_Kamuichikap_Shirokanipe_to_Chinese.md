# LLM-assisted Translation project of Ainu shin'yoshu (アイヌ神謡集) collected by Chiri Yukie 知里幸惠 (1903 - 1922).

## Chinese Translation of

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
Translate the following text from Japanese to Chinese. The original text is a Japanese translation of a Ainu chant, sung by Ainu god telling his story. 
Use story-telling and poetic tone. Keep the original Japanese meaning accurately. Use modern Chinese. Display in Traditional Chinese.
If a term cannot be translated, keep the original language.

梟の神の自ら歌った謡
「銀の滴しずく降る降るまわりに」

「銀の滴降る降るまわりに,金の滴
降る降るまわりに.」という歌を私は歌いながら
流に沿って下り,人間の村の上を
通りながら下を眺めると
昔の貧乏人が今お金持になっていて,昔のお金持が
今の貧乏人になっている様です.
海辺に人間の子供たちがおもちゃの小弓に
おもちゃの小矢をもってあそんで居ります.
「銀の滴降る降るまわりに
金の滴降る降るまわりに.」という歌を
歌いながら子供等の上を
通りますと,(子供等は)私の下を走りながら
云うことには,
「美しい鳥! 神様の鳥!
さあ,矢を射てあの鳥
神様の鳥を射当てたものは,一ばんさきに取った者は
ほんとうの勇者,ほんとうの強者だぞ.」
云いながら,昔貧乏人で今お金持になってる者の
子供等は,金の小弓に金の小矢を
番つがえて私を射ますと,金の小矢を
私は下を通したり上を通したりしました.
その中に,子供等の中に
一人の子供がただの(木製の)小弓にただの小矢
を持って仲間にはいっています.私はそれを見ると
貧乏人の子らしく,着物でも
それがわかります.けれどもその眼色を
よく見ると,えらい人の子孫らしく,一人変り
者になって仲間入りをしています.自分もただの小弓に
ただの小矢を番えて私をねらいますと,
昔貧乏人で今お金持の子供等は大笑いをして
云うには,
「あらおかしや貧乏の子
あの鳥,神様の鳥は私たちの
金の小矢でもお取りにならないものを,お前の様な
貧乏な子のただの矢腐れ木の矢を
あの鳥,神様の鳥がよくよく
取るだろうよ.」
と云って,貧しい子を足蹴にしたり
たたいたりします.けれども貧乏な子は
ちっとも構わず私をねらっています.
私はそのさまを見ると,大層不憫に思いました.
「銀の滴降る降るまわりに,
金の滴降る降るまわりに.」という歌を
歌いながらゆっくりと大空に
私は輪をえがいていました.貧乏な子は
片足を遠く立て片足を近くたてて,
下唇をグッと噛みしめて,ねらっていて
ひょうと射放しました.小さい矢は美しく飛んで
私の方へ来ました,それで私は手を
差しのべてその小さい矢を取りました.
クルクルまわりながら私は
風をきって舞い下りました.
すると,彼かの子供たちは走って
砂吹雪をたてながら競争しました.
土の上に私が落ちると一しょに,一等先に
貧乏な子がかけついて私を取りました.
すると,昔貧乏人で今は金持になってる者の
子供たちは後から走って来て
二十も三十も悪口をついて
貧乏な子を押したりたたいたり
「にくらしい子,貧乏人の子
私たちが先にしようとする事を先がけしやがって.」
と云うと,貧乏な子は,私の上に
おおいかぶさって,自分の腹にしっかりと私を押えていました.
もがいてもがいてやっとの事,人の隙から
飛び出しますと,それから,どんどんかけ出しました.
昔は貧乏人で今は金持の子供等が
石や木片を投げつけるけれど
貧乏な子はちっとも構わず
砂吹雪をたてながらかけて来て一軒の小屋の
表へ着きました.子供は
第一の窗から私を入れて,それに
言葉を添え,斯々かくかくのありさまを物語りました.
家の中から老夫婦が
眼の上に手をかざしながらやって来て
見ると,大へんな貧乏人ではあるけれども
紳士らしい淑女らしい品をそなえています,
私を見ると,腰の央なかをギックリ屈めて,ビックリしました.
老人はキチンと帯をしめ直して,
私を拝し
「ふくろうの神様,大神様,
貧しい私たちの粗末な家へ
お出で下さいました事,有難う御座います.
昔は,お金持に自分を数え入れるほどの者で
御座いましたが今はもうこの様に
つまらない貧乏人になりまして,国の神様
大神様をお泊め申すも
畏れ多い事ながら今日はもう
日も暮れましたから,今宵は大神様を
お泊め申し上げ,明日は,ただイナウだけでも
大神様をお送り申し上げましょう.」という事を
申しながら何遍も何遍も礼拝を重ねました.
老婦人は,東の窗の下に
敷物をしいて私をそこへ置きました.
それからみんな寝ると直ぐに高いびきで
寝入ってしまいました.
私は私の体の耳と耳の間に坐って
いましたがやがて,ちょうど,真夜中時分に
起き上りました.
「銀の滴降る降るまわりに,
金の滴降る降るまわりに.」
という歌を静かにうたいながら
この家の左の座へ右の座へ
美しい音をたてて飛びました.
私が羽ばたきをすると,私のまわりに
美しい宝物,神の宝物が美しい音をたてて
落ち散りました.
一寸のうちに,この小さい家を,りっぱな宝物
神の宝物で一ぱいにしました.
「銀の滴降る降るまわりに,
金の滴降る降るまわりに.」
という歌をうたいながらこの小さい家を
一寸の間にかねの家,大きな家に
作りかえてしまいました,家の中は,りっぱな宝物の積場
を作り,りっぱな着物の美しいのを
早つくりして家の中を飾りつけました.
富豪の家よりももっとりっぱにこの大きな家の
中を飾りつけました.私はそれを終ると
もとのままに私の冑の
耳と耳の間に坐っていました.
家の人たちに夢を見せて
アイヌのニシパが運が悪くて貧乏人になって
昔貧乏人で今お金持になっている者たちに
ばかにされたりいじめられたりしてるさまを私が見て
不憫に思ったので,私は身分の卑しいただの神では
ないのだが,人間の家
に泊って,恵んでやったのだという事を
知らせました.
それが済んで少したって夜が明けますと
家の人々が一しょに起きて
目をこすりこすり家の中を見るとみんな
床の上に腰を抜かしてしまいました.老婦人は
声を上げて泣き,老人は
大粒の涙をポロポロこぼして
いましたが,やがて,老人は起き上り
私の処へ来て,二十も三十も礼拝
を重ねて,そして云う事には,
「ただの夢ただの眠りをしたのだと
思ったのに,ほんとうに,こうしていただいた事.
つまらないつまらない,私共の粗末な家に
お出で下さるだけでも有難く存じますものを
国の神様,大神様,私たちの不運な
事を哀れんで下さいまして
お恵みのうちにも最も大きいお恵みをいただき
ました事.」と云う事を泣きながら
申しました.
それから,老人はイナウの木をきり
りっぱなイナウを美しく作って私を飾りました.
老婦人は身仕度をして
小さい子を手伝わせ,薪をとったり
水を汲んだりして,酒を造る仕度をして,一寸の間に
六つの酒樽を上座にならべました.
それから私は火の老女,老女神と
種々な神の話を語り合いました.
二日程たつと,神様の好物ですから
はや,家の中に酒の香が
漂いました.
そこで,あの小さい子に態わざと
古い衣物を着せて,村中の
昔貧乏人で今お金持になっている人々を
招待するため使いに出してやりました.ので
後見送ると,子供は家毎に
入って使いの口上を述べますと
昔貧乏人で今お金持になっている人々は
大笑いをして
「これはふしぎ,貧乏人どもが
どんな酒を造ってどんな
御馳走があってそのため人を招待するのだろう,
行ってどんな事があるか見物して
笑ってやりましょう.」と
言い合いながら大勢打ち連れて
やって来て,ずーっと遠くから,ただ家を見ただけで
驚いてはずかしがり,そのまま帰る者もあります,
家の前まで来て腰を抜かしているのもあります.
すると,家の夫人が外へ出て
人皆の手を取って家へ入れますと,
みんないざり這いよって
顔を上げる者もありません.
すると,家の主人は起き上って
カッコウ鳥の様な美しい声で物を言いました.
斯々かくかくの訳を物語り
「この様に,貧乏人でへだてなく
互に往来も出来なかったのだが
大神様があわれんで下され,何の悪い考えも
私どもは持っていませんのでしたのでこの様に
お恵みをいただきましたのですから
今から村中,私共は一族の者
なんですから,仲善くして
互に往来をしたいという事を皆様に
望む次第であります.」という事を
申し述べると,人々は
何度も何度も手をすりあわせて
家の主人に罪を謝し,これからは
仲よくする事を話し合いました.
私もみんなに拝されました.
それが済むと,人はみな,心が柔らいで
盛んな酒宴を開きました.
私は,火の神様や家の神様や
御幣ごへい棚の神様と話し合いながら
人間たちの舞を舞ったり躍りをしたりするさまを
眺めて深く興がりました.そして
二日三日たつと酒宴は終りました.
人間たちが仲の善いありさまを
見て,私は安心をして
火の神,家の神
御幣棚の神に別れを告げました.
それが済むと私は自分の家へ帰りました.
私の来る前に,私の家は美しい御幣
美酒が一ぱいになっていました.
それで近い神,遠い神に
使者をたてて招待し,盛んな酒宴を
張りました,席上,神様たちへ
私は物語り,人間の村を訪問した時の
その村の状況,その出来事を詳しく話しますと
神様たちは大そう私をほめたてました.
神様たちが帰る時に美しい御幣を
二つやり三つやりしました.
彼かのアイヌ村の方を見ると,
今はもう平穏で,人間たちは
みんな仲よく,彼のニシパが
村に頭になっています,
彼の子供は,今はもう,成人
して,妻ももち子も持って
父や母に孝行をしています,
何時でも何時でも,酒を造った時は
酒宴のはじめに,御幣やお酒を私に送ってよこします.
私も人間たちの後に坐して
何時でも
人間の国を守護まもっています.
と,ふくろうの神様が物語りました.
```

### Output
```
貓頭鷹神祇的自述之歌
「銀之滴，紛紛落下於周圍」

我吟唱著「銀之滴，紛紛落下於周圍，金之滴，
紛紛落下於周圍」的歌謠，
沿著河流而下，當我經過人類的村莊，
向下俯瞰時，
昔日的貧困之人，如今已成富甲一方，而往昔的富裕人家，
如今卻淪為貧苦之民。
在海邊，孩子們正用玩具小弓和
玩具小箭嬉戲。
我吟唱著「銀之滴，紛紛落下於周圍，
金之滴，紛紛落下於周圍」的歌謠，
飛過孩子們的頭頂，（孩子們）一邊在我身下奔跑，
一邊說道：
「多麼美麗的鳥兒！是神明的鳥！
快，射箭射牠！
誰能射中這神明的鳥，第一個搶到的，
就是真正的勇者，真正的強者。」
說著，那些昔日貧窮如今富有的孩子們，
用金製的小弓，搭上金製的小箭，
向我射來，我讓金箭
從我的下方或上方穿過。
在這些孩子之中，
有一個孩子，手持著普通的（木製）小弓和普通的小箭，
加入他們的行列。我看到他，
衣著打扮顯然是貧窮人家的孩子。
但仔細觀察他的眼神，
卻隱約透露著偉人的後裔的氣息，他顯得與眾不同，
獨自一人加入了孩子們的遊戲。他也用普通的小弓，
搭上普通的小箭，瞄準我，
那些昔日貧窮如今富有的孩子們，便大聲嘲笑，
說道：
「真是可笑啊，貧窮人家的孩子！
那隻鳥，神明的鳥，連我們的
金箭都不屑一顧，又怎麼會理會你這種
窮孩子的爛木頭箭呢？
那隻鳥，神明的鳥，怎麼可能會被你射中呢？」
他們一邊說著，一邊對那貧窮的孩子拳打腳踢。
但那貧窮的孩子，
卻毫不在意，只是專心致志地瞄準我。
看到這情景，我感到非常憐憫。
我吟唱著「銀之滴，紛紛落下於周圍，
金之滴，紛紛落下於周圍」的歌謠，
緩緩地在天空中
畫著圓圈。那貧窮的孩子，
一隻腳遠遠地伸出，另一隻腳靠近，
緊緊地咬著下唇，瞄準著我，
然後猛然射出了箭。那小小的箭矢，美麗地飛翔著，
朝我而來，於是我伸出手，
接住了那小小的箭。
我旋轉著，
劃破長空，翩然降落。
孩子們見狀，奔跑著，
揚起漫天的沙塵，爭先恐後。
當我落到地面上的同時，最先趕到的，
是那貧窮的孩子，他一把抓住了我。
那些昔日貧窮如今富有的孩子們，
隨後趕到，
七嘴八舌地罵著，
推搡著、毆打著那貧窮的孩子，
「可惡的傢伙，貧窮人家的孩子！
竟然搶在我們前面！」
那貧窮的孩子，則將我
緊緊地抱在懷裡，牢牢地壓在自己的肚子上。
他奮力掙扎，好不容易，才從人群的縫隙中
掙脫出來，然後，拔腿就跑。
那些昔日貧窮如今富有的孩子們，
向他投擲石塊和木片，
但那貧窮的孩子毫不在意，
揚起漫天的沙塵，跑到了一間小屋的
門前。孩子
從第一扇窗戶將我放入，並
添油加醋地，將事情的來龍去脈告訴了屋裡的人。
屋內的老夫婦，
用手遮著眼睛，走了出來，
他們雖然非常貧窮，
卻散發著紳士淑女般的氣質。
看到我，他們深深地彎下腰，
驚訝不已。
老人整理了一下腰帶，
向我行禮，
「貓頭鷹神啊，偉大的神啊，
感謝您光臨我們這簡陋的家。
我們過去也曾是富裕人家，
但如今卻淪落至此，
讓國家的神明，偉大的神明寄宿於此，
實在是惶恐不安，但今日
天色已晚，今晚就請大神
在此歇息，明日，我們僅以Inau
恭送大神離去。」
他一邊說著，一邊一遍又一遍地行禮。
老婦人在東邊的窗戶下
鋪上墊子，將我放在那裡。
然後，大家都睡了，很快就發出了響亮的鼾聲。
我坐在我的身體，耳朵和耳朵之間，
不久，在午夜時分，
我起身。
我靜靜地吟唱著「銀之滴，紛紛落下於周圍，
金之滴，紛紛落下於周圍」的歌謠，
在這家的左邊和右邊，
發出美妙的聲音，飛翔著。
當我拍打翅膀時，我的周圍，
美麗的寶物，神明的寶物，發出清脆的聲音，
四處散落。
頃刻之間，我將這間小屋，變成了充滿華麗寶物，
神明寶物的地方。
我吟唱著「銀之滴，紛紛落下於周圍，
金之滴，紛紛落下於周圍」的歌謠，
在轉瞬之間，將這間小屋，變成了金碧輝煌的房屋，
寬敞的家宅，屋內堆滿了華麗的寶物，
神明的寶物，並迅速製作了精美的服飾，
裝飾著房屋。
我將這間寬敞的房屋，裝飾得比富豪的家
還要華麗。完成這一切後，
我恢復原狀，坐在我的頭盔，
耳朵和耳朵之間。
我讓這家人做了一個夢，
讓他們知道，Ainu的Nispa因為運氣不好而變得貧窮，
被那些昔日貧窮如今富有的傢伙們
嘲笑和欺負，我看到後感到非常可憐，
我雖然只是一個卑微的神明，
但還是寄宿在人類的家中，
給予他們恩惠。
做完這些後，過了一會兒，天亮了，
這家人一起起床，
揉著眼睛，看向屋內，大家都
嚇得癱坐在地上。老婦人
放聲大哭，老人
也流下了大滴的眼淚，
不久，老人起身，
來到我的面前，一遍又一遍地行禮，
然後說道：
「我們還以為只是一場夢，
沒想到，這一切竟然是真的。
我們這簡陋的家，
能讓您光臨，就已經感激不盡了，
國家的神明，偉大的神明，
憐憫我們的不幸，
賜予我們莫大的恩惠。」他一邊哭著，
一邊說道。
然後，老人砍下Inau的木材，
製作了精美的Inau，裝飾著我。
老婦人也打扮好，
讓小孩子幫忙，砍柴、
打水，準備釀酒，轉眼之間，
就在上座擺放了六個酒桶。
然後，我與火之老女，老女神，
以及各種神明，談論著各種故事。
過了兩天左右，因為是神明喜愛的食物，
屋內早已瀰漫著
酒的香氣。
於是，我特意讓那個小孩子
穿上舊衣服，去村子裡
邀請那些昔日貧窮如今富有的村民。
目送孩子離去後，孩子挨家挨戶地
進入，並說明來意，
那些昔日貧窮如今富有的村民們，
都大聲嘲笑，
「真是奇怪，這些窮人
能釀出什麼酒，又有什麼
美味佳餚，竟然還邀請我們？
我們去看看有什麼好笑的。」
他們一邊說著，一邊成群結隊地
前來，從遠處，僅僅是看到那間房屋，
就驚訝不已，感到羞愧，直接返回的也有，
來到房屋前，嚇得癱坐在地上的也有。
這時，房屋的女主人走了出來，
拉著每個人的手，請他們進入屋內，
大家都匍匐前進，
沒有人敢抬頭。
這時，房屋的主人起身，
用像杜鵑鳥一樣美妙的聲音說道：
他講述了事情的來龍去脈，
「像這樣，我們這些貧窮的人，無法毫無隔閡地
互相往來，
但大神憐憫我們，我們沒有任何邪惡的想法，
所以才得到了這樣的恩惠，
從今以後，我們全村人，都是一家人，
所以希望大家能夠和睦相處，
互相往來。」
人們聽後，
一遍又一遍地搓著手，
向房屋的主人道歉，並商議著
從此以後要和睦相處。
大家也向我行禮。
完成這些後，人們的心情都變得柔和起來，
舉辦了盛大的酒宴。
我與火神、家神、
御幣棚的神明們，一邊交談，一邊
欣賞著人們跳舞、唱歌的樣子，
感到非常高興。然後，
過了兩三天，酒宴結束了。
看到人們和睦相處的樣子，
我感到很安心，
向火神、家神、
御幣棚的神明們告別。
完成這些後，我回到了自己的家。
在我回來之前，我的家已經擺滿了美麗的御幣，
以及美酒。
於是我派遣使者，
邀請了遠近的神明，舉辦了盛大的酒宴，
在宴席上，我向神明們
詳細講述了訪問人類村莊時的
村莊狀況，以及發生的事情，
神明們都大大地稱讚了我。
神明們離開時，我贈送了他們
兩個或三個美麗的御幣。
看向那個Ainu村莊，
如今已經恢復了平靜，人們
都和睦相處，那位Nispa
成為了村莊的首領，
他的孩子，如今也已經成年，
娶妻生子，
孝順父母，
無論何時何地，只要釀了酒，
都會在酒宴開始時，將御幣和美酒送給我。
我也坐在人類的後面，
隨時隨地
守護著人類的國家。
貓頭鷹神這樣講述著。
```
