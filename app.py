import dash
from dash import Dash 
from dash import Output, Input, html, dcc, State
from dash.exceptions import PreventUpdate
import pandas as pd
import test

genre_list=['sports', 'romance', 'game', 'shounen', 'shoujo', 'demons', 'harem', 'magic', 'drama', 'mystery', 'ecchi', 'fantasy', 'comedy', 'thriller', 'historical', 'josei', 'police', 'shoujo ai', 'martial arts', 'adventure', 'kids', 'scifi', 'space', 'parody', 'cars', 'super power', 'yaoi', 'shounen ai', 'slice of life', 'military', 'action', 'supernatural', 'vampire', 'mecha', 'horror', 'psychological', 'samurai', 'music', 'hentai', 'school', 'dementia', 'yuri', 'seinen']
genre_list = [{'label': value, 'value': value} for value in genre_list]

Studio_list=['namu animation', 'triple x', 'breakbottle', 'toei animation', 'success co', 'studio junio', 'production ims', 'zerog', 'lilix', 'kaeruotoko shokai', 'comix wave films', 'gainax', 'future planet', 'studio voln', 'doga kobo', 'sprite animation studios', 'ph studio', 'oh production', 'dandelion animation studio llc', 'shirogumi', 'wtoon studio', 'life work', 'feel', 'acc production', 'seven', 'picture magic', 'studio fantasia', 'plum', 'telecartoon japan', 'dax production', 'studio 4c', 'bones', 'public amp basic', 'calf studio', 'panda factory', 'olm', 'studio 3hz', 'bestack', 'selfish', 'passione', 'shogakukan music amp digital entertainment', 'image house', 'cookie jar entertainment', 'dmmfutureworks', 'studio puyukai', 'kaname productions', 'daewon media', 'orange', 'gathering', 'view works', 'haoliners animation league', 'aubec', 'studio matrix', 'manglobe', 'cg year', 'egg', 'studio g1neo', 'glam', 'bouncy', 'gansis', 'studio bogey', 'gonzo', 'studio pierrot', 'studio who', 'studio cucuri', 'odolttogi', 'studio world', 'lide', 'olm digital', 'minami machi bugyousho', 'bridge', 'ekura animal', 'studio kikan', 'triangle staff', 'mili pictures', 'artland', 'diomedea', 'amber film works', 'mappa', 'tengu kobo', 'shochiku animation institute', 'tpo', 'acgt', 'studio hibari', 'dle', 'green bunny', 'typhoon graphics', 'landq studios', 'aic spirits', 'studio egg', 'areal', 'hal film maker', 'flavors soft', 'youc', 'agent 21', 'seven arcs', 'ufotable', 'studio 1st', 'satelight', 'nhk', 'domerica', 'fuji tv', 'dynamo pictures', 'animaruya', 'dongwoo aampe', 'studio deen', 'dwango', 'group tac', 'nakamura production', 'blue cat', 'dai nippon printing', 'tsuchida productions', 'karaku', 'studio z5', 'marza animation planet', 'wao world', 'madhouse', 'studio hakk', 'studio flag', 'studio khronos', 'silver link', 'blade', 'jcstaff', 'beijing huihuang animation company', 'anime antenna iinkai', 'gemba', 'shinei animation', 'trigger', 'animation do', 'magic bus', 'larx entertainment', 'polygon pictures', 'kokusai eigasha', 'trislash', 'drop', 'tnk', 'think corporation', 'project no9', 'cloverworks', 'trinet entertainment', 'studio moriken', 'joker films', 'msc', 'tatsunoko production', 'moogoo', 'cstation', 'studio jam', 'studio colorido', 'asread', 'darts', 'himajin planning', 'mushi production', 'tokyo movie shinsha', 'brain039s base', 'ishimori entertainment', 'milky cartoon', 'bampt', 'appp', 'studio gallop', 'lerche', 'shanghai foch film culture investment', 'natural high', 'schoolzone', 'thundray', 'jcf', 'garden lodge', 'heartbit', 'planet', 'nippon animation', 'studio march', 'kyoto animation', 'daichi doga', 'aic plus', 'asahi production', 'craftar', 'rising force', 'telescreen bv', '10gauge', 'chaos project', 'production reed', 'pastel', 'sparkly key animation studio', 'jinnis animation studios', 'eampg films', '81 produce', 'studio wombat', 'arcs create', 'strawberry meets pictures', 'echo', 'dongyang animation', 'platinum vision', 'ginga ya', 'kooki', 'charaction', 'fukushima gainax', 'threed', 'tms entertainment', 'c2c', 'moss design unit', 'barnum studio', 'japan vistec', 'tezuka productions', 'pine jam', 'studio flad', 'amuse', 'aic frontier', 'pb animation co ltd', 'anime r', 'visual 80', 'studio gokumi', 'gen productions', 'pierrot plus', 'mmdgp', 'wit studio', 'd amp d pictures', 'oz', 'kinema citrus', 'nut', 'aic build', 'daume', 'science saru', 'fanworks', 'khara', 'tama production', 'kyotoma', 'mook dle', 'ixtl', 'studio ponoc', 'kamikaze douga', 'teamkg', 'gcmay animation amp film', 'office takeout', 'nexus', 'echoes', 'radix', 'kachidoki studio', 'tokyo kids', 'ishikawa pro', 'oddjob', 'production ig', 'purple cow studio japan', 'remic', 'aic asta', 'ajiado', 'taki corporation', 'kenji studio', 'gohands', 'rockwell eyes', 'office take off', 'studio ghibli', 'topcraft', 'lidenfilms', 'ascension', 'realthing', 'actas', 'bandai namco pictures', 'studio anima', 'zexcs', 'xebec zwei', 'sting ray', 'ashi production', 'signal md', 'pie in the sky', 'studio lings', 'digital frontier', 'aic', 'keyeast', 'front line', 'studio 9 maiami', 'connect', 'bootleg', 'vega entertainment', 'gampg entertainment', 'code', 'creators in pack', 'enoki films', 'axsiz', 'telecom animation film', 'trex', 'hoods entertainment', 'studio nue', 'millepensee', 'bee media', 'artmic', 'tomovies', 'gakken eigakyoku', 'annapuru', 'studio sign', 'oxybot', 'naz', 'studio eromatick', 'sunwoo entertainment', 'xebec', '3xcube', 'opera house', 'emt²', 'kanaban graphics', 'digital media lab', 'yaoyorozu', 'studio comet', 'suzuki mirano', 'synergysp', 'piko studio', '8bit', 'sugar boy', 'jumondo', 'arms', 'eiken', 'white fox', 'dast', 'ilca', 'venet', 'issen', 'zerog room', 'bee train', 'geno studio', 'pollyanna graphics', 'tonko house', 'kazuki production', 'robot communications', 'studio lan', 'japan taps', 'studio zero', 'dwarf', 'steve n039 steven', 'onionskin', 'marvy jack', 'graphinica', 'anpro', 'studio live', 'minakata laboratory', 'seven arcs pictures', 'phoenix entertainment', 'primetime', 'l²studio', 'aic classic', 'hotline', 'studio acat', 'square enix', 'pink pineapple', 'kitty films', 'big bang', 'sanzigen', 'azeta pictures', 'troyca', 'shaft', 'yumeta company', 'the answer studio', 'studio ox', 'imagineer', 'pa works', 'yamato works', 'studio blanc', 'emon', 'qualia animation', 'at2', 'chiptune', 'hs pictures studio', 'm2', 'nomad', 'imagin', 'palm studio', 'animate film', 'heewon entertainment', 'pra', 'studio rikka', 'egg firm', 'trans arts', 'knack productions', 'shuka', 'ordet', 'david production', 'hoods drifters studio', 'genco', 'wawayu animation', 'creators dot com', 'sunrise', 'a1 pictures', 'tyo animations', 'lesprit', 'indeprox', 'studio core', 'rabbit gate', 'tamura shigeru studio', 'lmd', 'heloinc', 'asura film', 'layduce', 'encourage films', 'studio chizu', 'ripromo']
Studio_list = [{'label': value, 'value': value} for value in Studio_list]


Producer_list=['studio mausu', 'cherrylips', 'toei animation', 'ing', 'highlights entertainment', 'kadokawa daiei studio', 'tbs', 'ray', 'nippon shuppan hanbai nippan kk', 'tencent japan', 'kaeruotoko shokai', 'i0', 'sentai filmworks', 'comix wave films', 'liverpool', 'gainax', 'bs fuji', 'future planet', 'jay zone comic', 'oh production', 'nintendo', 'directions', 'gentosha comics', 'dandelion animation studio llc', 'audio planning u', 'shirogumi', 'ltd', 'cyclone graphics inc', 'memorytech', 'gen039ei', 'life work', 'wtoon studio', 'rironsha', 'three fat samurai', 'acc production', 'flying dog', 'picture magic', 'fujiko f fujio pro', 'studio fantasia', 'level5', 'plum', 'telecartoon japan', 'tablier communication', 'amgakuin', 'polygram japan', 'dax production', 'nintendo of america', 'toppan printing', 'hiroshi planning', 'coamix', 'takara tomy arts', 'public amp basic', 'tokuma japan', 'kadokawa pictures japan', 'film workshop', 'docomo anime store', 'gigno systems', 'aniplex of america', 'kansai telecasting', 'yuhodo', 'datam polystar', 'project lights', 'tavac', 'futabasha', 'zyc', 'olm', 'daiichikosho', 'dear stage inc', 'yomiko advertising', 'half hp studio', 'medicos entertainment', 'famimacom', 'bestack', 'greenwood', 'hiroshima television', 'nottv', 'notes', 'milky animation label', 'shogakukan music amp digital entertainment', 'azumaker', 'visual art039s', 'daiei', 'music ray039n', 'hasbro', '1st place', 'dmmfutureworks', 'cyberagent', 'tate anime', 'toshiba digital frontiers', 'ac create', 'viki', 'broccoli', 'age', 'vap', 'daiichi shokai co', 'mainichi shimbun', 'gmode', 'ntt docomo', 'orange', 'crei', 'chugai mining co', 'trans cosmos', 'rankinbass', 'ensky', 'kyoraku industrial holdings', 'pazzy entertainment', 'my theater dd', 'ms pictures', 'sammy', 'haoliners animation league', 'shelty', 'milestone music publishing', 'bandai namco entertainment', 'project eureka ao', 'bs japan', 'aubec', 'nihon ad systems', 'onlead', 'sony pcl', 'pony canyon enterprise', 'imagi', 'fmf', 'sogo vision', 'universal studios', 'nelvana', 'newgin', 'line corporation', 'sotsu music publishing', 'ishimori pro', 'hokkaido cultural broadcasting', 'studio g1neo', 'bouncy', 'universal entertainment', 'aline', 'gansis', 'freewill', 'klab', 'apollon', 'moe', 'studio pierrot', 'sony pictures entertainment', 'youmex', 'kinyosha', 'japan home video', 'shogakukan productions', 'cbs', 'showgate', 'kino production', 'sky perfect well think', '5pb', 'minami machi bugyousho', 'fuji creative', 'dmm pictures', 'tc entertainment', 'takara', 'shounen gahousha', 'kenmedia', 'tokyu recreation', 'studio kikan', 'triangle staff', 'studio izena', 'alchemist', 'acraft', 'kadokawa media taiwan', 'network', 'active', 'gyao', '4kids entertainment', 'ascii media works', 'baramiri', 'kadokawa contents gate', 'diomedea', 'saban brands', 'amber film works', 'usen', 'adores', 'miracle bus', 'capcom', 'asgard', 'bungeishunjuu', 'tpo', 'tsubasa entertainment', 'gimik', 'bishop', 'studio hibari', 'mainichi broadcasting system', 'imagica', 'yoon039s color', 'soeishinsha', 'ziz entertainment ziz', 'yomiuri shimbun', 'dle', 'green bunny', 'nada holdings', 'studio elle', 'nikkatsu', 'bstbs', 'jm animation', 'tv aichi', 'dive ii entertainment', 'landq studios', 'nexon', 'yahoo japan', 'ministry of the navy', 'kawade shobo shinsha', 'ai addiction', 'fuji pacific music publishing', 'techno sound', 'hal film maker', 'epicross', 'orchid seed', 'agent 21', 'sanrio', 'tv tokyo', 'studio tulip', 'bigface', 'studio zain', 'edge', 'onemusic', 'konami', 'good smile company', 'dream force', 'hot bear', 'nhk', 'unext', 'fuji tv', 'tokai television', 'animaruya', 'twin engine', 'flex comix', 'bandai', 'wowow', 'right gauge', 'lawson hmv entertainment', 'studio deen', 'akita shoten', 'production goodbook', 'dwango', 'enlight pictures', 'group tac', 'spo entertainment', 'north stars pictures', 'jinnan studio', 'tokyo mx', 'earth star entertainment', 'just pro', 'colopl', 'dji', 'yaoqi', 'dai nippon printing', 'akabeisoft2', 'i was a ballerina', 'keisei electric railway', 'rondo robe', 'studiorf inc', 'quick corporation', 'donuts', 'kadokawa shoten', 'pashmina', 'tap', 'visual vision', 'marza animation planet', 'harappa', 'wao world', 'magic capsule', 'madhouse', 'usagi ou', 'otogi production', 'penta show studios', 'walt disney japan', 'studio flag', 'coloredpencil animation design', 'nhkbs2', 'primastea', 'emi', 'team entertainment inc', 'overlap', 'hakuhodo', 'hakuhodo dy music amp pictures', 'tsukuru no mori', 'bushiroad music', 'nitroplus', 'jcstaff', 'nhk enterprises', 'yellow film', 'anime antenna iinkai', 'mobcast', 'meruhensha', 'shinei animation', 'world cosplay summit', 'gakken', 'trigger', 'contents seed', 'tsuritama partners', 'shizuoka daiichi television', 'cosmic ray', 'animation do', 'magic bus', 'c amp i entertainment', 'nippon television music', 'heroz', 'chiba tv', 'yoshimoto creative agency', 'comico', 'horipro', 'kokusai eigasha', 'beyond c', 'media do', 'hulu', 'nippon ichi software', 'sotsu', 'four some', 'cloverworks', 'rakuonsha', 'avex pictures', 'victor entertainment', 'trinet entertainment', 'digital works', 'studio moriken', 'marine entertainment', 'msc', 'tatsunoko production', 'suiseisha', 'hobibox', 'indigo line', 'comic umenohone', 'kitty media', 'nozomi entertainment', 'warner bros japan', 'media rings', 'asahi shimbun', 'bandai namco games', 'stardust promotion', 'evil line records', 'japan sleeve', 'links', 'qreazy', 'trinity sound', 'darts', 'hakoniwa academy student council', 'himajin planning', 'kadokawa', 'mushi production', 'tokyo movie shinsha', 'nelke planning', 'asmik ace entertainment', 'animax', 'kinoshita koumuten', 'china literature limited', 'milky cartoon', 'appp', 'gdh', 'east japan marketing amp communications', 'natural high', 'fujiampgumi games', 'angelfish', 'nichion', 'brave hearts', 'muse communication co', 'pansonworks', 'tmskyokuchi', 'chrono gear creative', 'yomiuri tv enterprise', 'madoka partners', 'studio gooneys', 'heartbit', 'cospa', 'planet', 'tasogare otomeamnesia production partners', 'fukuoka broadcasting system', 'teichiku entertainment', 'toshiba entertainment', 'lucky paradise', 'warner bros', 'tokuma shoten', 'kyoto animation', 'kids station', 'tencent penguin pictures', 'amg music', 'beam entertainment', 'felix film', 'asahi production', 'studio gram', 'marubeni', 'iwatobi high school swimming club', 'craftar', 'telescreen bv', 'tyo', 'hokkaido azmacy', 'nihon eizo', 'spacey music entertainment', 'discovery', 'diabolik lovers mb project', 'japananime', 'production reed', 'dynamic planning', 'pastel', 'jinnis animation studios', 'eampg films', 'innocent grey', 'blue eyes', 'marvelous aql', 'solid vox', 'nhn playart', '81 produce', 'kss', 'tv saitama', 'chippai', 'aquamarine', 'tohan corporation', 'echo', 'saban entertainment', 'dentsu', 'xflag', 'ginga ya', 'raku high student council', 'studio jack', 'movic', 'ytv', 'live viewing japan', 'on the run', 'kfactory', 'rikuentai', 'casio entertainment', 'cbc', 'voyager entertainment', 'tms entertainment', 'ai ga areba daijobu', 'sankyo planning', 'grooove', 'c2c', 'marvelous', 'barnum studio', 'miyagi television broadcasting', 'tezuka productions', 'neft film', 'hakuhodo dy media partners', 'amuse', 'agone', 'pixy', 'pb animation co ltd', 'xflag pictures', 'visual 80', 'yomiuri advertising', 'slowcurve', 'gen productions', 'pierrot plus', 'mmdgp', 'wit studio', 'd amp d pictures', 'kadokawa media house', 'bandai visual', 'studio tron', 'nbcuniversal entertainment japan', 'rakuten', 'fujishouji', 'atlus', 'jormungand production partners', 'kbs', 'bulls eye', 'cocoro free', 'qtec', 'enotion', 'ken on', 'mirai film', 'tohokushinsha film corporation', 'amino', 'oz', 'project no name', 'eye move', 'tv setouchi', 'procidis', 'tokuma japan communications', 'dena', 'assez finaud fabric', 'exa international', 'infinite', 'daume', 'picante circus', 'fanworks', 'shuuhei morita', 'tv tokyo music', 'cammot', 'parco', 'tose', 'khara', 'chukyo tv broadcasting', 'shinchosha', 'myung films', 'shizuoka broadcasting system', 'dentsu razorfish', 'kodansha', 'mary jane', 'viz media', 'shochiku', 'kyotoma', 'sega', 'romantica club', 'chukong technologies', 'bushiroad', 'dic entertainment', 'starchild records', 'studio take off', 'audio highs', 'age global networks', 'jade animation', 'bmg japan', 'avex entertainment', 'hipland music corporation', 'kanetsu co', 'mad box', 'china animation characters', 'geneon universal entertainment', 'studio noix', 'audio tanaka', 'radix', 'to entertainment', 'tokyo kids', 'academy productions', 'po10tial', 'production ig', 'purple cow studio japan', 'valkyria', 'remic', 'sunrise music publishing', 'digiturbo', 'ajiado', 'jidaigeki channel', 'tsuburaya productions', 'senran kagura partners', 'jy animation', 'iqiyi', 'shogakukan', 'kioon music', 'big west', 'synergy japan', 'seikaisha', 'kenji studio', 'cromea', 'ima group', 'studio ghibli', 'kimi to boku production partners', 'topcraft', 'animeigo', 'lidenfilms', 'ob planning', 'actas', 'nec avenue', 'anik', 'bandai namco pictures', 'fujio production', 'international digital artist', 'topinsight international co', 'design factory', 'universal pictures japan', 'studio zealot', 'sunny side up', 'ashi production', 'bsi', 'akom', 'project is', 'bs ntv', 'inu x boku ss production partners', 'shanghai tiantan culture amp media', 'miracle robo', 'sedic international', 'anime consortium japan', 'the berich', 'sound team don juan', 'sapporo television broadcasting', 'sakura create', 'aic', 'digital frontier', 'front line', 'jam', 'forecast communications', 'shufunotomo', 'hero communication', 'bootleg', 'mk pictures', 'image kei', 'frontier works', 'd3', 'zack promotion', 'fields', 'vega entertainment', 'drecom', 'gampg entertainment', 'kmmj studios', 'code', 'toranoana', 'enoki films', 'tosho printing', 'mag garden', 'toy039s factory', 'gree', 'telecom animation film', 'trex', 'ichijinsha', 'shingeki no kyojin team', 'omnibus japan', 'idea factory', 'soyuzmultfilm', 'ryukyu asahi broadcasting', 'hoods entertainment', 'kanon sound', 'toho', 'white bear', 'quaras', 'yamamura animation', 'wargaming japan', 'hobby japan', 'studio nue', 'inc', 'glovision', 'yomiuri telecasting', 'bee media', 'kiyosumi high school mahjong club', 'hisashishi videos', 'artmic', 'cygames', 'dtechno', 'studio kyuuma', 'gakken eigakyoku', 'drights', 'sanyo bussan', 'hoso seisaku doga', 'exit tunes', 'xing', 'naz', 'cyberconnect2', 'asatsu dk', 'aquaplus', 'air agency', 'gzbrain', 'sol blade', 'xebec', '3xcube', 'shanghai jump network technology', 'opera house', 'sony music entertainment', 'charaanicom', 'digital media lab', 'duckbill entertainment', 'studio comet', 'synergysp', 'plus one', 'animatsu entertainment', 'nippon columbia', 'subaru', 'bandai namco live creative', 'nichinare', 'jumondo', 'medianet', 'shochiku music publishing', 'bs11', 'moonbell', 'tv osaka', 'white fox', 'dast', 'furyu', 'ilca', 'ebook initiative japan co', 'bee train', 'queen bee', 'frencel', 'pioneer ldc', 'toshiba emi', 'nutech digital', 'robot communications', 'nishinippon broadcasting', 'righttracks', 'incs toenter', 'fujimi shobo', 'wako productions', 'studio lan', 'delfi sound', 'softx', 'aoni entertainment', 'olem', 'bilibili', 'nagoya tv housou', 'steve n039 steven', 'arcturus', 'hakusensha', 'lawson', 'sumitomo', 'softbank creative corp', 'banpresto', 'graphinica', 'kotobukiya', 'sme visual works', 'biglobe', 'animatic', 'warner music japan', 'medicrie', 'tomy company', 'studio chant', 'phoenix entertainment', 'primetime', 'feng', 'toho animation', 'nippon television network', 'houbunsha', 'sun tv', 'shinano kikaku', 'kobunsha', 'aniplex', 'marui group', 'lastrum music', 'nihikime no dozeu', 'dmmcom', 'atx', 'meiji seika', 'enterbrain', 'walkers company', 'sanx', 'konami digital entertainment', 'pencil', 'volks', 'square enix', 'animac', 'pink pineapple', 'kitty films', 'hobi animation', '12 diary holders', 'cotton doll', 'big bang', 'az creative', 'jtb entertainment', 'trilogy future studio', 'sanctuary', 'lune pictures', 'shaft', 'bandai namco rights marketing', 'studio kelmadick', 'nihon falcom', 'king records', 'yumeta company', 'the answer studio', 'tv asahi', 'bandai channel', '501st joint fighter wing', 'unlimited partners', 'cic', 'sony music communications', 'abc animation', 'studio ox', 'jp room', 'shueisha', 'quatre stella', 'atelier musa', 'melonbooks', 'mellow head', 'pony canyon', 'studio mir', 'kujoukun no bonnou wo mimamorukai', 'studio blanc', 'benesse corporation', 'happinet pictures', 'nippon cultural broadcasting', 'emon', 'yamasa', 'nomad', 'walt disney studios', 'lucent pictures entertainment', 'silkys', 'soft garage', 'takeshobo', 'media factory', 'imagin', 'kakao japan', 'i will', 'palm studio', 'gaga', 'animate film', 'sav the world productions', 'heewon entertainment', 'radio osaka', 'critical mass video', 'dentsu tec', 'index', 'smiral animation', 'asketch', 'pra', 'egg firm', 'children039s playground entertainment', 'trans arts', 'knack productions', 'koei', 'venus vangard', 'crunchyroll sc anime fund', 'studio acat', 'being', 'beat frog', 'genco', 'tokyo theatres', 'kddi', 'sunrise', 'lantis', 'zeroa', 'dndreampartners', 'top marshal', 'studio pastoral', 'tyo animations', 'imove', 'tencent animation', 'mages', 'grouper productions', 'ntt plala', 'toei video', 'asahi broadcasting', 'ultra super pictures', 'indeprox', 'studio core', 'rabbit gate', 'kinoshita group holdings', 'dream creation', 'rcc chugoku broadcasting', 'dwango music entertainment', 'rab aomori broadcasting', 'trick block', 'koei tecmo games', 'virgin babylon records', 'production ace', 'klockworx']
Producer_list = [{'label': value, 'value': value} for value in Producer_list]

Types_list = ['TV', 'Movie', 'OVA', 'Special', 'ONA', 'Music']
Types_list = [{'label': value, 'value': value} for value in Types_list]

# Create the Dash app
app = dash.Dash(__name__)

# Define the layout
app.layout = html.Div(children=[
    html.H1("MLOPS"),
    dcc.Input(id="Anime_Title", placeholder="Anime Title"),
    dcc.Dropdown(id="Anime_Genre", options=genre_list, multi=True, placeholder="Anime Genre(s)"),
    dcc.Input(id="Anime_Description", placeholder="Anime Description"),
    dcc.Dropdown(id="Anime_Type", options=Types_list,placeholder="Anime Type"),
    dcc.Dropdown(id="Anime_Producer", options=Producer_list + [{"label": "Other", "value": "Other"}], multi=True, placeholder="Anime Producer"),
    dcc.Dropdown(id="Anime_Studio", options=Studio_list + [{"label": "Other", "value": "Other"}], multi=True, placeholder="Anime Studio"),
    html.Div(id="other_producer_div", style={"display": "none"}, children=[
        dcc.Input(id="Other_Producer", placeholder="Enter Other Producer")
    ]),
    html.Div(id="other_studio_div", style={"display": "none"}, children=[
        dcc.Input(id="Other_Studio", placeholder="Enter Other Studio")
    ]),
    html.Button('Submit', id='btn'),
    html.Div(id="result")
])

# Define the callback to show/hide the Other Producer and Other Studio input boxes
@app.callback([Output(component_id="other_producer_div", component_property="style"),
               Output(component_id="other_studio_div", component_property="style")],
              [Input(component_id="Anime_Producer", component_property="value"),
               Input(component_id="Anime_Studio", component_property="value")])
def show_hide_other_inputs(Anime_Producer, Anime_Studio):
    producer_style = {"display": "none"}
    studio_style = {"display": "none"}

    if Anime_Producer and "Other" in Anime_Producer:
        producer_style = {"display": "block"}

    if Anime_Studio and "Other" in Anime_Studio:
        studio_style = {"display": "block"}

    return producer_style, studio_style

# Define the callback to process the form submission and display the results
@app.callback(Output(component_id="result", component_property="children"),
              [Input(component_id="btn", component_property='n_clicks')],
              [State(component_id="Anime_Title", component_property="value"),
               State(component_id="Anime_Genre", component_property="value"),
               State(component_id="Anime_Description", component_property="value"),
               State(component_id="Anime_Type", component_property="value"),
               State(component_id="Anime_Producer", component_property="value"),
               State(component_id="Anime_Studio", component_property="value"),
               State(component_id="Other_Producer", component_property="value"),
               State(component_id="Other_Studio", component_property="value")
              ])
def display_result(btn, Anime_Title, Anime_Genre, Anime_Description, Anime_Type, Anime_Producer, Anime_Studio, Other_Producer, Other_Studio):
    l=[Anime_Title,Anime_Genre,Anime_Description,Anime_Type,Anime_Producer,Anime_Studio]
    if all(x==None for x in l) or btn is None:
        raise PreventUpdate

    # Convert multiple value inputs into lists if it's a dropdown component
    if isinstance(Anime_Genre, str):
        Anime_Genre = [x.strip() for x in Anime_Genre.split(',')]
    if isinstance(Anime_Producer, str):
        Anime_Producer = [x.strip() for x in Anime_Producer.split(',')]
    if isinstance(Anime_Studio, str):
        Anime_Studio = [x.strip() for x in Anime_Studio.split(',')]

    # Check if Other_Producer is not None and append it to the Anime_Producer list
    if Other_Producer:
        Anime_Producer.remove('Other')
        Anime_Producer.append(Other_Producer)

    # Check if Other_Studio is not None and append it to the Anime_Studio list
    if Other_Studio:
        Anime_Studio.remove('Other')
        Anime_Studio.append(Other_Studio)

    new_data = {
        'Title': [Anime_Title],
        'Genre': [Anime_Genre],
        'Synopsis': [Anime_Description],
        'Type': [Anime_Type],
        'Producer': [Anime_Producer],
        'Studio': [Anime_Studio]
    }

    df = pd.DataFrame(new_data)

    # Call predict function to get the prediction for the new data
    prediction = test.predict(df)

    # Append the prediction to the dataframe
    df['Prediction'] = prediction

    # Generate the table HTML code
    table = html.Table([
        html.Tr([html.Th(col) for col in df.columns]),
        *[html.Tr([html.Td(df.iloc[i][col]) for col in df.columns]) for i in range(len(df))]
    ])

    return html.Div([
        html.H2("New Data with Prediction"),
        table
    ])



if __name__ == '__main__':
    app.run_server(debug=True, port=7042)

