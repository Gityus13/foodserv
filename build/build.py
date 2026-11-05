#!/usr/bin/env python3
"""Generates a single index.html containing AZ, EN and RU (switched in place by JS). Edit TEXT below, then run: python3 build/build.py"""
import re, datetime, pathlib
ROOT = pathlib.Path(__file__).resolve().parent.parent
Y = datetime.date.today().year
SINCE = 2008
PHONE, PHONE_TEL, WA = "+994 50 706 9438", "+994507069438", "https://wa.me/994507069438"
REQUEST = "https://info.foodserv.az"
DOMAIN = "https://foodserv.az"
LANGS = [("az", "index.html", "az_AZ", "./"), ("en", "", "en_US", ""), ("ru", "", "ru_RU", "")]

# key, az, en, ru
TEXT = [
("title","FoodService | Azərbaycanda premium qida distribütoru","FoodService | Premium food distributor in Azerbaijan","FoodService | Дистрибьютор продуктов питания премиум-класса в Азербайджане"),
("desc","2008-ci ildən restoran, otel, supermarket və katerinq şirkətləri üçün yüksək keyfiyyətli qida məhsullarının topdan satışı və çatdırılması.","Wholesale supply and delivery of premium food products to restaurants, hotels, supermarkets and caterers across Azerbaijan since 2008.","Оптовые поставки и доставка продуктов питания премиум-класса для ресторанов, отелей, супермаркетов и кейтеринга по всему Азербайджану с 2008 года."),
("n_about","Haqqımızda","About","О компании"),("n_products","Məhsullar","Products","Продукция"),("n_services","Xidmətlər","Services","Услуги"),("n_contact","Əlaqə","Contact","Контакты"),
("call","Zəng edin","Call us","Позвонить"),
("h1a","Azərbaycanda premium","Premium food distribution","Дистрибьютор продуктов"),("h1b","qida distribütoru","across Azerbaijan","премиум-класса в Азербайджане"),
("h_p","Keyfiyyətli qida məhsullarını restoranlara, otellərə və supermarketlərə bütün ölkə üzrə dəqiqliklə çatdırırıq.","We deliver quality food products to restaurants, hotels and supermarkets nationwide, with precision and care.","Доставляем качественные продукты ресторанам, отелям и супермаркетам по всей стране — точно и бережно."),
("b_prod","Məhsullarımız","Our products","Наша продукция"),("b_talk","Bizimlə əlaqə","Get in touch","Связаться с нами"),
("a_h2","Etibarlı tərəfdaş. Sabit keyfiyyət.","A reliable partner. Consistent quality.","Надёжный партнёр. Стабильное качество."),
("a_p1","FoodService 2008-ci ildən Azərbaycanda restoranlara, otellərə, supermarketlərə və katerinq xidmətlərinə yüksək keyfiyyətli qida məhsulları təqdim edir.","Since 2008, FoodService has supplied high-quality food products to restaurants, hotels, supermarkets and catering services across Azerbaijan.","С 2008 года FoodService поставляет высококачественные продукты ресторанам, отелям, супермаркетам и кейтеринговым службам по всему Азербайджану."),
("a_p2","Məhsulları etibarlı yerli və beynəlxalq təchizatçılardan əldə edir, müştərilərimizə yalnız təzə və yüksək keyfiyyətli məhsullar çatdırırıq.","We source from trusted local and international suppliers, so our clients receive only fresh, high-quality products.","Мы работаем с надёжными местными и международными поставщиками, чтобы клиенты получали только свежие продукты высокого качества."),
("f1t","Keyfiyyət zəmanəti","Quality assurance","Гарантия качества"),("f1d","Seçilmiş təchizatçılar və ardıcıl keyfiyyət standartları.","Vetted suppliers and consistent quality standards.","Проверенные поставщики и стабильные стандарты качества."),
("f2t","Sürətli çatdırılma","Fast delivery","Быстрая доставка"),("f2d","Bütün ölkə üzrə vaxtında və etibarlı logistika.","Timely, dependable logistics nationwide.","Своевременная и надёжная логистика по всей стране."),
("f3t","Premium məhsullar","Premium products","Продукция премиум-класса"),("f3d","Yerli və beynəlxalq mənbələrdən geniş çeşid.","A broad range from local and international sources.","Широкий ассортимент от местных и международных поставщиков."),
("f4t","24/7 dəstək","24/7 support","Поддержка 24/7"),("f4d","Sifarişlərinizlə bağlı həmişə əlçatandıq.","Always available for your orders.","Всегда на связи по вашим заказам."),
("s1","Müştəri","Clients","Клиентов"),("s2","Məhsul","Products","Товаров"),("s3","Şəhər","Cities","Городов"),("s4","İllik təcrübə","Years of experience","Лет опыта"),
("p_h2","Hər kateqoriyada təzəlik və keyfiyyət","Freshness and quality in every category","Свежесть и качество в каждой категории"),
("p_p","Yerli və beynəlxalq təchizatçılardan geniş çeşid.","A wide range from local and international suppliers.","Широкий ассортимент от местных и международных поставщиков."),
("p1t","Təzə tərəvəzlər","Fresh vegetables","Свежие овощи"),("p1d","Yerli mənbələrdən təmin edilən təzə tərəvəzlər, birbaşa sizə çatdırılır.","Fresh vegetables from local sources, delivered straight to you.","Свежие овощи от местных производителей с доставкой к вам."),
("p2t","Süd məhsulları","Dairy","Молочная продукция"),("p2d","Süd, pendir, yoğurt və digər süd məhsulları.","Milk, cheese, yogurt and other dairy products.","Молоко, сыры, йогурты и другая молочная продукция."),
("p3t","Ət məhsulları","Meat","Мясная продукция"),("p3d","Biznesiniz üçün yüksək keyfiyyətli, helal sertifikatlı ət.","High-quality, halal-certified meat for your business.","Мясо высокого качества с сертификатом халяль для вашего бизнеса."),
("sv_h2","Biznesinizə uyğun təchizat həlləri","Supply solutions built around your business","Решения по поставкам под ваш бизнес"),
("sv1t","Etibarlı çatdırılma","Reliable delivery","Надёжная доставка"),("sv1d","Effektiv logistika şəbəkəmiz sifarişlərin Azərbaycanın hər yerinə vaxtında çatmasını təmin edir.","Our logistics network gets your orders to every part of Azerbaijan on time.","Наша логистическая сеть доставляет заказы в любую точку Азербайджана вовремя."),
("sv2t","Topdan satış","Wholesale","Оптовые продажи"),("sv2d","Böyük həcmli sifarişlər üçün xüsusi topdan qiymətlər.","Dedicated wholesale pricing for large-volume orders.","Специальные оптовые цены для крупных заказов."),
("sv3t","Planlı çatdırılma","Scheduled delivery","Плановые поставки"),("sv3d","Biznes ehtiyaclarınıza və inventar dövrünüzə uyğun müntəzəm qrafik.","Regular delivery schedules aligned with your inventory cycle.","Регулярные графики поставок под ваш цикл закупок."),
("c_h2","Əməkdaşlığa hazırsınız?","Ready to work together?","Готовы к сотрудничеству?"),
("c_p","Azərbaycan üzrə yüzlərlə biznes qida təchizatı üçün FoodService-ə etibar edir.","Hundreds of businesses across Azerbaijan rely on FoodService for their food supply.","Сотни компаний по всему Азербайджану доверяют FoodService поставки продуктов."),
("c_req","Sorğu göndərin","Send a request","Отправить запрос"),
("ft_tag","2008-ci ildən Azərbaycan üzrə premium qida təchizatı.","Premium food distribution across Azerbaijan since 2008.","Дистрибуция продуктов премиум-класса по Азербайджану с 2008 года."),
("rights","Bütün hüquqlar qorunur.","All rights reserved.","Все права защищены."),
("m1","Restoranlar","Restaurants","Рестораны"),("m2","Otellər","Hotels","Отели"),("m3","Supermarketlər","Supermarkets","Супермаркеты"),("m4","Katerinq","Catering","Кейтеринг"),
("ck_t","Sayt işləməsi və statistika üçün kukilərdən istifadə edirik.","We use cookies to run the site and measure traffic.","Мы используем файлы cookie для работы сайта и статистики."),
("ck_y","Qəbul et","Accept","Принять"),("ck_n","Rədd et","Decline","Отклонить"),
]

TEMPLATE = r'''<!DOCTYPE html>
<html lang="{{lang}}">
<head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{{title}}</title>
<meta name="description" content="{{desc}}">
<link rel="canonical" href="{{url}}">
<meta property="og:type" content="website"><meta property="og:site_name" content="FoodService"><meta property="og:title" content="{{title}}"><meta property="og:description" content="{{desc}}"><meta property="og:url" content="{{url}}"><meta property="og:locale" content="{{loc}}"><meta property="og:image" content="https://foodserv.az/assets/og.png"><meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#0a3329">
<link rel="icon" href="assets/favicon.svg" type="image/svg+xml"><link rel="icon" href="assets/favicon.png" sizes="32x32" type="image/png"><link rel="apple-touch-icon" href="assets/apple-touch-icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Geologica:wght@300;400;600&family=Onest:wght@400;500;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/css/style.css">
<script>document.documentElement.className='js'</script>
<script type="application/ld+json">{"@context":"https://schema.org","@type":"Organization","name":"FoodService","url":"https://foodserv.az","foundingDate":"2008","telephone":"{{ptel}}","areaServed":"AZ"}</script>
</head>
<body>
<div class="pgb"></div>
<header class="hd"><div class="wrap">
<a class="logo" href="#home" aria-label="FoodService"><img class="lm" src="assets/logo.png" alt="" onerror="this.parentNode.classList.add('nl');this.remove()"><span class="lf"><svg viewBox="0 0 32 32" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"><rect x="2" y="2" width="28" height="28" rx="6"/><path d="M9 22c0-8 5-12 14-12 0 8-5 13-13 13M9 22l8-8"/></svg>FoodService</span></a>
<nav class="mn" aria-label="Main"><a href="#about">{{n_about}}</a><a href="#products">{{n_products}}</a><a href="#services">{{n_services}}</a><a href="#contact">{{n_contact}}</a></nav>
<div class="hr"><div class="lg">{{langs}}</div><a class="btn sm" href="tel:{{ptel}}">{{phone}}</a>
<button class="bg" aria-label="Menu" aria-expanded="false"><i></i><i></i></button></div>
</div></header>
<div class="mm" id="mm"><a href="#about">{{n_about}}</a><a href="#products">{{n_products}}</a><a href="#services">{{n_services}}</a><a href="#contact">{{n_contact}}</a><a href="tel:{{ptel}}">{{phone}}</a></div>
<main>
<section class="hero" id="home"><div class="hbg"></div><div class="wrap hg">
<div class="ht"><h1><span class="ln"><span>{{h1a}}</span></span><span class="ln"><span>{{h1b}}</span></span></h1>
<p class="hp">{{h_p}}</p>
<div class="ba"><a class="btn pr1" href="#products">{{b_prod}}</a><a class="tl" href="#contact">{{b_talk}}</a></div></div>
<svg class="rt" viewBox="0 0 700 560" fill="none" aria-hidden="true">
<g class="rp" stroke="#8fd1b9" stroke-width="2.5" stroke-linecap="round"><path id="mp" pathLength="1" d="M60 450C210 430 250 300 380 285S560 160 640 90"/><path pathLength="1" style="--dl:1.6s" d="M380 285C450 380 530 400 610 430"/><path pathLength="1" style="--dl:2.1s" d="M60 450C200 510 360 520 480 495"/></g>
<g class="nd" fill="#0a3329" stroke="#8fd1b9" stroke-width="2.5"><circle cx="380" cy="285" r="10" style="--dl:1.5s"/><circle cx="640" cy="90" r="10" style="--dl:3s"/><circle cx="610" cy="430" r="10" style="--dl:2.4s"/><circle cx="480" cy="495" r="10" style="--dl:2.8s"/></g>
<g class="rl"><text x="360" y="256" text-anchor="end" style="--dl:1.7s">{{m1}}</text><text x="640" y="58" text-anchor="end" style="--dl:3.2s">{{m2}}</text><text x="630" y="472" text-anchor="end" style="--dl:2.6s">{{m3}}</text><text x="480" y="542" text-anchor="middle" style="--dl:3s">{{m4}}</text><text class="hl" x="60" y="412" style="--dl:.6s">FoodService</text></g>
<circle class="hub" cx="60" cy="450" r="16" fill="#f0b323"/>
<circle r="7" fill="#f0b323"><animateMotion dur="9s" begin="3.4s" repeatCount="indefinite" keyPoints="0;1;1" keyTimes="0;.8;1" calcMode="linear"><mpath href="#mp"/></animateMotion></circle>
</svg></div></section>

<section class="mq" aria-hidden="true"><div class="mt"><span>{{m1}}</span><span>{{m2}}</span><span>{{m3}}</span><span>{{m4}}</span><span>{{m1}}</span><span>{{m2}}</span><span>{{m3}}</span><span>{{m4}}</span></div></section>

<section class="sec" id="about"><div class="wrap ag">
<h2>{{a_h2}}</h2>
<div><p class="lead">{{a_p1}}</p><p class="mu">{{a_p2}}</p>
<dl class="fg"><div class="fe"><dt>{{f1t}}</dt><dd>{{f1d}}</dd></div><div class="fe"><dt>{{f2t}}</dt><dd>{{f2d}}</dd></div><div class="fe"><dt>{{f3t}}</dt><dd>{{f3d}}</dd></div><div class="fe"><dt>{{f4t}}</dt><dd>{{f4d}}</dd></div></dl></div>
</div><div class="wrap"><figure class="ph wide"><img src="assets/img/about.jpg" alt="" onload="this.closest('.ph').classList.add('ok')"></figure></div></section>

<section class="stats"><div class="wrap sg">
<div><b data-n="500" data-s="+">500+</b><span>{{s1}}</span></div><div><b data-n="1000" data-s="+">1000+</b><span>{{s2}}</span></div><div><b data-n="10" data-s="+">10+</b><span>{{s3}}</span></div><div><b data-since="2008" data-s="+">{{yrs}}+</b><span>{{s4}}</span></div>
</div></section>

<section class="sec" id="products"><div class="wrap pg2">
<div class="ps"><h2>{{p_h2}}</h2><p class="mu">{{p_p}}</p><figure class="pimg"><img class="on" src="assets/img/vegetables.jpg" alt="" onload="this.closest('.pimg').classList.add('ok')"><img src="assets/img/dairy.jpg" alt="" onload="this.closest('.pimg').classList.add('ok')"><img src="assets/img/meat.jpg" alt="" onload="this.closest('.pimg').classList.add('ok')"></figure></div>
<ul class="pl">
<li class="pr o"><button aria-expanded="true"><span>{{p1t}}</span><i class="px"></i></button><div class="pd"><div><p>{{p1d}}</p></div></div></li>
<li class="pr"><button aria-expanded="false"><span>{{p2t}}</span><i class="px"></i></button><div class="pd"><div><p>{{p2d}}</p></div></div></li>
<li class="pr"><button aria-expanded="false"><span>{{p3t}}</span><i class="px"></i></button><div class="pd"><div><p>{{p3d}}</p></div></div></li>
</ul></div></section>

<section class="sec alt" id="services"><div class="wrap">
<h2 class="sh">{{sv_h2}}</h2>
<div class="sg3"><div class="sv"><figure class="ph"><img src="assets/img/delivery.jpg" alt="" onload="this.closest('.ph').classList.add('ok')"></figure><h3>{{sv1t}}</h3><p>{{sv1d}}</p></div><div class="sv"><figure class="ph"><img src="assets/img/wholesale.jpg" alt="" onload="this.closest('.ph').classList.add('ok')"></figure><h3>{{sv2t}}</h3><p>{{sv2d}}</p></div><div class="sv"><figure class="ph"><img src="assets/img/schedule.jpg" alt="" onload="this.closest('.ph').classList.add('ok')"></figure><h3>{{sv3t}}</h3><p>{{sv3d}}</p></div></div>
</div></section>

<section class="gal"><div class="gt"><figure class="gi"><img src="assets/img/gallery-1.jpg" alt="" onload="this.parentNode.classList.add('ok');this.closest('.gal').classList.add('ok')"></figure><figure class="gi"><img src="assets/img/gallery-2.jpg" alt="" onload="this.parentNode.classList.add('ok');this.closest('.gal').classList.add('ok')"></figure><figure class="gi"><img src="assets/img/gallery-3.jpg" alt="" onload="this.parentNode.classList.add('ok');this.closest('.gal').classList.add('ok')"></figure><figure class="gi"><img src="assets/img/gallery-4.jpg" alt="" onload="this.parentNode.classList.add('ok');this.closest('.gal').classList.add('ok')"></figure><figure class="gi"><img src="assets/img/gallery-5.jpg" alt="" onload="this.parentNode.classList.add('ok');this.closest('.gal').classList.add('ok')"></figure></div></section>

<section class="cta" id="contact"><div class="wrap cg">
<div><h2>{{c_h2}}</h2><p>{{c_p}}</p></div>
<div class="cc"><a class="num" href="tel:{{ptel}}">{{phone}}</a>
<div class="ba"><a class="btn pr1" href="tel:{{ptel}}">{{call}}</a><a class="btn gh" href="{{wa}}" target="_blank" rel="noopener">WhatsApp</a><a class="btn gh" href="{{req}}" target="_blank" rel="noopener">{{c_req}}</a></div></div>
</div></section>
</main>
<footer class="ft"><div class="wrap fg2">
<div><a class="logo" href="#home" aria-label="FoodService"><img class="lm" src="assets/logo.png" alt="" onerror="this.parentNode.classList.add('nl');this.remove()"><span class="lf">FoodService</span></a><p>{{ft_tag}}</p></div>
<nav><a href="#about">{{n_about}}</a><a href="#products">{{n_products}}</a><a href="#services">{{n_services}}</a><a href="#contact">{{n_contact}}</a></nav>
<div><a href="tel:{{ptel}}">{{phone}}</a><a href="{{wa}}" target="_blank" rel="noopener">WhatsApp</a></div>
</div><div class="wrap cp">&copy; {{year}} FoodService. <span data-t="rights">{{rights}}</span></div></footer>
<div class="mb"><a href="tel:{{ptel}}">{{call}}</a><a href="{{wa}}" target="_blank" rel="noopener">WhatsApp</a></div>
<div class="ck" role="dialog" aria-live="polite"><span data-t="ck_t">{{ck_t}}</span><div><button class="btn sm" data-c="y">{{ck_y}}</button><button class="btn gh" data-c="n">{{ck_n}}</button></div></div>
<script src="assets/js/i18n.js"></script>
<script src="assets/js/gsap.min.js"></script>
<script src="assets/js/ScrollTrigger.min.js"></script>
<script src="assets/js/main.js"></script>
</body></html>
'''

import json
tpl = re.sub(r"<(\w+)([^>]*)>\{\{(\w+)\}\}</\1>", r'<\1\2 data-t="\3">{{\3}}</\1>', TEMPLATE)
d = {k: v[0] for k, *v in TEXT}
d.update(lang="az", url=DOMAIN + "/", loc="az_AZ", ptel=PHONE_TEL, phone=PHONE, wa=WA, req=REQUEST, year=Y, yrs=Y - SINCE,
         langs="".join(f'<button data-l="{l}"{" class=on" if l=="az" else ""}>{l.upper()}</button>' for l, *_ in LANGS))
tpl = tpl.replace(" data-t=\"langs\"", "")
html = re.sub(r"\{\{(\w+)\}\}", lambda m: str(d[m[1]]), tpl)
html = html.replace("<b data-n=", "<b data-n=")
data = {l: {k: v[i] for k, *v in TEXT} for i, (l, *_) in enumerate(LANGS)}
html = html.replace('<script src="assets/js/i18n.js"></script>', "<script>window.I18N=" + json.dumps(data, ensure_ascii=False) + ";</script>")
(ROOT / "index.html").write_text(html, encoding="utf-8")
sm = f'<url><loc>{DOMAIN}/</loc><lastmod>{datetime.date.today().isoformat()}</lastmod></url>'
(ROOT / "sitemap.xml").write_text(f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">{sm}</urlset>\n')
print("built")
