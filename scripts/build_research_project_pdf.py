#!/usr/bin/env python3
"""Build the project handout from its Markdown source.

Install the document-only dependency: python -m pip install reportlab
Run from any directory: python scripts/build_research_project_pdf.py

The source remains coursework/agentic_ai_research_project.md. The layout uses
ReportLab's bundled Vera fonts, so it does not depend on local system fonts.
"""

from html import escape
from pathlib import Path
import re
from urllib.parse import urljoin

import reportlab
from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (
    BaseDocTemplate, Flowable, Frame, KeepTogether, PageBreak, PageTemplate,
    Paragraph, Spacer, Table, TableStyle,
)


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "coursework/agentic_ai_research_project.md"
OUTPUT = SOURCE.with_suffix(".pdf")
REPOSITORY = "https://github.com/erangaeb/agentsway-lab/blob/master/coursework/"
NAVY = colors.HexColor("#142C40")
TEAL = colors.HexColor("#007F7A")
INK = colors.HexColor("#24394A")
MUTED = colors.HexColor("#576B79")
PALE = colors.HexColor("#EDF6F4")
LINE = colors.HexColor("#D7E3E7")
WHITE = colors.white
PAGE_W, PAGE_H = A4
MARGIN = 46
WIDTH = PAGE_W - 2 * MARGIN

FONT_DIR = Path(reportlab.__file__).parent / "fonts"
for name, filename in [
    ("Vera", "Vera.ttf"), ("Vera-Bold", "VeraBd.ttf"),
    ("Vera-Italic", "VeraIt.ttf"), ("Vera-BoldItalic", "VeraBI.ttf"),
]:
    pdfmetrics.registerFont(TTFont(name, str(FONT_DIR / filename)))
pdfmetrics.registerFontFamily(
    "Vera", normal="Vera", bold="Vera-Bold", italic="Vera-Italic",
    boldItalic="Vera-BoldItalic",
)

BODY = ParagraphStyle(
    "Body", fontName="Vera", fontSize=10, leading=15,
    textColor=INK, spaceAfter=9, alignment=TA_LEFT,
)
SMALL = ParagraphStyle("Small", parent=BODY, fontSize=8, leading=11.6, spaceAfter=0)
LABEL = ParagraphStyle(
    "Label", parent=BODY, fontName="Vera-Bold", fontSize=8,
    leading=12, textColor=TEAL, spaceAfter=8,
)
H2 = ParagraphStyle(
    "Heading", parent=BODY, fontName="Vera-Bold", fontSize=15,
    leading=20, textColor=NAVY, spaceBefore=12, spaceAfter=10,
    keepWithNext=True,
)
H3 = ParagraphStyle(
    "Subheading", parent=H2, fontSize=11, leading=16,
    spaceBefore=8, spaceAfter=7,
)
TITLE = ParagraphStyle(
    "Title", parent=H2, fontSize=28, leading=34, spaceBefore=0, spaceAfter=15,
)
BULLET = ParagraphStyle(
    "Bullet", parent=BODY, leftIndent=13, firstLineIndent=0,
    bulletIndent=0, spaceAfter=6,
)


def inline(text):
    """Convert the inline markup used in the brief to ReportLab markup."""
    text = escape(text)
    text = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", text)

    def link(match):
        label, target = match.groups()
        url = urljoin(REPOSITORY, target)
        return f'<a href="{escape(url, quote=True)}" color="#007F7A"><u>{label}</u></a>'

    return re.sub(r"\[([^\]]+)\]\(([^)]+)\)", link, text)


def para(text, style=BODY):
    return Paragraph(inline(text), style)


def blocks(text):
    """Render paragraphs, headings, and lists without rewriting source content."""
    result = []
    for block in re.split(r"\n\s*\n", text.strip()):
        lines = block.splitlines()
        if block.startswith("### "):
            result.append(para(block[4:], H3))
        elif block.startswith("## "):
            result.append(para(block[3:], H2))
        elif all(re.match(r"(?:- |\d+\. )", line) for line in lines):
            for line in lines:
                match = re.match(r"(-|\d+\.) (.*)", line)
                marker, content = match.groups()
                result.append(Paragraph(
                    inline(content), BULLET,
                    bulletText="•" if marker == "-" else marker,
                ))
        else:
            result.append(para(" ".join(lines)))
    return result


def panel(label, content):
    cell = [para(label.upper(), LABEL)] + blocks(content)
    table = Table([[cell]], colWidths=[WIDTH])
    table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), PALE),
        ("LINEBEFORE", (0, 0), (0, -1), 3, TEAL),
        ("LEFTPADDING", (0, 0), (-1, -1), 15),
        ("RIGHTPADDING", (0, 0), (-1, -1), 15),
        ("TOPPADDING", (0, 0), (-1, -1), 12),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 7),
    ]))
    return KeepTogether([Spacer(1, 8), table])


class PageTitle(Flowable):
    def __init__(self, label, title, stage=None):
        super().__init__()
        self.label, self.title, self.stage = label, title, stage
        self.heading = para(title, TITLE)

    def wrap(self, avail_width, avail_height):
        _, title_height = self.heading.wrap(avail_width, avail_height)
        self.title_height = title_height
        self.width, self.height = avail_width, title_height + 45
        return self.width, self.height

    def draw(self):
        c = self.canv
        key = self.label.lower().replace(" ", "-")
        c.bookmarkPage(key)
        c.addOutlineEntry(self.title, key, level=0)
        c.setFillColor(TEAL)
        c.setFont("Vera-Bold", 8)
        c.drawString(0, self.height - 10, self.label.upper())
        if self.stage:
            for i in range(1, 5):
                c.setFillColor(TEAL if i == self.stage else LINE)
                c.roundRect(self.width - 82 + (i - 1) * 22, self.height - 11, 16, 4, 2, fill=1, stroke=0)
        self.heading.drawOn(c, 0, 15)


class Roadmap(Flowable):
    def __init__(self, rows):
        super().__init__()
        self.rows = rows
        self.width, self.height = WIDTH, 276

    def draw(self):
        c = self.canv
        for i, (name, focus, deliverable) in enumerate(self.rows):
            y = self.height - (i + 1) * 69
            c.setFillColor(PALE if i % 2 == 0 else colors.HexColor("#F4F7F9"))
            c.roundRect(0, y + 5, WIDTH, 59, 7, fill=1, stroke=0)
            c.setFillColor(TEAL)
            c.circle(25, y + 35, 13, fill=1, stroke=0)
            c.setFillColor(WHITE)
            c.setFont("Vera-Bold", 9)
            c.drawCentredString(25, y + 32, str(i + 1))
            title = re.sub(r"^\d+\.\s*", "", name)
            p = para(title, ParagraphStyle("RoadmapTitle", parent=H3, spaceBefore=0, spaceAfter=0))
            p.wrap(WIDTH - 64, 30)
            p.drawOn(c, 49, y + 41)
            p = Paragraph(inline(focus) + "<br/>" + inline(deliverable), SMALL)
            _, h = p.wrap(WIDTH - 64, 40)
            p.drawOn(c, 49, y + 39 - h)


def page_chrome(c, doc):
    c.saveState()
    c.setFillColor(NAVY)
    c.rect(0, PAGE_H - 9, PAGE_W, 9, fill=1, stroke=0)
    c.setFont("Vera-Bold", 8)
    c.drawString(MARGIN, PAGE_H - 34, "AGENTSWAY / LAB")
    c.setFont("Vera", 7.5)
    c.setFillColor(MUTED)
    c.drawRightString(PAGE_W - MARGIN, PAGE_H - 34, "MASTER’S COURSE IN AGENTIC AI")
    c.setStrokeColor(LINE)
    c.line(MARGIN, 42, PAGE_W - MARGIN, 42)
    c.setFont("Vera", 7)
    c.drawString(MARGIN, 28, "RESEARCH PROJECT  /  FROM USE CASE TO RESEARCH PAPER")
    c.setFont("Vera-Bold", 8)
    c.setFillColor(TEAL)
    c.drawRightString(PAGE_W - MARGIN, 28, f"{doc.page:02d}")
    c.restoreState()


def main():
    source = SOURCE.read_text(encoding="utf-8")
    parts = re.split(r"^## (.+)$", source, flags=re.M)
    sections = dict(zip(parts[1::2], parts[2::2]))
    objective, table = sections["Objective"].split("| Project stage |", 1)
    rows = [
        [cell.strip() for cell in line.strip().strip("|").split("|")]
        for line in table.splitlines() if re.match(r"\| [1-4]\. ", line)
    ]
    if len(rows) != 4:
        raise ValueError("Expected four project stages in the source overview table.")

    story = [
        Spacer(1, 22),
        para("RESEARCH PROJECT", LABEL),
        para("Agentic AI", ParagraphStyle(
            "CoverTitle", parent=TITLE, fontSize=48, leading=57, spaceAfter=8,
        )),
        Paragraph("From Use Case<br/>to Research Paper", TITLE),
        Spacer(1, 6),
        *blocks(objective),
        Spacer(1, 15),
        para("ONE PROJECT. FOUR CONNECTED STAGES.", LABEL),
        Roadmap(rows),
        Spacer(1, 10),
        para("PROJECT BRIEF  /  AGENTSWAY LAB", LABEL),
        PageBreak(),
        PageTitle("Project foundations", "How to approach the project"),
        para("Learning outcomes", H2),
        *blocks(sections["Learning outcomes"]),
        Spacer(1, 12),
        panel("Use AI throughout the research project", sections["Use AI throughout the research project"]),
    ]

    stage_names = [key for key in sections if key.startswith("Project Stage ")]
    if len(stage_names) != 4:
        raise ValueError("Expected four project stage sections.")
    for index, name in enumerate(stage_names, 1):
        title = name.split(": ", 1)[1]
        text = sections[name].strip()
        if index == 4:
            text, research = text.split("### Research starting points", 1)
            text, sharing = text.split("### Optional next step: share or publish your research", 1)
        task, deliverable = (text.split("### Deliverable", 1) if index < 4 else (text, None))
        story.extend([
            PageBreak(), PageTitle(f"Project stage {index} / 4", title, index),
            *blocks(task.replace("### Task\n", "", 1).strip()),
        ])
        if deliverable:
            story.append(panel("Deliverable", deliverable))

    research, paper_deliverable = research.split("### Deliverable", 1)
    story.extend([
        PageBreak(), PageTitle("Submission & resources", "Bring the project together"),
        panel("Stage 4 deliverable", paper_deliverable),
        para("Final submission", H2),
        *blocks(sections["Final submission"]),
        para("Before submitting", H2),
        *blocks(sections["Before submitting"]),
        PageBreak(), PageTitle("Beyond the course", "Share your research"),
        para("Optional next step: share or publish your research", H2),
        *blocks(sharing),
        para("Research starting points", H2),
        *blocks(research),
    ])

    document = BaseDocTemplate(
        str(OUTPUT), pagesize=A4, title="Agentic AI Research Project: From Use Case to Research Paper",
        author="Agentsway Lab", subject="Master’s course in agentic AI — research project brief",
        leftMargin=MARGIN, rightMargin=MARGIN, topMargin=62, bottomMargin=58,
    )
    frame = Frame(MARGIN, 58, WIDTH, PAGE_H - 120, leftPadding=0,
                  rightPadding=0, topPadding=0, bottomPadding=0)
    document.addPageTemplates(PageTemplate(id="Brief", frames=[frame], onPage=page_chrome))
    document.build(story)
    print(f"Created {OUTPUT.relative_to(ROOT)} ({document.page} pages)")


if __name__ == "__main__":
    main()
