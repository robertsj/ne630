# L06 Local Audio Transcript

Course: NE 630

Playlist source: https://youtube.com/playlist?list=PLy481lNHlnHoEO95vM-xYX2bydD25v20L

Video: NE 630 - Lesson 6

URL: https://www.youtube.com/watch?v=9ts1NQrdXuE

Video ID: 9ts1NQrdXuE

YouTube upload date: 20230901

Duration: 52:28

Transcript source: Local faster-whisper transcription from YouTube audio.

Whisper model: large-v3; detected language: en.

Generated: 2026-06-28

Note: This transcript is machine-generated from audio and lightly wrapped only. It should be reviewed before being quoted, published, or used as polished lesson text.

Requested language: en

## 00:00

Yeah, I like it much better on work that's usually like hit space and it like

## 00:30

me. Yeah.

## 00:33

Just to the 90s.

## 00:36

I saw Charlie.

## 00:40

I don't.

## 00:43

Yeah.

## 00:46

Yeah.

## 00:50

And that's exactly what she always.

## 00:58

Yeah.

## 00:59

Yeah.

## 01:00

Yeah.

## 01:00

Yeah.

## 01:30

I like

## 01:44

really weird like

## 01:47

that and

## 01:48

although

## 01:49

I

## 01:50

all right

## 02:10

so how'd the homework go

## 02:13

it was due like five minutes

## 02:16

ago right something

## 02:17

uh

## 02:20

uh

## 02:20

so if you hadn't

## 02:22

uploaded it I don't know if it shuts

## 02:24

off automatically but uh try to get

## 02:26

it done ASAP I want I

## 02:28

purposely had it done before the class so that

## 02:30

you wouldn't put it in class or

## 02:32

whatever make this you know like a final

## 02:34

homework session um

## 02:35

I will hopefully get

## 02:37

those uh

## 02:39

graded by sometime over

## 02:42

the weekend uh with uh

## 02:43

some solutions and so forth but

## 02:45

I suspect it was

## 02:47

pretty straightforward based on what we

## 02:50

talked about last time

## 02:51

um

## 02:53

so this time

## 02:56

we're going to I'm going to wrap up some

## 02:58

stuff from from the last uh

## 03:01

bit of material on resonances and then

## 03:03

today we're going to play with

## 03:04

probabilities a little bit I introduced

## 03:07

this

## 03:08

um

## 03:09

kind of as a

## 03:11

I don't know I don't know if we need it

## 03:12

but I talked a bit last time um

## 03:16

about trying to fill in some of your

## 03:18

knowledge on probabilities and I think

## 03:20

it makes sense when we talk about things

## 03:21

like the chi spectrum which is this

## 03:23

mathematical representation for the

## 03:25

neutron energies that come out same

## 03:27

thing with Boltzmann uh Maxwell Boltzmann

## 03:29

and then specifically next chapter

## 03:32

um

## 03:33

which will probably hit the section maybe

## 03:35

not next week uh but the week after

## 03:37

when we talk about the energy

## 03:39

dependence of neutrons in a react so

## 03:41

we've talked about you know the energy of neutrons

## 03:43

emerging from fission but what we really need to

## 03:45

understand is how neutrons start

## 03:47

off from fission and then

## 03:49

propagate through a medium lose energy

## 03:52

cause the fissions that we care about

## 03:54

and what we'll find is in order to do

## 03:57

analysis

## 03:57

like in practice we're going to have to

## 04:00

go from the nasty looking cross sections

## 04:02

that we saw last time and we'll wrap up

## 04:04

today to

## 04:06

single Values that are representative

## 04:08

for all energies or at least several

## 04:11

discrete energies uh bins of energies

## 04:14

right and so that that'll require that

## 04:16

we treat um the neutrons energy spectrum

## 04:19

as a probability distribution.

## 04:20

So it helps to have a little bit of the vocabulary

## 04:24

in place before we get there.

## 04:27

So first thing I want to do is wrap up the resonances

## 04:30

and I'll go back to what I had last time.

## 04:36

Remember, this was the sort of the picture

## 04:39

that motivates why there are resonances, right?

## 04:42

You have the binding energy of a neutron

## 04:44

being added to this target nucleus

## 04:46

to form that compound nucleus.

## 04:47

That neutron also has some kinetic energy.

## 04:50

And if those two things add up to just the right amount,

## 04:53

you're going to hit one of the excited states

## 04:55

of the compound nucleus, this A plus one nucleus.

## 05:02

And if that's the case,

## 05:03

you're going to have a much more,

## 05:05

a higher probability that the reaction happens

## 05:07

because things fit nicely, okay?

## 05:10

And this picture also helps explain things

## 05:14

like why inelastic scattering

## 05:16

requires an incident

## 05:17

neutron to have a certain kinetic energy.

## 05:20

Usually that's going to be tens of keV

## 05:22

up to meV for smaller nuclei, so forth, okay?

## 05:26

But what does this lead to

## 05:28

in terms of the cross-section energy dependence, right?

## 05:32

This is the kind of a very simple cartoon

## 05:34

that illustrates the energetics of the nuclei,

## 05:36

but how does that manifest as the cross-section?

## 05:40

And so if you looked, if you did the reading,

## 05:43

you probably came across this ugly expression

## 05:46

for, here,

## 05:47

I only have it for the capture cross-section.

## 05:49

There was a similar one for the scattering cross-section,

## 05:52

but this is the Bright-Wigner approximation.

## 05:54

So you've probably heard of Wigner before, Eugene Wigner.

## 05:57

He was a Hungarian physicist,

## 06:01

Nobel prize-winning physicist,

## 06:02

who was very, very instrumental

## 06:04

in all of the quantum mechanics and stuff

## 06:06

that led to sort of the nuclear age, right?

## 06:11

He, along with Fermi,

## 06:15

probably the two biggest ones that I can think of,

## 06:17

in terms of like what they did

## 06:18

for kind of traditional nuclear engineering, okay?

## 06:22

But Bright was another scientist at the time,

## 06:25

so they both would have had work in the Manhattan Project.

## 06:29

So what we're seeing here is kind of an ugly expression.

## 06:33

You can come up with an expression

## 06:35

that looks similar to this,

## 06:36

doing some pretty simple quantum mechanics.

## 06:39

So, you know, when I say simple quantum mechanics,

## 06:42

like quantum is not easy,

## 06:44

but, you know, when you take a class on thermodynamics,

## 06:47

or fluid mechanics,

## 06:48

you start off with these little kind of like one-dimensional,

## 06:51

very idealized problems.

## 06:53

Does that, like, that idea make sense?

## 06:55

Well, you can do the same thing in quantum mechanics,

## 06:57

where you have a particle,

## 06:58

it has a wave function subject to a pretty simple potential

## 07:02

that represents like a nuclear force.

## 07:04

And you can get an expression that looks somewhat like this, right?

## 07:08

But the idea here is you've got this cross-section,

## 07:10

and it has an energy dependence, right?

## 07:12

E is the energy of the neutron.

## 07:14

ER is the residence energy.

## 07:16

That's where we,

## 07:17

we expect this thing to peak.

## 07:18

And it's got this one over this business here, right?

## 07:22

So it's going to,

## 07:23

it's going to peak at E equal ER, okay?

## 07:26

Some of the other parameters are not,

## 07:31

I mean, they're defined a little bit in the book,

## 07:33

but this is the peak sigma value.

## 07:39

And that's at E is equal to ER, okay?

## 07:44

And it's a function also,

## 07:47

of the neutron wavelength, right?

## 07:50

You'll see that in the book.

## 07:52

And I gave you a definition in the homework statement

## 07:54

for next week, what this is.

## 07:56

I'm not going to write it down,

## 07:56

because I will see it in a moment in a slide, right?

## 08:00

This is the total or full width, okay?

## 08:08

This has units of EV or energy units.

## 08:13

So why is it called a width?

## 08:15

It's actually kind of a misnomer,

## 08:16

but it's related inversely to the time

## 08:20

that the compound nucleus survives.

## 08:22

Do you remember Heisenberg's uncertainty principle?

## 08:25

Kind of like you can't know something's speed

## 08:28

and its location to both, to like arbitrary precision.

## 08:32

Same thing holds true for energy and time, right?

## 08:36

So the lifetime of this compound nucleus

## 08:38

is inversely proportional to the energy, right?

## 08:42

And that's the energy that we're talking about here, the ER.

## 08:46

Okay.

## 08:46

And then we have the individual partial widths.

## 08:54

And the big thing here would be like,

## 08:58

if I have the width for gamma,

## 09:01

well, this thing is the fraction of reactions

## 09:10

that lead to absorption, okay?

## 09:19

So you put all this together,

## 09:20

it's that fraction is actually, it's, one, two, three, four,

## 09:22

what's dictating.

## 09:23

Like if this compound nucleus is formed, right?

## 09:25

We have the neutron interaction

## 09:27

where the compound nucleus is formed.

## 09:29

This fraction gamma sub gamma over the full gamma

## 09:33

tells you what's the likelihood

## 09:35

that you're gonna have an N gamma reaction

## 09:37

as opposed to like a resonance scattering.

## 09:40

Yeah.

## 09:41

For your partial width term, is that R sub I?

## 09:44

Yeah, so I, in our case, we only have I gamma sub N

## 09:48

for elastic scattering and gamma sub gamma

## 09:51

for the resonance.

## 09:52

So you could have the capture, but you could have fission,

## 09:55

you could have all sorts of other reactions too, right?

## 09:58

But the book and my presentation

## 10:00

only deals with those two, right?

## 10:03

So yeah, we're, I guess I could clarify,

## 10:05

I is equal to N gamma fission, so on and so forth, okay?

## 10:14

So what the Breit-Wigner approximation is,

## 10:17

is a formula that captures the energy dependence

## 10:20

of a single resonance, right?

## 10:22

So at one energy,

## 10:23

this is how we get the peak in the cross section.

## 10:25

Now, when we looked at the cross section

## 10:27

for uranium-235, 238, we saw a lot of resonances.

## 10:31

So is this a good approximation for that mess?

## 10:36

It would be hard, I think, to judge.

## 10:39

What we do in practice,

## 10:41

if we have this single level Breit-Wigner formula,

## 10:44

where level in this case, level means energy level, right?

## 10:47

So one energy of the compound nucleus.

## 10:50

If you have this expression,

## 10:52

but you have multiple resonances,

## 10:53

you use this expression for each resonance and then you add it up okay it's as simple as that

## 10:59

now there are actually more complicated forms than just the single level right single energy

## 11:04

bright vigner there's a multi-level bright vigner approximation that has some weird interference

## 11:09

effects between the energies it's the same thing that you see in the scattering cross section where

## 11:14

you have even in the book it describes it as like this quantum mechanical interference effects

## 11:19

between the compound nucleus formation and this thing called potential scattering which is like

## 11:24

traditional billiard ball scattering okay you can have multi-level and then you can have uh

## 11:29

all the way through something called r matrix theory which is that's like the kind of the

## 11:34

purest physical model for it where not only do you have interference between the different energies

## 11:40

but you have interference between the different exit channels of the reaction that means

## 11:45

is it elastic scattering is it fission all these things interplay

## 11:49

at the end of the day though it's just a gigantic numerical model for the data that we measure

## 11:56

so all the stuff that leads to these resonance parameters and then ultimately the cross sections

## 12:01

that we have it's a gigantic regression problem right it's like somebody took excel all the

## 12:07

measured data and fit it not to an exponential not to ax equal b or something but this nastiness

## 12:14

right where you in that process you have to figure out what are those resonance

## 12:19

energies which are usually pretty easy to pick out because it's like well yeah there's a peak

## 12:23

in the cross section okay so that that helps and then all these other things it's fitted right so

## 12:28

there's a lot of theory that leads to this expression but at the end of the day the

## 12:31

evaluation is a good part data analytics and that's when i joke about the black magic of it all

## 12:38

it's because of that right we're fitting lines essentially um so anyway there's that and then

## 12:46

let me go back to the slides here

## 12:49

okay so we've got that now what i'm going to do is actually show you an example of reconstructing

## 12:57

it because i'm asking you to do this for the next homework okay so i'm going to go ahead

## 13:01

load up some of the stuff for doing numerical stuff you don't have to use python as i've said

## 13:04

before you can use matlab you could try to do this in excel it wouldn't be terrible but i'm

## 13:09

going to use python here so we've got the resonance energy and those two widths we add them up to
get

## 13:14

the total width gamma we have lambda zero which is the reduced

## 13:19

i can't spell reduced wavelength at e equals er right so you remember the de broglie wavelength

## 13:25

from 495 right it's inversely proportional to the square root of the energy and so we choose

## 13:31

that energy f resonance energy this is you can work out the four pi and the neutron mass and

## 13:38

all that that i give to you here as i do in the problem statement and then the peak value sigma 0

## 13:44

is there and then i'll choose some energies for

## 13:55

plotting so this this resonance is the first one so if you look at the um table of values i'll i'll

## 14:02

go to that in a moment so basically in the problem statement for this lesson uh last lesson i give

## 14:08

you six of these resonance uh parameters right so you get six g n or gamma n six g gamma gammas and

## 14:17

six uh energies okay this is just the first one at six point six seven ev right so i'm
reconstructing

## 14:26

using the expression before turning it into barnes and then for comparison i'm loading the

## 14:31

same data that i had showed you last time when we had the messy plots of the the cross sections i'm

## 14:36

loading that same text file which we got from the brookhaven site okay and then i'm just narrowing

## 14:42

the plot so that we're looking at the vicinity of that one resonance okay so what we get out of it

## 14:49

e naught where is

## 14:52

is that i

## 15:00

go and what's it's kind of neat right because the cross-section that we get at a single level

## 15:09

bright penguin this blue curve one matches up as we'd expect because that's where the

## 15:13

peak is this orange curve is from the data that we got from the site so this is like the

## 15:18

evaluated tabulated data that you might use in a code like mcp for instance

## 15:23

right this blue one came from essentially three parameters the two widths and that uh the the

## 15:30

energy the resonant energy

## 15:32

everything else was a function of you know what a neutron is right so it's interesting that you get

## 15:36

something that looks like this and remember this is a log plot right so the fact that we're
capturing

## 15:41

it that well on a log plot means yeah it's pretty good okay and that's just three parameters gives

## 15:46

us that that fit okay there's some other stuff going on that we're not going to get and if we

## 15:51

went out here to energy that's going to decay away there's going to be another resonance right here

## 15:56

so you can imagine taking this blue curve and then adding another one right here that's going to
fill

## 16:00

in some of these things and then you can take it away all the way through so what i've given you

## 16:05

in that problem statement are the resonance parameters for the between uh i think it's the

## 16:10

first six but it takes you all the way through a hundred ev right and so i'm going to have you

## 16:15

reconstruct it just like this i mean you could take my code if you want and do copy and paste

## 16:20

and fill in each of the resonance i don't care how you do it uh but i'd like you to see how it's all

## 16:26

reconstructed okay actually but one quick question

## 16:33

that i have for you if you look closely the blue curve peaks higher than the orange curve

## 16:41

why do you think that is it's something we i touched on it just briefly last time

## 16:56

i said it in words i didn't put any pictures what happens when the target nucleus in this

## 17:03

case the uranium-238 what happens when it heats up right if you've got neutrons going into uranium

## 17:08

but that uranium is you know hot what's happening to those nuclei

## 17:13

yeah so the nuclei themselves are wiggling around which means that they some of them like as

## 17:21

neutrons go in maybe we have this parallel plane into a slab of u238 in some cases they're going

## 17:27

to be moving toward the neutron which means that the neutron doesn't have to go as fast in order

## 17:33

for the kinetic energies to add up to whatever that that resonant energy is right so it broadens

## 17:38

the range of neutron incident energies that will lead to the reaction what that does is it takes

## 17:43

this very sharp blue curve and it takes this very sharp blue curve and it takes this very sharp blue

## 17:45

blue curve and it takes this very sharp blue curve and it takes this very sharp blue curve and it
takes

## 17:45

curve and it starts to flatten it out a little bit right it makes it broader hence doppler

## 17:50

broadening why do we call it doppler broadening where else have we have you ever heard of doppler

## 17:56

before in another physical context yeah where the how sound changes with speed or it's moving

## 18:04

faster yeah right an ambulance goes by it starts off as a high-pitched chirp and then i let you

## 18:10

hear this decrease in the frequency right it's the same thing here neutrons are moving around

## 18:17

so if the ambulance the u238 is coming closer to it the the effective speed is that the neutron

## 18:24

needs is so it's not a one-for-one analogy but that's where the name comes from okay and the

## 18:30

reason why we don't see that in the blue curve it's the resonance parameters that's independent

## 18:34

of temperature it's the way that you handle the temperature is by modifying the the the shape of

## 18:40

it right

## 18:40

for once you assume a distribution for whatever that um target nucleus velocity is right there's

## 18:46

a way to do that it's an ugly math expression that we don't have to go into but um yeah so if

## 18:51

you remember the tabulated data was evaluated at roughly room temperature which is significantly

## 18:57

warmer than zero degrees kelvin okay which is where those resonance parameters are are defined

## 19:03

yeah so just some some comments so we've i've already said that if you have to uh compute

## 19:11

a cross-section for multiple residences you just take the numerical expression right i computed it

## 19:16

as a numpy array right so i've got this array of numbers for one set of resonance parameters

## 19:20

if you want it for multiple you just compute that array for all of them you add it up right they all

## 19:26

that they add on top of each other okay it would be more complicated if we use something that

## 19:31

weren't the simple single level bright wigner right but otherwise it's it's quite similar to

## 19:37

that okay every monte carlo code that you use in your model is uh it's a single level bright vigner

## 19:40

right but otherwise it's it's quite similar to that okay every monte carlo code that you use on the

## 19:40

mix when you you compare it to everything else right you add it up okay you add it up okay it's more
complicated

## 19:40

number one that's the first step right and you put a half of a second of it on top of each other you
add it up

## 19:40

you've ever heard of for neutronics, whether it's MCMP, FITS, OpenMC, uses data that shows up in

## 19:47

tabulated form. MCMP ships with several gigabytes worth of neutron cross-section data. Why? Because

## 19:55

things like uranium-238 require something like 100,000 to 200,000 data points in order to

## 20:01

linear interpolate, right? So the MCMP, for instance, will simulate neutrons at any energy,

## 20:07

the neutron can have any energy for the problem. The cross-sections, of course, aren't

## 20:12

closed-form functions. We can't just evaluate sigma at E. So what does it do? It has this

## 20:17

pre-generated tabulated set of points where it can do linear interpolation, right? And it has

## 20:22

to have close enough energy points so that that interpolation is highly accurate, okay? Now,

## 20:28

if you imagine what happens when we have temperature effects, if I turn up the temperature

## 20:32

from 300 to 600 degrees, that's going to broaden those cross-sections, which means that I'm

## 20:37

going to have to have another 200,000 data points in order to capture this new shape of the

## 20:43

cross-section, okay? Now, if you think about a nuclear system, a reactor, how many different

## 20:48

temperatures are you going to encounter? It depends, but certainly it's a continuum, right?

## 20:55

But to capture most of it, you're going to need whatever your coolant temperature is, which is

## 20:59

about 300 degrees C. You're going to need whatever your fuel temperature is, which ranges from

## 21:03

maybe as low as 300 degrees C in cold conditions up to 12.

## 21:07

100 degrees C in the middle of the fuel. And because you've got to capture the gradient of

## 21:13

temperature, you end up needing something like six different sets of cross-sections for

## 21:18

temperature, which means that that uranium-238 business, that's multiplied by six times.

## 21:24

You add it all up, that's where you get the six to seven to eight gigabytes of data that shows up

## 21:29

on those three DVDs that Los Alamos doesn't want to give you anymore because, well,

## 21:33

ARSIC doesn't want to give it anyway. But the same thing is true for FITS.

## 21:37

The data, though, that's provided by the evaluators, if I go to Brookhaven, the reason I

## 21:41

choose Brookhaven as my source as opposed to some of these other ones, Brookhaven is the,

## 21:46

they're like the lead institution in the U.S. for doing the evaluations of this data, meaning that

## 21:50

if we go to the experimental data and we want to come up with the resonance parameters and

## 21:56

everything like that, Brookhaven is the one in charge of that. There's some work at Oak Ridge

## 22:00

as well, but Brookhaven is kind of the main one. All the data that they provide us, though,

## 22:07

this NDEF6B format that I talked about before, this thing that they've generated from all their

## 22:13

physics models, it's a bunch of resonance parameters. They don't give you tabulated data.

## 22:18

They give you those gammas, the sigma zero, the ERs, all that stuff. That's what they're giving

## 22:24

you. So if we're going to use it in practice, we've got to dump it into a separate set of codes,

## 22:30

right? There's ENJOY, which is the Los Alamos generated one. There's PREPRO, which I think

## 22:35

was Livermore, if you know the history.

## 22:37

Of the Manhattan Project, you know that thing started off at Los Alamos, right? And then there

## 22:42

was some politicking involved, and so they thought it would be good to have a competitor for Los

## 22:47

Alamos, and that's when Livermore showed up. And so PREPRO is the Livermore version of ENJOY.

## 22:53

Then you have AMPEX, which is the Oak Ridge version of all that, and there are other ones

## 22:58

out there too, okay? So this process of going from the evaluated data to ENJOY or through ENJOY to

## 23:07

populated data, that doesn't show up super often in a nuclear engineering curriculum, and that's

## 23:12

sad to me, right? It's something that I've had to learn about kind of just by way of exploring.

## 23:19

But it's good to be aware, I think. I mean, if you want to be a practicing nuclear engineer,

## 23:26

we should know where our data comes from. I mean, if you feel comfortable just going to the back of

## 23:31

a book, reading a table, that's fine. But I think there's value in understanding

## 23:36

where some of the data comes from. And I think that's a good thing.

## 23:37

This stuff comes from if you're using it, okay? Any questions? I do, now that I'm thinking about

## 23:47

it, there is one thing I want to show back at that Brookhaven site. You know, I've talked about

## 23:54

this experimental data versus the evaluated data versus this tabulated data. It's like three

## 24:00

different forms of the data. We only ever really use the tabulated data because that's what we need

## 24:06

in a, you know, tool like MCMP. We're aware now of the resonance parameters,

## 24:10

the evaluated form, and we can reconstruct for this very simple case. But where the hell does

## 24:15

this data come from in the first place? Like, what is it that is being measured and then used

## 24:20

for this evaluation? If we go to this site, I'll go to uranium. I'll do uranium-238. And then I'll

## 24:31

look at the total, okay? There's also experimental data. So this is the evaluated data. This is a

## 24:42

pre-constructed, so they're actually using pre-pro behind the scenes to take all those

## 24:46

resonance parameters and generate this curve. But if you look at the experimental data,

## 24:50

we'll see if this works. I'll plug in so I don't die. Yeah, it's a wild mess, right?

## 25:03

There are all sorts of experimental data sets. I'm not sure, does this go further than that?

## 25:10

Looks like these are the, how many are there?

## 25:14

Right, I guess they've got 53 going all the way back to 1955, okay? And if you just take that,

## 25:30

right? So if I look at that, where's the update? Is there an update one? Yeah, update plot.

## 25:41

Okay, I've taken just these things. So apparently Meister in 1996 was really diving into the first

## 25:48

three resonances of uranium-238.

## 25:51

You've got some Abfelterer in 2001 was looking at these large, broad resonances in that continuum

## 26:00

region. And we've got two measurements out here, right? Well, when you put them all together,

## 26:06

you've got a mess of data with a bunch of uncertainties. And the job of the evaluator

## 26:11

is to take models like that single-level Breit-Wigner. All the more complicated models do

## 26:18

is give you more tuning knobs, essentially, right?

## 26:21

They have more parameters, more degrees of freedom, right? Which makes the fitting process

## 26:26

harder. But this is where we get the data. You've got somebody out there who had two neutron
energies

## 26:32

of interest. They're putting it through a foil of U-238, measuring what comes out, so on and so

## 26:38

forth, right? That's the business of measuring cross-section data, okay? We need the cross-section

## 26:43

data because when you take that, multiply it by number densities, you get macroscopic sigmas.

## 26:49

You take that, multiply it by a flux. You get,

## 26:51

reaction rates. You get fissions per second per centimeter cubed. What do we care about as a

## 26:57

nuclear engineer analyzing a reactor? We care about what's happening in the reactor in terms

## 27:02

of fissions per second, right? We want to know fissions per second over absorptions per second

## 27:07

to give us things like the multiplication, right? Remember I said that K value, it's easy enough to

## 27:13

understand it. It's kind of in the simple picture of one neutron goes in, maybe we get two out. But

## 27:18

to define K, that multiplication factor numerically,

## 27:21

we evaluate that with the model, requires that we have all of this data in place, right? Whether

## 27:27

it's in something like MCMP, what little table of values that we use for some diffusion calculations

## 27:32

later on in the course, but it all has to come from measurements like this that get distilled

## 27:38

through the theory, evaluated, and then tabulated, okay? All right. That is everything I want to say

## 27:47

about this nuclear data stuff. I would love to spend more time.

## 27:51

But I don't think that we have the luxury to be able to do so, okay? Any questions on that? That's

## 28:01

sort of an aside, scratching an itch that had been bothering me for the past week. Anybody going to

## 28:10

the game tomorrow? Anybody supposed to have people come into town who can't because of the damn

## 28:16

airport situation? Anybody aware of that? Like the airport is shut down, like, yeah, makes it
certainly

## 28:26

awkward. Okay. So, probability density functions. I gave you some online reading. It was the best
thing

## 28:36

I could find out there in the time that I had to look for things or books. I even started making

## 28:42

copies, but that copy machine, if you've ever used it, is terrible. So, I wasn't able to get things

## 28:47

to fit. So, I gave you what I got. But I'll summarize kind of the main things that you need

## 28:51

to take away from this for probability density functions. Everything that we care about here

## 28:55

is a random variable passed. What I mean by that is there's some thing that we care about. It has

## 29:03

to be an observable, right? One of my favorite examples to motivate the simplest distribution

## 29:09

or probability density function, uniform, is the time that I would have to sit and wait for a bus

## 29:15

when I was living in Boston, Massachusetts, right? You can look at the bus sign. It says it's going

## 29:21

to come every 15 minutes. The fact is it never stays on schedule.

## 29:25

It doesn't end up being okay most of the time, waiting 15 minutes and getting it. But even though

## 29:31

it says it's going to be there at 8, it's never going to be there at 8. So, there's always a shift.

## 29:36

And so, the time that I actually wait is something that I will observe. It did feel like I waited

## 29:42

longer than I should every time, but it was still a time that I could observe. And the frequency

## 29:47

with which a certain time I would wait would be was roughly uniform, okay? So, when I talked about

## 29:55

a variable, it will be something that is actually observable, right? How far a neutron goes into a

## 30:02

certain medium. One actual neutron, not on the average. I'm talking about one neutron. How far

## 30:06

does it go through a medium? How long do we wait for a radionuclide to decay from a sample, right?

## 30:12

These are strictly observable things. We use probability density functions to describe the

## 30:18

frequency with which we observe certain values, okay? I care for this class primarily about

## 30:25

continuous random variables, things that have values that span from 0 to 10 minutes or something,

## 30:32

right? Where it's not just countable 0, 1, 2. It could be any number between. I could also talk

## 30:37

about discrete things, like how many radioactive decays do I observe in a delta T, right? That

## 30:44

would give me things like Poisson process, right? But which you probably, if you had detection,

## 30:48

that probably rings a bell, okay? So, I'm only going to care about continuous random variables,

## 30:54

and I'm only going to care about

## 30:55

one-dimensional things. I'm not going to try to go into multiple dimensions, right? So,

## 31:00

for a random variable x, we're going to use, I'm going to use f of x as my PDF, right? So,

## 31:08

probability density function PDF satisfies these things. It has to be positive everywhere

## 31:16

where the random variable has a possible value, right? So, if I'm waiting for a bus,

## 31:21

I can't wait an infinite amount of time for the bus, right? Like, it says I'm going to,

## 31:25

it'll come every 15 minutes. So, the time I wait naturally should be zero minutes to 15 minutes,

## 31:32

anywhere in between that. So, if my a would be I wait zero, b, the upper bound would be I wait 15

## 31:37

minutes. So, it has to be positive. You can't have a negative probability, okay? Probabilities

## 31:42

are naturally zero or greater. If I'm outside of the range of possible x values, right? The times,

## 31:50

right? I can't wait a negative minute, and I can't wait 16 minutes if my maximum weight,

## 31:55

I'm supposed to be 15. We call this the support, right? The possible values of our random variable

## 32:01

that's called the support of the corresponding distribution, okay? And then, very important,

## 32:06

the integral over the entire range should be equal to one. This is just a statement that

## 32:14

says all probabilities add up to 100%, right? You can't miss out. So, if I gave you a function,

## 32:20

I said this is the probability distribution, you might say, are you sure? And then,

## 32:25

I actually checked that it's normalized, integrated over the range of x to make sure

## 32:29

that everything adds up to one or integrates to one, okay? So, we use these sorts of functions

## 32:35

to describe random things, random processes, okay? Because they're continuous, which means

## 32:42

that everything, basically, the probabilities associated with a certain value is like an area

## 32:50

under the curve. That means if I try to define the probability for a single

## 32:55

value, I'm going to be able to get a certain value. So, if I try to define the probability for a
single value,

## 32:55

I'm going to be able to get a certain value. So, if I try to define the probability for a single
value,

## 32:55

like, what's the probability I wait exactly five minutes for the bus if the wait time is 0 to 15?

## 33:03

What's that probability for me to wait, to be there for exactly five minutes? It seems like

## 33:12

there should be a non-zero answer for it, but it turns out it's zero, right? At least in this

## 33:17

mathematical model of it, right? That there's a probability that I wait between four and a

## 33:23

half and five and a half minutes, right? That actually has an assignable value.

## 33:26

But just one number, it's zero, right? Because the associated area under the curve is the height of

## 33:33

that probability times the width, which is dx. Well, dx is infinitesimally small, so we wouldn't

## 33:41

have a value. So, anytime we're using a continuous treatment, we only ever get probabilities for

## 33:50

finite ranges of the value. So, it only ever makes sense for my bus waiting example to say between
this

## 33:56

time and this time. Never, what's the probability of this time specifically, right? That's probably

## 34:03

the main thing to take away from that. All right. So, my favorite distribution is probably the

## 34:13

uniform, because it's the easiest one, and it's the one that we can use computationally to give

## 34:18

values to every other distribution through some sort of sampling technique. Now, some of what

## 34:23

I'm talking about, maybe we won't need. Mostly, it's things that I'm interested in, but it also

## 34:29

relates a little bit to a course I hope to be teaching in spring, ME777, Monte Carlo. So,

## 34:40

actually, that's one that you might consider, too, because I hope that I can do the 415 that

## 34:45

I was talking about, but the Monte Carlo might be more relevant. So, who had Dr. Dunn for 495?

## 34:54

Right. So, Dr. Dunn and Dr. Schultes, but both of them have retired now.

## 34:59

They together wrote a book called Exploring Monte Carlo Methods and taught a course

## 35:03

probably for the past 10 years, sort of a general course on the methods. Of course,

## 35:09

they're nuclear engineers, and in particular, folks who cared about neutron or particle

## 35:14

transport. So, they kind of went into it with that background, and it shows, but it's a much

## 35:21

more general technique that can be applied to engineering or really any technical discipline

## 35:26

where you have computational models.

## 35:29

You almost always have to treat the uncertainties involved in some way, and Monte Carlo methods as

## 35:36

a class of methods let you do that, right? So, we'll get a very, very, like, we'll get a baby

## 35:41

version of it at the end of the lesson today, okay? But anyway, so that's kind of driving why

## 35:49

I'm talking about this, too, because I'd like to teach that course, and maybe some of you will find

## 35:52

this stuff interesting, okay? So, these are my three probability distributions that I'll use as

## 35:58

an example.

## 35:59

There are other ones, though, right? And, in fact, you have to look at them for your homework

## 36:04

for next week. There's the Maxwell-Boltzmann distribution, right? I'm not going to write it

## 36:08

down because it's there in the book, and there's also the Watt spectrum, which is used to model

## 36:13

this fission distribution. I don't know if he calls it the Watt spectrum, but that's what the

## 36:17

spectrum is. The same things that we talked about here apply to those distributions, right? Sampling

## 36:23

from them is a little bit more challenging. I'm not going to have you do that, but computing things

## 36:26

like means, expected values.

## 36:29

You can use what we're doing here, okay? All right. So, these are just a couple examples of

## 36:38

these distributions. So, we have the uniform exponential and then the normal, which is also

## 36:44

known as the Gaussian distribution, okay? So, what I've done here for the uniform distribution,

## 36:57

it's a uniform between x equal 2.5 and 7.5, right? So, this could be like, I will weight 2.5 to 7.5,

## 37:05

minutes for my bus, okay? And it's uniform, so it's a flat function. The only thing that makes

## 37:11

it not flat all the way is the fact that to the left of 2.5 and to the right of 7.5, those values

## 37:18

don't exist. Everything else is flat. So, you can see here that the value of the PDF is 0.2.

## 37:26

Where does this come from? Why does it have that value?

## 37:40

Yeah. So, if I integrate a line, right? So, the area under, this is a particularly easy example,

## 37:47

which is probably also why I like it. It's a rectangle, right? There's no curvature here.

## 37:51

So, the area of this rectangle has to be equal to what? If it represents all of the probabilities

## 37:58

associated with this variable. It has to be 1, right? So, if I know that my width is the 5,

## 38:04

as you point out, then the height has to be 1 over 5 so that the product is 1, okay? Less

## 38:09

easy to say the same thing for the orange curve and then the green curve, right? But these are

## 38:15

distributions, so you could compute the area, and it would be at least approximately 1 for this

## 38:20

range, okay? So, we've got the uniform distribution. We have the exponential distribution,

## 38:25

right? Where I have the parameter is 1 over 3. So, the exponential distribution,

## 38:32

go over here, okay? The exponential distribution,

## 38:48

for the random variable x, has a parameter lambda. And this thing looks like lambda times

## 38:56

e to the minus lambda x. All right. Makes sense. It's an exponential.

## 39:04

What processes follow or are well modeled by this exponential distribution? So, decay is

## 39:14

good,

## 39:18

and,

## 39:19

and,

## 39:20

but,

## 39:20

but,

## 39:20

and,

## 39:20

and,

## 39:20

specifically for decay what part of that process the time for a certain nucleus to decay right

## 39:34

so there's another process related to decay that would not be modeled by this but would in fact be

## 39:41

a discrete distribution oh dear god what the hell happened here okay that's no good i don't know

## 39:58

what what happened there yeah what other process would be represented by the exponential
distribution

## 40:05

the one that we saw more recently than the decay example so remember the time it takes for

## 40:18

something to decay is related to the exponential decay of or exponential attenuation time of number

## 40:26

that you start with where else did we see attenuation earlier this week right when we

## 40:34

talked about neutrons going

## 40:36

into a slab so this is also a good model for exponential attenuation of a particle going

## 40:47

through a slab we could easily switch lambda for sigma if you remember what is sigma it's

## 40:57

the macroscopic cross-section has units of one over centimeter it represents the distance

## 41:02

i'm sorry that's that basically the interaction probability per unit path for a neutron if you

## 41:09

take

## 41:09

one over sigma what do you get you get the mean free path the the the distance on the average

## 41:16

that a neutron is expected to go before it has a collision if you think about what lambda is lambda

## 41:21

is the decays per unit time of a nucleus if you take one over lambda you get the mean time to decay

## 41:30

right it's a completely analogous right and it shows up in any of these exponential attenuation

## 41:35

things so this represents the distribution probability of the distribution of a neutron

## 41:39

so this represents the distribution probability of the distribution for neutrons entering a slab

## 41:42

in attenuating right with where the material has this uh cross-section capital sigma so

## 41:58

those are examples of the functions if i want to be able to use it right i've got to be able to

## 42:09

compute things like expectation values there are really two things that we have to to be able to

## 42:13

compute one a probability that the variable the random variable falls in a certain range and like

## 42:18

i said before that's you integrate the value of the value of the value of the value of the value of

## 42:20

the value of the value of the values of the terms a of it's not what you do in

## 42:24

the

## 42:46

unit

## 42:48

hardly

## 42:49

shouldn't work

## 42:49

the theory of this is really strong to us Secondly, this bar itemially controls the

## 42:50

of my random variable g of x where x has a distribution defined by f of x the expectation

## 42:57

value of g of x is given by this expression right so probably the very first one to consider is what

## 43:05

if we let g of x be x itself right if i do that then what what i'm actually computing is

## 43:16

did i do wrong here um i wonder if i'm not connected or something i feel like something

## 43:48

happened to my system there we go yeah that's the expectation value of x have you ever seen

## 43:56

this expression before you should have seen it in things like finding centroids

## 44:08

right so if i want to find the expected value of x i have to weight it with my probability density

## 44:18

and integrate it with my probability density and integrate it with my probability density

## 44:18

over the the range right so this thing has we often we would use things like bar of x

## 44:27

right it's the mean so the expected value in this case is is the mean if we were to take this this

## 44:34

random variable sample it but you know observe it a million times on the average we'd expect it to

## 44:39

have this numerical value now what if there is definitely something goofy with the

## 44:57

the

## 44:57

i had just a terrible time earlier trying to um fix the notebook so i used jupiter notebook but

## 45:09

they made this transition to a a backwards incompatible form and so i wasted a good part

## 45:15

of my morning trying to figure that out okay right so we could compute the expected value

## 45:22

that gives us the the x bar the mean value what about if we take the expected value of x which we

## 45:29

now know is the average

## 45:30

we take x minus that square it and then find the expected value of that quantity anybody know what

## 45:37

that is maybe a different way of looking at it coming from a different direction

## 45:44

it would be the variance right so if you like in plain english what we would be doing if we

## 45:52

set g of x equal to x minus the expected value of x squared what we're doing is over that entire

## 45:58

range we are adding up all the squared deviations and we're adding up all the squared deviations

## 46:02

right it's no longer discrete so we have to do it continuously so we're getting the squared

## 46:07

deviation and then we're taking the average of it okay that's exactly what the variance is right

## 46:13

we're seeing how far off the mean is from every other value of the random variable or the function

## 46:18

f of x of that random variable okay so that that is the variance so we get the mean and the variance

## 46:24

as as expectation values but this applies much more uh generally right what we're going to do

## 46:32

next chapter is take cross-section values right so cross-sections are functions of energy we're

## 46:38

going to take a probability density for the flux right so it'll be some function of e and we're

## 46:44

going to compute flux weighted or spectrum weighted cross-section value that's going to

## 46:49

give us effective cross-sections that will let us capture on the average appropriate reaction rates

## 46:55

using say one value as opposed to using 200 000 values for you know uranium 238 i would

## 47:02

say that a large part of reactor physics in practice is all about being able to go from

## 47:07

those massive cross-section sets down through a certain number of approximations to get

## 47:12

simple values that you can use to compute the quantities of interest right certainly we do that

## 47:18

in an undergrad class like this but even in practice a good part of the reactor physicist

## 47:23

job is to do that either do understand or some combination of all these simplifications

## 47:32

that go from the massive data that we have to you know some final expression okay for you know k

## 47:37

effective for instance all right just a couple minutes left um any questions so far i mean is

## 47:47

is this new stuff at all or is this primarily familiar

## 47:52

ish okay so is anybody in walter mcneil's class

## 48:02

okay so it's some this stuff should definitely be not new right and so i think he actually gave

## 48:09

me the idea of at least sketching out part of it okay um of this little simulation so what i'm

## 48:15

going to do is i have a material with a macroscopic cross-section here i've set it to one we can

## 48:21

explore what happens later i'm going to shoot 1000 neutrons into this slab right we know already

## 48:29

from earlier this week that they are subject to

## 48:32

exponential attenuation right we've kind of built up that model and then applied it so

## 48:36

what i want to do here is sample how far these neutrons go into this medium before they have

## 48:42

their interaction and once it has that interaction we're going to stop caring all we care about are

## 48:46

those neutrons that have what we would care about are the neutrons that have not had an interaction

## 48:51

right the uncollided intensity here i'm just going to to compute that distance where they

## 48:57

have that interaction keep keep track of that this is essentially the world's most important

## 49:02

the world's simplest monte carlo simulation right and from from the the location or the distance

## 49:08

that they go before having that interaction i can build up estimates of the neutron flux i

## 49:12

can compute reaction rates i can figure out how many visions or visions happen here versus here

## 49:16

this is like the very first step of that process okay so i have a number of particles i'm going

## 49:23

to take this function expone.rvs this is just the built-in scipy function to get random numbers from

## 49:30

the exponential distribution

## 49:32

yep in fact let's see will will this work out here is that better okay and then i'm going to use

## 49:42

mattplotlib's histogram function to show that right so i've got a thousand particles i'll end

## 49:46

up with a thousand distances and what i want to see is what what do those look like on the average

## 49:51

okay and lo and behold it looks like an exponential distribution of course if you

## 49:58

sample from an exponential distribution then you should reconstruct the distribution

## 50:02

and then if you do that you can reconstruct the same distribution in effect all the histogram is

## 50:06

is a is a piecewise constant representation of your your underlying distribution okay it won't

## 50:14

always be so easy right because in some situations we'll have many more complicated functions as
part

## 50:21

of that that neutron's lifetime right in a code like mc and p or fits for instance you'll have a

## 50:28

neutron you sample how far it goes that's honestly one of the things that i'm going to be able to do
is

## 50:32

the key pieces in the life cycle of a neutron in a monte carlo code you sample how far it goes

## 50:38

if if it goes and has a collision great you do the collision you figure out what its new energy

## 50:43

is after you know having a scatter or you record its death if it had an absorption event or if it

## 50:49

left the system you can put a you can add a counter for i've left the building or if you're

## 50:54

going between different material regions you can move it to the boundary and then start life again

## 51:00

but this little sampling procedure is the fundamental unit in a monte carlo simulation

## 51:07

right there's a lot more going on because of the more complicated data uh the various reactions

## 51:12

that you could account for but this is this is it four lines of code is like the workhorse under the

## 51:18

hood of monte carlo simulation codes okay and so if you want to learn more about that sort of stuff

## 51:24

uh either look for walter's class you know in the next cycle uh you could look for me777

## 51:30

next semester or um talk to one of the nuclear faculty for doing some research um and using

## 51:38

monte carlo tools right where you'd be benefit from having kind of an understanding of what's

## 51:42

going on behind the scenes so that takes us to the end uh happy friday i'll get the homeworks

## 51:50

uh looked at maybe turned around by monday it's easy if i have people staying at my house i like

## 51:55

to be quiet or not in my house and so that forces me to be at the office where i'm like

## 52:00

more productive so the weekends strangely are my productive time um if you have questions of

## 52:05

course stick around as i pack up otherwise enjoy the football game for those who are going and i'll

## 52:10

see you all on monday no i won't see you on monday it's labor day i'll see you on wednesday enjoy
the

## 52:16

long weekend
