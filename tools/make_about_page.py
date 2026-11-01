"""Builds the founder page /about-harleen-kaur/.
Usage: python3 tools/make_about_page.py .
Edit the text below and re-run to update the page.
"""
import json, os, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from make_course_pages import SITE, HEAD_FONTS, LOGO, WA_ICON, FOOTER, COURSES, e  # noqa: E402

SLUG = "about-harleen-kaur"
NAME = "Harleen Kaur"
ROLE = "Founder & Lead Coach"
QUOTE = ("I've taught students on four continents, and I've learned one thing: every student can master Science "
         "and Math when the basics are strong. My job is to find what's missing, rebuild it with patience, and help "
         "each student walk into exams with confidence.")
BIO = [
    "Harleen brings more than 10 years of international experience across Canada, the United States, the United "
    "Kingdom, Australia, New Zealand and India. She holds a B.Sc. and an M.Sc. and has a background in pharmacy, "
    "which gives her a deep, practical understanding of Chemistry and Biology.",
    "She founded QueensCoaching to give high school students the personal attention they rarely get in a busy "
    "classroom. Her approach is simple: find the gaps from earlier grades, close them while covering the "
    "curriculum, and build the confidence students need for university.",
    "Harleen personally coaches Grade 9–12 Chemistry, Biology and Math, in person in Ottawa and live online.",
]
COUNTRIES = ["Canada", "United States", "United Kingdom", "Australia", "New Zealand", "India"]
TEACHES = ["sch3u-chemistry-tutor-ottawa", "sch4u-chemistry-tutor-ottawa", "sch4c-college-chemistry-tutor-ottawa",
           "sbi3u-biology-tutor-ottawa", "sbi4u-biology-tutor-ottawa", "mth1w-grade-9-math-tutor-ottawa",
           "mpm2d-math-tutor-ottawa", "mcr3u-functions-tutor-ottawa", "mhf4u-advanced-functions-tutor-ottawa"]
TITLE = "Harleen Kaur, Founder & Lead Coach | QueensCoaching Ottawa"
DESC = ("Meet Harleen Kaur, founder of QueensCoaching: 10+ years of international experience, B.Sc. and M.Sc. with a "
        "pharmacy background, coaching Grade 9–12 Chemistry, Biology and Math in Ottawa and online.")


def page():
    url = f"{SITE}/{SLUG}/"
    courses = {c["slug"]: c for c in COURSES}
    person_ld = {
        "@context": "https://schema.org", "@type": "Person",
        "name": NAME, "jobTitle": ROLE, "url": url,
        "image": f"{SITE}/images/harleen-kaur-square.jpg",
        "description": DESC,
        "worksFor": {"@type": "EducationalOrganization", "@id": f"{SITE}/#business", "name": "QueensCoaching", "url": SITE + "/"},
        "knowsAbout": ["Chemistry", "Biology", "Mathematics", "Ontario high school curriculum", "SCH4U", "SBI4U", "MHF4U"],
    }
    crumb_ld = {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Home", "item": SITE + "/"},
        {"@type": "ListItem", "position": 2, "name": NAME, "item": url}]}
    lds = "\n".join(f'<script type="application/ld+json">\n{json.dumps(x, ensure_ascii=False, indent=2)}\n</script>' for x in (person_ld, crumb_ld))
    bio = "".join(f'<p style="margin:0 0 16px;font-size:18px;color:var(--ink-soft)">{e(p)}</p>' for p in BIO)
    countries = "".join(f'<span class="pill">{e(c)}</span>' for c in COUNTRIES)
    teaches = "".join(f'<a class="pill" href="/{s}/"><strong>{e(courses[s]["code"])}</strong> {e(courses[s]["short"])}</a>' for s in TEACHES if s in courses)

    return f'''<!doctype html>
<html lang="en-CA">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(TITLE)}</title>
<meta name="description" content="{e(DESC)}">
<link rel="canonical" href="{url}">
<meta name="theme-color" content="#4B2A7B">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="icon" href="/favicon-32.png" sizes="32x32" type="image/png">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<meta property="og:type" content="profile">
<meta property="og:site_name" content="QueensCoaching">
<meta property="og:title" content="{e(TITLE)}">
<meta property="og:description" content="{e(DESC)}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{SITE}/images/harleen-kaur.jpg">
<meta property="og:locale" content="en_CA">
<meta name="twitter:card" content="summary_large_image">
{HEAD_FONTS}
<link rel="stylesheet" href="/styles.css">
{lds}
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<div class="topbar"><div class="wrap">
  <span>Grade 9–12 Math &amp; Science · Free assessment · In person in Ottawa · Online worldwide</span>
  <a href="tel:+16132976844">Call or WhatsApp +1 613.297.6844</a>
</div></div>
<header class="site-header"><div class="wrap">
  <a class="logo" href="/" aria-label="QueensCoaching home">{LOGO}<span><span class="logo-name">QueensCoaching</span><span class="logo-tag">Rule your subject</span></span></a>
  <nav class="nav" aria-label="Main">
    <a href="/#courses">Courses</a>
    <a href="/sch4u-chemistry-tutor-ottawa/">Chemistry</a>
    <a href="/#exams">Exam Prep</a>
    <a href="/#method">How It Works</a>
    <a href="/#faq">FAQ</a>
  </nav>
  <a class="btn btn-gold" href="/#book">Book Free Assessment</a>
</div></header>

<main id="main">
<section class="brand">
  <div class="wrap"><nav class="breadcrumb" aria-label="Breadcrumb"><a href="/">Home</a> › <span>{e(NAME)}</span></nav></div>
  <div class="wrap founder" style="padding-top:40px;padding-bottom:72px">
    <img class="founder-photo" src="/images/harleen-kaur.jpg" alt="Harleen Kaur, Founder and Lead Coach of QueensCoaching" width="640" height="800">
    <div class="hero-copy">
      <span class="badge badge-solid">Meet the founder</span>
      <h1 style="margin:0;font-family:var(--serif);font-weight:600;font-size:clamp(36px,4.6vw,56px);letter-spacing:-.02em;line-height:1.08">{e(NAME)}</h1>
      <p class="hero-sub" style="font-weight:600;color:var(--gold-light)">{e(ROLE)}, QueensCoaching</p>
      <blockquote class="founder-quote" style="color:#fff;font-size:20px">&ldquo;{e(QUOTE)}&rdquo;</blockquote>
      <div class="btn-row">
        <a class="btn btn-gold" href="/#book">Book a free assessment with Harleen</a>
        <a class="btn btn-outline" href="https://wa.me/16132976844">WhatsApp Harleen</a>
      </div>
    </div>
  </div>
</section>

<section class="section"><div class="wrap grid-2">
  <div>
    <p class="eyebrow">Her story</p>
    <h2 class="h2">10+ years of international experience, now in Ottawa</h2>
  </div>
  <div>{bio}</div>
</div></section>

<section class="section alt"><div class="wrap grid-2">
  <div class="pill-box" style="background:#fff">
    <h3>Experience across six countries</h3>
    <div class="pills">{countries}</div>
  </div>
  <div class="pill-box" style="background:#fff">
    <h3>Qualifications</h3>
    <ul class="founder-facts" style="margin:0">
      <li>Bachelor of Science (B.Sc.)</li>
      <li>Master of Science (M.Sc.)</li>
      <li>Background in pharmacy</li>
    </ul>
  </div>
</div></section>

<section class="section"><div class="wrap">
  <p class="eyebrow">What Harleen teaches</p>
  <h2 class="h2">Grade 9–12 Chemistry, Biology and Math</h2>
  <p class="lead">Taught 1-on-1 by Ontario course code, with personalized notes and stationery included.</p>
  <div class="pills">{teaches}</div>
</div></section>

<section class="section alt"><div class="wrap">
  <p class="eyebrow">Her approach</p>
  <h2 class="h2">We fix the basics while we cover the curriculum.</h2>
  <ol class="steps" style="margin-top:28px">
    <li><p class="step-num">01</p><h3>Assess</h3><p>A free session with a foundations check, shared with parents.</p></li>
    <li><p class="step-num">02</p><h3>Plan</h3><p>A written roadmap: the gaps to close and the course to cover.</p></li>
    <li><p class="step-num">03</p><h3>Coach</h3><p>1-on-1 sessions with personalized notes and practice.</p></li>
    <li><p class="step-num">04</p><h3>Report</h3><p>A before-and-after progress note every month.</p></li>
  </ol>
</div></section>

<section class="section brand cta"><div class="wrap narrow">
  <h2>Learn with Harleen</h2>
  <p>Start with a free assessment and foundations check. No obligation.</p>
  <div class="btn-row" style="justify-content:center">
    <a class="btn btn-gold" href="/#book">Book Free Assessment</a>
    <a class="btn btn-outline" href="https://wa.me/16132976844">Chat on WhatsApp</a>
  </div>
</div></section>
</main>

{FOOTER}

<a class="wa-float" href="https://wa.me/16132976844" aria-label="Chat with QueensCoaching on WhatsApp">{WA_ICON}</a>
</body>
</html>
'''


if __name__ == "__main__":
    root = sys.argv[1]
    d = os.path.join(root, SLUG)
    os.makedirs(d, exist_ok=True)
    with open(os.path.join(d, "index.html"), "w", encoding="utf-8") as f:
        f.write(page())
    print("wrote", SLUG)
