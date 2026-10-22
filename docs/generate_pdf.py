# from reportlab.lib.pagesizes import letter
# from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, HRFlowable
# from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
# from reportlab.lib import colors

# def create_resume_pdf(filename="Amirul_Rosli_Resume.pdf"):
#     doc = SimpleDocTemplate(
#         filename,
#         pagesize=letter,
#         rightMargin=40, leftMargin=40, topMargin=40, bottomMargin=40
#     )
    
#     styles = getSampleStyleSheet()
    
#     # Custom styles
#     title_style = ParagraphStyle(
#         'NameTitle',
#         parent=styles['Heading1'],
#         fontName='Helvetica-Bold',
#         fontSize=18,
#         leading=22,
#         alignment=0,
#         textColor=colors.HexColor('#1A1A1A')
#     )
    
#     contact_style = ParagraphStyle(
#         'ContactInfo',
#         parent=styles['Normal'],
#         fontName='Helvetica',
#         fontSize=9,
#         leading=12,
#         textColor=colors.HexColor('#4A4A4A')
#     )
    
#     section_style = ParagraphStyle(
#         'SectionHeader',
#         parent=styles['Heading2'],
#         fontName='Helvetica-Bold',
#         fontSize=12,
#         leading=16,
#         textColor=colors.HexColor('#0F2C59'),
#         spaceBefore=10,
#         spaceAfter=4
#     )
    
#     body_style = ParagraphStyle(
#         'BodyTextCustom',
#         parent=styles['Normal'],
#         fontName='Helvetica',
#         fontSize=10,
#         leading=14,
#         textColor=colors.HexColor('#2C2C2C')
#     )

#     story = []

#     # Header
#     story.append(Paragraph("MUHAMMAD AMIRUL BIN ROSLI", title_style))
#     story.append(Spacer(1, 3))
#     story.append(Paragraph("Petaling Jaya, Selangor, Malaysia | +60 12-345 6789 | amirul.rosli@email.com | linkedin.com/in/amirul-rosli", contact_style))
#     story.append(Spacer(1, 8))

#     # Education
#     story.append(Paragraph("EDUCATION", section_style))
#     story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor('#0F2C59'), spaceAfter=6))
#     story.append(Paragraph("<b>Universiti Teknologi Malaysia (UTM)</b> &mdash; <i>Skudai, Johor</i>", body_style))
#     story.append(Paragraph("<b>Bachelor of Computer Science (Software Engineering) with Honours</b> | Oct 2022 &ndash; July 2026", body_style))
#     story.append(Paragraph("• <b>CGPA:</b> 3.42 / 4.00", body_style))
#     story.append(Paragraph("• <b>Relevant Coursework:</b> Data Structures & Algorithms, Object-Oriented Programming (Java), Web Application Development, Database Systems, Software Architecture.", body_style))
#     story.append(Spacer(1, 8))

#     # Internship
#     story.append(Paragraph("INTERNSHIP EXPERIENCE", section_style))
#     story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor('#0F2C59'), spaceAfter=6))
#     story.append(Paragraph("<b>IT Trainee Intern</b> &mdash; Nexon Tech Solutions Sdn Bhd, Cyberjaya", body_style))
#     story.append(Paragraph("<i>Feb 2026 &ndash; July 2026</i>", body_style))
#     story.append(Paragraph("• Assisted the software team in maintaining and bug-fixing web application components using HTML, CSS, and JavaScript.", body_style))
#     story.append(Paragraph("• Executed test cases and logged software defect reports using Jira.", body_style))
#     story.append(Paragraph("• Wrote basic SQL queries to assist with backend database maintenance on PostgreSQL.", body_style))
#     story.append(Paragraph("• Participated in weekly development stand-ups and assisted seniors with technical documentation.", body_style))
#     story.append(Spacer(1, 8))

#     # Academic Projects
#     story.append(Paragraph("ACADEMIC PROJECTS", section_style))
#     story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor('#0F2C59'), spaceAfter=6))
#     story.append(Paragraph("<b>Student Event Management System</b> (Final Year Project)", body_style))
#     story.append(Paragraph("• Designed and built a web application for student activity management using PHP, HTML/CSS, and MySQL.", body_style))
#     story.append(Paragraph("• Integrated user role management for student committees and general participants.", body_style))
#     story.append(Spacer(1, 8))

#     # Skills
#     story.append(Paragraph("SKILLS & LANGUAGES", section_style))
#     story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor('#0F2C59'), spaceAfter=6))
#     story.append(Paragraph("• <b>Programming Languages:</b> Java, C++, Python (Basic), PHP, JavaScript", body_style))
#     story.append(Paragraph("• <b>Web & Database:</b> HTML5, CSS3, SQL (MySQL, PostgreSQL)", body_style))
#     story.append(Paragraph("• <b>Developer Tools:</b> Git, GitHub, VS Code, Jira", body_style))
#     story.append(Paragraph("• <b>Languages:</b> Bahasa Melayu (Native), English (Professional)", body_style))

#     doc.build(story)
#     print(f"PDF generated: {filename}")

# if __name__ == "__main__":
#     create_resume_pdf()


from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    HRFlowable,
    KeepTogether,
)

OUTPUT_FILE = "fictional_veteran_resume.pdf"


def create_resume_pdf(filename=OUTPUT_FILE):
    doc = SimpleDocTemplate(
        filename,
        pagesize=letter,
        rightMargin=0.58 * inch,
        leftMargin=0.58 * inch,
        topMargin=0.48 * inch,
        bottomMargin=0.48 * inch,
        title="Veteran Resume",
        author="Resume Tailor V1 Test Data",
    )

    styles = getSampleStyleSheet()

    name_style = ParagraphStyle(
        "CandidateName",
        parent=styles["Title"],
        fontName="Helvetica-Bold",
        fontSize=18,
        leading=22,
        alignment=TA_LEFT,
        textColor=colors.HexColor("#1A1A1A"),
        spaceAfter=3,
    )

    contact_style = ParagraphStyle(
        "Contact",
        parent=styles["Normal"],
        fontName="Helvetica",
        fontSize=8.5,
        leading=11,
        textColor=colors.HexColor("#444444"),
        spaceAfter=7,
    )

    section_style = ParagraphStyle(
        "Section",
        parent=styles["Heading2"],
        fontName="Helvetica-Bold",
        fontSize=11,
        leading=14,
        textColor=colors.HexColor("#0F2C59"),
        spaceBefore=7,
        spaceAfter=3,
        keepWithNext=True,
    )

    body_style = ParagraphStyle(
        "ResumeBody",
        parent=styles["BodyText"],
        fontName="Helvetica",
        fontSize=9,
        leading=11.5,
        textColor=colors.HexColor("#292929"),
        spaceAfter=2,
    )

    bullet_style = ParagraphStyle(
        "ResumeBullet",
        parent=body_style,
        leftIndent=13,
        firstLineIndent=-8,
        spaceAfter=1.5,
    )

    story = []

    def section(title):
        story.append(Paragraph(title.upper(), section_style))
        story.append(
            HRFlowable(
                width="100%",
                thickness=0.8,
                color=colors.HexColor("#0F2C59"),
                spaceAfter=4,
            )
        )

    def bullet(text):
        story.append(Paragraph(f"&bull; {text}", bullet_style))

    # All identity and employment information below is fictional test data.
    story.append(Paragraph("DANIEL HAKIM BIN SALLEH", name_style))
    story.append(
        Paragraph(
            " Petaling Jaya, Selangor, Malaysia"
            " | veteran.candidate@example.com"
            " | 010-000 0000"
            " | linkedin.com/in/veteran-candidate",
            contact_style,
        )
    )

    section("Professional Summary")
    story.append(
        Paragraph(
            "Former military logistics and operations specialist transitioning "
            "to an entry-level software development role. Experienced in "
            "equipment records, procedural documentation, troubleshooting, "
            "team coordination, and routine reporting. Has completed introductory "
            "programming coursework and a small personal Python project. "
            "Seeking to build on these foundations in a junior software role.",
            body_style,
        )
    )

    section("Technical Training")
    story.append(
        Paragraph(
            "<b>Introductory Software Development Certificate</b> — "
            "Community Technology Programme",
            body_style,
        )
    )
    story.append(
        Paragraph("Jan 2025 – Apr 2025", body_style)
    )
    bullet(
        "Completed introductory exercises in Python, variables, conditional "
        "logic, loops, functions, and basic error handling."
    )
    bullet(
        "Practised HTML and CSS fundamentals by building a simple static "
        "web page as a course exercise."
    )
    bullet(
        "Used Git for basic version control exercises, including commits "
        "and maintaining a small local repository."
    )

    section("Professional Experience")
    story.append(
        Paragraph(
            "<b>Logistics and Operations Specialist</b> — "
            "Malaysian Armed Forces Unit",
            body_style,
        )
    )
    story.append(Paragraph("Jun 2016 – Dec 2024", body_style))
    bullet(
        "Maintained equipment inventory records and updated spreadsheet "
        "trackers to support routine stock checks and handovers."
    )
    bullet(
        "Investigated discrepancies in equipment records and followed "
        "established procedures to resolve or escalate issues."
    )
    bullet(
        "Performed first-line checks on assigned communications and "
        "office equipment, documenting faults for specialist support."
    )
    bullet(
        "Prepared daily activity summaries, equipment status reports, "
        "and handover notes for supervisors and incoming personnel."
    )
    bullet(
        "Coordinated tasks across a small team during scheduled operations "
        "and helped new team members learn standard procedures."
    )
    bullet(
        "Followed access-control, information-handling, safety, and "
        "record-keeping procedures in a structured working environment."
    )

    section("Personal Project")
    story.append(
        Paragraph(
            "<b>Personal Expense Tracker</b> — Learning Project",
            body_style,
        )
    )
    story.append(Paragraph("Mar 2025 – Apr 2025", body_style))
    bullet(
        "Created a small command-line Python program to record expense "
        "descriptions and amounts entered by a user."
    )
    bullet(
        "Added basic input checks and calculated a running total for "
        "the entered expenses."
    )
    bullet(
        "Saved and loaded records using a local text file; tested the "
        "program manually with sample entries."
    )

    section("Skills")
    bullet(
        "<b>Programming:</b> Python fundamentals; introductory HTML and CSS."
    )
    bullet(
        "<b>Tools:</b> Git basics, spreadsheets, text editors, equipment "
        "tracking records, and routine reporting."
    )
    bullet(
        "<b>Work practices:</b> Documentation, troubleshooting, procedural "
        "compliance, teamwork, task coordination, and handovers."
    )

    section("Education")
    story.append(
        Paragraph(
            "<b>Diploma in Logistics Management</b> — "
            "Institute of Technical Studies",
            body_style,
        )
    )
    story.append(Paragraph("2013 – 2016", body_style))
    bullet(
        "Coursework included inventory control, operations planning, "
        "workplace communication, and basic computer applications."
    )

    section("Languages")
    bullet("Bahasa Melayu — Native.")
    bullet("English — Working proficiency.")

    # story.append(Spacer(1, 5))
    # story.append(
    #     Paragraph(
    #         "<i>TEST DATA: This resume, its candidate, employer, education "
    #         "provider, dates, and contact details are fictional and were "
    #         "created solely to test a resume-tailoring workflow.</i>",
    #         ParagraphStyle(
    #             "TestNotice",
    #             parent=body_style,
    #             fontSize=7.5,
    #             leading=9,
    #             textColor=colors.HexColor("#666666"),
    #         ),
    #     )
    # )

    doc.build(story)
    print(f"Generated: {filename}")


if __name__ == "__main__":
    create_resume_pdf()
