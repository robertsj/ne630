# L32 Local Audio Transcript

Course: NE 630

Playlist source: https://youtube.com/playlist?list=PLy481lNHlnHoEO95vM-xYX2bydD25v20L

Video: NE 630 - Lesson 32

URL: https://www.youtube.com/watch?v=gcoRc_tfe54

Video ID: gcoRc_tfe54

YouTube upload date: 20231110

Duration: 52:03

Transcript source: Local faster-whisper transcription from YouTube audio.

Whisper model: large-v3; detected language: en.

Generated: 2026-06-28

Note: This transcript is machine-generated from audio and lightly wrapped only. It should be reviewed before being quoted, published, or used as polished lesson text.

Requested language: en

## 00:01

and my own remaining professor

## 00:04

will say that the

## 00:06

to the

## 00:08

and the rest is

## 00:10

really hard

## 00:12

to do it like that.

## 00:14

But what I like, I

## 00:16

do not

## 00:18

go anywhere near the

## 00:20

So I'm going to say why I like this

## 00:23

.

## 00:24

This one, I mean, that's

## 00:26

Yeah, this one

## 00:28

is this one

## 00:30

.

## 00:33

I don't like it.

## 00:35

I don't

## 00:43

All right, let's go ahead and get started.

## 00:46

It's been a while since I sat down and actually

## 00:48

solved the differential equation.

## 00:50

So this is

## 00:52

instructive for me too.

## 00:54

All right.

## 00:56

So last time we talked about

## 00:58

the neutron diffusion equation.

## 01:00

I didn't

## 01:01

derive it.

## 01:02

I wouldn't even say the book derives

## 01:04

it, maybe heuristically.

## 01:06

Right.

## 01:07

But at the end of the day, from

## 01:09

sort of a macroscopic view of neutron

## 01:11

balance, we were able to zero

## 01:13

down into a small

## 01:16

differential volume.

## 01:18

And the balance is then described

## 01:20

by this thing called the diffusion equation.

## 01:22

So I've written it here.

## 01:23

I've omitted the vision term

## 01:25

and I'm dropping the triple prime

## 01:27

on the source term just because that's

## 01:29

more work for me to write up.

## 01:30

But as written,

## 01:33

it's sort of applicable to any geometry.

## 01:36

We have three dimensions

## 01:39

bundled up into this R term.

## 01:42

Where the different coordinate systems

## 01:44

would play a role is in the evaluation

## 01:46

of this diffusion term

## 01:48

with the gradient of the flux

## 01:51

and then the divergence of this quantity here.

## 01:54

D times grad B with the minus sign.

## 01:58

Anybody remember what that is?

## 01:59

Right.

## 02:04

D times grad B with the minus sign.

## 02:06

That's a special quantity.

## 02:08

The current.

## 02:09

Right.

## 02:10

So this is we were able to eliminate

## 02:12

the current, this term called J,

## 02:14

by using Fick's law.

## 02:16

Right.

## 02:17

Which relates the current to the flux.

## 02:20

And we'll look a little bit later on

## 02:24

at what the sort of implied assumptions

## 02:29

are when applying Fick's law.

## 02:31

Fick's law we just kind of pulled out of thin air.

## 02:33

And it's phenomenological.

## 02:35

So it just works in practice.

## 02:37

And it does also for neutrons

## 02:39

subject to certain constraints.

## 02:41

Right.

## 02:42

For our purposes,

## 02:43

we're not going to worry about those in practice,

## 02:45

but I'll highlight them

## 02:47

probably with some simulation

## 02:49

to show you where diffusion fails.

## 02:51

Okay.

## 02:52

And then you can come and see me in 806

## 02:54

or some other class to learn more if you like.

## 02:57

Okay.

## 02:58

So what we'll do today is focus on the solution

## 03:00

of that boxed equation

## 03:02

for one-dimensional so-called slab geometry.

## 03:06

Right.

## 03:07

What does slab geometry mean?

## 03:08

It means that we're going to deal with things

## 03:10

in the Cartesian coordinate system,

## 03:12

and we're going to choose one axis

## 03:14

along which the neutron flux varies.

## 03:17

And in the other dimensions,

## 03:19

we assume everything is constant.

## 03:21

Okay.

## 03:22

There were some questions in the notes.

## 03:25

When is this valid or when is this appropriate?

## 03:29

Okay.

## 03:30

It's never perfect,

## 03:33

but there are some situations

## 03:35

in which the variation in one dimension

## 03:38

is significantly greater than variation

## 03:41

in the other dimensions.

## 03:42

A very simple example is

## 03:44

if I want to measure the cross section

## 03:47

of a piece of metal,

## 03:49

right,

## 03:50

the nuclear cross section,

## 03:51

like getting a sigma value,

## 03:53

one of the ways I do that is to use a thin foil,

## 03:56

right,

## 03:57

a thin foil placed in a neutron beam

## 03:59

where the neutrons are all monodirectional,

## 04:02

right,

## 04:03

and they're going through transmission.

## 04:05

Now,

## 04:06

that particular geometry is well approximated

## 04:10

by one-dimensional along the x-axis

## 04:13

if that's our beam line.

## 04:15

It turns out diffusion theory sucks

## 04:17

for that particular problem,

## 04:19

right,

## 04:20

but that's one application of where a geometry

## 04:22

like the one we're talking about would be applicable.

## 04:26

1D is also easy

## 04:28

to do compared to 2D and 3D,

## 04:31

right,

## 04:32

so it's a good thing for us to learn,

## 04:34

and Cartesian coordinates in particular

## 04:36

are much easier than,

## 04:37

say, cylindrical or spherical coordinates,

## 04:40

right,

## 04:41

and the reason for that

## 04:42

is the type of differential equation

## 04:44

that Cartesian coordinates leads to,

## 04:46

and we'll talk about that

## 04:48

in the next pseudo slide,

## 04:49

but first of all,

## 04:50

are there questions related to the homework

## 04:52

that is due this evening?

## 04:55

I had a number of folks in office hours yesterday,

## 04:57

and it's one of those things

## 04:59

where the problem basically introduces you

## 05:02

to the mechanics of some of the terms

## 05:04

that we saw last time,

## 05:06

right,

## 05:07

with vectors,

## 05:08

the current,

## 05:09

the leakage through faces.

## 05:10

It's one of those things

## 05:11

where you just have to dive in

## 05:12

and kind of play with the numbers

## 05:13

to get a sense for it,

## 05:14

so hopefully you can do that,

## 05:16

but no questions?

## 05:19

We're making progress?

## 05:22

Has everyone started?

## 05:23

Actually,

## 05:24

hopefully you have,

## 05:25

okay,

## 05:26

but once you get going,

## 05:27

it shouldn't take you too long

## 05:29

to do that.

## 05:37

All right,

## 05:38

so as I typically do,

## 05:40

I pre-populate some of the stuff

## 05:41

so that I don't have to sit

## 05:43

and write the whole time,

## 05:44

and I can talk a little bit more,

## 05:45

but just to clarify

## 05:47

what we're doing with the term,

## 05:50

this nabla or del, right,

## 05:52

this is called the Laplacian,

## 05:54

and that comes from,

## 05:55

this operation, right?

## 05:57

As I was talking to folks

## 05:58

in office hours about this,

## 06:00

this Laplacian is really

## 06:02

a dot product of two vectors, okay?

## 06:05

The vectors in this case

## 06:06

have functional components, right?

## 06:08

It's not just numbers.

## 06:09

It's actually like a derivative

## 06:10

of that in this case,

## 06:12

but when you break it down

## 06:13

into this structure,

## 06:15

you get two,

## 06:17

three component vectors

## 06:19

dotted with each other,

## 06:20

and if you remember,

## 06:21

the dot product takes this term

## 06:23

times this term,

## 06:24

this term times this term,

## 06:25

adds it up,

## 06:26

the result is this,

## 06:27

but what is missing in that,

## 06:29

if I can get my pen,

## 06:31

would be the del operator,

## 06:36

which applied to a function

## 06:37

as a gradient,

## 06:38

but del by itself

## 06:39

is just the vectorized

## 06:40

partial derivatives, right?

## 06:42

So that would be del, del x,

## 06:45

del, del y,

## 06:48

and then I guess I didn't

## 06:49

leave myself enough room there,

## 06:50

so I'll put it beforehand,

## 06:51

del, del z,

## 06:53

and then the second,

## 06:54

the second vector

## 06:56

is del operating on f,

## 06:58

which that's the,

## 06:59

that's what we call the gradient, right?

## 07:01

So we still have the del, del x,

## 07:03

but now it's del f,

## 07:06

del x, del f,

## 07:09

del y, and del f,

## 07:12

del z, right?

## 07:14

So that's the gradient of f.

## 07:16

This is the del operator.

## 07:17

You dot them together,

## 07:18

which gives you the so-called Laplacian,

## 07:20

and you get this thing here,

## 07:22

okay, right?

## 07:23

Very, very common form

## 07:26

in a lot of physics models, right,

## 07:29

that end up being second order

## 07:31

partial differential equations.

## 07:33

You see this in the wave equation.

## 07:34

You see this in Schrodinger's equation,

## 07:36

which is a type of wave equation.

## 07:38

You see it in the heat conduction equation.

## 07:40

If you're doing it in 3D,

## 07:41

you see it here, of course,

## 07:43

in the neutron diffusion equation

## 07:45

where f would be replaced with f.

## 07:47

So what we're going to do now

## 07:49

is assume a constant d, right?

## 07:51

The reason for that is,

## 07:52

I can't just use the Laplacian

## 07:55

in the diffusion equation

## 07:57

unless d is constant,

## 07:59

because if you remember,

## 08:01

that first part of the diffusion equation

## 08:03

looks like minus del dr

## 08:10

and then del phi, right?

## 08:13

This is like a derivative,

## 08:14

then the function,

## 08:15

then the derivative.

## 08:16

We'd have to use the product rule, right,

## 08:19

or whatever the equivalent would be

## 08:21

in multiple dimensions.

## 08:22

So if we assume d is constant,

## 08:23

then the spatial derivative of d,

## 08:25

it just pulls right out, okay?

## 08:28

So if we assume constant d,

## 08:30

then what we have is minus d,

## 08:33

and then because now we're in one dimension,

## 08:37

we can replace the partial

## 08:39

with a regular derivative,

## 08:41

and so we have the second derivative

## 08:44

of the flux with respect to x.

## 08:49

So all this is to say,

## 08:53

we start off with sort of a full derivative,

## 08:55

you know,

## 08:56

a full specified three-dimensional vectorized approach,

## 08:59

and when we say that we're going to go

## 09:01

to just one Cartesian coordinate,

## 09:03

all of that sort of simplifies to this,

## 09:06

where we've assumed a constant value

## 09:08

for the diffusion coefficient, okay?

## 09:11

So one way to kind of motivate

## 09:17

why you could write this down in the first place

## 09:19

is think of the example flux

## 09:22

that I gave you for the homework due today.

## 09:24

It's a function of x and y, right?

## 09:27

So when you plugged it in

## 09:28

to the full gradient,

## 09:30

what was your derivative with respect to z?

## 09:32

What was that z component of your current?

## 09:35

Zero.

## 09:36

Zero, right?

## 09:37

So if you have a solution

## 09:39

that is only a function of x or x and y,

## 09:43

the z component will just go away, right?

## 09:46

Even if you put it into your original equation,

## 09:48

you will just have that.

## 09:49

So you can, by assumption,

## 09:51

assume that your flux does not depend on y and z,

## 09:54

then you get to this, right?

## 09:56

And where would you assume that?

## 09:58

Where you have,

## 10:00

where you know that the variation along the x-axis,

## 10:03

for instance,

## 10:04

is significantly greater than in the y and z dimensions,

## 10:08

like this thin foil that I talked about, right?

## 10:12

Diffusion is not great for that particular problem,

## 10:14

but in real-world systems,

## 10:18

where would one be?

## 10:21

So there are some reactors that use plate-style fuel, right?

## 10:26

Where it's actually just like a finite thickness plane,

## 10:29

actually the MIT research reactor uses plate fuel.

## 10:32

Their core is not a plate,

## 10:34

but they have assemblies of plate fuel.

## 10:37

So think of the unit cell analysis that we did powered by OpenMC.

## 10:41

We did the cylinder within the water box

## 10:44

or the coolant-filled box.

## 10:46

If I were to do a unit cell analysis of the MIT reactor fuel,

## 10:50

I would probably do it with a one-dimensional approximation, right?

## 10:54

Probably also in OpenMC or something like that,

## 10:57

where I have reflection to capture,

## 10:59

or to account for the y and z dimensions, right?

## 11:02

So there are real systems that are reasonably well-approximated by 1D.

## 11:07

So for our purposes,

## 11:09

it's not that we're trying to model anything with great fidelity.

## 11:13

It's because it's easier to do, right?

## 11:16

And we'll be able to get some good understanding from it, okay?

## 11:22

Why would we assume a constant D?

## 11:27

I put this bubble here

## 11:30

because I wanted to remind myself

## 11:32

that we should be thinking about that assumption as well.

## 11:36

In an actual system with the diffusion coefficient,

## 11:39

which we know is a function of the total cross-section

## 11:42

or the transport cross-section,

## 11:44

is that ever going to be constant?

## 11:51

Well, nothing in life is constant,

## 11:53

as I found out in my many years being on Earth.

## 11:56

But yeah, sure, it could be constant, right,

## 11:58

if you have a uniform material.

## 12:00

But we also know that in a real reactor,

## 12:02

things like temperature matter.

## 12:04

So if you imagine you have a fuel element

## 12:06

or a moderator,

## 12:08

like the temperature gradients

## 12:10

are going to cause material properties to be non-constant.

## 12:15

So will D ever actually be constant?

## 12:18

In reality, no.

## 12:20

But what we can do is treat it as piecewise constant

## 12:23

so that when we get next week to multiple regions,

## 12:26

we can assume each region has its own diffusion coefficient.

## 12:29

And we'll do the same thing for the absorption coefficient

## 12:32

or cross-section.

## 12:33

And other things.

## 12:35

And the reason we would do that is,

## 12:37

one, it simplifies things, of course.

## 12:39

And to be honest,

## 12:41

the variation in something like the diffusion coefficient

## 12:44

or the absorption coefficient that we would want in practice

## 12:48

is so small compared to,

## 12:51

it's a small variation compared to being constant.

## 12:54

And I would say if there's anything specific

## 12:57

that you need to know about a solution

## 13:00

subject to something that's non-constant,

## 13:02

you have gone into the realm of

## 13:05

it's not worth doing it by hand.

## 13:07

Right?

## 13:08

If you're trying to find some nuanced physical impact

## 13:11

of a non-constant diffusion coefficient

## 13:13

for the case where, like in practice,

## 13:15

it actually would vary,

## 13:16

not just some textbook problem to make your life miserable,

## 13:19

then I say you should be using something else.

## 13:21

You should be using a tool for that.

## 13:23

But for the case of constant values,

## 13:25

that gives us a set of problems

## 13:27

that we can actually do by hand

## 13:29

and extract some physical intuition from it.

## 13:31

Right?

## 13:32

So I don't do math for the sake of math,

## 13:34

which is a concept that I absolutely hate.

## 13:37

So let us proceed.

## 13:43

All right.

## 13:44

So just talked about the constant sigma A,

## 13:46

which goes with the sigma D.

## 13:48

And what's super nice about that

## 13:50

is in this one-dimensional planar geometry,

## 13:54

we're assuming everything is along the x-axis,

## 13:57

which means our domain is like a finite slab of material

## 14:01

that's infinite in the y and z dimensions.

## 14:03

Okay?

## 14:04

That's why it's often called plane.

## 14:06

I guess if somebody was telling me

## 14:07

about the heat transfer stuff that you were doing,

## 14:09

you often did one-dimensional problems, right?

## 14:12

And I think you called that planar.

## 14:15

Is that what it was called?

## 14:17

I can't remember the nomenclature from every other class,

## 14:19

but in any way, this is what we have.

## 14:22

So once we make those assumptions

## 14:24

about the coefficients D and sigma A being constant, right?

## 14:27

It doesn't matter what is on the right-hand side.

## 14:29

That can be any function of x.

## 14:31

But if we assume that the coefficients are constant,

## 14:33

then the neutron diffusion equation

## 14:37

is fill in the blanks for me.

## 14:40

What order equation is it?

## 14:43

It's second order, right?

## 14:45

Where does that come from?

## 14:48

Second derivative, right?

## 14:50

So we've got a second order.

## 14:53

Okay.

## 14:54

What other property does this have?

## 14:58

Ordinary.

## 15:00

So it's ordinary and that's tucked into the ODE.

## 15:03

So as ordinary as opposed to partial, right?

## 15:06

What other important descriptor

## 15:10

have you might have heard for differential equations?

## 15:15

It's not separable.

## 15:17

It would be nice if it were,

## 15:18

because then things would be super easy, right?

## 15:21

Do you see, so our unknown here is the flux, okay?

## 15:26

We see derivatives of the flux.

## 15:27

We see the flux itself.

## 15:28

Do we see any flux squared terms, right?

## 15:31

Or square root of the flux?

## 15:33

So it's linear, right?

## 15:35

It's linear combinations of the unknown or derivatives thereof, okay?

## 15:40

That's important because if it were nonlinear,

## 15:43

we wouldn't be able to solve it, right?

## 15:45

There might be some very special cases that we could solve,

## 15:48

but in general, nonlinear differential equations are beasts, right?

## 15:53

Okay.

## 15:54

And then constant coefficients.

## 15:57

Okay.

## 15:59

So any higher order linear ODE with constant coefficients,

## 16:02

is a super nice thing to work with, okay?

## 16:07

Because the solution is always a sum of exponentials,

## 16:13

with the exception that sometimes you have to add in the independent variable X

## 16:19

in our case and multiply that by an exponential.

## 16:22

So you might have E to the something and then X times E to the something.

## 16:26

Maybe that rings a distant bell, right?

## 16:28

It's related to the system of first order equations that we have.

## 16:31

Remember we talked about prompt neutrons

## 16:34

and then the delayed neutron precursors.

## 16:36

We found that those solutions were also exponential

## 16:39

when rho was a constant function, okay?

## 16:43

So all this, you can go back to your math class

## 16:46

and kind of motivate for yourself why it's exponentials,

## 16:49

but because it's constant coefficients,

## 16:51

that's what leads to exponentials as the solution,

## 16:54

which means you can always just assume E to the alpha X in our case,

## 16:59

plug it in,

## 17:00

and you'll get your possible answers, okay?

## 17:03

So if things are not constant coefficients, right,

## 17:07

if instead we had X times sigma A times phi of X,

## 17:12

we can still solve it,

## 17:14

but the solution won't be exponentials, right?

## 17:18

In fact, if we were to do this for cylindrical coordinates, right,

## 17:21

we'd have a slightly different form for the diffusion equation

## 17:24

as a function of whatever our one-dimensional variable is,

## 17:27

probably the radius, okay?

## 17:29

And if we do that,

## 17:30

we would end up with solutions that were not exponentials,

## 17:33

but instead,

## 17:35

anybody know what the solution to cylindrical problems usually deals with?

## 17:40

True.

## 17:42

Close.

## 17:43

They're nasty functions, kind of like trig functions,

## 17:45

but even nastier.

## 17:46

They're called Bessel functions, okay?

## 17:48

And if we go to the spherical domain,

## 17:50

the solutions are spherical Bessel functions, right?

## 17:54

So when we're dealing with,

## 17:56

when we have constant coefficients,

## 17:57

things are so much easier

## 17:58

because it's exponentials,

## 18:00

and exponentials, as it turns out,

## 18:01

that's the same things as sine and cosines,

## 18:03

that's the same things as the sinches and coshes,

## 18:06

depends on the application,

## 18:07

which you should choose,

## 18:08

but it's exponentials.

## 18:09

So exponentials are something that we're familiar with.

## 18:12

So let's work through an example.

## 18:16

So we're going to be tackling this thing

## 18:17

for the rest of our time today.

## 18:19

Hopefully we get through it, right?

## 18:21

But it should set you up pretty well

## 18:22

for the homework due Monday.

## 18:25

What we're going to do is consider

## 18:27

the slab of material from negative a to a.

## 18:31

I've centered it at x equals zero

## 18:33

because sometimes symmetry is our friend

## 18:35

when solving problems.

## 18:37

What's nice is if you have a slab of width,

## 18:40

whatever, to call it w,

## 18:42

it's up to you, the modeler, right,

## 18:44

the problem solver,

## 18:45

to situate it on the x-axis the way you want.

## 18:48

Here, I'm giving that to you.

## 18:49

You might choose to explore other ways to set it up, okay?

## 18:53

So we're going to assume constant d and sigma a,

## 18:56

and we're going to take our source term

## 18:59

to be that thing in the upper right that's blue.

## 19:01

It's a combination of a constant, the one,

## 19:04

and then a symmetric cosine.

## 19:06

I say symmetric because it's symmetric

## 19:08

about the x equals zero, right?

## 19:10

And I've sketched out one possible shape

## 19:15

for that flux, right,

## 19:16

for a b that's not equal to zero, for instance.

## 19:19

Maybe that's b over one, okay?

## 19:21

We're going to assume that the flux at negative a

## 19:24

is equal to phi sub a,

## 19:26

and the flux at plus a is equal to phi sub r.

## 19:30

Now, a detailed discussion of boundary conditions

## 19:33

is what we'll do on Monday for the same equation,

## 19:37

but it should seem reasonable

## 19:39

that we have to set something, right?

## 19:41

I mean, we could keep it with undetermined coefficients,

## 19:44

and that's fine,

## 19:45

but it's hard to plot things

## 19:46

if you don't have your coefficients set.

## 19:48

So we'll just set the flux to some value,

## 19:49

and this is the simplest way to do it,

## 19:51

just define what those values are

## 19:53

on the left and right, okay?

## 19:55

And then when we get done with everything,

## 19:57

we're going to go ahead and plot it,

## 19:58

and we'll specifically do that for the case

## 20:00

where the fluxes vanish at the boundaries, right?

## 20:03

So phi l and phi r go to zero,

## 20:05

so I can actually write that too.

## 20:08

So phi l equals phi r equals zero, right?

## 20:14

Okay, so first of all, what are the equations?

## 20:17

If I'm going to go through the problem-solving process,

## 20:30

I have to start with something.

## 20:32

I know it was just there in the previous page,

## 20:34

but what is my starting point?

## 20:38

The diffusion equation, right?

## 20:40

So I can write it like it is in the book.

## 20:44

Where is my...

## 20:46

There it is, okay.

## 20:48

But I'm going to make a substitution,

## 20:50

the same one that's made in the book.

## 20:52

So let's say that l, the diffusion length,

## 20:55

is equal to d over sigma a.

## 20:58

I guess we could say that l squared is d over sigma a, right?

## 21:02

So that l is equal to...

## 21:04

l is equal to the square root of d over sigma a.

## 21:08

And then I can rewrite my diffusion equation

## 21:10

as minus d squared phi dx squared

## 21:18

plus 1 over l squared times phi of x.

## 21:26

And then we have whatever our source term is

## 21:29

on the right-hand side.

## 21:30

I won't write that out.

## 21:31

I'll wait to the next slide.

## 21:32

Okay.

## 21:33

And that should be divided by d.

## 21:35

Okay.

## 21:36

And then subject to phi at minus a is equal to phi l,

## 21:42

and phi at plus a is equal to phi r,

## 21:46

l and r for left and right, of course.

## 21:48

Yeah.

## 21:51

So those are the equations.

## 21:52

Now, why would we switch to this term l, right,

## 21:56

the diffusion length?

## 21:58

As you'll see, that symbol l will show up in our solutions, right?

## 22:04

We're going to deal with exponentials,

## 22:07

and we're going to have exponentials that have l in that exponent, right?

## 22:11

So it's sort of a...

## 22:13

We're helping ourselves out by reorganizing the equation.

## 22:16

And it turns out the diffusion length has physical meaning, right?

## 22:19

And there's a whole section in this chapter in the book that discusses l.

## 22:24

I won't cover that now.

## 22:25

We'll just use it kind of as a mathematical trick

## 22:29

to simplify things just a little bit.

## 22:36

So the trick with solving equations like this

## 22:45

is to figure out a solution

## 22:48

that satisfies both the boundary conditions

## 22:52

and the forcing function,

## 22:54

the inhomogeneous term.

## 22:56

When I say inhomogeneous term,

## 22:58

that means anything in the equation

## 23:00

that isn't multiplied by the flux

## 23:03

or a derivative of the flux, okay?

## 23:06

These are things that are injecting something into the system.

## 23:09

In our case, it's a source of neutrons, right?

## 23:13

So the first thing we do is to find the homogeneous solution, right?

## 23:18

And that's to set that right-hand side equal to zero.

## 23:21

So what we're trying to solve then is this equation, right?

## 23:26

d phi h dx squared minus 1 over l squared.

## 23:33

I'm flipping the sign around a little, okay?

## 23:36

phi h of x.

## 23:39

It's equal to zero.

## 23:41

I know that in the book they use the g subscript,

## 23:45

but I'm an old dog who doesn't want to learn this new trick,

## 23:48

so I'm going to call it h for homogeneous, right?

## 23:51

And it's said in the book

## 23:53

that it's sometimes called the homogeneous solution.

## 23:56

And the reason for that is it's homogeneous

## 23:58

because you remove the inhomogeneities, right?

## 24:01

The right-hand side forcing function, okay?

## 24:04

Now, I've already said that the solution to this

## 24:07

is going to be an exponential,

## 24:08

but if you look at this carefully,

## 24:10

there's got to be some easy relationship

## 24:12

between the function phi of h,

## 24:15

whatever our homogeneous solution is,

## 24:17

and its second derivative, right?

## 24:19

And we're already aware of a number of functions

## 24:21

that have special relationships,

## 24:23

like cosine of x.

## 24:25

Take its second derivative.

## 24:27

You get cosine of x back with a minus sign.

## 24:29

And then if you have something in with the x,

## 24:31

cosine of ax,

## 24:32

well, then you get a squared times minus cosine of x

## 24:35

when you plug it into the second derivative.

## 24:37

So in this case, we have,

## 24:41

if we separated it

## 24:42

and put the one over l squared phi h

## 24:46

on the right-hand side,

## 24:47

then we'd have to have the second derivative

## 24:49

matching the sign of the original function, right?

## 24:53

So that suggests in this case

## 24:55

that we're not going to have sinusoidal behavior, right?

## 24:58

That would probably be the wrong.

## 25:00

Now, we could substitute it.

## 25:01

We could put a cosine in,

## 25:03

and as long as we put an i in,

## 25:06

things would work.

## 25:07

Right?

## 25:08

Because if you put an i in a cosine,

## 25:10

well, anyway,

## 25:11

but it'll be an exponential.

## 25:13

And cosines, cinches,

## 25:15

all those functions can be defined

## 25:17

in terms of exponential.

## 25:18

So do you remember the trick for proceeding?

## 25:21

How do you find the constant

## 25:23

that goes in the exponent of the exponential?

## 25:27

Well, we don't know.

## 25:28

I mean,

## 25:29

by the time you get through a couple of these problems,

## 25:31

you'll just kind of know what you're looking for.

## 25:33

But the idea is first to say,

## 25:35

hey,

## 25:36

I'm going to set,

## 25:37

you know,

## 25:38

my function to be equal to e to the alpha x.

## 25:45

Right?

## 25:46

I'm going to take this function,

## 25:47

e to the alpha x,

## 25:48

and I'm going to plug it in.

## 25:49

So if I do that,

## 25:50

what do I get?

## 25:51

I get alpha squared

## 25:54

times e to the alpha x

## 25:58

minus

## 26:00

1 over l squared

## 26:02

times e to the alpha x

## 26:05

equal 0.

## 26:06

Right?

## 26:07

Now, e to the alpha x is never 0,

## 26:09

so I can divide by it.

## 26:11

And that means I just cancel it out,

## 26:14

which means then that alpha squared

## 26:19

is equal to 1 over l squared,

## 26:25

which means that alpha is equal to plus or minus 1 over l.

## 26:34

Right?

## 26:35

Plus or minus the square root of 1 over l squared,

## 26:37

which just is 1 over l.

## 26:38

Okay?

## 26:39

So that means that my homogeneous solution,

## 26:43

I can actually move some of this stuff up a little bit.

## 26:46

Okay?

## 26:47

My homogeneous solution is going to be some combination

## 26:50

of an exponential with the plus 1 over l

## 26:53

and then with the minus 1 over l.

## 26:57

Right?

## 26:58

And so we can write this like that.

## 27:02

Plus,

## 27:04

let me

## 27:06

do this,

## 27:07

e to the,

## 27:08

the x over l plus c1 e to the minus x over l.

## 27:15

Okay?

## 27:16

So that's,

## 27:17

that's step one.

## 27:19

And in a sense,

## 27:20

that's the easy part because that will be the same,

## 27:23

no matter what the problem is,

## 27:25

as long as it's one dimensional,

## 27:28

you've got constant coefficients and you're in Cartesian coordinates.

## 27:31

So slab geometry,

## 27:32

this will always be the homogeneous solution.

## 27:35

Now,

## 27:36

if it turned out that,

## 27:38

l squared was complex,

## 27:41

right?

## 27:42

Then you've got i's that show up.

## 27:43

You're squaring i's.

## 27:44

When you square i,

## 27:45

what do you get?

## 27:46

Negative 1.

## 27:47

So I've written it like this,

## 27:49

where I have the second derivative minus this coefficient times the,

## 27:52

the function.

## 27:53

If l squared were,

## 27:55

imagine it was just a constant times i.

## 27:58

i squared is minus 1.

## 27:59

That would pop out the minus sign.

## 28:01

And I'd be back to this thing where I'd need a cosine or a sine

## 28:06

to knock out that second derivative.

## 28:07

Right?

## 28:08

In our case,

## 28:09

though,

## 28:10

l is d over sigma a or square root of that.

## 28:13

Will that ever be negative?

## 28:15

Would it ever make sense to have a diffusion coefficient,

## 28:21

which we saw before is 1 over 3 times this transport cross section.

## 28:25

Could that ever be negative?

## 28:27

Not,

## 28:28

not in a world in which I live anyway,

## 28:30

right?

## 28:31

Same thing for the,

## 28:32

the absorption cross section.

## 28:33

That should never be negative either,

## 28:34

right?

## 28:35

Weird things would happen if things went to zero,

## 28:37

right?

## 28:38

I don't care about that.

## 28:40

So l squared will always be positive.

## 28:43

For how we,

## 28:44

I was real and positive,

## 28:46

right?

## 28:47

Things would happen if it weren't.

## 28:49

In fact,

## 28:50

when we get to the end of the chapter and we bring back in multiplication

## 28:55

with that new Sigma app,

## 28:58

that's going to end up changing things.

## 29:00

And it could be the case then that that sign will flip and that our

## 29:04

fundamental solution still being an exponential would be better written as

## 29:07

signs and cosines.

## 29:08

Okay.

## 29:09

So keep that,

## 29:10

I guess,

## 29:11

tucked away in your minds for when we revisit that sometime,

## 29:14

probably the next week.

## 29:15

Okay.

## 29:16

Anyway,

## 29:17

so this is our,

## 29:18

our homogeneous solution.

## 29:19

Now,

## 29:20

what do we do with that?

## 29:21

Well,

## 29:22

there's one step.

## 29:25

We've got to account for that source term first.

## 29:27

So there was a question in the,

## 29:29

in the notes that,

## 29:30

that you're sending me,

## 29:31

like,

## 29:32

why do we have to do this homogeneous solution in the first place?

## 29:35

Well,

## 29:36

it's,

## 29:37

it's,

## 29:38

it's,

## 29:39

it's a pretty good question.

## 29:40

So,

## 29:41

so the homogeneous solution,

## 29:45

the,

## 29:46

what does a homogeneous solution give us?

## 29:48

If you put it back into the diffusion equation,

## 29:55

what do you get on the right-hand side?

## 29:57

You get zero,

## 29:58

right?

## 29:59

Cause that's what you started with on the right-hand side.

## 30:01

The homogeneous solution is the solution to the diffusion equation when

## 30:04

you have zero on the right-hand side.

## 30:06

So what's funny is we can take the solution,

## 30:08

plug it right back into the diffusion equation.

## 30:10

And we,

## 30:11

it goes to zero,

## 30:12

which makes you think,

## 30:13

have we done anything?

## 30:14

Well,

## 30:15

what it's done is it's given us two degrees of freedom,

## 30:16

right?

## 30:17

So,

## 30:18

you know,

## 30:19

if we plug this in here,

## 30:20

C2,

## 30:21

my bad,

## 30:22

right?

## 30:23

When we plug this in,

## 30:24

in order to capture the source term,

## 30:26

we're going to need these two degrees of freedom to satisfy the boundary

## 30:30

conditions,

## 30:31

right?

## 30:32

So really just gives us,

## 30:34

it gives us flexibility.

## 30:36

Okay.

## 30:37

Now,

## 30:38

what it doesn't account for is the fact that we do have this right-hand

## 30:41

side.

## 30:42

So we're going to need to get a particular solution.

## 30:45

That we had,

## 30:46

it was minus D times D square fee,

## 30:51

D X squared plus Sigma a times fee X.

## 30:57

And our source term was one plus B cosine of PI times X over two

## 31:06

a.

## 31:07

Okay.

## 31:08

And then if we were to put it in terms of L,

## 31:11

we could do minus,

## 31:14

let me actually adopt this note nomenclature.

## 31:17

You've seen the double prime for a second derivative before,

## 31:20

I believe.

## 31:21

So that's still saved me a little bit of time.

## 31:24

Okay.

## 31:25

And then I have one over L squared times fee of X.

## 31:30

And then I have one over D plus B over D cosine.

## 31:39

Okay.

## 31:40

All right.

## 31:45

Now,

## 31:46

okay.

## 31:47

So let's do this.

## 31:48

We already know that if I plug in my homogeneous solution to this

## 31:50

left-hand side.

## 31:51

That evaluates to zero.

## 31:53

So I'm still stuck with zero is equal to this thing on the right-hand

## 31:56

side.

## 31:57

Right?

## 31:58

So I've got to come up with some way to handle that.

## 31:59

Now I've underlined there.

## 32:02

The method of undetermined coefficients,

## 32:04

which like many topics for math is given like this big formal name.

## 32:08

That maybe helps you remember it.

## 32:10

Right.

## 32:11

But if I could describe the method in plain English,

## 32:14

it's this.

## 32:15

Assume that.

## 32:16

Assume that your particular solution looks like your right-hand side.

## 32:23

Plug it in.

## 32:24

And then solve for.

## 32:26

Undetermined coefficients that you use to scale each term.

## 32:29

And what do I mean by that?

## 32:30

If I have a right-hand side,

## 32:32

that looks like this.

## 32:34

Okay.

## 32:35

It consists of two terms,

## 32:37

one over D.

## 32:38

So that's a constant.

## 32:39

Okay.

## 32:40

And then I have the B over D times this cosine term.

## 32:42

So a sinusoid.

## 32:44

What I'm saying in the undetermined coefficient method is let's assume a

## 32:48

particular solution.

## 32:50

Of the form.

## 32:51

C3.

## 32:55

A constant.

## 32:57

Plus C4.

## 32:59

Times.

## 33:01

The functional form.

## 33:03

That.

## 33:04

Is.

## 33:05

The cosine.

## 33:06

So we'll have a cosine.

## 33:08

Pi X.

## 33:09

Two.

## 33:10

A.

## 33:11

Okay.

## 33:12

Now.

## 33:14

In general.

## 33:15

If you are doing this method.

## 33:17

And one of the functional forms.

## 33:19

Is a cosine.

## 33:20

On the right-hand side.

## 33:21

It's good practice.

## 33:22

To put the.

## 33:23

Sort of the pair function with it.

## 33:25

So you think a cosine.

## 33:26

You should.

## 33:27

Maybe try putting a sign as well.

## 33:29

So we would do this.

## 33:30

And put a sign.

## 33:31

Hi.

## 33:32

X.

## 33:33

Two.

## 33:34

A.

## 33:35

Right.

## 33:36

Because if you go through all of this,

## 33:37

you plug it in.

## 33:38

It might be the case that you can't.

## 33:39

Find.

## 33:40

A.

## 33:41

S.

## 33:42

S.

## 33:43

S.

## 33:44

A.

## 33:45

B.

## 33:46

S.

## 33:47

B.

## 33:48

S.

## 33:49

S.

## 33:50

Q.

## 33:51

S.

## 33:52

For this case that does not always.

## 33:54

That is not always going to be the case,

## 33:55

but because.

## 33:56

Time limited in.

## 33:57

A.

## 33:58

Situations like this.

## 33:59

I'm going to say that not needed.

## 34:00

Okay.

## 34:01

So we're left with.

## 34:02

This form.

## 34:04

Now,

## 34:07

if I plug this in.

## 34:08

To the.

## 34:09

Original equation.

## 34:12

Right.

## 34:13

That.

## 34:14

Bismalt from the.

## 34:15

başka.

## 34:16

then what I hope I can do is pick out some patterns

## 34:21

and figure out what these two coefficients are, okay?

## 34:24

If I'm able to recognize something, then great.

## 34:27

If I plug it in and I don't have a way to define one of them,

## 34:31

that means I'm missing some sort of term, okay?

## 34:33

But in general, this ought to work.

## 34:35

So if I plug the particular solution in, okay, what do I get?

## 34:41

So I have d squared dx squared of c3 plus c4 cosine pi x over 2a.

## 34:55

And then I have 1 over l squared times c3 plus c4 times cosine pi x over 2a.

## 35:09

And this has to be equal to what I have.

## 35:12

On the right-hand side, the 1 over d plus bd cosine pi x over 2a.

## 35:21

Adjust this a little bit, okay?

## 35:24

Well, the second derivative of a constant is 0, right?

## 35:31

And then I have a c4 times, what's the second derivative of this cosine term?

## 35:41

Yeah, so I'm going to get a negative, right?

## 35:43

And then what pops out of the cosine when I take its derivative?

## 35:46

Yeah, I get a pi over 2a, but because I'm taking it twice, I get that quantity squared.

## 35:54

So I have pi over 2a squared, and then this is multiplied by my original function, okay?

## 36:05

And then I have this c3 over l squared plus c4 over l squared times the cosine term.

## 36:16

And then this is equal to the same right-hand side.

## 36:22

Now,

## 36:23

this is where we can use sort of just inspection, right?

## 36:29

We look at it.

## 36:30

If I see on the left-hand side, the only term that I have that's constant is c3 over l squared.

## 36:37

And if I take that and match it on to this term, then I have an equation for c3, okay?

## 36:47

Likewise, I can bundle up the cosine terms.

## 36:53

And say that this is cosine of pi x over 2a, right?

## 37:01

I've got a c4 over l squared, and then I'm subtracting a c4 times this pi term.

## 37:14

c4 times pi over 2a squared, okay?

## 37:21

And what that leaves me with is this term.

## 37:28

And this term has to go with this, right?

## 37:36

So as long as your particular solution, your form, is a sum of what I would call independent terms,
right?

## 37:45

Linearly independent things that are obviously not scalar multiples of each other, you can pick out
the coefficients.

## 37:51

Now, does this process feel familiar?

## 37:55

Obviously, in the book, there's an example of it for a slightly simpler case than this.

## 37:59

But it's a process.

## 38:01

And it's one of those things that I think you would have had to do more than once, okay?

## 38:06

So what does this give us for our coefficients?

## 38:10

Can somebody tell me what c3 must be?

## 38:21

Yeah.

## 38:22

L squared.

## 38:25

L squared over d.

## 38:27

And what is c4?

## 38:29

c4 must be b over d divided by the term 1 over l squared minus.

## 38:46

Actually, that shouldn't be a minus.

## 38:47

That should be a minus.

## 38:47

That shouldn't be a minus.

## 38:47

That shouldn't be a minus.

## 38:47

That should be, did I forget my minus sign?

## 38:52

There's my minus sign.

## 38:53

So that should be a plus.

## 38:55

That should be a plus, okay?

## 38:58

All right.

## 38:59

So this means that c4 is equal to b over d.

## 39:03

That's this term here in front of the cosine, right?

## 39:06

And divided then by 1 over l squared.

## 39:16

That's this thing here.

## 39:17

Plus pi over 2a squared.

## 39:21

Right?

## 39:22

Plus pi over 2a squared, okay?

## 39:33

Now, we could certainly manipulate it a little bit, maybe get it somewhat nicer looking.

## 39:39

I don't think there's anything wrong with that particular way of writing it.

## 39:43

Yeah.

## 39:44

So that's it for the particular solution.

## 39:47

Now, if you were a good child and you get your solution, particular solution, c3 and c4, the
coefficients, what should you do?

## 40:01

What can I do?

## 40:02

Bug them in and make sure that everything is still hunky-dory, right?

## 40:05

We won't do that here because I already did this and it's the same thing I got in my notes.

## 40:09

So I've done it twice.

## 40:10

It would be really sad if I got it wrong both times.

## 40:13

Okay.

## 40:14

All right.

## 40:15

So that's our particular solution.

## 40:17

So now what we need to do is apply the boundary conditions to get our c1 and c2 to the homogeneous
equation.

## 40:26

So if we didn't have boundary conditions specified, we're done, right?

## 40:30

There's nothing more that we could do.

## 40:32

In order to define what c1 and c2 should be in our homogeneous solution, right?

## 40:37

We've got the particular solution, and then the homogeneous solution would be there to handle any
boundary condition that we could apply.

## 40:44

Okay.

## 40:44

So if we apply these boundary conditions to find c1 and c2, what does that require we do?

## 40:52

Well, we have to take our full solution.

## 40:54

Our full solution is phi of x is equal to the homogeneous solution.

## 41:02

Plus the particular solution, okay?

## 41:05

And so for the boundary condition at x equal minus a, what we're saying is that phi of minus a is
equal to whatever that left boundary condition was.

## 41:22

So we have to plug in minus a to this expression in order to come up with an equation, right?

## 41:28

So just to remind ourselves where we are.

## 41:36

Okay.

## 41:36

This thing is c1 times e to the x over l plus c2 e to the minus x over l plus c3 plus c4 times
cosine of pi x over 2a.

## 42:00

Okay.

## 42:00

The nice thing is with the coefficients, the c3 and c4, we don't actually have to keep writing every
single.

## 42:06

term out, right?

## 42:07

Because c4 was obviously sort of ugly.

## 42:09

There's no point in writing it.

## 42:11

Until you get to the end and you really want to do some simplification, just keep it in terms of the
coefficient because you know you've already solved them, right?

## 42:18

That's especially true if what I, like in the homework, what I say to do is plot it, right?

## 42:24

Way easier if you keep it in this term because then in your code, you can say c1 is equal to this,
c2 is equal to this, c3 is equal to this, c4 is.

## 42:31

And then you add the terms together and the code becomes a lot cleaner.

## 42:36

And if the code is cleaner, that means your thought process was cleaner.

## 42:39

And that same clarity translates to pen and paper.

## 42:43

Okay.

## 42:43

So keep it, keep it organized like that.

## 42:45

All right.

## 42:47

So, so at that left boundary condition, we have c1 is equal e to the minus a sub l plus c2 e to the
positive a over l.

## 43:08

The constant is still a constant.

## 43:10

And now we have c4 cosine of pi times a over 2a, right?

## 43:18

So this represents one equation, but we can actually simplify it a little bit because cosine of pi
times a over 2 times a is cosine of pi over 2, which is, right?

## 43:31

That's, that's cosine of 90 degrees.

## 43:33

So that goes to zero.

## 43:34

So we don't have that.

## 43:36

And then similarly for our right-hand boundary condition, we have c1.

## 43:42

e to the positive a over l plus c2 times e to the minus a over l plus the same constant.

## 43:50

And for the same reason, the cosine term goes away.

## 43:53

So what we end up with is this boxed system of two unknowns, right?

## 44:05

If I wanted to, I could write it out like this.

## 44:08

I have e to the minus a over l e to the a l e to the a.

## 44:16

Now e to the minus a l c1, c2, and this would have to be equal to vl minus c3, and then vr minus c3,
okay?

## 44:36

So if you put it in matrix notation, you would have this.

## 44:40

Now, two-by-two system, totally straightforward to solve, right?

## 44:44

But as you can imagine with exponentials, you know,

## 44:47

the coefficient of the equation is going to be the same.

## 44:48

The coefficients end up being kind of ugly, right?

## 44:50

But you could do it.

## 44:52

For the special case that vl is equal to vr is equal to 0,

## 45:00

then it turns out that c1 is equal to c2 is equal to minus l squared times e to the a l over d.

## 45:14

e to the 2a.

## 45:18

Over l plus 1, okay?

## 45:26

And so this is the form that I'll use for plotting the solution, okay?

## 45:32

But you could do this for any possible value of phi l and phi sub r.

## 45:39

When we get to next lesson, we're going to talk about other boundary conditions, right?

## 45:43

It's usually not super physically meaningful to set the flux value to be a certain number,

## 45:50

at a certain location, right?

## 45:53

Because what are you trying to do with the flux?

## 45:56

Your purpose in taking the diffusion equation and solving it is to say what the flux is.

## 46:02

So it's usually more common to say things like, hey, I have no neutrons coming into my system,
right?

## 46:10

Sort of like, you know, like basically outside of a reactor, it's a vacuum, for instance.

## 46:15

So no neutrons coming in.

## 46:17

That boundary condition will have to do with the flux, but it actually relates to,

## 46:20

something called the partial current, which is another function of phi, right?

## 46:25

Related to the net current, okay?

## 46:27

Setting the flux to zero at some location is sort of like a,

## 46:32

just a sad version of a vacuum boundary condition, right?

## 46:38

And so we'll see how to do that correctly next time.

## 46:42

But this is a fairly straightforward way to handle it, okay?

## 46:47

So we have c1 and c2, right?

## 46:50

For the specific case of the fluxes vanishing, we have c3 and c4.

## 46:55

Is there anything else that we need?

## 47:02

No, that's it.

## 47:03

We've solved the diffusion equation.

## 47:05

It doesn't seem super satisfying yet because I haven't written down some nice,

## 47:09

clean form of the flux, but we don't need to do that.

## 47:12

We've got the coefficients.

## 47:13

I'm not a big fan of like, take this form for the flux and show that it's this form, right?

## 47:19

That's a very typical sort of textbook thing to do.

## 47:21

It's nice to be able to manipulate things.

## 47:23

Remember, trig identities and all that.

## 47:24

But what we need to be able to do is follow this process, right?

## 47:29

If you think about it, this is really an algorithm for solving differential equations,

## 47:33

right, of the sort that we're looking at.

## 47:36

So let's go ahead and see what the solution looks like, okay?

## 47:41

So I've got some code ready to go, okay?

## 47:45

So in my code, I'm making a function for the flux.

## 47:50

It takes in the x values and then my coefficients a, d,

## 47:54

sigma.

## 47:55

Along with b for the source term.

## 47:57

And just as I said a moment ago, I'm keeping things in terms of these coefficients, right?

## 48:02

So it makes for a significantly cleaner looking solution, okay?

## 48:07

So I get the c1 and c2, right, for the case of the flux vanishes at the boundary.

## 48:12

That's here, okay?

## 48:14

And then c3 and c4 for the particular solution.

## 48:17

And then I'm just returning the sum of the two exponentials with that constant

## 48:22

and then the cosine term, okay?

## 48:24

And so I'm just returning the sum of the two exponentials with that constant

## 48:24

and then the cosine term, okay?

## 48:25

And so I have that and then I can plot it.

## 48:31

So let me actually, I'll start with the case that b is equal to zero.

## 48:34

So that's just that constant source term, right?

## 48:37

So the source term is the orange curve here.

## 48:39

And then my flux solution is the blue thing, okay?

## 48:43

Now, if you look at it, I mean, one could argue that it's sort of parabolic looking.

## 48:49

It almost looks like it could be a cosine, but it is, I tell you,

## 48:54

not a cosine, right?

## 48:55

If anything, it would look like a Cauchy function because if we set b to zero,

## 49:00

this is just a constant source and that's identical to the problem in the book, right?

## 49:06

And I think you might have asked, like, no, but Clay,

## 49:09

maybe you pointed out something about the solution.

## 49:12

Like, how do you get these Cauchys and things?

## 49:14

Well, what is the hyperbolic cosine?

## 49:21

Yeah, it's a combination of the e to the plus thing,

## 49:25

and then the e to the minus thing.

## 49:26

And so because of symmetry, we have that,

## 49:30

and the solution will be a hyperbolic cosine, right?

## 49:33

So check the book for that.

## 49:35

I know many of you wrote down that problem in the solution,

## 49:37

but it's the same thing here.

## 49:39

And what I've showed you for the solution is not in terms of the hyperbolic cosines, right?

## 49:44

But those are just combinations of the exponentials.

## 49:47

So if I vary this and I add a little bit of the cosine term, right,

## 49:52

b is equal to one, then I have a solution that looks like,

## 49:56

obviously, it's gone higher in the middle because now my source term is higher, right?

## 50:01

And if I wanted to look at what it looks like if I make it negative, right,

## 50:07

this is what I had started with before.

## 50:10

And so at the middle of this lab, in this case, the source actually goes to zero, right?

## 50:15

Because I'm taking one minus that cosine.

## 50:17

So it goes to zero.

## 50:18

And so our flux takes on some sort of bizarre looking,

## 50:22

I don't know, it kind of looks like a smiling penguin, maybe.

## 50:26

I don't know, a frog.

## 50:28

I'm trying to figure out a way or a reason for i's to go on here,

## 50:32

but I couldn't justify that.

## 50:34

So that's it, right?

## 50:37

The only other thing that you have to do for your homework is to switch the coefficients,

## 50:41

because I think they're different numbers, but then also compute the current, right?

## 50:46

And so you'll plot the current as a function of x along with the flux, okay?

## 50:52

Any questions?

## 50:55

Yeah.

## 50:56

What reading should we do over the weekend, your notes?

## 50:59

Yeah, I've got to get that page.

## 51:00

I've been, obviously, with the exam and everything,

## 51:03

I've been spending a lot of time not catching up, but just handling the inflow.

## 51:08

So just the next section, right?

## 51:11

So on the section, what is that, 6.4 on interface conditions,

## 51:15

boundary conditions, and so forth, right?

## 51:18

So basically what we'll do as far as problems go is we'll go from the single region,

## 51:26

right?

## 51:26

With these sort of arbitrary boundary condition of setting the flux to multiple regions,

## 51:32

and then more realistic boundary conditions, right?

## 51:35

Ones that model things that matter, that are more realistic for practical applications,

## 51:42

like the idea of having no neutrons entering the system, right?

## 51:47

Which is pretty, like if you have a reactor,

## 51:50

you're likely not having a neutron source outside of the reactor, right?

## 51:54

And the way to model that.

## 51:56

Just through an appropriate boundary condition, okay?

## 51:59

All right, I will see you on Monday.
