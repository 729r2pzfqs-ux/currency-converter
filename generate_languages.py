#!/usr/bin/env python3
"""Generate multi-language pages for currency converter"""

import re
import os

# Translations for each language
TRANSLATIONS = {
    'en': {
        'lang': 'en',
        'title': 'Currency Converter | Crypto, Travel, Salary & Inflation Calculator',
        'description': 'Free currency converter with crypto support, travel mode, salary cost-of-living calculator, and inflation adjuster.',
        'site_name': 'Currency Converter',
        'hero_title': 'Universal Currency Converter',
        'hero_subtitle': 'Crypto + Fiat • Travel Mode • Salary Calculator • Inflation Adjuster',
        'convert': 'Convert',
        'travel': 'Travel',
        'salary': 'Salary',
        'inflation': 'Inflation',
        'from': 'From',
        'to': 'To',
        'i_have': 'I have',
        'travel_intro': "That's worth in popular destinations:",
        'my_salary': 'My salary',
        'equivalent_in': 'Equivalent in',
        'equivalent_salary': 'Equivalent salary',
        'adjusted_for': 'Adjusted for cost of living',
        'amount_past': 'Amount in the past',
        'worth_today': 'Would be worth today',
        'cumulative': 'cumulative inflation',
        'avg_per_year': 'average per year',
        'why_use': 'Why Use Our Converter?',
        'crypto_fiat': 'Crypto + Fiat',
        'crypto_desc': 'Convert between traditional currencies and crypto in one place.',
        'travel_mode': 'Travel Mode',
        'travel_desc': 'See your money in 24+ travel destinations instantly.',
        'salary_compare': 'Salary Comparison',
        'salary_desc': 'Compare salaries across cities with cost of living adjustment.',
        'rate_info': 'Updated every 60 seconds • Rates from ECB & CoinGecko',
    },
    'de': {
        'lang': 'de',
        'title': 'Währungsrechner | Krypto, Reise, Gehalt & Inflationsrechner',
        'description': 'Kostenloser Währungsrechner mit Krypto-Unterstützung, Reisemodus, Gehaltsrechner und Inflationsrechner.',
        'site_name': 'Währungsrechner',
        'hero_title': 'Universeller Währungsrechner',
        'hero_subtitle': 'Krypto + Fiat • Reisemodus • Gehaltsrechner • Inflationsrechner',
        'convert': 'Umrechnen',
        'travel': 'Reisen',
        'salary': 'Gehalt',
        'inflation': 'Inflation',
        'from': 'Von',
        'to': 'Nach',
        'i_have': 'Ich habe',
        'travel_intro': 'Das entspricht in beliebten Reisezielen:',
        'my_salary': 'Mein Gehalt',
        'equivalent_in': 'Entspricht in',
        'equivalent_salary': 'Entsprechendes Gehalt',
        'adjusted_for': 'Angepasst an Lebenshaltungskosten',
        'amount_past': 'Betrag in der Vergangenheit',
        'worth_today': 'Wäre heute wert',
        'cumulative': 'kumulative Inflation',
        'avg_per_year': 'durchschnittlich pro Jahr',
        'why_use': 'Warum unseren Rechner nutzen?',
        'crypto_fiat': 'Krypto + Fiat',
        'crypto_desc': 'Tauschen Sie traditionelle Währungen und Krypto an einem Ort.',
        'travel_mode': 'Reisemodus',
        'travel_desc': 'Sehen Sie Ihr Geld sofort in 24+ Reisezielen.',
        'salary_compare': 'Gehaltsvergleich',
        'salary_desc': 'Vergleichen Sie Gehälter mit Lebenshaltungskostenanpassung.',
        'rate_info': 'Alle 60 Sekunden aktualisiert • Kurse von EZB & CoinGecko',
    },
    'es': {
        'lang': 'es',
        'title': 'Conversor de Divisas | Cripto, Viajes, Salario e Inflación',
        'description': 'Conversor de divisas gratuito con soporte cripto, modo viaje, calculadora de salarios y ajustador de inflación.',
        'site_name': 'Conversor de Divisas',
        'hero_title': 'Conversor Universal de Divisas',
        'hero_subtitle': 'Cripto + Fiat • Modo Viaje • Calculadora Salarial • Ajuste de Inflación',
        'convert': 'Convertir',
        'travel': 'Viajes',
        'salary': 'Salario',
        'inflation': 'Inflación',
        'from': 'De',
        'to': 'A',
        'i_have': 'Tengo',
        'travel_intro': 'Eso equivale en destinos populares:',
        'my_salary': 'Mi salario',
        'equivalent_in': 'Equivalente en',
        'equivalent_salary': 'Salario equivalente',
        'adjusted_for': 'Ajustado por costo de vida',
        'amount_past': 'Cantidad en el pasado',
        'worth_today': 'Valdría hoy',
        'cumulative': 'inflación acumulada',
        'avg_per_year': 'promedio por año',
        'why_use': '¿Por qué usar nuestro conversor?',
        'crypto_fiat': 'Cripto + Fiat',
        'crypto_desc': 'Convierte monedas tradicionales y cripto en un solo lugar.',
        'travel_mode': 'Modo Viaje',
        'travel_desc': 'Ve tu dinero en más de 24 destinos al instante.',
        'salary_compare': 'Comparación Salarial',
        'salary_desc': 'Compara salarios entre ciudades con ajuste de costo de vida.',
        'rate_info': 'Actualizado cada 60 segundos • Tasas de BCE y CoinGecko',
    },
    'fr': {
        'lang': 'fr',
        'title': 'Convertisseur de Devises | Crypto, Voyage, Salaire et Inflation',
        'description': 'Convertisseur de devises gratuit avec support crypto, mode voyage, calculateur de salaire et ajustement d\'inflation.',
        'site_name': 'Convertisseur de Devises',
        'hero_title': 'Convertisseur Universel de Devises',
        'hero_subtitle': 'Crypto + Fiat • Mode Voyage • Calculateur Salarial • Ajustement Inflation',
        'convert': 'Convertir',
        'travel': 'Voyage',
        'salary': 'Salaire',
        'inflation': 'Inflation',
        'from': 'De',
        'to': 'Vers',
        'i_have': 'J\'ai',
        'travel_intro': 'Cela vaut dans les destinations populaires:',
        'my_salary': 'Mon salaire',
        'equivalent_in': 'Équivalent à',
        'equivalent_salary': 'Salaire équivalent',
        'adjusted_for': 'Ajusté au coût de la vie',
        'amount_past': 'Montant dans le passé',
        'worth_today': 'Vaudrait aujourd\'hui',
        'cumulative': 'inflation cumulée',
        'avg_per_year': 'moyenne par an',
        'why_use': 'Pourquoi utiliser notre convertisseur?',
        'crypto_fiat': 'Crypto + Fiat',
        'crypto_desc': 'Convertissez devises traditionnelles et crypto en un seul endroit.',
        'travel_mode': 'Mode Voyage',
        'travel_desc': 'Voyez votre argent dans plus de 24 destinations instantanément.',
        'salary_compare': 'Comparaison Salariale',
        'salary_desc': 'Comparez les salaires entre villes avec ajustement du coût de la vie.',
        'rate_info': 'Mis à jour toutes les 60 secondes • Taux BCE et CoinGecko',
    },
    'pt': {
        'lang': 'pt',
        'title': 'Conversor de Moedas | Cripto, Viagem, Salário e Inflação',
        'description': 'Conversor de moedas gratuito com suporte a cripto, modo viagem, calculadora de salário e ajuste de inflação.',
        'site_name': 'Conversor de Moedas',
        'hero_title': 'Conversor Universal de Moedas',
        'hero_subtitle': 'Cripto + Fiat • Modo Viagem • Calculadora Salarial • Ajuste de Inflação',
        'convert': 'Converter',
        'travel': 'Viagem',
        'salary': 'Salário',
        'inflation': 'Inflação',
        'from': 'De',
        'to': 'Para',
        'i_have': 'Eu tenho',
        'travel_intro': 'Isso vale em destinos populares:',
        'my_salary': 'Meu salário',
        'equivalent_in': 'Equivalente em',
        'equivalent_salary': 'Salário equivalente',
        'adjusted_for': 'Ajustado pelo custo de vida',
        'amount_past': 'Valor no passado',
        'worth_today': 'Valeria hoje',
        'cumulative': 'inflação acumulada',
        'avg_per_year': 'média por ano',
        'why_use': 'Por que usar nosso conversor?',
        'crypto_fiat': 'Cripto + Fiat',
        'crypto_desc': 'Converta moedas tradicionais e cripto em um só lugar.',
        'travel_mode': 'Modo Viagem',
        'travel_desc': 'Veja seu dinheiro em mais de 24 destinos instantaneamente.',
        'salary_compare': 'Comparação Salarial',
        'salary_desc': 'Compare salários entre cidades com ajuste de custo de vida.',
        'rate_info': 'Atualizado a cada 60 segundos • Taxas do BCE e CoinGecko',
    },
    'zh': {
        'lang': 'zh',
        'title': '货币转换器 | 加密货币、旅行、薪资和通胀计算器',
        'description': '免费货币转换器，支持加密货币、旅行模式、薪资生活成本计算器和通胀调整器。',
        'site_name': '货币转换器',
        'hero_title': '通用货币转换器',
        'hero_subtitle': '加密+法币 • 旅行模式 • 薪资计算器 • 通胀调整器',
        'convert': '转换',
        'travel': '旅行',
        'salary': '薪资',
        'inflation': '通胀',
        'from': '从',
        'to': '到',
        'i_have': '我有',
        'travel_intro': '在热门目的地相当于：',
        'my_salary': '我的薪资',
        'equivalent_in': '相当于',
        'equivalent_salary': '等效薪资',
        'adjusted_for': '根据生活成本调整',
        'amount_past': '过去的金额',
        'worth_today': '今天的价值',
        'cumulative': '累计通胀',
        'avg_per_year': '年平均',
        'why_use': '为什么使用我们的转换器？',
        'crypto_fiat': '加密+法币',
        'crypto_desc': '在一个地方转换传统货币和加密货币。',
        'travel_mode': '旅行模式',
        'travel_desc': '即时查看您的资金在24+目的地的价值。',
        'salary_compare': '薪资比较',
        'salary_desc': '根据生活成本比较不同城市的薪资。',
        'rate_info': '每60秒更新 • 汇率来自欧洲央行和CoinGecko',
    },
    'ja': {
        'lang': 'ja',
        'title': '通貨換算 | 暗号通貨、旅行、給与、インフレ計算機',
        'description': '暗号通貨対応、旅行モード、給与生活費計算機、インフレ調整機能付きの無料通貨換算ツール。',
        'site_name': '通貨換算',
        'hero_title': 'ユニバーサル通貨換算',
        'hero_subtitle': '暗号通貨+法定通貨 • 旅行モード • 給与計算 • インフレ調整',
        'convert': '換算',
        'travel': '旅行',
        'salary': '給与',
        'inflation': 'インフレ',
        'from': 'から',
        'to': 'へ',
        'i_have': '所持金',
        'travel_intro': '人気の目的地での価値：',
        'my_salary': '私の給与',
        'equivalent_in': '相当額',
        'equivalent_salary': '相当給与',
        'adjusted_for': '生活費調整済み',
        'amount_past': '過去の金額',
        'worth_today': '今日の価値',
        'cumulative': '累積インフレ',
        'avg_per_year': '年平均',
        'why_use': 'なぜ当ツールを使うのか？',
        'crypto_fiat': '暗号通貨+法定通貨',
        'crypto_desc': '従来の通貨と暗号通貨を一箇所で換算。',
        'travel_mode': '旅行モード',
        'travel_desc': '24以上の目的地で即座に金額を確認。',
        'salary_compare': '給与比較',
        'salary_desc': '生活費を考慮した都市間給与比較。',
        'rate_info': '60秒ごとに更新 • ECBとCoinGeckoのレート',
    },
    'hi': {
        'lang': 'hi',
        'title': 'मुद्रा परिवर्तक | क्रिप्टो, यात्रा, वेतन और मुद्रास्फीति कैलकुलेटर',
        'description': 'क्रिप्टो समर्थन, यात्रा मोड, वेतन जीवन-यापन लागत कैलकुलेटर के साथ मुफ्त मुद्रा परिवर्तक।',
        'site_name': 'मुद्रा परिवर्तक',
        'hero_title': 'यूनिवर्सल मुद्रा परिवर्तक',
        'hero_subtitle': 'क्रिप्टो + फिएट • यात्रा मोड • वेतन कैलकुलेटर • मुद्रास्फीति समायोजक',
        'convert': 'परिवर्तित',
        'travel': 'यात्रा',
        'salary': 'वेतन',
        'inflation': 'मुद्रास्फीति',
        'from': 'से',
        'to': 'में',
        'i_have': 'मेरे पास है',
        'travel_intro': 'लोकप्रिय गंतव्यों में इसकी कीमत:',
        'my_salary': 'मेरा वेतन',
        'equivalent_in': 'के बराबर',
        'equivalent_salary': 'समकक्ष वेतन',
        'adjusted_for': 'जीवन यापन की लागत के लिए समायोजित',
        'amount_past': 'अतीत में राशि',
        'worth_today': 'आज की कीमत होगी',
        'cumulative': 'संचयी मुद्रास्फीति',
        'avg_per_year': 'प्रति वर्ष औसत',
        'why_use': 'हमारे परिवर्तक का उपयोग क्यों करें?',
        'crypto_fiat': 'क्रिप्टो + फिएट',
        'crypto_desc': 'पारंपरिक मुद्राओं और क्रिप्टो को एक ही स्थान पर बदलें।',
        'travel_mode': 'यात्रा मोड',
        'travel_desc': '24+ गंतव्यों में अपना पैसा तुरंत देखें।',
        'salary_compare': 'वेतन तुलना',
        'salary_desc': 'जीवन यापन लागत समायोजन के साथ शहरों में वेतन की तुलना करें।',
        'rate_info': 'हर 60 सेकंड में अपडेट • ECB और CoinGecko से दरें',
    },
    'ar': {
        'lang': 'ar',
        'title': 'محول العملات | العملات المشفرة والسفر والراتب والتضخم',
        'description': 'محول عملات مجاني مع دعم العملات المشفرة ووضع السفر وحاسبة الراتب ومعدل التضخم.',
        'site_name': 'محول العملات',
        'hero_title': 'محول العملات العالمي',
        'hero_subtitle': 'مشفرة + تقليدية • وضع السفر • حاسبة الراتب • معدل التضخم',
        'convert': 'تحويل',
        'travel': 'سفر',
        'salary': 'راتب',
        'inflation': 'تضخم',
        'from': 'من',
        'to': 'إلى',
        'i_have': 'لدي',
        'travel_intro': 'هذا يساوي في الوجهات الشائعة:',
        'my_salary': 'راتبي',
        'equivalent_in': 'يعادل في',
        'equivalent_salary': 'الراتب المكافئ',
        'adjusted_for': 'معدل حسب تكلفة المعيشة',
        'amount_past': 'المبلغ في الماضي',
        'worth_today': 'سيساوي اليوم',
        'cumulative': 'التضخم التراكمي',
        'avg_per_year': 'المتوسط سنوياً',
        'why_use': 'لماذا تستخدم محولنا؟',
        'crypto_fiat': 'مشفرة + تقليدية',
        'crypto_desc': 'حول العملات التقليدية والمشفرة في مكان واحد.',
        'travel_mode': 'وضع السفر',
        'travel_desc': 'شاهد أموالك في أكثر من 24 وجهة فوراً.',
        'salary_compare': 'مقارنة الراتب',
        'salary_desc': 'قارن الرواتب بين المدن مع تعديل تكلفة المعيشة.',
        'rate_info': 'يتم التحديث كل 60 ثانية • الأسعار من البنك المركزي الأوروبي و CoinGecko',
    },
    'ru': {
        'lang': 'ru',
        'title': 'Конвертер валют | Крипто, Путешествия, Зарплата и Инфляция',
        'description': 'Бесплатный конвертер валют с поддержкой криптовалют, режимом путешествий, калькулятором зарплаты и инфляции.',
        'site_name': 'Конвертер валют',
        'hero_title': 'Универсальный конвертер валют',
        'hero_subtitle': 'Крипто + Фиат • Режим путешествий • Калькулятор зарплаты • Инфляция',
        'convert': 'Конвертировать',
        'travel': 'Путешествия',
        'salary': 'Зарплата',
        'inflation': 'Инфляция',
        'from': 'Из',
        'to': 'В',
        'i_have': 'У меня есть',
        'travel_intro': 'Это стоит в популярных направлениях:',
        'my_salary': 'Моя зарплата',
        'equivalent_in': 'Эквивалент в',
        'equivalent_salary': 'Эквивалентная зарплата',
        'adjusted_for': 'С учётом стоимости жизни',
        'amount_past': 'Сумма в прошлом',
        'worth_today': 'Стоило бы сегодня',
        'cumulative': 'накопленная инфляция',
        'avg_per_year': 'в среднем в год',
        'why_use': 'Почему наш конвертер?',
        'crypto_fiat': 'Крипто + Фиат',
        'crypto_desc': 'Конвертируйте традиционные валюты и криптовалюты в одном месте.',
        'travel_mode': 'Режим путешествий',
        'travel_desc': 'Мгновенно смотрите ваши деньги в 24+ направлениях.',
        'salary_compare': 'Сравнение зарплат',
        'salary_desc': 'Сравнивайте зарплаты между городами с учётом стоимости жизни.',
        'rate_info': 'Обновляется каждые 60 секунд • Курсы ЕЦБ и CoinGecko',
    },
    'tr': {
        'lang': 'tr',
        'title': 'Döviz Çevirici | Kripto, Seyahat, Maaş ve Enflasyon Hesaplayıcı',
        'description': 'Kripto desteği, seyahat modu, maaş yaşam maliyeti hesaplayıcısı ile ücretsiz döviz çevirici.',
        'site_name': 'Döviz Çevirici',
        'hero_title': 'Evrensel Döviz Çevirici',
        'hero_subtitle': 'Kripto + Fiat • Seyahat Modu • Maaş Hesaplayıcı • Enflasyon Ayarlayıcı',
        'convert': 'Çevir',
        'travel': 'Seyahat',
        'salary': 'Maaş',
        'inflation': 'Enflasyon',
        'from': 'Kaynak',
        'to': 'Hedef',
        'i_have': 'Bende var',
        'travel_intro': 'Popüler destinasyonlarda değeri:',
        'my_salary': 'Maaşım',
        'equivalent_in': 'Eşdeğeri',
        'equivalent_salary': 'Eşdeğer maaş',
        'adjusted_for': 'Yaşam maliyetine göre ayarlanmış',
        'amount_past': 'Geçmişteki miktar',
        'worth_today': 'Bugünkü değeri',
        'cumulative': 'kümülatif enflasyon',
        'avg_per_year': 'yıllık ortalama',
        'why_use': 'Neden bizim çeviricimizi kullanmalısınız?',
        'crypto_fiat': 'Kripto + Fiat',
        'crypto_desc': 'Geleneksel para birimleri ve kripto\'yu tek yerden çevirin.',
        'travel_mode': 'Seyahat Modu',
        'travel_desc': '24+ destinasyonda paranızı anında görün.',
        'salary_compare': 'Maaş Karşılaştırma',
        'salary_desc': 'Yaşam maliyeti ayarlamasıyla şehirler arası maaş karşılaştırın.',
        'rate_info': 'Her 60 saniyede güncellenir • ECB ve CoinGecko kurları',
    },
}

# Language names for dropdown
LANG_NAMES = {
    'en': 'English',
    'de': 'Deutsch',
    'es': 'Español',
    'fr': 'Français',
    'pt': 'Português',
    'zh': '中文',
    'ja': '日本語',
    'hi': 'हिन्दी',
    'ar': 'العربية',
    'ru': 'Русский',
    'tr': 'Türkçe',
}

def generate_hreflang_tags():
    """Generate hreflang tags for all languages"""
    tags = ['<link rel="alternate" hreflang="x-default" href="https://convert-currency.org/">']
    tags.append('<link rel="alternate" hreflang="en" href="https://convert-currency.org/">')
    for lang in TRANSLATIONS.keys():
        if lang != 'en':
            tags.append(f'<link rel="alternate" hreflang="{lang}" href="https://convert-currency.org/{lang}.html">')
    return '\n    '.join(tags)

def generate_lang_dropdown(current_lang):
    """Generate language dropdown with all options"""
    options = []
    for lang, name in LANG_NAMES.items():
        selected = ' selected' if lang == current_lang else ''
        options.append(f'<option value="{lang}"{selected} class="text-gray-800">{name}</option>')
    return '\n                '.join(options)

def create_language_file(lang, t):
    """Create HTML file for a specific language"""
    
    # Read template
    with open('index.html', 'r') as f:
        html = f.read()
    
    # Update lang attribute
    html = re.sub(r'<html lang="en">', f'<html lang="{lang}">', html)
    
    # Update title and meta
    html = re.sub(r'<title>.*?</title>', f'<title>{t["title"]}</title>', html)
    html = re.sub(r'<meta name="description" content=".*?">', f'<meta name="description" content="{t["description"]}">', html)
    
    # Update canonical
    if lang == 'en':
        canonical = 'https://convert-currency.org/'
    else:
        canonical = f'https://convert-currency.org/{lang}.html'
    html = re.sub(r'<link rel="canonical" href=".*?">', f'<link rel="canonical" href="{canonical}">', html)
    
    # Update hreflang tags
    hreflang_pattern = r'<link rel="alternate" hreflang="en".*?<link rel="alternate" hreflang="x-default".*?>'
    html = re.sub(hreflang_pattern, generate_hreflang_tags(), html, flags=re.DOTALL)
    
    # Update OG tags
    html = re.sub(r'<meta property="og:title" content=".*?">', f'<meta property="og:title" content="{t["title"]}">', html)
    html = re.sub(r'<meta property="og:description" content=".*?">', f'<meta property="og:description" content="{t["description"]}">', html)
    
    # Update site name in header
    html = re.sub(r'<span class="text-xl font-bold">Currency Converter</span>', f'<span class="text-xl font-bold">{t["site_name"]}</span>', html)
    
    # Update language dropdown
    old_dropdown = r'<select id="langSelect".*?</select>'
    new_dropdown = f'''<select id="langSelect" class="bg-white/10 text-sm rounded-lg px-3 py-2 border border-white/20" onchange="switchLang(this.value)">
                {generate_lang_dropdown(lang)}
            </select>'''
    html = re.sub(old_dropdown, new_dropdown, html, flags=re.DOTALL)
    
    # Update hero
    html = re.sub(r'<h1 class="text-3xl md:text-4xl font-bold mb-3">Universal Currency Converter</h1>', 
                  f'<h1 class="text-3xl md:text-4xl font-bold mb-3">{t["hero_title"]}</h1>', html)
    html = re.sub(r'<p class="text-slate-400">Crypto \+ Fiat.*?</p>',
                  f'<p class="text-slate-400">{t["hero_subtitle"]}</p>', html)
    
    # Update mode buttons
    html = re.sub(r'</i> Convert', f'</i> {t["convert"]}', html)
    html = re.sub(r'</i> Travel', f'</i> {t["travel"]}', html)
    html = re.sub(r'</i> Salary', f'</i> {t["salary"]}', html)
    html = re.sub(r'</i> Inflation', f'</i> {t["inflation"]}', html)
    
    # Update labels
    html = re.sub(r'>From</label>', f'>{t["from"]}</label>', html)
    html = re.sub(r'>To</label>', f'>{t["to"]}</label>', html)
    html = re.sub(r'>I have</label>', f'>{t["i_have"]}</label>', html)
    html = re.sub(r"That's worth in popular destinations:", t["travel_intro"], html)
    html = re.sub(r'>My salary</label>', f'>{t["my_salary"]}</label>', html)
    html = re.sub(r'>Equivalent in</label>', f'>{t["equivalent_in"]}</label>', html)
    html = re.sub(r'>Amount in the past</label>', f'>{t["amount_past"]}</label>', html)
    html = re.sub(r'>Would be worth today</label>', f'>{t["worth_today"]}</label>', html)
    
    # Update features section
    html = re.sub(r'>Why Use Our Converter\?</h2>', f'>{t["why_use"]}</h2>', html)
    html = re.sub(r'<h3 class="font-bold mb-2">Crypto \+ Fiat</h3>', f'<h3 class="font-bold mb-2">{t["crypto_fiat"]}</h3>', html)
    html = re.sub(r'>Convert between traditional currencies and crypto in one place\.</p>', f'>{t["crypto_desc"]}</p>', html)
    html = re.sub(r'<h3 class="font-bold mb-2">Travel Mode</h3>', f'<h3 class="font-bold mb-2">{t["travel_mode"]}</h3>', html)
    html = re.sub(r'>See your money in 24\+ travel destinations instantly\.</p>', f'>{t["travel_desc"]}</p>', html)
    html = re.sub(r'<h3 class="font-bold mb-2">Salary Comparison</h3>', f'<h3 class="font-bold mb-2">{t["salary_compare"]}</h3>', html)
    html = re.sub(r'>Compare salaries across cities with cost of living adjustment\.</p>', f'>{t["salary_desc"]}</p>', html)
    
    # Update rate info
    html = re.sub(r'>Updated every 60 seconds.*?</p>', f'>{t["rate_info"]}</p>', html)
    
    # Add language switcher script
    lang_switch_script = '''
    <script>
        function switchLang(lang) {
            if (lang === 'en') {
                window.location.href = '/';
            } else {
                window.location.href = '/' + lang + '.html';
            }
        }
    </script>
</body>'''
    html = re.sub(r'</body>', lang_switch_script, html)
    
    # Write file
    filename = 'index.html' if lang == 'en' else f'{lang}.html'
    with open(filename, 'w') as f:
        f.write(html)
    print(f'Created {filename}')

# Generate all language files
for lang, translations in TRANSLATIONS.items():
    create_language_file(lang, translations)

print(f'\n✅ Generated {len(TRANSLATIONS)} language files!')
