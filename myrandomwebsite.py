import random

license = """
This is free and unencumbered software released into the public domain.

Anyone is free to copy, modify, publish, use, compile, sell, or
distribute this software, either in source code form or as a compiled
binary, for any purpose, commercial or non-commercial, and by any
means.

In jurisdictions that recognize copyright laws, the author or authors
of this software dedicate any and all copyright interest in the
software to the public domain. We make this dedication for the benefit
of the public at large and to the detriment of our heirs and
successors. We intend this dedication to be an overt act of
relinquishment in perpetuity of all present and future rights to this
software under copyright law.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR
OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
OTHER DEALINGS IN THE SOFTWARE.

For more information, please refer to <http://unlicense.org/>
"""

top_level_domains = [
    "com", "org", "net", "int", "edu", "gov", "mil", "arpa", "academy",
    "accountant", "accountants", "active", "actor", "ads", "adult", "aero",
    "africa", "agency", "airforce", "amazon", "analytics", "apartments",
    "app", "apple", "archi", "army", "art", "arte", "associates",
    "attorney", "auction", "audible", "audio", "author", "auto", "autos",
    "aws", "baby", "band", "bank", "bar", "barefoot", "bargains",
    "baseball", "basketball", "beauty", "beer", "best", "bestbuy", "bet",
    "bible", "bid", "bike", "bingo", "bio", "biz", "black", "blackfriday",
    "blockbuster", "blog", "blue", "boo", "book", "boots", "boston", "bot",
    "boutique", "box", "broadway", "broker", "build", "builders",
    "business", "buy", "buzz", "cab", "cafe", "call", "cam", "camera",
    "camp", "cancerresearch", "capital", "car", "cards", "care", "career",
    "careers", "cars", "case", "cash", "casino", "catering", "catholic",
    "center", "cern", "ceo", "cfd", "channel", "chat", "charity", "cheap",
    "christmas", "church", "circle", "city", "claims", "cleaning", "click",
    "clinic", "clothing", "cloud", "club", "coach", "codes", "coffee",
    "college", "community", "company", "compare", "computer", "condos",
    "construction", "consulting", "contact", "contractors", "cooking",
    "cool", "coop", "country", "coupon", "coupons", "courses", "cpa",
    "credit", "creditcard", "cruise", "cricket", "cruises", "cyou", "dad",
    "dance", "data", "date", "dating", "day", "deal", "deals", "degree",
    "delivery", "democrat", "dental", "dentist", "design", "dev",
    "diamonds", "diet", "digital", "direct", "directory", "discount", "diy",
    "docs", "doctor", "dog", "domains", "dot", "download", "drive",
    "earth", "eat", "eco", "education", "email", "energy", "engineer",
    "engineering", "edeka", "entertainment", "enterprises", "equipment",
    "esq", "estate", "events", "exchange", "expert", "exposed", "express",
    "fail", "faith", "family", "fan", "fans", "farm", "fashion", "fast",
    "feedback", "fiat", "film", "final", "finance", "financial", "fire",
    "fish", "fishing", "fit", "fitness", "flights", "florist", "flowers",
    "fly", "foo", "food", "foodnetwork", "football", "forsale", "forum",
    "foundation", "free", "frontdoor", "fun", "fund", "furniture", "fyi",
    "gallery", "game", "games", "garden", "gdn", "gift", "gifts", "gives",
    "glass", "gle", "global", "gold", "golf", "google", "gop", "graphics",
    "green", "gripe", "grocery", "group", "guide", "guitars", "guru",
    "hair", "hangout", "health", "healthcare", "help", "here", "hiphop",
    "hiv", "hockey", "holdings", "holiday", "homegoods", "homes",
    "homesense", "horse", "hospital", "host", "hosting", "hot", "hotels",
    "house", "how", "ice", "icu", "inc", "industries", "info", "ing",
    "ink", "insurance", "insure", "international", "investments", "irish",
    "jewelry", "jobs", "joy", "kim", "kitchen", "kosher", "kpn", "land",
    "lat", "law", "lawyer", "lease", "leclerc", "legal", "life",
    "lifeinsurance", "lighting", "like", "limited", "limo", "link", "live",
    "living", "loan", "loans", "locker", "lol", "lotto", "love", "ltd",
    "luxury", "makeup", "management", "map", "market", "marketing",
    "markets", "mba", "med", "media", "meet", "meme", "memorial", "men",
    "menu", "mint", "mobi", "mobile", "mobily", "moe", "mom", "money",
    "monster", "mortgage", "motorcycles", "mov", "movie", "museum", "music",
    "name", "navy", "network", "new", "news", "nexus", "ngo", "ninja",
    "now", "ntt", "observer", "org", "one", "ong", "onl", "online", "ooo",
    "open", "organic", "origins", "page", "partners", "parts", "party",
    "pay", "pet", "pharmacy", "phone", "photo", "photography", "photos",
    "physio", "pics", "pictures", "pid", "pin", "pink", "pizza", "place",
    "plumbing", "plus", "poker", "post", "press", "prime", "pro",
    "productions", "prof", "promo", "properties", "property", "protection",
    "pub", "qpon", "quebec", "racing", "radio", "read", "realestate",
    "realtor", "realty", "recipes", "red", "rehab", "reit", "rent",
    "rentals", "repair", "report", "republican", "rest", "restaurant",
    "review", "reviews", "rich", "rip", "rocks", "rodeo", "room", "rugby",
    "run", "safe", "sale", "salon", "save", "sbi", "scholarships",
    "school", "science", "search", "secure", "security", "select",
    "services", "shoes", "shop", "shopping", "show", "showtime", "silk",
    "singles", "site", "ski", "skin", "sky", "sling", "smile", "sncf",
    "soccer", "social", "software", "solar", "solutions", "song", "spa",
    "space", "spreadbetting", "spot", "sport", "srl", "storage", "store",
    "stream", "studio", "study", "style", "sucks", "supplies", "supply",
    "support", "surf", "surgery", "systems", "talk", "tattoo", "tax",
    "taxi", "team", "tech", "technology", "tel", "tennis", "theater",
    "theatre", "tickets", "tips", "tires", "today", "tools", "top",
    "tours", "town", "toys", "trade", "trading", "training", "travel",
    "travelersinsurance", "trust", "tube", "tunes", "uconnect", "university",
    "uno", "vacations", "ventures", "vet", "video", "villas", "vin", "vip",
    "vision", "vodka", "volvo", "vote", "voting", "voyage", "watch",
    "watches", "weather", "webcam", "website", "wed", "wedding", "whoswho",
    "wiki", "win", "wine", "winners", "work", "works", "world", "wow",
    "wtf", "xyz", "yachts", "yoga", "you", "youtube", "zero", "zip",
    "zone", "africa", "capetown", "durban", "joburg", "abudhabi", "arab",
    "asia", "doha", "dubai", "krd", "kyoto", "nagoya", "okinawa", "osaka",
    "ryukyu", "taipei", "tokyo", "yokohama", "alsace", "bzh", "corsica",
    "cat", "eus", "paris", "bcn", "barcelona", "cat", "eus", "gal",
    "madrid", "bayern", "berlin", "cologne", "koeln", "hamburg", "nrw",
    "ruhr", "saarland", "amsterdam", "bar", "brussels", "cymru", "wales",
    "frl", "gent", "helsinki", "irish", "ist", "istanbul", "london",
    "scot", "stockholm", "swiss", "tatar", "tirol", "vlaanderen", "wien",
    "zuerich", "boston", "miami", "nyc", "quebec", "vegas", "kiwi",
    "melbourne", "sydney", "lat", "rio", "aaa", "aarp", "abarth", "abb",
    "abbott", "abbvie", "abc", "accenture", "aco", "aeg", "aetna", "afl",
    "agakhan", "aig", "aigo", "airbus", "airtel", "akdn", "alfaromeo",
    "alibaba", "alipay", "allfinanz", "allstate", "ally", "alstom",
    "amazon", "americanexpress", "amex", "amica", "android", "anz", "aol",
    "apple", "aquarelle", "aramco", "audi", "auspost", "aws", "axa",
    "azure", "baidu", "bananarepublic", "barclaycard", "barclays",
    "basketball", "bauhaus", "bbc", "bbt", "bbva", "bcg", "bentley",
    "bharti", "bing", "blanco", "bloomberg", "bms", "bmw", "bnl",
    "bnpparibas", "boehringer", "bond", "booking", "bosch", "bostik",
    "bradesco", "bridgestone", "brother", "bugatti", "cal", "calvinklein",
    "canon", "capitalone", "caravan", "cartier", "cba", "cbn", "cbre",
    "cbs", "cern", "cfa", "chanel", "chase", "chintai", "chrome",
    "chrysler", "cipriani", "cisco", "citadel", "citi", "citic", "clubmed",
    "comcast", "commbank", "creditunion", "crown", "crs", "csc",
    "cuisinella", "dabur", "datsun", "dealer", "dell", "deloitte", "delta",
    "dhl", "discover", "dish", "dnp", "dodge", "dunlop", "dupont", "dvag",
    "edeka", "emerck", "epson", "ericsson", "erni", "esurance", "etisalat",
    "eurovision", "everbank", "extraspace", "fage", "fairwinds", "farmers",
    "fedex", "ferrari", "ferrero", "fiat", "fidelity", "firestone",
    "firmdale", "flickr", "flir", "flsmidth", "ford", "fox", "fresenius",
    "forex", "frogans", "frontier", "fujitsu", "fujixerox", "gallo",
    "gallup", "gap", "gbiz", "gea", "genting", "giving", "gle", "globo",
    "gmail", "gmo", "gmx", "godaddy", "goldpoint", "goodyear", "goog",
    "google", "grainger", "guardian", "gucci", "hbo", "hdfc", "hdfcbank",
    "hermes", "hisamitsu", "hitachi", "hkt", "honda", "honeywell",
    "hotmail", "hsbc", "hughes", "hyatt", "hyundai", "ibm", "ieee", "ifm",
    "ikano", "imdb", "infiniti", "intel", "intuit", "ipiranga", "iselect",
    "itau", "itv", "iveco", "jaguar", "java", "jcb", "jcp", "jeep",
    "jpmorgan", "juniper", "kddi", "kerryhotels", "kerrylogistics",
    "kerryproperties", "kfh", "kia", "kinder", "kindle", "komatsu", "kpmg",
    "kred", "kuokgroup", "lacaixa", "ladbrokes", "lamborghini", "lancaster",
    "lancia", "lancome", "landrover", "lanxess", "lasalle", "latrobe",
    "lds", "leclerc", "lego", "liaison", "lexus", "lidl", "lifestyle",
    "lilly", "lincoln", "linde", "lipsy", "lixil", "locus", "lotte", "lpl",
    "lplfinancial", "lundbeck", "lupin", "macys", "maif", "man", "mango",
    "marriott", "maserati", "mattel", "mckinsey", "metlife", "microsoft",
    "mini", "mit", "mitsubishi", "mlb", "mma", "monash", "mormon", "moto",
    "movistar", "msd", "mtn", "mtr", "mutual", "nadex", "nationwide",
    "natura", "nba", "nec", "netflix", "neustar", "newholland", "nfl",
    "nhk", "nico", "nike", "nikon", "nissan", "nissay", "nokia",
    "northwesternmutual", "norton", "nra", "ntt", "obi", "office", "omega",
    "oracle", "orange", "otsuka", "ovh", "panasonic", "pccw", "pfizer",
    "philips", "piaget", "pictet", "ping", "pioneer", "play", "playstation",
    "pohl", "politie", "praxi", "prod", "progressive", "pru", "prudential",
    "pwc", "quest", "qvc", "redstone", "reliance", "rexroth", "ricoh",
    "rmit", "rocher", "rogers", "rwe", "safety", "sakura", "samsung",
    "sandvik", "sandvikcoromant", "sanofi", "sap", "saxo", "sbi", "sbs",
    "sca", "scb", "schaeffler", "schmidt", "schwarz", "scjohnson", "scor",
    "seat", "sener", "ses", "sew", "seven", "sfr", "seek", "shangrila",
    "sharp", "shaw", "shell", "shriram", "sina", "sky", "skype", "smart",
    "sncf", "softbank", "sohu", "sony", "spiegel", "stada", "staples",
    "star", "starhub", "statebank", "statefarm", "statoil", "stc",
    "stcgroup", "suzuki", "swatch", "swiftcover", "symantec", "taobao",
    "target", "tatamotors", "tdk", "telecity", "telefonica", "temasek",
    "teva", "tiffany", "tjx", "toray", "toshiba", "total", "toyota",
    "travelchannel", "travelers", "tui", "tvs", "ubs", "unicom", "uol",
    "ups", "vanguard", "verisign", "vig", "viking", "virgin", "visa",
    "vista", "vistaprint", "vivo", "volkswagen", "volvo", "walmart",
    "walter", "weatherchannel", "weber", "weir", "williamhill", "windows",
    "wme", "wolterskluwer", "woodside", "wtc", "xbox", "xerox", "xfinity",
    "yahoo", "yamaxun", "yandex", "yodobashi", "youtube", "zappos", "zara",
    "zippo", "onion", "eth", "bit"
]

def get_random_website(names: list[str], tlds: list[str] = top_level_domains):
    name = random.choice(names)
    tld = random.choice(tlds)

    return f"{name}.{tld}"