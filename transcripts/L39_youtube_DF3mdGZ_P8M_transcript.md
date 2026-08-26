# L39 Local Audio Transcript

Course: NE 630

Playlist source: https://youtube.com/playlist?list=PLy481lNHlnHoEO95vM-xYX2bydD25v20L

Video: NE 630 - Lesson 39

URL: https://www.youtube.com/watch?v=DF3mdGZ_P8M

Video ID: DF3mdGZ_P8M

YouTube upload date: 20231201

Duration: 50:04

Transcript source: Local faster-whisper transcription from YouTube audio.

Whisper model: large-v3; detected language: en.

Generated: 2026-06-28

Note: This transcript is machine-generated from audio and lightly wrapped only. It should be reviewed before being quoted, published, or used as polished lesson text.

Requested language: en

## 00:00

for it on this computer all right so just a bit about where we are and what little bit we have

## 00:07

left so um we talked about the reflected reactor last time today we're going to talk a little bit

## 00:13

about reactor control specifically something called first order perturbation theory which

## 00:18

is a topic that could easily be covered in you know multiple lessons right it's actually kind of

## 00:25

uh i wouldn't call it super advanced but mathematically it would require us to sort

## 00:31

of deviate from from the um level of math that we've been doing if we wanted to really dive in

## 00:37

and uh sort of understand all the bits and pieces i'll talk a little bit about that as we go on

## 00:42

today next time on monday i'm hoping to have uh some numerical results that will help us

## 00:50

understand diffusion theory as uh in approximation right

## 00:55

we've been using it as sort of our way to just handle spatial effects it's not the only way to

## 01:01

do it in fact it is an approximation uh one would always say that when you write down math to model

## 01:06

the real world it's always an approximation when by definition modeling is to approximate what we

## 01:12

see around us so diffusion is a an approximation it's a pretty good one for a lot of the things

## 01:17

that we do but we'll see where it fails and what um maybe uh the the true solution looks like and

## 01:24

uh you all

## 01:25

also what i'll try to do is have a very specific example of two group um reflected reactor problems

## 01:32

because if you notice in the homework that's assigned for last time it says something about

## 01:39

showing the two group reflected flux you don't know what that looks like because i haven't showed

## 01:44

it to you it's not in the book because it requires a bit more math so don't worry about that that

## 01:48

part of it um you'll see that uh later on go ahead and take a guess i'm curious to see what

## 01:54

you think right

## 01:55

so do it don't worry about it being right i guess you know put something on there um and then i'll

## 02:01

show you uh what it would look like for some of the problems that we've been studying okay so uh

## 02:06

any questions for the homework that's due tonight i had a bunch of folks ask me about the geometry

## 02:12

and i'll make a clarification when in the problem statement i say we have our reactor from negative

## 02:18

a over two to a over two the same slab with a that we've been dealing with what language was

## 02:24

causing some kind of problem so i'll show you what it looks like and then i'll show you what it
looks like

## 02:25

so we can set it in a few slides so in terms of diagrams we can had some proof if we can get

## 02:27

some few clips hrysn so i'll show you one that's kind of like that in some ways is really important

## 02:32

to think about that let me just pause the slides代

## 02:36

this is an example because it already does the same it's still some kind of seem things

## 02:39

now but i'm not sure if we need to un MAScl to review that so you could probably scroll

## 02:43

to some

## 02:51

of different pieces but let me just pause and give you guys a bit more practice and I'll show you

## 02:54

if you're any subject life choice question here right and if not took it to say the same I'll see

## 02:55

this way it's just that you have less to write down if you assume the symmetry right because

## 02:59

then you only have the interface condition at a over 2 with the reflector and then a over 2 plus

## 03:09

t right so this is our reflector region this is our fuel region and the what all you need to do

## 03:16

is write down the equations for uh the interface condition and then the outer boundary because

## 03:22

reflection says that whatever our group structure is right here we're doing the two group we're

## 03:27

saying that the derivative of the flux goes to zero right that's the same thing as saying the

## 03:32

net current goes to zero meaning that there's no change across x equals zero which is what we would

## 03:37

expect if this thing were actually symmetric uh to a over 2 minus a over 2 and then minus a over

## 03:43

2 minus t so i could do that so that's you could certainly do the whole thing you would have an

## 03:51

additional set of

## 03:52

constants that the c1 c2 business but as we found several times ago if you assume that the flux here

## 04:01

is a combination of sines and cosines the sine term goes away right because we've chosen to

## 04:08

go from a over to minus a over 2 to a over 2 if we had instead done zero to a then all of our

## 04:14

business would be done using the sine as opposed to the cosine right so uh sometimes some decisions

## 04:20

that you make at this stage

## 04:22

will one it will impact the the final expressions you have but sometimes it will

## 04:26

make it a little bit simpler right so that's just something to keep up

## 04:30

um any other questions related to that homo yeah so with that our our flux is going to be non-zero

## 04:39

at the left like the side of the reflector but at the far side of the reflector it will be zero

## 04:44

right yeah so so the flux will have what actually the flux will be a peak right that that'll be its

## 04:51

largest value

## 04:52

and then over here i'm saying go ahead and use your zero flux condition just to make it simpler

## 04:58

right you can do it last time i showed you how you would set it up for the um zero incoming current

## 05:04

condition and it's just a kind of a nasty uh transcendental if you were to solve it right like

## 05:11

the purpose here isn't to solve you're writing down the equations right you are solving it then

## 05:16

in problem two when you apply the modified

## 05:22

one and a half group theory approximation which basically takes the two group approximation

## 05:26

and whittles it down to one group can somebody remind me what the primary assumption is

## 05:31

in going from two explicit diffusion equations to the single fast group equation what's there

## 05:41

there's an important approximation and you you know darn well that's something that i would

## 05:45

ask on the exam i like that sort of because it's simple it's a simple thing to ask and a simple

## 05:52

thing to answer if you if you caught it in

## 05:54

reading and appreciate it in the reading how did we go from two equations where we have an equation

## 06:07

for the thermal flux and the fat plus and bring that to just one equation it has to do with the

## 06:17

migration length right but the migration length in a way is combining the i mean it's literally

## 06:24

defined as uh as a function of the diffusion lines of each group right that's l one squared

## 06:33

plus l two squared to give you m squared right but that was that was how we get the modified

## 06:39

one and half group and that's just sort of hand waved in in the book right it gives us

## 06:44

a better approximation than just um going to one and half groups but there's an approximation that

## 06:50

like an actual assumption that is made before we get to that point

## 06:55

ignoring leakage in which which equation goes away thermal or fast

## 07:07

thermal right that said you're right it's we ignore thermal leakage and the reason for that is

## 07:13

there are two reasons for that one for the two group analysis that we've done with openmc and such

## 07:19

what was the ratio of the fast flux to the thermal flux josh do you remember like like

## 07:32

back in the envelope

## 07:33

sort of representative magnitude lindsay is it more than one or less than one

## 07:40

faster thermal ratio more than one yeah yeah right yes exactly yeah so you know

## 07:47

i remember i always made fun of myself because i i always just thought it was four

## 07:51

and it turns out no it's closer to eight or ten for a pwr it might be closer to four for

## 07:55

our highly thermalized reactor right so at one if you know that your your current has to be

## 08:03

proportional to your flux magnitude right like the bigger your flux is the big the bigger your

## 08:08

flux is the bigger your current could be okay so it all scales with what your magnitude is

## 08:13

so we already know that the fast flux is larger than the thermal flux now that doesn't necessarily

## 08:17

define the ratio of the gradients but in our case we know that the gradient would be then

## 08:22

multiplied by d if you look in the duderstadt and hamilton data that you have to use for this

## 08:28

problem you'll notice that the diffusion coefficient in the fast group tends to be about a factor of

## 08:32

three larger than the thermal group diffusion coefficient right that's a statement of

## 08:38

fast neutrons go farther than thermal neutrons right and that's just a statement saying that

## 08:43

the mean free path is larger for fast neutrons and that's something that we've talked about before

## 08:48

so in the end it would seem that thermal neutrons are going smaller distances and the flux is

## 08:57

smaller so those are two things that would lead us to think hey the leakage is probably smaller for

## 09:02

the thermal and if we just make that sort of let's just ignore it then you lose the derivative

## 09:09

term in the in the thermal uh equation and you have a direct link between the thermal flux and

## 09:15

fast right the derivative goes away so it's just now sigma a times phi two is equal to the

## 09:21

down scattered cross section times v one solve for v two in terms of v one plug that back into

## 09:28

the equation so that you're affecting the division term and voila you have

## 09:32

one diffusion equation okay what you're talking about with the migration length is rather than

## 09:38

just use the the original fast group equation which has its diffusion coefficient its removal

## 09:45

cross section and therefore it's l it's diffusion length you just plug in m instead of l

## 09:51

we don't have a mathematical justification for that right i'm i'm i did not have time

## 09:57

to like go through it and try to understand but my guess is that you can show it

## 10:02

in some sort of asymptotic way like rather than just saying that thermal leakage is zero

## 10:08

you could probably do some sort of expansion about thermal leakage being equal to zero right taylor

## 10:13

series blah blah blah i'm guessing that would lead to a more that would justify it mathematically

## 10:21

physically i think the book does a pretty good job of explaining that so cool any other questions

## 10:31

topics considerations

## 10:32

is it snowing

## 10:38

well you know maybe maybe that you know what that does that just pushes off leaf

## 10:43

dealing with leaves for another week so it'll probably be january or february before i feel

## 10:49

guilted by my neighbors into dealing with it and then the ans can have their fundraiser just like

## 10:54

just like they did last year right all right so why don't we go ahead and get started uh

## 11:00

yeah what's in the box

## 11:03

huh is that a voice

## 11:13

hello hello dr roberts

## 11:19

who is this what's in the box uh-huh interesting

## 11:35

oh interesting all right

## 11:44

uh

## 11:46

okay you're not gonna stay and

## 12:00

interesting all right well let's uh i don't know i i i not sure how to respond to that uh

## 12:06

all right so let's uh i want to review a little bit so last time we talked about

## 12:11

the reflected reactor and the very last thing we discussed was this idea of reflector savings and

## 12:16

uh we ended up with a final expression that's for biod Boot-ize when we more specifically wanted to

## 12:20

expression that um basically it gave us a way to interpret what the savings was i said in kind of

## 12:26

plain english the reflector savings represents the reduction in a critical width when you put a

## 12:35

reflector on the reactor right like for a given criticality like if you want k equal one a will

## 12:40

be smaller for our slab reactor than it would be without the reflector and that makes sense because

## 12:45

with the reflector we are reducing leakage so um for the bare reactor remember we have this

## 12:51

criticality condition right and we can solve that non-linearly if we want and we get a certain

## 12:58

buckling and then we get a k equal 1.25 in this case for for this particular data okay what we've

## 13:05

found then for the reflected reactor where we say that the reflector was infinitely thick it's a

## 13:14

much uglier

## 13:15

expressions if if we have a finite thickness right but we ended up with this now i put a prime

## 13:20

here i didn't have the prime there in the slides from last time but we ended up with with this

## 13:25

expression now what we can do with this expression is is sort of twofold the first thing we can do

## 13:31

is say hey for our unreflected reactor we got a buckling right the b squared term here we can

## 13:38

take that value b and plug it into this what that will give us is the critical width for

## 13:44

the

## 13:45

and by critical width it means we will get the same k or the same buckling we're choosing the

## 13:51

buckling if we choose the buckling remember there's a relationship between b and k and it's

## 13:57

just a function of the material properties right so if we know what b is or we know what k is that

## 14:03

we want we substitute that into the right hand side and what we get is the width of the reactor

## 14:09

that gives us that k value so if we take the bare value of b

## 14:15

substitute that into this expression where the diffusion coefficient for the reactor is d1 and

## 14:21

then the reflector properties are d2 and l what we get is is this a prime and if we put this into

## 14:30

if we actually use the numbers here okay that's our uh bare value um from above

## 14:40

and then if i want to see what a prime is it's 17.5356 centimeters so that's our bare value

## 14:46

that's a heck of a reduction remember our width for the slab reactor was 50 centimeters

## 14:54

we had a k of 1.25 and change but now if i put this infinitely thick reflector on either side

## 15:00

of the slab what i'm saying is to get the same k value of 1.25 i've shrunk my width down to 17

## 15:07

centimeters right from 50 that's huge now that reduction can be put into the reflector savings

## 15:15

terms but that's a huge reduction so if i put this infinitely thick reflector on either side of the

## 15:16

slab right because in the book there's this expression it was for the height of that uh

## 15:21

finite cylinder but it because we're putting a reflector on either side uh we reduce that the

## 15:28

we take the reduction in in the width and divide it by two right that's that i guess by convention

## 15:34

and so that reflector savings that we get is something like 16 um does that even make sense

## 15:44

yeah that's so 16.5

## 15:46

16.23 right so it's actually two times that that represents the total reduction but we're actually

## 15:51

reducing it uh on either side by 16 centimeters so that's pretty pretty substantial and then

## 15:57

there's also in the in the verbiage about the reflector savings this approximation

## 16:03

um based on the migration length of the mod of the reflector the diffusion coefficient of the

## 16:10

fuel and then the diffusion coefficient of the reflector now because i'm not using the one and

## 16:15

a half group equation or the one and a half group equation i'm just using the one and a half group

## 16:16

or the two group equation and we're just using the one group equation i don't have m but i do have

## 16:21

l right so the same thing in our one group terms would give us this value of the reflector savings

## 16:32

so it's an approximation it says in the book that it is an approximation how good an approximation

## 16:36

it depends on the problem here we're estimating about 10 centimeters instead of 16 centimeters so

## 16:42

right order of magnitude right it captures the fact that you're

## 16:45

critical width will be substantially smaller if you have the reflector on yourself okay any

## 16:57

questions about this when is the approximation valid uh so that's a good question um i would

## 17:08

expect it so it it would be i would expect it to be better a better approximation numerically

## 17:20

if the widths involved were large right so

## 17:24

50 centimeters that's not a really that's a pretty small reactor as it is like relative to

## 17:29

the mean free paths that we're talking about i think we'd have uh we'd see a better agreement

## 17:34

if we were you know several meters to begin with with and without reflector right because

## 17:41

uh the the impact of leakage on a larger reactor is already smaller right and so any approximation

## 17:49

to things related to leakage should also be

## 17:54

smaller and i bet they would converge but otherwise i'm not i'm not entirely sure right

## 17:59

my guess is that i get like we have an expression that gives us explicitly what the savings is in

## 18:05

terms of a and a prime right for a given buckling or a given item value um this thing would have to

## 18:12

come out of some sort of asymptotic expansion right think taylor series again like for some

## 18:17

small parameter um in this case that's probably a small leakage fraction i could be wrong good
question

## 18:24

um i would not expect you to to pull this out right i mean if i'm going to ask a question

## 18:29

about reflector savings i'm going to be looking for you to be doing some diffusion equation solution

## 18:35

right um yeah any other questions right go ahead and move on then to uh control right so

## 18:53

we've talked about control of the reactor before um in terms of reactivity right so we we have

## 19:01

things that impact reactivity like the buildup of fission products uh and so forth but in order

## 19:08

to keep the reactor critical right because a reactor almost always has excess reactivity and

## 19:14

well it has to right in practice right the only reactors that wouldn't would be maybe things that

## 19:19

are sub-critical systems right you can have sub-critical assemblies where you're putting

## 19:25

a source term in and you get the multiplication uh there are a number of those facilities out there

## 19:31

they're for experimentation and they're useful because if you're not a critical facility the

## 19:37

regulations are significantly easier to meet right critical reactors whether they're power or or not

## 19:44

or are there's more paperwork involved right uh so in order to keep our excess reactivity down in

## 19:52

like an operational sense we have to adjust the absorption cross-section in some way and so for

## 19:59

a pressurized water reactor like

## 20:01

the creek the the way to keep down excess reactivity is to dissolve boric acid in the

## 20:07

coolant right that's not possible for a BWR we talked a little bit about that earlier but BWR is

## 20:14

because they're boiling they have all sorts of stuff at the top of the core to deal with the

## 20:18

steam produced so there's no place for control rod mechanisms to sit and insert downward so they're

## 20:24

actually inserted from the bottom up uh and because of the boiling water we don't put in an

## 20:30

acid because

## 20:31

boiling water and acid together is a bad thing for most materials okay so how do we keep the things

## 20:38

set well we have the control elements but we also have a number of burnable poisons right so if you

## 20:45

imagine um in a fuel element right you've got your uo2 and so forth and that burns up right

## 20:51

you start to generate plutonium and so forth but you can imagine putting something else in

## 20:56

there that has a higher absorption cross-section than the uranium and the uh like I said uranium

## 21:01

235 and 238 and if you have something like boron 10 it will burn out faster than the uranium right

## 21:09

so like if you start off with a certain concentration its exponential decay in time

## 21:13

will be uh steeper than the uranium right so you can actually integrate these burnable poisons in

## 21:20

the fuel either kind of uniformly or there are cases where it's like a small layer on the outside

## 21:26

of the fuel pellets that's called uh ifba integrate

## 21:31

an integral fuel burnable absorber right where it's just like a thin several micron layer that

## 21:37

burns out quite quickly and if you think about it when do you need the reactivity reduction you need

## 21:43

it at the beginning of cycle right when you have the maximum excess reactivity and so when when you

## 21:48

do the if you were to look at the the reactivity of the function at a time and maybe this was in

## 21:55

the book or some one of the other resources if you if you have this bare u02

## 22:01

your excess reactivity will look something like this basically linear right which is the premise

## 22:08

of the linear reactivity model but if uh if we have some sort of burnable poison it would look

## 22:15

more like this right where in the very beginning we are burning out that strong absorber from the

## 22:24

surface of the fuel elements or maybe from you know within the fuel and then eventually it'll

## 22:29

match up with whatever the other curve would be of course you always do have some

## 22:33

cool boss right your number your neutron economy is is not as good as you didn't have it but you

## 22:38

do keep the reactivity check right and so you can imagine it's uh it's you know kind of an

## 22:44

interesting engineering problem to get the right amount so that you are getting back up to a higher

## 22:51

reactivity at the right point in time right it's a balance um and it's a much more difficult problem

## 22:56

for BWRs because not only you have burnable poisons but you have different types of poisons

## 23:02

different amounts

## 23:03

poison because BWRs are so much bigger you have all those control elements there's a lot more

## 23:08

spatial variation that goes on and in order to keep peaking at a minimum right so that you can

## 23:13

have uniform temperatures everywhere you have to play real uh the game is much more challenging

## 23:21

right to optimize these lattices or assemblies for BWRs because of this vertical poison right

## 23:27

so all that stuff is good and would be like actually to do that sort of design

## 23:32

um is what um I did in uh I taught at one time uh any 730 applied reactor Theory where we actually

## 23:42

used some um commercial tools uh from studs Vic and uh hopefully we'll be able to put that course

## 23:49

back into action I I have a meeting on Monday with somebody at Westinghouse they seem interested in

## 23:56

letting us use their tools their commercial tools like the same ones that they do for

## 24:00

um analyzing the

## 24:02

that they service. So we'll see if we can get that back on for those folks among you interested in

## 24:07

it, right? So that's sort of like what we would do in practice, but we can actually boil it down

## 24:13

to sort of a simpler change if we're talking about, you know, sort of the diffusion approximation

## 24:17

that we've been using. If we have a soluble poison, we're effectively talking about a uniform

## 24:23

change in sigma A, the absorption cross-section throughout the core. Now we could break, even

## 24:28

with diffusion theory, we could break up the core into regions that are fuel and regions that are

## 24:33

moderator, although we haven't done that yet. Like the most we've done is say, hey, we've got

## 24:37

the core region and outside of that we have a reflector, but the same principle could be used

## 24:42

to look at a single unit cell, right? And so the soluble poison would be really just affecting the

## 24:47

moderator, but in essence, we'll call that the uniform change, right? Something that's kind of

## 24:52

happening globally to the core. The other option, control rods, would represent some sort of

## 24:57

localized change, right?

## 24:58

So if we're talking about a typical PWR, these things come in from the top, right? So we're

## 25:03

talking like we could model this as an RZ geometry, and then as a function of Z, we would have some

## 25:11

increasing absorption, or if we're a BWR, it would be coming from the bottom, right? But local,

## 25:15

right? Some function of one of the independent variables, okay? But the idea is, given some

## 25:24

change in this, we want to know what the change in the reactivity is, right? So

## 25:28

usually we'll start off with a system that's critical. It's like I'm operating at, you know,

## 25:33

whatever my power is at K equal one. I want to know what my reactivity is going to be if I insert
the

## 25:39

control elements by, I don't know, 10 percent, okay? We know that if I insert control, K is going to
go

## 25:44

down, so my reactivity will be negative. And then if the reactivity is negative, there's a whole

## 25:49

bunch of other stuff that we can do, right? We know that if we are not at K equal one, we're no
longer

## 25:55

steady state, so we could go back to chapter six, chapter five material, and we could go back to

## 25:56

chapter six, chapter five material, and we could go back to chapter seven, and we could go back to

## 25:58

chapter eight, and we could go back to chapter nine, and we could go back to chapter 10, and we
could go back to

## 25:58

chapter 12, and do all of our kinetics, right? But we'd have to know what that change in reactivity

## 26:05

is, right? That was kind of one of the main assumptions in chapter five. We have to know what

## 26:11

our reactivity is in order to follow the transient after that step insertion, okay? So how do we
compute

## 26:19

this? Well, I don't know if you thought about this as you're reading the section for today, but
rather

## 26:28

than go through that derivation that the author gives, a much simpler, in theory, approach is just

## 26:35

solve the problem again, right? If we already have a critical system, I mean, we've solved the

## 26:40

eigenvalue problem, we got K equal one, we know what the buckling is, all that. If we want to know

## 26:45

how K changes, if we perturb the cross-section, well, why can't we just resolve the diffusion

## 26:51

equation? That's pretty easy to do if it's a uniform change, right? Because sigma A shows up

## 26:58

K infinity, and then it's fairly straightforward from that point. But if it's a localized change,

## 27:04

right? If we go from a barychord like this, if we get rid of the reflector, right? If I say, hey,

## 27:10

I'm going to insert control right here. Well, I've gone now from a homogeneous barychord to
something

## 27:16

that's heterogeneous. That starts to be a little bit more challenging, right? Because now I have

## 27:20

to break it up with new interface conditions and blah, blah, blah. So the point is, if we can

## 27:27

estimate the barychord, we can do that. And if we go from a barychord, we can do that. And if we

## 27:28

can estimate the change in reactivity in an easier way and have it be reasonably accurate,

## 27:34

then maybe we want to do that so that we don't have to solve the diffusion equation again. Because

## 27:39

I would be willing to guess if I asked who wants to solve the diffusion equation today for

## 27:44

good fun, very few of you would raise your hand. And that's fine because that's, you know, nobody

## 27:50

wants, well, I don't know, some, I want to sometimes, not every day, but some days. So

## 27:56

the second method is,

## 27:58

then let's use first order perturbation theory to estimate that delta rho. So what does first

## 28:04

order mean and what does perturbation mean? Well, the perturbation is the delta sigma a. That just

## 28:10

means we're changing something about the system. If we want to look at the math, it means that

## 28:14

we're changing something about the equation itself, some of the coefficient, for instance.

## 28:19

Okay. What does first order mean? Meaning first order derivatives in the equation.

## 28:32

So first, we've used that term,

## 28:35

first order, to describe differential equations. And first order in a differential equation means

## 28:39

that the derivative is a first derivative. In this case, there's a slightly different meaning.

## 28:50

What's that?

## 28:55

Yes.

## 28:58

Does it just mean that it's a really small perturbation?

## 29:02

Yes.

## 29:05

Those are on the right track.

## 29:07

The idea is, if we're, it's not stated explicitly here, but this is an approximation.

## 29:15

Right? So first order perturbation theory says that, hey, we're going to make a small change

## 29:19

to the system, in our case, delta sigma a. And if that's small enough, then the change to the flux,

## 29:26

if we were to do this direct resolving the diffusion equation, is also going to be small.

## 29:32

And the idea is, with this first order perturbation theory, the answer that we get,

## 29:37

will be equal to the true answer, to within some, some error margin.

## 29:43

And by first order, it says that we get it to within delta squared.

## 29:48

So the error in our approximation will be proportional to delta squared in all the terms that would
be perturbed.

## 29:55

So if we know that the flux would be something after the perturbation,

## 29:59

that'll be equal to the original flux plus some error term, right?

## 30:02

And what we're saying with first order perturbation theory is that the,

## 30:07

the error is, well, basically small.

## 30:10

So with, I guess, without showing more math, I can't, I don't want to talk too much more about that,

## 30:15

but it does mean that it's an approximation, but it's a pretty darn good one, right?

## 30:21

That's the, that's the main takeaway.

## 30:23

And it comes from some, some mathematical theory that I will only try to touch the surface of in
words, right?

## 30:30

You can look at the book for the case for diffusion theory, but it's actually a much broader topic.

## 30:36

Okay.

## 30:36

So that's,

## 30:37

that topic is first order perturbation theory.

## 30:39

And so the fundamental concept is we've got this change delta A.

## 30:45

Now, when we're computing something like reactivity,

## 30:47

if we know what the flux is and we know what the cross sections are,

## 30:51

the reactivity, or maybe the easier thing to compute is the, is the eigenvalue K.

## 30:57

If I know what K, if I know what the fluxes are, and I know what the cross sections are,

## 31:07

actually, this is not a bad exam question in concept,

## 31:11

right?

## 31:11

Because I think this is something that you can all do.

## 31:13

If I know for my slab reactor, what B is, right?

## 31:17

B, we'll say that it's the slab reactor, right?

## 31:21

The, without the reflector, if I know what B is, and I know what sigma A is, and because everything
we've done has been a constant sigma, right?

## 31:30

If I know what sigma A is, and I know what a new sigma F is, and I know what B is,

## 31:40

could somebody tell me?

## 31:41

What A is?

## 31:47

Like, if I, like here, I'm not actually writing down the form, but I could say that this is, you
know, equal to, you know, cosine of, of, uh, BX, right?

## 31:57

So I guess in this case, I also know what B is, so that, that B would be given as well.

## 32:02

So if I actually gave you an explicit mathematical function for a feet between minus A over two and
A over two, I gave you the solution that I could use.

## 32:14

Here is theСТing equation.

## 32:17

What is K?

## 32:24

Go back to the first principles.

## 32:26

What is K?

## 32:27

What are the first definition we have for K?

## 32:29

Gains over losses, right?

## 32:32

So we do have to write that down.

## 32:34

Gains over losses.

## 32:36

Right?

## 32:37

Now, what are my gains?

## 32:45

You know what the flux is, you know what the cross-section is as well.

## 32:49

What are the gains?

## 32:51

What's for the B prime?

## 32:53

What's for the-

## 32:53

Hy bleu?

## 32:54

Yeah, so I'm looking for the total number of fissions generated per second, right?

## 33:00

I don't want per centimeter.

## 33:02

I don't want per centimeter cubed.

## 33:03

I want per second, right?

## 33:05

So that means that gains should be equal to the integral.

## 33:11

If we're going to stick with that model, we'll be from minus a over 2 to a over 2 of nu sigma f time
phi of x d x.

## 33:24

Boom, right?

## 33:26

Same thing that we've talked about from almost day one, right?

## 33:29

We're looking for a reaction.

## 33:32

What about the losses?

## 33:39

What would the losses be?

## 33:40

I mean, you can use the gains as an example for at least part of it, yeah?

## 33:57

Yeah, so at least part of the losses would be the same integral, negative a over 2 to a over 2 of
sigma a times phi of x d x.

## 34:09

But that's not the whole story.

## 34:10

That's not the whole story about losses, right?

## 34:12

Yeah, and so we have plus leakage.

## 34:17

Now, the question is, how do we compute leakage?

## 34:20

We have vacuum on either side of this reflector.

## 34:30

Then the net current at either side will be the total number of beams, right, with the assumption
that we don't have anything coming in.

## 34:38

That's where using the flux codes, the zero condition makes that a little wonky, right?

## 34:42

Because that actually turns out that you have particles coming in.

## 34:44

Particles coming in, which is why I don't like that condition.

## 34:46

But with leakage, if I gave you this, then j is equal to minus d, which we also have times b prime
at x.

## 34:58

So you can evaluate this thing at x equal minus a over 2 and at a over 2.

## 35:04

Add those results together, and that is your lead.

## 35:08

So you have everything that you need to get k if you have the form for the flux.

## 35:14

Maybe we can think of that as like the reverse process, right?

## 35:22

Usually it's like, here's the diffusion equation.

## 35:24

Figure out what b is so that you can get k, right?

## 35:28

But at the same time, if you get b, well, then you get the flux, right?

## 35:32

So it better all work out so that we have balance.

## 35:35

Where was I going with this?

## 35:39

This represents the way that we would do the direct perturbation, right?

## 35:43

So I could say, hey, I have the flux.

## 35:46

I could take that flux.

## 35:48

Now, if I want, I could put in a sigma, a delta sigma a.

## 35:53

What that will do is give me the effect, the change in the loss, right?

## 35:59

If I just put in this new cross section to this integral of absorption, that will get me a change in
the losses.

## 36:06

But what that doesn't account for is the fact that if I change sigma a, well, then my buckling would
change, right?

## 36:14

Because if I change sigma a, then k would change.

## 36:16

k infinity changes.

## 36:18

And I would have this propagation of errors that isn't accounted for.

## 36:21

I'll have a pretty big error, and that error will be proportional to delta sigma a.

## 36:26

So I don't want to do it that way, right?

## 36:28

If I want to do a direct perturbation, what I mean is set sigma a to be the new value with the
perturbation added to it, and then re-solve the whole problem.

## 36:37

I'll get a new buckling.

## 36:39

If I get a new buckling, then I get a new cosine term.

## 36:42

If I have a new cosine term, then I have a new leakage term.

## 36:44

So I make a change to sigma a.

## 36:45

It propagates to everything else, right?

## 36:49

So that's why basically I have to re-solve if I want to do direct perturbation.

## 36:55

But if I use first-order perturbation theory, what I'm looking for is, can I do something where I
can just insert it into the equation like this and get an answer that isn't proportional to this
delta?

## 37:05

I want it to be proportional to delta squared, right?

## 37:08

And if delta is small, then delta squared should be even smaller.

## 37:11

That's the point here.

## 37:13

Okay.

## 37:14

So that's what we're after.

## 37:15

But it helps, I think, to kind of go back to the basics and understand k in terms of gains to
losses.

## 37:22

So the point here is if I were to make this perturbation sigma a and put it right in, I'm capturing
just that absorption chain.

## 37:33

But what I'm saying about first-order perturbation theory, kind of like the foundation of it, is not
just to put delta sigma a into your original loss.

## 37:42

But you need to weight it in some way.

## 37:48

You need to weight it by something called the importance function.

## 37:51

Right?

## 37:52

We know that if we have a reactor from negative a over 2 to a over 2, the flux is greatest in the
center.

## 37:59

Right?

## 38:00

And that's, I mean, in a sense, that's a statement of saying that if I'm a neutron born from vision,
I have a greater chance of causing more vision if I'm born at the center of the core than at the
periphery of the core.

## 38:10

Right?

## 38:11

Because if I'm born on the outside, then the chance that I leave the building to the leakage is
increased.

## 38:18

So I'm less important.

## 38:20

Right?

## 38:21

If I'm a fringe neutron.

## 38:23

Terrible saying that about fringe neutrons.

## 38:25

But they're not as important.

## 38:27

They won't lead to as much vision.

## 38:29

So a good way to understand the neutron importance is to say, hey, where in the system am I likely
to generate more fissions?

## 38:39

And then if I wanted to count every single neutron that is produced after I start the fission
process.

## 38:45

Right?

## 38:46

So if I have a neutron dropped at the center of the core, it will produce some new fissions, two or
three.

## 38:50

If it makes a fission.

## 38:51

I mean, it could still be absorbed.

## 38:53

But it will make some number of new fissions.

## 38:55

And then those will go on to make new fissions until maybe they all die out.

## 38:59

Right?

## 39:00

You can count those.

## 39:02

And then, you know, weight it in some way.

## 39:04

But the more neutrons a given neutron will lead to.

## 39:07

It is basically a statement of its importance.

## 39:13

And just heuristically, the center of the core is more important than the outside of the core.

## 39:20

Okay?

## 39:21

So if we're going to weight this change delta sigma A, we want to do it in a way that captures the
fact that things are more important in the center of the core.

## 39:30

Okay?

## 39:31

So that's kind of the idea.

## 39:33

And the importance is representative.

## 39:36

Is represented by a function called the adjoint.

## 39:40

Now if we're talking about one group diffusion theory, this adjoint is called the adjoint flux.

## 39:46

And in most textbooks it would be given a symbol like B star.

## 39:50

Right?

## 39:51

It might be a little different from book to book.

## 39:53

But usually they'll point out something that looks like the flux but with something that says, hey,
this is not quite the flux.

## 39:58

Okay?

## 39:59

So the importance is represented by this thing called the adjoint flux.

## 40:02

And the result.

## 40:09

For.

## 40:10

Our delta row.

## 40:15

Looks like this.

## 40:16

Now this equation is very similar to the one in the book.

## 40:19

Right?

## 40:20

But I'm going to point out a couple differences.

## 40:22

I'm doing it here specifically for the case of our slab problem.

## 40:26

And I'm using X sub L and X sub R for the left boundary and the right boundary.

## 40:30

So I'm integrating over all of that.

## 40:32

Now if you notice here, this P star shows up along with our P.

## 40:37

So this delta sigma A times C.

## 40:39

That's the same absorption that we would get.

## 40:41

Just sort of simple expressions for gains and losses.

## 40:44

That would be the perturbation and the losses.

## 40:47

But now, rather than just integrating delta sigma A times B, I'm weighting it by this thing.

## 40:53

B star.

## 40:54

Right?

## 40:55

And I've also included here what you would do to have the perturbation in sigma F.

## 41:00

Right?

## 41:01

Your vision term.

## 41:02

So that shows up divided by whatever your initial eigenvalue is.

## 41:05

Usually K is 1.

## 41:06

Usually you care about how far am I going to go away from critical if I make this change.

## 41:10

And then everything is divided by the vision rate.

## 41:14

But again, it's weighted by this thing called B star.

## 41:18

Right?

## 41:19

So this is basically equivalent to the expression that you would have in the book.

## 41:24

Now it turns out that one group diffusion theory, which is what we're using here, is a self-adjoint
equation or the operator.

## 41:34

Like the things working on B represents a self-adjoint operator.

## 41:39

Or for math, it's called Hermitian.

## 41:43

I don't know.

## 41:44

Have you ever heard that term?

## 41:46

Yeah.

## 41:47

In quantum.

## 41:48

Right?

## 41:49

So it's a self-adjoint Hermitian.

## 41:50

If you want to talk about matrices, you can say the same thing.

## 41:54

A matrix is Hermitian if it's equal to its transpose.

## 41:58

Complex transpose if it has complex numbers.

## 42:01

Basically, there's a whole lot of cool math that you can do when you deal with self-adjoint things.

## 42:07

For one group diffusion.

## 42:08

Right?

## 42:09

We get it.

## 42:10

And it turns out because of that, P star is actually just equal to P itself.

## 42:15

Which is why when you go to the book and the equation that looks a lot like this, you see P squared.

## 42:21

Right?

## 42:22

That's because it's one group.

## 42:25

Now, if we were doing two groups, it would not look like that.

## 42:29

Because the two group equations are not self-adjoint.

## 42:31

They're pretty nearly self-adjoint.

## 42:33

But things would look a lot different.

## 42:35

Think of it this way physically.

## 42:37

If we have two groups.

## 42:39

Consider our bare reactor.

## 42:41

Always the outside of the core is less important than the inside of the core.

## 42:47

That, I think, just makes some good sense.

## 42:50

But now the importance of a fast neutron being on the outside of the core versus a thermal neutron
being on the outside of the core.

## 42:57

That ratio will be different.

## 42:59

Right?

## 43:00

Because fast neutrons tend to go farther.

## 43:02

Right?

## 43:03

If you add in reflectors now.

## 43:05

Where you have a water blanket on the outside of the core.

## 43:08

Things look even different.

## 43:10

Right?

## 43:11

Because if I put a fast neutron in the water, there's a pretty good chance that it slows down and
reenters the core to cause fission.

## 43:18

Right?

## 43:19

That's the whole point of having the water there.

## 43:21

So its importance is going to be higher.

## 43:23

But if I put a thermal neutron into the reflector on the outside of the core, well, how much, how
likely is it for a thermal neutron to go back in?

## 43:31

A lot less.

## 43:32

Because its mean free path is so much smaller.

## 43:35

So that means that the adjoint for a fast.

## 43:37

Neutron is going to be larger in the reflector than it would be for the thermal neutron.

## 43:42

Right?

## 43:43

So all this stuff, like to work this out mathematically is beyond what this course is.

## 43:48

But there's actually a whole, I don't know, you could call it a whole section in an advanced reactor
course where we could talk about this stuff.

## 43:55

And it makes it a whole lot easier if we had access to like a numerical diffusion solver.

## 44:01

Right?

## 44:02

Where we could actually see some of this stuff.

## 44:03

I'll bring some of these results in next time.

## 44:05

But this is basically the takeaway.

## 44:06

The takeaway that I want you to have.

## 44:09

Because if you substitute phi star equal phi, then you get the same equation that's in the book.

## 44:15

Does somebody have the book in which equation?

## 44:19

Do I actually say it's 70, right?

## 44:25

It's just the integral over the change in sigma A over the weighted diffusion rate.

## 44:31

Okay.

## 44:33

But now you get it for that.

## 44:35

You get the deviation in new sigma F.

## 44:39

Okay?

## 44:40

So my claim here is that the change in rho, the reactivity that we get from this expression, is a
better estimate than if we took the same delta sigma A and plugged it sort of naively into our gains
and losses equation.

## 44:54

Right?

## 44:55

We could do that.

## 44:56

This would give us the right direction.

## 44:58

Right?

## 44:59

Obviously, if we increase sigma A, the absorption loss will go up.

## 45:03

Our k will go down.

## 45:04

Our reactivity will go down.

## 45:06

If we do the same here, it will also go down.

## 45:10

But the amount by which it goes down will be closer to if we resolve the whole equation.

## 45:15

Right?

## 45:16

Which is what we're trying to avoid.

## 45:18

So first-order perturbation theory is it doesn't really require a whole lot of extra work because
we're still computing an integral.

## 45:27

Right?

## 45:28

We have two integrals.

## 45:29

One for gains, one for losses.

## 45:30

We have it here for gains and for losses.

## 45:32

The only thing that we're going to do is we're going to go down.

## 45:33

The only thing that's different is the fact that we're being a little bit smarter and we're
weighting those changes by the appropriate adjoint, which for one-group diffusion is the flux
itself.

## 45:44

So the difference between this and that is zero if delta sigma A, our change in the Dorton cross-
section, is uniform.

## 45:53

Right?

## 45:54

Because if it's a uniform change, then the weighting doesn't change anything.

## 45:57

Right?

## 45:58

If we go from sigma A equal 0.1 inverse centimeters to 0.11 inverse centimeters.

## 46:02

Everywhere.

## 46:03

Then it will pull out from everything we can.

## 46:05

We don't need the adjoint in the first place.

## 46:08

But if sigma A depends on space, as it is written here.

## 46:14

Right?

## 46:15

Going back to this model.

## 46:17

If I'm just changing sigma A in the center 50% of the core, for instance, which might represent a
finite control element being driven into the core, then the weighting matters.

## 46:30

Right?

## 46:31

And the fact that in the center of the core, the change will be larger than if I were making it on
the outside of the core.

## 46:37

Yeah.

## 46:38

So you said that this, primarily, the local changes in control, which is going to be related to
control rods versus some type of a poison that's put into the coolant.

## 46:52

Is that relevant for any type of control rod insertion?

## 46:56

Or is that going to be for one or two control rods?

## 47:00

Or is it one bank that's inserted?

## 47:02

That's a good question.

## 47:04

This is applicable when the change to the cross section is relatively small.

## 47:10

Obviously, this is not a good way to do business if you're going from a critical state with no
control rods in to a subcritical state with all control rods all the way in.

## 47:21

Those two systems are very, very different.

## 47:24

And I would say that the delta sigma A then becomes large enough where delta sigma A squared.

## 47:29

Is also very large.

## 47:31

Right?

## 47:32

And then, basically, you would still have big errors.

## 47:35

And something like that where you're going from completely withdrawn to completely inserted for
control rods, you're most likely needing to rerun the model.

## 47:44

Right?

## 47:45

You know, resolve the diffusion equation or rerun your MCMP calculation or something like that.

## 47:49

Okay.

## 47:50

But, yeah.

## 47:51

So what would, like, could you know beforehand if the perturbation is too large for this
perturbation estimate to work?

## 47:58

Yeah.

## 47:59

That's something that you would probably develop a sense for if you were doing this, like, in sort
of routine engineering analysis.

## 48:06

Right?

## 48:07

But, yeah.

## 48:08

Good question.

## 48:10

So one point that I would say here is be careful if you're doing it over other coordinate systems.

## 48:17

Right?

## 48:18

If we're doing full 3D, these integrals, because we're integrating reaction rates.

## 48:22

Remember, what I'm looking for is absorption per second, neutrons leaking per second, fission
neutrons produced per second.

## 48:28

Not per volume.

## 48:30

These are actually integrals over volume.

## 48:32

It's just when we're dealing with slabs, it's over one dimension.

## 48:35

So be careful with the coordinate system.

## 48:38

The homework for this lesson, I have you revisiting our infinite cylinder.

## 48:43

Right?

## 48:44

So it's Bessel functions.

## 48:45

You have to be careful.

## 48:46

If you're integrating over the radius, it's not really one dimension.

## 48:51

You're integrating over the volume.

## 48:53

Which means that you have to have the appropriate differential volume in your integration.

## 48:57

Right?

## 48:58

Remember, the volume for our cylinder will go as R squared.

## 49:04

So it will be an integral over R.

## 49:06

But don't forget your 2 pi.

## 49:08

That makes sense.

## 49:09

Right?

## 49:10

Because you're integrating over the circle as opposed to just along the R.

## 49:14

Right?

## 49:15

I put a note in that, I think, in the homework statement.

## 49:18

But just be mindful of that.

## 49:21

Right?

## 49:22

It's really over the volumes.

## 49:24

So I don't have time to go through this.

## 49:26

But what I'll do is I'll head back to the office.

## 49:28

And I'll do this.

## 49:30

It will be a very simple numerical thing for our bare slab.

## 49:33

So I'll have those numbers inserted into the slides.

## 49:36

And we can revisit that next time.

## 49:38

But you'll have it available as potentially to help as you wrap up the homework for this lesson.

## 49:45

So I guess that is it.

## 49:48

Feel free to ask some questions as I wrap up.

## 49:51

But otherwise, have a good weekend.

## 49:53

And stay safe out there.

## 49:55

And the frozen tundra.
