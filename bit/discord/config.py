import os

guild_ids = [987673868430872626]
bug_reports_chat=987745873725390938
token = 'OTg2NTI0OTQxNDg4ODg1ODAx.GlkNRa.33q7wSlpxi8_q0xO7NhV77Ne5nWGYws69seqTI'
apikey = "LIVDSRZULELA"
owner_role_id = 988714473118380072
timer_role_id = 987394712736526506
bot_role = 987548809267646477
result_path = 'database/result.json'
russian_ban_word = r'(?:без|бес|в|во|воз|вос|возо|вз|вс|вы|до|за|из|ис|изо|на|наи|недо|над|надо|не|низ|нис|низо|о|об|обо|обез|обес|от|ото|па|пра|по|под|подо|пере|пре|пред|предо|при|про|раз|рас|разо|с|со|су|через|черес|чрез|а|ана|анти|архи|гипер|гипо|де|дез|дис|ин|интер|инфра|квази|кило|контр|макро|микро|мега|мата|мульти|орто|пан|пара|пост|прото|ре|суб|супер|транс|ультра|зкстра|экс|(?<= ))[ъь]?(?:(?:[хx][уy][ейiяyи]|[pп][иёе][zзsсc][dд]|[eе][лl][dд]|[еёeiи][бb]|шлю|твар|хер|мраз|шалав|манд|сипов|секел|поц|дроч|залуп|минд?ж|пид[оа]|курв|сперм|г[ао]нд|менстр|кун[аи]|сра[тл]|сса[тл]|бзд|перд|дри(?:ст|щ)|говн|жоп|целк|трах|харит|минет|блев|малаф|вагин)о*)+(?:адь|ак|алей|ан|ян|анин|янин|анк|янк|ар|арь|ариц|арк|ач|ени|ани|еств|ств|есть|ость|ец|к|изм|изн|ик|ник|нин|ин|атин|ист|иц|ниц|их|л|лк|льн|льник|льщик|льщиц|н|ог|г|р|от|ет|тель|итель|ун|чик|щик|чиц|ыш|ал|ел|аст|ат|ев|ов|енн|онн|енск|инск|ив|ит|овит|лив|шн|оват|еват|тельн|уч|юч|яч|чат|чив|а|я|е|и|нича?|ну|ова|ева|ствова|ся|сь|о|ск|жды|учи|ючи|то|либо|нибудь|ание|ение|ба|ь|исса|эсса|ива|ествова|изова|ирова|изирова|ства|ка|яка|ича|б|об|ытьб|в|ав|ощав|овлив|елив|члив|овь|o|тв|овств|инств|тельств|ляв|аг|инг|ург|уг|ыг|д|ад|иад|арад|оид|ядь|ое|ые|аж|ёж|ёжь|оз|ки|очки|ушки|нюшки|унюшки|еньки|ошеньки|охоньки|ами|ками|ай|атай|ей|ачей|ий|овий|стви|ни|ани|овани|ени|e|арий|ери|орий|ти|т|ци|аци|изаци|ици|нци|енци|ачий|ичий|a|ой|кой|уй|тяй|чак|авк|овк|ловк|анек|енек|онек|ышек|ежк|евик|овник|еник|ейник|арник|атник|истик|овщик|айк|ейк|инк|онк|унк|ок|онок|чонок|ушок|ерк|урк|вск|евск|овск|еск|ческ|ическ|истичес|лезск|эзск|йск|ейск|ийск|имск|нск|анск|ианск|унск|тельск|етк|отк|ютк|ук|чук|ацк|ецк|чк|ачк|ечк|ичка|очк|шк|ашк|ёшк|ишка|ишко|ушк|ышк|ык|ульк|усеньк|ошеньк|оньк|охоньк|юк|як|няк|ль|ла|ло|аль|овал|ёл|ель|ил|ол|оль|ул|ыль|онизм|им|ом|м|ком|иком|ышком|няком|уном|ишом|ым|нь|уган|иан|овиан|лан|ман|ебн|обн|евн|ивн|овн|ень|ен|ён|мен|смен|яжн|знь|езн|овизн|озн|иозн|бин|овин|лин|елин|нин|жан|чан|овчан|ичан|инчан|тян|итян|чин|щин|овщин|льщин|йн|ейн|нн|анн|ованн|ированн|ённ|овенн|ственн|менн|ионн|ационн|он|арн|орн|сн|снь|отн|ятн|ичн|иничн|очн|ашн|ишн|ышн|альн|идальн|иальн|ональн|уальн|ельн|абельн|ибельн|ительн|ильн|ынь|иян|ко|очко|енько|ошенько|онько|охонько|но|овато|атарь|ер|p|онер|мейстер|up|ор|вор|тор|атор|итор|ур|тур|amyp|итур|ырь|яр|с|ис|анс|есс|ус|ариус|ть|am|иат|дцать|надцать|евт|итет|нит|инит|ант|ент|мент|амент|емент|оть|иот|имость|ность|нность|енность|тость|ут|у|y|ку|еньку|оньку|ому|ану|оту|х|ах|ках|ох|ух|ц|авец|овец|лец|омец|нец|енец|инец|овиц|лиц|овниц|ениц|атниц|униц|ичниц|очниц|ешниц|льниц|тельниц|льц|ч|ич|евич|ович|нич|ыч|ш|аш|иш|айш|ейш|ошь|ош|уш|оныш|ащ|ищ|ище|ища|бищ|овищ|лищ|ущ|еющ|ы|ажды|ою|ую|остью|мя|ая|ее|ше|ший|ши|вши|вш|ёх|до|по|ему|рас|(?=.))*(?:ь|о|е|а|ам|ами|ас|am|ax|ая|е|её|ек|ей|ем|еми|емя|ex|ею|ёт|ёте|ёх|ёшь|и|ие|ий|й|им|ими|ит|ите|их|ишь|ию|jу|м|ми|мя|о|ов|ого|ое|оё|ой|ом|ому|ою|cm|у|ум|умя|ут|ух|ую|шь|(?=[^\w]))?'
allowed_host = 'https://'
banned_hosts = ['https://t.me', 'https://vk.com']
url_regex = r"[(http(s)?):\/\/(www\.)?a-zA-Z0-9@:%._\+~#=]{2,256}\.[a-z]{2,6}\b([-a-zA-Z0-9@:%_\+.~#?&//=]*)"
newcoming_id = 987433970922836068
prefix = '!'
mood_channel_id = 988384418236350464
emojis = {
    '😡':988385993273016340,
    '😭':988385843087552542,
    '🥲':988385717229092884,
    '😆':988385641798725632
}
reporter = 987744610027724820
path = '\\'.join(os.path.abspath('config.py').split('\\')[:-1])

class mafia:
    def __init__(self):
        self.mafia_roles = """Детектив — может застрелить игрока или узнать его роль.
        Священник — может застрелить игрока или узнать его роль, но взамен тоже покажет свою роль.
        Судья — может узнать роль и спасти от смерти.
        Журналист — может выбрать двух игроков и узнать, на одной они стороне или нет.
        Тюремщик — может узнать роль, и если это преступник, то он автоматически отправляется в тюрьму.
        Шериф — может застрелить игрока.
        Доктор — спасает от смерти.
        Телохранитель — выбирает игрока и погибает вместо него.
        Лунатик — притворяется одним из мафиози.
        Красотка — выбирает игрока, и он не может воспользоваться своими способностями.
        Поклонница — может проверить игрока.
        Крёстный отец — игрок, которого он выберет, не может голосовать днём.
        Вор — выбирает игрока, и он не может пользоваться своими способностями ночью.
        Адвокат — может узнать роль одного игрока.
        Стукач — может оклеветать игрока.
        Маньяк — может застрелить игрока.
        Потрошитель — может застрелить игрока, если он не мирный житель.
        Аферист — игрок, которого он выбрал, голосует как аферист.
        Якудза — сражается и против мафии, и против мирных жителей.
        Мирный — ничего не делает)
        Мафия — выбирает кого застрелить""".split('\n')
        self.mafia_roles_info = dict()
        for i in self.mafia_roles:
            tmp = i.split(' — ')
            self.mafia_roles_info[tmp[0]] = tmp[1]
        self.mafia_players = {
            'Обычный': {
                '3-5': {
                    "Мирный": 4, 
                    'Мафия': 1
                },  
                '6-8': {
                    'Мирный': 5,
                    'Мафия': 2,
                    'Доктор': 1,
                },
                '9-11': {
                    'Мирный': 6,
                    'Мафия': 3,
                    'Доктор': 1,
                    'Детектив': 1,
                },
                '12-14': {
                    'Мирный': 7,
                    'Мафия': 3,
                    'Доктор': 1,
                    'Детектив': 1,
                    'Красотка': 1,
                    "Маньяк": 1
                },
                '15-18': {
                    'Мирный': 10,
                    'Мафия': 3,
                    'Доктор': 1,
                    'Детектив': 1,
                    'Красотка': 1,
                    "Маньяк": 1,
                    'Потрошитель': 1
                },
            },
            "Экстра": {
                '3-5': {
                    "Мирный": 3, 
                    'Мафия': 1,
                    'Доктор': 1,
                },  
                '6-8': {
                    'Мирный': 3,
                    'Мафия': 2,
                    'Доктор': 1,
                    'Священник': 1,
                    'Маньяк': 1
                },
                '9-11': {
                    'Мирный': 4,
                    'Мафия': 3,
                    'Доктор': 1,
                    'Детектив': 1,
                    "Священник": 1,
                    "Маньяк": 1
                },
                '12-14': {
                    'Мирный': 5,
                    'Мафия': 3,
                    'Доктор': 1,
                    'Детектив': 1,
                    'Красотка': 1,
                    "Маньяк": 1,
                    "Священник": 1,
                    "Лунатик": 1
                },
                '15-18': {
                    'Мирный': 7,
                    'Мафия': 3,
                    'Доктор': 2,
                    'Детектив': 1,
                    'Красотка': 1,
                    "Маньяк": 1,
                    'Потрошитель': 1,
                    "Вор": 1,
                    "Судья": 1
                },
            }
        }