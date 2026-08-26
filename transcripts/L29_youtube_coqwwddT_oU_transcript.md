# L29 Local Audio Transcript

Course: NE 630

Playlist source: https://youtube.com/playlist?list=PLy481lNHlnHoEO95vM-xYX2bydD25v20L

Video: NE 630 - Lesson 29

URL: https://www.youtube.com/watch?v=coqwwddT_oU

Video ID: coqwwddT_oU

YouTube upload date: 20231101

Duration: 52:57

Transcript source: Local faster-whisper transcription from YouTube audio.

Whisper model: large-v3; detected language: en.

Generated: 2026-06-28

Note: This transcript is machine-generated from audio and lightly wrapped only. It should be reviewed before being quoted, published, or used as polished lesson text.

Requested language: en

## 00:03

right um do i add myself okay so uh today's going to be really quite informal uh as i said

## 00:34

we'll talk uh about this inclusion of feedback effects in the kinetics equations uh but i also

## 00:43

said that we would be spending more time on this in uh reactor lab where we'll actually get to

## 00:51

see the impacts of feedback uh through experiment but it helps to have kind of a sense for what what

## 00:57

would go on and how we would uh put together the equation so i've adapted some stuff that i've used

## 01:02

in the reactor lab class and put it in here um which is it's kind of neat because this is the

## 01:07

first this is only the second time i've taught this course i've taught reactor lab a few times

## 01:12

but i've never taught this and then reactor lab so there's a sort of a consistency that

## 01:18

maybe we get to enjoy that

## 01:21

um wouldn't otherwise be there okay uh so we'll go through this stuff i'll show you a little bit

## 01:26

of uh the code kind of talk through the mechanics of it and then we can play around with that and

## 01:32

then we should have plenty of time for any questions that you have right whether it's

## 01:37

the homework or um the exam right so i've drafted everything but like a final question related to

## 01:47

kinetics so i'm pretty i have a pretty good idea of

## 01:51

what will be on there so um hopefully that will help us through your questions okay so

## 01:58

kinetics we already had this set of equations from last time right um can somebody tell me what
these

## 02:05

are or how would you just this set of this is two equations how would we describe this particular

## 02:14

set of equations anything toss out some some isn't it neutral population and the population of the

## 02:29

unit fragments the precursors yeah yeah so we've got the first equation is a is a is the rate
equation

## 02:36

for the neutron density or the neutron population depending on how we normalize it and then the

## 02:41

second one is for the precursors am i making any assumptions there's no source there's no source

## 02:49

okay that's a good one what am i doing if i only include one function c you're averaging all the

## 02:58

differences yeah so this is the single

## 03:00

precursor group right so as we've seen before the more detailed um model is to assume some number of

## 03:08

precursors right or precursor groups where maybe we in reality we have up to 300 or so that have
been

## 03:16

measured precursors we don't track all those we lump them together into groups that have uh similar

## 03:23

half-lives right and so that way we can capture the time Dependence in a way that matches reality

## 03:29

this is the

## 03:30

kind of grossest or crudest approximation where everything is lumped together uh into one

## 03:36

precursor group which means that this decay constant Lambda is somehow average and we talked

## 03:41

a little bit about that last time and for the homework um that you have today uh that's I think

## 03:48

that's part of one of the questions so actually maybe before I move on from this are there

## 03:53

questions from the homework that you'd like to to tackle we got one that it might take a while to

## 04:00

get through

## 04:02

you know I'm not totally surprised right because that's uh I put that down and I I wrote the

## 04:24

solution for homework tenants it's on Canvas it'll be posted at midnight now of course you've
probably

## 04:29

noticed that when I give some some solutions

## 04:32

there are obviously some solutions that are coming from not me writing them right like that

## 04:36

you've seen in the past I've uh the number of times now that you've gotten an email or I've

## 04:41

said that I've went back and I've annotated some solutions it's because there have been

## 04:47

there's some sloppiness in some of the book solutions I don't know it must have been a

## 04:51

student I told you about the author you know he's at Northwestern or emeritus there I don't know who

## 04:55

would have written his solutions for him I think they're mostly right but they're some of it's

## 04:59

sloppy like uh the one for

## 05:02

when when you had to do the unit cell volumes they did it for some P over D ratio or some some ratio

## 05:09

that was different from what the book asked for it's like this is the solution for this the

## 05:13

mechanics are the same you plug it in Chuck and so one of my annotations would have been that but

## 05:18

then I looked at the solution for this particular problem it's like this is I hate this I hate I

## 05:23

hate this person who wrote this so I wrote it myself you're right it's not it's not trivial but

## 05:30

um it's not

## 05:32

it's not it's not terrible either you do have to so how did you approach it and where did you get

## 05:39

stuck oh yeah right there that's pretty accurate I tried the uh eigenvalue and eigenvector method

## 05:53

to get solutions for it and I got stuck with um my items that my eigenvectors both having like one

## 06:02

they're a one ones so I couldn't really solve the constants I've also tried doing integrating

## 06:10

factors and separability on these equations yeah so you don't need to use the integrating

## 06:16

factor so the where the integrating factor plays a role in a first order differential equation is to

## 06:25

um define the it basically gives you a way to integrate it and that's specific for

## 06:32

the case where you have a source term right in in homogeneity right with the equations that we're

## 06:38

considering it's we're assuming a critical reactor right and so without the source the solution is
so

## 06:46

a source term like in this case could be any function of time right so if it could be if

## 06:51

it's sinusoidal then your solution is going to have sinusoidal functions right if you don't have

## 06:56

the right hand side which is the case here because we're starting from a critical reactor we don't

## 07:02

have a solution as long as rho is constant which it is for our case the solution is a sum of two

## 07:08

exponential terms right there's no nothing else so you don't need the integrating factor is used to

## 07:14

get to whatever your solution form is when you have an arbitrary right hand side right because

## 07:18

you have that integral of whatever the source term is so in this case you'll end up with uh

## 07:25

let's see what would the so the matrix here and the eigenvalues would be

## 07:31

would

## 07:32

would satisfy right so here's what the matrix would be for this equation

## 07:39

um and I I have I think I put this in the notes from last time so you got the message I updated

## 07:46

the notes so that matrix looks like this we have a beta minus rho over Lambda we have a

## 07:54

minus no sorry a Lambda for the C we have a minus Lambda for the decay of the C and then

## 08:01

we have a beta over Lambda is that correct yes okay so then to find the eigenvalues of this

## 08:08

Matrix right you take the determinant of this minus Alpha which I'm using for the eigenvalue

## 08:16

times I right so what what you end up with then is a quadratic that looks like created minus row

## 08:23

Lambda minus Alpha and you have a minus Alpha minus minus Lambda minus Alpha

## 08:31

okay um minus this thing times that so Lambda data and is that correct I think so and this all has

## 08:48

to be equal to zero right so this is a quadratic you can get an expression for the elephants right

## 08:54

and that would actually give you the exact solution at least to with to the point of uh

## 09:00

having the two exponential terms the only thing that you wouldn't know that

## 09:03

you I you you can all solve this right right you have the numbers or you you could substitute

## 09:09

numbers but all we're looking for are the two roots of Alpha right so it's the quadratic formula

## 09:14

once you have those then your solution right so if it if if the answer to this is Alpha plus and

## 09:22

then Alpha minus right those are the two values I I think I told you last time you won't have

## 09:29

them be the same value right they will be different so you'll end up the only time

## 09:33

that you would have the same value is if Rho and Beta converge to each other right that's the

## 09:42

that's actually the tricky bit where where uh all the approximations that are like these two

## 09:48

assumptions that you're supposed to make that breaks down if Rho is close to Beta okay so you

## 09:55

get these two things then you know that your solution right for n n of t is going to be equal

## 10:02

to uh I I

## 10:03

in my own notes I used a times e to the Alpha plus t plus b times Alpha minus t that that is

## 10:13

the solution the only thing that I'm sorry b plus b times e right it's just the sum of these two

## 10:20

exponentials okay um you can write down the same thing for the precursors in terms of c and d right

## 10:28

so you've got these four coefficients but you you have and you have enough equations to solve for

## 10:33

everything right you have the two differential equations and then you have two initial conditions

## 10:37

four equations for four unknown coefficients a b c and d okay but you can simplify it a little

## 10:42

bit because you know that a plus b is equal to whatever your initial density is okay and that

## 10:50

density is arbitrary so you could just set n equal one right and then you have a simple

## 10:55

relationship between a and b a plus b is equal to one so a is equal to one minus b et cetera

## 11:03

um and so that that can simplify some things um I think the biggest thing though is

## 11:11

getting to a point where the alphas match the exponents in the given form right if you get to

## 11:18

that point you'll have basically gotten it so first of all one thing I'll point out is that

## 11:24

problem like any other problem in my assessment is worth four points right you don't need to have

## 11:31

solved the first part of it

## 11:33

do the other ones would you agree okay so if you're finding that it's just taking too long

## 11:39

I mean make a reasonable effort at it but like don't don't spend all of your time that's it I

## 11:45

thought about this it's like there's there's a there's a you know an incentive for learning can

## 11:53

be earning the point right but if you know I'm not giving you a hundred dollars to do it so it's

## 11:58

one point so like the effort that you can go in at that point you have to be self-selecting like do

## 12:03

I spend two hours on this or more to to get it right or do I try to focus my time that's something

## 12:10

that as a student I had a hard time doing which is why I had no life um so take that well we'll stop

## 12:17

that discussion there so uh you have this if you remember the solution that's given in 510 like the

## 12:24

thing that you're actually looking for is something that looks like n of p is equal to n not uh
where

## 12:32

we have

## 12:33

uh I'm trying to remember it off the top of my head it uh it ended up being row over beta minus

## 12:40

row e to the somebody tell me it's row over row minus beta no you're right okay so and oh it's

## 12:54

so and the what's the exponent for this one row minus theta yeah minus beta over right so that

## 13:01

that's that one and then this one

## 13:03

is uh beta over beta minus row e to the this one is lambda in time the row over beta minus

## 13:13

this is so this and this those the two are you that the multipliers on T those are the alphas

## 13:25

that you get right so if you can get those alphas and you have this then the only thing that you're

## 13:30

doing then is doing a little bit of algebra to get the

## 13:33

these two things which as you once you plug this solution back into the original differential

## 13:40

equation just like you would in like even if you hadn't made the approximations you'll you'll get an

## 13:47

equation for the two coefficients right so if I had written this before as 80 times this uh but

## 13:53

give me time I get those four equations for the four undetermined coefficients right so the the

## 14:00

hardest part is getting these things getting

## 14:03

the the coefficient to be Rho over beta minus Rho beta over beta minus Rho that's not once you've

## 14:11

gotten to that point that's pretty straightforward so it sounds like the challenge is coming up with

## 14:19

these as your roots from Alpha would you my problem was you said that there's also like a

## 14:31

CFG or it was like um C e to the Alpha

## 14:36

uh-huh I'm probably I'm having trouble getting that equipment too I think in that one just fine

## 14:42

but you should not what can you get I can get the nmt one but without the coefficients in front but

## 14:51

okay well so that for the precursors it's the same thing right because it in this case you you only

## 14:59

have two exponential functions both of your solution for both the number of neutrons and

## 15:05

the precursor

## 15:06

will be linear combinations of those two functions

## 15:10

so to write down the the C times this plus D times that that's a given

## 15:16

right then it's a matter of how do you find the C and D which you don't need to for this

## 15:22

right and actually there's a simple relationship between them right because you know that the

## 15:29

initial condition for the precursors is based on right so C naught is equal to n naught times

## 15:36

uh

## 15:38

so there would be a relationship so if this is A and this is B then the coefficient C and D for

## 15:48

the precursors will be related to A and B through this relationship right but it's it's really the

## 15:55

like so you say you got those the time constants these eigenvalues I got really close to what the

## 16:04

book wants okay so then um

## 16:06

um

## 16:07

um

## 16:07

um

## 16:08

um

## 16:08

um

## 16:08

um

## 16:08

um

## 16:08

um

## 16:08

um

## 16:08

um

## 16:08

um

## 16:08

um

## 16:08

um

## 16:08

um

## 16:08

um

## 16:08

um

## 16:08

um

## 16:08

um

## 16:08

um

## 16:08

um

## 16:08

yeah that's that's kind of the the biggest trick

## 16:15

um and I don't like the way that they that the assumptions are specified it's they're right but

## 16:21

they don't um

## 16:24

they're not as clear as they could be there's more discussions so certainly

## 16:27

but you'll have the solution uh tonight to look at it but um

## 16:33

I'm wondering what term do you have so what do you get either of them exactly not quite I don't
think

## 16:40

apply the assumptions perfectly okay kind of think if there was any thing I mean it's it's

## 16:51

just manipulating the terms uh factoring things out so that you end up with uh you'll end up with

## 16:57

something under the radicals that if you organize it the way that I did you'll have a one and then

## 17:04

it's either a plus or minus and then you'll have something like a lambda lambda over

## 17:09

rho minus beta something like that where the approximation is that this thing has to be much

## 17:16

larger than one okay or sorry that or maybe it's the inverse but the rho minus beta over the

## 17:25

lambda is much larger than one is that correct beta minus rho over the lambda is greater than

## 17:34

one yeah so the absolute so this ratio is much larger than one so you can just take that out of

## 17:41

it uh and then you'll I don't

## 17:43

know remember there's a square root here there might be a four there um I do know that at one

## 17:48

point you do need to take a Taylor series approximation and I can give you this hint

## 17:54

this this should actually help if you have a function f of s equal to the square root of one

## 18:09

plus a times s okay one of the things that that to get to the form that they have you need to get

## 18:17

rid of a radicals

## 18:18

I think that's one of one of the steps is getting rid of the square root now if x is small and it

## 18:24

like suppose a is order one or something it's just some coefficient if x is small then we can write

## 18:31

this as f of zero plus f prime at zero times um times x does that ring a bell from a distant health

## 18:46

class okay

## 18:48

this is something like I I hate when problems and I would have given you this hint earlier had I

## 18:54

uh sort of zeroed in on it I hate when when these sorts of things are hidden in assignments or

## 19:00

problems in an assignment I love this sort of approximation right so there's a there's a right

## 19:06

place to have it show up uh hopefully me giving you this hint uh sort of corrects that but if you

## 19:12

if you take this function f of x and say that x is small then you can

## 19:18

approximate it as this thing and well f of zero I plug in a zero that's going to be just one and

## 19:25

then if I plug uh what's the derivative of this thing right this is if this is one plus ax to the

## 19:35

one half so the derivative goes to one half one plus ax the minus one half times then the derivative

## 19:44

of this would be a well if I plug it in zero to this that's one plus zero

## 19:49

could be minus one half so that's still just one so this ends up being one and a half times a

## 19:58

x right so this will apply to one of the the roots as you're doing so maybe that's where the missing

## 20:09

thing is so take a stab at it it's it's not a huge chunk because you can do the other things

## 20:17

with without having that you can just

## 20:19

but yeah I was a little frustrated too with the way that the solution was the problem is fine but

## 20:30

the solution was I would never want to pass that on um but good questions the so the actual formal

## 20:43

solution is disgusting you would think that for two equations that the solution would be somewhat

## 20:50

simple you're finding that even for this approximation it's not trivial if you

## 20:54

take the actual full solution and do it I've used senpai right in class before for some simple
things

## 21:00

I use senpai just doing my normal like steps for for integrating differential equations it gets to

## 21:07

the point where it has so many terms that my browser freezes right like it's it's insane how

## 21:16

difficult that this set of equations is even for a step insertion of reactivity right that

## 21:23

is

## 21:24

these sorts of approximations are made. So I even went back to an old textbook from 1976,

## 21:30

Duderstad and Hamilton, and they go through some derivations and give the same approximation

## 21:34

using the same assumptions that are talked about in here. They didn't give the solution. They

## 21:39

basically just said the same thing that the problem statement says here. And at the time,

## 21:45

when I first would have read that almost 20 years ago or something, I would have been like,

## 21:49

well, why the hell do, like, why? Well, it makes sense now, because if you actually look at what

## 21:55

the real solution is analytically, it's completely intractable, even for something like this. Unless

## 22:00

maybe there's some math wizard over in the math building that has, you know, the appropriate

## 22:05

Laplace transforms and so forth. But at the end of the day, I don't think so, right? That's why

## 22:11

the approximations are made. So anyway, hopefully that answers your question, or at least

## 22:19

gives you a way to make your next decision. Any other questions related to the homework?

## 22:33

No? Speak now. Forever hold your peace, as it were. Who's done? Who's started? Okay, well,

## 22:47

that's good. Good, good, good. All right. Well, then I will continue on with what I'm doing here,

## 22:55

and then we can turn to exam questions if you have them thereafter.

## 23:01

All right. So we already have these equations, and if we dig back a little bit further into the

## 23:07

material, we know that the reactivity is a function also of temperature. Here, my discussion is

## 23:13

strictly for the fuel temperature. There would be a cooling temperature coefficient, too. But

## 23:17

we know that as a function of time, rho would be equal to some fixed value. Maybe we start off at

## 23:22

critical, or we put in a control rod, or something like this could be something that we choose to do

## 23:26

with time. This is what is happening due to the temperature. Now, where do we get this from?

## 23:31

Well, we get it from d rho dt is equal to alpha tf, and we know that that's roughly minus three

## 23:40

pcm per k for a PWR, right? So if we have the rho as a function of time, we have d rho dt as a

## 23:48

function of time, then what we need to do is complete this by figuring out how temperature

## 23:54

varies in time, okay? Because if we know how temperature varies in time, then we know how

## 24:01

the rho varies in time, right? So at the end of the day, if we're solving differential equations,

## 24:06

we need everything in terms of these time derivatives. So the simplest model that we can

## 24:15

make for the temperature assumes, or it makes the assumption that the temperature goes linearly

## 24:21

with the flux. So that means, like, I could have flux equals zero. If flux is zero, then the power

## 24:28

is zero, and I have some sort of initial temperature, right?

## 24:31

As I increase the temperature, sorry, increase the power, increase the flux, I'm saying that my

## 24:37

temperature follows suit. Now, for those of you in heat transfer, who's in heat transfer,

## 24:43

or who's had it, okay? What would this mean about the heat transfer process? If I go up in power,

## 24:52

right, and my temperature is immediately increasing with that, what does that mean?

## 25:01

Ultimately, if I produce energy, and it's deposited into a medium, it heats up. Does that

## 25:16

make sense? But if the time dependence of that temperature is linked directly to the power

## 25:24

generation rate, that means that if my power is increasing, my temperature increasing,

## 25:29

there's no lag in this case, right? Usually, there would be some sort of lag. That means that the

## 25:35

heat transfer is instantaneous, right?

## 25:40

Also assumes that I have maybe a fixed temperature on my final heat sink, which would be the coolant

## 25:44

in this case, so that all of this additional heat that's generated leads to this increased

## 25:49

temperature, this heat flux, that coolant temperature stays constant. If I were to do

## 25:54

this in a more realistic way, I would have a second temperature for the coolant, and there

## 25:59

would be an additional time coupling between the fuel temperature and the coolant temperature. We

## 26:04

know that for the fuel, we're heating it up, it does take some time for that energy to escape the

## 26:10

fuel element, right? If you think about it, you have a hot metal rod that put a current through it,

## 26:15

resistive heating, it's going to take time for the temperature profile to build up, and then for the

## 26:22

heat to start dissipating, whether it's being water cooled, you get convective heat losses,

## 26:29

it all changes as a function of time. It's never instantaneous. So this is like the dirt simple

## 26:34

way to model it.

## 26:37

This constant kappa has a whole...

## 26:40

bunch of physical parameters that go into it, things like the density of the fuel, the heat

## 26:46

capacity of the fuel, a bunch of other things that I won't go into in detail, but you'll see it in

## 26:52

just a moment when I define it numerically. So in this case, I have to define my fission

## 26:59

cross-section so that we can go from a flux to an energy production rate. At the end of the day,

## 27:05

we get this kappa value, and it's a pretty darn small number, right?

## 27:10

I don't think there's anything else that I want to point out, but yeah, all the parameters are

## 27:16

things that should look familiar, either from this class or from like a heat transfer class.

## 27:24

Oops, that's not what I want to do. All right, so setting up the kinetics, I'm going to put

## 27:32

everything into one function so that we don't have a whole lot of input parameters. The only

## 27:36

thing that I'm going to change would be my rho naught naught and my alpha. Alpha is my feed

## 27:42

back coefficient for the fuel temperature, and rho naught naught is a step insertion that I'm going

## 27:47

to place. So I'm repeating all those lines that we just saw for this kappa term, okay? And then

## 27:53

I'm going to insert the reactivity. So before we had a, like in the previous lesson, I had set up

## 28:01

a separate function for reactivity as a function time. I'm building that in here. So it starts off

## 28:06

rho is equal to zero, and then I can either add some reactivity, maybe between zero,

## 28:12

and five seconds, and then that is further adjusted by this alpha times whatever my delta t

## 28:19

is, okay? So I've got my sort of imposed system reactivity by changing maybe a control rod or

## 28:25

something like that, and then I have this feedback reactivity from changes in temperature. And then

## 28:31

for my three equations, right? So I've got my dn dt, and then I have my precursors. Those look the

## 28:36

same. Rho shows up here, so that equation doesn't change. It's just the value of

## 28:42

rho has this time dependence because the temperature is assumed to be changing, okay?

## 28:48

The precursors look the same, and then my dt dt, my temperature derivative, is what I saw before.

## 28:55

It's my kappa times the change in the flux, but I'm using n here, so it's v bar, the effective

## 29:03

speed, right? Which I've defined up here, so I'm assuming thermal neutrons, okay? So that's that,

## 29:12

and then I can set up the simulation basically the same way that I've done before, right? So I'll

## 29:17

start off with an initial neutron density, 10 to the 9 is close to a flux of 10 to the 13, so sort

## 29:24

of right order of magnitudes. We've got the initial precursor, and then we'll assume that we're

## 29:30

starting off at 300 degrees Kelvin, okay? Get those all into one initial condition vector, and we
can

## 29:41

get on to

## 29:42

solving it, right? So in this case, I am setting alpha to be 3 times 10 to the minus 5. In this

## 29:50

case, I'm using a negative sign in the function, so I'm using a positive value for the feedback

## 29:55

coefficient, even though the feedback coefficient is negative, because increase in temperature

## 30:00

brings down the power, okay? And so I'm looking at the neutron density here, so I'm plotting it out

## 30:10

before zero, I'm bringing it to zero, that's when I put in the step insertion of reactivity.
Remember,

## 30:15

beta was 0.0065, so this is actually pretty close to beta. I'm jumping up from, you know,

## 30:21

1 times 10 to the 9 to maybe peaking at 5 times 10 to the 9. Now, we saw last time that the closer

## 30:29

I got to beta, the closer rho gets to beta, the more my flux increases. This doesn't seem like a

## 30:37

increase okay so what i'm going to do is i'm going to take the same same simulation and i'm

## 30:43

going to pretend that i don't have temperature feedback right so if i take this term here and

## 30:49

multiply it by zero take a look at what the magnitude looks like now 10 to the 12th from

## 31:00

10 to you know basically said i didn't change order of magnitude last time now i'm increasing

## 31:05

it by a factor of a thousand huge right i can roll it back a little bit and say hey what if

## 31:14

this is equal to um say 1 times 10 to the minus 5 right i've increased to 10 to 10 but um and then

## 31:27

what if i went to something like 12 okay then i'm hardly increasing at all our reactor has a

## 31:34

fuel temperature coefficient that's roughly 12 pcm

## 31:38

per k right it's about four times as large as a typical pwr that's one of the reasons that

## 31:43

we can pulse so when we pulse we we take out lots of control we're talking about

## 31:49

a dollar and a half to two dollars of reactivity right huge huge change in in reactivity and

## 31:56

because of the strong negative feedback we go up in power pretty rapidly but we're also producing

## 32:01

heat that instantaneously heats up the fuel bringing uh down the reactivity through feed

## 32:08

back and we basically we'll we'll see next semester that it goes up by orders of magnitude

## 32:13

right we blip at about a gigawatt of power for about 20 milliseconds before feedback turns back

## 32:20

around okay so it's not too hard to to model the pulse the thermodynamics of of that um that sort

## 32:28

of transient in a bit of code like this but we'll we'll save that for next time so at any rate if i

## 32:35

wanted to just compare for a very

## 32:37

small let's say reactivity basically we can we can produce the image that you have in the book

## 32:46

so i'll call this sol1 and sol2 uh if i have no feedback it'll be that and then sol2 is this so

## 32:56

if i take this make that one that two okay you'll probably notice in the book there is

## 33:08

one

## 33:09

we could take this out further in time too where this would go up and start to curve over this

## 33:14

one's going to continue up on its exponential rise so feedback has a damping effect that's what

## 33:19

feedback negative feedback does stops things from um sort of compounding okay so feedback

## 33:25

incredibly important right in in the analysis of real systems right that's all i want to say

## 33:32

about feedback as part of kinetics we've got about 15 minutes left i'm happy to answer anything that

## 33:38

you want to talk about uh related to the exam how many questions i am expecting it to be about

## 33:49

75 as long as the last one so that was four questions and whatever sheet so it i'm making

## 33:57

it shorter if that i think maybe is what you're asking the topics range from everything that we

## 34:07

uh started right after the last one which was primarily uh the unit cell analysis

## 34:13

right so we use the unit cell analysis to understand uh sort of basic

## 34:23

uh how would i describe that basically getting reaction rates and such for

## 34:29

realistic reactors so that we could use then things like the four factor formula to understand

## 34:34

really a lot of the physics right if you remember one of the one of the things that

## 34:38

we're looking at all along is what happens to those neutrons born at high energies from a

## 34:43

fission right they've slowed down and so forth but how do you model that in a way that is easy

## 34:48

enough to do with pen and paper right it's cool to use codes right but using something like the

## 34:54

four factor formula definitely helps us um understand uh in in simpler terms what what's

## 35:01

going on so we did the unit cell analysis uh we went into the four factor formula which

## 35:07

accounts a little bit for spatial effects right you know in the um let's say the thermal

## 35:13

utilization we we have this term called the disadvantage factor which accounts for the

## 35:18

difference in the thermal fluxes between a moderator or non-fuel zone and the fuel zone

## 35:25

we had the resonance escape probability which we saw there were we had two approaches really

## 35:31

to compute the resonance escape probability um they both mean the same thing uh they just come

## 35:37

from different sources of data if we use the approach that's this exponential to something

## 35:42

that has to do with the resonance integral right that's that's sort of a correlation that's like a

## 35:49

fit to data remember the resonance integral itself is really just an effective cross section

## 35:54

right that's that's the effect of fast group cross-section right normalized in a different

## 35:59

way but when you put it into that exponential term you get the right thing a better way to remember

## 36:05

what the resonance escape probability is is to think of it in terms of reaction rates or fractions

## 36:12

of neutrons of different energies can somebody tell me in plain english what the resonance escape

## 36:16

probability is now we only care about this term p for thermal spectrum reactors it really doesn't

## 36:27

have a meaning for fast spectrum reactors fast spectrum reactors in a in that sense are much

## 36:32

simpler right because you just need the reaction rates everywhere right but for the resonance

## 36:36

escape probabilities applies to the four factor formula for thermal reactors what how would you

## 36:42

describe it in plain english the likelihood of a neutron slowing down past a resonance energy

## 36:48

thing without getting absorbed by it yeah and so we have resonances from as low as 6.67 ev

## 36:56

right in plutonium 230 sorry in uranium 238 all the way up to you know tens of kev so neutrons

## 37:04

are born at circa 1 mev the resonance escape probability is the probability that it makes

## 37:09

it down past that say 6.6

## 37:12

7 ev we've used the cutoff of one ev so the fraction of all neutrons born that make it

## 37:18

below an ev is what we call the resonance escape probability another way to look at that if we are

## 37:24

playing with open mc in the unit cell analysis is uh to to look at the fractions of neutrons

## 37:30

based on their depth if you don't have leakage the only way that you as a neutron can leave the

## 37:36

system is by being absorbed right and if we're talking about

## 37:41

a two group framework you can either be absorbed at fast energies which is everything above ev or

## 37:49

at thermal energy which is everything below so if i gave you something like the number of neutrons

## 37:55

uh absorbed above one ev and the number of neutrons absorbed below one ev what's the resonance
escape

## 38:04

probability call the number absorbed above one ev call that x call the number absorbed below one ev

## 38:15

why what's the resonance escape probability in terms of x and y x over y yeah uh x over x plus y

## 38:28

so what is x x was my fast absorption right so you're saying fast absorptions to all absorptions

## 38:39

way around the other way around thermal detortions to all of your attention so in this case it would

## 38:43

be y over x plus five right what about thermal absorbing so what's the resonance escape probability

## 38:46

Salwar did you know that the nos охùng of and what is x so you get a potential absorption that's

## 38:47

in respect of the highburden muon doctr sph beim but normal absorption is my cust mode and you get
that

## 38:50

thermal utilization what does that mean in plain english that's our f term yeah

## 39:07

yes yeah so if you're a thermal neutron what what's my probability dying in the fuel right

## 39:18

so we've already bypassed all the the fast neutron stuff right p gets us there p says hey

## 39:24

you're fast here's the probability that you make it to thermal now you start doing your balance of

## 39:28

thermal the fast fission factor sort of corrects all that then by saying hey it turns out that

## 39:33

some neutrons born are actually caused by fast neutrons but thermal utilization is the probability

## 39:38

that a thermal neutron is absorbed in the fuel so again you can understand that through reaction

## 39:43

rates if i tell you the number of neutrons being absorbed in the non-fuel region is x

## 39:50

and the number of neutrons being absorbed in the fuel region is y well then the fraction of

## 39:56

neutrons being absorbed in the fuel which is equal to thermal utilization would be y over y plus x

## 40:02

right so

## 40:03

you can definitely if i give you reaction rates you should be able to compute these four factors

## 40:07

right um the only uh the only one of the four factors that that has sort of an option is p

## 40:15

right so if i gave you something like the resonance integral uh the uh fuel sorry the

## 40:21

moderator cross-section you should be able to do do that too but if i gave you just regular old

## 40:26

reaction rates in the in one group uh in the two group so fast group and then thermal group you

## 40:31

should be able to compute all four of these

## 40:33

quantities one thing i'll point out is that so i wrapped up uh grading homework seven a couple

## 40:39

days ago that's live look at the solution to that uh i pointed this out in my email to you all but

## 40:46

um there were a number of folks who just kind of like hand waved the thing where i wanted you to

## 40:50

write out the four factors in terms of the reaction rates the reason why having the form

## 40:55

of the four factors in this reaction rate format was useful or is useful to us if we use something

## 41:02

like open mc2 and we use something like open mc2 and we use something like open mc2 and we use
something

## 41:03

like open mc all we're ever going to get are reaction rates right volume integrated energy

## 41:09

integrated reaction rates it doesn't have a built-in function for resonance escape probability

## 41:15

we have to do that ourselves based on the physics and the physics says that the number of neutrons

## 41:20

that of all neutrons that are absorbed at thermal energies is the resonance escape probability right

## 41:27

so that that's what i was looking for and a lot of folks just kind of um hand wave that away

## 41:33

and so take a look at that if you have questions on it because i guarantee you'll see it on friday

## 41:38

based on this discussion um what else we went from the unit cell stuff and then we started

## 41:47

tackling time what was the very first thing we did in the time domain it was where only the number

## 41:59

densities of things were changing not the flux right so it's chapter 10 the long-term behavior

## 42:05

we did a little bit on temperature effects right so we saw

## 42:08

just a moment ago things like the reactivity feedback coefficients but we then went to the

## 42:13

time dependence of of the nuclides and we started off with vision products like xenon 135 right and

## 42:21

then as part of the homework which i'm hoping i can get grading all wrapped up um tonight the

## 42:27

solutions are there like the number one thing is i want you to have solutions um to to go back so

## 42:32

you like whatever you submitted for your your own solution definitely take a look at at mine so you

## 42:38

have a sense of uh what's going on if you feel like you didn't okay so the very first thing that

## 42:42

we did was looked at xenon one of the things that we we did there were kind of two big takeaways one

## 42:49

after a few days of operation the buildup of xenon does what to the reactivity right you start off

## 43:00

with a fresh core you kind of go up in power you're at whatever your power is you're you have

## 43:06

your control rod set at some some position so that you're critical if you're operating then for at

## 43:12

least three days you've built up xenon it has a half-life of uh you know like it with the iodine

## 43:19

we're talking about half-life of like 16 hours total okay we build up to an equilibrium

## 43:25

concentration what happens to my reactivity go down why this xenon is a big neutron poison right

## 43:36

it's got a cross-section that's like a million Barnes so it doesn't take a whole lot of it to

## 43:40

build up before your reactivity goes down now in practice

## 43:43

um but we could just say that yeah row goes down or K goes down in practice that means that we have

## 43:48

to adjust our control rods that was that exercise that you had in uh homework eight um that where

## 43:55

you had to go through okay definitely look at the solution for that it's it's long in the sense that

## 44:00

I wrote a whole bunch of things kind of describing every step in detail but the the process is
pretty

## 44:05

straightforward because it's a lot of copy and paste right you're using that modified four

## 44:09

factor formula from chapter 10. where basically all of

## 44:13

these things fission products were the change in the actinides it shows up in the first two factors

## 44:20

Ada times F right so thermal absorptions in the fuel or fission neutrons generated in the fuel to

## 44:27

thermal neutrons absorbed everywhere is essentially what that product is okay so we had that uh then
we

## 44:34

went into the aconite so we saw the very simplified plutonium uranium um chain right where we assume

## 44:41

that the uranium 238

## 44:43

um doesn't change in time so that we're just depleting the u-235 and building up the plutonium

## 44:48

239. in fact you saw a very similar problem when we um looked at the thorium chain right so you had

## 44:57

thorium 232 with protectinium 233 and then uranium 233 so you I think you had to write down the

## 45:03

equations and then solve that very similarly to how the uranium equations were tackled in in the

## 45:09

book okay any questions about that

## 45:13

stuff either the fission product generation or the the depletion of fuel

## 45:21

you should definitely be able to write down the equations because you've seen say the thorium

## 45:26

equations out two times right in the quiz early on and then you saw it this past time now I I can

## 45:33

expect you to be able to manipulate solve it maybe find an equilibrium value right so one of the

## 45:39

things that for the thorium cycle for instance um

## 45:43

I don't think it was in the problem statement but you have thorium right so thorium 232 absorbs

## 45:48

a neutron turns into thorium 233. that then the case to protectinium 233 which then decays into

## 45:55

uranium 233. that's where we get the fuel that's why we use thorium for breeding right because as

## 46:01

a function of time you can actually build up more Fissile stuff than what you started with the

## 46:06

challenge though is the protectinian protectinium has this half-life of almost a month right so

## 46:11

building up the protactinium, it takes then for it to decay before you start getting the uranium

## 46:16

233. And there's another challenge that would make the use of thorium kind of interesting for

## 46:22

the reactor physicist. The protactinium has a pretty large absorption cross-section, right? So

## 46:28

you build up this protactinium that you need for the uranium, but you're also depleting it at the

## 46:34

same time. It will reach an equilibrium value, but that has a net effect of reducing reactivity,

## 46:39

just like xenon, right? Because in a sense, it's poison until it decays away to

## 46:44

the uranium. So it's no different than treating the xenon, right? You've got to build up from

## 46:51

whatever your source is, and then you've got to decay, just like xenon. So protactinium in this

## 46:56

case would look a lot like that, but it's something that you should be able to take

## 47:01

the equations and come up with an expression for something like its worth. What else did we do?

## 47:09

So that was an evolution of the material in time. We did a little bit on the linear reactivity

## 47:18

model, but I view that as sort of like a standalone by itself. It will not show up on Friday. Maybe
it

## 47:25

would show up on the final exam. And then we went into the kinetic stuff, right? So we talked first

## 47:33

just how would the neutron density change in the absence of the delayed neutron precursors,

## 47:39

right? That turns out to be pretty straightforward. There's not a whole lot going on with one

## 47:43

differential equation. Precursors definitely contribute some complexity, as we're seeing,

## 47:49

right? So obviously, we'd never touch a problem like this on an exam. For that kind of content

## 47:56

and the time that you have on exam, I'm a much bigger fan of things like I drop my phone in,

## 48:01

here's what the power looks like, what's the period of the reactor, things like that,

## 48:05

or estimate the reactivity. And I apologize again for last time,

## 48:09

we had that prompt jump approximation where it's like, why is the sign wrong? I did not read

## 48:16

carefully enough when I was going through the book, taking the equations. The form, of course,

## 48:21

was for a drop in reactivity, like I put in a control rod, not the other way around, right? So

## 48:29

I fixed that in the notes, so you can go back to that. But the prompt jump approximation is useful

## 48:35

for interpreting plots like that, right? You'd see the

## 48:39

initial jump and that you can infer from that then what the reactivity is.

## 48:45

What other stuff? So of course, there's content in the reading that we haven't touched on,

## 48:49

like there's a section on the so-called in-hour equation in the book. I don't know if any of you

## 48:55

had heard of the in-hour equation beforehand. I always think it's goofy because the name comes

## 49:00

from the use of inverse hours for periods. And I've never used hours for any of that stuff. So

## 49:08

I use seconds.

## 49:09

I don't know exactly why that is. But really, there's no... Go ahead.

## 49:16

What about a burn-up in fuel and temperature, or fuel temperature coefficients for moderator and

## 49:24

fuel?

## 49:25

Yeah. So being able to understand what they are and how they would apply, I'm not going to ask

## 49:31

you to... So you've had to compute some of them from expressions in the book. I'm not going to...

## 49:38

Right.

## 49:39

I find it weird to have you write down or internalize some sort of correlation because

## 49:46

the resonance escape... Or sorry, the resonance escape probability, which you need for the fuel

## 49:51

temperature coefficient, has those resonance integrals and so forth. I don't think anybody

## 49:57

needs to write down a fit for UO2 from 1958 for that. I mean, I could give it to you and then you

## 50:04

could analyze it, but that's not so important to me.

## 50:08

Right.

## 50:09

I would be able to use that particular equation. But knowing what it is, being able to compute it,

## 50:15

predicting what happens if I turn the temperature up in my fuel, like, yeah, reactivity will change

## 50:21

golden light, right? That's sort of the underlying principle for where does the fuel temperature

## 50:26

feedback come from in the first place, right? That's an important thing to think about. Same

## 50:33

thing with the moderated temperature coefficient. What is actually driving that? Actually,

## 50:39

somebody tell me.

## 50:40

Yeah.

## 50:40

I got it.

## 50:41

Yeah.

## 50:41

So, for the moderator, the coolant temperature coefficient, what's causing that to happen?

## 50:49

What's causing the reactivity to change if I change my coolant temperature? In what way?

## 51:04

The density changes, right?

## 51:05

Yeah. So, the macroscopic cross section changes because the mass density changes,

## 51:10

right? Because if you go up in temperature for a fixed pressure, then your density will deviate.

## 51:16

And if your density goes down, your cross section goes down.

## 51:19

Depending on where you are on, say, to P over D curve,

## 51:21

it might not lead to a positive reactivity might lead to a negative reactivity but the effect is

## 51:26

there right that you go down in cross-section and you have to kind of trace where that change

## 51:31

leads you in the four factors so things like that would be important for uh the feedback effects

## 51:38

kind of getting back to what's the physical thing happening that changes our balance of neutrons

## 51:43

i think there's anything else i don't know i think in this you know 10 to 15 minutes that

## 51:59

we've talked to we've covered all the topics by name that i would expect um you to be aware of

## 52:06

so yeah all right so uh exam on friday it's the same same procedure as last time uh a sheet of

## 52:16

notes uh you can either extend what you had from last time or get going on a on a new set of notes

## 52:21

um definitely go through old homework problems look at the solutions to understand where you

## 52:28

might have deviated from my my thinking on things

## 52:31

you

## 52:31

but yeah it'll be shorter um than last time for sure and uh yeah i think i think you'll all do

## 52:41

you'll do well all right i will see you on friday
