"""Builds QueensCoaching local area pages (e.g. /tutor-orleans-ottawa/).
Usage: python3 tools/make_local_pages.py .
Shares header, footer and course list with make_course_pages.py.
To add an area later: add an entry to AREAS and re-run.
Only list schools that have been checked against a reliable source.
"""
import json, sys, os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from make_course_pages import SITE, HEAD_FONTS, LOGO, WA_ICON, FOOTER, COURSES, e, TOPBAR, header  # noqa: E402

AREAS = [
    {
        "slug": "tutor-orleans-ottawa",
        "name": "Orléans",
        "title": "Math & Science Tutor in Orléans, Ottawa | Grade 9–12 | QueensCoaching",
        "desc": "1-on-1 high school Math, Chemistry, Biology and Physics tutoring in Orléans, Ottawa. In-home or online sessions, every Ontario course code, notes and stationery included. Book a free assessment.",
        "h1": "High School Math & Science Tutor in Orléans",
        "intro": "1-on-1 Grade 9–12 Math, Chemistry, Biology and Physics tutoring for Orléans families, in your home or live online. We fix the basics while we cover the curriculum, with personalized notes and stationery included.",
        "neighbourhoods": ["Avalon", "Chapel Hill", "Convent Glen", "Fallingbrook", "Queenswood Heights", "Notre-Dame-des-Champs"],
        "schools": [("Sir Wilfrid Laurier Secondary School", "OCDSB"), ("Cairine Wilson Secondary School", "OCDSB"), ("St. Matthew High School", "OCSB"), ("St. Peter Catholic High School", "OCSB")],
        "local_angle": "Orléans is one of Ottawa's largest family communities, and many students juggle sports, part-time jobs and long east-end commutes. In-home sessions save the drive, and evening and weekend times fit around busy schedules.",
        "featured": ["mth1w-grade-9-math-tutor-ottawa", "mpm2d-math-tutor-ottawa", "sch4u-chemistry-tutor-ottawa", "mhf4u-advanced-functions-tutor-ottawa"],
        "faq": [
            ("Do you come to our home in Orléans?", "Yes. We offer in-home sessions across Orléans, including Avalon, Chapel Hill, Convent Glen and Fallingbrook, as well as live online sessions."),
            ("Do you tutor students from any Orléans high school?", "Yes. We tutor by Ontario course code, so we can help students from any school in Orléans or across Ottawa."),
            ("Can you help with EQAO Grade 9 Math?", "Yes. Our MTH1W tutoring includes practice in EQAO's online format. The result counts toward the final course mark."),
            ("Are sessions available on evenings and weekends?", "Yes. Tell us your best times when you book the free assessment and we'll match you with a coach."),
        ],
    },
    {
        "slug": "tutor-kanata-ottawa",
        "name": "Kanata",
        "title": "Math & Chemistry Tutor in Kanata | Grade 9–12 | QueensCoaching",
        "desc": "1-on-1 high school Math, Chemistry, Physics and Biology tutoring in Kanata, Ottawa. Calculus, Advanced Functions and Grade 12 Chemistry, in-home or online. Notes and stationery included. Book a free assessment.",
        "h1": "High School Math & Chemistry Tutor in Kanata",
        "intro": "1-on-1 Grade 9–12 Math, Chemistry, Physics and Biology tutoring for Kanata families, in your home or live online. Strong preparation for university STEM programs, with personalized notes and stationery included.",
        "neighbourhoods": ["Kanata Lakes", "Morgan's Grant", "Beaverbrook", "Katimavik", "Bridlewood", "Glen Cairn"],
        "schools": [("Earl of March Secondary School", "OCDSB"), ("A.Y. Jackson Secondary School", "OCDSB"), ("All Saints Catholic High School", "OCSB"), ("Holy Trinity Catholic High School", "OCSB")],
        "local_angle": "With Kanata North's technology park nearby, many Kanata students aim for engineering, computer science and other STEM programs. Those programs usually ask for Grade 12 Calculus, Advanced Functions and Sciences, which is exactly where we focus.",
        "featured": ["mcv4u-calculus-vectors-tutor-ottawa", "mhf4u-advanced-functions-tutor-ottawa", "sph4u-physics-tutor-ottawa", "sch4u-chemistry-tutor-ottawa"],
        "faq": [
            ("Do you come to our home in Kanata?", "Yes. We offer in-home sessions across Kanata, including Kanata Lakes, Morgan's Grant, Bridlewood and Glen Cairn, as well as live online sessions."),
            ("Which courses do engineering programs usually need?", "Many Ontario engineering programs ask for MCV4U, MHF4U, SCH4U and SPH4U. Check each program's admission requirements, and we can help you plan."),
            ("Do you tutor students from any Kanata high school?", "Yes. We tutor by Ontario course code, so we can help students from any school in Kanata or across Ottawa."),
            ("Can you help with AP or IB courses?", "Yes. We support AP and IB Math and Science alongside the Ontario courses."),
        ],
    },
    {
        "slug": "tutor-barrhaven-ottawa",
        "name": "Barrhaven",
        "title": "Math & Science Tutor in Barrhaven | Grade 9–12 | QueensCoaching",
        "desc": "1-on-1 high school Math and Science tutoring in Barrhaven, Ottawa. Grade 9 Math and EQAO prep through Grade 12 Chemistry and Calculus, in-home or online. Notes and stationery included. Book a free assessment.",
        "h1": "High School Math & Science Tutor in Barrhaven",
        "intro": "1-on-1 Grade 9–12 Math, Chemistry, Biology and Physics tutoring for Barrhaven families, in your home or live online. From the Grade 9 transition to Grade 12 university courses, with personalized notes and stationery included.",
        "neighbourhoods": ["Longfields", "Half Moon Bay", "Stonebridge", "Chapman Mills", "Davidson Heights", "Barrhaven Centre"],
        "schools": [("John McCrae Secondary School", "OCDSB"), ("Longfields-Davidson Heights Secondary School", "OCDSB"), ("St. Joseph High School", "OCSB"), ("St. Mother Teresa High School", "OCSB")],
        "local_angle": "Barrhaven is one of Ottawa's fastest-growing family communities, with many students starting high school each year. A strong start in Grade 9 Math and Science makes every later course easier, so we put extra focus on that transition.",
        "featured": ["mth1w-grade-9-math-tutor-ottawa", "mpm2d-math-tutor-ottawa", "sch3u-chemistry-tutor-ottawa", "sbi4u-biology-tutor-ottawa"],
        "faq": [
            ("Do you come to our home in Barrhaven?", "Yes. We offer in-home sessions across Barrhaven, including Longfields, Half Moon Bay, Stonebridge and Chapman Mills, as well as live online sessions."),
            ("My child is starting Grade 9. When should we start?", "The summer before Grade 9 or the start of the semester is ideal. We strengthen fractions, integers and algebra so MTH1W and EQAO feel manageable."),
            ("Do you tutor students from any Barrhaven high school?", "Yes. We tutor by Ontario course code, so we can help students from any school in Barrhaven or across Ottawa."),
            ("Are sessions available on evenings and weekends?", "Yes. Tell us your best times when you book the free assessment and we'll match you with a coach."),
        ],
    },
    {
        "slug": "tutor-nepean-ottawa",
        "name": "Nepean",
        "title": "Math & Science Tutor in Nepean, Ottawa | Grade 9–12 | QueensCoaching",
        "desc": "1-on-1 high school Math, Chemistry, Biology and Physics tutoring in Nepean, Ottawa. Every Ontario course code plus AP and IB support, in-home or online. Notes and stationery included. Book a free assessment.",
        "h1": "High School Math & Science Tutor in Nepean",
        "intro": "1-on-1 Grade 9–12 Math, Chemistry, Biology and Physics tutoring for Nepean families, in your home or live online. Ontario courses plus AP and IB support, with personalized notes and stationery included.",
        "neighbourhoods": ["Centrepointe", "Craig Henry", "Bells Corners", "Crestview", "Tanglewood", "Qualicum"],
        "schools": [("Merivale High School", "OCDSB"), ("Sir Robert Borden High School", "OCDSB"), ("Bell High School", "OCDSB")],
        "local_angle": "Nepean is central to the west and south of the city, so in-home sessions are easy to arrange. Families here often ask about specialized programs like AP and IB, and we support those alongside the regular Ontario courses.",
        "featured": ["mhf4u-advanced-functions-tutor-ottawa", "sch4u-chemistry-tutor-ottawa", "sbi4u-biology-tutor-ottawa", "sph4u-physics-tutor-ottawa"],
        "faq": [
            ("Do you come to our home in Nepean?", "Yes. We offer in-home sessions across Nepean, including Centrepointe, Craig Henry, Bells Corners and Crestview, as well as live online sessions."),
            ("Can you help with AP or IB courses?", "Yes. We support AP and IB Math and Science, including SL and HL, alongside the Ontario courses."),
            ("Do you tutor students from any Nepean high school?", "Yes. We tutor by Ontario course code, so we can help students from any school in Nepean or across Ottawa."),
            ("Are sessions available on evenings and weekends?", "Yes. Tell us your best times when you book the free assessment and we'll match you with a coach."),
        ],
    },
    {
        "slug": "tutor-stittsville-ottawa",
        "name": "Stittsville",
        "title": "Math & Science Tutor in Stittsville | Grade 9–12 | QueensCoaching",
        "desc": "1-on-1 high school Math, Chemistry, Biology and Physics tutoring in Stittsville, Ottawa. In-home or online, every Ontario course code, notes and stationery included. Book a free assessment.",
        "h1": "High School Math & Science Tutor in Stittsville",
        "intro": "1-on-1 Grade 9–12 Math, Chemistry, Biology and Physics tutoring for Stittsville families, in your home or live online. We fix the basics while we cover the curriculum, with personalized notes and stationery included.",
        "neighbourhoods": ["Fairwinds", "Jackson Trails", "Westwood", "Fernbank", "Granite Ridge", "Crossing Bridge"],
        "schools": [("Maplewood Secondary School", "OCDSB"), ("Sacred Heart High School", "OCSB")],
        "local_angle": "Stittsville's high school options are growing: Maplewood Secondary School opened in 2024 and is adding a grade each year. Whatever school your child attends, we follow the same Ontario course codes, so tutoring stays consistent as they move up.",
        "featured": ["mth1w-grade-9-math-tutor-ottawa", "mpm2d-math-tutor-ottawa", "sch4u-chemistry-tutor-ottawa", "mcv4u-calculus-vectors-tutor-ottawa"],
        "faq": [
            ("Do you come to our home in Stittsville?", "Yes. We offer in-home sessions across Stittsville, including Fairwinds, Jackson Trails, Westwood and Fernbank, as well as live online sessions."),
            ("Do you tutor students from any Stittsville high school?", "Yes. We tutor by Ontario course code, so we can help students from any school in Stittsville or across Ottawa."),
            ("Can you help with EQAO Grade 9 Math?", "Yes. Our MTH1W tutoring includes practice in EQAO's online format. The result counts toward the final course mark."),
            ("Are sessions available on evenings and weekends?", "Yes. Tell us your best times when you book the free assessment and we'll match you with a coach."),
        ],
    },
]

BOARD = {"OCDSB": "Ottawa-Carleton District School Board", "OCSB": "Ottawa Catholic School Board"}


def page(a):
    url = f"{SITE}/{a['slug']}/"
    courses = {c["slug"]: c for c in COURSES}
    biz_ld = {
        "@context": "https://schema.org", "@type": "Service",
        "name": f"High school Math & Science tutoring in {a['name']}",
        "serviceType": "Tutoring",
        "description": a["desc"],
        "provider": {"@type": ["EducationalOrganization", "LocalBusiness"], "@id": f"{SITE}/#business", "name": "QueensCoaching", "url": SITE + "/", "telephone": "+1-613-297-6844"},
        "areaServed": [{"@type": "Place", "name": f"{a['name']}, Ottawa, ON"}] + [{"@type": "Place", "name": f"{n}, Ottawa, ON"} for n in a["neighbourhoods"]],
    }
    faq_ld = {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": ans}} for q, ans in a["faq"]]}
    crumb_ld = {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Home", "item": SITE + "/"},
        {"@type": "ListItem", "position": 2, "name": "Areas we serve", "item": SITE + "/areas/"},
        {"@type": "ListItem", "position": 3, "name": a["name"], "item": url}]}
    lds = "\n".join(f'<script type="application/ld+json">\n{json.dumps(x, ensure_ascii=False, indent=2)}\n</script>' for x in (biz_ld, faq_ld, crumb_ld))

    hoods = ", ".join(a["neighbourhoods"])
    featured = "".join(
        f'<article class="card"><span class="tag">{e(courses[s]["short"])}</span><h3 class="course-title">{e(courses[s]["code"])}</h3><p>{e(courses[s]["intro"].split(". ")[0])}.</p><a class="card-link" href="/{s}/">See {e(courses[s]["code"])} tutoring →</a></article>'
        for s in a["featured"] if s in courses)
    all_courses = "".join(f'<a class="pill" href="/{c["slug"]}/"><strong>{e(c["code"])}</strong> {e(c["short"])}</a>' for c in COURSES)
    schools = "".join(f'<li style="border:1px solid var(--lavender-line)"><strong>{e(n)}</strong> · {e(BOARD[b])}</li>' for n, b in a["schools"])
    faqs = "".join(f"<details><summary>{e(q)}</summary><p>{e(ans)}</p></details>" for q, ans in a["faq"])
    other = "".join(f'<a class="pill" href="/{x["slug"]}/">Tutor in {e(x["name"])}</a>' for x in AREAS if x is not a)

    return f'''<!doctype html>
<html lang="en-CA">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(a['title'])}</title>
<meta name="description" content="{e(a['desc'])}">
<link rel="canonical" href="{url}">
<meta name="theme-color" content="#4B2A7B">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="icon" href="/favicon-32.png" sizes="32x32" type="image/png">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<meta property="og:type" content="website">
<meta property="og:site_name" content="QueensCoaching">
<meta property="og:title" content="{e(a['title'])}">
<meta property="og:description" content="{e(a['desc'])}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{SITE}/og-image.png">
<meta property="og:locale" content="en_CA">
<meta name="twitter:card" content="summary_large_image">
{HEAD_FONTS}
<link rel="stylesheet" href="/styles.css">
{lds}
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
{TOPBAR}
{header('Areas')}

<main id="main">
<section class="brand">
  <div class="wrap"><nav class="breadcrumb" aria-label="Breadcrumb"><a href="/">Home</a> › <a href="/areas/">Areas we serve</a> › <span>{e(a['name'])}</span></nav></div>
  <div class="wrap hero" style="display:grid;gap:48px;grid-template-columns:repeat(auto-fit,minmax(min(100%,460px),1fr));align-items:center;padding-top:40px;padding-bottom:72px">
    <div class="hero-copy">
      <span class="badge badge-solid">In-home &amp; online · {e(a['name'])}</span>
      <h1 style="margin:0;font-family:var(--serif);font-weight:600;font-size:clamp(34px,4.4vw,54px);letter-spacing:-.02em;line-height:1.08">{e(a['h1'])}</h1>
      <p class="hero-sub">{e(a['intro'])}</p>
      <div class="btn-row">
        <a class="btn btn-gold" href="/book/">Book a Free Assessment</a>
        <a class="btn btn-outline" href="https://wa.me/16132976844">WhatsApp us</a>
      </div>
    </div>
    <div class="white-card">
      <h2 style="margin:0;font-family:var(--serif);font-size:24px;font-weight:600;color:var(--purple)">Tutoring in {e(a['name'])} at a glance</h2>
      <dl class="facts">
        <dt>Grades</dt><dd>9 to 12, every Ontario Math &amp; Science course</dd>
        <dt>Sessions</dt><dd>In your home in {e(a['name'])}, or live online</dd>
        <dt>Areas</dt><dd>{e(hoods)} and nearby</dd>
        <dt>Included</dt><dd>Personalized notes, stationery, 1-on-1 attention</dd>
        <dt>Start</dt><dd>Free assessment with a foundations check</dd>
      </dl>
    </div>
  </div>
</section>

<section class="section"><div class="wrap grid-2">
  <div>
    <p class="eyebrow">Tutoring for {e(a['name'])} families</p>
    <h2 class="h2">We fix the basics while we cover the curriculum.</h2>
  </div>
  <div>
    <p class="big-quote" style="margin:0 0 16px">Looking for a <strong>high school math tutor in {e(a['name'])}</strong>, or a <strong>science tutor</strong> for Chemistry, Biology or Physics? {e(a['local_angle'])}</p>
    <p style="margin:0;color:var(--muted)">Every student starts with a free assessment. We find the gaps from earlier grades, close them while teaching the current course, and send parents a progress note every month.</p>
  </div>
</div></section>

<section class="section alt"><div class="wrap">
  <p class="eyebrow">Popular courses</p>
  <h2 class="h2">Course tutoring for {e(a['name'])} students</h2>
  <p class="lead">Taught by Ontario course code, so sessions match exactly what your child is learning at school.</p>
  <div class="grid">{featured}</div>
  <div class="pill-box" style="margin-top:24px"><h3>All courses we tutor</h3><div class="pills">{all_courses}</div></div>
</div></section>

<section class="section"><div class="wrap grid-2">
  <div>
    <p class="eyebrow">High schools in {e(a['name'])}</p>
    <h2 class="h2">Tutoring for students from any {e(a['name'])} school</h2>
    <p style="margin:0;color:var(--muted)">We follow the Ontario curriculum by course code, so we can help students from any high school. Nearby English-language high schools include:</p>
  </div>
  <div>
    <ul class="check-list" style="list-style:none">{schools}</ul>
    <p style="margin:14px 0 0;font-size:14px;color:var(--muted)">QueensCoaching is an independent tutoring service and is not affiliated with these schools or school boards.</p>
  </div>
</div></section>

<section class="section alt"><div class="wrap">
  <p class="eyebrow">How it works in {e(a['name'])}</p>
  <h2 class="h2">From first message to first session</h2>
  <ol class="steps" style="margin-top:28px">
    <li><p class="step-num">01</p><h3>Book</h3><p>Fill in the short form or WhatsApp us. We reply within 24 hours.</p></li>
    <li><p class="step-num">02</p><h3>Assess</h3><p>A free session, at home in {e(a['name'])} or online, with a foundations check.</p></li>
    <li><p class="step-num">03</p><h3>Plan</h3><p>A written plan within 24 hours: the gaps to close and the course to cover.</p></li>
    <li><p class="step-num">04</p><h3>Coach</h3><p>Regular 1-on-1 sessions at times that suit your family.</p></li>
  </ol>
</div></section>

<section class="section"><div class="wrap narrow">
  <h2 class="h2" style="margin-bottom:28px">Questions from {e(a['name'])} parents</h2>
  <div class="faq">{faqs}</div>
</div></section>

<section style="padding-bottom:80px"><div class="wrap">
  <h2 style="margin:0 0 16px;font-size:20px">Other areas we serve</h2>
  <div class="pills">{other}<a class="pill" href="/areas/">Online, anywhere</a></div>
</div></section>

<section class="section brand cta"><div class="wrap narrow">
  <h2>Ready to get started in {e(a['name'])}?</h2>
  <p>Book a free assessment with a foundations check. No obligation.</p>
  <div class="btn-row" style="justify-content:center">
    <a class="btn btn-gold" href="/book/">Book Free Assessment</a>
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
    for a in AREAS:
        d = os.path.join(root, a["slug"])
        os.makedirs(d, exist_ok=True)
        with open(os.path.join(d, "index.html"), "w", encoding="utf-8") as f:
            f.write(page(a))
        print("wrote", a["slug"])
