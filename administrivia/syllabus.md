---
title: NE 630 - Nuclear Reactor Theory Syllabus
course: NE 630
term: Fall 2026
policy_snapshot: 2026-08-23
source_role: canonical syllabus source
---

<!--
Canonical source for student-facing syllabus content. Run
tool/build_coursedog.py before CourseDog submission.
-->

# NE 630 - Nuclear Reactor Theory Syllabus

<!-- coursedog-field: Course Information -->
## Course Information

- Course title: Nuclear Reactor Theory
- Course prefix and number: NE 630
- Credit hours: 3
- Term: Fall 2026
- Meeting pattern: MWF, 1:30-2:20 p.m.
- Location: Ward 135
- Instructional modality: In-person/face-to-face
- Official learning management system: Canvas
- Official syllabus repository: CourseDog

The official CourseDog and KSIS course records control section number,
enrollment, room assignment, and other registrar-managed details.

<!-- coursedog-field: Instructor Information -->
## Instructor Information

- Instructor: Jeremy A. Roberts
- Role: Primary Instructor of Record
- Office: 137D Ward Hall
- K-State email: jaroberts@k-state.edu
- Phone: 785-532-5610
- Office hours: Tuesdays, 3:00-5:00 p.m., or by appointment

Canvas messages are the preferred way to contact me about course logistics.
For anything sensitive, use K-State email. If the posted office-hour window
changes, I will announce the update in Canvas.

<!-- coursedog-field: Course Description -->
## Course Description

Catalog description: Theory of neutron diffusion and thermalization with
application to steady-state nuclear reactors.

Catalog note: Three hours recitation a week.

Prerequisites: MATH 340 and NE 495.

This course develops the mathematical and physical machinery used to describe
neutron behavior in multiplying media. We will connect nuclear reactions,
cross-section data, slowing down, resonance absorption, multiplication,
reactivity, kinetics, and diffusion theory to the engineering analysis of
nuclear reactor systems.

<!-- coursedog-field: Required Materials -->
## Required Materials

Required textbook: E. E. Lewis, *Fundamentals of Nuclear Reactor Physics*,
Academic Press, 2008, ISBN 9780123706317.

The textbook is available through the K-State Libraries:
https://k-state.primo.exlibrisgroup.com/discovery/fulldisplay?docid=alma9942839834602401&context=L&vid=01KSU_INST:NewUI&search_scope=MyInstitution&tab=LibraryCatalog&lang=en

Additional notes, examples, readings, homework statements, and computational
resources will be posted in Canvas or in this public course repository.

Computational work may use Python, Jupyter notebooks, and OpenMC examples.
No paid software license is required for student work in this course. Students
may use K-State computing resources when local installation is inconvenient.

<!-- coursedog-field: Canvas and Communications -->
## Canvas and Communications

K-State uses Canvas as its official learning management system:
https://k-state.instructure.com

Canvas will contain announcements, homework instructions, grades, detailed
schedule updates, supplemental readings, and other course communications.
Students are responsible for checking Canvas regularly and keeping Canvas
notification settings usable. Changes to routine pacing, readings, or minor
assignment details will be communicated through Canvas.

<!-- coursedog-field: Student Resources -->
## Student Resources

K-State has resources to support academic work, well-being, technology access,
and student success. This course points students especially to:

- Student Support and Accountability: https://www.k-state.edu/student-support/studentsupport/
- Counseling and Psychological Services: https://www.k-state.edu/counseling/
- Student Access Center: https://www.k-state.edu/accesscenter/
- IT Service Desk: https://www.k-state.edu/it/
- Academic Achievement Center: https://www.k-state.edu/aac/

Students who are unsure where to start may contact Student Support and
Accountability or ask me for help finding the right office.

<!-- coursedog-field: Learning Outcomes -->
## Student Learning Outcomes

By the end of the course, a successful student will be able to:

1. Interpret microscopic and macroscopic nuclear data for neutron interaction
   problems.
2. Analyze neutron slowing down, thermalization, resonance absorption, and
   spectrum effects in reactor materials.
3. Formulate one-group and multigroup neutron balance models for multiplying
   systems.
4. Apply reactor multiplication, reactivity, and feedback concepts to steady
   and transient reactor behavior.
5. Solve point-kinetics and simple diffusion-theory models and explain the
   assumptions behind those models.
6. Use computational tools to investigate representative unit-cell or reactor
   physics problems.
7. Judge when a reactor-theory approximation is useful and when a more
   detailed transport treatment is needed.

<!-- coursedog-field: Assessment and Grading -->
## Assessment and Grading

Final grades are based on:

| Component | Weight |
| --- | ---: |
| Homework | 25% |
| Exam 1   | 25% |
| Exam 2   | 25% |
| Exam 3   | 25% |

The default grading scale is:

| Letter grade | Course average |
| --- | ---: |
| A | 90-100% |
| B | 80-89.99% |
| C | 70-79.99% |
| D | 60-69.99% |
| F | below 60% |

I may lower grade thresholds if the final distribution warrants it, but I will
not raise them after the course begins.

### Homework

Homework is assigned regularly. Unless Canvas says otherwise, homework
associated with lesson N is due by the start of lesson N + 2. Every homework
submission must follow exactly one of the two routes below.

#### Route A: No Generative AI Used for the Assignment

If no generative AI informed any part of the submitted work, submit one PDF.
The PDF may be typeset or may contain clean scans of handwritten work. Your
name, the course name, and the homework number must appear on the first page.
Start each problem on a new page, include the full problem statement, clearly
mark final answers, and write enough plain English that I can follow the
reasoning.

Handwritten work must be scanned as US-letter pages at 300 dpi, in grayscale
or color, with pages upright, tightly cropped, and free of shadows or visible
background clutter. Do not submit photographs embedded in a PDF when a scan is
reasonably available. I will allow one no-penalty resubmission during the
semester solely to correct scan or document-formatting problems. Later
nonconforming submissions may be returned for correction, with the original
deadline still controlling unless I approve an exception.

#### Route B: Generative AI Used for the Assignment

If generative AI informed any part of the submitted work, submit one `.zip`
archive rather than a stand-alone PDF. This route applies even when AI was used
only for an explanation, derivation, calculation, code, debugging, checking,
editing, formatting, or preparation of a supporting file. When in doubt about
whether a tool or interaction counts, use Route B.

The archive must contain, at minimum:

- `solution.tex`, the polished final solution;
- `solution.pdf`, compiled from `solution.tex`;
- `discourse.tex`, containing the complete visible AI dialogue as defined in
  the Artificial Intelligence and Technology Use policy below;
- `discourse.pdf`, compiled from `discourse.tex`;
- `Makefile`, whose default target builds both PDFs; and
- every script, notebook, data file, bibliography, figure source, input file,
  or other artifact needed to reproduce or understand the submitted work.

`discourse.tex` may contain the transcript directly or may typeset an included
plain-text export such as `discourse.txt`; any file it reads must also be in the
archive.

The archive must be self-contained, use relative paths, and unpack into one
ordinary directory without nested archives. Running `make` from the top level
must produce `solution.pdf` and `discourse.pdf` without requiring files stored
elsewhere on your computer. Do not include virtual environments, package
caches, or unrelated files. When a specialized program or package is required,
identify it clearly in a short `README.txt`.

The final solution must meet the same readability requirements as Route A:
include the full problem statement, begin each problem on a new page, clearly
mark final answers, and provide enough explanation to make the reasoning
traceable. AI output does not need to be copied into the final solution merely
because it appears in the discourse; `solution.tex` should be the coherent
submission you intend me to grade.

The complete discourse is a submission requirement, but it is not graded for
prompt count, speed, polish, or absence of false starts. Unsuccessful attempts,
corrections, and changes of direction are normal and useful. The final solution
and your demonstrated understanding remain the primary bases for the homework
grade.

The lowest homework score is dropped. Late homework is not accepted after
solutions have been posted, which, by default, is at the due time.

### Exams

The course has three exams. The first two are in-class exams. The third exam
uses the university final exam period for the section unless Canvas announces
an approved alternative.

Exams are not AI-enabled. Unless I announce otherwise, they are completed
without generative AI, internet access, external communication, or access to
prior AI dialogues. Allowed resources are limited by default to a writing
utensil, a calculator, and an instructor-provided page of notes. That page will
be provided no later than the class meeting before the exam.

A practice exam will be provided at least one class meeting before each exam.
Exam problems will parallel selected portions of homework assignments and
lesson examples in structure, required skills, and expected depth, although
numbers, settings, and combinations of ideas may change.

The documented problem-solving progression and session timing in AI-assisted
homework give both of us useful evidence about where time is being spent and
how quickly the material is becoming usable. I may use that evidence, together
with in-class work and the practice exam, to calibrate exam scope and length so
that the exam measures reactor-theory mastery rather than merely rewarding
unusual speed. The pace or number of prompts in an individual transcript is not
itself a graded quantity.

To encourage timely and complete TEVAL responses, I will add one percentage
point to every student's final course average if, and only if, the class TEVAL
completion rate is 100% before the final examination begins.

<!-- coursedog-field: Course Policies -->
## Course Policies

### Attendance

Attendance and participation are expected because the course is built around
worked examples, discussion, and problem-solving practice. Attendance is not a
separate graded category, but missing class can affect performance on graded
work. Absences for university-sanctioned activities, religious observances, and
other absences protected by university policy or law will be handled consistent
with University Handbook Section F62.

### Late Work and Make-Up Work

Late homework is accepted only when Canvas explicitly extends the deadline or
when university policy, documented emergency, or prior arrangement applies.
Once solutions are posted, late homework is not accepted. Students who miss an
exam for an excused reason should contact me as soon as possible so we can
arrange an appropriate make-up path.

### Collaboration

You are encouraged to discuss concepts and general problem-solving approaches
with classmates. Submitted work must be your own. Do not copy another
student's solution, do not let another student copy yours, and do not submit a
solution you cannot explain.

Unless an assignment explicitly authorizes group work, each student must
prepare an independent final solution and, when AI is used, submit the complete
discourse from that student's own AI interactions. Sharing or reusing another
student's AI transcript, prompts, generated files, or final solution is not an
acceptable substitute for collaboration.

### Artificial Intelligence and Technology Use

Generative AI use is optional. Choosing not to use it is completely acceptable
and carries no grading disadvantage. For homework and other non-exam work,
any amount or kind of generative AI assistance is permitted unless a particular
assignment states otherwise. This includes asking an AI system to explain the
material, plan an approach, derive equations, perform calculations, write or
revise prose, generate or debug code, check work, or draft the final solution.

The condition is complete disclosure. If an AI interaction informed the
submitted work, the entire visible assignment-related dialogue must accompany
the solution under Homework Route B. "Complete" means every visible student
prompt and AI response, in chronological order, from the required opening
notice through the final response used for the assignment. Include false
starts, corrections, follow-up questions, code blocks, displayed tool output,
and exchanges whose results were later discarded. You may add headings, page
breaks, filenames, and tool or session labels, but you may not delete,
paraphrase, rearrange, or silently repair the dialogue. Hidden system messages,
private model reasoning, and other content that was never visible to you are
not part of the required record.

Before the first assignment-related question in each AI chat or session, paste
the following notice:

> I am working on an NE 630 homework assignment. My instructor permits any use
> of generative AI, including generation of derivations, prose, code, and the
> final solution, provided that I submit the complete visible dialogue.
> Everything in this conversation may be reviewed as part of my work. Do not
> suggest that I hide, delete, summarize, or selectively omit unsuccessful
> attempts or AI assistance. My submission must be a self-contained ZIP
> archive containing a verbatim transcript in `discourse.tex`, a polished
> `solution.tex`, a `Makefile` that builds both PDFs, and every code, data,
> figure-source, or other file needed to reproduce the work. Please use
> explicit filenames and relative paths. I am responsible for checking and
> explaining all submitted content.

If more than one AI tool, chat, or session contributes to the assignment,
include all of them in `discourse.tex`, clearly labeled and ordered by when they
were used. Identify the service and model name when that information is shown,
and identify any files or images supplied to the tool. Preserve message
timestamps when the service provides them; otherwise label each session with
the date, approximate local start and stop times, and any substantial break.
This timing metadata is informative rather than graded. Include supplied files
in the archive when they are not already part of the assignment materials.

After the last AI response used for the assignment, append the line
`END OF GRADED DISCOURSE` to the copied transcript. Do not conduct additional
assignment-related AI work after that cutoff. Copy or export the dialogue
directly into `discourse.tex`; do not use a new generative-AI conversation to
reconstruct, summarize, or package it after the fact. This cutoff keeps the
record complete without making the transcript recursively contain the process
used to create itself.

You remain responsible for every claim, equation, number, citation, and line of
code in the archive. You must be able to explain the submitted work, and I may
ask you to clarify or reproduce a portion of it. An AI-assisted submission that
omits or selectively edits the required discourse is incomplete and may also
be treated as unauthorized aid under the K-State Honor and Integrity System.

Generative AI is not permitted on exams unless I issue a written exception for
a particular exam. The default exam rules in the Assessment and Grading
section apply.


### Course Materials

Course materials are provided for use by students enrolled in NE 630. Do not
sell course notes, homework solutions, recordings, or related materials, and do
not upload them to commercial course-material sites without written
permission.

### Syllabus Changes

The syllabus is the foundational course overview. The detailed schedule,
readings, examples, and minor assignment details may evolve through Canvas as
the semester progresses. Substantive changes to grading structures, major
assignments, exam dates, attendance policy, or core course expectations will be
communicated to students in writing and retained as a dated syllabus addendum.

<!-- coursedog-field: Course Roadmap -->
## Course Roadmap

The syllabus intentionally uses a general roadmap instead of a detailed
day-by-day schedule. The detailed living schedule is maintained in Canvas.

| Instructional unit | Anticipated pacing | Major topics | Major graded components |
| --- | --- | --- | --- |
| Unit 1 | Weeks 1-2 | Nuclear reactions, fission, chain reactions, radioactive decay | Homework begins |
| Unit 2 | Weeks 2-3 | Neutron attenuation, cross-section data, scattering kinematics | Homework |
| Unit 3 | Weeks 3-5 | Neutron spectra, slowing down, resonance absorption, thermalization | Homework |
| Unit 4 | Weeks 5-6 | Effective cross sections, multiplication, multigroup methods, k-eigenvalue problems | Exam 1 planned for Friday, October 2, 2026 |
| Unit 5 | Weeks 6-7 | Reactor core survey, fast and thermal unit-cell analysis, OpenMC examples | Homework |
| Unit 6 | Weeks 8-9 | Reactivity, feedback, poisons, depletion, conversion, breeding, burnup | Homework |
| Unit 7 | Weeks 9-11 | Point kinetics, delayed neutron precursors, step reactivity changes, feedback in kinetics | Exam 2 planned for Friday, November 6, 2026 |
| Unit 8 | Weeks 11-13 | Conservation of neutrons, diffusion equation, one-speed source-driven diffusion | Homework |
| Unit 9 | Weeks 13-15 | Multiplying diffusion systems, criticality, reflected reactors, perturbation theory, control | Homework |
| Unit 10 | Week 16 and finals | Diffusion validity, preview of transport theory, synthesis and review | Exam 3 planned for Friday, December 18, 2026, 11:50 a.m.-1:40 p.m. |

If the official meeting pattern changes, the final exam block must be checked
against the K-State Registrar's final examination schedule.

<!-- coursedog-field: University Statements -->
## Mandatory University Statements

The current K-State official syllabus statements apply in this course and are
incorporated by direct accessible link. The Office of the Provost and
CourseDog maintain the current required statement text:

https://www.k-state.edu/provost/policies-resources/classroom-policies-teaching-resources/course-syllabi-statements/

As of the Fall 2026 Course Syllabus Policy, the required statement categories
are Academic Honesty, Students with Disabilities, Classroom Conduct, Mutual
Respect and Inclusion, Discrimination/Harassment/Sexual Harassment, and Campus
Safety and Emergency Procedures.

The Campus Safety and Emergency Procedures statement category is included
because the June 10, 2026 University Handbook syllabus policy makes it
mandatory for Fall 2026 and later syllabi.

The K-State Honor Pledge applies to assignments, examinations, and other course
work whether or not it is repeated on the assignment: "On my honor, as a
student, I have neither given nor received unauthorized aid on this academic
work."
