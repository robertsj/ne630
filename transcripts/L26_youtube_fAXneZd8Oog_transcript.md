# L26 Local Audio Transcript

Course: NE 630

Playlist source: https://youtube.com/playlist?list=PLy481lNHlnHoEO95vM-xYX2bydD25v20L

Video: NE 630 - Lesson 26

URL: https://www.youtube.com/watch?v=fAXneZd8Oog

Video ID: fAXneZd8Oog

YouTube upload date: 20231025

Duration: 54:34

Transcript source: Local faster-whisper transcription from YouTube audio.

Whisper model: large-v3; detected language: en.

Generated: 2026-06-28

Note: This transcript is machine-generated from audio and lightly wrapped only. It should be reviewed before being quoted, published, or used as polished lesson text.

Requested language: en

## 00:02

So those of you who have had me in 495 know how I feel about parking.

## 01:01

You can imagine that I have similar opinions about things like inspections by the city, code
violations, things like fallen branches.

## 01:11

So I went out to Wally World yesterday to get some groceries, and I show up at my house to bring
back some frozen goods before going on to something else.

## 01:20

I see a yellow card on my door.

## 01:23

I'm like, what the hell is this?

## 01:25

Well, I go, it's from the fire department, which is where the inspection stuff is.

## 01:31

It's housed.

## 01:31

I've had them, like, come and say I've had long grass before, right, because that happened.

## 01:35

But this one was about specifically limbs and debris and so forth, and they circled limbs.

## 01:42

And it's like I have, like, a big branch that fell in my front yard out of the tree, right?

## 01:46

It's been stormy weather.

## 01:48

How the hell do we have a system where that's worth somebody's time to go do?

## 01:54

And what bothers me is they try to frame it in this way that suggests it's all about property.

## 02:01

It's all about property values and so forth, right?

## 02:02

Well, my property taxes continue to go up, right?

## 02:07

So my property value is going in the right direction.

## 02:10

So I'm not sure what they're worried about.

## 02:12

And then what bothers me even more is right there where this big branch has fallen, there's a big
missing chunk of curb, which, of course, is not my property.

## 02:21

That's the city's property.

## 02:22

And so I had to take my first angry little man emotions, bring them down a notch.

## 02:30

And then.

## 02:31

And write a nice, neutrally voiced email that said, Hey, is this what you're talking about?

## 02:35

And I put a picture where I circled the branch.

## 02:38

And then I said, if that's the case, okay, great.

## 02:41

But this other circled thing, which is the missing curb, when is the city going to take care of
this?

## 02:47

And I got a response back that was also equally neutral in tone and said, this is the person you
contact for the curb issue.

## 02:55

So I will do that.

## 02:56

But I was, it had this been two years ago or three years ago.

## 03:00

When the first half of my.

## 03:01

Time here, I would have probably blown up and had an aneurysm.

## 03:03

And so I'm working on myself, you know, anyway, all right, let's go ahead and get started.

## 03:14

So today we're going to extend what we did last time.

## 03:18

And primarily what we're going to do is not assume that multiplication is there.

## 03:24

We're going to bring back multiplication and get ourselves back to reactor systems.

## 03:29

Right. Without multiplication, we don't have changes.

## 03:31

The reactors.

## 03:32

Are going to be able to do that.

## 03:34

And so we're going to have to build a new structure for the reactor systems.

## 03:36

And so I'm going to go ahead and do that.

## 03:37

So let's get started.

## 03:39

So I want to point out, though, a couple administrative points, right?

## 03:42

There are now two assignments that are posted.

## 03:45

One is due on Sunday following pattern we've had for the past couple of weeks, and that will take
that will be the homework problems corresponding to today's lesson, Monday's lesson.

## 03:55

And then last Friday's lesson on the linear activity model.

## 03:58

Right.

## 03:59

So that wasn't in the homework that was just do.

## 04:01

I'll get the solution to the homework.

## 04:02

Okay.

## 04:02

that was just submitted, hopefully by the end of today, and I'll get that posted. I won't have

## 04:08

everything rated right away, but you'll have the solution. I always try to have the solutions ready

## 04:13

for you to examine. The reason why I'm breaking up the homeworks the way that I am this time is

## 04:19

because we have an exam next Friday, right? And so we have today's lesson, which is on the kinetics

## 04:27

with multiplication. We'll add in delayed neutron precursors on Friday, and that makes it a more

## 04:34

challenging problem, right? Because we go from a single differential equation, which scares some

## 04:39

of you by itself, to a system of differential equations, which makes things slightly more

## 04:45

challenging. On Friday, we'll look at sort of the set of equations in all their glory detail,

## 04:52

as it were, and apply some computational techniques. Now, on an exam, I won't have you

## 04:57

use computation. I'm going to have you use computation. I'm going to have you use computation.

## 04:57

But I think it's worth being able to set up the systems and exploring what the solutions look

## 05:02

like, right? Because you can look at solutions in a book, and it's like, man, that's fine. But it's

## 05:07

nice to sort of touch the process of getting those solutions. And those solutions are not ones that

## 05:12

you want to do by hand, right? Monday, we turn, we continue with the delayed neutron precursors,

## 05:18

and we examine some of the simplified cases that you can actually tackle by hand, right? And so

## 05:23

there are a couple of problems that will be there. You have access to them now. So

## 05:26

if you have any questions, please feel free to reach out to me. And I'll see you in the next

## 05:27

If you want, and you know that you're going to be tied up mid next week before the exam,

## 05:31

start looking at the stuff now, do the reading, get going on it, so that when we get to the lesson

## 05:36

material, the live time, it's not the first time that you're seeing it, right? You know,

## 05:40

I give reading assignments, I know that not everybody does the reading in advance, right?

## 05:44

You come here, hope that I tell you the Holy Gospel, and then you go and read the book after.

## 05:50

That probably works in some cases, but that's maybe not the most efficient use of this time.

## 05:55

So do the reading. And if you have the time,

## 05:57

or know that you won't have the time next week,

## 05:59

go ahead and dive into some of the homework problems

## 06:01

because what happens when you try it and you can't do it

## 06:04

and you have time to ask questions,

## 06:06

well, you can ask the questions

## 06:07

and hopefully we get you further along

## 06:10

than you might have otherwise.

## 06:12

And then Wednesday of next week,

## 06:14

lesson 29 is on, it's continuing with kinetics,

## 06:20

but kinetics with the addition of feedback effects, right?

## 06:23

There's a little blip in chapter five, section six

## 06:28

on feedback and it's just one page.

## 06:31

That's all I'm having you read.

## 06:32

You can skip ahead and look at chapter eight,

## 06:34

which we had bypassed and route to nine

## 06:37

for feedback effects.

## 06:38

What chapter eight has is a description

## 06:40

of sort of like a super simple thermal hydraulics model

## 06:44

for a reactor.

## 06:45

That's sort of out of the scope of this class.

## 06:47

It could be built in if I wanted it to,

## 06:50

but we have an entire class next semester

## 06:52

where we're going to be talking about

## 06:53

that will let us look at the reactor that we have

## 06:56

and its response related to temperature feedback effects.

## 07:00

So I'll reserve a detailed description

## 07:04

of all the thermal stuff until next time.

## 07:07

And maybe by then more of you will have had

## 07:09

some bits of heat transfer too.

## 07:11

We'll see, right?

## 07:12

But rather than try to force it all in,

## 07:14

which means then that Wednesday,

## 07:16

there's not a whole lot of content

## 07:17

that I'm going to present.

## 07:19

It's basically, here's a simplified model.

## 07:21

Hopefully I give you a sense

## 07:23

of what the pieces are,

## 07:24

like fuel heats up from power production.

## 07:28

If the flux goes up, power goes up,

## 07:30

temperature goes up,

## 07:30

temperature leads to heat dissipation to the coolant.

## 07:33

That temperature goes up.

## 07:34

These all have feedback effects

## 07:36

from those feedback reactivity coefficients

## 07:39

we just talked about, right?

## 07:41

So all this stuff is coming full circle.

## 07:43

So we'll play around with that a little bit,

## 07:45

but that should also give us some time on Wednesday

## 07:47

to tie up any loose ends

## 07:49

that you might have in preparations

## 07:51

for the exam.

## 07:53

And on that Friday.

## 07:55

Sound cool?

## 07:57

All right.

## 08:03

Let's go ahead and dive in, right?

## 08:07

So for next time,

## 08:09

I guess I should,

## 08:11

you can follow the page.

## 08:12

You don't really have to jump into 5.5.

## 08:14

5.4 is more informational than anything.

## 08:18

It describes the delayed neutron precursors

## 08:20

and how it shows up in the equations.

## 08:22

Basically, it's deriving the equations, right?

## 08:25

Which is maybe not the most,

## 08:28

you know, stimulating stuff.

## 08:29

It's in section 5.5 that the solutions get going.

## 08:33

We'll tackle the equation from 5.4 next time numerically,

## 08:36

which is not something that's covered in the book, right?

## 08:38

It'll just give us a way to explore some of the solutions.

## 08:41

So today what we're doing is looking at neutron kinetics

## 08:44

with multiplication.

## 08:47

All right.

## 08:47

So last time, one of the equations that we had

## 08:51

in the slides was this one.

## 08:53

And this was sort of after we had boiled down the massive

## 08:57

diffusion equation.

## 08:58

Right?

## 08:58

With energy, time and space dependence.

## 09:01

This is one of the steps that we ended up at before I said,

## 09:04

hey, let's just ignore this fission term, right?

## 09:06

And simplify it to be purely absorbing.

## 09:08

Okay.

## 09:08

So we'll start off from this,

## 09:11

which is still in terms of the neutron flux.

## 09:13

The flux, of course, is sort of the useful quantity to use

## 09:16

because a flux times a cross-section is a really

## 09:19

natural quantity.

## 09:20

That's the reaction rate.

## 09:22

Now, what we did last time was to replace that flux

## 09:25

with the neutron density, right?

## 09:27

So phi.

## 09:28

Phi is equal to nv, right?

## 09:30

And so if we do that, we'll get closer to what we had last time.

## 09:36

But I want to point out when we bring back fission,

## 09:38

I had written last time 1 over keff.

## 09:42

Eff is f for effective.

## 09:45

And that's when we've used k infinity so far in this class,

## 09:49

that represents the multiplication factor

## 09:51

for an infinite system.

## 09:53

Doesn't have to be homogeneous, just infinite.

## 09:55

Keff.

## 09:56

Or keff.

## 09:57

Eff.

## 09:58

Is more commonly used for any system

## 10:00

that has a finite extent.

## 10:02

The book, I think, uses just k without a subscript.

## 10:06

What I'm using keff here for is as a scaling parameter

## 10:11

that will adjust this fission term so that if we're doing

## 10:14

a time-dependent problem without a source,

## 10:18

I can force the system to be in steady state.

## 10:20

Now, what I mean by that will be a little bit clearer

## 10:23

when we get to a numerical example.

## 10:25

But you know that maybe you have a feeling for it.

## 10:27

If I have k not equal to 1, the reactor

## 10:30

is not going to be in steady state.

## 10:32

If we're using software packages like OpenMC,

## 10:35

let's say, which does allow neutron kinetics,

## 10:38

it does support neutron kinetics,

## 10:39

but there are a lot of other tools that will do it.

## 10:41

The common way to look at how a reactor responds

## 10:46

to some perturbation, like you eject a control rod

## 10:49

or something, and you want to know how the population is

## 10:51

going to increase, you always start off

## 10:54

with a steady state solution.

## 10:55

OK?

## 10:56

Now.

## 10:56

We know steady state corresponds to k equal 1.

## 10:59

But playing around with OpenMC or the unit cell stuff

## 11:03

that you did, maybe you can imagine how incredibly difficult

## 11:06

it would be for a computer model to give you

## 11:09

a solution such that k is exactly equal to 1.

## 11:14

Does that make some sense?

## 11:16

So even if you know that your system is critical

## 11:18

with statistical uncertainty or numerical errors,

## 11:23

it's essentially impossible to guarantee

## 11:25

that you will have k equal to 1.

## 11:26

It doesn't mean that your model isn't of a steady state

## 11:29

reactor, though.

## 11:30

It just means that you're going to have an eigenvalue k that

## 11:32

is slightly different from 1, like 1.001 or whatever, OK?

## 11:37

Because in reality, what we do with a reactor like ours

## 11:41

is we get to a point where we just stop seeing changes

## 11:44

in the power, right?

## 11:45

That's when we say, hey, it's critical, so k must be 1.

## 11:47

We don't have the same sort of thing in a Monte Carlo

## 11:51

or other simulation tool.

## 11:52

So what we do is we come up with that steady state solution,

## 11:56

right?

## 11:56

What we call critical.

## 11:58

It might have a k that's just slightly greater than 1

## 12:01

or slightly less than 1.

## 12:02

And so we use that value as the scaling parameter.

## 12:05

That means that all of the cross sections and so forth

## 12:08

are in balance with each other for that one value, right?

## 12:11

And that can be your initial condition for a larger scale

## 12:15

kinetics problem, OK?

## 12:17

For our purposes, though, we're not using OpenMC

## 12:19

to get that initial condition, right?

## 12:21

Our initial condition is going to be,

## 12:23

as you'll see in many of the book problems, assume you start

## 12:26

with a steady state solution, a critical reactor, k equal 1.

## 12:30

So for our purposes, that k effective

## 12:33

is just going to be set to 1.

## 12:34

And if it helps you sleep at night,

## 12:37

forget I ever talked about it, OK?

## 12:39

So once we make that assumption and we recognize that sigma t

## 12:46

minus sigma s is back to our sigma a, our absorption

## 12:49

cross-section, and that the flux is actually

## 12:52

the density times the average neutron speed, and we're going

## 12:56

to do that, we can plug all that in, do a little bit

## 13:00

of rearranging, and come up with dn dt is equal to k infinity

## 13:05

minus 1 over the lifetime times n plus whatever our source is.

## 13:09

And that's equivalent to equation 512 in the book, OK?

## 13:20

So one of the things that the book does describe a bit

## 13:25

is how to incorporate the non-leakage probability

## 13:28

that we've seen before coupled with the four-factor formula.

## 13:31

And I don't know that it's all that important.

## 13:34

Certainly, I'm not going to spend time

## 13:37

going through that explanation.

## 13:39

Because at the end of the day, the equation

## 13:41

that you get, which in the book is equation 522,

## 13:46

is the exact same thing without the infinities.

## 13:49

So for my own, to be sort of self-consistent

## 13:53

with my presentation, all the terms

## 13:56

that I'm going to use in this set of slides,

## 13:58

and I believe in the slides for next time,

## 14:00

will include the infinity.

## 14:01

Just because I'm not explicitly applying

## 14:07

the non-leakage probability, OK?

## 14:09

Because we really haven't covered leakage yet.

## 14:12

That's a chapter 6 thing, chapter 6 and 7 thing.

## 14:16

Question?

## 14:17

Non-leakage probability was on the denominator

## 14:19

in your bottom equation, right?

## 14:21

Or what is that, l infinity or 1 infinity?

## 14:24

This is l infinity.

## 14:25

So remember, l is the average neutron lifetime.

## 14:28

Oh.

## 14:29

Right?

## 14:29

So that is the product of the average neutron lifetime.

## 14:31

Oh.

## 14:31

So that is the product of the average neutron lifetime.

## 14:32

The speed times the absorption cross-section, right?

## 14:36

So it's the mean time before a neutron is absorbed.

## 14:40

Is that ringing a bell?

## 14:41

Yeah.

## 14:42

Yep.

## 14:46

Yeah, l is not a good letter in math script.

## 14:50

I hate that.

## 14:50

But I'm trying my best to be consistent with the book.

## 14:53

But yeah, good question.

## 14:54

Any time that it's not obvious, just holler out,

## 14:58

raise your hand, whatever.

## 15:04

All right, so let's go ahead and use that equation as our

## 15:09

starting point.

## 15:10

And we're going to do some simplifications here

## 15:12

to really dive into sort of an important difference

## 15:16

between the solutions we get when we have multiplication

## 15:19

and the solutions that we have when we don't have multiplication

## 15:22

or when the system is purely absorbing.

## 15:24

So we're going to start by assuming that we don't have

## 15:27

a source in the system.

## 15:29

This idea of having a source versus no source

## 15:31

is incredibly important in practice

## 15:33

because in order for a reactor to operate,

## 15:36

it needs a first neutron to initiate.

## 15:39

That chain reaction, right?

## 15:41

Now, if I had a critical reactor sitting out in a field

## 15:45

somewhere, there is a chance that it would go up in power

## 15:50

because we have all sorts of things coming from outer space,

## 15:53

cosmic rays, all sorts of interactions

## 15:55

that those rays can have that could introduce a neutron

## 15:58

to the system, right?

## 15:59

So it is never a safe thing to do

## 16:01

to have a critical pile of material

## 16:04

sitting in your back shed, right?

## 16:06

That is not something that you should do

## 16:07

because you can never assume that it

## 16:09

will be not exposed to neutrons.

## 16:13

In a reactor like ours, we don't rely on these cosmic rays.

## 16:17

We actually put in a neutron source

## 16:19

in order to start that chain nuclear reaction.

## 16:22

After a certain period of time, we'll

## 16:26

find that the density has gone up or the flux has gone up,

## 16:28

power has gone up, and the source doesn't matter anymore.

## 16:31

It could be the case that the reactor operators actually

## 16:34

remove the source at that point, right?

## 16:36

Because its contributions are basically negligible.

## 16:39

I'm not sure if we do that here.

## 16:41

Do we pull it out at power?

## 16:44

Yeah.

## 16:45

So are you an operator or?

## 16:46

No, just track the staff.

## 16:47

OK.

## 16:48

And so when they get to power, they actually

## 16:50

remove the source then?

## 16:51

I don't know that for sure.

## 16:52

But I know we have a source and we

## 16:54

use it for different things, testing when trips and stuff.

## 16:58

Got it.

## 16:58

Yeah.

## 16:59

So I don't think that they pull the source

## 17:01

because that would be something where somebody would be up

## 17:03

there at the pool moving it around.

## 17:04

So I think it's the source is always there,

## 17:06

which makes you wonder like, hey, if I'm at power

## 17:08

and that source is there.

## 17:09

Right.

## 17:09

So what's happening to the population because of it?

## 17:12

Well, that source is so weak that at power it's negligible.

## 17:15

But it's not when you're first starting up.

## 17:17

OK.

## 17:18

So for this case, we're going to also

## 17:20

assume that we have an initial number of neutrons

## 17:24

or an initial neutron density.

## 17:26

And so we want to determine n of t, right?

## 17:30

So the density as a function of time.

## 17:34

OK.

## 17:34

So the first things we need to do

## 17:36

are to write down the equations.

## 17:38

I'm going to be sort of.

## 17:39

I'm going to be a bit dantic in the steps

## 17:41

that I use to solve this, right?

## 17:43

Because I think it's always useful to reinforce

## 17:46

some good problem solving habits.

## 17:48

So the very first thing when tackling

## 17:51

a differential equation or system of equations

## 17:53

is to write down the equations.

## 17:54

Here we actually have two.

## 17:56

It might not be obvious, but we have

## 17:57

the original differential equation

## 17:59

and we have the initial condition.

## 18:01

Any time that we have an initial value problem,

## 18:04

we need the initial condition.

## 18:06

I mean, in this case, is that actually saying anything new?

## 18:09

But I'm putting n subscript zero.

## 18:11

I'm saying, hey, there ought to be a value that's given.

## 18:13

Otherwise, I've got to assume something.

## 18:15

This is the equation that we are solving.

## 18:18

It looks almost identical to what we solved last time.

## 18:21

And now we have a different constant.

## 18:23

I've moved it over to the right hand side as well.

## 18:25

But it's the same thing that we have.

## 18:31

The second step is to recognize any special features

## 18:35

for the equation.

## 18:36

Figure out its type.

## 18:37

And if you know its type, then there

## 18:38

are usually certain tricks.

## 18:40

The thing about differential equations

## 18:42

that I think, in many cases, scares students

## 18:47

or makes students uncomfortable is

## 18:49

that they don't necessarily understand how to.

## 18:56

Maybe a better way to say it is don't

## 18:59

be afraid of differential equations

## 19:01

because all you need to do is apply an algorithm.

## 19:04

You have a differential equation.

## 19:06

It's one of a variety of types, and there

## 19:08

are tricks for each one of them.

## 19:10

You're not ever supposed to be able to figure out

## 19:12

an arbitrary differential equation.

## 19:14

That's for the math PhDs to work on.

## 19:15

As an engineer, you're given a differential equation.

## 19:18

You've got a book of possible techniques.

## 19:21

You're only responsible for having access

## 19:23

to those techniques, whether you keep it in your mind,

## 19:25

you keep it on your cliff's nose, whatever.

## 19:27

So what kind of equation is this?

## 19:33

It's differential because I see d and dt.

## 19:35

So any equation that has a derivative of the unknown

## 19:38

that we're looking for is, by definition,

## 19:40

a differential equation.

## 19:42

OK?

## 19:43

So what type of derivative is it?

## 19:48

It's a first derivative, so it's a first-order differential

## 19:51

equation.

## 19:52

Do we see any instances where the unknown, which

## 19:56

is our density, is it squared anywhere?

## 19:59

Is it tucked into a sign or anything like that?

## 20:02

No, it's only some coefficient, possibly

## 20:04

a function of time, multiplied by that thing.

## 20:06

So it's linear.

## 20:08

So it's linear first-order differential equation.

## 20:11

Because there is just.

## 20:12

It's just a regular d and not a partial symbol,

## 20:15

meaning that n depends only on one variable.

## 20:19

Do you know what we call it when that's the case?

## 20:22

Ordinary.

## 20:23

It's ordinary, right?

## 20:24

Which is weird because the alternative is partial, right?

## 20:27

So in some sense, ordinary shouldn't be ordinary.

## 20:30

It should be like impartial, but that doesn't sound right.

## 20:32

So ordinary just means function of one variable.

## 20:35

So it's ordinary first-order differential equation.

## 20:38

In this case, it has constant coefficients,

## 20:40

which simplifies our life a little bit.

## 20:41

But there's a more important property

## 20:43

about this specific equation.

## 20:45

Anybody know what that is?

## 20:49

Is it like separable?

## 20:50

It's separable.

## 20:51

And the reason for that is we have a function of n

## 20:53

on the left-hand side, in this case, the derivative.

## 20:55

We have the n right here.

## 20:56

And there is no what I would call inhomogeneous term.

## 20:59

There's no forcing function.

## 21:00

There's no source because we set the source equals 0.

## 21:03

That makes it separable, right?

## 21:04

So what we do when it's separable is to rearrange things in a way that we can apply,

## 21:11

and we can integrate them directly.

## 21:13

Remember, when we solve a differential equation, it's all about integration.

## 21:17

What we did last time with the integrating factor, all that does is it puts it into a

## 21:21

form that we can integrate both sides.

## 21:24

A separable equation, when you adjust it like this, gets it into a form where you can integrate

## 21:28

both sides.

## 21:30

I would say the biggest battle in differential equations is getting it into a form where

## 21:35

you can integrate both sides, right?

## 21:37

At least that's the case for these first-order equations.

## 21:41

So in this form, I think I can do some integration, right?

## 21:45

So we're going to integrate the left from n at 0 to n at the time in the future, and

## 21:51

the right-hand side, which is a function of t from time equals 0 to time equals t, right?

## 21:58

And if we do that, we end up with this sequence of steps that I've laid out in gross detail,

## 22:06

but it's there for your resources later on if you're attached to it.

## 22:10

All right.

## 22:11

We're going to tackle this.

## 22:13

A lot of times, folks will use dummy variables, and usually I do that too, but I recognize

## 22:18

now that you don't really have to.

## 22:20

You can just choose to do that integration on both sides using what would otherwise be

## 22:24

the dummy variable.

## 22:25

So rather than integrate from any of 0 to n of t due to t prime, so the dummy variable

## 22:31

goes from the integrand to the integral bound.

## 22:35

But at the end, you just swap them because this thing is equivalent to this because it's

## 22:40

arbitrary, simple, OK?

## 22:43

So what we end up with is this form that is exponential that looks a hell of a lot like

## 22:50

we saw last time, OK?

## 22:52

There is one important difference, though.

## 22:54

When we had the solution last time, in that exponent of the exponential term was minus

## 23:02

sigma a, right?

## 23:06

Minus sigma a times, sorry, minus 1 over sigma a times b bar.

## 23:12

Right?

## 23:13

The lifetime.

## 23:14

OK?

## 23:15

Here, we have that k infinity.

## 23:16

K infinity, basically, we could set that to 0, and we recover the solution that we had

## 23:20

last time.

## 23:21

The k infinity is what we get with multiplication, OK?

## 23:24

So the value of k infinity will dictate whether this exponential is one of attenuation, which

## 23:32

we saw last time, or growth, right?

## 23:36

So the key difference here is that by adding multiplication, we insert the option.

## 23:41

Of growing in time.

## 23:44

That's something you don't get if you have a purely absorbing system, OK?

## 23:49

And if we apply that initial condition, then we end up with the final box solution, which

## 23:55

is equivalent to 524 in the book if we drop those infinities that I've kept.

## 24:07

Maybe I asked this earlier in the course.

## 24:09

You've all had differential equations.

## 24:10

When, how many, for whom is it right now?

## 24:15

For whom was it like last semester?

## 24:18

I know everybody's schedules get different.

## 24:20

I mean, I think on the average, it's like maybe two semesters, three semesters ago.

## 24:25

Is that four semesters?

## 24:27

Four?

## 24:28

Yeah.

## 24:29

I mean, when I was an undergrad, I had done all the calc in high school, because I was

## 24:35

an overachiever and didn't have a life.

## 24:37

And I had differential equations my first year, and while that felt really cool and

## 24:42

fantastic at the time, it turned out to be really not useful.

## 24:46

Because.

## 24:47

If you don't have applications for the math, the math becomes useless.

## 24:54

And I probably wouldn't have said that at the time, but I'm getting very critical about

## 24:59

the way things are done in practice.

## 25:01

Basically, my sensitivity to BS has gone way, way up, which is why that yellow card story

## 25:09

is meaningful, because it means that I'm working on this.

## 25:12

Right?

## 25:13

So anyway, that's our solution to the.

## 25:17

Problem.

## 25:18

Problem without a source.

## 25:19

Okay.

## 25:20

So one thing that we can do to kind of connect to what we've seen in the past is to all this

## 25:26

relationship between what we've called the reactivity and this, this eigenvalue.

## 25:31

Now this is covered also in chapter five, but it's a little bit later than where we

## 25:35

are right now.

## 25:36

I want to do that here though, because there's a problem that I've assigned I think benefits

## 25:42

from you seeing it now.

## 25:44

But if we do, if we recall this definition.

## 25:46

Then we can actually rewrite that that the solution as a function of time in terms of

## 25:53

the reactivity.

## 25:54

Right.

## 25:55

And so the only other thing I've got to introduce is this thing here, which is called the mean

## 25:58

generation time.

## 26:00

It takes our average neutron lifetime, which is the terrible L right.

## 26:04

Infinity divided by K infinity.

## 26:06

So this capital Lambda, that mean generation time is numerically almost the same as the

## 26:13

neutron lifetime.

## 26:14

If K.

## 26:15

Is close to one.

## 26:17

Right.

## 26:18

So if K is close to one thing, then numerically, if K is one, then these two are identical.

## 26:24

But if not, then what K infinity does is it reduces it even more.

## 26:29

That means that if you have a system who basically the more supercritical you are, the lifetime

## 26:35

goes down.

## 26:36

It sort of exacerbates the, the, the, the, the, the exponential growth.

## 26:41

Okay.

## 26:42

Now in this form.

## 26:44

Things.

## 26:45

Are quite a bit easier to understand when it comes to when is this exponential growth

## 26:51

or decay, because this is N not times E to a coefficient that Lambda is always going

## 26:58

to be positive.

## 26:59

That's a lifetime.

## 27:00

We can't have neutrons with negative lifetime.

## 27:01

So what we have is, is that Lambda is scaling row.

## 27:05

Well, we know what row is row is the reactivity, a positive row means that we are super critical,

## 27:11

right?

## 27:12

A positive row means that K is greater than one.

## 27:15

A negative row means that K is less than one.

## 27:17

A row of zero means that K is equal to one, right?

## 27:21

Critical.

## 27:22

So what this means is if the system is supercritical, its population has to grow in time.

## 27:31

If it's subcritical, it will decay in time.

## 27:34

Right.

## 27:35

And I guess in the extreme row would be like negative infinity, right?

## 27:39

Because then K would be zero and we would have pure absorption.

## 27:45

And so yes, things would decay very fast.

## 27:47

What if row is equal to zero, right?

## 27:55

That makes sense.

## 27:56

That's another way to say it's steady state.

## 27:58

So every time I've said that criticality means steady state, steady state doesn't mean anything

## 28:03

unless you have some way to account for time dependence, right?

## 28:06

In which case it has, you know, it's constant time here.

## 28:11

You can actually see that if row is equal to zero or in this case, K is equal to one,

## 28:16

then the exponential goes away.

## 28:18

It's just E to the zero and we were left with an unchanging population.

## 28:22

All right.

## 28:26

So multiplication lets us have exponential growth, which is incredibly important, right?

## 28:32

It's very important in practice because that's the only way that we can go from zero power

## 28:37

to some higher power, right?

## 28:39

Or increased power in general.

## 28:42

It's the reason why things like atomic weapons are so violently powerful, right?

## 28:49

Because the amount of energy that is released is an exponentially growing function of time,

## 28:54

right?

## 28:55

Anytime that you deal with exponential things can happen really fast that wouldn't otherwise

## 29:00

be possible.

## 29:02

Okay.

## 29:03

So without any multiplication, I had said the number of neutrons in the sourceless system

## 29:09

can only decrease.

## 29:10

We'll bring back the source at the end of the lesson, right?

## 29:13

But with multiplication, the number of neutrons can decrease or they can stay the same, or

## 29:18

they can increase, right?

## 29:19

So we've got three options.

## 29:21

So just by adding that multiplication makes us a much more interesting game.

## 29:25

All right.

## 29:29

So as an example, let's assume that we start with a neutron density of one.

## 29:36

We'll take our neutron lifetime to be a millisecond.

## 29:41

And what I'd like you to do is pull out your calculators or computers or what the hell

## 29:48

is the one where you move things.

## 29:49

Okay.

## 29:50

You could use the slide rule too.

## 29:51

I'm not sure if that'll help, but maybe, right?

## 29:52

And what I'd like you to do is compute n at one second into the future for these three

## 30:03

cases, right?

## 30:04

K infinity equal 0.99, K infinity equals 1, K infinity equal 1.001, right?

## 30:11

I guess case B is probably pretty straightforward given what we just saw.

## 30:14

So focus on A and B, right?

## 30:18

And then as we get some numbers in...

## 30:20

I'll toss them on to the, I can't remember, did I actually, yeah, I've got myself set

## 30:31

up to do it computationally too, but I'll use this also as a cell to write your numbers.

## 30:43

All right.

## 30:44

So for A...

## 30:45

Good.

## 31:18

If I put A, B, W, X, Y, and Z on one, would you remember playing the game of New York

## 31:28

Wars?

## 31:29

Yeah.

## 31:30

Yeah.

## 31:31

Yeah, I think so.

## 31:32

We used to have a game that you could transfer.

## 31:33

And of course, if you had source code, you could go and make it easier to manage this

## 31:42

because you're using some products, just like playing Ornstein or Godmode.

## 31:47

One time I used a hex editor to edit something in that game called Crush, Kill, and Destroy,

## 31:57

which was a command and conquer clone of sorts.

## 32:00

I could get all of my mind jewels that I wanted.

## 32:03

I think we both bothered.

## 32:04

I'm not sure what the problem is.

## 32:05

Of course, the satisfaction wasn't winning, it was the act of learning how to do the number.

## 32:20

All right, so what are we getting for A?

## 32:35

First of all, is it greater than one or less than one?

## 32:39

Right, because it's a negative reactivity, so it should decay.

## 32:43

And so what is it?

## 32:45

0.67?

## 32:52

Okay.

## 32:52

What about B?

## 32:57

I heard a zero.

## 32:58

I think it's one, right?

## 33:01

Because it's unchanging.

## 33:02

And then for C, sanity check, is it greater than one or less than one?

## 33:07

Right, it should be greater than one.

## 33:08

And what is that number?

## 33:11

2.72, right?

## 33:15

It's E, if I recall.

## 33:17

No, is it E?

## 33:20

Yeah, that's right.

## 33:21

So we can do that.

## 33:23

So import numpy, it's np, np.exp of, what is it?

## 33:32

1.

## 33:32

1 minus 0.999 divided by 1E minus 3.

## 33:38

Okay.

## 33:40

Oh, got that.

## 33:48

Okay, got that.

## 33:49

And then if I wanted the other one of interest, we have that.

## 34:02

Cool.

## 34:05

Now, just to play with this a little bit, I'm going to plot these populations as a function of time.

## 34:14

And what I get is this plot, right?

## 34:19

So, of course, we get our values at one.

## 34:21

The orange curve stays constant, and we have this decrease and increase.

## 34:27

Now, I could take it out for a lot longer, and it would just continue to increase, which we'll find
out next Wednesday.

## 34:34

It's not going to, like, the increase that we have is not indefinite, because at some point, you've
produced so much energy and therefore so much heat that your system fundamentally,

## 34:44

it fundamentally has to do something.

## 34:46

In the case of a nuclear weapon, of course, you explode.

## 34:50

In the case of a nuclear reactor, it could be that your feedback mechanisms will turn that power
increase down in a safe way that doesn't cause structural damage.

## 34:59

But in other reactors, it might be the case that your reactivity goes up, the energy production is
so large that, you know, you have a meltdown or something.

## 35:07

But still, the reactivity would have to turn over because you have reactivity effects, kind of.

## 35:15

All right.

## 35:15

So, now, let's go ahead and bring back the source and consider something called a source-driven
subcritical system.

## 35:23

So, we're going to consider only cases where K infinity is less than one or our reactivity row is
less than zero, okay?

## 35:33

When would we actually see a source-driven subcritical system?

## 35:38

Well, the first place that we'll see it is at our reactor when we start up, right?

## 35:43

Because when we start up, we are with...

## 35:45

We're drawing control rods.

## 35:46

So, from a cold shutdown situation, which you should be familiar with after the homework, we remove
control rods, and we increase our reactivity, but not up to the point of being critical, right?

## 35:59

So, we have that source that Alex had described, the population is going to increase, and what we're
looking for is a point where it will continue to increase if we have that source in there, right?

## 36:11

Ultimately, though, we want to get to some point where it gets to sort of an asymptotic value.

## 36:15

So, we want to get to some point where it stays put, right?

## 36:16

That's where we sense criticality.

## 36:21

So, this is the equation that we have.

## 36:23

So, in this case, I'm not going to go through all of the details, but this is the equation that we
had in the last lesson.

## 36:33

What I've done is I've replaced the sigma A with or just the lifetime term with our full term here
that involves K infinity.

## 36:42

So, you can go back to the slides last time and do...

## 36:45

You can do a one-to-one comparison if you'd like, right?

## 36:49

But what we end up then with is this sort of generic form that I could adjust a little bit, but this
is sort of as far as I need to go to make it general, right?

## 36:59

Because this is for any initial condition, and as written, it's good for any source term, all right?

## 37:07

When we do things by hand, it's almost always going to be the case that the source term is a
constant, right?

## 37:13

The minute that you start putting...

## 37:15

The minute that you start putting functions of time, it's doable, right?

## 37:17

Then you have...

## 37:18

It's just uglier solutions.

## 37:20

So, we'll probably consider just, you know, fixed sources, which is, you know, for the case of the
source in the reactor, but I think it's an ambi source, amauricium beryllium source that produces
neutrons from an alpha N reaction.

## 37:36

You know, that thing is decaying in time, but for the purposes of reactor startup, it's essentially
a constant source term, right?

## 37:44

So, that's not a...

## 37:45

That's not a terrible use case to consider, okay?

## 37:49

So, we have that equation.

## 37:52

Now, if we set that source to a constant, then things simplify considerably, and we're left with an
equation that if you sort of look back a little bit and imagine the K infinity minus one over L
infinity is just a number.

## 38:07

We've seen this before, right?

## 38:10

Probably the first place we've seen an equation like this is for the production.

## 38:15

Of a radioisotope, given some sort of source terms, forcing function, right?

## 38:21

You have R nuclei produced per second, and it has a decay constant, right?

## 38:26

And so, what we're seeing here is that production term with effectively that decay constant, right?

## 38:33

And then the decay of whatever our initial condition, right?

## 38:36

So, basically, a first-order differential equation with a constant right-hand side will always have
this form for the solution, right?

## 38:43

So, not a bad one.

## 38:45

Commit to memory if you're into that sort of thing.

## 38:47

But being able to get to it from the first principles is also useful.

## 38:51

So, if we set this, the initial condition N of zero to zero, and we drop the infinities, then you
get Lewis's equation 5.26, right?

## 39:01

So, you can reference that in the book.

## 39:05

So, with this equation, let's go ahead and tackle another example.

## 39:11

Let's assume that our initial condition is zero.

## 39:13

We'll assume that our source term is one, or we could leave it as an arbitrary s-naught and then
scale our answer to be the density per s-naught.

## 39:22

But let's just set it to one.

## 39:24

And we'll assume a lifetime now of 10 to the minus two.

## 39:27

That makes things a little bit cleaner on the graph, right?

## 39:31

So, we'll compute and then plot this density as a function of time for zero to 10 seconds, right,
for four different k-infinity values.

## 39:40

And then we're going to look at.

## 39:43

And then kind of wax poetic for a bit about what N of t over s-naught looks like as t goes to
infinity.

## 39:50

This is sort of the main takeaway of this lesson.

## 39:53

And it brings us back then to homework seven, which was that one where I had that big verbose
solution, which I hope you all looked at, right, related to the two group equations in k-infinity.

## 40:07

So, that might sound esoteric or abstract or unrelated now, but I'll tie it together in the end, I
promise.

## 40:13

So, to plot all this, I know that you could take out your calculators and do this one by hand, but I
want to just use Python to get to the visualization right away.

## 40:24

So, I'm making a function, right, for the number, the density of neutrons as a function of time and
for a given k-infinity.

## 40:33

I'm hard coding the lifetime and the source from inside that function.

## 40:37

I'm returning it all, right?

## 40:38

So, this is one way that you can set up the...

## 40:41

Doing something to plot.

## 40:44

I'm going to set my times from 0 to 10 as asked for, and I'm going to use quite a few data points.

## 40:49

Probably don't need to because this thing isn't changing that quickly, but I don't know that in
advance, so I'll try to account for that.

## 40:57

And then I'm just, you know, copying and pasting the plot command.

## 41:01

I also have a line here that will change it to log scale so we can go back and forth easily between
log.

## 41:08

So, I don't know if you've ever run into this where you have, like...

## 41:11

Four different plots that use the plot command, and it's like, oh, this would look a hell of a lot
better on a log plot, and then you're copying and pasting semi-log y in place.

## 41:19

That's what I've done before, and it's like, well, you don't actually have to do that.

## 41:22

You can just have this line here that turns it into log, or you can write linear or comment it out
or whatever.

## 41:28

By default, of course, plot will give you a linear, linear plot, okay?

## 41:33

Now, if I plot this, this is what I see.

## 41:37

And let me make this figure a bit bigger for our viewing.

## 41:41

This is kind of important, right?

## 41:47

I'll zero out in a bit, but what we're seeing is a very sharp increase in the number, right?

## 41:55

The density of neutrons.

## 41:56

Remember, I'm saying density.

## 41:58

The book refers to n as being the number.

## 42:01

It's just a matter of have you divided by volume or not, right?

## 42:04

We don't know what the volume is in an infinite reactor.

## 42:06

So, you could think of it as number per unit volume, which is the density.

## 42:11

That's why I'm using it that way.

## 42:12

We have this increase for all of them, for any value of these key infinities.

## 42:16

We go up, but then it starts to fold over and tapers off to this asymptotic value, right?

## 42:22

So, this is for 0.5.

## 42:23

This is for 0.9, 0.99, and 0.999, 0.999, right?

## 42:28

And I haven't carried this further, far enough in time for it to totally hit its asymptote, but you
can imagine that it is doing that.

## 42:36

And if you don't believe me, you can just ask me to take it out further, okay?

## 42:40

So, what's happening here?

## 42:46

And importantly, look at this y-axis, right?

## 42:49

So, for the blue line, we're at, so this is 10 to the minus 2.

## 42:53

So, this is 2 times 10 to the minus 2.

## 42:57

This is about 10 to the minus 1.

## 43:00

The green one is roughly 10 to the 0.

## 43:03

The red curve is going to asymptote to 2, 3, 4, 5, something higher, okay?

## 43:09

Remember, we're starting off with an initial condition of 1.

## 43:13

So, for the green curve and the red curve,

## 43:15

we're ending up with a neutron density that is greater than what we started with, right?

## 43:22

For the blue curve and the orange curve, so for K infinity of 0.5 and 0.9,

## 43:27

we are ending up with a neutron density that is smaller than what we had started with, right?

## 43:37

Because, sorry, not started with, because we're starting with 0, but I guess smaller than the source
term, okay?

## 43:44

So, these ones are bigger than the source term.

## 43:46

These ones are smaller than the source.

## 43:47

Numerically, can you find a relationship?

## 43:58

Maybe it'd be easier if I set this to the linear plot, okay?

## 44:05

And maybe it would be easier if I get rid of the red curve just for a moment, okay?

## 44:11

So, that green curve appears to be asymptoting at exactly 1.

## 44:19

Why is that?

## 44:28

And how could it be that we end up with a term larger than the S naught

## 44:31

when we bring back that 0.99?

## 44:36

9.

## 44:37

The red curve that I just deleted.

## 44:40

Does it make any sense?

## 44:53

Well, think of it this way.

## 44:53

If I have a reactor that is very, very close to critical,

## 44:56

that means if I put one neutron in, maybe it, or maybe it's not one neutron,

## 45:02

because then it could be extinguished right away.

## 45:03

But if I put a million neutrons in, if I'm very, very close to critical,

## 45:07

it's going to be the case that maybe I put in the million,

## 45:10

and then the next generation, I have 999,999, right?

## 45:15

Because, like, I will decrease.

## 45:18

In time.

## 45:19

And then I will go down a little bit more, a little bit more.

## 45:22

Now, that's if I only put it in at that very first instant.

## 45:27

This is a source term that is constant in time.

## 45:30

So, that means that at every, if we break up time into generations, okay?

## 45:35

I'm putting in a million at generation zero.

## 45:37

I'm putting in a million new ones at generation one, and then two, and three, and four.

## 45:42

Now, if I get to generation 10, I still have neutrons that are,

## 45:47

that are decaying away from generation zero, one, two, three, and four, right?

## 45:52

So, I'm building up.

## 45:53

And if I'm that close to K equal one, then the total number of neutrons that I have

## 45:58

in the system is going to increase beyond whatever that source term is, right?

## 46:02

And if I put in a million at time zero, not all of them are going to be gone

## 46:07

by the time I get to time, you know, 10 seconds, right?

## 46:11

If I start off with enough of them, and my decay constant is, you know, small enough,

## 46:17

right?

## 46:17

So, what this means is that if I'm sufficiently close to critical,

## 46:22

by introducing source terms, like continuously in time, I will build up a population

## 46:27

that is bigger than the source term string, okay?

## 46:31

That's multiplication, right?

## 46:33

So, we've talked about the multiplication factor, and that has a very specific meaning.

## 46:36

It's the, it tells you sort of the ratio of the number of neutrons

## 46:40

that you get from one generation to the other.

## 46:43

What this idea of multiplication is, is if I am injecting using some

## 46:47

external source of neutrons, if I'm injecting a certain number per second

## 46:52

into the system constantly, multiplication tells me how much

## 46:56

that is amplified if I wait long enough, right?

## 46:59

There will be some buildup in the beginning, like the minute I put that source in to the reactor,

## 47:04

like if I have, if I have a critical reactor with no neutrons, right, N of zero, zero,

## 47:09

I put that constant source term in, it's going to take me several generations to build up,

## 47:13

and the closer to K equal one that I get, the longer,

## 47:17

it will take to build up, which is evidenced by that red plot that I had to go

## 47:21

because I hadn't turned it over again.

## 47:23

Now, this is all related to what we had talked about before.

## 47:28

So, you might remember from homework seven, you had to deal with phi one and phi two,

## 47:33

the two group stuff, right?

## 47:34

And I had these poorly worded problems where I said, hey, take the two group equation,

## 47:39

get rid of the, the multiplication stuff, and just put in a unit source.

## 47:43

Now, go back to the solution.

## 47:45

One of the, one of the ways that you could, you know,

## 47:47

you could interpret that problem led to a phi one solution that looks like this, okay,

## 47:53

where if I didn't have the multiplication, it would just be S naught over sigma R one,

## 47:58

right?

## 47:59

That's what you get if you put, if you delete the multiplication, but if you have the multiplication

## 48:04

in there or solve with the, all the thermal stuff, you end up with this expression, okay?

## 48:08

Now, if you take that and you apply a couple simplifications to bring it back into the

## 48:16

terms that we have here.

## 48:17

In this kinetics lesson, that would be taking the sigma R one and calling that sigma A, right?

## 48:23

Basically ignoring the fact that there was thermal stuff anyway, the removal cross section,

## 48:27

remember is the total cross section minus the self scatter.

## 48:30

The only other thing that you have is absorption and then scatter into other groups.

## 48:34

So, if you forget about the thermal group for a moment, then the removal is effectively an
absorption

## 48:40

of the fast neutron, okay?

## 48:41

So, if you take, if you make that connection and then you set the, the fast group flux to be our,

## 48:47

our speed times N, our B times N, then you can rewrite this expression as this.

## 48:55

And that is equivalent to equation 528 in the book.

## 49:01

And this represents the numerical value that we're hitting on that previous plot, right?

## 49:06

So, when we asymptote, this is the expression for what that is.

## 49:09

Okay?

## 49:10

So, the fact that N is either greater than or less than S naught is influenced in part

## 49:16

by the one minus.

## 49:17

K infinity, but also by whatever that lifetime is.

## 49:20

So, the fact that just at K equal, let's see, what was it?

## 49:27

K equal 0.99.

## 49:28

That's when we hit the value of one.

## 49:32

Well, that's a function of 0.99 being related to 0.01 for that lifetime, right?

## 49:37

They, they, they match in that, that case.

## 49:41

And so, we end up with the value of one, right?

## 49:46

So,

## 49:47

Depending on what L infinity is, you might need a slightly closer to critical K infinity

## 49:53

to to have it.

## 49:55

But the, where multiplication is more useful is not to understand what the density is.

## 50:00

Because the neutron density is of course the most fundamental unit, but the neutron density

## 50:06

Doesn't, is not what we use to scale to power.

## 50:11

That power comes from the flux times a fusion cross section.

## 50:14

So, if we're looking to, to understand how the sorority of the of the attraction to this

## 50:16

totality can be converted tochair, it 소, instead, revolutionary, above the slope of the should,

## 50:17

source might um how the source could be used to amplify like the reactor power we'd look at the

## 50:24

flux and then we'd have you know s naught divided by one minus k so anyway this this this factor of

## 50:31

one over one minus k infinity this m term here that i've defined without the infinities is called

## 50:36

the multiplication and in reactor lab next semester we will use this quantity to understand

## 50:44

when the reactor gets to critical we'll watch m keep increasing right because the closer you get

## 50:50

to k equal one the bigger the multiplication is the more your power increases and we will use that

## 50:59

to to approach criticality in an experiment literally called the approach to criticality

## 51:04

or the one over m experiment okay um i think that's all i wanted to say so the reason i bring

## 51:14

back homework seven in this problem four

## 51:16

is when we talked earlier about k infinity and then the idea of criticality it was always with

## 51:22

this steady state interpretation you can't really talk about steady state until you have time

## 51:27

we've now introduced time and we find that if we let time go out far enough d and dt goes to zero

## 51:35

right when you have a solution that flattens out like that it's no longer changing in time

## 51:39

that is the definition of steady state right we could get to that same answer if we took our

## 51:44

original kinetics equation

## 51:46

right if we go back to this thing here

## 51:52

right we could get to that same thing if that's our solution we'd need to go back to this thing

## 52:00

we would set the d dt to zero once we expand this right so that's one way you can easily find the

## 52:05

steady state solution to an equation if it has it you can get it by setting the derivative to zero

## 52:10

and then adjusting and solving for whatever your unknown is okay that's everything i wanted to talk

## 52:15

about today

## 52:16

right so the source driven multiplication is important it also has other uses there have been

## 52:21

uh research efforts looking at using things like accelerators to produce neutrons to slam into

## 52:28

subcritical systems why is that of potential use it's much easier to license a nuclear facility

## 52:35

that does not use a critical system right criticality is it that's uh that's something

## 52:41

that takes a lot of safety procedures to manage if you know that you're subcritical

## 52:46

it's easy to use a nuclear facility but if you know that you're subcritical it's easy to use a

## 52:46

nuclear facility but if you know that you're subcritical it's easier to get past the nrc

## 52:48

regulations it's just it so far hasn't been something that's economically viable right but

## 52:53

the idea is the same you're just producing neutrons um at a much higher level right to

## 52:59

actually produce power okay i will see you all on friday

## 53:03

this thing yeah i just kind of want to look at the

## 53:13

what i'm getting

## 53:15

so

## 53:16

what was that big size

## 53:18

uh big size that that changes the size of my my plot

## 53:27

and what are you getting that's off

## 53:48

and what are you getting that's off

## 53:52

um

## 53:54

um

## 53:56

um

## 53:58

um

## 54:00

um

## 54:02

um

## 54:04

um

## 54:06

um

## 54:08

um

## 54:10

um

## 54:12

um

## 54:14

um

## 54:16

um

## 54:18

um

## 54:23

um

## 54:26

um

## 54:31

um

## 54:34

um

## 54:38

um

## 54:40

um

## 54:42

um

## 54:44

um

## 54:46

um
