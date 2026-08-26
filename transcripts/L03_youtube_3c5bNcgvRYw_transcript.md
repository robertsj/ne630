# L03 Local Audio Transcript

Course: NE 630

Playlist source: https://youtube.com/playlist?list=PLy481lNHlnHoEO95vM-xYX2bydD25v20L

Video: NE 630 - Lesson 3

URL: https://www.youtube.com/watch?v=3c5bNcgvRYw

Video ID: 3c5bNcgvRYw

YouTube upload date: 20230825

Duration: 53:03

Transcript source: Local faster-whisper transcription from YouTube audio.

Whisper model: large-v3; detected language: en.

Generated: 2026-06-28

Note: This transcript is machine-generated from audio and lightly wrapped only. It should be reviewed before being quoted, published, or used as polished lesson text.

Requested language: en

## 00:30

I'm glad to hear of talks of trombones and other things that suggest you have

## 00:49

lives outside of this class for now kind of um what was I gonna say oh uh tonight's the

## 00:59

international night at the union I forget what they call it it's different from years past but

## 01:05

I'm guessing it'll be the same where they have tables from different student groups that

## 01:10

represent different nations or cultures or whatever I remember enjoying that I'm not sure

## 01:15

how great it'll be in 105 degree temperatures but um anyway thought I'd point that out is there

## 01:22

anything else of interest um I don't think so a little bit of administrivia uh you'll

## 01:31

notice I posted the first homework and the problems that are in that homework are the

## 01:35

same ones that you should have seen on these uh pages so right so we've got three for today

## 01:45

let's just go back to oh there's the image there there's the video right so from last

## 01:55

time there is one problem from the book and then uh an open-ended one somewhat open-ended

## 02:02

fragment pair so I'll touch that on that a little bit as we get started today

## 02:07

um for this one I'll point out fission is kind of a challenging problem that

## 02:13

is it I've noticed in the past say five years there's been a lot of research to better understand

## 02:20

the fundamentals of fission as you can imagine when you have that many nucleons interacting in

## 02:24

some way under the hood to describe that requires a hell of a lot of quantum mechanics that is
beyond

## 02:32

our understanding as it were right I I kind of understand some of the basic principles things

## 02:36

things like doing modeling electrons not so bad but even electrons for larger atoms it's really

## 02:44

complicated to to model that from like a first principles perspective right there if you talk

## 02:49

about material science trying to design new materials trying to design new semiconductors

## 02:54

with appropriate band gaps and so forth all that happens at that electronic scale and to model that

## 02:59

using software numerical methods is incredible

## 03:02

incredibly challenging it's almost impossible to do the same thing for nuclear effects because we

## 03:07

simply don't know what the nuclear forces right you have two nucleons together it's like yeah I

## 03:12

know that two neutrons will tend to glue together along with some protons but we don't we don't we

## 03:17

can't write down what that looks like right we don't have a a easy well understood way to describe

## 03:26

how that strong nuclear force actually binds these things together so a lot of what we have in

## 03:31

practice is

## 03:32

a combination of what we would call a phenomenological model meaning that we observe

## 03:37

things and we kind of mapped map to it along with a lot of measurements and so forth right and we'll

## 03:42

get into how that plays out for us uh over the actually probably that'll be starting Monday when

## 03:48

we get into a review of things like the neutron flux and interactions how far does the neutron

## 03:54

go through some material before it has a collision on an average um so anyway point all that out

## 04:02

because it may or may not be challenging to find I did some Googling myself you can find some
examples

## 04:09

so you don't have to just whatever you do cite your resources right that's just good practice

## 04:15

okay any questions from lessons one or two or even the computational example

## 04:23

um from Tuesday night that I posted thank you again for those who were able to make it and keep me

## 04:30

company easy peasy so far

## 04:34

I hope so all right so then let me go back to my lesson three stuff okay there's all that and then

## 04:48

I will go to my can we see this all right or do I have to do the lights is it any is it fine as is
or

## 05:00

really the lights okay perfect thank you okay so

## 05:09

last time we talked about fission and we cared mostly at that point about those prompt neutrons

## 05:15

right because the prompt neutrons can uh naturally form this chain reaction and as you go from one

## 05:21

generation to the other getting either more neutrons or fewer neutrons or you keep the

## 05:26

same number of neutrons remember that's what we uh where we introduce this concept of multiplication

## 05:32

and that multiplication factor K which is one of the most fundamental concepts in basic reactor

## 05:38

physics even even

## 05:39

full reactor physics in practice there there's a whole slew of applications that is based primarily

## 05:46

on the calculation of what K is for given system all right uh but the other things that we get and

## 05:51

the things that drive the power that we get out of fission are those two massive fission fragments

## 05:56

that then go through the material lose losing all their kinetic energy which shows up then as

## 06:02

heat okay one of the the properties of these things is that they tend to be incredibly neutron rich

## 06:09

right if you remember the chart of the nuclides right you have all these nuclides they have a

## 06:15

given mass number and a given Z number proton number they have a given number of protons and

## 06:19

a given number of neutrons there tends to be a stable ratio of protons to neutrons and that

## 06:26

changes with the overall size of the nucleus the more massive the closer to things like uranium you

## 06:31

get the more neutrons you need to keep everything glued together you remember from 495 why you would

## 06:39

need these

## 06:39

neutrons to help keep things glued together as you go to the right on the mass number

## 06:47

as you get bigger and bigger nuclei why would you need more neutrons to act as glue

## 06:53

we'll give you a go ahead yeah the columbic uh repulsion of the proton so you simply need those

## 07:01

neutrons in the strong nuclear force again we we understand that there is a nuclear force that is

## 07:07

keeping everything together we don't understand necessarily all the details certainly I don't I'm

## 07:11

sure there's been work over the past 50 years to uh highlight a little bit more but what that means

## 07:16

is if you go from something that's really really big with a whole lot of extra neutrons for the

## 07:20

glue and you split it into two things that are smaller so you're scaled back to the left on that

## 07:24

that that graphic you end up with a higher neutron to proton ratio than than would be found in the

## 07:31

so-called valley of stability right so there's actually a really nice graphic from another book

## 07:37

that um

## 07:41

used for a class like this but i think it's it's still a little bit too advanced um it's actually

## 07:48

a book but the author's name is paul royce uh he's was is somehow he was uh in france at edf

## 07:56

their nuclear power laboratory um so it's a translation which means that some of the some

## 08:02

of the language is a little weird you know to me anyway um and i'm not sure how that would

## 08:08

uh be digested by by a class of this nature but this is one way to look at it there are

## 08:14

plenty of other ways that that can be used to show this stuff but at the

## 08:20

uh the horizontal axis here is z so the number of protons and then the vertical axis is n the

## 08:29

number of neutrons this dashed line represents the so-called valley of stability right so if i took

## 08:36

a a nucleus of

## 08:38

a certain number of protons here right and i went up the right number of neutrons for it to be
stable

## 08:45

right for it not to be radioactive right but when i talk about stability the opposite of stability

## 08:51

is something that's radioactive those are our two options in their physics plan so if i if i'm

## 08:57

stable i'm on that line but because i'm this massive uranium-235 or whatever it is and i'm

## 09:02

split i come with that ratio that i started with with neutrons to protons and so i have

## 09:06

many more now in that fission

## 09:08

process we tend to have fission fragments that cluster into these two loads if i were to draw

## 09:15

this out in a slightly different way i and in fact i think this is maybe one that is in our textbook

## 09:25

now right it would be something like this where i have a distribution of these things it's a

## 09:31

bimodal where i'm centered at roughly 90 and roughly 140 as a function of

## 09:38

a now of course for a given mass number 90 there are several combinations of z and n that that can

## 09:45

add up to that right and so there will be some sort of distribution and you'll see that in some of
the

## 09:50

data if it were available but primarily we end up with things that center right around 90 and right

## 09:56

around 140 and that's what we're seeing in this image here right you can imagine this if i if i

## 10:02

took it rotated it down and then showed it almost like as a histogram or something like that you

## 10:07

would see the bimodal

## 10:08

now why why would we get these two separate let's say centroids why why do we have something that

## 10:15

is a little bit smaller at about 90 nucleons and something a little bit larger at 140. if you think

## 10:20

about they add up and you get close to the you know whatever the 235 that you might have started

## 10:25

with why would we have two separate things i don't expect anybody to know but maybe maybe you

## 10:35

did some reading and caught something somewhere yeah doesn't depend on what they came down to

## 10:43

uh it

## 10:44

not necessarily because the decays would be in the future so by the time things are kind of

## 10:48

organizing that that that shouldn't impact it i don't think so i don't know that there's actually

## 10:55

a clear answer but but something that i've read and it it makes a lot of sense uh and it has to

## 11:01

do with something called magic numbers you remember from 495 uh this concept of of that magic number

## 11:10

raise your hand if you've heard of that before okay so

## 11:15

i guess if you had me i know i talked about it might not have showed up uh unless

## 11:20

it were me talking about it um so magic numbers are are these special numbers of nucleons that

## 11:27

tend to give a lot of stability to the nucleus it it's not an exact analog but it's very close

## 11:34

in a conceptual sense to electron orbital shells closing so if you think about it on

## 11:41

the upper left of the periodic table you have hydrogen and below that you have lithium and you

## 11:45

have a whole bunch of these other metals that what do we call that first column uh the what's that

## 11:55

yeah so those things if you could describe them in one english word what would it be

## 12:04

you toss lithium or sodium or something in water what happens

## 12:07

it's it's a reactive reactive right chemically reactive incredibly reactive why because those

## 12:13

things have if you're in the first column or in the second column you've got one lonely electron

## 12:19

or two lonely electrons that would much rather be paired up with say something on the right hand

## 12:24

side that's missing one or two which is why those first two columns love to match up with the things

## 12:29

in the right the third and second to the from the right right because the very right most is

## 12:37

totally stable okay so that's why things like those alkaline metals will pair with things like

## 12:42

fluorine or oxygen right because the oxygen wants those those electrons same thing in so that that

## 12:48

pairing and then you remember things like the s orbital the d p does that bring a very distant

## 12:55

belt from like a chemistry class it's the same thing in nuclear physics with these magic numbers

## 12:59

the numbers don't line up with the same numbers of electrons that we see in the period of periodic

## 13:04

table and stability there but they there is a pattern so one of them is 50. one month is four

## 13:09

which is why helium two and two is really really um uh stable i believe there's one in the 20s i

## 13:17

I can't remember them off the top of my head, but the 50 and the 82 are important because

## 13:24

basically if you're in one of these lobes, either the number of neutrons or the number

## 13:29

of protons or possibly both are happening to center right around one of those magic

## 13:33

numbers.

## 13:34

So probabilistically, we're sort of like average at a very, very stable number of

## 13:39

nucleons, either number of protons or the number of neutrons.

## 13:42

And then we have these, you know, nothing is perfect, right?

## 13:45

And so we have distributions about those values.

## 13:49

So I'd point that out.

## 13:50

The way to read this graphic, and I'll be uploading this too after the fact, is the

## 13:55

very dark circles, that is a value, a probability that you get that ZA combination.

## 14:04

It's the probability, I think, Y here, greater than 1000 PCM.

## 14:10

Now, if you had me in 495, maybe you remember PCM stands for percent milli.

## 14:15

That means 1% times than one in a thousand.

## 14:20

So what you get is one part in 10,000.

## 14:23

It's just a way that it's often used in nuclear engineering, specifically with respect to

## 14:29

things like the multiplication factor or the reactivity, a concept we'll learn about later.

## 14:35

It's just a shorthand for dealing with really small numbers, right?

## 14:39

It makes it easier to see.

## 14:40

So anyway, these things that are dark, that's a percent or more you would expect.

## 14:45

And then as you get away from those centers, you have things that are much less common,

## 14:51

much less frequent, right?

## 14:52

So all in all, there are, at least our textbook suggests that there are 40-ish pairs that

## 14:58

you get out of that immediate fission process, right?

## 15:02

So you get 40 possible pairs of fission fragments, which would require that there are something

## 15:07

like 80 things in play.

## 15:09

But then remember, things start to decay and you start to see other things show up in a

## 15:14

matter of seconds.

## 15:15

And some of those things lead to neutrons, which is where I will go next.

## 15:23

So of all the things that live in that chart of the nuclides, there are about 100 processes

## 15:29

that ultimately lead to the ejection of a neutron sometime in the future.

## 15:35

If you look at the chart of nuclides, there are some things that exist as neutron emitters.

## 15:41

The things that we care about often are these fission fragments.

## 15:45

That are strongly neutron rich.

## 15:49

They get rid of their neutrons by converting them into protons through beta minus, right?

## 15:53

Basically the ejection of an electron.

## 15:55

But sometimes the daughter product that they leave behind is also often radioactive.

## 16:00

And sometimes it's so energetic, it has an excitation level beyond what's called the

## 16:06

neutron separation energy, right?

## 16:08

Which is something that if you still have your 495 book, you can go.

## 16:11

But basically, it's like we've done.

## 16:14

We.

## 16:15

Know what binding energy is, right?

## 16:16

The binding energy is the difference between this nucleus all by itself.

## 16:21

And then when you take all the nucleons and split them apart, right?

## 16:25

That the mass difference then multiplied by 931.5, MEV gives you what that binding energy is.

## 16:32

The neutron separation energy is similar, but it's the difference between a nucleus and

## 16:38

then the nucleus with one neutron plucked away, right?

## 16:43

And you will get different masses and often.

## 16:45

It will be that it's almost you always need to take energy or have energy to remove one

## 16:51

of these nuclear neutrons.

## 16:53

However, if the starting nucleus has excitation energy, it's already dancing really, really

## 16:59

violently. It might have enough energy to just knock off one of the neutrons itself.

## 17:03

But the only reason that it had that energy is because it is the result of a beta decay.

## 17:09

OK, so that's where the neutrons of interest come from that can and will influence that chain

## 17:15

reaction discussion that we had last time.

## 17:17

The neutrons that come out are not quite the same as the prompt neutrons.

## 17:21

Somebody remind me, what's the average energy of a neutron coming promptly out of fission?

## 17:26

2 MeV.

## 17:27

Turns out that these delayed neutrons, the things that come out either a few seconds later or up to
a

## 17:32

minute later following the fission event are less energetic, somewhere between 0.2 and 0.6 MeV.

## 17:39

So hundreds of KeV, right?

## 17:41

That has some impacts, but it's still compared to, say, 0.2 MeV.

## 17:45

Thermal neutrons, they're incredibly energetic.

## 17:47

OK, now, of these hundred processes, there are a couple of examples that I wrote down.

## 18:00

Let's see where we go.

## 18:02

OK, and they're pretty big ones.

## 18:04

So one is Bromine 87, which will beta decay into, well, what will it beta decay into?

## 18:23

What will happen?

## 18:23

So I don't expect you to know the chart.

## 18:26

OK.

## 18:26

The chart of the nuclides.

## 18:27

In fact, I wouldn't, outside of some things that I just remember.

## 18:30

But if I start off with 87 nucleons, does beta decay change the number of nucleons?

## 18:39

No.

## 18:40

Not the total number of nucleons.

## 18:42

What will happen to Z?

## 18:47

Right, so Z goes up, N goes down, A stays the same.

## 18:50

What we end up with is Krypton, right?

## 18:56

Krypton 87.

## 18:56

OK, and it's in an excited state.

## 18:59

So we'll often put a star to indicate that sort of thing.

## 19:02

And then this will decay into Krypton 86.

## 19:09

And if it goes from Krypton 87 to Krypton 86, what must be there along with that Krypton 86?

## 19:18

A neutron, right?

## 19:20

So that's one of these examples of neutron decay.

## 19:23

And because this, the, this, the half-life from Bromine 87 goes up, then this goes up.

## 19:24

The attack goes down.

## 19:25

And that's just a few second.

## 19:26

OK, so that's the start point.

## 19:26

So we're going to put a start point which indicates that there are many nucleons that go up.

## 19:26

chromine 87 to the krypton 87 is roughly a minute right so remember before we said that that the

## 19:33

neutron lifetime if we only cared about those prompt neutrons was something really really small

## 19:38

10 to the minus 6 10 to the minus 7 seconds if you start mixing in a little bit of like a source

## 19:44

of neutrons that shows up a minute later the average time dependence changes significantly

## 19:49

and it goes basically you have much more time to react that's why we can operate reactors this

## 19:55

presence of the delayed neutrons okay another example is iodine 137 which goes to

## 20:03

xenon 137 by way of beta emission and then this of course goes to xenon 136 plus its delayed

## 20:12

neutron right and there are again roughly a hundred processes that look like this that

## 20:18

would lead us to a neutron emission it all starts with this thing being in an excited state

## 20:25

you

## 20:25

beyond the neutron separation energy okay and that's what this thing here s sub n is

## 20:35

in fact there's one other thing that i can do quick so if i do bnl new dat

## 20:45

three and this is a site that i had brought up earlier um and talked a bit so this this is the

## 20:54

chart of the nuclides in a very condensed graphical form a lot of things that we can

## 20:58

look at here um one of them is the neutron separation energy and you can see you know

## 21:05

just hovering over uh if we look at the menu this would give us sort of the the amount of

## 21:11

energy it would require to yank one of those neutrons off an otherwise stable nucleus okay

## 21:16

uh other things that we could do to do decay mode right so all the beta emitters are are here

## 21:28

um which just means that they have too many neutrons and they want to get to the left to

## 21:34

this region of stability right the so-called valley of stability so uh it this is a good

## 21:40

um site and if you want things like half-life you can hover over I guess that's what the default is

## 21:45

so of course the things that are black their half-lives are not measured because they're

## 21:50

apparently stable and as you go away from the the stability you start to see basically the halflives

## 21:57

get shorter and shorter and shorter the further away you get right so there are a lot of ways to

## 22:01

visualize stability half-life is one of them you could look at binding energy per nucleon you could

## 22:05

look at all these other things they're all related right um so yeah this is one site that you can
use

## 22:14

lots of other sites that you can use to fill in any data gaps that we might have from from the

## 22:19

textbook okay all right so i thought then that i would take the rest of the time to go through

## 22:37

setting up and solving some radioactive decay problems now i know you've seen some of this

## 22:43

stuff before and in fact depending on what sorts of problems you've been asked to to solve in the

## 22:48

past none of this might all this might just be reviewed and i think that's totally fine

## 22:53

um how long ago did you take math 340

## 22:57

it's like a year or two years going on three years now

## 23:02

right so i mean if like unless you had done so in a another class i mean could you

## 23:10

do you feel confident that you could just walk into a classroom and solve an initial value problem

## 23:17

with no prep it probably depends on the problem of course but do you feel like you you you remember

## 23:27

sort of the spectrum of typical problems and the techniques that you've been using

## 23:30

that you use to to solve them

## 23:34

i i don't so if you're if you're feeling nervous about saying no don't be because it it still

## 23:40

takes me some time so uh one thing that i've said in in classes like this and in uh in

## 23:47

the past i don't really care what your math ability is right if math if you want to say

## 23:52

to yourself math scares me to yourself that's fine i mean you probably shouldn't tell that

## 23:56

to other people uh but it's not you know i never thought

## 24:00

i i have never thought of myself as being good at math you know it's everything is relative

## 24:06

right you know so i've gotten by in life with whatever math capabilities i have but the the

## 24:14

further along i got the more i found that i could give myself a boost of confidence by using other

## 24:19

tools to either fill in the gaps or give me sanity checks or whatever for me those tools tend to be

## 24:24

computational right and so i'll try to incorporate a little bit of that too but i thought it would
be

## 24:30

good to

## 24:30

just to go through some of the the details so that we're all on the same page and along the way

## 24:36

you'll get at least a short glimpse of the way that i think about some of these problems uh and

## 24:43

then you know how to solve it and you can adopt them if if you want um that's uh up to you okay

## 24:49

so we'll start off with the the absolute simplest decay problem where we just have

## 24:54

a number of nuclei of some species i don't care what that is yet this is just you know the basic

## 25:00

math for it okay so we've got the the number of species with time we're given an initial condition

## 25:07

right this is an initial value problem it's ill specified if we don't have an initial condition

## 25:12

and if it's not given then you have to put it you have to assume some something that looks like this

## 25:18

okay the decay constant lambda uh anybody remember what unit that has

## 25:27

one over second so i highly recommend that anytime you do decay problems

## 25:33

that you do it in seconds okay so often half-lives which are of course related to lambda

## 25:40

are given in whatever the sort of natural unit would be if it's a few minutes and it'll be a few

## 25:45

minutes rather than a few minutes times 60 seconds right it's just easier to write out so does
anybody

## 25:52

remember what the relationship between lambda and the half-life is yep so we can either do

## 26:03

lambda is equal to ellen

## 26:05

two over t one half or flip it around right so if we're given the half-life we sub we put it into

## 26:11

this expression we get lambda so anytime i said unfortunately most of the data out there is for the

## 26:18

half-life so we're almost always going to be converting it into a decay constant for for

## 26:23

these sorts of computations um but why is that i think it's easier to understand the time

## 26:29

than it is in inverse time i mean it's just something that we work with more often okay so

## 26:35

this is a a special type of differential equation and i believe that the term is separable

## 26:43

right what i mean by separable is you can get one function on one side and the other

## 26:49

function if there is on the other side so that means i can say hey this is actually dn

## 26:54

over n and this is minus lambda dt now if i integrate this what do i get this on the left hand

## 27:05

there's a sp this ratio has a special name

## 27:13

well that's what i will get so if i if i then if i integrate this

## 27:17

right and i won't use units right now then i get the natural log of n this thing here

## 27:25

i believe is called the logarithmic uh derivative logarithmic derivative which makes sense because

## 27:32

then if you do the anti derivative which is an integral you get the log right so we get ln of n

## 27:38

of t is equal to minus lambda d t plus some sort of constant of integration right and then

## 27:50

how do i get the n of t all by itself yeah i exponentiate right so now i have n of t is equal to

## 28:04

e raised to the oh i should have sorry when i integrate this is t

## 28:12

and then plus c but this is also equal to e to the c e to the minus lambda t

## 28:22

and that's where we would solve or somehow introduce our initial condition

## 28:31

cool i think that's just about what you would expect for this sort of problem right

## 28:42

so that's that's simple decay this is the only place where this very simple

## 28:48

math trick will work the techniques that you use for other ones will also work for this this one

## 28:54

happens to be simple enough that that you can do it this way right so um i'm not sure how useful

## 29:01

remembering that something is separable will be unless you're in a math class or something like

## 29:05

that where you have those sort of problems i don't think it'll show up again here okay so that's

## 29:10

simple decay now decay with production is slightly more complicated right

## 29:17

if you

## 29:18

remember your math class i don't know which book actually you wouldn't have used a textbook it's

## 29:22

all that online the online notes for 340 is that correct right but even i think i looked at that

## 29:28

at one point in the nomenclature is for whatever reason certain classes across the world tend to

## 29:34

use some similar nomenclatures so you would have the unknown be y you would have a coefficient p

## 29:41

of t and then you would have a right hand side that's a q and then there's this integrating

## 29:46

factor mu or whatever it was called

## 29:48

and there's this boxed equation that you would plug and chug with for this sort of problem does

## 29:54

that ring a bell for anyone you know what the problem is for me i have a pretty bad memory for

## 30:00

stupid details right so i don't remember boxed equations very well i remember principles right

## 30:08

and so i remember what the purpose of an integrating factor tends to be

## 30:11

and so what i'm looking for in a problem like this is

## 30:16

some some function where i can do d d t of n of t and i know what that form is it's e to the

## 30:28

something right and in my case it's going to be e to the lambda t and i remember this this is this

## 30:35

is how i solve these sorts of initial value problems because i can never remember what that

## 30:40

sort of generic form the boxed equation is okay so think of this as an aside if i take

## 30:46

this time derivative of this product well by way of the product rule what do i get

## 30:50

i should get an n prime times the e i use prime here for derivative as a shorthand right times

## 31:00

lambda t plus n of t times lambda times e of lambda t does that look correct okay now if i

## 31:13

start to look at what comes out of this derivative i can actually see some pieces of my original

## 31:18

equation i've got the n prime that's my dndt i have the n of t times a lambda that's right here

## 31:24

and then i have this exponential term that's floating there it's like well what can i do well

## 31:29

i can take that same term and multiply the right hand side by it so what i can do is say that i

## 31:38

have dn dt times e lambda

## 31:43

you

## 31:43

lambda t plus n t lambda e lambda t and that has to be equal to r of t whatever my my rate of

## 31:55

production is times e to lambda t and then of course you can cancel out the e to the lambda t's

## 32:01

and you're back to your original equation which means that by introducing this e to the lambda t

## 32:06

i haven't changed anything but what i have done is i've let myself write all the stuff that has

## 32:12

to do with n of t

## 32:13

in this form which is nice because i don't care what's inside the parentheses i care that it's a

## 32:19

derivative and what i want to do with a differential equation to solve it is to get rid of
derivatives

## 32:25

that's why when we solve a differential equation we can it's synonymous to say that we integrate

## 32:32

the differential equation right yeah

## 32:34

uh nope i so i thought about that too when i was prepping my notes but i'm not going to do that

## 32:47

but because we move this so what i've done is i've said this is n prime plus lambda and equal r

## 32:55

right so if you put it in the form that would lead to the boxed expression from the math class

## 33:00

like this the lambda here is the p and so it's e to the you know p or integral of p with dt or

## 33:07

anyway this is i i believe this is right okay because if uh then we could yes definitely has

## 33:17

to be right because otherwise we would have a

## 33:18

negative sign over here and we wouldn't want that because it'd be positive on the right hand side

## 33:22

okay so we have this and so i can get rid of uh that and so now what i want to do is i want to

## 33:28

integrate this expression from some initial time to some other time i also hate having to remember

## 33:36

like what do i do for if if my initial condition is not at zero or whatever well just you know do

## 33:41

the integration from some initial time and go on uh with with the process so what i'm going to do

## 33:48

is integrate this expression from some initial time to some other time and go on uh with with the

## 33:48

process so what i'm going to do is integrate this the differential equation with the e to the

## 33:52

lambda t substituted and i'm going to integrate it from t naught to my actual time dt of n of t i'm

## 34:05

going to fix this in just a sec because we should be careful with our things okay what's the problem

## 34:13

with the way that i've written this what would your math instructor yell at you to do

## 34:20

if you have the independent variable in this case the t showing up both inside of the integral

## 34:27

and the integrand and in the bounds of the integral yeah somehow i mean like it would be

## 34:33

as written here it's actually i don't even know what what that would represent what kind of what

## 34:39

what do i have to do to the t that shows up inside of the integral to make it different from the t

## 34:44

that's in the integral bound i'll give you a hint it rhymes with mummy variable

## 34:52

dummy variable so i'll put a prime on it right so if it's inside the integral it shouldn't matter

## 34:58

what i call it but this is what i want to do to that left hand side stuff and now i'm going to

## 35:04

integrate the right hand side which would be t naught to t of r and i'll do it automatically

## 35:10

this time okay and so that's that's my my equation now and so i'll move all this stuff up a little

## 35:22

bit okay so

## 35:29

what's the integral of a derivative is that same thing yeah it's the same thing but where

## 35:40

the integrand is evaluated at the bounds of the integral right so what i would do here is say hey

## 35:46

i've got n of t prime e Lambda t prime all this stuff is evaluated at my initial time and then

## 35:59

whatever my final time is t right i've kept here the the primes to

## 36:03

be careful and then on the right hand side i have i'll keep this the same right t not t r of t prime

## 36:17

e of Lambda t prime and i forgot my dt okay and so once i have it in this form it's i can

## 36:29

actually evaluate it at those bounds so now i have n of t

## 36:35

Lambda t

## 36:38

minus n of t not E Lambda t not and then

## 36:47

I can't really do anything to this right hand side because I don't know what r of t is as

## 36:54

written in the original problem actually has written in the original problem that I keep yes so

## 37:01

it's just some arbitrary function of t right so this is about as far as I could

## 37:06

you without giving you a specific form for t now we'll find in other applications where that r will

## 37:13

be some function of t it won't be constant but as long as it's an easy sort of thing like another

## 37:17

exponential you can evaluate this integral right then it's just math you know kelp 2 type stuff so

## 37:24

no no problem i think okay so i'm gonna make a couple of assumptions here now to simplify

## 37:32

for some cases that are pretty common okay the first thing i'm going to do is i'm going to say

## 37:37

um so simplify i'm going to say that t naught is equal to zero right we're going to start from

## 37:46

you know all we care about is maybe like in a lapse time right and i'm also going to say that

## 37:51

r of t is equal to r naught right it's going to be constant once i make these assumptions

## 37:59

or i somehow i clarify my problem statement

## 38:02

so that i know i can do these things things get a lot easier because now i have n of t

## 38:10

let me put a little break here so now i have n of t e to the lambda t as i had before i have minus

## 38:18

n of zero e to the lambda t naught if t naught is zero will just be a one so i don't have anything

## 38:26

more to do there and if my r of t is now a constant i can pull it out

## 38:32

of the integral and now my integral from zero to t is just of the remaining bit of that integrand

## 38:41

the e to the lambda t prime d t prime and i can further work that out to be r naught times so

## 38:56

what's the integral of e to the lambda t

## 39:05

one over lambda yep

## 39:06

and so i have um let's see back that up

## 39:15

one over lambda e to the lambda t prime this whole thing evaluated at zero and t which means

## 39:26

that this is r not over lambda e to the lambda t so this would be e to the lambda t minus one okay

## 39:38

now let me

## 39:39

let me rearrange a little bit on this side if i what i'll do is i'll take the n not

## 39:48

and i'll well no i'll i'll leave it here okay now to isolate the n of t i'm gonna move the n

## 39:57

not over to the right hand side and then i'm gonna divide through by e to the lambda t that'll leave

## 40:01

me n of t all by itself and what i end up with is a slight change in this r naught term right
because

## 40:11

if i divide through by e to the lambda t i'm going to cancel this one out that's going to become a 1

## 40:16

and now i have e to the minus lambda t here i had moved over the initial value right it was

## 40:28

minus over here it's a plus over here but because i've divided by e to the lambda t this 2 has e to

## 40:34

the minus lambda t and that it's really hard to draw on a surface when you're not looking at your

## 40:46

pencil so part of my my nasty artwork here so that that's the the um the the final answer we've

## 40:55

got just about 10 minutes left any questions on that now i have no idea if the way that i

## 41:02

solve that or talk through my math is any different from what you you had learned in the past but um

## 41:08

the one thing that i didn't do is resort to some previously boxed equation now you can the box

## 41:15

equation that i'm going to show you is the only boxed equation that i have you can use for the

## 41:16

the boxed equation that i'm going to show you is the boxed equation that i'm going to use for the

## 41:16

I have here if you can take a mental snapshot of that you can go ahead and use it I've done that

## 41:21

in the past for for similar I mean this is a an attenuation expression where you have some

## 41:26

forcing function a positive forcing function it works here in decay it will also work when we

## 41:31

have things like neutrons going into a piece of material right and we want to understand how it's

## 41:37

being attenuated through material which we'll talk about next week and we'll have similar

## 41:41

expressions in that domain too okay but we'll return to this numerically in just a little bit

## 41:49

if we have the time to do so okay the last little bit that I want to do on with the sort of pen and

## 41:58

paper approach is this decay chain and really what I want to do here is just kind of write

## 42:04

down the equations and then we'll spend some time looking at the solution so as one of those

## 42:09

examples of fission products that

## 42:11

are beta emitters we have strontium 94 and I said something last time about that being one of the

## 42:16

main contributors to the heat generation of spent nuclear fuel it cesium 137 some of these other

## 42:23

things that have pretty relatively short half-lives we're talking you know tens of years right where

## 42:28

the heat load is present high specific activity meaning that for the mass that you have because

## 42:34

it's decaying so quickly the betas are so energetic you're generating a lot of heat okay so this is

## 42:39

one of the reactions that that

## 42:41

comes out of all of those beta emitters we have strontium 94 it beta decays over the course of 1.255

## 42:48

minutes on the average uh well not on the average it's the half-life but related to the average to

## 42:54

what is Y

## 42:56

yeah I I think I could spell it but anyway so you get yttrium 94 which two is a beta emitter

## 43:05

with a half-life of 18.7 minutes and this then decays to zirconium 94 which

## 43:11

is stable right so this is a a decay chain with two radioactive species and then a terminal stable

## 43:17

uh species so I started writing out the equations here so we're going to start off with a fixed

## 43:23

number of the strontium right maybe we just pulled a nuclear reactor out and we have the strontium

## 43:29

there and we want to compute what's going to be generated from that okay so uh we're going

## 43:33

to assume that this is our model rather than having a generation term we'll say that s n s r of zero

## 43:41

is equal to n not right so we're going to start off with some number of strontium okay so

## 43:48

what I need to do is write the balance for the yttrium right so d n y d t okay

## 43:58

like the strontium it has the decay term right so we have a term that's the nice thing about decay

## 44:07

chains there's so much symmetry in the structure it's it's fairly straightforward to write uh

## 44:13

now now that's this would describe the decay of the yttrium if I had no other uh considerations

## 44:20

right if I started with a fixed amount this would tell me how it evolves in time what am I missing

## 44:25

here the production right this is just my loss term right I start off with a certain number the

## 44:32

Lambda in plain English is the probability per unit time that I decay right so you start off with a

## 44:40

number times the probability that you decay per unit time gives you your loss rate okay same thing

## 44:46

can be said for the gain rate in this case it's going to be all the losses of the strontium will

## 44:50

turn up as source terms for the yttrium okay and then finally we have the zirconium

## 45:02

and because this has no decay the only thing it has is a source term and that'll be the positive

## 45:10

yttrium uh in decay we always see products of the form lambda times n and here is a is a number

## 45:22

right it's the number of nuclei of lambda is our decay constant or effectively probability per unit

## 45:28

time that we decay what is that product called generically speaking lambda times a number what

## 45:38

there's a special name for it the activity okay so in the book

## 45:49

you

## 45:50

there will be referencing to activity uh you know it's defined sort of implicitly in some

## 45:55

of the verbiage but inactivity is just the the actual absolute number of decays per second right

## 46:01

if this is my absolute number of nuclei and this is that decay constant their product is the

## 46:08

absolute right for the given sample of n nuclei a represents the number at that point in time that

## 46:13

i expect on average to be decaying right so typically radioactive sources are

## 46:19

quantum

## 46:20

altered more or less then are inactive by a more positive cantilever potential than the

## 46:24

äterpial

## 46:37

so that's what this is now what's going to happen here is that these decays are going to be decays

## 46:45

right and so here actually this is a function of the equation we just passed here so the expression

## 46:47

of the equation is this equation okay and the equation is the equation that is the equation

## 46:48

we just take and call it the equation of decay right the equation that is defined in terms of
activity

## 46:49

the r of t is going to be the solution to the d n s r d t equation right and then you'll evaluate

## 46:57

that integral that i had pointed out before and then once you're done with that you have some

## 47:01

explicit function and y of t right you have the number of the yttrium as a function of time

## 47:06

that makes this thing straightforward to to solve because that's just an integral right you have

## 47:13

d n z r d t is equal to something on the right hand side you just integrate both sides and you

## 47:19

get your result so i've done that for you in the sense that you have a solution in the notebook

## 47:27

right so some decay examples here's that decay with constant production uh just as some you know

## 47:35

numbers for fun i've set n not to one r not to one and lambda to one if you weren't there on

## 47:42

tuesday night you'll find

## 47:43

you'll find

## 47:43

you'll find

## 47:43

you'll find

## 47:43

you'll find

## 47:43

in code i will misspell lambda because lambda spelled properly is a python keyword right so

## 47:50

i can't use it so it's not because i'm dumb and i can't spell lambda i'm dumb for different reasons

## 47:55

okay all right i'm going to run that cell and what i'm doing is so decay constant is 0.1 i'm looking

## 48:03

at the evolution over 100 seconds and for this decay with production we see something that there's

## 48:11

some features to this that are pretty important right we start off with zero because i went very

## 48:16

close to zero because i had an initial value one hardly shows up on this and then as i go in time

## 48:21

i'm rapidly approaching some sort of asymptotic value do you remember what this asymptotic value

## 48:29

is called in the textbook starts with an s it's a certain kind of activity

## 48:39

saturation activity right so this is the saturation number of nuclei but if i took that

## 48:46

and multiply it by lambda i would have the activity that this thing approaches to right

## 48:51

basically what happens at this point in time is the number being produced is exactly offset by the

## 48:57

number uh being lost through decay right so in effect what happens to the derivative right as i

## 49:04

go up to that asymptote what is d and dt way out here zero so in effect we don't actually have to

## 49:13

solve the equation if all i care about is that saturation activity

## 49:16

i can take the original ode the ivp set that derivative to zero and then solve for what i

## 49:23

want in this case if i set the dndt to zero i bring the lambda n over here to the left hand side

## 49:29

well then my my asymptotic value for n is equal to r over lambda and my asymptotic activity would

## 49:37

be that thing times lambda which would just be r right so the number decaying per second must be

## 49:42

exactly the number being produced per second which is r in that case okay that's that's

## 49:46

what saturation activity means for our decay chain i've actually put all the numbers here so

## 49:53

you'll have all that i set up the functions representing the solution so that's the simple

## 49:58

one that's just the strict decay this is the somewhat ugly expression that you get when you

## 50:04

actually evaluate that integral where the source term is the strontium number in the yttrium

## 50:10

equation and this the actual solution is in the book too although uh that the work isn't done for

## 50:16

that and then here's the

## 50:18

even slightly uglier one for the zirconium and if i i should actually evaluate that cell okay

## 50:26

and so that's what this thing looks like so not not trivial functions right the the math to get

## 50:32

there is i would say reasonably straightforward but we start off with strontium of course it's

## 50:36

going down really quickly because it's half-life is only what a minute and chain right so i put

## 50:42

this in second so i'm going for an hour here and so that goes on very quickly and as it goes on

## 50:47

very quickly

## 50:48

the yttrium goes up pretty quickly but then as you lose the strontium forcing function it too starts

## 50:54

to decay down all the while the amount of zirconium is increasing now if i instead plot this on a
log

## 51:01

scale it seems to approach an asymptote and it it makes it easier to to give ourselves a sanity

## 51:10

check if i started off with one million strontium nuclei right and if the zirconium itself is not

## 51:16

radioactive meaning that

## 51:18

once i get it it stays what do i expect if i take t to infinity the number of zirconium to be

## 51:27

a million right everything that started as strontium has to pass through being yttrium

## 51:32

and then finally ends up the zirconium so that's a a really good sanity check for you to do

## 51:37

and then this is for those who showed up on on tuesday or watch the videos this is how i would

## 51:44

do it if i wanted to use numerical methods right so i set up the

## 51:48

tel Pike over here

## 51:50

to interpret

## 52:03

the look it goes through this male's word when i golf or when i'm purple

## 52:11

and i'll say t is indeed used

## 52:14

so power equal to three

## 52:16

three

## 52:17

and it's a looking difference in this process canceling and tracing the relation to表示 h about aし

## 52:17

answer numerically being a totally separate method i feel pretty good about those math abilities
that

## 52:23

i was talking about earlier so hopefully you can take these numerical tools use them at your

## 52:28

leisure to to check your analytic work and then hopefully be able to use them in practice uh later

## 52:34

in life so that is everything that i wanted to talk today again it'll take me some time to pack

## 52:39

up my stuff so if you have questions feel free to come up otherwise i will see you on monday so be

## 52:44

looking for the uh sort of lecture prep stuff um sometime later today
