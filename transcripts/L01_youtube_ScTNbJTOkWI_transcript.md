# L01 Local Audio Transcript

Course: NE 630

Playlist source: https://youtube.com/playlist?list=PLy481lNHlnHoEO95vM-xYX2bydD25v20L

Video: NE 630 - Lesson 1

URL: https://www.youtube.com/watch?v=ScTNbJTOkWI

Video ID: ScTNbJTOkWI

YouTube upload date: 20230821

Duration: 51:19

Transcript source: Local faster-whisper transcription from YouTube audio.

Whisper model: large-v3; detected language: en.

Generated: 2026-06-28

Note: This transcript is machine-generated from audio and lightly wrapped only. It should be reviewed before being quoted, published, or used as polished lesson text.

Requested language: en

## 00:01

bigger, that down there, get this here, and finally go to the syllabus.

## 00:33

All right, so welcome to NE630, Nuclear Reactor Theory. I believe that's the official title,

## 00:41

is that correct? It is our undergraduate course on the topic of nuclear reactor physics,

## 00:50

which I talked a little bit about in some of the online verbiage that I gave. Why is there

## 00:58

not a power strip available? Oh, it's just one under here. Wow. That's not ADA compliant.

## 01:09

I just ended up leaving this brick in here. I'm recording. I have a feeling that I'll be

## 01:21

recording.

## 01:22

I'm going through battery quicker than I would otherwise be going through. All right, cool.

## 01:32

Okay, so this is one of the courses in the nuclear option. Is there anybody who's not

## 01:40

formally enrolled in the nuclear option? Yeah, so you're here for fun, or?

## 01:50

I didn't know we had to be enrolled in the nuclear option, but if I showed up, it would be terrible.

## 01:55

Okay, so are you just learning that now, or?

## 01:59

Is that something that had come up more recently?

## 02:03

Okay, yeah, so it doesn't stop you from being in the class. The distinction is what goes on the

## 02:12

piece of paper that you get for your records and so forth, so if you want to be included in the

## 02:17

option officially and have that on your diploma and other records, transcripts, and so forth,

## 02:24

you've got to get that officially done through your advisor. I don't know exactly what the

## 02:28

process is.

## 02:29

It's usually somebody else just deals with that, but you have the knowledge now, so you can act on

## 02:34

it. Okay, so this is one of the courses in the option, and actually, just chatting with some of

## 02:43

my faculty colleagues, we always have a big meeting before the semester starts, and whether

## 02:50

or not you're aware of it, the option that you have combined with the rest of your mechanical

## 02:54

engineering curriculum looks a lot like a traditional nuclear engineering course, but it's not

## 02:57

like a traditional nuclear engineering course. It's a lot like a traditional nuclear engineering
course,

## 02:57

but it's a lot like a traditional nuclear engineering course. It's a lot like a traditional nuclear

## 02:58

engineering program that you would find in any other, you know, university program, so I did my

## 03:05

undergrad training at the University of Wisconsin. They're similar in the sense that they've got a

## 03:10

nuclear program embedded in a larger department. It's not as large as engineering physics, but

## 03:15

there are a whole lot of programs out there that are embedded in other departments, mostly because

## 03:21

nuclear had a kind of a dip in enrollment and so forth, research dollars, a whole bunch of

## 03:28

stuff happening in the 90s that led to a lot of programs either disappearing completely, which is

## 03:33

sad, or being sucked up into larger departments, as was the case here, right, being part mechanical.

## 03:40

For nuclear power applications, that's not a bad way for the program to have gone, right, because

## 03:46

mechanical engineering includes courses in thermo, fluids, heat transfer, all those are really

## 03:52

relevant for understanding how nuclear reactors work in like a big picture engineering sense.

## 03:57

What we're covering in this class is a lot of stuff that's happening in the 90s that led to a lot of
programs,

## 03:58

but we're not going to talk about heat transfer. I mean, we might have to rely on some basics to get
an

## 04:08

appreciation for the big picture, as it were, but we're fundamentally worried about the neutrons and

## 04:14

what they do, but combined with that background in heat transfer, fluids, thermodynamics, material

## 04:21

properties, and such that you would have had in another department, you do get sort of the

## 04:26

background that you would expect in a typical undergraduate program. So, I think that's a lot of

## 04:28

things that we're going to talk about in this class.

## 04:29

And then, of course, there are other degrees that you can pursue, master's, PhD, et cetera. That's

## 04:34

something that you are interested in. So, I just wanted to point that out.

## 04:39

A little bit about myself, I guess, before I dive in. My name is Jeremy Roberts. I'm super informal,

## 04:45

so you can do the whole doctor, professor business if you want. I'm totally fine with

## 04:51

just being called by my name, too. Whatever makes you comfortable is fine with me.

## 04:58

But like I said, I'm from Wisconsin, and actually, I just spent the past half year in Green Bay,

## 05:04

Wisconsin. I just bought a house up there. I was on leave working for a software company that does

## 05:08

some nuclear stuff, and that leave has ended, so I transitioned back, but I do have a home base up

## 05:14

there now, so I can see my kiddos. I think we all went through some life changes with COVID and so

## 05:20

forth. I went through maybe more than is typical. But anyway, so I spent some time there. I went to

## 05:27

MIT for my PhD. I went to MIT for my PhD. I went to MIT for my PhD. I went to MIT for my PhD. I went
to

## 05:28

MIT for my PhD work. I've been at K-State since 2013, so this is now going to be my 11th year

## 05:34

here, right? Strangely enough, even though I am a reactor physicist, I suppose, by training,

## 05:40

computational anyway, this is only the second time I've taught this course. First time was

## 05:45

last semester, right before I was about to jet out and try this software business for a while,

## 05:50

just the way the department was organized at that time. So maybe you've heard of Dr. Bindra.

## 05:56

He went to Purdue.

## 05:58

A year and a half ago or something like that. He had been teaching the course, which is odd

## 06:02

because he's a reactor thermal hydrolysis. He's the one who cares about that heat transfer. So

## 06:06

anyway, certainly I know the topic, but you'll have to call me out sometimes because you've

## 06:13

heard of this expert bias where somebody who knows a hell of a lot about something, or at least

## 06:17

thinks they know a hell of a lot about something, will kind of forget that you don't. That will

## 06:24

happen. I am warning you.

## 06:28

I'm also encouraging you to point out when it does happen so that we can maybe not get lost in

## 06:33

some details or so that we can get some details out of the way and get onto sort of what I'm going

## 06:38

for. So that's something to be aware of. Anything else about me that's relevant?

## 06:47

Computational, reactor physicist. I like to play guitar. I'm getting into boxing. I've had some

## 06:55

anger to get past over the past few years.

## 06:58

I live very close to campus. I've had some of the A&S folks come and help me clean my yard as I was

## 07:05

getting prepared to be out of town for a while. So I'll probably do some more fundraising for the
A&S

## 07:10

group this fall because I hate breaking leaves and I still have yet to fix my leaf shredder.

## 07:17

I got this big giant 6.5 horsepower predator like engine thing for chopping wood and shredding

## 07:25

leaves. And I broke the carburetor post.

## 07:28

And I never recovered from that. Yeah. So computational, not mechanical, right? Okay.

## 07:35

So about this class, we don't have to spend a whole lot of time on the administrivia. The textbook

## 07:42

that I brought my own copy of here is a really neat book for a couple of reasons. One,

## 07:49

it's pretty straightforward. It doesn't have a lot of the, I wouldn't call it fluff. It's just

## 07:55

you get, you know, if you understand Hamilton is the one that I would have,

## 07:58

I would have liked to have a book that was written in the mid seventies. It was written,

## 08:02

has a lot of good stuff. It's slightly more advanced than I think can be expected of a class

## 08:06

given the context of everything. And it has a lot of information that's just not needed.

## 08:13

This is streamlined. And what's neat about this author, Elmer Lewis, he's a professor emeritus

## 08:19

at Northwestern, right? Northwestern doesn't have a nuclear engineering program. I'm not sure that

## 08:24

they ever did, but he was a nuclear engineer. He was there.

## 08:28

Probably because of proximity of Northwestern to Chicago and in Chicago is Argonne national lab,

## 08:33

where he had a lot of connections. And so he was teaching in the mechanical engineering

## 08:38

program at Northwestern and wrote this book to teach a course that served as an elective course

## 08:44

for them. So it's almost like any 495 is here for a lot of mechanical students, only it's not

## 08:52

an elective, right? Because you have to take it. So that, that the fact that it's required is what

## 08:57

maybe sours the opinion.

## 08:58

This was, I guess, a very popular course. And because of it being sort of a standalone,

## 09:04

you'll notice that if you, maybe you've checked the PDF, it does cover a little bit of what 495

## 09:10

covers in the beginning. And we'll review that over the next few sessions, at least the bits

## 09:17

and pieces that we need. But I like it because it's also organized in a way that I think makes

## 09:22

sense to me pedagogically, meaning how do we take this big problem that we want to solve,

## 09:27

understanding what neutrons are, and how do we take this big problem that we want to solve,

## 09:28

and what neutrons do in a nuclear reactor and break down the mathematical model that we need

## 09:33

to describe what they do into the bits and pieces that we can kind of chomp on a bit at a time and

## 09:40

come away with a better understanding of the whole. There's no way that we can take something

## 09:45

like this. If I can go to the course introduction, there was a purpose here to put an equation

## 09:52

like this. I could have broken it up a little bit better. Maybe I'll zoom in, right? This is a nasty

## 09:58

partial differential equation with some integrals. It's an integral differential. This is the

## 10:02

diffusion equation, right? This isn't even the whole story. I could do the neutron transport

## 10:06

equation and it would just get ugly. But as written here, I mean, that should probably make

## 10:12

you feel uncomfortable. Maybe you felt like, what the hell am I getting myself into? Don't worry,

## 10:17

we're not going to solve this equation directly. We're going to take it and we're going to break

## 10:20

it into the pieces. We're going to get rid of some of the variables and hopefully piece together an

## 10:25

understanding of all of the physics that comprise this equation. And I think that's going to be a

## 10:28

topic of reactor physics or reactor theory, okay? As far as the course mechanics will go,

## 10:41

I'm going to simplify it a little bit over what I had done last time. We're going to do

## 10:47

homeworks and exams. There'll be traditional in-class exams, I believe, at this point is what

## 10:53

I'm planning to do. I purposely don't put any details in there to give you some flexibility,

## 10:58

but I am planning on having three each for the point.

## 11:01

So 60% of the whole. And then homeworks, I say approximately 12. If I get my act together,

## 11:08

it'll be closer to 15, as long as I can keep assigning problems per lecture, as I've done

## 11:14

for the lessons day. And the way the homeworks will work is for a lesson like today or any other

## 11:20

day, we'll have two or three homework problems, I think. I mean, it depends on kind of the style

## 11:26

of the problem. Most of them will come out of the book. And there are associated,

## 11:31

solutions with everything. I'll give them out as part of the lecture notes, and I'll show you

## 11:36

an example that I have for today. I'll assign it for that lecture. You'll know what it is.

## 11:40

And then every week, the Monday, Wednesday, Friday, all those problems are due the following

## 11:44

Friday, right? So what that means is we have a week where there's only two days of class.

## 11:50

Well, the following week, you'll have fewer things due, right? All of the problems will

## 11:54

be roughly equally weighted. Some of them are more complex than others. We might have a greater

## 12:00

number, if I think.

## 12:01

Something has to be addressed more thoroughly. But I'm hoping that throughout, it's kind of a

## 12:08

reasonably consistent points per week that you can count on. So if we're not getting to the end,

## 12:13

it's like, oh, I need, you know, 40 extra homework points to make whatever grade you're

## 12:19

shooting for, right? You'll notice I don't have anything for the grading in here. I'm

## 12:23

defaulting to the K-State standard, 90, 80, whatever. As I've said to other classes in the

## 12:31

past, I don't have anything for the grading in here. I'm defaulting to the K-State standard,

## 12:31

especially ones that are beyond the entry level. I don't care about the grades. I mean,

## 12:35

I know you do. And it's like an important thing on your minds because you want the shiniest record

## 12:41

that you can. But I don't want it to get in the way of the learning, as it were, right? So

## 12:47

I guess along the way, if we have any concerns about where you are, I mean, feel free to reach

## 12:56

out. But I'm hoping that everyone can comfortably be in the A-B range, right?

## 13:02

And that makes my life easier. It makes me feel like I'm doing a better job. It makes you feel

## 13:06

like you're doing a better job. And then we all walk away to Christmas time happy. That's what

## 13:10

I'm, it is fall, right? Yeah. So cool. Any, I'll say one thing about the prereqs. So of course,

## 13:20

you've had to have 495. Anybody not have 495? Wouldn't think it'd be possible. And then math

## 13:27

240. Is it 240 or is it?

## 13:31

It's a 340. I can't remember. Yeah. So they changed that to 340. I guess I was copying the

## 13:39

prereqs from a course catalog. That must be out of date. Who's had 400? I guess maybe a better

## 13:46

question. Who has not had any 400? So who does not know how to program Python? Are you just hedging

## 13:57

your bets? Have you programmed Python before? You've had 400? Okay. So I missed you on that.

## 14:05

Are you in it now?

## 14:06

No.

## 14:07

Okay. So one person not in.

## 14:10

I worked sort of at it, but I had to go out.

## 14:13

Okay. So.

## 14:14

But I'm taking it again right now because I've had experience with it.

## 14:18

Good. So it's not a prereq. I only point it out because it can be super helpful. I mean,

## 14:24

that's the point of computer programming is to help you get things done, or at least that's my

## 14:29

mantra when teaching. So I taught ME 400 for several years. I know it's changed fundamentally

## 14:35

from what, what I'm doing now. But it's, it's, it's, it's, it's, it's, it's, it's, it's, it's, it's,

## 14:36

it's, it's.

## 14:37

deftly what it was.

## 14:40

It's changed from the DOM to what I did. And I think what I did would better align with

## 14:48

courses like this, as opposed to, what it aims for now, which is, I guess, probably more

## 14:52

hardware driven with the Arduino focus and such. But the cool thing is, because I like

## 14:57

computing, you'll, you'll get to learn some computing along the way, right? So there's

## 15:00

not I'm not going to expect that, you know, how to do anything specifically. I do hope

## 15:02

that you're comfortable on your computers and willing, that you're willing to work with

## 15:03

me. But I don't think there's anything in here that will require the fact that I'm not

## 15:04

teaching.

## 15:04

But I have evidence that you're not. But that fact that I admit that you have evidence like

## 15:04

so that you have ability to learn and you are willing to work on it. So thank you for

## 15:05

require that you do something on the computer with the exception of maybe some computer

## 15:10

oriented problems that would use OpenMC, but I can organize that in a way that you'd be working

## 15:16

with somebody else possibly, right? So I want to get all that is kind of open-ended. I wanted to

## 15:21

get a sense for where you all are on that before saying that, yes, we will do something or no,

## 15:28

we won't. All right. So as far as the lectures, I already said I'm informal. I expect these

## 15:37

lessons, but the live part of the lessons, I guess for nomenclature, I'm going to call lesson

## 15:43

the entire set of materials that goes together with a lecture. That's the reading, all that.

## 15:48

So we could call this a lecture because I am just a talking head at the front of the room,

## 15:52

right? But as part of that, you should be doing some preparation. You'll be doing some problems

## 15:56

after the fact.

## 15:58

And to help you and help me stay organized, I'm going to try to have a page set up like this for

## 16:05

each lesson, ideally in advance. I guess this was published before lecture, but I'm hoping to kind

## 16:12

of ramp up and get ahead by about a week and so forth. And that will also let me help fill out

## 16:18

the lesson schedule, which is currently not filled in. So for lesson one today, I'll give the date

## 16:27

and then some learning.

## 16:28

And then for lesson two, I'm going to give the date and then some learning objectives. You've

## 16:28

probably heard about learning objectives. There are learning objectives in a general sense. There

## 16:32

are ABET objectives and so forth. I get so bogged down in the nomenclature that I found a resource

## 16:38

that I liked, and I'm sticking with this idea of macro versus micro. Macro might be those things

## 16:43

that you would see on like a course syllabus. You'll notice I didn't have anything on the

## 16:47

syllabus itself because I hate copy and paste too. That's going to be one place I don't read it

## 16:52

and everything else. But these micro objectives, you can think of these as examples of maybe

## 16:58

problems, like the sorts of problems that you'd be able to solve after getting through and mastering

## 17:02

the material of a given lesson, right? So I am willing to bet that even without having done the

## 17:08

reading, you would be able, many of you would be able to explain the nomenclature of this symbol

## 17:13

here, right? X with an A to the upper left and a Z to the lower left. Alex, did you remember what
that is?

## 17:22

Yeah, but I always get them flipped around. Some of the nomenclature is different, but you have like
your element numbers,

## 17:27

is that?

## 17:28

It's A, it's your atomic number.

## 17:31

The mass number. Yeah, so that's the crappy thing is we use A when you think atomic, but actually
the atomic number is Z, right?

## 17:39

Do you remember what the atomic number is?

## 17:41

Protons.

## 17:42

Number of protons. Do you remember what the mass number is?

## 17:45

Protons.

## 17:45

Yeah, so the number of nucleons, right? So neutrons and protons are, we can call them nucleons. And
then X is the

## 17:53

one or two letter symbol for an element, right?

## 17:58

The thing that you would find on a periodic table, right? You probably remember things like Q-value.
Who had 495 with me?

## 18:05

Yeah, all right. I figured you'd look, a lot of people would know you. So, I mean, you know how I
operate and yet you're still here, so that's cool.

## 18:13

All right, so lots of these micro objectives and many of these things will be mapped on to specific
problems where I think that you would need extra practice.

## 18:24

There are some things here that, you know, I know that you've done.

## 18:28

It before. So like with the overlap with 495, I might not waste your time by having you do something
again, right?

## 18:36

That doesn't mean that it wouldn't show up in an exam format at some point.

## 18:40

But ideally, if I'm focusing on certain things in lessons and lectures, those are the things that
would show up on an exam, too.

## 18:48

Right. We also have some key terms.

## 18:50

And then this is kind of the key thing for what you do before the lecture, right?

## 18:54

So if you got that, the email from me.

## 18:58

You'll know that you should be reading sections one through 1.1 through 1.3 in the book.

## 19:03

A lot of it should look pretty familiar as you're reading to find the key terms, right?

## 19:08

So I'm going to try to list these key terms and you can define them in your notes, especially if you
don't know them, right?

## 19:14

If you remember what a nuclide is or a proton or the atomic number, don't waste your time, right?

## 19:20

I'm not asking you to fill in boxes just for the sake of filling in boxes, but do it if you really
do think that there is a gap.

## 19:28

And then be considering these learning objectives along the way after lecture is where you start to
show me what you know through some assessment.

## 19:36

We'll get some informal assessment here in the class.

## 19:39

I might do pop quizzes, a bit formative in the sense that you'll turn something in.

## 19:44

I'll give you the answer. You'll know in your heart that you were right or wrong, and that'll be the
end of it.

## 19:49

That's what formative assessment is.

## 19:52

But after after the fact, you'll have to do some more summative assessment, right?

## 19:57

That will be the.

## 19:58

You'll have to do some more homeworks and then the exam, so you've got three homework problems,
sometimes they'll add a little bit more, because I think that the problem has some low hanging fruit
that we should pick, and in this case, I put that verbiage here, that'll connect to a little bit of
what I'll talk about here, and then here's that little bit about how organized the homeworks, which
I guess I could put syllabus, and then I might put some enrichment things here.

## 20:23

So as I was trying to piece together kind of big picture context of what I wanted to talk about
today.

## 20:28

Well, we'll go about this a little bit more then we can go through a part of thisth, a little bit
more detailed.

## 20:32

And I'm thinking I'm very liking how all wiederzone I folks tried to put it this way, so I'll take
this a little bit

## 20:55

I truly, very much appreciate this.

## 20:56

There.

## 20:56

Really awesome.

## 20:57

Awesome.

## 20:57

Fun.

## 20:57

You're very welcome.

## 20:58

For.

## 20:58

So if you've had, if you're one of the, it looks like the majority who had me in 495, you have seen
Jupyter Notebooks in action, right?

## 21:11

Who has never seen a Jupyter Notebook?

## 21:15

Have you ever heard of it?

## 21:17

Okay, so basically a Jupyter Notebook is a web-based tool that is strongly associated with Python.

## 21:25

It doesn't have to be Python, but it looks kind of like what you see here.

## 21:29

It's a document that includes both written stuff.

## 21:33

It doesn't have to just be text.

## 21:34

You can have images.

## 21:35

So basically document-type stuff along with some code, right, where you have code blocks.

## 21:40

I don't expect you to be able to use this or want to use this or anything like that, but I'll use it
as a way to combine some basic textual or data or whatever along with some of the programming.

## 21:53

I will also be using.

## 21:55

Where did I set that?

## 21:57

So rather than doing stuff on the board, which is challenging to capture for distance folks, I will
be using this thing here when we get to that point.

## 22:13

There we go.

## 22:21

Yeah.

## 22:22

And do I have the setup to use?

## 22:25

I guess I do not have it.

## 22:31

So I just got this computer all set.

## 22:33

So I don't have the presentation version of it yet, it seems.

## 22:40

But that is fine.

## 22:42

I can actually blow it up a little bit.

## 22:45

Okay.

## 22:45

So I've gone through the course administrivia, course objective, rephrase in a different way.

## 22:52

Okay.

## 22:52

So I guess at this point I can dive in.

## 22:58

And hopefully this is all being captured.

## 23:02

I'm having issues.

## 23:03

Okay.

## 23:03

So I use.

## 23:03

Linux almost.

## 23:05

So I do have a Windows machine at home, but I try to use Linux because it's easier to manage all the
software that I need for technical stuff.

## 23:16

But there are sometimes hiccups.

## 23:18

And when you put something, you start over on a computer, we will run into hiccups.

## 23:27

So hopefully not too many.

## 23:29

Let's see if I can get.

## 23:31

Well, the Jupyter Notebook and DSTAS.

## 23:33

Yeah, so what my plan is, is to post all of the Jupyter Notebooks in their executed form.

## 23:42

I don't expect that I'll have to rely on them too much, but it's hard to, it kind of depends on the
mood of the class, if that's the right way to do it.

## 23:52

But yeah, any, anything that I do in here, I'll try to make available.

## 23:54

So there will be a video somewhere that has everything that my screen is capturing along with the
voiceover.

## 24:01

This thing.

## 24:02

Anybody ever use?

## 24:03

My paint.

## 24:04

It's like a nice version of the MS paint that has all sorts of brushes and so forth.

## 24:09

And with the pad, it gives you pretty crisp output.

## 24:13

Basically it's an image file that it produces.

## 24:15

I can also make that available to sort of like the, as if somebody took a picture of the board after
we're done.

## 24:21

Okay.

## 24:26

Here's the route.

## 24:26

So the very first thing that's talked about in the book is this concept of powered energy.

## 24:35

Specifically energy density of, of nuclear reactors.

## 24:38

Right.

## 24:38

And that fundamentally relates to an equation that you're all familiar with.

## 24:44

I would, I would also call it the most famous equation, this side of 1900.

## 24:51

Right.

## 24:51

If we go before 1900, one could argue that F equals ma is more famous, right?

## 24:56

But equals MC squared is definitely a famous equation.

## 25:04

Something that.

## 25:05

Changed the world fundamentally because it, it really unlocked the idea that things were very
different from what we thought classically, right?

## 25:16

Lots of things came out of that, you know, just revolution, right?

## 25:21

Well, one of the things, this mass to energy equivalence made it possible to even conceive of a
source of energy that was as large as nuclear is.

## 25:31

Okay.

## 25:31

So when we take a look at this equation, what do we see here?

## 25:35

What are these terms?

## 25:39

C is the speed of light.

## 25:40

C is the speed of light.

## 25:41

Yep.

## 25:41

So that's the light speed.

## 25:49

Do we know what that number is?

## 25:55

Yep.

## 25:56

So I'll be super concise with the numbers.

## 26:03

We'll round to three, right?

## 26:05

What is the E and what is the M?

## 26:10

Yes.

## 26:11

That's it.

## 26:12

So what is the E and what is the total energy and if we're in SI units of meters, seconds, this
would be in jewels, but we'll find often that it's better to use things like MEV, right?

## 26:26

Or we could be using a typical power, like watt multiplied by some time, like an hour, watt hour or
kilowatt hours.

## 26:34

Those are things that we see often in the energy production, electricity production applications.

## 26:41

Okay.

## 26:41

And then what is this, this mass?

## 26:43

Okay.

## 26:44

It's not the rest mass.

## 26:50

What's the other mass?

## 26:53

What do we even call that mass if it's not rest mass?

## 26:58

Yeah, we, I think that's what we would call it, the relativistic mass, but that of course relates to
the, the rest mass, right?

## 27:10

Because this, so E equals MC squared, this is just, it's a statement that says, hey, energy is
fundamentally related to mass, but that mass is not the mass that we're going to think of, like rest
mass, like whenever we talk about masses, that would be the rest mass.

## 27:23

So the thing that we have to remember is that the relativistic mass is equal to the rest mass scaled
by this thing that you might remember, a square root of one minus beta squared, where beta is equal
to the ratio of the thing's speed, right?

## 27:46

The velocity of the object that we're talking about, or speed, because we don't care about the
direction right now, divided by.

## 27:53

The speed of light, right?

## 27:54

So beta, in this case, is the fraction of the speed of light, whatever object there is.

## 28:00

So we know that, that relativistically speaking, if we get this mass increase, right, beta is going
to be some fraction of fraction is bounded by zero and one, so it can be between zero and one, but
you're taking one minus something that is less than one greater than zero.

## 28:16

That means you're increasing M naught, right, to get whatever your relativistic mass is.

## 28:20

And the closer you get to the speed of light, bigger beta.

## 28:23

The smaller the denominator is, and therefore the bigger the M is and the bigger your total energy
is.

## 28:28

So the thing is, when things go super fast, their total energy is increasing, right?

## 28:35

Bigger than we would expect it to be classically.

## 28:37

And that's pretty important because that changes potentially all of the kinematics that you've
learned, right?

## 28:42

You know, billiard ball type collisions, all that stuff is subject to this, okay?

## 28:46

So the very first thing I want to do is when we talk about neutrons, do we care about relativistic
effects?

## 28:56

Do you have a sense for that?

## 28:57

Like everything that we do in this class is going to involve neutrons to some degree or another,
right?

## 29:02

And a lot of it, when we get one of the very first things we do with that ugly equation I showed,
the diffusion equation,

## 29:09

one of the things that we want to understand reasonably thoroughly is when neutrons are born from
fission,

## 29:15

they have energies that are on the order of 2 MeV, right?

## 29:21

And then they migrate through the sea of water, oxygen.

## 29:25

Uranium and all this other stuff that you find in a reactor, and they slow down to thermal energies.

## 29:30

For those who had 495, I showed you this beautiful piece of artwork that I had produced that shows
you, in essence,

## 29:37

the nuclear physics involved in nuclear fission reactors and the energy production, right?

## 29:44

There's a big swath of fission probability in one part of the graph, and you need your neutrons to
go from fast energies to low energies to get to that point where they can cause fission.

## 29:55

Right?

## 29:56

This process of neutrons slowing down, how do neutrons slow down?

## 30:00

Yeah, moderation.

## 30:02

And what is that process?

## 30:04

Moderation, it's just billiard ball kinematics with hydrogen and other things.

## 30:08

But for a thermal reactor like the one we have over a couple hallways down or at Wolf Creek,
everything is driven by thermal neutron-induced fission.

## 30:18

The way we get thermal neutrons, meaning low-energy neutrons, is to take them from their fast
energies that they have at birth,

## 30:25

they pack them from fission, knock them around in some hydrogen that lives in the water that we use
to cool the reactors,

## 30:32

they lose the energy through these billiard ball kinematics and ultimately produce fission.

## 30:38

So, we need to understand that process.

## 30:39

So, can we do that using regular old dynamics, the same dynamics that you would have had in your
dynamics course,

## 30:47

possibly physics 2 course, or do we have to do relativistic?

## 30:51

I claim we don't need to use relativistic kinematics.

## 30:54

Right?

## 30:55

range of interest. So you might remember that neutrons, no, why can't,

## 31:05

did not, there we go. Okay. So the neutron, neutrons in reactors range

## 31:21

in energies of, we'll say approximately zero up to 25 MeV, right? The distribution of energies

## 31:38

that come out of fission, I mean, it's a distribution, right? I don't know what the

## 31:43

highest energy ever reported is, but the average is 2 MeV. The maximum that we would expect to see

## 31:51

is something like 25, and that's very, very low probability.

## 31:55

Okay. So the question I have is how can we assess what fraction, how can we, I guess

## 32:03

the question I'd like to answer is what fraction of the speed of light in a neutron be going at

## 32:11

before the error and the kinetic energy is greater than 1% between relativistic

## 32:21

and classical treatments?

## 32:24

Why do you buy them into like,

## 32:25

I'd say that again?

## 32:28

I think it's one of the five, like, five ways forward in speed of light.

## 32:33

Yes, I think that I, it will be a fraction of about that name, right? The specific error that

## 32:42

we choose will dictate that. So we can, we can definitely solve the problem many different ways

## 32:46

with different limits, but it's, I think we're sketching out the solution to this, right? So

## 32:51

what I mean by that is

## 32:54

what,

## 32:56

is

## 32:58

the maximum

## 33:00

beta such

## 33:03

that

## 33:04

E

## 33:07

classical

## 33:09

where's my eraser?

## 33:17

I need a bigger eraser.

## 33:24

So what,

## 33:28

actually, I'll make this my relativistic,

## 33:36

relativistic minus E

## 33:38

classical over

## 33:40

E

## 33:41

relativistic.

## 33:42

High-precision.

## 33:43

Is less than some error, right? Which could be 1% or whatever.

## 33:49

So in order to solve this,

## 33:51

we actually have to go back to

## 33:53

equal m c squared, to classical mechanics.

## 33:56

What is the kinetic energy, right?

## 33:58

If you, if you were just doing F equal m A from dynamics,

## 34:02

How do we define the, the kinetic energy of a moving object?

## 34:12

Yeah, it's, it's that, that, right?

## 34:14

So.

## 34:15

Okay. So my classical, so this is classical, classical K E right. I'm using E here. I don't

## 34:32

really like using E for kinetic energy, but you'll notice that the book adopts that when you go

## 34:37

through the reading, the author starts off E for total energy, but we're going to use it now for

## 34:41

kinetic energy because we can get past the relativistic stuff. Okay. So the classical

## 34:47

kinetic energy is equal to one half M naught because classic physics only cares about the

## 34:55

rest mass times E squared, right? The relativistic kinetic energy is equal to what? This is kind of

## 35:04

a tricky thing because there's not like an apparent kinetic energy formula for the relativistic

## 35:10

particle. How do we get it?

## 35:22

So it will look like that. So the key thing is E equals MC squared. That's the total energy,

## 35:28

right? We also know that there's a rest mass energy, like the M naught times E squared. So

## 35:33

the difference is the kinetic energy, right? So the expression we're looking for is

## 35:39

the, so the total energy, which is MC squared minus the rest mass energy, M naught C squared.

## 35:53

But because we know that M,

## 35:54

is actually a function of M naught, this is equal to one over square root of one minus

## 36:02

beta squared minus one all times M naught C squared, right? See how I get that? I substituted

## 36:11

my expression for M, the relativistic mass here. That's the one over the square root business times

## 36:17

M naught. And so I can pull out the M naught, okay?

## 36:19

Minus one below or outside, right?

## 36:24

This is outside, right? So the one times M naught C squared, that's this thing here.

## 36:32

In fact, do I have a color wheel? No, give me the regular color. There we go.

## 36:38

So minus one is not in the denominator?

## 36:39

Correct. Yeah, let me, there we go. Okay. So we have these two expressions. So now what we,

## 36:49

what we need to do is actually just set up the, the, the equation, right? So what we're looking

## 36:56

for is,

## 36:57

find beta such that

## 37:02

E R minus E C over E R is less than some, some error, and we'll call this one percent, so zero,

## 37:16

0.01, okay? This is, this is what we're trying to solve. And why would I say less than epsilon?

## 37:26

Why would I find beta?

## 37:27

Such that this is less than, well, we know that the error will be monotonic increasing as a function

## 37:33

of beta, right? The, the bigger beta gets, right, the closer the speed of light that, that we get,

## 37:39

the, the error between, or the difference between the classical and the relativistic approach will

## 37:43

continue to grow, right? We're not going to have any wiggling and try to find, like, a minimum

## 37:48

that's trapped between two peaks or anything like that. So it's reasonably straightforward. We'll

## 37:52

know that it is some reasonably large fraction of the speed of light. So beta will be,

## 37:57

you know, the, the, the, the, the, the, the, the, the, the, the, the, the, the, the, the, the, the,
the, the,

## 37:57

I don't know, point, it would be the 0.2, 0.3, 0.4, right? So this is the statement of the problem.

## 38:03

How the hell do we solve it? Like, how would you, how would you solve this problem? Any ideas?

## 38:20

So my hypothesis, and I'm far too old and lazy to pursue this, is if you actually substitute all

## 38:27

the expressions in, right, you have the, all these radicals, the, the square, one minus the square

## 38:32

root of, uh, one over one minus beta squared, right? Uh, under,

## 38:38

under the square root symbol. I bet if you took that and you started multiplying things out,

## 38:43

you would end up with a quadratic equation for beta, uh, after some manipulation. Who wants

## 38:48

to solve a quadratic equation? I mean, it's not that terrible. I should, I should actually

## 38:53

encourage you to, to go through that, but I, I don't think that's the important thing here.

## 38:58

What's more important to me is being able to get to the solution reasonably quick. And this is

## 39:02

where I would then turn to something like a computer, uh, program, uh, Python, something like that,

## 39:08

where we can actually find it more, uh, straightforwardly. So we can do it. We could,

## 39:14

we could do some guess and check. We could probably solve it analytically. If it is that

## 39:18

quadratic, uh, if somebody can show me that it is, I might, that might be willing. I might make

## 39:23

that an extra credit point, uh, for the homeworks, right? Maybe I'll formalize that in the, um,

## 39:28

homework statement when I get that out. Okay. But there's a, a, a different way that I'd like to do

## 39:34

it. And it looks like this. Okay. I'm going to take beta and,

## 39:38

so I'm using num, uh, Python here with some numpy math. I'll live for those who have used

## 39:43

Python. Those are probably some of the more common things that you would use. Okay. So what I'm
going

## 39:48

to do is I'm going to take beta and I've limited it here from just about zero. I don't want to put

## 39:53

zero in because then I get a divide by zero. I bet zero divided by zero issue. Okay. And then

## 39:58

I'm going to put it in a range up to about 0.15 and I'm going to break it up to 2,000 points.

## 40:02

Okay. So this is basically just giving me a vector of beta starting from zero and then stepping.
It's

## 40:07

giving me steps so that I can plot the functions. One of the easiest way to solve a problem or at

## 40:13

least get a partial solution to a problem like this is to take this thing on the top, recognize

## 40:21

that this thing, the denominator here is just some function of beta, right? The relativistic energy

## 40:27

here has some betas in it. The classical energy also has some betas. If we view this as one half

## 40:35

M naught times,

## 40:37

beta squared times C squared, right? So V squared is equal to beta squared times C squared.

## 40:44

Can you believe that? Right? Because V is equal to beta C. Okay. So we can see that both of them

## 40:53

are beta. So we get some function of beta over the relativistic energy, right? Which is some other

## 41:00

function of beta. And we could solve for, we could reorganize it like that. But when you have these

## 41:07

things that are when they cross a threshold, you can just plot them against each other and find out

## 41:13

where, where, where something crosses. So the way that I'm doing that in this image that I'm

## 41:20

generating in Python is I'm going to take this thing here. So that's the relativistic expression,

## 41:27

right? And I'm taking that relativistic expression, subtracting away the classical,

## 41:32

and then dividing by the relativistic. This is the error. This is the error that I'm doing.

## 41:37

I'm looking for where this error crosses the specific value that I care about. So let me go

## 41:44

ahead and load these things. Okay. So this is a function of B that I will evaluate at each one

## 41:54

of these betas. Okay. So I'm taking beta, I'm plugging in these values that I have here into

## 41:59

this function F, and then this is what I get. So I specifically chose the X and Y coordinates so

## 42:06

that things would fit nicely.

## 42:07

So that we didn't have to play the guess and check, but you'd be able to plot it. And with

## 42:13

default values, you'd see that it crosses down here and you'd be able to do it. And so if we

## 42:17

look at this, this thing crosses at somewhere between 0.1 and 0.12, right? So, you know,

## 42:27

roughly 11% of the speed of light is where we see that these two expressions for kinetic energy

## 42:35

diverge by more than 1%.

## 42:36

If I go past

## 42:37

that speed, I'm going to have an error that's larger. Okay. Now the question is, I have beta.

## 42:43

Has that actually answered my question? I guess as a state of here it did, but what I really want

## 42:48

to know is what energy, what kinetic energy can neutron have before we have to start caring about

## 42:53

how do we get that energy from beta velocity? Yeah. So we get the velocity, the answer,

## 43:00

and then the classical value. We're looking for what classical value is going to be an error. So

## 43:07

to do that, I'll take this cutoff value that I found. And in fact, I actually used a slight,

## 43:14

I added an additional layer here. I could just use the 0.11, but if you've had anybody ever

## 43:20

use F solve in Python, it's a side by thing. It's a root finder, right? So if I wanted to find out

## 43:28

exactly where this blue curve, which is a function of beta equals this value 0.01, I can make a new

## 43:36

function that I call an objective function here, plug it in, and then I can actually get that

## 43:41

value to whatever precision I want, right? So it's going to be 0.1154. So 11% just visually

## 43:52

is not a bad estimate, right? So graphical solutions to these sorts of problems, totally

## 43:57

fine for kind of like, you know, thumb in the wind, back of the envelope type things. If you

## 44:01

need to dive in, then you should use something more, I guess, robust. And there are ways to do

## 44:08

this in Excel if you're more comfortable with that. And if I show you something like this and

## 44:13

you really want to learn more, I'm happy to help you out. I don't think we'll have time in the

## 44:18

class to explore a lot of these things. But anyway, so we get that, and then we get the energy,

## 44:24

and that turns out to be 6.25, right? Now, I said that the energies that we see in a reactor could

## 44:30

be all of that.

## 44:31

25 MeV, but the probability that we find neutrons that energetic is pretty low, right? The average

## 44:39

energy of neutrons coming out of fission is about 2 MeV. The most probable is 1 MeV. So if we're up

## 44:44

to 6 MeV, there's a very small chance that relative distance effects matter at all. And

## 44:50

remember, that's just the neutron form. What we care about is in the small amounts. The vast

## 44:54

majority of neutrons in our world will be far from the 12 and 6 value. And I point all this

## 45:01

out because I don't want to go into too much detail, but I want to point out that the

## 45:01

it's in the book, and I thought it was really wise of him to include that, because why do we

## 45:07

talk about this rest mass versus relativistic mass unless we understand where we don't have

## 45:13

to worry about it? There's no sense in learning about it unless you know why it would be important

## 45:19

to use, okay? The other thing in the reading is, well, actually, before we do that, I do want to

## 45:26

go back to this very briefly, okay?

## 45:36

So in the very first pages of the chapter, he talks about the energy density of things. So

## 45:49

he motivates it in one way. I could motivate it in a different way. So think about the

## 45:57

Wolf Creek. That's the closest commercial nuclear power plant that we have. Anybody

## 46:02

know how powerful it is? What kind of electricity?

## 46:05

So I'm going to round that to 1,000, right, to keep my math. You'll notice I love to round,

## 46:14

right? So we've got a plant at Wolf Creek. It's about 1,000 megawatts electric, right?

## 46:23

How do we go from megawatts electric to the actual power being produced?

## 46:29

Yeah, or divide by 0.33 for the efficiency, right? So if we have an efficiency of,

## 46:34

you know, roughly 0.3, I think to follow my notes, I'll keep it at 0.3, right? Now,

## 46:42

basically what I want to do is understand for that power that it produces, how much fuel are

## 46:49

we using? And then how much power, how much energy do we have per amount of fuel, right?

## 46:54

This is kind of like one of those eye-opening things. Do you know how much fuel there is in

## 46:59

a plant like that? So did you intern there? Yeah. So do you know, like, how much uranium,

## 47:04

is there? I don't know how much uranium, but we've got 192 single elements and many, many,

## 47:10

many, you know, pellets inside of each element. Yeah. So good rules of thumb in these assemblies,

## 47:17

each one of the assemblies is roughly a half ton of uranium, right? So if you've got about 200 of

## 47:23

them, you just have to, you've got about 100 tons of uranium in the reactor. Every, so often,

## 47:31

every year and a half or so, about one third of it,

## 47:34

it is refueled, right? You've got this kind of like stacked use of the fuel so that you

## 47:38

maximize how much energy you get out. But at the end of the day, all this fuel that goes in there

## 47:43

stays in there for about five years. So you've got a hundred tons producing this much power over

## 47:48

five years, okay? You can work out what the energy density of that is, and then you can compare it
to

## 47:54

the coal, right? If you read in the book for the same size plant, you've got 10,000 tons of coal

## 47:59

being burned per day. The difference between the energy density, how much you're producing,

## 48:04

per kilogram of the fuel is several orders of magnitude, right? It's incredible. That's one

## 48:12

of the reasons why nuclear is so, I guess, important, why it was adopted, because it

## 48:20

doesn't use as much stuff, right? It has its own issues, but it's really, it doesn't, the footprint

## 48:26

that it has is very small. So I won't go into this. Maybe I'll reformulate it a bit for the

## 48:32

homework. But yeah,

## 48:34

the reason why we care about nuclear in general, nuclear, not just power, but in any context,

## 48:41

is the fact that we have so much energy being, or so much energy that we can use at a small scale,

## 48:49

right? The reactions that are occurring are a million times stronger than the chemical

## 48:54

reactions that drive things like coal combustion and so forth, okay? So I'm going to wrap up here

## 49:00

and point out just a couple,

## 49:04

some resources. So I'm not going to have you actually compute Q values, because you've done

## 49:09

that, right, in 4.95. But if you wanted to be able to find these atomic masses, there's actually a

## 49:15

Python module in Mendeleev, called Mendeleev, that you can import. If you've ever done pip install

## 49:21

for Python stuff, you can do it there. What's super nice, and I checked this out, for those

## 49:26

who had me in 4.95, remember I used Collab on Google, right? In Google, you can actually install

## 49:33

packages. It installs it on your computer, right? So you can install it on your computer, right?

## 49:34

I think it only installs it locally while you're using it, but if it's a small package, it's,

## 49:38

you know, free. I checked it out. That actually works. There's also another thing offered by the

## 49:44

IAEA. It has the nuclear data, the masses, and everything like that. So whenever we need to find

## 49:49

the masses, you'll have to use an online resource, because unlike the Schultes and Faw book that we

## 49:54

have for 4.95, not that I've required that officially anyway, because I offered my own

## 49:59

module, this doesn't have it. There's actually very little data, which is also kind of a reason I'd

## 50:04

like it, because we don't need to kill trees to share the data that's freely available on the web,

## 50:10

right? And anytime that you would need it for an exam or whatever, I'm going to give it to you,

## 50:13

okay? And then the other thing that really supplements what's in the book as far as

## 50:18

binding energy, mass defects, and so forth, is here at Brookhaven's site, New Data, right? And

## 50:24

so maybe next time I'll spend a little bit of time navigating that. It's super, super visually rich,

## 50:31

which I just love, okay? So before next time, look for the next page. It'll be the next couple

## 50:37

sections in the book. And yeah, let me know if you have any questions. Best way to reach me

## 50:45

is through Canvas email. I try to avoid the Outlook box as much as I can, so the Canvas,

## 50:52

I'll be monitoring that pretty regularly. So any questions? All right, then I will see you on

## 51:03

Wednesday.
