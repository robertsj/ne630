# L12 Local Audio Transcript

Course: NE 630

Playlist source: https://youtube.com/playlist?list=PLy481lNHlnHoEO95vM-xYX2bydD25v20L

Video: NE 630 - Lesson 12

URL: https://www.youtube.com/watch?v=SJvGncqHE98

Video ID: SJvGncqHE98

YouTube upload date: 20230918

Duration: 47:29

Transcript source: Local faster-whisper transcription from YouTube audio.

Whisper model: large-v3; detected language: en.

Generated: 2026-06-28

Note: This transcript is machine-generated from audio and lightly wrapped only. It should be reviewed before being quoted, published, or used as polished lesson text.

Requested language: en

## 00:05

All right, I think I have everyone back. I'm not a fan of this version of zoom but it'll have to
work. Can I.

## 00:20

Can somebody actually just speak up so I don't have to deal with the extra windows. If you see what
you're supposed to see.

## 00:28

Looks good. All right, thank you. All right, so, as I was saying in the beginning of the class I'd
said that we'd have three exams, roughly every five weeks, right to cover each third of the course
so that first exam will be in two Fridays.

## 00:52

So that will be on 929. Can somebody verify that that's the.

## 01:01

I think that's the Friday.

## 01:03

The last Friday of September.

## 01:07

Yep. All right, perfect. Yeah, so it'll be in class in class, and it'll cover lessons.

## 01:19

One through six today's 1213 and 14.

## 01:25

So to cover the lessons of this week.

## 01:29

The lesson on Friday is.

## 01:32

I think it's an important topic.

## 01:34

It's more computational in the sense that we'll be dealing with matrices that come out of this cross
section condensation producing effective cross sections but we'll do it for multiple energy groups,
and we'll talk about energy groups on Wednesday,

## 01:52

but the idea is that we break up that the range of energies of interest into energy bins, right so
we could, we could do it into two bins, right, going from 10 to the minus three EVs, or lower bound
up to 10.

## 02:02

So, we would have three EVs, or lower bound up to one EV. That could be one group and we would call
that the thermal group and then everything above that to our maximum energy of about 10 me would be
what we call the faster.

## 02:14

There's a lot of good intuition that we can develop by using such a two group method and that's
actually what we'll cover on Wednesday on Friday we'll take it a step further and look at larger
group structures where we can actually compute.

## 02:30

The spectra in a multi-group.

## 02:31

in a multi-group format, right? Once we condense the cross sections, making our physical assumptions

## 02:36

and so forth, we can actually back out a problem dependent solution. And that kind of goes beyond

## 02:43

what the book does, right? So the reading for Wednesday, really the reading for this week is

## 02:50

just section five of the book, which has some stuff in it. We'll be using some of it. I'm

## 02:54

deviating a little bit because I think this is maybe the one spot in the book where I know better

## 03:00

as it were. And then the week thereafter, we'll move into something entirely different. But the

## 03:06

exam topics will be everything through this week. Probably not a whole lot of emphasis on what we do

## 03:12

on Friday, because that'll be using Python or whatever language you're comfortable with. It

## 03:18

could be MATLAB, Octave, something where we can actually use matrices. But the concepts that

## 03:23

drive what we do on Friday will be the same things that we covered today and on Wednesday.

## 03:30

I have...

## 03:30

I have the homework two solution up. I have the homework three solution ready to deploy. I just

## 03:36

didn't upload it yet. I will buzz through grading, get you back some feedback. Hopefully those were

## 03:43

straightforward and the solutions there will kind of point you in the right direction. I'll give as

## 03:48

much feedback as I can for the 20-something of you through the rubric format on Canvas. But

## 03:56

if you have questions on the past homeworks or on the...

## 04:00

Upcoming homework, go ahead and let me know. So I posted homework four from the material last week.

## 04:05

I got that live. You had access to the questions. I didn't change any of the questions. I just

## 04:09

consolidated them into one page. So there should be no surprises there. And I will get the...

## 04:17

I will continue doing as I've been doing, putting homework questions on the lesson page so that you

## 04:22

know right away what it is. And I would definitely let you know if I have to change something due to

## 04:26

an error. So there's a little bit to do for today's lesson.

## 04:30

There will be something on Wednesday's lesson. There will probably be something simple for Friday's
lesson,

## 04:37

but because I'm not going to try to include that specific content on the exam, I'll focus primarily

## 04:43

on what we do today and on Wednesday. So I guess before I dive in further, are there any questions

## 04:52

about anything we did last week, any administrative issues, whatever? And go ahead and please just

## 05:00

unmute so that I don't have to deal with a frozen chat box again. All right. So feel free to send me
a

## 05:14

message if there's something more individual. I know that at least one student cannot do the exam

## 05:20

on that Friday. So if you've got to shift it a day before or the Monday after, I always prefer doing

## 05:28

it if students can do it before, but I understand that removes a day of possible prep. So I'd be

## 05:34

fine.

## 05:34

I'm doing it on a Monday, but I'd really hesitate to do it any later than that, unless there's some

## 05:39

really compelling medical or other personal reason. So yeah. So we'll talk more about the exam

## 05:46

when I am back in person on Wednesday or Friday. All right. So let's dive in. So last time,

## 05:57

looking back, I think two major things that we discussed. One was the form of the neutron flux

## 06:04

at the low energies. And that form is given here, E times the exponential of minus E over KT,

## 06:12

where K is the Boltzmann constant, T is the temperature of the medium. Now this distribution

## 06:18

popped out of a purely scattering medium. And what I said is it's an okay approximation to

## 06:24

increase the effective temperature to handle things like absorption, which tends to shift

## 06:30

the spectrum from the left to the right, so-called spectral hardening. All right.

## 06:34

This is just an approximation, right? The actual solution, numerical computation of the thermal

## 06:41

spectrum requires that we have detailed scattering laws, but it is possible, right? That there are

## 06:47

computational methods, but the basic shape is pretty well captured by this Maxwellian distribution.

## 06:54

All right. And then putting it all together, we now have an idea of what the spectrum looks like

## 07:00

across all energies, right? From the lowest energies, this Maxwellian, through the

## 07:04

resonance range, where we have one over E, or possibly the narrow resonance approximation. And

## 07:10

then at the fast energies, we have a flux that looks a heck of a lot like that Chi spectrum

## 07:14

of neutrons emerging from fission, right? Now, what we're going to do is take the spectrum

## 07:20

and apply it to a couple of questions. The first one, I'm actually going to start with the end in

## 07:26

mind, as it were. There are two sections in the book to read, 3.5 and 3.6. 3.6 is a couple

## 07:33

paragraphs. It's very...

## 07:34

very straightforward, and it defines what K-infinity is. And so I'm going to start with

## 07:38

that, and I'm going to then go backwards and decide, or describe how we compute effective

## 07:44

cross-sections. And then to do that numerically, we're going to have to have some way of handling

## 07:49

the spectrum over all energies, right? Because we've got these three separate functional forms.

## 07:55

And part of the homework for today, and maybe it was Friday's homework, I asked you to put together

## 08:04

a spectrum using some sort of continuity conditions to go from the thermal to the

## 08:09

epithermal to the fast. It's not a unique solution, right? There are many possible ways to combine

## 08:17

these forms together, and I'll show you one way today that we can then use to compute these

## 08:22

effective cross-sections, okay? So K-infinity, right? So we talked about K earlier on, and K is

## 08:30

what we call the multiplication.

## 08:36

Factor. And I've drawn out a cartoon where we have one neutron going in. It produces maybe

## 08:43

two neutrons or three neutrons from fission. Maybe one of those goes on to cause fission,

## 08:48

and the others just get absorbed, right? And so early in this chapter, there was this quantity

## 08:55

eta that was introduced as a function of E, and this specifically was the ratio of the number

## 09:06

of neutrons going in. And so I've drawn out a cartoon where we have one neutron going in,

## 09:06

and this specifically was the ratio of the number of fissions, sorry, the number of neutrons

## 09:10

emitted per fission divided by the absorption, right? So basically, this is the number of fission

## 09:18

neutrons emitted per absorption of any kind, and it's an energy-dependent function. You had to

## 09:25

look at this for the last homework. Pretty straightforward. It gives us at least a first

## 09:30

glimpse of what we could do to define a multiplication factor sort of from the ground

## 09:36

up without, you know, resorting to cartoons, an actual quantitative way to do it. But the

## 09:40

challenge with eta, as described in the book and as written here, is it depends on energy, right? So

## 09:45

we need just one number, ideally, right? One number to represent the number of neutrons that

## 09:56

we get per neutron absorbed, okay? And that's, in fact, exactly what k infinity is. Earlier,

## 10:02

when we talked about the multiplication factor, we said that the

## 10:05

multiplication factor is equal to the number of neutrons in generation n plus one divided by

## 10:15

the number of neutrons in generation n, okay? This is with the assumption that every fission

## 10:26

generation has sort of the same time period, and if it's in steady state, we basically have the

## 10:33

number of neutrons all the time.

## 10:35

If we have more neutrons on the average per generation, then k will be greater than one,

## 10:40

and our population will be increasing. And if it were less than one, of course, our population would

## 10:47

go down to zero, okay? Now, this infinity symbol is important because that means that we have

## 10:53

no leakage from the system, which means that the only way that neutrons can be lost is by

## 11:02

being absorbed, right? So neutrons can be lost by being absorbed, right? So neutrons can be

## 11:05

only be absorbed. So if neutrons can only be absorbed, then my question to you is, for this

## 11:21

number of neutrons born in generation n, what happens to them? And when does that happen?

## 11:31

Any ideas? You can go ahead and unmute, just speak up. We'll be informal here.

## 11:48

I'll pick on Alex. Alex, are you out there?

## 11:58

I think he's in the classroom, and that one doesn't have a mic.

## 12:02

Okay. All right. Who is just speaking?

## 12:05

This is Danny.

## 12:07

Do you want to go ahead and answer on Alex's behalf?

## 12:10

Yeah. Out of that generation, they're kind of getting absorbed in like an n-gamma reaction or

## 12:17

disappearing and becoming multiple neutrons in fission.

## 12:21

Right. So of these neutrons, so if we,

## 12:24

view the fission process as an absorption process where the neutron is lost, but then we get these

## 12:31

two new ones or three new ones for the next generation, it sounds like what you're saying

## 12:35

is that all of these neutrons in generation n are absorbed.

## 12:39

Yes. Yeah. And that makes sense,

## 12:41

because we only have, absorption is a way for neutrons to die. So then the second part of the

## 12:47

question is, when are these things absorbed? So that's maybe a tough question, but conceptually,

## 13:02

if we are expecting the neutrons that come in generation n plus one to be caused by fission,

## 13:09

that means that those, those absorptions are happening in that generation to produce those

## 13:14

neutrons. Because remember we get, we get neutrons almost immediately out of the fission event.

## 13:18

And so what I'm claiming is that this number of neutrons that is born in generation n becomes

## 13:24

the number absorbed in generation n plus one.

## 13:30

Right.

## 13:31

Right.

## 13:31

Generation n plus one. So another way then to write this k infinity is not as a ratio of the

## 13:39

number of neutrons in successive generations, but rather as the number of neutrons in, let's say,

## 13:51

let's say born in generation n plus one, use that word born as sort of a gains term, a production

## 14:01

term. And then over the number,

## 14:04

of neutrons absorbed or lost in generation n plus one. And then once we've written it like that,

## 14:17

it doesn't really matter if we're talking about a full generation, it doesn't matter which

## 14:21

generation we're talking about. We're really just considering a Delta T, a certain period of time.

## 14:28

And if we're talking about the number born in a certain amount of time, or the number lost in a

## 14:34

certain amount of time, what we're really talking about then are the reaction rates corresponding

## 14:39

to each of those things. So what this means is that this is the rate of neutron production divided

## 14:53

by the rate of neutron destruction. Or if I wanted to use really concise language, it would be

## 15:08

gains over losses, right? That's usually how in my mind, I define K, it's gains over losses.

## 15:16

And put in this way, it actually gives us an easy pathway to add back other ways for neutrons to be

## 15:23

lost, right? We're making the assumption here that neutrons can only be absorbed, that the system is

## 15:28

infinite, so that there are no boundaries for neutrons to go through and never come back.

## 15:32

But when we write it like gains to losses or rate of neutron production to rate of neutron
destruction,

## 15:37

we can start looking at it in a different way. We can start looking at it in a different way. We can

## 15:37

start adding back pieces to that destruction. Like we have a certain number of neutrons leaving

## 15:42

the boundary of a reactor per second. Well, that's a destruction, right? From the system,

## 15:46

because we're not going to get it back necessarily. That's where we would put things

## 15:50

like reflectors and so forth, but that takes us into the spatial domain, which we're going to

## 15:53

cover in the last third of the course. But this idea of gains to losses is important. And for

## 16:00

this infinite reactor, we already have the mathematical terminology to define it sort of

## 16:07

explicitly.

## 16:07

Right. And what that looks like then is the number of neutrons produced per fission times the

## 16:18

number of fissions happening per second and per centimeter cubed if we want to be volumetric. And

## 16:23

so what that looks like is, hey, we've got a new bar and we know that new bar is a function of E.

## 16:32

And we know that the fission rate is the fission cross section, which is also a function

## 16:37

of E. And then we have the flux, which is a function of E. Okay. That's our reaction rate.

## 16:45

But the problem is because that's an energy dependent function, right? It's per EV. We

## 16:51

don't want per EV. We want the total number of neutrons produced everywhere in our infinite

## 16:57

system. And that means overall energies. So we take the integral from zero to infinity over

## 17:06

energy.

## 17:07

Right. And we can do the same thing in the denominator for the absorption there for the

## 17:13

destruction. And so the destruction being only from absorption, we can do the same thing where

## 17:18

we integrate over the absorption rate, which is sigma A, which the A here, remember combines the

## 17:28

N gamma, the N fission, anything else that removes the neutron. Right. And so this will be a
function

## 17:35

of E.

## 17:36

So what's interesting when we look at it like this, there's a definite analog between what I've just

## 17:47

written for K infinity and what we had seen before for what I was calling the reproduction factor,

## 17:53

eta. Now, eta will show up again as a single number when we discuss the four factor formula.

## 18:00

And in that scenario, it's been averaged in some way over the spectrum, just like you had to explore

## 18:06

in the last home. For thermal reactors, it'll be averaged over the thermal spectrum for fast

## 18:12

reactors. I've never actually seen it shown in a textbook type setting, but we will average it over
the

## 18:18

fast spectrum, basically the range of energies where we expect the neutrons to be doing the good

## 18:25

stuff for us, causing fission.

## 18:27

But for now, what we have is this definition of K infinity. And as written, this is totally fine.

## 18:34

This is this is useful.

## 18:35

It gives us a way to.

## 18:36

Interpret the ratio of gains to losses.

## 18:42

But the challenge is we would like to be able to define K infinity without having to use these
integrals or having the

## 18:51

integral show up.

## 18:52

And so what what I'm proposing is that instead of writing it as this integral, it would be really
nice if we could

## 19:00

just do this.

## 19:01

We could say, hey, we've got a new sigma f.

## 19:05

We're going to put a bar over the hole.

## 19:06

Thing. And then we're going to put that multiplied by phi over a bar over sigma a times phi.

## 19:18

Where when I write phi without the energy, I mean that phi is equal to the integral from zero to
infinity or whatever.

## 19:27

We choose our lower and upper bounds to be of phi of e d e.

## 19:32

So we would call this the total flux.

## 19:37

Right. The energy integrated flux.

## 19:40

Okay.

## 19:40

And once we write it in this form, because we've integrated away energy, these things cancel out.

## 19:46

And so we're left with this ratio of new bar.

## 19:52

There's actually I should be careful.

## 19:53

There is a separate bar over the new right over sigma a.

## 19:59

Okay. Now, if this were a system with just one new slide, then of course, the sigmas would become
lowercase sigma microscopic values.

## 20:07

But if it's.

## 20:07

A mixture, we can write it as macroscopic.

## 20:12

Okay.

## 20:14

And this is this is what we're after.

## 20:17

We would like for our infinite homogeneous system to be able to define these so-called effective
cross-sections so that if we have a total flux, we are able to compute the the multiplication factor
k infinity.

## 20:34

Okay.

## 20:34

So what we'll do now is kind of.

## 20:37

Look at mathematically, how do these effective cross-sections get defined?

## 20:42

Right. Any questions?

## 20:44

All right. Doesn't seem like it, right?

## 20:53

So this is basically a summary of chapter three, section six, that short one that I was talking
about in Lewis, which builds on the section three point five that discusses effective cross-sections
throughout the three major energy regimes that we talked about.

## 21:10

Okay.

## 21:10

So I'm going to start off.

## 21:12

With what we.

## 21:14

Started off with for this whole chapter, which is the spectrum equation or the slowing down
equation.

## 21:20

Okay.

## 21:20

So we started off talking about K effective or ADA in our case, and then dove into this balance
equation for neutrons coming out of fission, possibly slowing down, getting to thermal energies and
such.

## 21:34

And that balance equation was this thing here, right?

## 21:37

So I called it slowing down if we were only caring about slowing down the neutrons, but the spectrum
equation might be more accurate here.

## 21:44

So.

## 21:44

So we wrote this down before we understand the different pieces, right?

## 21:48

The, the left-hand side Sigma T times Sigma as Sigma T times fee is our rate at which neutrons are
removed from energy.

## 21:57

E okay.

## 21:59

That's good for the balance equation, but for our K infinity above really what we'd want is the rate
at which neutrons are removed from the system.

## 22:07

Okay.

## 22:08

And so in order to put this balance equation.

## 22:11

In a single sort of like, you know, balance.

## 22:14

Of total loss rates, total scatter rates, total fission rates, et cetera.

## 22:18

We're going to integrate both sides over E from zero to infinity.

## 22:23

And remember, anytime I do zero to infinity, it could be our 10 to the minus three EB up to a 10
MEV.

## 22:31

I'll leave it as zero to infinity just to make it slightly easier notation.

## 22:36

Okay.

## 22:36

So when we integrate that left-hand side.

## 22:40

From zero to infinity, Sigma.

## 22:43

T.

## 22:45

E fee of E.

## 22:48

D E.

## 22:50

This is.

## 22:52

Our let's say total.

## 22:56

Total interaction rate.

## 23:00

Now, once we've done this integration, we can't really consider it.

## 23:05

All losses, right?

## 23:07

Because we know that a neutron loss from some energy E shows up.

## 23:13

Possibly at some lower energy.

## 23:15

If it's down scattering or.

## 23:16

A higher energy, if it's up scattering.

## 23:18

So it's better to call this the total interaction rate.

## 23:22

When before at a certain energy, it really was the, the, the removal rate of neutrons from a certain
energy.

## 23:28

Okay.

## 23:29

Now what I'd like to be able to do is write this as follows.

## 23:32

So Sigma T.

## 23:34

Bar times fee.

## 23:36

Okay.

## 23:37

Where again, fees, my total flux.

## 23:38

So if we, if we force.

## 23:41

This equivalence between the integral on the left-hand side and this simple.

## 23:45

Product of one number Sigma T bar times fee, another number.

## 23:50

This gives us it right away.

## 23:53

How to define Sigma T.

## 23:55

And it's as easy as solving for it, which means that we divide both sides by the total flux.

## 24:01

So that means that Sigma T.

## 24:04

Is equal to this integrated.

## 24:08

Total interaction, right?

## 24:12

P of E.

## 24:14

D E.

## 24:15

Divided by fee, the total flux, which.

## 24:20

We defined before as the integral of fee.

## 24:25

He from our lower bound to our upper bound.

## 24:28

Okay.

## 24:29

And if you look carefully, what this is doing is.

## 24:33

Taking our total cross section as a function of E it's a function of E.

## 24:39

And what we're doing is computing expectation value.

## 24:43

With some probability density function.

## 24:45

For E.

## 24:47

And if we look at it like that, that means that our probability density function, this weighting
function that we're using is actually equal to fee of E.

## 24:57

Scaled by.

## 24:59

It's total value.

## 25:02

Right? So in essence.

## 25:06

If you remember our constraints on a probability density function.

## 25:12

It has to be positive, but not negative everywhere. It can be.

## 25:13

It has to be positive, but not negative everywhere. It can be.

## 25:15

It has to be positive, but not negative everywhere. It can be.

## 25:15

It has to be positive, but not negative everywhere. It can be.

## 25:15

Zero, of course.

## 25:16

So it just has to be non negative everywhere.

## 25:18

And it's integral over the appropriate range is equal to one.

## 25:22

Well, if we take the of E or of course that might be a huge magnitude, but if we.

## 25:27

Divide by its integral, this normalizes it so that it is a bonafide probability density.

## 25:34

Function. And so that's, that's when we compute this effective cross section or what the book refers
to as an energy average cross section.

## 25:42

What we're really doing is computing an effective.

## 25:44

Sorry. An.

## 25:45

Expectation value, right?

## 25:49

So that that's how we define it.

## 25:51

And we, without loss of generality, we can take this T and turn it into an X, right?

## 25:56

So for any reaction X, the effective cross section is equal to.

## 26:04

The integral of that cross section as a function of energy times.

## 26:09

V of E D E.

## 26:12

Over this total flux.

## 26:15

Okay.

## 26:16

That is.

## 26:18

Sort of the.

## 26:19

Idea of an effective cross section in a nutshell.

## 26:23

Okay.

## 26:24

Now this is over the entire energy range, right?

## 26:28

This does not stop us from doing something like.

## 26:32

E of sub X and.

## 26:37

I'll say common G.

## 26:40

That's not, that's not a good.

## 26:48

Oh, no.

## 26:49

Oh, what was that?

## 26:50

All right.

## 26:51

Control Z.

## 26:52

Okay.

## 26:53

Let me get rid of.

## 26:54

Just do that.

## 26:58

Okay.

## 26:59

Sorry.

## 27:00

It was supposed to be a Sigma.

## 27:01

Not.

## 27:02

Okay.

## 27:03

All right.

## 27:04

So I can define a reaction, an effective reaction cross section for reaction X, and I'm going

## 27:09

to index it by this additional G.

## 27:11

And what I mean by this G is I can take that integral and say that I can integrate it from

## 27:21

E.

## 27:22

Of G minus one.

## 27:24

To E of G.

## 27:26

But it's the same.

## 27:28

Integrand.

## 27:29

Right.

## 27:30

The stuff inside of the integral will be still that function Sigma X of E times fee of E.

## 27:36

D E.

## 27:37

But now that normalization that we had before is no longer the total flux over the entire

## 27:43

energy range.

## 27:44

It'll just be.

## 27:45

The total flux.

## 27:46

Over this.

## 27:50

Interval.

## 27:51

Of energies.

## 27:52

From E G minus one.

## 27:54

To EG.

## 27:55

Okay.

## 27:56

And what I mean, what I mean by this EG minus one to EG.

## 28:02

It's something like if I took our energy range.

## 28:05

Of, you know, zero to infinity or whatever our upper bound is, and I chopped it up.

## 28:12

Right.

## 28:13

So maybe.

## 28:14

This is E G.

## 28:17

Minus one.

## 28:18

And this is E of G.

## 28:20

Okay.

## 28:21

That's.

## 28:22

That's going to be the way that we define.

## 28:24

The total flux.

## 28:25

Of energy.

## 28:26

And so.

## 28:27

We're going to be using cross sections for the two group approximation,

## 28:30

which is what we'll cover on Wednesday.

## 28:32

And then we can extend this to any number of groups that we want.

## 28:35

Just as kind of a.

## 28:36

A big picture view of this.

## 28:38

When we get cross section data from the NNDC or wherever our,

## 28:42

our source of end of data might be.

## 28:44

In order to use that data in deterministic.

## 28:47

Code.

## 28:48

So not Monte Carlo.

## 28:49

I'm talking about codes that will actually take the slowing down.

## 28:52

Of the energy.

## 28:54

Of the energy.

## 28:55

Of the energy.

## 28:56

Of the energy.

## 28:57

Of the energy.

## 28:58

And then we can use the full on neutron transport equation and solve it.

## 29:01

We have to take that continuous energy representation,

## 29:03

sort of the tabulated cross sections that we get from.

## 29:05

You know,

## 29:06

NNDC.

## 29:07

And average it in these energy bins that are called groups.

## 29:11

And so for.

## 29:13

A lot of practical applications.

## 29:15

We might.

## 29:16

Use several hundred to several thousand groups.

## 29:19

At the smallest scale,

## 29:20

small spatial scales,

## 29:21

you know,

## 29:22

And then we can use that to.

## 29:24

I guess.

## 29:25

Whittle it down then ultimately to say two groups.

## 29:28

It turns out that two group analysis was sort of the bread and butter

## 29:32

of reactor analysis throughout the eighties, maybe even the nineties.

## 29:36

As computer power has grown,

## 29:38

it's become more common to use a better fidelity approach in energy.

## 29:43

And even continuous energy now with computers being able to handle the

## 29:48

Monte Carlo, but.

## 29:49

There's still a lot.

## 29:51

Of that.

## 29:52

You know,

## 29:53

One of the things that we're seeing is that we're looking at the

## 29:55

intersection of energy.

## 29:56

Domain.

## 29:57

And we're seeing that.

## 29:58

We're seeing that some of the energy that is contained by reducing this

## 30:01

energy.

## 30:02

Domain from, you know,

## 30:03

10 to the minus three all the way up to 10 me on a continuum.

## 30:06

Down to just a few bins. Right. And so we'll, we'll see.

## 30:08

The impact of that on, on Wednesday and Friday.

## 30:12

So.

## 30:13

This handles the cross section.

## 30:15

Like Sigma T or Sigma.

## 30:17

A something that is just strictly a function of energy.

## 30:20

Right. Remember, we have the other things here. I'm just going to highlight what happens when we
take this thing and integrate it over that range.

## 30:28

Right. So if we have that scattering integral, this is what we start with.

## 30:34

Sigma s from e prime to e times phi of e prime d e.

## 30:42

Right. That's what we start with on the right hand side. But now I'm saying, hey, let's integrate
that over e.

## 30:52

From zero to infinity. Now, remember, the scattering cross-section that shows up in that integral is
a function of e prime going to e.

## 31:02

Right. So if we take this this integral of e, we can actually just integrate away this dependence.

## 31:09

Right. So what we end up with is zero to infinity of sigma s of e prime phi e prime d e.

## 31:21

OK, so that's just.

## 31:22

By definition. Right. What we're saying, what we're doing is going from this cross-section that
handles the probability of going from e prime down to some other e or up to some other e.

## 31:32

And we're integrating away all of the possible outgoing energies. Right. Because we can take the
flux and multiply it by that integrated scattering cross-section.

## 31:41

And what that does is it tells us about the number of neutrons scattering at energy e prime rather
than the number of neutrons scattering at e prime that then scattered down to some other energy.

## 31:52

Right. So.

## 31:52

Different quantities. And so once we get it in that form, again, we can take this integral, set it
equal to some effective cross-section at e prime for scattering and multiply that by the total flux.

## 32:07

So basically, any of these cross-sections can be captured in the same way.

## 32:13

I'll wait till Wednesday, possibly Friday, to work on how we will represent this entire group.

## 32:21

Or group to group or energy to energy cross-section and sort of this energy bin or multi-group
format.

## 32:28

Right. We don't need it now, so I'll leave it till then.

## 32:31

OK.

## 32:32

Any questions about that?

## 32:42

All right. So the concept is simple.

## 32:44

And for this case where we're integrating over the entire energy range, it doesn't seem too
complicated.

## 32:51

Right. It'll be good. We'll have to work on the mechanics a bit more on Wednesday when we add an
additional energy group.

## 32:59

Right.

## 32:59

Rather than going over the whole energy domain.

## 33:01

But still, there are some practical considerations for for computing these.

## 33:06

Right. Because we still have to compute integrals of this form.

## 33:11

Right. We still have to be able to take some spectrum that we have, multiply it by some cross-
section that we have to compute that that total numerator.

## 33:20

And then we can do the same thing for the flux itself.

## 33:23

And that will give us the value.

## 33:24

So it probably pays to look a little bit.

## 33:29

At some computational examples so that you have a handle of how you would actually do this.

## 33:35

So let me go ahead and open up my browser here.

## 33:39

So I've started.

## 33:41

Sketching out a solution.

## 33:44

A couple of things here that should help with today's and probably even last week's stuff.

## 33:49

OK, so what I'm doing is defining functions for the spectra in each of the energy regimes of
interest.

## 33:51

So let me go ahead and open up my browser here.

## 33:52

Right. So I've started.

## 33:53

Sketching out a solution.

## 33:57

A couple of things here that should help with today's and probably even last week stuff. Okay. So
what I'm doing is.

## 33:58

Defining functions. Britney Speck.

## 33:59

interest for a thermal spectrum reactor. We'll hopefully get a chance to explore some fast

## 34:05

reactor spectra as time goes on. But for now, we'll worry about the thermal spectrum reactors

## 34:10

because we emphasize this slowing down to the thermal domain. So we have the thermal spectrum

## 34:18

here as the Maxwellian. I've chose, so here's an approximate Boltzmann constant. I'm taking

## 34:26

the temperature to be 900, which is a little high, but I've chosen that to sort of push it

## 34:32

over to the right so it matches the 1 over E curve a little bit more easily, right? You'll

## 34:39

explore a different way to do that in the homework, okay? And for the epithermal flux,

## 34:44

I'm being simple for the moment and doing 1 over E. And then for the fast flux, I'm using

## 34:49

a model for the chi spectrum that I believe we've seen before with

## 34:56

the

## 34:56

hyperbolic sign, right? There are a couple of different ways to do it, but that's what I'm

## 35:00

doing. And notice that I don't have any constants in front, right? I'm going to treat the
normalization

## 35:06

constant as part of my graphing process, okay? The other thing that I'm doing is I'm loading the

## 35:12

same cross-section data that I've done before, and I'm using as a total cross-section a combination

## 35:19

of the uranium-238 total cross-section and the hydrogen total cross-section, so something very

## 35:25

similar to what you're seeing here. And I'm using the same cross-section data that I've done before,

## 35:26

so something very similar to what you're seeing here. And I'm using the same cross-section data that

## 35:26

you've been working on for the homework, where you have a mixture of these two things.

## 35:29

And then to make the narrow resonance spectrum, I'm taking that total cross-section

## 35:37

and creating a function based on interpolation. So I got all of the energies from the cross-section

## 35:43

data. I unionized them, which means putting all the cross-sections onto the same energy grid,

## 35:50

which of course is also done by interpolation. But here I'm doing that so that now I have this

## 35:55

function phi nr, which is the energy grid, and I'm using the same cross-section data,

## 35:56

that can be evaluated at any energy, and what it'll return is 1 over e times sigma t of e for

## 36:03

this particular mixture of materials. I could have done it differently, but I think this is a

## 36:09

good starting point. So now I've got basically two options for my epithermal spectrum. Now I'm

## 36:16

going to plot these things, and I'm going to plot each of them separately. And you'll notice I have

## 36:21

some pretty wild constants out in front. And the way that I chose these constants,

## 36:26

is just by eyeballing the graph. What I've tried to do is make it so that the Maxwellian

## 36:33

intersects the 1 over e spectrum at about 1 e v. It's not perfect, and you'll see what I've done

## 36:41

to kind of fix that up later on. And then also so that the 1 over e meets up nicely with the

## 36:47

chi spectrum at about 0.1 m e v, right? So it's totally heuristic. It's totally based on my

## 36:54

visual judgment. So I'm going to plot these constants, and I'm going to plot each of them

## 36:56

separately. And there's a different way to do it is what I'm having you do for the homework,

## 37:01

where you actually enforce continuity by using the slowing down, which should end up probably

## 37:07

giving you something that looks a lot like what I have here anyway. Okay, so I'm going to go ahead

## 37:11

and show what this looks like, if I could go ahead and define all these first. Okay, right. And so

## 37:19

what I've done is I plotted all four of those curves. So we've got the red curve here is the

## 37:24

Maxwellian. And then I've plotted all four of those curves. So we've got the red curve here is

## 37:26

the Maxwellian. And then I've plotted all four of those curves. So we've got the red curve here is

## 37:26

the Maxwellian. And it crosses the black curves at roughly one e v, which are the one over e and

## 37:31

then the narrow resonance spectrum approximations, respectively. And then over here at roughly 10 to

## 37:37

the five e v or point one m e v, I've got the black curve meeting up with the blue chi spectrum,

## 37:45

the dashed line is the narrow resonance. And because of the value of the total cross sections

## 37:51

at those higher energies being because they're lower, the one over e,

## 37:56

it kind of creeps up a little bit, but not too far off. One thing that I haven't told you about yet

## 38:04

is something that you've seen in the book. And actually, I'll wait for a moment and fix my graph

## 38:13

a little bit by putting in the appropriate label. So this is the spectrum as a function of e, right?

## 38:23

And that should be clear. And then my x axis is, you know, I don't know, I don't know, I don't know,

## 38:26

I don't know, I don't know, I don't know, I don't know, I don't know, I don't know, I don't know.

## 38:26

The energy e and e v. Okay. Now, what I'm going to do is I'm going to take these three curves

## 38:32

or four curves, I'll choose one of the intermediate flux spectra, and I'm going to combine them in

## 38:37

such a way that I can take any energy e and get back the appropriate value of the flux. So I'm

## 38:42

going to try to find a way to smooth out a way to link up the red curve, black curve in the blue

## 38:49

curve. And what that looks like is as follows. I'm going to have the spectrum function that takes an

## 38:54

e, right? I'm going to have the spectrum function that takes an e, right? I'm going to have the

## 38:56

spectrum function that takes an e, right? I'm going to make an array that has the appropriate

## 39:00

number of values. And then I'm going to define a temporary variable that is the thermal spectrum

## 39:06

at all the energies, right? We know that we're going to toss away a lot of the values because

## 39:10

the thermal spectrum is not what we're using beyond one e v. So what I'm doing here is I'm

## 39:16

filtering it. This nomenclature here is I want to take all the energies e that are greater than one,

## 39:23

I'm going to take their location or their indices,

## 39:26

and those indices of my temporary are going to be set to zero. So basically, this is saying that,

## 39:31

hey, take that thermal spectrum you just computed and toss away any values for energies greater than

## 39:37

one e v, okay? I can do the same thing for the thermal, sorry, epithermal spectrum. So I'm going

## 39:45

to use the same phi epi that I had before. I'm using the same normalization constraint that I

## 39:51

had before the 0.01, okay? And then I'm going to toss away all the values that are greater than

## 39:56

all values that are here less than a half e v rather than the one e v. I'll show you why in a

## 40:01

moment. And then I'm tossing away all the values greater than 0.1 m e v, right? And then I can do

## 40:07

the same thing with the fast. I'm going to toss away everything less than 0.1 m e v. So this is

## 40:12

one way in Python, although similar, you can do it similarly in MATLAB or Octave using this sort of

## 40:19

filtering process. This will give me an entire array that uses values from the appropriate

## 40:26

value. So I'm going to toss away everything less than 0.1 m e v. So this is one way in Python,

## 40:26

although similar, you can do it similarly in MATLAB or Octave using this sort of filtering process.

## 40:26

So this is one way in Python, although similar, you can do it similarly in MATLAB or Octave using
this sort of

## 40:26

spectrum. I guess I could call them. Okay. So I'll go ahead and do this. And then here's what it

## 40:31

looks like, right? So I've made it, remember, this is a log-log plot. So any sort of aberrations,

## 40:38

any funny things are actually quite funny, right? Anything that looks sort of small on a log-log

## 40:45

plot is on a linear scale, usually pretty large. So you see this little glitch here and a little

## 40:50

glitch there. On this plot, totally fine. If you were to look at this on a linear scale,

## 40:56

it would look probably a little strange, okay? If I, instead of using 0.5 as my cutoff here,

## 41:04

went to what we had said is our thermal cutoff of 1 e v, that changes things substantially,

## 41:11

right? And what that does is it causes the Maxwellian to be used further to the right

## 41:18

than sort of our engineering judgment would want it to be, right? And so we could do a couple

## 41:24

things. We could try to do something.

## 41:26

Some sort of averaging between the 1 over e and the Maxwellian. Realistically, for our purposes,

## 41:33

it doesn't matter. As long as we get it to look sensible, it's about right, okay? So I'm going

## 41:40

to keep it like that. And that's our flux spectrum. Now that we have the flux spectrum as a function

## 41:46

of e, we are able to multiply that point-wise with cross-sections evaluated at the same energies.

## 41:55

And if we can do that...

## 41:56

That gives us the integrand of the integral that we need to evaluate for an effective cross-section.

## 42:03

But you've already done that sort of computation before. You've just, for one of your homeworks,

## 42:08

had to compute an effective eta value over one or another region of energy, right? So you can

## 42:15

use things like the trapezoid rule. If you had those functions, you could use the built-in quad.

## 42:20

But it's something that you can do numerically, right? And that's the cool thing about having

## 42:25

access to the real data.

## 42:26

Data is we can just compute these things directly, right? Rather than having to look up values from
a

## 42:31

table in the back of the book, which is a procedure and modality of instruction that I just, I don't

## 42:39

like because I don't like calling around big books with tables in the back, okay?

## 42:45

The one thing that I was mentioning before that I want to show you that you've seen

## 42:48

in the book that I haven't done is to plot the flux rather than as a function of energy per unit,

## 42:56

energy, but rather as a per unit lethargy. So in the previous homework, you had to deal a little

## 43:03

bit with this separate quantity called lethargy, which is related to the energy. Really what the

## 43:10

lethargy does is that rather than having this one over E and sort of this exponential, basically

## 43:18

rather than having to look at the flux on a log plot, the lethargy lets you do it on a linear

## 43:23

scale. But there's a pretty simple trick. And it's one over E, and it's one over E, and it's one
over E,

## 43:25

and it's one over E, and it's one over E, and it's one over E, and it's one over E, and it's one
over

## 43:26

E. And if I take the spectrum E, right? So this is my phi of E. If I take that and I multiply it

## 43:34

by E, what I end up with is a picture that looks like this. This is the same thing as if I had

## 43:41

converted that spectrum from phi of E to phi of U, where U is equal to the log of E over E.

## 43:56

Right? So E0 being some, sorry, E0 over E. Yes. Right? So this is the definition for the lethargy

## 44:10

that you've seen in the book, where E0 here would be our maximum system energy, like 10 MeV or

## 44:14

something like that. So if I were to do that, that change of variables, which we've seen we can do

## 44:19

for probability densities, but we could do it also for phi. So if I got phi of U, what I would get

## 44:25

is a plot that looks like this, which is the same thing as phi of U. So if I got phi of U, what I

## 44:27

would get is E times phi of E. In this format, things are sometimes easier to see, but there's

## 44:34

another reason that this is an important way to be able to look at the flux or reaction rate or

## 44:41

a cross-section. And it's because on a log-log plot, typically the areas under a curve from one

## 44:48

energy to another energy are totally unequivalent areas. And that makes sense because the area

## 44:54

under a curve on a typical log-log plot, the width of a delta is the area under a delta.

## 44:57

So if I were to draw a rectangle, it's going to have a really narrow width because I'm at lower

## 45:03

energies and it's log-log, right? So I'd be at 10 to the minus one or something from here to here,

## 45:10

roughly one EV would be this width, right? Whereas if I go over here on a regular log-log plot,

## 45:16

I would be having a width of 10 to the five, 10 to the six, whatever it might be. So by converting

## 45:22

to this E times phi of E, which is equivalent to the flux per unit lethargy, all of these

## 45:27

areas under the curve are equivalent, right? So plotting any of these energy dependent functions

## 45:35

as per unit lethargy is a good way to compare sort of relative total integrals, which for

## 45:44

these effective cross-sections is a pretty useful thing to do. So I challenge you to go look in the

## 45:49

book and find a picture that looks like this. And you'll see that there is a spectrum in chapter

## 45:55

three that looks a heck of a lot like this one.

## 45:57

Here, which is exactly what we get when we take this sort of spectrum and multiply it by E, okay?

## 46:05

So that is everything that I wanted to talk about today. As I said in the beginning, we're going to

## 46:11

take this concept of the effective cross-section and apply it to the two-group formalism. There's

## 46:17

nothing in the book specifically about two groups. In the book, the effective cross-sections are

## 46:22

generated at thermal, intermediate, and fast. We're going to tackle it with everything below

## 46:27

about one EV.

## 46:27

Being thermal and everything above that being fast and come away with some simple expressions,

## 46:34

not only for K infinity, but for certain quantities that we'll see even later on as

## 46:40

parts of the four-factor formula. So any questions? Doesn't sound like it. So that will be it for

## 47:00

today. I appreciate you guys hanging in with me while on travel, and we will pick up this discussion

## 47:08

on the next one. Thank you.

## 47:08

I appreciate you guys hanging in with me while on travel, and we will pick up this discussion on

## 47:08

Wednesday live in person. I see something for the chat will pop up. Cool. All right. Then have

## 47:21

yourselves a good day, and we'll catch up in a couple days.

## 47:25

Thanks.

## 47:25

See ya.
