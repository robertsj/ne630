# NE 630 - Nuclear Reactor Theory

This document provides the syllabus and course policies.
Please read it carefully.

The rest of this repository contains notes, examples, and other resources
for NE 630 - Nuclear Reactor Theory,
taught at Kansas State University.  All materials were developed by
Jeremy Roberts.

## Course Details

### Time and Place

1:30pm--2:20pm MWF Ward 135
 
### Instructor
 - Jeremy Roberts
 - 137D Ward Hall
 - Office Hours: T 3-5pm or by appointment; see my [calendar](https://calendar.google.com/calendar/embed?src=j.alyn.roberts%40gmail.com&ctz=America/Chicago) and shoot me an email through Canvas. 


## Course Description 

From the catalog: Theory of neutron diffusion and thermalization with application to steady-state nuclear reactors.
For a brief introduction to this course, head to Course Introduction under the Administriva module.
 
## Textbook

E. E. Lewis, *Fundamentals of Nuclear Reactor Physics*, Academic Press, 2008. 

This book is available online through the library.  You may use [this link](https://k-state.primo.exlibrisgroup.com/discovery/fulldisplay?docid=alma9942839834602401&context=L&vid=01KSU_INST:NewUI&search_scope=MyInstitution&tab=LibraryCatalog&lang=en) to access it (credentials required).
 
## Prerequisites

NE 495 and MATH 340.  Though not required, having had ME 400 or some other programming experience should be useful in this course.

## Lectures 

Lectures, I hope, will be informal yet provide useful interpretation of the readings and demonstration of the associated problem-solving techniques.  In other words, verbal Cliff's notes and worked examples.  However, I'm only one of the 20+ of us, so y'all need to participate to make the time most valuable.  That means doing the reading (including this syllabus;  the reading for our first lecture is Sections 1.1--1.3 of the textbook.)

Although I do not plan to record our live sessions this term, I've provided a link to a YouTube channel with videos recorded during the Fall 2023 semester.  My plan is to follow the same lesson schedule and present the same material, but some details will surely differ.  

## Assessment

Assessment for the course is based on the following breakdown:

- homeworks (each lesson; total 40%)
- exams (3, each worth 20%)

A small number of homework problems are assigned for each lesson.  Unless otherwise stated, homework for lesson N is due by the start of lesson N + 2.  No late homework will be accepted once solutions are posted.  Because life happens, the lowest homework is dropped, i.e., you can miss one without penalty.  Homework submissions must be submitted as a single PDF file.  Your name, the course name, and the homework number should be in the upper right corner of the first page.  Each problem should start on a new page, and the full problem statement should be included.  Final answers should be circled, and there should be no crossed out or otherwise extraneous work.  Use plain English to explain what you are doing as is applicable. I have no personal preference for the type of paper you use, but experience suggests engineering paper yields cleaner work.  Note, you may feel free to typeset your solutions with Word, LaTeX, or other tools.


## Schedule

|  #            | Date          | Topics                                                         | Reading |
|---------------|---------------|----------------------------------------------------------------|---------|
|	1	|	M 08/19	|	Nuclear reactions. 	|	FNRP 1.1-1.3	|	
|	2	|	W 08/21	|	Nuclear fission and chain reactions.	|	FNRP 1.4-1.5	|	
|	3	|	F 08/23	|	Radioactive decay.	|	FNRP 1.6-1.7	|	
|	4	|	M 08/26	|	Neutron attenuation.	|	FNRP 2.1-2.2	|	
|	5	|	W 08/28	|	Using cross-section data.	|	FNRP 2.3-2.4. BNL Sigma.	|	
|	6	|	F 08/30	|	Understanding cross-section data.	|	FNRP 2.3-2.4 (again)	|	
|	 	|		|	HOLIDAY	|		|	
|	7	|	W 09/04	|	Scattering kinematics	|	FNRP 2.5	|	
|	8	|	F 09/06	|	"Eta" as the simplest "k". Moderators.	|	FNRP 3.1-3.3	|	
|	9	|	M 09/09	|	The fast spectrum. Slowing down and 1/E.	|	FNRP 3.4.	|	
|	10	|	W 09/11	|	Slowing down with rsonance absorption and NR.	|	FNRP 3.4. Supplement on NR/WR.	|	
|	11	|	F 09/13	|	Thermal spectrum. 	|	FNRP 3.4.	|	
|	12	|	M 09/16	|	Effective cross sections and k.	|	FNRP 3.5-3.6.	|	
|	13	|	W 09/18	|	Multigroup method and the two-group equations.	|	Supplement on MG method.	|	
|	14	|	F 09/20	|	The k-eigenvalue problem in 2 and more groups.	|	Supplement on MG method.	|	
|	15	|	M 09/23	|	A survey of power reactor cores.	|	FNRP 4.1-4.2. 	|	
|	16	|	W 09/25	|	Fast reactor unit cell analysis.	|	FNRP 4.3.	|	
|		|	F 09/27	|	EXAM 1	|	Covers lessons 1--14	|	
|	17	|	M 09/30	|	Thermal reactor unit cell analysis.  Four factors.  	|	FNRP 4.4.  	|	
|	18	|	W 10/02	|	Modeling unit-cells in OpenMC I.	|	Supplement on OpenMC on Beocat.	|	
|	19	|	F 10/04	|	Unit-cell design considerations: SFR enrichment and PWR P/D.		FNRP 4.4 (especially last subsection).	|	
|	20	|	M 10/07	|	Reactivity. 	|	FNRP 9.1-9.4.	|	Depletion and kinetics represent models that 
|	21	|	W 10/09	|	Reactivity feedback. 	|	FNRP 9.1-9.4.	|	require the solution of systems of first-order equations
|		|	F 10/11	|	WILDCAT PAUSE DAY	|		|	Spatial will require 2nd order BVPs.
|	22	|	M 10/14	|	Long-term effects I. Xenon-135 and Samarium-149.	|	FNRP 10.1-10.3	|	Solving systems of equations.
|	23	|	W 10/16	|	Long-term effects II. Depletion, conversion and breeding.	|	FNRP 10.4.	|	Introduce burnup.
|	24	|	F 10/18	|	Long-term effects III. Linear-reactivity model.	|	FNRP 10.5. Supplement.	|	More informational. Burnup credit, other topics.
|	25	|	M 10/21	|	Kinetics I. Point kinetics without multiplication. Lifetime.	|	FNRP 5.1-5.2(through Eq. 5.8)	|	Fun and useful applications.
|	26	|	W 10/23	|	Kinetics II. PK with multiplication (with and without source)	|	FNRP 5.2(rest)-5.3	|	
|	27	|	F 10/25	|	Kinetics III.  PKE with precursors.  In-hour.	|	FNRP 5.4	|	
|	28	|	M 10/28	|	Kinetics IV.  Step changes in reactivities.	|	FNRP 5.5	|	
|	29	|	W 10/30	|	Kinetics V. Step changes with reactivity feedback.	|	FNRP 5.6.  Supplements (if needed)	|	
|		|	F 11/01	|	EXAM 2 	|	Covers lessons 15--28	|	
|	30	|	M 11/04	|	REVIEW	|		|	
|	31	|	W 11/06	|	Conservation of neutrons and the diffusion equation.	|	FNRP 6.1--2.	|	
|	32	|	F 11/08	|	One-speed, single-region, source-driven diffusion in slabs.	|	FNRP 6.3	|	
|	33	|	M 11/11	|	One-speed, multi-region, source-driven diffusion in slabs.	|	FNRP 6.4	|	
|	34	|	W 11/13	|	One-speed diffusion with multiplication.	|	FNRP 6.5 and 6.7	|	
|	35	|	F 11/15	|	Criticality in slabs and cylinders.	|	FNRP 7.1--7.3	|	
|	36	|	M 11/18	|	Two-group criticality models.	|	DH 7.III.B-C, FNRP 7.4	|	
|	37	|	W 11/20	|	Reflected reactors	|	FNRP 7.5	|	
|	38	|	F 11/22	|	Perturbation theory and control.	|	FNRP 7.6	|	
|	X	|	M 11/25	|	HOLIDAY	|		|	
|	X	|	W 11/27	|	HOLIDAY	|		|	
|	X	|	F 11/29	|	HOLIDAY	|		|	
|	39	|	M 12/02	|	Testing when diffusion is "good enough"	|	N/A	|	
|	40	|	W 12/04	|	A tast of neutron transport theory	|		|	
|	41	|	F 12/06	|	REVIEW	|		|	
|		|	W 12/11	|	FINAL EXAM - 2 hours, Open-Book/Note 12:35 - 1:30 pm	|		|	

## Mandatory Statements


### Statement Regarding Academic Honesty

Kansas State University has an Honor and Integrity System based on personal integrity, which is presumed to be sufficient assurance that, in academic matters, one's work is performed honestly and without unauthorized assistance. Undergraduate and graduate students, by registration, acknowledge the jurisdiction of the Honor and Integrity System. The policies and procedures of the Honor and Integrity System apply to all full and part-time students enrolled in undergraduate and graduate courses on-campus, off-campus, and via distance learning. A component vital to the Honor and Integrity System is the inclusion of the Honor Pledge which applies to all assignments, examinations, or other course work undertaken by students. The Honor Pledge is implied, whether or not it is stated: "On my honor, as a student, I have neither given nor received unauthorized aid on this academic work." A grade of XF can result from a breach of academic honesty. The F indicates failure in the course; the X indicates the reason is an Honor Pledge violation.


### Statement Regarding Students with Disabilities

At K-State it is important that every student has access to course content and the means to demonstrate course mastery. Students with disabilities may benefit from services including accommodations provided by the Student Access Center. Disabilities can include physical, learning, executive functions, and mental health. You may register at the Student Access Center or to learn more contact:  

```
Manhattan/Olathe/Global Campus – Student Access Center  
accesscenter@k-state.edu
785-532-6441    

K-State Salina Campus – Julie Rowe; Student Success Coordinator
jarowe@k-state.edu
785-820-7908    
```

Students already registered with the Student Access Center please request your Letters of Accommodation early in the semester to provide adequate time to arrange your approved academic accommodations. Once SAC approves your Letter of Accommodation it will be e-mailed to you, and your instructor(s) for this course.  Please follow up with your instructor to discuss how best to implement the approved accommodations. 

### Statement Defining Expectations for Classroom Conduct

All student activities in the University, including this course, are governed by the Student Judicial Conduct Code as outlined in the Student Governing Association By Laws, Article V, Section 3, number 2. Students who engage in behavior that disrupts the learning environment may be asked to leave the class.


### Statement on Mutual Respect and Inclusion in K-State Teaching and Learning Spaces

At K-State, faculty and staff are committed to creating and maintaining an inclusive and supportive learning environment for students from diverse backgrounds and perspectives. K-State courses, labs, and other virtual and physical learning spaces promote equitable opportunity to learn, participate, contribute, and succeed, regardless of age, race, color, ethnicity, nationality, genetic information, ancestry, disability, socioeconomic status, military or veteran status, immigration status, Indigenous identity, gender identity, gender expression, sexuality, religion, culture, as well as other social identities.

Faculty and staff are committed to promoting equity and believe the success of an inclusive learning environment relies on the participation, support, and understanding of all students. Students are encouraged to share their views and lived experiences as they relate to the course or their course experience, while recognizing they are doing so in a learning environment in which all are expected to engage with respect to honor the rights, safety, and dignity of others in keeping with the K-State Principles of Community. 

If you feel uncomfortable because of comments or behavior encountered in this class, you may bring it to the attention of your instructor, advisors, and/or mentors. If you have questions about how to proceed with a confidential process to resolve concerns, please contact the Student Ombudsperson Office. Violations of the student code of conduct can be reported using the Code of Conduct Reporting Form. You can also report discrimination, harassment or sexual harassment, if needed.

### Statement Regarding Discrimination, Harassment, and Sexual Harassment

Kansas State University is committed to maintaining academic, housing, and work environments that are free of discrimination, harassment, and sexual harassment. Instructors support the University’s commitment by creating a safe learning environment during this course, free of conduct that would interfere with your academic opportunities. Instructors also have a duty to report any behavior they become aware of that potentially violates the University’s policy prohibiting discrimination, harassment, and sexual harassment, as outlined by PPM 3010.  

If a student is subjected to discrimination, harassment, or sexual harassment, they are encouraged to make a non-confidential report to the University’s Office for Institutional Equity (OIE) using the online reporting form. Incident disclosure is not required to receive resources at K-State. Reports that include domestic and dating violence, sexual assault, or stalking, should be considered for reporting by the complainant to the Kansas State University Police Department or the Riley County Police Department. Reports made to law enforcement are separate from reports made to OIE. A complainant can choose to report to one or both entities. Confidential support and advocacy can be found with the K-State Center for Advocacy, Response, and Education (CARE). Confidential mental health services can be found with Lafene Counseling and Psychological Services (CAPS). Academic support can be found with the Office of Student Life (OSL). OSL is a non-confidential resource. OIE also provides a comprehensive list of resources on their website. If you have questions about non-confidential and confidential resources, please contact OIE at equity@ksu.edu or (785) 532-6220. 
