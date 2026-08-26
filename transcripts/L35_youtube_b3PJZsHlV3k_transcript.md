# L35 Local Audio Transcript

Course: NE 630

Playlist source: https://youtube.com/playlist?list=PLy481lNHlnHoEO95vM-xYX2bydD25v20L

Video: NE 630 - Lesson 35

URL: https://www.youtube.com/watch?v=b3PJZsHlV3k

Video ID: b3PJZsHlV3k

YouTube upload date: 20231116

Duration: 32:02

Transcript source: Local faster-whisper transcription from YouTube audio.

Whisper model: large-v3; detected language: en.

Generated: 2026-06-28

Note: This transcript is machine-generated from audio and lightly wrapped only. It should be reviewed before being quoted, published, or used as polished lesson text.

Requested language: en

## 00:02

So last time, we talked about diffusion and the diffusion equation with multiplication.

## 00:08

Today, we're going to take a deeper dive into criticality, which was the last topic that we touched
on last time,

## 00:14

and then we'll take a brief tour of Bessel functions and then set you up for applications with them.

## 00:25

So, criticality. Remember, the problem that we had was a slab of material with those properties from
negative a over 2 to positive a.

## 00:36

What we wanted to do was explore the flux as a function of k-infinity, basically as new sigma f
would go from zero to some upper value.

## 00:50

For k-infinity greater than one, we found that the solution changed and the final form that we had
was given here.

## 00:58

It was in terms of cosines as opposed to exponentials or the hyperbolic functions.

## 01:04

And in this case, the kappa squared.

## 01:07

The kappa squared is k-infinity minus one over L squared, which is equal to our material buckling,
right?

## 01:16

B sub m.

## 01:19

We also noticed that when the quantity a times kappa over two approached pi over two,

## 01:26

the term cosine of a times kappa over two in the previous flux term vanished, and then the flux
would blow up, right?

## 01:34

So if I go back to that flux,

## 01:39

I can see that the cosine of a times kappa over two is in the bottom here.

## 01:40

And if that goes to pi over two, then the cosine goes to zero and we're dividing by zero and things
break down.

## 01:47

It's called a singularity.

## 01:49

That singularity happens when the system is critical.

## 01:55

So we can look at this a little bit more carefully if we break down what happens when this buckling
goes to that value, right?

## 02:05

So we have the material buckling, which is a function.

## 02:08

Only of material properties.

## 02:10

So we have k-infinity minus one over L squared, and this has to be equal to pi over a squared,
right?

## 02:17

That's the term that would make that cosine term go to zero.

## 02:20

And the pi over a term is related to the geometric buckling, right?

## 02:26

So there are these two concepts, material and geometric buckling, which have been talked about in
the book.

## 02:32

They've been used historically.

## 02:34

And what it's really doing is giving you parameters that you can use to

## 02:38

very easily put balance of materials and the geometry of a system, right?

## 02:46

It's basically you have these two things that you have adjustable knobs for.

## 02:50

You have the materials, whether you're putting more fissile material in or you have the geometry,
whether you make your reactor bigger, right?

## 02:56

So these two quantities are super useful, especially in this one group diffusion analysis.

## 03:03

So with this buckling, we can rearrange terms.

## 03:08

We can isolate k-infinity, and what we have is k-infinity is equal to L squared times pi over a
squared plus one.

## 03:14

And if we rearrange a little bit further, we get one is equal to k-infinity over the sum of one plus
L squared times pi over a squared, right?

## 03:24

And we can identify everything on the right-hand side outside of k-infinity as being our probability
of non-leakage, right?

## 03:31

So we have k-infinity times the probability of non-leakage, but we know what k-infinity is.

## 03:36

k-infinity is our new sigma f over sigma a.

## 03:38

So in essence, what we have is all of our gains that we would have from fission.

## 03:44

If you imagine a flux term being introduced here, right, we have all of our gains and then only the
losses from absorption.

## 03:50

That's what k-infinity is.

## 03:52

When we go to a finite system, right, something that actually has boundaries where neutrons can
leave the building, then we have losses from leakage, right?

## 04:00

So the k-infinity is gains to losses from absorption.

## 04:04

And then p sub nL, the non-leakage probability, would be the losses from absorption over absorption.

## 04:08

So we have losses from absorption over all losses, right?

## 04:10

Losses from absorption over all losses tells us the probability that we are being absorbed.

## 04:16

If you're a neutron, you only have two ways to die.

## 04:18

You can be absorbed or you can leave the system through leakage, right?

## 04:22

So losses from absorption over total losses represents our probability of being absorbed, which is
equivalent to being the probability of non-leakage, right?

## 04:31

And so we can also write this fraction k-infinity over the sum in this way.

## 04:38

Right?

## 04:39

If we multiply through by sigma a on the top and bottom, we get new sigma f over sigma a plus d
times that geometric buckling.

## 04:48

And I put here the ratio gains to losses.

## 04:51

That would be a little bit clearer if I were multiplying the top and the bottom by the flux, right?

## 04:56

Then I would actually have the reaction rates.

## 04:57

But in all of this, the buckling is just a really easy way to encapsulate the materials by
themselves and then the geometry by themselves.

## 05:07

And depending on how you—

## 05:08

how you represent the terms, you can kind of isolate the different loss terms relative to the gains.

## 05:17

So anyway, hopefully breaking it down this way gives you a couple different ways to interpret the
terms that we're dealing with.

## 05:27

So each of the statements, though, on the previous slide correspond to criticality, right?

## 05:31

And that's exactly when losses are in balance with the gains, right?

## 05:36

So that's k equal 1.

## 05:38

Now, just like a real critical system, we only get a steady state flux if there is no source, right?

## 05:45

The whole problem with that blowing up of the cosine term is because that was for a problem that had
a source term.

## 05:51

It was on the boundary.

## 05:53

Maybe it wasn't in the boundary.

## 05:54

It could either be from the boundary having, like, an incident current, or it could be from a volume
source, right?

## 05:59

If you have a critical system, you can't put a source in because then your population will grow
without bound.

## 06:06

And if it's growing, then it's not in state.

## 06:08

So what happens when the bucklings don't match, right?

## 06:13

Criticality is exactly when the material buckling is equal to the geometric buckling.

## 06:18

Well, as described in section 7.2 in the book, we can still characterize the steady state flux,
right?

## 06:24

That means solve the neutron diffusion equation by introducing k as a new parameter.

## 06:30

So k is the k eigenvalue.

## 06:33

That's the term that we've been using all along.

## 06:36

But we're going to put it into this equation almost as a new parameter.

## 06:38

So k is the k eigenvalue. That's the term that we've been using all along. But we're going to put it
into this equation almost as a new parameter.

## 06:38

But we're going to put it into this equation almost as a new parameter.

## 06:40

So for slab geometry, the diffusion equation with k looks like this.

## 06:45

Or we can organize it a little bit differently and represent it again, as a buckling term, right?

## 06:51

So this bracketed term k infinity, which is now adjusted by k, minus 1 over l squared,

## 06:58

that's the same material buckling that we've seen before.

## 07:01

Now, it's just being adjusted by k.

## 07:03

So this is equivalent to 7.4 in the book, but it's specific to slabs here,

## 07:08

which I hope will make some of this discussion a little bit easier. So in other words, by

## 07:14

introducing this K, we are reducing or increasing K infinity. Or if we're talking about like a

## 07:22

specific physical thing, as the book suggests, maybe we're modifying the number of neutrons

## 07:27

produced per fission, right? It's all the same, right? We're adjusting the fission term. And

## 07:33

that's either adjusting K infinity or nu sigma f, sigma f, or nu. I like the way the book

## 07:38

describes it, giving us a concrete example for K adjusting the number of neutrons. So what we're

## 07:44

doing is finding K that reduces or increases K infinity so that the material buckling is equal

## 07:50

to the geometric buckling. So then our goal is let's determine what the K is given the

## 07:58

materials and geometry, right? So we might have materials and a geometry that are not in balance

## 08:02

so that we can adjust the number of neutrons. And then we might have materials and a geometry

## 08:03

that are not in balance so that we can adjust the number of neutrons. And then we might have

## 08:03

we don't have a sustainable chain reaction. K will be less than one, or maybe K will be greater

## 08:08

than one. Or we can use this setup to determine the materials or geometry that gives us a certain

## 08:14

K. And usually we're looking for K equal one, right? That's what we would be doing in reactor

## 08:19

design. So let's work through an example where we try to find this critical buckling, okay? So we'll

## 08:29

use the same system as an example, the one that we started with, the slab of material from negative
A

## 08:34

over two to A over two, right? But we're going to apply vacuum conditions. And by vacuum, I mean the

## 08:40

zero incident partial current condition. It's a little bit more challenging than the case of just

## 08:45

setting the flux to zero at the boundaries, but it will give us a little bit more to digest in terms

## 08:52

of some of the expressions that come out of it, okay? So first of all, step one, we have our

## 08:56

equations. So I'm writing the diffusion equation on the left in buckling form. And then my boundary

## 09:03

conditions are my flux to zero at the boundaries. And then I'm writing the flux to zero at the

## 09:04

rightward current, partial current at the left boundary is zero. So no neutrons coming in and

## 09:10

same thing at the right boundary. The general solution is going to be a cosine and a sine term,

## 09:17

right? These are the functions that we would choose to use for a positive buckling term,

## 09:22

where we have K infinity greater than one. So with that flux, we can substitute

## 09:29

into the boundary conditions and we end up with these expressions. Now,

## 09:34

these are slightly complicated, but as I suggested and showed in the last lesson,

## 09:41

we can manipulate these conditions and simplify our lives considerably, right? So if we subtract

## 09:47

the first condition from the second one, right, what we end up with is this expression for C2,

## 09:55

which means that C2 goes to zero, very similar to the case that we saw last time.

## 09:59

And if we substitute C2 into our left boundary condition,

## 10:04

we're left with then for C1 is the following. Now, this would seem like we've hit a dead end

## 10:11

because we have C1 times all the stuff equal to zero. So there's nothing that's telling me what

## 10:17

C1 is. Well, that is part of this process. So we don't solve for C1, right? The equation is

## 10:27

only satisfied for whatever our critical buckling value is, B or B squared, right? That's the nature

## 10:33

of eigenvalue. So we don't solve for C1, right? That's the nature of eigenvalue. So we don't solve

## 10:34

problem. We get a solution, a shape, a flux that has an arbitrary normalization,

## 10:42

but corresponding to that flux is a special value, this number K or this number B that

## 10:48

we're trying to find, the critical buckling or the critical eigenvalue K, okay?

## 10:53

So if we simplify that previous expression, right, the one that I have here, right,

## 10:58

with a sine and a cosine, of course, I'm going to separate them, bring the sine,

## 11:03

the cosine on one side, divide by the cosine. So we get the number of bugs that weler,

## 11:04

the sine, and then I have this transcendental equation, meaning something that I'll have to

## 11:10

use a numerical solver if I want a value, where I have a cotangent of the buckling times a over 2

## 11:17

is equal to 2 times b times d. This is our criticality condition. This is what's going

## 11:22

to tell us what our eigenvalue k is. First, we get b, and then we can relate b to k.

## 11:28

So what we're looking for is the smallest positive value of b squared that satisfies this equation.

## 11:34

And corresponding to that will be the flux, phi of x, that is positive everywhere and is called

## 11:43

the fundamental mode. And corresponding also to b is the largest eigenvalue k. So we're looking

## 11:50

for the smallest b, and we're looking for the largest k, because there's an inverse relationship.

## 11:57

So without numbers, this is about as far as we can go. Remember, because we don't have

## 12:04

the eigenvalue k, we don't have the eigenvalue k. So we don't have the eigenvalue k.

## 12:04

So anything to define c1, that's not going to go anywhere. But we would be able to proceed

## 12:12

if we were using the simpler boundary conditions. In that case, b squared is equal to pi squared

## 12:17

over a squared. And that gives us immediately the functional form. That gives us b directly.

## 12:24

But with our criticality condition, the boxed equation here, we don't have a way to solve for

## 12:29

b without putting in numbers. That's the nature of this particular expression for

## 12:34

b. And that comes specifically from the boundary conditions that we're using.

## 12:39

So for your homework, you'll be doing this problem. And I'll have that also in the page

## 12:46

for you on Canvas. So it's here. I'm going to move on, though. Beyond the buckling, once we get that

## 12:55

value of b, what do we do with it? Well, the very first thing that we want to do is get that

## 12:58

eigenvalue, k, gains to losses. And so we remember that k is equal to k infinity over this other

## 13:04

stuff, 1 plus l squared.

## 13:06

Times b squared, which, in effect, is accounting for the non-leakage probability. Not even,

## 13:12

in effect, that is the definition of the non-leakage probability, 1 over 1 plus l squared

## 13:16

b squared. So if we know what k infinity is, or if we knew what nu sigma f is, we have sigma a,

## 13:23

we have d, so we can evaluate l. Given all this stuff, we can evaluate what k is. And so for

## 13:31

problem 35.1, you should find that b squared is roughly,

## 13:36

0.06, right? I'm asking you to dive in and, you know, figure it out to more decimal places than

## 13:42

this, but this should give you kind of a sanity check. Now, that number combined with d equal 1,

## 13:48

sigma a equal 0.1, k infinity equal 1.5, let's get the critical eigenvalue, k.

## 13:54

All right, so we can put all those numbers in, and what we get is k is equal to 0.9375.

## 14:00

All right, that's a number. What can we kind of infer about the system?

## 14:07

Obviously, it's subcritical, right? k is less than 1. And so if we wanted to make it critical,

## 14:12

we would have to do one of two things, either increase k infinity, right? That could be

## 14:18

increasing nu sigma f. You could also be decreasing sigma a, but that also would be

## 14:26

then affecting l, the diffusion length, which changes some things. But that's all material

## 14:32

stuff. So all that stuff would be totally reasonable.

## 14:36

Also make the system bigger, right? We could increase a, which would decrease b squared,

## 14:42

the buckling, right? Remember, the buckling goes as pi over a, or b squared goes as pi squared over

## 14:48

a squared. So if we increase a, we are decreasing the buckling. Remember, leakage is proportional

## 14:53

to the buckling. So the bigger the system is relative to its volume, the smaller is the

## 15:00

fraction of neutrons leaking from the system, right? That's just kind of a principle you can

## 15:05

take away from all this stuff.

## 15:06

We minimize leakage by minimizing the amount of surface area relative to the volume of the

## 15:12

reactor. So now, given b squared, the buckling, we also have the form for the flux, right? v of x

## 15:22

is now equal to c times cosine of bx, right? Same thing that we would have had for a different

## 15:27

boundary condition, but now we have the correct buckling for that condition. So this c is the c1

## 15:34

that we saw before when we had our general solution for the slab.

## 15:38

So now we have the flux, okay? And it's our remaining constant of integration. And like the

## 15:43

eigenfunctions I just talked about before, its magnitude is arbitrary. And so we have to come

## 15:48

up with some way to normalize it. And what's discussed in the book is relating the flux and

## 15:54

its normalization coefficient to the reactor power. So one way to do that is to link the flux

## 16:02

to the average reactor power density, p triple prime, right? So p triple prime would be equal to

## 16:08

times sigma f times phi bar, where phi bar is the spatially average flux. Gamma here is the amount

## 16:14

of energy released per fission, and it's specifically in units of joules, so that that value is
listed

## 16:21

in the reading that you have, okay? So if we want the spatially average flux, we integrate over that

## 16:26

term, divide by a. Oh, looks like I'm forgetting to divide by a here. Let me go ahead and fix that.

## 16:38

One over a. There we go. I think I had it correct on the right-hand side. So that is our

## 16:47

normalization constraint. Now, if we had a finite reactor, like the finite cylinder described in the

## 16:55

reading, then we would use the total power, right? And that's just the integral of the power
density.

## 17:01

Basically, same idea. It just depends on how we are deciding to integrate the flux. And for

## 17:07

something like our system, we're going to have to integrate the flux. And so we're going to have to

## 17:08

slab reactor. Integrating over volume is sort of, it's a murky idea. Like, what is the dimension in

## 17:16

the y and z directions, right? We could do it, but, you know, is a per, like, use a unit one
centimeter

## 17:24

like we did for the unit cell analysis with the four-factor stuff earlier on, but we'll just keep

## 17:29

it with the reaction rates, which corresponds to the power density. All right. So now we can turn

## 17:38

to the neutron diffusion equation in

## 17:40

silicon.

## 17:40

All right. So in cylindrical coordinates, the diffusion equation is given there. Now,

## 17:45

I've expanded it from the form that you see in the book to what's now boxed, right, where we

## 17:50

separate all those terms. And what we'll do is apply boundary conditions similar to what we've

## 17:56

done before. It just has to be that the flux has to be finite everywhere. Okay. That's one of the

## 18:03

other assumptions that, not even assumptions, constraints that we've been using sort of all

## 18:08

along to cancel out some of the terms.

## 18:10

Now, the problem with the boxed equation is that the differential equation is no longer one with

## 18:16

constant coefficients, right? Because the first derivative of the flux with respect to the radius

## 18:21

r has a coefficient of one over r, and that's decidedly not a constant coefficient. So all of

## 18:28

our use of exponentials basically goes away, right? That's the beauty of the constant coefficient

## 18:36

differential equation, right? Everything is a plane wave, e to the something,

## 18:40

maybe sometimes it's easier to work with cosines and sines or the hyperbolic functions, but at the

## 18:45

end of the day, it's just exponentials. And here we don't have that. So to get a sense for what

## 18:54

functions we'll need for the cylindrical coordinate system, I thought it would be

## 18:58

useful to go back a little bit to some basics of math that you've probably seen before and maybe

## 19:03

long forgotten. And so let's recall that a polite function, f of x, can be written as this,

## 19:10

a series expansion, right? And in fact, the series expansion I'm showing you here is the

## 19:15

McLaurin series, which is a Taylor series where we're expanding the function about the origin,

## 19:21

x equals zero, right? But it doesn't matter exactly which function we're using, because at the end
of

## 19:26

the day, it can be just written as a sum of powers of x, right? A power series representation for
the

## 19:33

function. So let's assume that our function, our solution to the differential equation in

## 19:39

cylindrical coordinates is a function of x. So let's assume that our function, our solution to

## 19:40

the differential equation can be treated like this, right? But what we'll do is start off with

## 19:48

slab geometry, because we already know what the solution is there. So we will go ahead and

## 19:54

substitute the flux as a function of x as a power series into our diffusion equation. I'm going to

## 19:59

do it without multiplication so that we're dealing with our exponential attenuation type terms that

## 20:05

we saw early on, okay? So when we do this substitution, we end up with,

## 20:10

this equation, all right? Now, if I take that derivative on the left-hand side and pass it

## 20:16

through, then I end up with this expression, all right? I have different powers of x in each of

## 20:24

those terms, and they all equal zero. Now, if this is to hold for any possible value of x,

## 20:29

that means I have to balance like powers of x, okay? So that means that for, say, the

## 20:40

x to the power of zero, right, just the constant term, I have two times one times a two is equal to

## 20:48

one over l squared times a zero, and if I look for the next power of x, then I have three times two

## 20:54

times a times three, right? So that's for x to the one, and on the right-hand side, I have

## 20:59

one over l times a times one, so on and so forth. If we look closely, a pattern emerges. So I've

## 21:11

picked out the even term.

## 21:13

The a with a subscript that is an even term, and I can relate a four to a two, and a two to a zero,

## 21:22

and then a four to a zero, and the pattern turns out to be this. I get my a sub two i is some power

## 21:33

of l multiplied by a zero all over two i factorial. If I put that into my summation, along with my

## 21:41

powers of x, then I end up with a four to a zero. So I get a four to a zero, and then a four to a

## 21:43

zero. So I end up with my solution, my flux solution, is equal to the hyperbolic cosine,

## 21:50

all right? Now, this is probably not at all obvious at first glance, right? And I will tell

## 21:55

you that the a one term will lead to a recursion that we get the hyperbolic sine from, right? So

## 22:05

these two solutions that we get for arbitrary a one and a zero are the hyperbolic cosine and

## 22:11

hyperbolic sine that we've seen before. Well, maybe this is a little bit more obvious, but

## 22:13

this isn't as surprising as you might expect, because in appendix a, or maybe you've seen it

## 22:21

before, the exponential can be expanded as one plus x plus x squared over two plus x to the third

## 22:28

over six, so on and so forth. And then appendix a also tells us that the hyperbolic cosine and

## 22:33

hyperbolic sine are related to the exponential. I know I've talked about it in class, but here

## 22:38

is again. That means that any solution that could be a sum of e to the x,

## 22:43

and e to the minus x, right, that would be this thing here, a times e to the x plus b times e to

## 22:49

the minus x, can be written in terms of the hyperbolic cosine and sine, right? And that

## 22:54

expression is given here. So when you're working with slab problems, it might be the case that

## 22:59

solutions are easiest to work with in terms of the hyperbolic sine and cosine. I didn't push that

## 23:05

early on, mostly because I just wanted you to start writing down some equations. But if you

## 23:11

start to get particular about,

## 23:13

how the final solution looks, you might look to the hyperbolic functions to help simplify some of

## 23:20

the expressions. Now, just to demonstrate that I'm not, you know, making stuff up related to the

## 23:28

series, I've implemented a function here that produces the series representation of the

## 23:35

hyperbolic cosine, where I'm adding the first 25 terms. Now, if I go beyond that, then I start

## 23:42

having issues evaluating the factorial. And

## 23:45

what that suggests is, if you're using a computer tool that has the hyperbolic cosine, it's

## 23:51

probably doing something pretty cool numerically, in order to evaluate numbers, sort of that would

## 23:56

require more terms than this, right. The exact details are beyond even me. I mean, I noticed some

## 24:03

possibilities, but it's pretty cool, because a lot of these functions that we use in practice,

## 24:09

are, they're all infinite series, right? But they're all

## 24:14

some

## 24:15

sum of polynomial terms. So when we use a computer to evaluate them, the computer's got to be doing

## 24:21

something pretty cool and quite robust to give us answers. What I'm showing you here is maybe cool,

## 24:28

but I wouldn't call it robust. But for the range of values that I'm showing for x from negative

## 24:34

one to one, it seems to work pretty well. And so there it is. So I'm using the built-in numpy

## 24:40

hyperbolic cosine. That's my red stars. And those are laid on top of my black curve, which is my

## 24:47

series expansion. And visually, I don't see a difference, right? So it seems that my math was

## 24:52

right. Now we can take this back to the cylinders and solutions of this equation. So we'll do the

## 25:00

same thing. We'll take our series expansion for the flux. I apologize, that should be in terms of

## 25:07

R. Quickly fix that, okay?

## 25:10

And we'll put it in terms of R.

## 25:10

We'll put that into the equation. And what we get is the following, okay? Now, that one over R

## 25:17

could cause us problems. It could mean that all of this is misbehaving, being impolite at R equals

## 25:24

zero. But let's be daring and assume that we can multiply through by R, right? That should get rid

## 25:31

of that singularity, okay? And when we do that, we end up with this expression. And if I keep going

## 25:38

and match the powers,

## 25:40

then I get at least the first several look like this, okay? Now, I didn't take this all the way

## 25:48

home. I actually referenced the Wolfram's site that has lots of these series expansions. I got

## 25:56

pretty close, I'll tell you that. But for the expansion I did, the odd terms go to zero, but

## 26:02

the even terms form a recurrence relationship that is similar to the one we just saw for the
hyperbolic

## 26:08

cosine. And when we do that, we get the first several look like this, okay? And when we do that,

## 26:10

what that recurrence relationship leads to is this sum. And what that defines is the Bessel

## 26:16

function of the first kind, which is usually given the letter J, and specifically of order

## 26:23

zero, right? That order zero comes from the equation that we just solved. There's a more

## 26:28

general form of that equation. There's some integer or possibly non-integer parameter that

## 26:33

goes into it that will lead to Bessel function of the first kinds of different orders. And then if

## 26:38

we flip some signs around, then we get the first kind of order zero. And then if we flip some signs

## 26:39

around, then we get the first kind of order zero. And then if we flip some signs around, then we get

## 26:40

other Bessel functions, right? So obviously the odd terms before canceled out, there's another

## 26:48

trick that we would do to recover the other function that goes along with it, like the

## 26:52

sine to the cosine, right? There would be a Bessel function of the second kind, right? Which is

## 26:58

usually given the letter Y. And then there are modified Bessel functions of the first and second

## 27:03

kind, which are usually given I and K as the letters. And the difference between the Bessel

## 27:10

function of the first kind and the second kind and the modified and the non-modified is sort of like

## 27:16

hyperbolic sine versus sine. So the Bessel function of the first kind is like a sine or a cosine.
The

## 27:24

Bessel function of the second kind would be like a sine. And then the modified Bessel function of

## 27:30

the first kind would be like the hyperbolic cosine, right? Something that suggests more

## 27:35

exponential attenuation than this oscillatory behavior.

## 27:40

So if you need to evaluate this Bessel function, you can use SciPy. It has a bunch of special

## 27:47

functions built in. And so the Bessel function of the first kind is this JV, and we give it the

## 27:52

first argument is zero, that's its order, and then whatever the value that you're evaluating it at.

## 27:59

And so if I want to take a look at this function, boom, there it is. Very similar to what you have

## 28:04

in the textbook, right? And also in appendix B of the textbook, there is a table of

## 28:10

Bessel function values. I'm not a big fan of using pre-tabulated values. I'd rather just use

## 28:16

like a function like this, but it could be the case that that table is of use to you, right?

## 28:22

We can also use SimPy. And if I run this, then I get the symbol for the Bessel function, right? And

## 28:30

I could also substitute a numerical value in and get that out too. But if we're going to use the

## 28:36

Bessel functions to do, say, continuity conditions, right?

## 28:40

Or some sort of a boundary condition like vacuum where I need to evaluate the current,

## 28:47

I'm going to need the gradient, or in our case, the derivative of the Bessel function. And so

## 28:53

I can use SimPy to do that as well, right? And we find a relationship between the Bessel function

## 29:01

of the first kind, order zero, or its derivative, and the next order, right? And that's

## 29:10

given here. So this property, along with several others of Bessel functions, are also included in

## 29:15

Appendix B of the textbook. And so I encourage you to reference that as you, you know, are reading

## 29:22

the chapter material, chapter seven, and as you head into this second problem for this lesson.

## 29:30

So we're going to consider an infinitely tall cylindrical reactor of radius r. And then by

## 29:35

following the example that I went through in the previous slides for the

## 29:40

slab reactor with vacuum conditions, I'd like you to derive a similar criticality condition for

## 29:46

the critical buckling. And then just like we did above, we'll put in some actual values, so r

## 29:51

radius of 25 centimeters, and then everything else. And I want you to come up with the critical

## 29:56

buckling, and then the corresponding multiplication factor k. So you'll notice here that I'm having
you

## 30:02

do an infinitely tall reactor. So we're not doing the separation of variables. I think the book does

## 30:07

a solid job of

## 30:09

explaining the separation of variables. And as you see from the reading, once you've done that

## 30:14

separation, it's just a matter of solving the two separate differential equations, right? So not a

## 30:21

whole lot beyond what you're doing here for just one dimension, okay? So we won't focus too much

## 30:29

on doing, you know, both z-dependence and r-dependence. I don't know that we get a whole

## 30:34

lot of value out of it. I think we get more value out of exploring multiple

## 30:39

regions. And so as we sort of near the very end of the course, I'm hoping that we can get to a two

## 30:46

region cylindrical problem that maps onto the unit cell analysis that we had done before. Of course,

## 30:54

when we were using OpenMC, we had a cylinder enclosed in a box. Well, we're not going to be

## 30:59

able to do that with our simple diffusion equation and sort of the pen and paper approach, but we

## 31:05

will be able to have a fuel cylinder inside of a,

## 31:09

a larger moderator cylinder, right? Where we preserve, say the, the overall volume of the

## 31:15

areas. Okay. So once we get to that point, maybe we'll be able to do it also with two energy groups

## 31:21

and try to reproduce some of the numbers that we were computing using OpenMC, right? Using

## 31:28

to get things like the flux value, the, the disadvantage factor. So that's sort of the,

## 31:34

the, the light at the end of the tunnel, as we head into the last two,

## 31:39

two weeks of the semester. So bear with me. I think we're, we're making good progress and I,

## 31:47

I look forward to wrapping things up. Have yourselves a wonderful and relaxing and safe holiday,

## 31:54

and I'll see you in, oh, just over a week.
