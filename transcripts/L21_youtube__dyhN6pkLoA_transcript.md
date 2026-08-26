# L21 Local Audio Transcript

Course: NE 630

Playlist source: https://youtube.com/playlist?list=PLy481lNHlnHoEO95vM-xYX2bydD25v20L

Video: NE 630 - Lesson 21

URL: https://www.youtube.com/watch?v=_dyhN6pkLoA

Video ID: _dyhN6pkLoA

YouTube upload date: 20231013

Duration: 57:17

Transcript source: Local faster-whisper transcription from YouTube audio.

Whisper model: large-v3; detected language: en.

Generated: 2026-06-28

Note: This transcript is machine-generated from audio and lightly wrapped only. It should be reviewed before being quoted, published, or used as polished lesson text.

Requested language: en

## 00:00

there's uh there's office

## 00:02

like what is it that i use

## 00:18

actually stays with us

## 00:33

not showing is charging which is bizarre because

## 00:36

yeah i don't know why but anyway we'll we'll proceed all right are there any questions from

## 01:01

last time i know it was a little um jumbled at the end trying to use uh the the jupiter notebook

## 01:11

what i did for you is i went back and i finished the last couple of cells

## 01:16

in the notebook to show you what what you can do with the uh unit cell class uh i think matt had

## 01:23

let's see matt yeah but he had pointed out or asked a question a good one uh if openmc has

## 01:30

documentation for using the stuff and my immediate response was well we're using the unit cell class

## 01:36

we're like sort of avoiding the openmc um api or let's say functions directly but if you notice

## 01:45

when i did something like pwr.unit cell i'm sorry i've just started pwr.fuel it returned

## 01:52

i'll speak of the devil

## 02:03

no

## 02:09

let's see if i have uh

## 02:15

uh let's see all right to give you an example of what i'm talking about

## 02:29

um

## 02:29

when we create the the unit cell that uh with the lwr unit cell pwr is an object it's of that

## 02:38

class that i made for you that hides a lot of the openmc stuff but some of its attributes like

## 02:43

pwr.fuel that's that's an openmc object that's a that's a material definition right so matt

## 02:49

i called you up because you had asked me a good question last time like is there documentation

## 02:54

for the openmc stuff and i said the class that i have is my own you can look at the code but

## 02:59

actually store some of the openmc stuff there is a lot of useful um you know things that you can do

## 03:04

so pwr.fuel is an openmc material object so necessarily that has all the stuff that defines

## 03:11

that material so for instance pwr.fuel.density returns the mass density so in our case that'll

## 03:17

be the 10 grams per cc you can also do pwr.coolant to get nuclide atom densities and what that
returns

## 03:26

is a dictionary a python dictionary which is in this case just a

## 03:29

mapping of string names so h1 u238 whatever to the number density that we're looking for right and

## 03:36

there's some other things there so i guess the the correct answer to your question would have been

## 03:42

yes there actually is documentation for openmc i don't think it's as robust as say the the numpy or

## 03:49

sci-fi or some of these other things that have been developed but uh you can definitely inspect

## 03:53

that um what i'm hoping is that i give you enough by way of example that you don't have to dive in

## 03:59

i do expect or i wouldn't be surprised if there are some of you who are just interested in you

## 04:04

know playing around and doing a little bit more uh whether you get into some undergrad research

## 04:08

or you're just interested in exploring something a bit more um so anyway if you run into something

## 04:13

where it's like huh i wonder if i could be able to do this but i can't find anything just ask

## 04:18

it but i can point you in the right direction it seemed like the openmc user guide wasn't like

## 04:23

particularly helpful but the help functions uh were yeah so that that's actually a good

## 04:29

a good uh point so if i do openmc documentation right i'll come here they have all the stuff

## 04:37

online so the user guide is more of a let's say a big picture overview of how to do it and the

## 04:46

the reason that it's organized the way it is is the openmc input structure is all based on those

## 04:51

xml files you don't really see them i mean you probably saw them in your folder after you ran

## 04:56

openmc but they adopted the xml

## 05:00

way of doing things years ago like over a decade ago what they've added since then was this really

## 05:06

uh pretty fully functioned python api when i say api i don't want it to be all jargony do you know

## 05:13

what api means have you heard that term do you associate it with how to use something it basically

## 05:22

what so api stands for application programmer interface which is this

## 05:26

just with like a stupid overbearing phrase right

## 05:29

It just means all the functions that some code gives you, right?

## 05:32

So if I'm using the OpenMC API, what I mean is when I import it,

## 05:36

the API is all of the functions that I can call.

## 05:38

It's my way of interacting with the engine, as it were, right?

## 05:42

So if you want to learn how to use the stuff on the Python side,

## 05:46

it's all under the Python API.

## 05:47

So Alex, where you say that the user guide is probably not so great,

## 05:51

for what we're doing, it's not.

## 05:52

The Python API is probably what you want to do.

## 05:56

And when you do...

## 05:56

I cannot click on that.

## 05:57

Yeah, and when you do help on the things that you would have been calling help for,

## 06:02

it's going to tell you the same stuff that this has.

## 06:05

So anyway, I point that out for, I guess, completeness sake.

## 06:10

The last little bit of this lesson 20 that I did,

## 06:14

let me blow it up just a little bit so you can see.

## 06:17

I think we got to this point, we did some stuff.

## 06:20

And then basically, I'm just filling out all of those coefficients

## 06:24

that show up in the books expression

## 06:27

for the Python API.

## 06:27

For the resonance escape probability.

## 06:29

And once I plug things in,

## 06:31

I end up with this value of minus 2.482 PCM.

## 06:37

And that's actually not totally correct

## 06:40

because that should be per K.

## 06:41

So I wonder, will that run again?

## 06:44

I'll have to rerun the whole thing.

## 06:46

So the coefficient is always a reactivity

## 06:50

per whatever your temperature was.

## 06:53

And then the last thing I put in there,

## 06:54

which could be useful for the homework,

## 06:57

is if you take the finite difference approach,

## 07:02

you go from that derivative of D rho D,

## 07:04

whatever you're changing,

## 07:05

the finite difference looks like this

## 07:07

and you can expand it to K,

## 07:08

you end up with this.

## 07:11

And so that's probably something that you'd need for, yeah.

## 07:16

Did you mean to have the number of batches equal to a million

## 07:19

or the number of particles?

## 07:21

The number of particles.

## 07:23

Did I say batches?

## 07:24

You have NG on there,

## 07:25

which is referencing batches.

## 07:27

So you can, yeah, my bad.

## 07:34

Yes, we, at least we did the math and it took about 10 and a half days.

## 07:43

Yeah, I apologize, that's a typo.

## 07:45

So NG is a parameter, that's for generations.

## 07:48

So I mean, you can basically the number that what we're going

## 07:52

for is a large enough total number of neutrons being simulated.

## 07:55

You can break it up into generations or you can either increase

## 07:59

the number of generations for a fixed number of particles

## 08:01

per generation or increase the number of particles

## 08:04

for a fixed number of generations.

## 08:06

For our problem, the difference will be small.

## 08:09

The reason that it's broken up like that is there are some problems,

## 08:14

big problems that have big spatial dependence.

## 08:17

Ours has some spatial dependence, but it's not very much.

## 08:19

Okay. For if you're doing a full core, like a full PWR,

## 08:23

where you have all 193 assemblies, the spatial dependence is incredibly,

## 08:29

very important, right?

## 08:31

Remember when I made the simulation, I had to assume something about the

## 08:35

very first neutron generation and I said that they all were born at the origin.

## 08:39

And then for the first several generations, I think five in my case,

## 08:43

we discard all of the information and that's to build up a steady

## 08:49

state spatial distribution, right?

## 08:50

So if you just put your reactor and you put a point source in the middle,

## 08:55

the next generation will have diffused away from that point source and then

## 08:59

the next generation thereafter will have diffused until it reaches some sort of steady state shape

## 09:03

right so just like we've used open mc to come up with the spectrum of neutron energies that i've

## 09:10

called the steady state or the critical spectrum there will be a critical spatial shape too we

## 09:15

haven't touched that stuff that's what we'll do in the last third of the course but for open mc

## 09:20

and the simulation process that it uses you need to iterate until that spatial distribution hits

## 09:26

its sort of equilibrium um shape and so for big problems you have to increase the number of

## 09:32

generations to make that happen for our problem it's so small you can just keep five active

## 09:38

generations and include it so uh for how many people did that really cause a big issue or did

## 09:43

you did you come up with the did you figure out that i made a small mistake yeah okay or no sorry

## 09:51

yeah okay so i mean is it going to help anybody if i just say turn this in

## 09:56

on

## 09:56

sunday night instead raise your hand if that makes any difference okay lindsey for you you can

## 10:04

you can we can we can do it on sunday night right so then then you can reflect on this week and say

## 10:10

is this week actually getting worse and worse and you can say no because jeremy on friday said i

## 10:16

could just turn it in later and so the week is getting better you're welcome so go ahead and

## 10:21

if you've already submitted stuff great if you need a little bit of time uh to correct for for

## 10:26

the issue that was just mentioned i'm going to go ahead and i'm going to go ahead and i'm going to

## 10:27

issue that was just pointed out by all means do it because i have zero intent of grading things

## 10:32

tonight um and i don't want the computational stuff to be last minute because i know it can be

## 10:37

it can be um frustrating in fact last night um i will we'll get to the numbers but i wanted to see

## 10:47

what the uh coefficients for the sodium uh cooled fast reactor were doing basically the same sort of

## 10:53

pin cell model and just adjusting the temperatures and doing the finite difference

## 10:56

so what i'm going to do is i'm going to go ahead and i'm going to go ahead and i'm going to go ahead

## 10:56

and i'm going to go ahead and i'm going to go ahead and i'm going to go ahead and i'm going to go
ahead

## 10:56

and i'm going to go ahead and i'm going to go ahead and i'm going to go ahead and i'm going to go
ahead

## 10:57

So what I found is that, or what I was trying to do is I went to 50 generations with 10

## 11:02

million particles per generation and on a 20 core instance on, on demand, that takes

## 11:08

roughly an hour, right?

## 11:09

But because of the way that I wanted to do it, I was looping through all the plutonium

## 11:13

fractions.

## 11:14

I wanted to see how the coefficient changed as a function of how much plutonium was in

## 11:17

there.

## 11:18

So I looped it and being everything in a Jupyter notebook or in Python, I was just having a

## 11:23

heck of a time getting everything deployed.

## 11:25

And so I finally did it this morning, but even, even then the statistics were pretty

## 11:30

bad.

## 11:30

So I'd have to go to higher numbers of particles.

## 11:33

So the finite for, I think for the LWR, it'll work just fine.

## 11:36

But I think for the sodium cooled fast reactor, the uncertainties are just a lot higher.

## 11:44

Question.

## 11:44

With the SMR, are we supposed to make an assumption on your dual radius pitch and

## 11:51

I think, what was the question that I had you do for that?

## 11:55

Uh, was that, was I asking you to come up with the coefficients?

## 11:59

I think so.

## 12:00

Yeah.

## 12:00

Yeah.

## 12:00

So fuel and cooling, the reason for that was because like, there's a lot of different SFR,

## 12:06

like design possibilities and whereas like PWR to BWR, they're going to be pretty similar

## 12:12

as far as your fuel.

## 12:13

Yeah.

## 12:14

So I think of all the SFR, um, and similar, it doesn't just have to be sodium.

## 12:19

It could be lead or others that the dimensions of the fuel is about what we've seen, right?

## 12:24

So there.

## 12:25

They tend to be a little bit smaller than the light water reactor fuel elements, but

## 12:28

that the order of magnitude is about the same.

## 12:30

So you could use the defaults for that, or you could choose what I had done in an earlier

## 12:35

lesson, which might actually be the defaults.

## 12:38

I can't think that's what, what that is.

## 12:40

What I did is I use the, the, the, from, from the previous lesson, it wouldn't let me run

## 12:44

it, uh, without putting something in, but they don't, so far don't have, it does not

## 12:50

have a default value, but for some reason they seem to be coded different because it

## 12:54

has default values.

## 12:56

You can run the health function, but you have to put them in for whatever.

## 12:59

And should I say that?

## 13:00

That's probably, I was probably doing that at midnight one night before there are people

## 13:06

though.

## 13:06

There are default values.

## 13:07

They just aren't included by default.

## 13:09

Oh, yeah.

## 13:11

I probably listed default values.

## 13:13

And if I didn't, if I didn't actually put that in the arguments, then the documentation

## 13:17

from the health is wrong.

## 13:19

I mean, basically what you're doing is you're giving me a lot of feedback for, for doing

## 13:23

it.

## 13:23

Like I would love to turn.

## 13:24

It in to a full-fledged module that I can use, um, in the future.

## 13:29

Uh, you're seeing, you're seeing it in a, an alpha version, right?

## 13:33

So I appreciate the feedback, but you're able to get it to work.

## 13:36

Did you see coefficients that were even remotely sensible?

## 13:42

Okay.

## 13:42

All right.

## 13:43

So I'll, I'll give some numbers as we go along today and we can talk more about that.

## 13:46

The SFR stuff, uh, I even pointed out that to, to really do a detailed analysis of the

## 13:51

reactivity coefficients is we have, we need more.

## 13:54

Stuff we, it, uh, turns out that the, the most important pieces of the reactivity feedback

## 14:00

in a fast reactor are something that happens only at the large scale with spatial effects

## 14:05

included.

## 14:06

Okay.

## 14:07

Um, all right.

## 14:08

So let me, oh, my computer is now charging.

## 14:12

Nice.

## 14:13

Nice of it to, uh, do that.

## 14:15

Okay.

## 14:16

So, um, so last time, yeah, what we talked about was reactivity and the units that we

## 14:22

used to describe reactivity.

## 14:23

And then the all important reactivity coefficient, which is really just a derivative, right?

## 14:28

The sensitivity, uh, of the reactivity to some change in, uh, a parameter and the parameters

## 14:34

that we cared about in that I'm asking you to, to assess numerically are the temperature

## 14:39

of the fuel and the temperature of the coolant or moderator.

## 14:43

Um, so in the whitewater reactor case, the coolant and moderator, of course, that's the

## 14:47

water.

## 14:48

So in the book, you'll see the subscript M and I'll use that when describing the PWR

## 14:52

stuff here.

## 14:53

Okay.

## 14:53

So the final thing that we took away, um, before we wanted to, to do some, uh, numerical

## 14:59

evaluation was to get this coefficient so that the moderate, uh, both, both the coefficients

## 15:05

for fuel and for the coolant or moderator, usually given the letter alpha, right?

## 15:11

That's just a common thing, um, that I've often seen in the literature.

## 15:15

And so equation nine 16 gives us this simplified expression for the fuel temperature coefficient.

## 15:21

So you'll sometimes see the acronym.

## 15:23

Um, the FTC, not federal trade commission, but fuel temperature coefficient.

## 15:32

And the key things here that it's a function of this thing called gamma bar, which is some,

## 15:38

it's a correlation and it has two constants and it depends on the, um, the density and

## 15:44

diameter of the fuel.

## 15:45

And then it depends on the resonance escape probability, importantly evaluated at 300 K

## 15:52

or room temperature, right?

## 15:53

Because where we get the, the value of the resonance escape probability comes from the

## 15:58

resonance integral.

## 16:00

And that was what we discussed a little bit last time being, uh, generated from an experiment

## 16:07

where they actually looked at a UO two fuel rod of varying sizes and computed what that

## 16:13

resonance integral is, the effective resonance integral for that geometry.

## 16:17

Okay.

## 16:18

When we use open MC to actually compute a K value, we don't need any of that, right?

## 16:23

We're getting the.

## 16:23

What we, what the book has is this very simple expression based on, on some, uh, integral

## 16:29

experiments for getting that.

## 16:31

And that's, what's plugged into here.

## 16:33

And then we get the, we account for the new temperature by way of the square root, um,

## 16:39

that shows up, right?

## 16:39

So when we put that all in, uh, as we actually just saw in the slides, we'll, we'll end up

## 16:49

with fuel temperature coefficients that are, you know, basically.

## 16:52

In the range minus two to three PCM per Kelvin.

## 16:59

And so that's a pretty typical range of value then really smacked down in the middle of

## 17:03

that is what we'd expect for a typical pressurized water reactor.

## 17:08

What I'd also said last time is that value is, uh, you know, it's reasonably large, um, and

## 17:15

it's negative.

## 17:16

It's a, well, I always have a negative Doppler coefficient or fuel temperature coefficient.

## 17:20

When the term fuel temperature.

## 17:22

Coefficient and Doppler coefficient are usually interchangeable.

## 17:26

And the reason for that is the fuel temperature coefficient is driven by the Doppler effect.

## 17:30

As those resonances widen, it's basically widening the range of energies that neutrons

## 17:36

can land in as they slow down.

## 17:38

Right.

## 17:38

And so the other thing that happens with that is you remember the idea of self-shielding.

## 17:44

Well, if the peak of my cross section goes down because it's broadening, that means that

## 17:48

the flux in the middle of that, that resonance is not.

## 17:52

As, uh, reduced as it would be right.

## 17:55

So remember now resonance where you have the flux is proportional to one over the cross

## 18:00

section.

## 18:00

Well, if that peak of the cross section has been reduced because the resonance is, is

## 18:05

spreading as a whole, well, then the flux depression is going to be less.

## 18:09

The self-shielding effect is going to be reduced.

## 18:11

And that stuff that we talked about, like self-shielding leads to less absorption is

## 18:15

going to be undone.

## 18:16

So when we have the temperature increase, we actually lose that self-shielding so that

## 18:21

the actual absorption.

## 18:22

The absorption rate goes up.

## 18:24

Okay.

## 18:25

That's where the feedback comes from.

## 18:27

So if our temperature goes up, maybe because our power has gone up, the, uh, Doppler broadening

## 18:32

widens, those resonances, the flux, uh, dip goes down and we actually see an increase

## 18:38

in absorption.

## 18:39

And that absorption of course, is in the resonance of the due to 38, which means that our

## 18:43

reactivity goes down, right?

## 18:45

We're losing neutrons.

## 18:46

I could ultimately get down to the thermal energies, pause vision, uh, in your new two

## 18:50

35.

## 18:51

Okay.

## 18:52

Um, so what we'll talk about today is the moderator temperature coefficient or MTC.

## 18:57

And then, uh, at the very end, a little bit on excess reactivity and reactivity defects,

## 19:02

and this will all lead into what we'll start next time.

## 19:05

Uh, you'll read 10.1 and 10.3.

## 19:08

It'll seem sort of like an off topic where we discuss Xenon and Sumerium as, uh, poisons

## 19:15

that build up when a reactor is first started up.

## 19:18

So we're going to get into the time domain starting on Monday.

## 19:22

Uh, but.

## 19:22

The way that I'm breaking it up is we'll, we'll cover chapter 10 before we go back to

## 19:26

chapter five.

## 19:27

And the reason for that is even though we're incorporating time dependence, what we are

## 19:33

not doing is assuming that the flux or the neutron population is changing in time.

## 19:37

All we're caring about right now is the time change of nuclide concentrations.

## 19:43

Okay.

## 19:43

So we'll start off with the things that evolved pretty quickly, which is Xenon and then Sumerium,

## 19:48

but then we'll also take that and understand how the fuel.

## 19:52

It's self changes in time.

## 19:54

So we know that uranium two 35 visions.

## 19:56

So it produces a bunch of things.

## 19:58

It could be Xenon.

## 19:59

It could be Sumerium.

## 20:00

We know that uranium two 38 will absorb neutrons and turn into ultimately plutonium two 30.

## 20:06

Not right.

## 20:07

So you've got this evolution of actinides that is very, very important to understand,

## 20:12

to basically to understand that it lets you know why, for instance, Wolf Creek is refueled

## 20:20

every 18 months.

## 20:21

Okay.

## 20:21

We'll be able to do.

## 20:22

That and then whether it's next, it'll probably be the week after we'll talk a little bit

## 20:26

about something called the linear reactivity model.

## 20:30

Right.

## 20:30

So we're basically sticking with this, this concept of reactivity.

## 20:34

We're going to add a little bit of time and then we'll come back around to chapter five

## 20:37

and see how the neutron population itself changes in time over very small time intervals.

## 20:43

Right.

## 20:43

We're we're kinetics and dynamics are important, right?

## 20:48

But let's wrap up with the reactivity.

## 20:52

Let's see.

## 20:56

All right.

## 20:57

So the moderator temperature coefficient.

## 21:01

First of all, I want you to consider our simple model for the eigenvalue K for multiplication

## 21:06

factor, four factor formula.

## 21:08

Right.

## 21:09

Where does the moderator explicitly show up in these four factors?

## 21:13

We've got four factors in the four factor formula.

## 21:17

We've seen an expression for these in the books and you've played around a little bit in that
Jupiter notebook.

## 21:22

In which of these four factors does the moderator show up explicitly as some part of the, the, the
expression?

## 21:33

What's that?

## 21:34

Yeah.

## 21:34

P and F.

## 21:36

Right.

## 21:36

So we know that F, let me maybe change my, right.

## 21:45

So we have the F, which is the thermal utilization.

## 21:48

Um, I'll write it in the sort of the simplified form that the book has.

## 21:53

Uh, which is similar to what I've done before.

## 21:57

Uh, I'm terrible with that Greek letter, right?

## 22:01

And this is the fuel volume.

## 22:04

And then we have moderator, Sigma a, T and then the fuel, right.

## 22:18

Okay.

## 22:18

This remember the little squiggle.

## 22:20

I can't even remember which letter it is.

## 22:22

That's the, the disadvantage factor.

## 22:24

So that's the ratio of the moderator flux to the.

## 22:27

Um,

## 22:27

to the fuel flux okay so if we look at this thermal utilization we've got one over one plus

## 22:33

this this term the ratio of the volumes and then the ratio of the macroscopic absorption

## 22:40

cross-section so uh and then the other one noted was was p right the resonance escape

## 22:47

probability which the simplified expression that we've been using is this which essentially

## 23:01

equivalent to what i have covered in 400 right there's actually very little difference between

## 23:09

what what i'm doing in these uh the past couple lectures and what we did in 400 with the exception

## 23:14

of introducing the open mc stuff right so these are the the two factors that explicitly have the

## 23:19

moderator show up and by explicitly i mean it has a term that has the m label on it for moderators
so

## 23:25

that's the moderator absorption cross-section right the thermal cross-section and then the

## 23:31

same thing

## 23:31

for uh the scattering cross-section here and i should probably put the t for the thermal right

## 23:38

if we were doing the two group notation these would be the group two values right question

## 23:44

is uh in the denominator of that uh uh for p is that the slowing down decrement in the middle yes

## 23:53

so how does the moderator temperature show up in these two expressions

## 24:01

obviously it's not explicitly right but it it does show up implicitly

## 24:07

how the cross-section yeah so in both of these expressions we have a cross-section for

## 24:17

the moderator uh whether it's the absorption or the uh scattering cross-section so we'll just call
it

## 24:25

cross-section x for the moderator how do we define this thing it's just way back to week one or two

## 24:35

how do we define a macroscope

## 24:36

cross-section right so it would be n of the moderator times whatever the cross-section is

## 24:48

and then how do we define the number density

## 24:55

right so rho m times n a over whatever the molecular mass of the moderator is times

## 25:06

that so in the book that this the discussion of a

## 25:09

mass density basically how to compute the moderator temperature coefficient

## 25:14

begins and ends with the number density but i prefer to link it to the thing that we would

## 25:19

actually be looking up a change in and that's the mass density right that's this thing here so

## 25:26

you'll have to excuse my use of rho for two different things in this lesson we're using

## 25:30

it first for reactivity but we also often use it for the mass density so this is the

## 25:37

mass density

## 25:39

of in our case it's of water okay so when the when for our reactors everything is always under

## 25:50

constant pressure although the same arguments would apply i think if we didn't have constant

## 25:54

pressure so if our temperature of the moderator goes up then the terms that will change will have

## 26:00

to be the the sigma terms right whether it's the uh absorption cross-section here or the

## 26:06

scattering cross-section here and we know the thing that has to be actually changed

## 26:11

is the mass density so when i turn up the temperature of the water under constant

## 26:16

pressure what happens to its density say it decreases it decreases right because it gets

## 26:25

closer to the boiling point right so at least in that phase before we start having a steam

## 26:30

component or but i guess while our quality is zero uh we'd expect that density and i guess even if

## 26:37

our quality goes up then our density is falling even more rapidly right so in general we'd expect

## 26:42

temperature to go up density to go down

## 26:44

right so i can just summarize that here temperature goes up the density of our water goes

## 26:55

down okay so without even doing something quantitatively let's consider that f term

## 27:03

if i'm increasing my temperature the density goes down that means the number density goes

## 27:08

down that means my cross-section goes down what does that do to f i'm taking i have one

## 27:15

over

## 27:15

one plus this term this term is proportional to my density so if this thing goes down

## 27:23

what happens to f increase you go up and what does that mean what's happening if the density of the

## 27:33

water is going down that means there's less what's happening in the water less absorption right
which

## 27:39

means that fractionally there's more happening in the fuel right that's what fuel is it's telling me

## 27:45

something about the probability of thermal neutrons doing their business in the fuel

## 27:49

so if f goes if t goes up rho is down f goes up okay that doesn't tell me though the whole story

## 27:58

about the reactivity though right because f is just one part of the of the product okay

## 28:08

what about p if i increase the temperature rho goes down right so my cross-section goes down

## 28:16

that means that i have e to the negative something that's getting

## 28:20

increased so that means that p goes down which makes some sense if i have less moderator than

## 28:27

i'd expect so we can't say right off the bat which of those effects is going to dominate that they

## 28:32

seem to be going in different directions right so we can't say what's happening to the reactivity

## 28:38

and this should make you think then back to the question i posed on monday

## 28:41

what where do we operate the reactor on that p over d curve

## 28:46

and we'll get back to that in just a moment all right so

## 28:54

where's my number two okay so in the book uh actually there's really not much of a derivation

## 29:01

but i thought i'd sketch out a little bit of how i would and and ultimately did solve this problem

## 29:08

so if i want to figure out how f actually changes beyond just kind of eyeballing it like we just did

## 29:14

what i would do is write f like this where it's one

## 29:16

plus one plus one over one plus uh a constant c i don't care what c is yet but i'm just saying that

## 29:23

it's c times rho right so i'm identifying that that thermodynamic term that is going to change

## 29:29

when i change the temperature right and then we know that the reactivity uh coefficient is a sum

## 29:35

is that i guess as a reminder we have the whatever our our reactivity coefficient is so d

## 29:43

rho dt uh in this case moderator this is going to be equal to one or approximately equal to one

## 29:50

over k dk dtm right and then we broke this up into the four components from the four factors so

## 29:59

because we we think that only p and f are relevant we would have

## 30:03

one over p dp dtm plus one over f

## 30:12

f

## 30:13

d f dtm right so what i'm doing first is for f and then i'll do it for p on the next uh page

## 30:20

i'm just looking for these um i guess you have what we call these logarithmic derivatives

## 30:26

basically the derivative divided by the the quantity okay all right so in this form it's

## 30:38

it's quite a bit easier to do the derivative rather than trying to take around all those

## 30:42

other terms and so what you end up with which is equivalent to what's in the book

## 30:48

is this o dtm over rho

## 31:01

h2o okay now it's this thing that actually connects us to the thermodynamic properties

## 31:11

because this thing is equal to minus beta m where beta m is the volumetric coefficient

## 31:27

of thermal expansion so you've all had thermodynamics you probably have i actually

## 31:42

know i think we've gone away from having a gigantic book and you probably have a small

## 31:46

book with online resources or something like that so is this term volumetric coefficient

## 31:51

of thermal expansion something that you've heard before right so it basically is telling you that

## 31:58

if i change the temperature the relative change in the volume is some number so

## 32:04

the relative change in the volume is going to be minus the relative change in the density

## 32:08

because they're inversely related which is why there's that minus sign now for our uh

## 32:16

operating regime of a pwr so for a pwr the pressure is on the order of 15.5 mega pascals

## 32:26

which roughly is like 150 atmospheres okay so very very high pressure and the temperature

## 32:34

of the water it varies of course because we're adding heat to it from the beginning or the inlet

## 32:41

of the core to the outlet of the core but sort of an average value is uh by 300 c or roughly 600

## 32:49

kelvin you'll notice i drop all the time 20 degrees here and there but for our purposes

## 32:56

that's um that's fine okay so this for for these um for this you know pressure in that

## 33:04

temperature this is about minus 2.9 times 10 to the minus 4 uh per kelvin right because it's

## 33:20

per kelvin because we're it's not an absolute volume change or an absolute density change it's

## 33:25

a relative change in that quantity yeah do you all feel like you have a a like a go-to source

## 33:33

for getting a number like that my guess is you would look get up on

## 33:40

google and you'd probably find yourself at engineering toolbox because that's what happened

## 33:44

to me i wasn't super satisfied with their interface for that because i i like to proselytize

## 33:52

programming and the use of python and such i thought maybe i would

## 33:56

take a very quick look here so there's uh this is kind of messy but

## 34:06

there's a module called iap

## 34:10

pws which is an acronym that has to do with some uh consortium that evaluated water and steam

## 34:17

properties but you can do you can install it very uh very easily here's the the page for iapws okay

## 34:26

if you want to get it on your own system you can do pip install iapws so for if you're using on

## 34:32

demand you could go into the terminal the same place that we had done the install of openmc

## 34:38

you could do

## 34:40

activate openmc-env to be in that same environment where you have numpy and all that

## 34:45

stuff and just type in pip install iapws and then you'll have the the thing um that i'm showing here

## 34:53

and what's neat is it has this this um this class called iapws97 which is water uh it's a steam

## 35:04

table right it's a just a class that represents the steam table so for 300 kelvin 15.5

## 35:10

um mpa i can get alfav which is this beta that i'm talking about i don't even know what the five

## 35:17

letter acronym would be here but when i get that i get 0.00289 blah blah blah and just as a sanity

## 35:24

check i'm like well this is for the volume this is not for row how would i verify that it actually

## 35:30

gives me or that minus that gives me the change in row well i can compute

## 35:35

row i i started perturbing temperatures and things just to see how sensitive it was right

## 35:40

So for 14.5, and then I'm doing a finite difference, so I use temperature 302 minus the density at
300, divided by, why did I divide by 2?

## 35:54

What is that about?

## 35:56

Oh, 2, that's my delta.

## 35:58

So I'm taking my density at 302 degrees minus the density at 300 degrees, dividing it by 2, and then
dividing it by my density at 300, because it's a relative change.

## 36:11

And lo and behold, the number I get, it's off just a little bit, right, because it's a finite
difference, but it's the same number, right?

## 36:18

So you can rest assured that the volumetric coefficient of thermal expansion is minus the
corresponding change in density.

## 36:28

Okay.

## 36:28

So that's more of a sanity check and sort of highlights that there is a steam table built into
Python if you install it, which is pretty cool.

## 36:36

OpenMC behind the scenes, when we use the LWR unit cell, water is set as the coolant.

## 36:42

And behind the scenes, it's using something like this to account for the change in the density as a
function of temperature, right?

## 36:48

So you get the density change automatically from OpenMC without having to think about it.

## 36:57

All right.

## 36:57

So just like we can do for F, do the same sort of thing for P, and where did I go here, right?

## 37:18

So the resonance escape probability was E to this ratio of fuel quantities divided by moderator
quantities.

## 37:27

Again, we can just put all that other stuff into a constant D.

## 37:31

Then if you were to actually do the derivative things that you can recognize were P,

## 37:35

you can do the derivative things that you can recognize were P,

## 37:35

you can do the derivative things that you can recognize were P,

## 37:35

and it's not so hard to convince yourself then that the expression we're after is this,

## 37:47

the rho H2O DTM, where again, this thing shows up, and that's the minus beta M.

## 38:02

So when you take this expression for 1 over P DTM, put it with the 1 for P,

## 38:11

you end up with the moderator temperature coefficient looking like this.

## 38:20

And this is exactly what's in the book, right?

## 38:36

What's neat is because of the sort of simplified expressions that we're using for each of the four
factors,

## 38:42

all we really need to know in addition to the sort of original four factors that we start with,
right?

## 38:48

So if I say, hey, compute the reactivity coefficient for this PWR,

## 38:52

at you know this operating condition if you've already had to compute k for that problem you

## 38:59

already have p and you have f you would just need this beta value right which would be given and

## 39:04

then you have access to the moderator temperature coefficient right all right so let's do

## 39:15

an exercise if we have p is equal to 0.6 which is reasonable for a pdvr uh at you know sort of

## 39:27

operating like full power conditions f equal 0.95 and using the same beta term of 2.9 times 10 to

## 39:35

minus 4 per kelvin let's determine alpha m in units of pcm per k so just take a few minutes

## 39:42

i'll scroll up just a little bit so you have this amazing

## 39:47

amazing

## 39:47

basically you're just plugging and chugging but i want to make sure that you can get it into

## 39:51

pcm per k that's helpful

## 39:55

remember that 2.5 times 10 to minus 5 or 2.5 pcm

## 40:06

right so for that

## 40:24

instead of taking a native sign out and just like getting better

## 40:32

uh no um you could definitely do that i think so

## 40:39

it's sort of like the obvious it's like it's easy to recognize the log of one over p when going for

## 40:49

the derivation and that's actually how then the book will use it so the book has the same expression

## 40:53

but you're absolutely right you're out of time

## 40:58

awesome

## 40:59

i would agree yeah

## 41:02

yeah

## 41:05

good point

## 41:08

is that what you're talking about yeah i think i think that that's right

## 41:24

oh yeah oh wow do we have any numbers

## 41:34

so uh where's my

## 41:42

i got did i did i hear minus 13 yeah pcm per k that's what i got as well

## 41:52

yeah so minus 13 pcm per k it's a little bit larger by a factor of five times larger than

## 42:02

the fuel temperature coefficient does that seem like does that make sense does it is that

## 42:08

surprising i don't know if it should be surprising but think about it this way even though it's a
bit

## 42:14

larger the range of coolant temperatures that we'd expect to see in the reactor it's pretty small

## 42:20

right so if our inlet temperature is say 280 degrees c

## 42:24

you're going to get a lot of coolant in the reactor and you're going to get a lot of coolant

## 42:24

we get a maximum delta t of maybe 50 degrees in the core right it's we don't have a human working

## 42:30

range of temperature because of the property it's water so at maximum we'd expect a change

## 42:36

um you know from during operations of you know maybe maybe you know tens of degrees now if you

## 42:43

incorporate from startup right where you're at cold conditions at you know roughly 30 degrees c

## 42:48

or something room temperature then it's a bit bigger but the fuel temperature always ranges

## 42:53

quite a bit more right because our

## 42:54

typical fuel temperatures uh about 900 c or 1200 k right so much much larger changes in the fuel

## 43:01

temperature right uh so before we move on to the sort of the very last thing what does this mean

## 43:09

about the p over d curve right so if you remember kind of like cartoon wise we had k infinity

## 43:16

versus p over d and it looks something like this it varied depending on the temperature

## 43:23

so if we had k infinity um and it looks like this if you were looking at it under waypoint

## 43:27

it's probably going to be k 10 and sometimes it can be k 15 and then it can be 10 to the

## 43:32

time that we're talking about so that's the he's the the term right so if we had k infinity

## 43:36

and we had k infinity and we went a little bit further up we can say yeah we could get

## 43:44

k infinity we can go down and have k infinity with a k infinity right but if we went a little

## 43:49

further up we could get some k infinity off of k infinity and there's the difference the

## 43:52

number of k infinity over k infinity goes up of k infinity right because k infinity is

## 43:54

the number of k infinity touched up not 10 to the time that it goes up so that's kind of

## 43:55

alpha equal minus 13 pcm has to be under moderated why because your alpha m is bigger than your

## 44:03

your alpha f or the alpha f shouldn't play a role here but i agree that it's under

## 44:10

right so why is it under moderated if you think about it p over d

## 44:21

is something like it's not exactly equal to but there's a relationship between p over d

## 44:30

and the volume of the moderator to the volume of the fuel right if p over d is very large that

## 44:37

means that relatively speaking we have more water than we do fuel right if we keep increasing that

## 44:43

which is why the curve tends to go down the further right we go more water means more

## 44:49

absorption f is going down okay but if p over d it kind of has a correspondence to the volume

## 44:56

of the moderator to the volume of the fuel that means that

## 45:00

if we decrease the volume of the moderator for you know fixed operating condition we'd be going

## 45:06

to the left on the curve right well what's one way to change the moderator volume to heat it up

## 45:14

right or maybe the volume is fixed but its density goes down right so but it's the same impact here

## 45:20

so if i increase the moderator temperature and reduce its density that's the same effect as going

## 45:26

from the right to the left on this p over d right i have if my density moderator goes down

## 45:32

then the amount of moderator to fuel goes down so i go to the left if i'm in this over moderated

## 45:38

regime what happens to my k infinity if my temperature of the moderator the water temperature

## 45:48

goes up it's going to increase is that what i want no i mean at the like what just who cares

## 45:59

about what i want what that would mean is alpha would be positive right now generally i don't want

## 46:05

any of my alpha to be positive right so i'm going to increase the temperature of the water

## 46:06

to be positive because usually the changes that are happening are are maybe not things that i

## 46:13

want basically i always want negative feedback negative feedback coefficients lead to stabler

## 46:18

dynamics but if i'm in this over moderated regime if for whatever reason i have a a spike in the

## 46:25

power eventually that energy gets out into the coolant if the coolant temperature increases and

## 46:31

that leads to an increase in the reactivity then i'm going to have this sort of

## 46:36

sort of

## 46:36

self-driving power increase it'll happen on a time scale that's that's you know minutes as opposed
to

## 46:41

being instantaneous but still not something that i want to deal with if i were right at the optimum

## 46:47

you might think that's really good because then i have a very large reactivity somehow i'm using

## 46:50

my neutrons the best way possible well if i'm right at the top then the derivative of this

## 46:55

thing is zero which that corresponds to alpha equals zero which means that the temperature

## 47:01

of the moderator has no impact which means i don't get the negative feedback okay is that

## 47:06

bad no but um the closer you are to optimum or to the right hand side means that that you might

## 47:14

actually go over to the over somewhere in your operating regime right because we know that in

## 47:18

time our fuel the fuel composition changes and so forth so the reactors that we have in practice

## 47:25

operate in this under moderated regime right and the reason for that is that leads to a coefficient

## 47:31

that is negative so for typical pwrs the the range is from

## 47:36

you know a few pcm per k to about minus 30 pcm per k you might think to see values as as high in

## 47:44

magnitude as minus 80 right but this is a between let's say 10 to 30 or minus 10 to minus 30 pcm per

## 47:51

k is pretty typical for this quantity yeah um so is it true then that your alpha is not always

## 47:58

negative for basically like going from cold shut down to like yes there there are some there are

## 48:06

uh regimes where it can be slightly positive that's not usually what we want um that the nrc has

## 48:14

regulations to dictate what those magnitudes can be i'm not an expert on on the regulatory but in

## 48:21

general we we want it to be negative yeah right um yeah so i gave a a link to the maple reactors

## 48:29

which i i hope you get a chance to look at it was uh some they were interesting in the sense that

## 48:35

they were for radioactivity and they were for the radioactivity and they were for the

## 48:36

isotope production but when they did their experiments they mispredicted alpha right and

## 48:42

that it's not in their case it wasn't that they couldn't have positive value they couldn't

## 48:48

understand why it was positive based on their simulation and if their simulation is wrong for

## 48:52

that why should you believe the simulation for any other part of it right that was the case that a

## 48:57

a canadian reactor physicist a professor at um at montreal had made and that it makes a lot of

## 49:04

sense to me right

## 49:06

um all right very last well so i guess just to summarize here for the pwr this was like two

## 49:14

minus two to three pcm per k this is like minus 10 to minus 30 pcm per k for the sodium cooled

## 49:26

fast reactor this is on the order of minus 0.5 pcm per k and then for the coolant density effect

## 49:36

this is on the order of 0.5 positive pcm per k now remember here the sodium cooled fast reactor

## 49:43

that sodium is doing nothing for the reactivity uh in the way that water is water we need the to

## 49:50

slow down the neutrons the sodium is doing nothing except pooling the reactor so it represents

## 49:56

neutron poison right so when i decrease the poison right the the absorption i will always

## 50:03

increase my reactivity which is why this is a problem so i'm going to go ahead and show you

## 50:06

the the the reaction value of this reactor which is the positive value now you might look it's like

## 50:10

uh those are about the same order of magnitude don't they cancel out isn't your reactor like

## 50:14

just dynamically out of control turns out that these are not the primary factors right for

## 50:20

reactivities of a sodium-cooled fast reactor the primary ones are geometric the expansion

## 50:25

coefficients actually and actually and then radially right there are some other effects

## 50:30

about fuel elements bowing right under under the heated load especially on the outside because
they're

## 50:35

on the other side so they bow a little bit those are the more important factors but as you can

## 50:39

imagine that's really hard to do with a unit cell model right so that's not something that we can

## 50:44

touch um very last little bit about defects right so if we take a reactor from from its kind of cold

## 50:55

shutdown conditions along through its startup what i can sketch out the the pieces here right so

## 51:04

if this is our cold shutdown right that means that my tf equal t uh moderator equal 300k so

## 51:19

roughly room temperature okay if i remove my control elements right and i get to critical

## 51:27

we call it cold critical then my reactivity goes down a little bit because uh cold

## 51:35

critical or at my

## 51:37

critical

## 51:37

excess reactivity goes down and then one thing that is done is the pumps to cool an lwr are run

## 51:45

to get the water and the fuel to an equilibrium temperature of about 600 degrees k basically the

## 51:52

coolant temperature that you'd expect at full power so this is called hot zero power

## 52:00

and then we actually go down a little bit more and this is the um

## 52:07

this is hot full power okay now what i mean by the excess reactivity is

## 52:17

how like without any control how reactive is this fuel right as we go up in temperature

## 52:26

the fuel temperature coefficient tells us that we will go down in reactivity because of Doppler

## 52:31

broadening we also know that the moderator temperature coefficient is negative we'll go

## 52:36

down in reactivity we'll go down in reactivity because of Doppler broadening we also know that

## 52:37

So excess reactivity, like we always put more fuel into a reactor than we need because we have to
compensate for that very first fission.

## 52:45

So no matter what, we have to go in with K greater than one or reactivity greater than zero.

## 52:51

So by excess reactivity, I mean by how much more than zero is our reactivity.

## 52:57

So we have to compensate for these temperature changes. These are known as defects.

## 53:02

So this is getting all the way down to this point where excess reactivity is down here.

## 53:06

This is the power defect. So we would call this from power.

## 53:14

This would be from the isothermal temperature.

## 53:20

And then this is what we call the shutdown margin.

## 53:24

And that represents how much of that reactivity is being held down by the control elements.

## 53:30

The big question, though, for us and what we're going to explore starting next week,

## 53:35

is what do we do about this additional excess reactivity?

## 53:41

This is reactivity equals zero. That represents what we can do at steady state.

## 53:47

But if after all the temperature increases and so forth, we're still left with this excess
reactivity,

## 53:54

which, again, we need to if we're going to have more than one fission, how do we compensate that
during time?

## 54:01

Right. And that's one of the things that we'll cover next week.

## 54:06

And for PWR,

## 54:07

the answer is you mix some boron in the water, right?

## 54:11

For PWR, you don't put boron in the boiling water because boiling water with acid is pretty bad
because it's boric acid that's dissolved in the water.

## 54:19

So what do you do? You use your control elements and something called burnable poisons,

## 54:24

which are there in the fuel and they're burned along with the fuel at a slightly different rate to
keep this excess reactivity in check.

## 54:33

Right. You can't have too much. That's also something that the NRC.

## 54:35

There's guidelines for that. Right.

## 54:39

So that's one of the things that we'll cover during the next several weeks up through, I guess, when
our next exam is.

## 54:46

So thanks for sticking around for a few extra minutes.

## 54:49

And then, again, if you didn't get the homework in already or you want to go back and change
something, you have until Sunday evening.

## 54:58

I'll get that adjusted. All right. Have yourselves a good weekend.

## 55:03

What's that top region?

## 55:04

Shut down margin.

## 55:10

Yeah, so there's a similar figure in the book that I didn't like.

## 55:16

So I made my own variant.

## 55:18

We'll see that one book again, but when we get to that, I'm dependent on that.

## 55:22

I actually made those in the second public for the over-nominate graph of the factors.

## 55:27

So I found that I kept the diameter constant.

## 55:31

I got the value.

## 55:34

So that made the function, you know, there is a value.

## 55:39

I ran it like a hundred times in the bar.

## 55:43

I think it's starting to plateau right around there.

## 55:46

But if you're going forward, I think you're going to find that it increments down.

## 55:51

So it's plateauing at that.

## 55:54

That's okay.

## 55:55

Yes.

## 55:56

At some point.

## 56:01

Are you starting with those small?

## 56:03

Yeah.

## 56:04

Yeah.

## 56:04

Yeah.

## 56:04

Yeah.

## 56:04

Yeah.

## 56:04

Yeah.

## 56:04

Yeah.

## 56:04

Yeah.

## 56:04

Yeah.

## 56:04

Yeah.

## 56:04

Yeah.

## 56:04

Yeah.

## 56:04

Yeah.

## 56:04

Yeah.

## 56:04

I would expect it to hit a maximum and then come down.

## 56:10

Now, I haven't.

## 56:13

I would expect it to look something like that down.

## 56:16

If it's a little bit different.

## 56:19

And I don't.

## 56:22

Problem.

## 56:25

Right.

## 56:26

Right.

## 56:27

Moderator.

## 56:28

And I know that that doesn't.

## 56:30

The values that they give in that book might not be safe.

## 56:34

The values.

## 56:34

but it should capture at least some rain right um maybe worth it getting that rain

## 56:39

you could try it so uh you yeah definitely change your your step so that you can take

## 56:45

one giant step and kind of verify but um yeah i would expect it to go up and then come back down

## 56:52

how rapidly depends on a number of things um and this is again based on a very simple

## 57:00

yeah set of data so yeah i just wanted to get a better idea of what it should come out as right

## 57:04

i'm doing it right yeah okay um question so openmc it calculates the k values yep um for us is there
