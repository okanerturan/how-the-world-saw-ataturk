// The branching guided tour: a prologue that ends at a fork, six paths, and a finale.
// Every stop is a record id in data/gazes.jsonl whose latest check verdict is neither
// `not-found` nor `contradicted`. Each note is curatorial narration and must stay supportable
// by that record's fields or its vault note. `name` overrides the voice's display name.

export const PROLOGUE = {
  title: `The man and the moment`,
  line: `1919 to 1922: a general in Anatolia, a country that was supposed to be finished, and the first people who tried to say what they saw.`,
  stops: [
    {
      id: 'harbord-1919-10-16',
      note: `September 1919, Sivas. An American general sent to report on Armenia met the leader of the Turkish national movement and wrote to the Secretary of State that he was a Dardanelles commander, “a young man of force and keen intelligence”. The praise is measured and sits beside the Armenian fears Harbord also relayed, but it is one of the first foreign portraits.`,
    },
    {
      id: 'yahya-kemal-1921',
      note: `At home, a poet put it more boldly. Writing for the Istanbul press during the National Struggle, Yahya Kemal argued that since the Greek landing at İzmir Mustafa Kemal was no longer an individual but a symbol: “This work belongs not to one person but to a nation. Those who take Mustafa Kemal for one person are mistaken.”`,
    },
    {
      id: 'fevzi-cakmak-tbmm-1921-09-19',
      name: 'Fevzi Çakmak and İsmet İnönü',
      note: `September 1921, days after the battle of the Sakarya. From the front, Fevzi Çakmak and İsmet asked the Assembly to make the Commander-in-Chief a Marshal and give him the title Gazi, crediting his measures “on the battlefield itself” with the victory. The honours came from below, as requests, and the Assembly passed them unanimously by show of hands.`,
    },
    {
      id: 'clare-sheridan-1922-09',
      note: `A year later his army was at Smyrna. The British sculptor Clare Sheridan, there as a journalist, found the Gazi sphinx-like and unfathomable, with “hard determination” in his blue eyes: the one man who had led the Turks from overwhelming defeat to victory. From here the world’s gaze divides. Choose a path.`,
    },
  ],
};

export const PATHS = [
  {
    id: 'the-liberator',
    title: 'The Liberator',
    question: 'Who saw a liberator?',
    line: `From Libya to Korea, from Bengal to Lima, the colonised world read his victory as news about itself.`,
    next: ['the-founders', 'faith'],
    stops: [
      {
        id: 'senussi-1920-11-25',
        note: `The first to come was a Muslim leader from Africa. Ahmed Sharif as-Senussi, head of the Senussi order, whose work in Libya Kemal had seen for himself, sat as the Assembly’s guest in Ankara in November 1920, and Kemal thanked him at the banquet for urging the nationalists on since March 1920. His own words are not printed; his support is known from Kemal’s speech and from his Eid telegram praying for the struggle.`,
      },
      {
        id: 'dong-a-ilbo-1920',
        note: `At the other end of Asia, under Japanese rule, Korea’s national-movement newspaper Dong-A Ilbo covered “Kemal Pasha” again and again from the early 1920s, as a history running parallel to Korea’s own. Under the censor’s eye, admiring another nation’s liberation was a way of speaking about one’s own; the paper’s Kemal grew from “ambitious revolutionary” to “founder of the new country”.`,
      },
      {
        id: 'garvey-1922',
        note: `In September 1922, days after Smyrna, Marcus Garvey put him on the front page of The Negro World: “Mustapha Kemal has become the man to the hour.” He told his followers they would not be used in Britain’s war against the Turks, and answered the charge of barbarism by pointing at British bombing in Africa.`,
      },
      {
        id: 'nazrul-1922',
        note: `In Bengal the young Kazi Nazrul Islam, later Bangladesh’s national poet, greeted the Turkish army’s sword as vengeance for the colonised. His poem “Kamal Pasha”, in Agni-Veena (1922), carries the punning refrain “Kamal Tu Ne Kamal Kiya Bhai”: Kamal, you have worked a wonder, brother.`,
      },
      {
        id: 'al-islam-congress-cheribon-1922-10',
        note: `In Java, the Al-Islam Congress at Cheribon, led by Tjokroaminoto, cheered the victory over the Greeks and resolved to cable Mustafa Kemal its congratulations, with Arab donors paying for the telegram. A Dutch paper reported that the colonial authorities would not send it.`,
      },
      {
        id: 'el-imparcial-1922',
        note: `The news crossed the Atlantic too. In San Juan, Puerto Rico, El Imparcial ran a portrait titled “El Caudillo de Angora”: Turkey the first betrayed people to rise, and Kemal a sober, silent leader, “aclamado como salvador”, acclaimed as saviour.`,
      },
      {
        id: 'inc-gaya-1922-12',
        note: `In December 1922 the Indian National Congress, meeting at Gaya, carried by a large majority a resolution moved by the poet Sarojini Naidu: “This Congress congratulates Ghazi Kemal Pasha and the Turkish nation on their recent successes.” It pledged India to the struggle for Turkey’s free and independent status.`,
      },
      {
        id: 'rusafi-1923',
        note: `The Iraqi poet Ma’ruf al-Rusafi addressed an ode “To the hero of the greater East”, its opening verse a pun on the names Mustafa and Kemal: “You defeated the sons of Yunan with a victory that left the West in tumult and confusion.”`,
      },
      {
        id: 'jose-carlos-mariategui-1925',
        note: `From Lima, the Peruvian Marxist José Carlos Mariátegui saw not a strongman but a revolution, moved by “a spontaneous interior impulse”, with Kemal “el caudillo de la insurrección y de la victoria” against the Entente and English capitalism. It was a sympathetic synthesis from newspapers, and it says nothing of the Kurds, the Armenians or the single-party state.`,
      },
      {
        id: 'rabindranath-tagore-1926',
        note: `In November 1926 Rabindranath Tagore’s ship put in at Istanbul. Too unwell to go ashore, the Nobel poet received the press in his cabin and said the Turkish president had “showed us the way to civilization”. The two never met, but Tagore later asked him for books on Turkey, and Atatürk sent 41 volumes to his university.`,
      },
      {
        id: 'sukarno-1928-07',
        note: `In 1928 the young Indonesian nationalist Sukarno set Kemal’s victory at Afyon Karahisar beside Japan’s of 1905: a battle that “all Asia felt” as a victory of East over West. Twelve years later, in exile, he would call him a “giant”.`,
      },
      {
        id: 'sharawi-1935',
        note: `And in April 1935 the Egyptian feminist Huda Sha’arawi, in Istanbul for the international women’s congress, told him to his face that “Father of the Turks” was not enough: “for us you are Atasharq”, Father of the East. Her words survive through her memoirs, quoted by a critic who cited them to condemn her, and another scholar reports the saying independently.`,
      },
    ],
  },

  {
    id: 'the-founders',
    title: 'The Founders',
    question: 'Who tried to build one of their own?',
    line: `Kings, presidents and generals looked at Ankara and saw a method: how to make a modern state, and make it fast.`,
    next: ['the-liberator', 'changes-of-heart'],
    stops: [
      {
        id: 'zogu-1926-02',
        name: 'Ahmet Zogu (King Zog)',
        note: `In February 1926 Albania’s president, Ahmet Zogu, received Turkey’s first envoy and, by the envoy’s report, called the Turkish reforms an example for Muslim countries, Albania above all, with special sympathy for Mustafa Kemal. Two years later he crowned himself King Zog. His exact words are lost; only the dispatch survives.`,
      },
      {
        id: 'faisal-i-1927',
        note: `King Faisal I of Iraq told Turkey’s ambassador in London in 1927 that he followed the reforms, could only revere the Gazi’s genius, and had not expected such results when the national movement began: “There is no doubt that you will be a model to be followed by all Asian nations.”`,
      },
      {
        id: 'amanullah-1928-05-20',
        note: `In May 1928 Amanullah Khan of Afghanistan became the first foreign sovereign received in the new capital. At the banquet he set the two struggles side by side, called Atatürk his brother and the “sole author” of Turkey’s nine-year rise. He fell from power the next year.`,
      },
      {
        id: 'hikmat-sulayman-1935',
        note: `For the Iraqi politician Hikmat Sulayman, Kemal was a programme. On one historian’s account, after visiting Turkey in 1935 he wrote articles urging secularism and modernisation on Turkish lines, and in October 1936 the first army coup in the modern Arab world made him prime minister.`,
      },
      {
        id: 'jinnah-1938-12-26',
        note: `Weeks after Atatürk’s death, Muhammad Ali Jinnah, president of the All-India Muslim League, told its session at Patna: “In Kemal Ataturk the Islamic world has lost a great hero.” With that example before them, he asked, would India’s Muslims stay in the quagmire?`,
      },
      {
        id: 'chiang-kai-shek-1940-10',
        name: 'Chiang Kai-shek',
        note: `At war with Japan, Chiang Kai-shek used his National Day message of October 1940 to hold up Kemal’s ten years of fighting, state-building and reform. That spirit of resolve and hard, practical work, he told the Chinese, “should all be emulated by us”.`,
      },
      {
        id: 'mohammad-reza-pahlavi-1961',
        note: `Iran’s Reza Shah had gone to see for himself: in 1934, his son recalled, he visited neighbouring Turkey “to observe the remarkable progress made”. Mohammad Reza Shah, writing in 1961, credited the republic to Atatürk’s “dynamic leadership”, founded after the Turks had abolished their “archaic caliphate”.`,
      },
      {
        id: 'bourguiba-1965',
        note: `Habib Bourguiba, Tunisia’s president, told the Turkish Assembly in 1965 that the victory of the Sakarya was “the strongest memory of my twentieth year”, and that the Kemalist revolution had been a leaven for his own. He was candid too: Arab reserve towards Atatürk, he said, came from his stance on religion.`,
      },
      {
        id: 'sadat-1978',
        note: `Anwar Sadat grew up with Atatürk’s photograph in the family house, his father calling him “a great man”. At the military academy, he wrote, “Ataturk continued to be my ideal. I started to read books on the Turkish Revolution.” The memoir is retrospective, written when he was already president.`,
      },
      {
        id: 'ben-bella-1984-07',
        note: `Ahmed Ben Bella, Algeria’s first president, now in exile, admired the man who had defied the Greeks and the Western powers behind them, and argued with one choice: “His counting the Turks as Western was a very vital mistake. But that aside, I have great admiration for him.”`,
      },
      {
        id: 'elcibey-1992',
        note: `When the Soviet Union broke up, the new Turkic republics reached for the same model. Azerbaijan’s President Ebülfeyz Elçibey told the Turkish Assembly in 1992: “Our first road is Mustafa Kemal’s road; after that we will build our state.”`,
      },
      {
        id: 'karimov-2000-10-17',
        note: `In Tashkent in 2000, Uzbekistan’s President Islam Karimov went further than any of them: “My path is Atatürk’s path. I took Atatürk as my model.” Seventy-four years after Zogu, the founders were still coming.`,
      },
    ],
  },

  {
    id: 'enemies-who-saluted',
    title: 'Enemies Who Saluted',
    question: 'Who fought him, and saluted?',
    line: `The soldiers and statesmen who stood against him, at Gallipoli and in Anatolia, were often the first to say how good he was.`,
    next: ['changes-of-heart', 'the-founders'],
    stops: [
      {
        id: 'venizelos-1921-07-08',
        note: `Begin with the enemy at full voice. In July 1921, out of office and in exile, the Greek statesman Eleftherios Venizelos warned British readers of The Times: “if Kemal reaches Constantinople the freedom of the sea is involved, and your supremacy in the Mediterranean.” Here Kemal is a threat, not yet a character.`,
      },
      {
        id: 'cew-bean-1921',
        note: `That same year Australia’s official war historian, C. E. W. Bean, who had walked the Gallipoli battlefield in 1919 and heard from a Turkish officer what Kemal had done there, wrote of “a formidable force under a formidable leader”. To have failed against such a man, historians suggest, made the Anzac defeat more honourable.`,
      },
      {
        id: 'townshend-1922',
        name: 'Sir Charles Townshend',
        note: `In May 1922 Sir Charles Townshend, the general who had surrendered to the Ottomans at Kut and was now an MP, rose in the Commons to defend Kemal as a patriot created by Allied blunders, compared him to Washington, and said: “I know him well and respect him.”`,
      },
      {
        id: 'kondylis-1924-06-21',
        note: `After the rout in Asia Minor, Athens argued over who was to blame. In June 1924 General Georgios Kondylis, later prime minister, told parliament that one need only compare the “masterly resistance” Mustafa Kemal had set against the Greek army “to understand the difference between the commanders”.`,
      },
      {
        id: 'prince-andrew-of-greece-1930',
        note: `Prince Andrew of Greece had commanded a Greek army corps in Asia Minor in 1921. In his 1930 account, Towards Disaster, he judged that one Greek manoeuvre might almost have destroyed the Turkish army, “if it had not been commanded by leaders of great military capacity as Mustapha Kemal Pasha and Ismet Pasha.”`,
      },
      {
        id: 'liddell-hart-1930',
        note: `The British strategist B. H. Liddell Hart, writing the history of the war that same year, remembered “the then unknown Mustapha Kemal” at Anzac, and counted him with Liman von Sanders among the “able commanders” Allenby had to outwit in 1918.`,
      },
      {
        id: 'venizelos-1934-01-12',
        note: `Then the turn. On 12 January 1934 Venizelos, the man behind the 1919 Smyrna landing, wrote to the Nobel committee proposing Mustafa Kemal for the Peace Prize: “The man to whom this invaluable contribution to the cause of peace is due is, of course, the President of the Turkish Republic.” The letter also served the Greek-Turkish pact Venizelos had signed in 1930; the committee never wrote an evaluation.`,
      },
      {
        id: 'salonika-city-council-1938',
        note: `When he died in November 1938, his birth city, Greek Thessaloniki since 1912, voted to give his name to the street where he was born, choosing mourning over grievance. Greece’s leader, Ioannis Metaxas, went to the funeral in person.`,
      },
      {
        id: 'harington-1940',
        note: `General Sir Charles Harington had commanded the Allied forces at Constantinople in 1920–23. Looking back in 1940 he called his old adversary “a real soldier”, who held the Greeks on the Sakarya and at Afyon “saw his chance and seized it”, though he also noted that Allied arms stocks had fed the Turkish army.`,
      },
      {
        id: 'wavell-1940',
        note: `Field Marshal Wavell, writing Allenby’s life the same year, named him one of “two of the best Turkish commanders” of 1918: “the future Ataturk, who was to regenerate the Turkish nation”.`,
      },
      {
        id: 'hawke-1990',
        note: `Anzac Day 1990, Lone Pine, the 75th anniversary. Australia’s prime minister, Bob Hawke, honoured the Turkish dead as men “dying in defence of their homeland, inspired by the indomitable leadership of a Man of Destiny”, known to history as Kemal Atatürk.`,
      },
      {
        id: 'karamanlis-2008-01-24',
        note: `And in 2008 Kostas Karamanlis, on the first official visit of a Greek prime minister since 1959, wrote at Anıtkabir that “Kemal Ataturk and Eleftherios Venizelos had the political courage, will and vision” not to let the tragedies of the past block peace. The two old enemies end this path side by side.`,
      },
    ],
  },

  {
    id: 'faith',
    title: 'Faith and the Caliph',
    question: 'What did the believers see?',
    line: `In 1924 he abolished the Caliphate. Believers never agreed about him, and some of the most moving words come from those who disagreed most.`,
    next: ['changes-of-heart', 'the-liberator'],
    stops: [
      {
        id: 'ahmad-shawqi-1922',
        note: `In 1922 Egypt’s “Prince of Poets”, Ahmad Shawqi, hailed the victor as a new conqueror of Islam: “Allahu akbar, how many wonders in the conquest! O Khalid of the Turks, renew Khalid of the Arabs.” The same poem praised him for sparing the monks and the cross in war.`,
      },
      {
        id: 'said-nursi-1923',
        note: `The scholar Said Nursi came to Ankara in 1922 to applause, hoping for a republic built on the Qur’an, and found what he called a current of atheism. When Kemal rebuked him before the deputies for his letter on prayer, he answered: “Pasha! Pasha! After belief, the most elevated truth in Islam is the obligatory prayers.” Offered posts, he declined. The scene is his movement’s own memory of it.`,
      },
      {
        id: 'abdulmecid-ii-1924',
        note: `On 3 March 1924 the Caliphate was abolished and the last Caliph, Abdülmecid II, was deposed and expelled. In exile at Territet he told a British journalist: “Those who combat its influence cannot be numbered among the servants of progress.” Kemal is named only in the journalist’s framing.`,
      },
      {
        id: 'ahmad-shawqi-1924',
        note: `Shawqi mourned the Caliphate in a new poem, yet refused the word others were using: “Shall I say that he who revived the community is an apostate, and that he who restored rights is a libertine?” He did not curse; he asked that advice be carried to the Ghazi, so that he might turn back.`,
      },
      {
        id: 'rashid-rida-manar-1928-10',
        note: `In Cairo, Rashid Rida’s al-Manar fought the reforms for years. Yet even while attacking the new Latin alphabet in 1928, its editorial conceded: “by my life, it is a great soul and a far-reaching ambition, though we Muslims abhor this new plan.”`,
      },
      {
        id: 'iqbal-1936',
        note: `Muhammad Iqbal, the poet-philosopher often called the spiritual father of Pakistan, took his defence. Answering Nehru’s charge that Turkey had left Islam, he wrote in 1936: “it is only the spirit of Islam that has worked out through the Ataturk”, while still calling the Turkish Qur’an and the Swiss code errors.`,
      },
      {
        id: 'muhammadiyah-meeting-surabaya-1938',
        note: `When he died, believers far away mourned him as one of their own. In Surabaya, the Muhammadiyah branch opened a public meeting with a minute’s silence for “this great Islamite”, and a prayer from the Qur’an was recited.`,
      },
      {
        id: 'roncalli-1938',
        note: `In Istanbul the Vatican’s envoy, Angelo Roncalli, the future Pope John XXIII, prayed for him alongside the Greek Orthodox patriarch who had also died, setting aside the “cold sentiments” others held and leaving judgment to a Lord he believed meek and kind. The diary passage is known only in a later English quotation, and its date is muddled in the source.`,
      },
      {
        id: 'sayyid-qutb-zilal-1960',
        note: `For Sayyid Qutb, the Muslim Brotherhood’s ideologue, writing his Qur’an commentary in the 1950s and 60s, Atatürk’s movement was the clearest case of one “uncompromising in its enmity to everything Islamic”, and the end of the Caliphate the loss of the last institution that united Muslims.`,
      },
      {
        id: 'khomeini-1978',
        note: `Ayatollah Khomeini condemned Reza Shah’s ban on the veil as a “shameful imitation of the ungodly Ataturk”. His target was Tehran; Atatürk is the model he blamed. The date is approximate.`,
      },
      {
        id: 'john-paul-ii-1979-11-28',
        note: `In November 1979 John Paul II laid a wreath at Anıtkabir. That evening, Turkish newspapers reported, he told President Korutürk that he was the first pope to bow there, and that his “admiration for Atatürk and the Turkish State” rested on its treatment of religious and ethnic communities.`,
      },
      {
        id: 'benedict-xvi-2006-11-28',
        note: `And in 2006, two months after his Regensburg lecture had angered much of the Muslim world, Benedict XVI began his journey to Turkey at Anıtkabir, writing that he gladly made his own the founder’s words: “peace at home, peace in the world”.`,
      },
    ],
  },

  {
    id: 'claimed-by-every-creed',
    title: 'Claimed by Every Creed',
    question: 'Whose side was he on?',
    line: `Communists, fascists and liberals each found their own Kemal. He belonged to none of them, and several of them said so.`,
    next: ['changes-of-heart', 'enemies-who-saluted'],
    stops: [
      {
        id: 'stalin-pravda-1920-11',
        note: `November 1920. Soviet Russia stood ready to back Ankara against the Entente, and Stalin, then commissar for nationalities, told Pravda the struggle would win “together with the Kemalists, if they do not betray the cause of the liberation of the oppressed peoples”. He already expected a swing to the Right.`,
      },
      {
        id: 'lenin-aralov-1921',
        note: `Lenin, briefing his envoy to Ankara at the end of 1921, put it plainly: “Of course, Mustafa Kemal Pasha is not a socialist”, but a good organiser, a talented commander and a clever statesman leading a bourgeois-national revolution. The words are the envoy’s, recalled decades later.`,
      },
      {
        id: 'mussolini-1922-09',
        note: `On the far right, the Fascist leader Benito Mussolini read the victory of September 1922 coolly: “Kemal Pasha’s victory is definitive as regards Anatolian territory.” He saw it as the product of French arms against Britain, and a lesson that Europe needed a lasting peace.`,
      },
      {
        id: 'ho-chi-minh-1924-01-01',
        name: 'Ho Chi Minh',
        note: `Writing in L’Humanité in 1924 as Nguyen Ai Quoc, the young Ho Chi Minh admired the Turks for tearing up Sèvres and founding a republic, then drew the Marxist line: “like all bourgeois revolutions, the Turkish revolution is profitable only to one class: the moneyed class.”`,
      },
      {
        id: 'stalin-sun-yat-sen-1927',
        note: `By 1927 Stalin had a label. Asked whether China could have a Kemalist revolution, he called it “a revolution of the top stratum, a revolution of the national merchant bourgeoisie”, turned against peasants and workers. The Soviet line had moved from support with a warning to a class verdict.`,
      },
      {
        id: 'carlo-sforza-1931',
        note: `Liberals saw something else. Carlo Sforza, Italy’s former foreign minister and once its High Commissioner at Constantinople, wrote in 1931 that of all the post-war dictators only Mustafa Kemal seemed a success, because he practised self-restraint and dropped the caliphate’s world claims. He said he had judged so in 1919.`,
      },
      {
        id: 'hitler-1933',
        note: `In July 1933 Hitler called Atatürk’s Turkey “a star in the darkness”. The phrase ran on the front page of the Völkischer Beobachter and, a historian finds, became the Nazi line on Turkey. Only the phrase survives; the full interview has not been seen.`,
      },
      {
        id: 'herriot-1934',
        note: `The French Radical Édouard Herriot came back from a 1933 visit with a rationalist’s Kemal: “The Ghazi believes in science, in reason”, a disciple, “unconscious perhaps”, of Auguste Comte and Descartes. He said it in Ankara’s own French-language review.`,
      },
      {
        id: 'ledesma-ramos-1935',
        name: 'Ramiro Ledesma Ramos',
        note: `The Spanish fascist Ramiro Ledesma Ramos, writing under a pseudonym in 1935, simply put him in the row: the “national revolutions” of astonishing success were “Mussolini, Kemal, Hitler and – why not? – Stalin”.`,
      },
      {
        id: 'mao-zedong-1940-01',
        note: `Mao Zedong, in January 1940, granted that a “petty Kemalist dictatorship of the bourgeoisie” had arisen in special conditions, but insisted China could not repeat it: Kemalist Turkey, he wrote, had thrown herself “into the arms of Anglo-French imperialism”.`,
      },
      {
        id: 'orwell-1943-10-22',
        note: `George Orwell noticed the scramble. In 1943 he recalled that “when almost any ally against Fascism seemed acceptable, left-wingers found themselves praising Mustapha Kemal”, as an example of the Left’s readiness to accept “very doubtful allies”.`,
      },
      {
        id: 'nazim-hikmet-1945-11-10',
        note: `The last word goes to a communist who was also a Turk. In 1945, a prisoner in Bursa, the poet Nâzım Hikmet published lines from his epic of the War of Independence in an Atatürk anniversary issue, showing Kemal on Kocatepe before the 1922 offensive: “He looked like a blond wolf / And his blue eyes flashed like flint.”`,
      },
    ],
  },

  {
    id: 'changes-of-heart',
    title: 'Changes of Heart',
    question: 'Who changed their mind?',
    line: `The most revealing gazes are the ones that moved. The same people, years apart.`,
    next: ['faith', 'enemies-who-saluted'],
    stops: [
      {
        id: 'churchill-1920',
        note: `March 1920. Winston Churchill, Secretary of State for War, listed “the hostile forces of Mustapha Kemal” among Britain’s worries for Mesopotamia and warned of their junction with the Bolsheviks.`,
      },
      {
        id: 'churchill-1929',
        note: `Nine years later, in The World Crisis, Churchill wrote of “the Man of Destiny whom we have met in these volumes on the Gallipoli Peninsula”, a man with the qualities of a “Warrior Prince”, and called his 1922 offensive “complicated and masterly”. He still tied the victorious army to the burning of Smyrna.`,
      },
      {
        id: 'lloyd-george-1920',
        note: `December 1920. Prime Minister David Lloyd George dismissed “Mustapha Kemal, who is a mutinous general”, and refused to buy his good will by giving him Smyrna against the Greeks’ wishes.`,
      },
      {
        id: 'lloyd-george-1938',
        note: `In 1938, long out of office, Lloyd George wrote that Kemal had been the unexpected “portent” at the peace conference: “It was owing to his prompt and daring leadership that the ineffective and bungled British attack at Suvla Bay had been checked.” Allied intelligence about him, he admitted, had been “unintelligent”.`,
      },
      {
        id: 'lawrence-1919-09-15',
        note: `T. E. Lawrence, in a secret memorandum of September 1919, judged him “much the more able” than Enver but without Enver’s magnetism, and too hesitant to act except in desperate or very favourable circumstances.`,
      },
      {
        id: 'lawrence-1934-11-28',
        note: `Fifteen years later the hesitation had gone from Lawrence’s verdict. To Liddell Hart he wrote, in November 1934: “Mustapha Kemal was a great patriot, and anti-foreign from 1913 onwards.”`,
      },
      {
        id: 'huseyin-avni-tbmm-1922-05-04',
        note: `A change of heart could take two days. On 4 May 1922, in a closed sitting, the Erzurum deputy Hüseyin Avni fought the clause handing the Commander-in-Chief the Assembly’s powers: “a man is not given a thousand jobs, gentlemen; be jealous of your right.” His quarrel was with the office, not the man.`,
      },
      {
        id: 'huseyin-avni-tbmm-1922-05-06',
        note: `Kemal answered him sharply. On 6 May Hüseyin Avni replied: “there is no one who does not know the degree of the Pasha’s sacrifice”, and promised to say everything to him plainly rather than whisper behind his back.`,
      },
      {
        id: 'arnold-toynbee-1922',
        note: `Arnold Toynbee had edited Britain’s 1916 Blue Book on the Armenians. After reporting the Greek-Turkish war, he wrote in 1922, without ever having met him, that Kemal “proved by a personal demonstration that a Turk can be his own master in Anatolia”.`,
      },
      {
        id: 'toynbee-1954',
        note: `Three decades on, in A Study of History, Toynbee found his genius in a refusal: turning down the pan-Turanian “mirage” was “one of the most signal evidences of Ghazi Mustafa Kemal Ataturk’s political genius”.`,
      },
      {
        id: 'ben-badis-1924',
        note: `In Algeria, Abdelhamid Ben Badis had praised the Kemalists while they fought. In March 1924, weeks after the abolition, he published “The Great Catastrophe” and charged them with crimes against the Caliphate and the faith: “we turned a blind eye to their evils to preserve Islamic unity — and never imagined they would abolish the Caliphate.”`,
      },
      {
        id: 'ben-badis-1938',
        note: `Fourteen years later the same pen wrote his obituary: “the greatest man humanity has known in modern history”, the hero of Gallipoli and the Sakarya. Mustafa Kemal, Ben Badis now wrote, “did not rebel against Islam but against those who call themselves Muslims”.`,
      },
    ],
  },
];

export const FINALE = {
  title: 'The Flame',
  line: `After 1938 the world kept coming back to him, and the praise outlived the century.`,
  stops: [
    {
      id: 'eisenhower-1959-12-06',
      note: `December 1959, a state dinner in Ankara. President Eisenhower called the changes made under Atatürk breathtaking in scope and swiftness: “an inspiration and a guiding light to all newly independent nations, determined on progress, prosperity, and peace.”`,
    },
    {
      id: 'kennedy-1963-11',
      note: `For the 25th anniversary of his death, in November 1963, John F. Kennedy recorded a tribute calling him one of the great men of the century, and the birth of the Turkish republic an unmatched example of “national self reliance”.`,
    },
    {
      id: 'mandela-1992-05-20',
      note: `In May 1992 Nelson Mandela said he was unable to accept the Atatürk International Peace Prize; the news agency that reported it recorded no reason. In the same breath he said: “I have a great deal of respect for Ataturk and for the Turkish people themselves.”`,
    },
    {
      id: 'clinton-1999',
      note: `In November 1999 Bill Clinton told the Turkish Assembly: “In a sense, we are all here today because of Kemal Ataturk”, because he “pledged Turkey’s future to the democracy symbolized by this proud assembly.”`,
    },
    {
      id: 'pamuk-2007',
      note: `Orhan Pamuk, Turkey’s Nobel laureate, read the hats and dress codes from the inside: Atatürk, he wrote in 2007, “found a way of confronting the shame” that Westernised Turks felt before European eyes.`,
    },
    {
      id: 'obama-2009',
      note: `In April 2009 Barack Obama came from the mausoleum to the Assembly: “the greatest monument to Ataturk’s life is not something that can be cast in stone and marble. His greatest legacy is Turkey’s strong, vibrant, secular democracy.”`,
    },
    {
      id: 'guterres-2026-03-12',
      note: `In March 2026 the UN Secretary-General, António Guterres, accepting the Atatürk International Peace Award, said that Atatürk “understood that peace does not emerge by chance. It is a deliberate choice”, and that “peace at home” captured the spirit of the UN Charter.`,
    },
    {
      id: 'de-gaulle-1968-10-27',
      note: `We close where the flame was named. In October 1968 Charles de Gaulle stood in Dolmabahçe, the palace where Atatürk died, and wrote: “Atatürk pouvait mourir, puisque la lumière brillait, puisque la flamme brûlait, puisque le pays était en marche.” Atatürk could die, since the light was shining, since the flame was burning, since the country was on the march.`,
    },
  ],
};

// 10 November 1938: the reading of the weeks after his death opens with these records, in this order
// (well-known names, admiring voices first). The rest of that period follows by itself: people, then
// institutions, then newspapers. Every id must be a checked record whose `era` is `funeral`.
export const FUNERAL_LEAD = [
  'roosevelt-1938', 'lebrun-1938', 'jinnah-1938-12-26', 'farouk-1938', 'zahir-shah-1938-11-11', 'manuel-azana-1938',
  'hirohito-1938', 'ben-badis-1938', 'choudhry-rahmat-ali-1938', 'lyons-1938', 'prince-paul-yugoslavia-1938',
  'haj-amin-al-husseini-1938', 'nahhas-pasha-1938', 'loraine-1938-11-25', 'reuter-1938-11-22', 'albert-sarraut-1938-2',
  'zafar-ali-khan-1938-11-poem', 'ismet-inonu-assembly-1938-11-11', 'celal-bayar-1938-11-11', 'hitler-1938',
  'goebbels-1938-11', 'roncalli-1938',
];
