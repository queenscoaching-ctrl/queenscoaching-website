"""Builds the home page and the main tab pages of QueensCoaching:
/ (home), /courses/, /exam-prep/, /how-it-works/, /areas/, /book/
Usage: python3 -I tools/make_site_pages.py <site_folder>
The menu, footer and Google Analytics come from make_course_pages.py.
Pricing is shared on request only, so no page lists prices.
"""
import json, os, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from make_course_pages import SITE, FORM, COURSES, e, shell, ld, crumbs_ld, breadcrumb, cta_band  # noqa: E402
from make_local_pages import AREAS  # noqa: E402

WA = "https://wa.me/16132976844"

BUSINESS_LD = {
    "@context": "https://schema.org",
    "@type": ["EducationalOrganization", "LocalBusiness"],
    "@id": f"{SITE}/#business",
    "name": "QueensCoaching",
    "slogan": "Rule your subject",
    "description": "1-on-1 Grade 9–12 Math and Science tutoring in Ottawa and online, with exam preparation for EQAO, SAT, AP, IB and GCSE.",
    "url": SITE + "/",
    "logo": SITE + "/logo.png",
    "image": SITE + "/og-image.png",
    "telephone": "+1-613-297-6844",
    "founder": {"@type": "Person", "name": "Harleen Kaur", "jobTitle": "Founder & Lead Coach", "url": SITE + "/about-harleen-kaur/", "image": SITE + "/images/harleen-kaur-square.jpg"},
    "email": "myqueenscoaching@gmail.com",
    "sameAs": ["https://g.page/r/CS7iYiJB7OacEBM"],
    "hasMap": "https://g.page/r/CS7iYiJB7OacEBM",
    "address": {"@type": "PostalAddress", "addressLocality": "Ottawa", "addressRegion": "ON", "addressCountry": "CA"},
    "areaServed": [{"@type": "City", "name": "Ottawa"}, "Orléans", "Kanata", "Barrhaven", "Nepean", "Stittsville", "Findlay Creek", "Riverside South"],
    "knowsAbout": ["SCH3U", "SCH4U", "SBI3U", "SBI4U", "MTH1W", "MPM2D", "MFM2P", "SNC1W", "SNC2D", "MCR3U", "MHF4U", "MCV4U", "SPH3U", "SPH4U", "EQAO Grade 9 Math", "SAT", "AP", "IB", "GCSE"],
}

FAQ = [
    ("Which courses do you teach?", "Every Ontario Grade 9–12 Math and Science course, including MTH1W, MPM2D, SNC2D, SCH3U, SCH4U, SBI4U, MHF4U, MCV4U, SPH3U and SPH4U."),
    ("Are notes and stationery really included?", "Yes. Every student gets personalized notes for each unit plus notebooks, binders and practice worksheets at no extra cost."),
    ("How much does tutoring cost?", "Every student's needs are different, so we share pricing after the free assessment, together with a written plan for your child. There is no obligation."),
    ("What happens in the free assessment?", "We check the foundations your child's course depends on, find the gaps holding their marks back, and send you a written plan with a winning strategy within 24 hours."),
    ("Does the EQAO Grade 9 Math assessment affect my child's mark?", "Yes. EQAO results are included in the final MTH1W course mark. We prepare students for its online format."),
    ("My child follows GCSE, IB or CBSE. Can you help?", "Yes. We coach GCSE, IGCSE, A-level, IB, CBSE and AP Math and Science online, in your time zone."),
    ("How do online sessions work?", "Live 1-on-1 video with a shared whiteboard. Notes are sent digitally, and stationery can be shipped within Canada."),
]

SUBJECT_CARDS = f'''<div class="grid">
    <article class="card">
      <span class="tag">Grade 9–12</span>
      <h3 class="course-title">Math</h3>
      <ul class="codes"><li><a href="/mth1w-grade-9-math-tutor-ottawa/"><strong>MTH1W</strong> · Grade 9 Math</a></li><li><a href="/mpm2d-math-tutor-ottawa/"><strong>MPM2D</strong> · Grade 10 Math</a></li><li><a href="/mhf4u-advanced-functions-tutor-ottawa/"><strong>MHF4U</strong> · Advanced Functions</a></li><li><a href="/mcv4u-calculus-vectors-tutor-ottawa/"><strong>MCV4U</strong> · Calculus &amp; Vectors</a></li></ul>
      <a class="card-link" href="/courses/#math">All Math courses →</a>
    </article>
    <article class="card card-feature">
      <span class="tag tag-gold">Signature · Grade 11–12</span>
      <h3 class="course-title">Chemistry</h3>
      <ul class="codes"><li><a href="/sch3u-chemistry-tutor-ottawa/"><strong>SCH3U</strong> · Grade 11 Chemistry</a></li><li><a href="/sch4u-chemistry-tutor-ottawa/"><strong>SCH4U</strong> · Grade 12 Chemistry</a></li><li><a href="/sch4c-college-chemistry-tutor-ottawa/"><strong>SCH4C</strong> · College Chemistry</a></li><li>Special personalized classes</li></ul>
      <a class="card-link" href="/chemistry-tutor-ottawa/">See the Chemistry program →</a>
    </article>
    <article class="card">
      <span class="tag">Grade 11–12</span>
      <h3 class="course-title">Biology</h3>
      <ul class="codes"><li><a href="/sbi3u-biology-tutor-ottawa/"><strong>SBI3U</strong> · Grade 11 Biology</a></li><li><a href="/sbi4u-biology-tutor-ottawa/"><strong>SBI4U</strong> · Grade 12 Biology</a></li><li>Health science prep</li></ul>
      <a class="card-link" href="/courses/#biology">All Biology courses →</a>
    </article>
    <article class="card">
      <span class="tag">Grade 11–12</span>
      <h3 class="course-title">Physics</h3>
      <ul class="codes"><li><a href="/sph3u-physics-tutor-ottawa/"><strong>SPH3U</strong> · Grade 11 Physics</a></li><li><a href="/sph4u-physics-tutor-ottawa/"><strong>SPH4U</strong> · Grade 12 Physics</a></li><li>Engineering prep</li></ul>
      <a class="card-link" href="/courses/#physics">All Physics courses →</a>
    </article>
  </div>'''

STEPS = '''<ol class="steps">
    <li><p class="step-num">01</p><h3>Assess</h3><p>A free session with a foundations check, shared with parents.</p></li>
    <li><p class="step-num">02</p><h3>Plan</h3><p>A written plan with a winning strategy within 24 hours: the gaps to close and the course to cover.</p></li>
    <li><p class="step-num">03</p><h3>Coach</h3><p>1-on-1 sessions with personalized notes, stationery and practice.</p></li>
    <li><p class="step-num">04</p><h3>Report</h3><p>A before-and-after progress note for parents every month.</p></li>
  </ol>'''

FOUNDER = '''<section id="founder" class="section alt"><div class="wrap founder">
  <img class="founder-photo" src="/images/harleen-kaur.jpg" alt="Harleen Kaur, Founder and Lead Coach of QueensCoaching" width="640" height="800" loading="lazy">
  <div>
    <p class="eyebrow">Meet the founder</p>
    <h2 class="h2">Harleen Kaur, Founder &amp; Lead Coach</h2>
    <blockquote class="founder-quote">&ldquo;I&rsquo;ve taught students on four continents, and I&rsquo;ve learned one thing: every student can master Science and Math when the basics are strong. My job is to find what&rsquo;s missing, rebuild it with patience, and help each student walk into exams with confidence.&rdquo;</blockquote>
    <ul class="founder-facts">
      <li>10+ years of international teaching experience across Canada, the US, the UK, Australia, New Zealand and India</li>
      <li>B.Sc. and M.Sc., with a background in pharmacy</li>
      <li>Personally coaches Grade 9–12 Chemistry, Biology and Math</li>
    </ul>
    <div class="btn-row">
      <a class="btn btn-gold" href="/book/">Book a free assessment with Harleen</a>
      <a class="btn btn-ghost" href="/about-harleen-kaur/">Read Harleen&rsquo;s story</a>
    </div>
  </div>
</div></section>'''

PROVIDE = '''<div class="grid-wide" style="margin-top:32px">
    <div class="card">
      <span class="icon-box"><svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="#4B2A7B" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M14 3H6a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V9z"/><path d="M14 3v6h6"/><path d="M8 13h8M8 17h5"/></svg></span>
      <h3>Personalized notes</h3>
      <p>Clear, unit-by-unit notes written for your child's gaps, not photocopies. Kept in a binder they own.</p>
    </div>
    <div class="card">
      <span class="icon-box"><svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="#4B2A7B" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 20h9"/><path d="M16.5 3.5a2.1 2.1 0 0 1 3 3L7 19l-4 1 1-4z"/></svg></span>
      <h3>All stationery included</h3>
      <p>Notebooks, binders and practice worksheets, so students arrive ready to learn.</p>
    </div>
    <div class="card">
      <span class="icon-box"><svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="#4B2A7B" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="8" cy="8" r="3"/><circle cx="16" cy="8" r="3"/><path d="M3 20c0-3 2.5-5 5-5s5 2 5 5M11 20c0-3 2.5-5 5-5s5 2 5 5"/></svg></span>
      <h3>True 1-on-1 attention</h3>
      <p>One coach, one student, every session. No group crowding, no waiting for help.</p>
    </div>
  </div>'''


def page_hero(crumbs, eyebrow, h1, sub, buttons=True, extra=""):
    btns = (f'<div class="btn-row"><a class="btn btn-gold" href="/book/">Book Free Assessment</a>'
            f'<a class="btn btn-outline" href="{WA}">WhatsApp us</a></div>') if buttons else ""
    return f'''<section class="brand">
  {breadcrumb(crumbs)}
  <div class="wrap page-hero">
    <p class="eyebrow">{eyebrow}</p>
    <h1>{h1}</h1>
    <p class="hero-sub">{sub}</p>
    {btns}{extra}
  </div>
</section>'''


# ---------------- Home ----------------
def home():
    body = f'''<section class="hero brand"><div class="wrap">
  <div class="hero-copy">
    <span class="badge">Grade 9–12 specialists</span>
    <h1>Grade 9–12 Math &amp; Science Tutoring, <span>built on strong basics.</span></h1>
    <p class="hero-sub">1-on-1 coaching for every Ontario course, from Grade 9 Math to Grade 12 Chemistry, plus SAT, AP, IB and GCSE prep. In person in Ottawa, online worldwide.</p>
    <div class="chips">
      <span class="chip">Every Ontario course code</span>
      <span class="chip">Personalized notes included</span>
      <span class="chip">Stationery included</span>
      <span class="chip">True 1-on-1 only</span>
    </div>
    <p class="hero-note">Quick question? <a href="{WA}">Message us on WhatsApp</a></p>
  </div>
  <div class="book-card">
    <p class="eyebrow">Free · No obligation</p>
    <h2>Book a free assessment</h2>
    <p>In one session we'll:</p>
    <ul>
      <li>Check the foundations your child's course depends on</li>
      <li>Find the gaps holding their marks back</li>
      <li>Send you a written plan with a winning strategy within 24 hours</li>
    </ul>
    <a class="btn btn-gold" href="/book/">Book My Free Assessment →</a>
    <p class="small">100% confidential · Reply within 24 hours</p>
  </div>
</div></section>

<section class="stats alt" aria-label="At a glance"><div class="wrap">
  <div><p class="stat-num">Grade 9–12</p><p class="stat-label">Math &amp; Science specialists</p></div>
  <div><p class="stat-num">20+ courses</p><p class="stat-label">Every Ontario Math &amp; Science code</p></div>
  <div><p class="stat-num">Notes + stationery</p><p class="stat-label">Included with every program</p></div>
  <div><p class="stat-num">Ottawa + online</p><p class="stat-label">In person or any time zone</p></div>
</div></section>

<section class="section"><div class="wrap">
  <p class="eyebrow">Courses</p>
  <h2 class="h2">Every Grade 9–12 Math &amp; Science course</h2>
  <p class="lead">Your <strong>high school math and science tutor in Ottawa</strong>, teaching by Ontario course code so sessions match exactly what your child is learning at school.</p>
  {SUBJECT_CARDS}
  <div class="btn-row" style="margin-top:28px"><a class="btn btn-ghost" href="/courses/">See all courses →</a></div>
</div></section>

{FOUNDER}

<section class="section"><div class="wrap">
  <div class="grid-2" style="margin-bottom:48px">
    <div><p class="eyebrow">What makes us different</p><h2 class="h2">We fix the basics while we cover the curriculum.</h2></div>
    <p class="big-quote">Most students struggle in Grade 11 Chemistry or Grade 12 Calculus because of a gap from years earlier, such as fractions, algebra or unit conversions. We find those gaps first and close them while teaching the current course.</p>
  </div>
  {STEPS}
  <div class="btn-row" style="margin-top:28px"><a class="btn btn-ghost" href="/how-it-works/">How it works →</a></div>
</div></section>

<section class="section alt"><div class="wrap">
  <p class="eyebrow">Find what you need</p>
  <h2 class="h2">Start where your teen is</h2>
  <div class="grid" style="margin-top:28px">
    <article class="card"><span class="tag">Exam Prep</span><h3>January &amp; June exams</h3><p>A unit-by-unit plan so your teen walks in ready, not cramming.</p><a class="card-link" href="/exam-prep/">Exam Prep →</a></article>
    <article class="card"><span class="tag">Areas</span><h3>In person near you</h3><p>Kanata, Barrhaven, Orléans, Nepean, Stittsville, or live online anywhere.</p><a class="card-link" href="/areas/">Find your area →</a></article>
    <article class="card"><span class="tag">Parent Guides</span><h3>Is SCH3U hard?</h3><p>Plain-English guides to Ontario Grade 9–12 Math and Science courses.</p><a class="card-link" href="/guides/">Read the guides →</a></article>
  </div>
</div></section>

{cta_band()}'''
    return shell("Grade 9–12 Math & Science Tutor in Ottawa & Online | QueensCoaching",
                 "1-on-1 Grade 9–12 Math, Chemistry, Biology and Physics tutoring in Ottawa and online. Every Ontario course code, plus EQAO, SAT, AP, IB and GCSE prep. Notes and stationery included. Book a free assessment.",
                 "/", body, ld(BUSINESS_LD), active="Home")


# ---------------- Courses ----------------
GROUPS = [
    ("math", "Math", "Grade 9–12", ["MTH1W", "MPM2D", "MCR3U", "MHF4U", "MCV4U"],
     [("MFM2P", "Grade 10 Math (applied)"), ("MBF3C", "Grade 11 College Math"), ("MDM4U", "Data Management"), ("MAP4C", "College Tech Math")]),
    ("chemistry", "Chemistry", "Signature program", ["SCH3U", "SCH4U", "SCH4C"], []),
    ("biology", "Biology", "Grade 11–12", ["SBI3U", "SBI4U"], [("SBI3C", "Grade 11 College Biology")]),
    ("physics", "Physics", "Grade 11–12", ["SPH3U", "SPH4U"], [("SPH4C", "Grade 12 College Physics")]),
    ("science", "Grade 9–10 Science", "Foundations", [], [("SNC1W", "Grade 9 Science"), ("SNC2D", "Grade 10 Science"), ("SNC2P", "Grade 10 Science (applied)")]),
]


def courses():
    by = {c["code"]: c for c in COURSES}
    pills = "".join(f'<a class="pill" href="#{gid}">{e(name)}</a>' for gid, name, *_ in GROUPS)
    secs = ""
    for gid, name, tag, codes, extra in GROUPS:
        cards = "".join(
            f'<article class="card{" card-feature" if gid == "chemistry" else ""}"><span class="tag">{by[c]["code"]}</span>'
            f'<h3>{e(by[c]["short"])}</h3><p>{e(by[c]["intro"].split(". ")[0])}.</p>'
            f'<a class="card-link" href="/{by[c]["slug"]}/">View {by[c]["code"]} →</a></article>' for c in codes)
        more = ""
        if extra:
            more = '<div class="pill-box" style="margin-top:20px"><h3>Also coached</h3><div class="pills">' + "".join(
                f'<span class="pill"><strong>{code}</strong> {e(n)}</span>' for code, n in extra) + '</div></div>'
        secs += f'''<section id="{gid}" class="section" style="padding:44px 0 8px"><div class="wrap">
  <h2 class="h2">{e(name)} <span class="tag" style="vertical-align:middle">{e(tag)}</span></h2>
  {('<div class="grid" style="margin-top:20px">' + cards + '</div>') if cards else ''}
  {more}
</div></section>'''
    ladder = '''<section class="section alt" style="margin-top:56px"><div class="wrap">
  <p class="eyebrow">Ontario high school pathways</p>
  <h2 class="h2">Know where your courses lead</h2>
  <p class="lead">The university pathways for Math and Science, Grade 9 to Grade 12. Not sure which courses fit your goals? We'll plan it with you.</p>
  <p style="margin:0 0 12px;font-weight:700">Math</p>
  <div class="ladder">
    <a class="rung" style="text-decoration:none" href="/mth1w-grade-9-math-tutor-ottawa/"><strong>MTH1W</strong><span>Grade 9 Math</span></a><span class="arrow" aria-hidden="true">→</span>
    <a class="rung" style="text-decoration:none" href="/mpm2d-math-tutor-ottawa/"><strong>MPM2D</strong><span>Grade 10 Math</span></a><span class="arrow" aria-hidden="true">→</span>
    <a class="rung" style="text-decoration:none" href="/mcr3u-functions-tutor-ottawa/"><strong>MCR3U</strong><span>Grade 11 Functions</span></a><span class="arrow" aria-hidden="true">→</span>
    <a class="rung" style="text-decoration:none" href="/mhf4u-advanced-functions-tutor-ottawa/"><strong>MHF4U</strong><span>Advanced Functions</span></a><span class="arrow" aria-hidden="true">→</span>
    <a class="rung rung-top" style="text-decoration:none" href="/mcv4u-calculus-vectors-tutor-ottawa/"><strong>MCV4U</strong><span>Calculus &amp; Vectors</span></a>
  </div>
  <p style="margin:0 0 12px;font-weight:700">Science</p>
  <div class="ladder">
    <div class="rung"><strong>SNC1W</strong><span>Grade 9 Science</span></div><span class="arrow" aria-hidden="true">→</span>
    <div class="rung"><strong>SNC2D</strong><span>Grade 10 Science</span></div><span class="arrow" aria-hidden="true">→</span>
    <a class="rung" style="text-decoration:none" href="/sch3u-chemistry-tutor-ottawa/"><strong>SCH3U</strong><span>Grade 11 Chemistry</span></a><span class="arrow" aria-hidden="true">→</span>
    <a class="rung rung-top" style="text-decoration:none" href="/sch4u-chemistry-tutor-ottawa/"><strong>SCH4U</strong><span>Grade 12 Chemistry</span></a>
  </div>
  <a href="/book/" style="font-weight:700">Get help planning your pathway →</a>
</div></section>'''
    body = page_hero([("Home", "/"), ("Courses", None)], "Courses", "Grade 9–12 Math &amp; Science courses",
                     "Every Ontario course code, taught 1-on-1 in Ottawa or online. We fix the basics while we cover the curriculum. Personalized notes and stationery included.",
                     buttons=False, extra=f'<div class="pills anchor-pills">{pills}</div>') + secs + ladder + \
        '<section style="padding:32px 0 64px"><div class="wrap"><p style="margin:0;color:var(--muted)"><strong style="color:var(--ink)">Also offered:</strong> Grade 1–8 tutoring · IELTS &amp; CELPIP coaching for adults</p></div></section>' + cta_band()
    items = [{"@type": "ListItem", "position": i, "url": f'{SITE}/{c["slug"]}/', "name": f'{c["code"]} {c["short"]}'} for i, c in enumerate(COURSES, 1)]
    return shell("Grade 9–12 Math & Science Courses | Tutoring in Ottawa & Online | QueensCoaching",
                 "Every Ontario Grade 9–12 Math and Science course we coach 1-on-1 in Ottawa and online: MTH1W to MCV4U, SCH3U, SCH4U, SBI3U, SBI4U, SPH3U and SPH4U. Book a free assessment.",
                 "/courses/", body, ld({"@context": "https://schema.org", "@type": "ItemList", "itemListElement": items},
                                       crumbs_ld([("Home", "/"), ("Courses", "/courses/")])), active="Courses")


# ---------------- Exam Prep ----------------
def exam_prep():
    body = page_hero([("Home", "/"), ("Exam Prep", None)], "Exam preparation", "Exam prep that starts early, not the week before",
                     "From Ontario unit tests and final exams to EQAO, SAT, AP and IB. 1-on-1 in Ottawa or online, with a unit-by-unit plan and practice tests.") + f'''
<section class="section"><div class="wrap grid-2">
  <div>
    <p class="eyebrow">Ontario final exams</p>
    <h2 class="h2">January &amp; June exams, unit by unit</h2>
    <p style="margin:0 0 12px;font-size:18px;color:var(--ink-soft)">Final exams cover a whole semester. Cramming rarely works, because weak early units make later ones harder. We start with a free assessment to find the weak units, then build a plan that reviews them in order.</p>
    <p style="margin:0;font-size:18px;color:var(--ink-soft)">Exam dates are set by each school, so we plan backwards from your child's own exam schedule.</p>
  </div>
  <ul class="check-list">
    <li><strong>Free assessment</strong> to find weak units</li>
    <li><strong>Written exam plan</strong> within 24 hours</li>
    <li><strong>Past units reviewed</strong> step by step</li>
    <li><strong>Practice tests</strong> in the exam format</li>
    <li><strong>Personalized notes &amp; stationery</strong> included</li>
  </ul>
</div></section>

<section id="exams" class="section alt"><div class="wrap">
  <p class="eyebrow">Tests and exams we prepare for</p>
  <h2 class="h2">Ready for the exams that matter</h2>
  <p class="lead">From Ontario's Grade 9 Math assessment to university entrance tests, here and abroad.</p>
  <div class="grid-wide">
    <article class="card"><span class="tag">Ontario · Grade 9</span><h3 class="course-title">EQAO Grade 9 Math</h3><p>The province-wide MTH1W assessment, written online. Results are part of the final course mark.</p><a class="card-link" href="/mth1w-grade-9-math-tutor-ottawa/">MTH1W details →</a></article>
    <article class="card"><span class="tag">US universities · Grade 11–12</span><h3 class="course-title">SAT</h3><p>Digital SAT Math: strategy plus the math behind it, with timed practice.</p></article>
    <article class="card"><span class="tag">University credit · Grade 10–12</span><h3 class="course-title">AP exams</h3><p>AP Calculus, Chemistry, Biology and Physics, aligned with your school's AP course.</p></article>
  </div>
  <div class="pill-box" style="margin-top:28px"><h3>Also preparing students for</h3><div class="pills">
    <span class="pill">ACT</span><span class="pill">IB Diploma (SL &amp; HL)</span><span class="pill">GCSE / IGCSE</span><span class="pill">A-levels</span><span class="pill">CBSE Class 10 &amp; 12</span><span class="pill">NEET</span><span class="pill">Scottish National 5 &amp; Higher</span><span class="pill">Waterloo math contests (Pascal to Euclid)</span><span class="pill">Avogadro &amp; Chem 13 News</span><span class="pill">Alberta diploma exams</span>
  </div></div>
</div></section>

<section class="section"><div class="wrap">
  <p class="eyebrow">Grade 11 &amp; 12 finals</p>
  <h2 class="h2">The exams families ask us about most</h2>
  <div class="pills" style="margin-top:20px">
    <a class="pill" href="/sch3u-chemistry-tutor-ottawa/"><strong>SCH3U</strong> Grade 11 Chemistry</a><a class="pill" href="/sch4u-chemistry-tutor-ottawa/"><strong>SCH4U</strong> Grade 12 Chemistry</a><a class="pill" href="/mhf4u-advanced-functions-tutor-ottawa/"><strong>MHF4U</strong> Advanced Functions</a><a class="pill" href="/mcv4u-calculus-vectors-tutor-ottawa/"><strong>MCV4U</strong> Calculus &amp; Vectors</a><a class="pill" href="/sbi4u-biology-tutor-ottawa/"><strong>SBI4U</strong> Grade 12 Biology</a><a class="pill" href="/sph4u-physics-tutor-ottawa/"><strong>SPH4U</strong> Grade 12 Physics</a>
  </div>
</div></section>

{cta_band("Start exam prep now, not the week before.", "Book a free assessment and get your exam plan within 24 hours. No obligation.")}'''
    return shell("Exam Prep Tutor in Ottawa & Online: Grade 9–12 Finals, EQAO, SAT, AP | QueensCoaching",
                 "1-on-1 exam preparation in Ottawa and online for Ontario Grade 9–12 Math and Science finals, EQAO Grade 9 Math, SAT, AP and IB. Unit-by-unit plan and practice tests. Book a free assessment.",
                 "/exam-prep/", body, ld(crumbs_ld([("Home", "/"), ("Exam Prep", "/exam-prep/")])), active="Exam Prep")


# ---------------- How It Works ----------------
def how_it_works():
    body = page_hero([("Home", "/"), ("How It Works", None)], "How it works", "We fix the basics while we cover the curriculum.",
                     "Most students struggle in Grade 11 Chemistry or Grade 12 Calculus because of a gap from years earlier, such as fractions, algebra or unit conversions. Here is how we find those gaps and close them.") + f'''
<section class="section"><div class="wrap">
  <p class="eyebrow">Four steps</p>
  <h2 class="h2" style="margin-bottom:28px">From free assessment to confident student</h2>
  {STEPS}
</div></section>

<section class="section alt"><div class="wrap">
  <p class="eyebrow">What we provide</p>
  <h2 class="h2">Everything your child needs, included</h2>
  {PROVIDE}
</div></section>

<section class="section"><div class="wrap grid-2">
  <div>
    <p class="eyebrow">The free assessment</p>
    <h2 class="h2">What happens in the first session</h2>
    <p style="margin:0;font-size:18px;color:var(--ink-soft)">It is free and there is no obligation. Within 24 hours you get a written plan with a winning strategy, and we share pricing based on what your child needs.</p>
  </div>
  <ul class="check-list">
    <li><strong>A short chat</strong> about the course, marks and goals</li>
    <li><strong>A foundations check</strong> of the earlier skills the course depends on</li>
    <li><strong>The exact gaps</strong> holding marks back, explained in plain English</li>
    <li><strong>A written plan</strong> within 24 hours</li>
  </ul>
</div></section>

<section class="section alt"><div class="wrap grid-2">
  <div>
    <p class="eyebrow">In person or online</p>
    <h2 class="h2">Sessions that fit your family</h2>
    <p style="margin:0;font-size:18px;color:var(--ink-soft)">In person across Ottawa, or live online anywhere. Online sessions use 1-on-1 video with a shared whiteboard. Notes are sent digitally, and stationery can be shipped within Canada.</p>
  </div>
  <div class="pills"><a class="pill" href="/areas/">Areas we serve</a><a class="pill" href="/online-chemistry-tutor-ontario/">Online tutoring</a><a class="pill" href="/about-harleen-kaur/">Meet Harleen</a></div>
</div></section>

{cta_band()}'''
    return shell("How Our Tutoring Works: Free Assessment, Plan, 1-on-1 Coaching | QueensCoaching Ottawa",
                 "How QueensCoaching works: a free assessment and foundations check, a written plan within 24 hours, 1-on-1 coaching with personalized notes and stationery, and monthly progress notes.",
                 "/how-it-works/", body, ld(crumbs_ld([("Home", "/"), ("How It Works", "/how-it-works/")])), active="How It Works")


# ---------------- Areas ----------------
def areas():
    cards = "".join(
        f'<article class="card"><span class="tag">Ottawa</span><h3>{e(a["name"])}</h3><p>1-on-1 Grade 9–12 Math and Science tutoring in {e(a["name"])}, in person or online.</p>'
        f'<a class="card-link" href="/{a["slug"]}/">Tutoring in {e(a["name"])} →</a></article>' for a in AREAS)
    cards += ('<article class="card card-feature"><span class="tag tag-gold">Anywhere</span><h3>Online</h3><p>Live 1-on-1 video lessons with a shared whiteboard, in your time zone.</p>'
              '<a class="card-link" href="/online-chemistry-tutor-ontario/">Online tutoring →</a></article>')
    body = page_hero([("Home", "/"), ("Areas", None)], "Areas we serve", "In person across Ottawa, online anywhere",
                     "1-on-1 Grade 9–12 Math and Science coaching in neighbourhoods across Ottawa, plus live online sessions for students across Canada and abroad.") + f'''
<section class="section"><div class="wrap">
  <div class="grid">{cards}</div>
  <div class="pill-box" style="margin-top:28px"><h3>Also serving</h3><div class="pills"><span class="pill">Findlay Creek</span><span class="pill">Riverside South</span><span class="pill">Downtown Ottawa</span></div></div>
</div></section>

<section class="section alt"><div class="wrap">
  <p class="eyebrow">Online worldwide</p>
  <h2 class="h2">Live 1-on-1, in your time zone</h2>
  <div class="pills" style="margin-top:20px"><span class="pill">Across Canada</span><span class="pill">United States</span><span class="pill">United Kingdom</span><span class="pill">India</span><span class="pill">UAE</span><span class="pill">Australia</span></div>
</div></section>

{cta_band()}'''
    return shell("Tutoring Areas in Ottawa: Kanata, Barrhaven, Orléans, Nepean, Stittsville & Online | QueensCoaching",
                 "1-on-1 Grade 9–12 Math and Science tutoring across Ottawa (Kanata, Barrhaven, Orléans, Nepean, Stittsville) and online anywhere. Book a free assessment.",
                 "/areas/", body, ld(crumbs_ld([("Home", "/"), ("Areas", "/areas/")])), active="Areas")


# ---------------- Book ----------------
def book():
    faqs = "".join(f"<details><summary>{e(q)}</summary><p>{e(a)}</p></details>" for q, a in FAQ)
    faq_ld = {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in FAQ]}
    body = page_hero([("Home", "/"), ("Book a Free Assessment", None)], "Free · No obligation", "Book your free assessment",
                     "Tell us about the student and the course. We reply within 24 hours by phone, WhatsApp or email, and send a written plan with a winning strategy within 24 hours of the assessment.",
                     buttons=False) + f'''
<section class="section alt"><div class="wrap narrow">
  <div class="white-card" style="border:1px solid var(--lavender-line);padding:36px">
    <h2 style="margin:0;font-family:var(--serif);font-size:28px;font-weight:600;color:var(--purple)">It takes about 2 minutes</h2>
    <ul>
      <li>Grade, course and the course code or exam</li>
      <li>Your name, email and phone or WhatsApp</li>
      <li>In person (Ottawa) or online, and the best times to reach you</li>
    </ul>
    <div class="btn-row" style="margin-top:8px">
      <a class="btn btn-gold" href="{FORM}" target="_blank" rel="noopener">Open the Booking Form →</a>
      <a class="btn btn-ghost" href="{WA}">Or book on WhatsApp</a>
    </div>
    <p class="small" style="text-align:left">Opens in a new tab · 100% confidential · Reply within 24 hours · Prefer to talk? Call <a href="tel:+16132976844">613.297.6844</a></p>
  </div>
  <div class="review-strip">
    <span class="review-stars" aria-hidden="true">★★★★★</span>
    <p><strong>Already learning with us?</strong> Your honest Google review helps other Ottawa families find the right tutor.</p>
    <div class="btn-row"><a class="btn btn-gold" href="https://g.page/r/CS7iYiJB7OacEBM/review" target="_blank" rel="noopener">Leave a Google review</a><a class="btn btn-ghost" href="https://g.page/r/CS7iYiJB7OacEBM" target="_blank" rel="noopener">Read our Google reviews</a></div>
  </div>
</div></section>

<section id="faq" class="section"><div class="wrap narrow">
  <p class="eyebrow">Questions families ask</p>
  <h2 class="h2" style="margin-bottom:28px">Answers before you book</h2>
  <div class="faq">{faqs}</div>
</div></section>'''
    return shell("Book a Free Assessment | Grade 9–12 Math & Science Tutoring | QueensCoaching Ottawa",
                 "Book a free assessment with QueensCoaching: a foundations check for your child's Grade 9–12 Math or Science course and a written plan within 24 hours. In person in Ottawa or online.",
                 "/book/", body, ld(faq_ld, crumbs_ld([("Home", "/"), ("Book a Free Assessment", "/book/")])), active="Book")


PAGES = {"": home, "courses": courses, "exam-prep": exam_prep, "how-it-works": how_it_works, "areas": areas, "book": book}

if __name__ == "__main__":
    root = sys.argv[1]
    for slug, fn in PAGES.items():
        d = os.path.join(root, slug) if slug else root
        os.makedirs(d, exist_ok=True)
        with open(os.path.join(d, "index.html"), "w", encoding="utf-8") as f:
            f.write(fn())
        print("wrote", slug or "index.html")
