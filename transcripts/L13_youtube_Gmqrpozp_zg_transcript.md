# L13 Local Audio Transcript

Course: NE 630

Playlist source: https://youtube.com/playlist?list=PLy481lNHlnHoEO95vM-xYX2bydD25v20L

Video: NE 630 - Lesson 13

URL: https://www.youtube.com/watch?v=Gmqrpozp_zg

Video ID: Gmqrpozp_zg

YouTube upload date: 20230920

Duration: 52:17

Transcript source: Local faster-whisper transcription from YouTube audio.

Whisper model: large-v3; detected language: en.

Generated: 2026-06-28

Note: This transcript is machine-generated from audio and lightly wrapped only. It should be reviewed before being quoted, published, or used as polished lesson text.

Requested language: en

## 00:15

All right, so again, thanks for dealing with the sort of glitchy online thing that I did

## 00:37

the past couple times.

## 00:38

There will be one more occasion this term where I have to do that, and that'll be in

## 00:43

about a month or so, just sort of mid-October, so hopefully it'll be smoother the second

## 00:51

time around.

## 00:52

So all right, let me get to the notes here.

## 01:02

So last time we talked about effective cross-sections and the relationship of those cross-sections

## 01:10

to k-infinity, sort of the multiplication factor for these infinite medium systems.

## 01:15

That we care about.

## 01:17

And the reason that we care about these effective cross-sections is not so much in the form

## 01:23

that we talked about last time, but when we get to something called the multi-group method,

## 01:27

which is the topic of today and Friday, specifically today, we'll talk mostly about the two group

## 01:32

equations because they're, well, at the end of the day, they turn into systems of equations.

## 01:39

They're matrices.

## 01:40

And who wants to deal with a hundred by hundred matrix by hand?

## 01:44

I don't.

## 01:45

Two by two is fine.

## 01:47

So we use two groups, right?

## 01:49

We could do three groups, we could do four groups or whatever, but things are a little

## 01:53

bit easier with two groups.

## 01:55

And for thermal spectrum reactors, it's pretty sufficient to explore some of the major physics.

## 02:01

We've got fast neutrons and we've got thermal neutrons.

## 02:04

We lump those epithermal or the intermediate neutrons into the fast group.

## 02:08

So it's like thermal and non-thermal.

## 02:10

And there's a lot that we can do with just those two, those designations for each.

## 02:15

So it's trade-off for neutrons.

## 02:16

So any questions from what we've talked about the past several times?

## 02:24

How did the homework go or how is it going?

## 02:31

So, yeah, for this material, I understand that there's more that's not from the book

## 02:37

than there had been in some of the previous ones, right?

## 02:40

Because I think it's important to incorporate a little bit of the computational stuff in

## 02:47

general,

## 02:48

Sure.

## 02:49

Okay.

## 02:49

You cannot do a lot of reactor analysis with pen and paper alone.

## 02:53

I think being able to leverage some of these tools is important.

## 02:57

And as we go along, I will continue to incorporate stuff from outside of the book that is aligned
with the book.

## 03:05

And we'll be doing that a little bit today and then Friday, depending on if I can get things set up.

## 03:12

I'm hoping to deploy some examples using OpenMC, which is an open source Monte Carlo tool developed
at Argonne National Lab.

## 03:20

So for those of you who have heard of or used FITS before with Dr. Baddori, OpenMC is like that.

## 03:28

It's a Monte Carlo code. It uses some of this underlying nuclear data.

## 03:32

It's just it's free open source. And if I can get it deployed on Google Colab in an easy, sane way,
I'll do that.

## 03:39

And I'm also going to explore trying to set up.

## 03:42

A server will do it all through Jupyter Notebooks, right, which is something that you're at least
all visually familiar with.

## 03:48

If you haven't anybody not tried to run a Jupyter Notebook yet.

## 03:53

One one caveat to that, we we all, I think, have been using the Jupyter Notebook, but where we don't
not all of us have the nuclear data like installed locally.

## 04:04

Yes. And so, like, whenever you do try to run it, of course, it throws errors because we don't have.

## 04:08

Yes. So the past couple of ones, I.

## 04:10

Basically, to save myself time, I had written a helper function that just all the data that I'm
using, you have on campus.

## 04:19

Now I put that under the administrator view. You just got it.

## 04:21

Yeah, so that that's it's my fault. And it's mostly to save myself time.

## 04:28

I was hoping if you use some of the code that you just use the let's say the the various commands
right along with the data.

## 04:36

So for everything that you've had to do, I think you're only dealing with like.

## 04:40

Uranium 238. So you shouldn't need all the other things, but that might be different for the present
homework with the mixture of other things.

## 04:47

So, yeah, if there are computational issues, like if you feel like there's a gap between what I'm
asking and what I had given, right, just talk to me, I'll bridge that gap.

## 04:57

That's not a problem if it takes a little video tutorial or meeting on one of the nights over either
here in the computer lab.

## 05:07

Not that I want you to have to spend more time.

## 05:10

With me, I don't mind that, but you might mind that.

## 05:13

But I'm willing to do that.

## 05:15

So there are there likely are gaps, right, because I know how to do some of this stuff.

## 05:21

And I sometimes forget that maybe you haven't had certain pieces of preparation along the way.

## 05:27

So all you need to do is ask.

## 05:29

And I can't read minds very well anyway.

## 05:31

One other question we have with that.

## 05:34

There's a narrow resonance approximation problem on there.

## 05:38

Is that the example that we work through?

## 05:39

In class using the Jupyter notebook from I think it's lecture eight.

## 05:45

Can you remind me what the statement is?

## 05:46

Yeah, it says use in our approximation to approximate the flux spectrum for a thousand one mixture
of H2, H2.

## 05:56

Yes, that is almost like that could be copy and paste for my Jupyter if you were able to run it or
like if you get if you get it set up to run it.

## 06:05

So I think everything runs like the first time you open it.

## 06:08

But then like the moment you try to change.

## 06:09

Anything like I get it pulls up and it's like ran and finished state.

## 06:14

But then the moment you try to change anything, then that's when there is an error.

## 06:17

Yeah. So I've been uploading them in in the executed state so that what that does is it takes all
the images that it produces any of the outgoing equations, whatever.

## 06:27

So it's basically what you saw in class is what I'm uploading to rerun it, though, requires that you
have some of those other things.

## 06:34

And I can try to I can certainly upload.

## 06:39

The little Python helper file that I had, all that was doing was the loading in the cross sections
and then using interpolation to put them on one one energy grid.

## 06:51

Right. So hopefully what I'm doing in the code is kind of obvious, maybe how to do it right on your
own.

## 06:59

It may not be. But yeah, so anything that you need, just let me know.

## 07:03

I don't want the computational thing to. Computation should not be a burden. The whole.

## 07:09

Point of it is to release the burden, remove the burden from our own shoulders and put it on the
computer.

## 07:13

Right. So keep that in mind. If I'm failing at that or somehow missing the mark, just let me know.

## 07:20

OK. Yeah. So.

## 07:24

Yeah, so Friday, hopefully we can get things working so that you can at least tinker with Open MC.

## 07:30

I'm not going to require you to do a whole lot of stuff with it unless I have evidence that people
have zero issue running it right.

## 07:37

If we can actually use it sort of.

## 07:39

As a class, then I think there's a lot of pretty cool stuff that we can do with it.

## 07:45

And so I'll I'll wait till Friday to to show some of the examples.

## 07:49

But I think even a lot of the stuff that we've done so far, if we all had access to using Open MC
would be easier getting the data right.

## 07:59

All of their data is just in one big lump of files. Right.

## 08:03

So you wouldn't have to go to NNDC. The challenge is when I tried to introduce Open MC last year in
this class,

## 08:09

I had seven of you. Now I have 22 of you. And it was pretty challenging last year with only seven.

## 08:16

Right. I had everybody bring their laptops, install Linux for Windows.

## 08:20

They didn't have Mac. And it's like that takes us pretty far away from from the core mission of
reactor theory.

## 08:27

So I opted to step back a little bit and focus more on what what we've been doing.

## 08:36

All right. So all that said, then.

## 08:39

Other admin points. So next week, Friday, we'll have the exam right first exam, which will cover
everything through basically today.

## 08:48

So Friday, think of that is that there will be a little bit of stuff that builds on what we're doing
here.

## 08:53

But it's not going to like we'll get through the main theory stuff today.

## 08:57

So focus on through today for that exam. Right.

## 09:01

And I will get all of the homeworks up to date by the end of this week.

## 09:07

Solutions at least one of the solutions.

## 09:09

Has been posted for one of the more recent homeworks, and I'll get that up to get through six
ratings.

## 09:15

So I guess also think about admin stuff and being available for you.

## 09:20

I've always had office hours just by appointment. And really, I do that because if I in the past,
I've had office hours.

## 09:28

The only class that I ever had office hours that were routinely used was me four hundred.

## 09:33

And I suppose that might make sense given the nature of that court.

## 09:36

But for classes like this, I've never had.

## 09:39

One as completed to this point.

## 09:39

I can say for myself, I'm never switch тру в This hasn't fallen below 15 attendance, so I am totally
available if you need to ask me something or whatever.

## 10:05

So I know you working groups, literally.

## 10:07

So if you have questions, like you were just talking about, feel free to set up a time so that we
can dive into more detailed solutions.

## 10:08

All right.

## 10:08

All right, so to kick things off.

## 10:09

Think back over the past week or two.

## 10:10

We've talked about Ohio.

## 10:11

Instead, I don't have meetings.

## 10:11

I would say, hey, New Normal.

## 10:11

about the neutron spectrum, the flux spectrum, right? And we've tackled that by breaking it into

## 10:17

three regions that was sort of influenced by the physics, right? You have these fast neutrons born

## 10:22

from fission. There's not a whole lot going on at those fast energies, especially for thermal

## 10:27

spectrum reactors. Then those neutrons pass below the fission energies where chi, the fission

## 10:34

spectrum sort of tapers off and the neutrons enter the slowing down region where primarily elastic

## 10:40

scattering with light matter, low mass nuclei is bringing them lower and lower in energy, right?

## 10:46

And we end up with this effectively one over E, although we can get some detailed structure with

## 10:51

that narrow resonance approximation. And then we get down to the, you know, say single EV level,

## 10:56

and then things get a little weird because we have neutrons that start to gain energy

## 11:00

because of the thermal agitation of the target nuclei, right? But that sort of gives us the

## 11:08

framework for understanding the multi-group method.

## 11:10

We can break up this energy domain into different regions and then do something to enforce neutron

## 11:19

balance in each one of those energy bins. And these bins are what we're going to call groups.

## 11:24

I don't know exactly where the name group comes from, but that's just how it's been there in the

## 11:30

literature. So by group, I mean a range of energies that one or more ranges of energies

## 11:36

into which we break up this energy domain. So what,

## 11:40

what we're going to do is, is view the energy domain along one axis. And on the right-hand side,

## 11:46

our maximum energy in our case, that's been 10 MeV is E1. So we're going to index each energy by

## 11:53

this index G for group. And strangely, we're going to go from right to left,

## 12:00

increasing in index, decreasing in energy. Now this seems weird and it is weird, right? It doesn't

## 12:07

make a whole lot of sense, but the reason why we're going to do this is because we're going to

## 12:10

do this because we're going to do this. And the reason that historically this indexing scheme has

## 12:13

been used is because of this idea of increasing lethargy, right? So you, I think I pointed out

## 12:20

lethargy as one of your homework assignments. It's related to the energy. It's a log of a ratio.

## 12:26

Lethargy increases as neutrons slow down. What does lethargy mean in plain English?

## 12:32

Like laziness? Yeah. Laziness. Well, you know,

## 12:35

neutrons are slowing down. They're getting lazier and lazier, right? So this idea of

## 12:39

neutrons starting at 50, they're going to slow down. They're going to slow down. They're going to

## 12:40

fast energies and throughout their life, losing energies is kind of why the, the, I believe that's

## 12:46

why the indexing scheme is the way it is. They start off, this is like the first energy that

## 12:50

they are. And then as they live their life, say they go down in energy, but up in group index.

## 12:56

Okay. So just keep in mind that one will always mean our fastest energy group, right? These are

## 13:03

the fastest neutrons, whereas whatever E sub N, so we're going to have N groups, which requires

## 13:08

N plus one energy boundaries.

## 13:10

So this is group one, two, so on, right? Let me see if I can do that here. So this is group

## 13:20

equal one. This is group equal two. And all the way down here is group equal, whatever our number

## 13:32

of groups is. Okay. So for two energy groups, at least following the sort of rules that we've had

## 13:39

before, we're going to, we're going to, we're going to, we're going to, we're going to, we're

## 13:40

going to say that group one has energies from one EV less than E less than 10 MEV, right? We're

## 13:53

going to skip the fact that we've used this boundary at 0.1 MEV between the fast fission

## 13:59

neutrons and then the slowing down. And then group two is from our, whatever our lower bound is,

## 14:08

which we've taken to be 10 to the minus three EV.

## 14:12

Less than E, less than or equal to one EV. So traditionally these groups are called the fast

## 14:22

group and the thermal group. Okay. Now the choice of the cutoffs is relatively arbitrary, right? We

## 14:46

could choose 10 to be greater and we could choose 10 to the minus three to be lower. The division

## 14:52

at one EV is also subject to change. You'll notice if not today, but Friday, some of the

## 14:59

examples I have use 0.625 EV, right? As a cutoff. Now, why, why would this be like, what, what makes

## 15:08

it, how does it differ if this is one EV, five EV? It depends maybe on the, the, the things that you

## 15:15

have in your system, right? So when you get to the reactor lab, one of the things that you'll learn

## 15:20

about is cadmium. Cadmium is a strong neutron absorber and it has a resonance down at that sort

## 15:27

of sub EV level, right? And because of that, it's really good at taking away all neutrons below the

## 15:36

thermal energy, right? So there's a good, something called the cadmium cutoff and it's, you know,

## 15:40

something like 0.3, 0.4. And so if you use cadmium as a filter for thermal neutrons, well, one EV is

## 15:49

probably a little too large for the, for that cutoff, right? So you'd have to use something

## 15:53

lower. So it, it definitely depends on the system. We're just going to stick with one EV for now,

## 16:00

but just know that depending on, on a paper or a book that you read, it might be a little bit lower.

## 16:05

I kind of like that in our textbook, it's just an EV and 0.1 MEV. They're very simple numbers to,

## 16:11

to remember, and they are close to what your sort of practical values would be.

## 16:16

All right. So now that we, we, we've got this,

## 16:22

this idea of breaking the energy into groups, we can proceed to define these effective cross

## 16:29

sections over the energies of each group. So before we just took an effective cross-section

## 16:34

to be that average cross-section from 10 to the minus three, all the way up to 10 MEV. And

## 16:39

what that did is it gave us one set of cross-section values, one total flux with which

## 16:46

it's multiplied. And then we could take, say the ratio of new sigma F times V over sigma A times

## 16:51

V, the fees canceled because it's just one number. And we're left with that very first

## 16:56

definition for K infinity for our infinite homogeneous system. Although it doesn't even

## 17:01

have to be infinite and it doesn't have to be homogeneous. By the time we get this effective

## 17:04

cross-section, all the math looks the same. So that's one of the nice things we can start off

## 17:10

with just our dependence on energy, but everything I'm talking about will translate or can translate

## 17:15

over when we bring back space, possibly time and some of these other things. Okay. So for,

## 17:21

say given energy group G, right? For energies that are EG plus one, less than E less than EG,

## 17:28

the effective cross-section for some, oh no, why, why, why did it, I don't understand. There we go.

## 17:49

I see what's going on here. I've got to de-select that, but I do want it a little bit bigger.

## 17:59

There we go. All right. Okay. So this effective cross-section over

## 18:09

the range is going to be equal to the integral from EG plus one up to EG,

## 18:18

whatever that, that reaction cross-section is, which is a function of energy times phi of E

## 18:28

divided by phi sub G. Okay. So it's the same thing that we saw before. So whatever our flux

## 18:37

spectrum is, whatever our reaction cross-section,

## 18:39

which is this could be microscopic, but I'm going to leave it as macroscopic and we're integrating

## 18:44

over the energy, right? This, this range of energies and dividing by G sub G, which we,

## 18:50

before that was the integral of the flux from, you know, our lower bound to our upper bound.

## 18:54

So that means that our flux here, phi G is just the integral of the flux spectrum

## 19:06

over that same energy range. Okay. So this is typically called a group flux.

## 19:14

right so when we use a multi-group method the fluxes that we compute or represent in each of

## 19:20

the energy bins or groups is called a group wise flux okay now it's important to note that this

## 19:26

flux is a total flux or integrated okay so when we start off with our flux spectrum v of e what

## 19:49

units does that have per centimeter square per second and importantly per ev right it's a

## 19:59

spectrum okay that means a probability density for energy when we integrate it over energy we

## 20:07

lose the per ev so this thing is the total neutron flux in that energy bin right so it's

## 20:13

important when you start to use that flux not to pretend or make the mistake that that isn't a per

## 20:21

ev uh

## 20:22

quantity right so if if we want if i ask what the um what what the thermal neutron flux is

## 20:30

okay now if i just make that statement i guess one could argue that you could give me

## 20:36

phi sub two if we have a two group right but if i want it in terms of ev right what is the

## 20:41

flux spectrum then you would have to divide by the appropriate delta e right what the width of that

## 20:47

that bit okay this becomes uh an issue especially if if we use

## 20:52

you know if we use a thermal neutron flux and we have a thermal neutron flux and we have a thermal

## 20:52

neutron flux and we'll i'll show you this on friday if we compute the multi-group fluxes for

## 20:57

you know a given group um structure whether it's two groups or 100 groups and if i want to plot

## 21:03

that flux spectrum and compare it to sort of the continuous value like our maxwellian or one over

## 21:09

e and so forth we're going to get really wonky plots unless we take these values and normalize

## 21:16

it to the energy width right or divide by the energy width to convert it okay so that's something

## 21:20

that certainly i've made that up but i'm not going to do that right now so i'm going to do that

## 21:22

mistake before uh and i i'm sure i've had students make that mistake before okay so

## 21:39

now that we know what a basic cross-section looks like in this multi-group format we can

## 21:44

start to tackle the pieces of the slowing down equation ultimately what we want is that spectrum

## 21:50

equation in a multi-group format or in our case today the two-group format right so this is part

## 21:56

of that spectrum equation right we have the total interaction rate on the left-hand side

## 21:59

we have the scattering uh term here and what we're going to break this down and then we also have

## 22:06

vision uh you know external sources i'm going to ignore those for a moment and tackle just this

## 22:11

thing right so to motivate the effective cross-section last time we started off with this

## 22:16

thing on the left-hand side and i said hey let's just integrate it from 10 to the minus 3 up to 10

## 22:21

meb our whole energy range of interest right or maybe zero to infinity right and that that gives

## 22:26

us a total interaction rate well if we do the same integration rate and we do the same integration
rate

## 22:29

on the right-hand side we're still left with the e prime right because if i integrate this from

## 22:36

over some range of energies e that's for the the the e variable that doesn't touch e prime right

## 22:43

that's the the tricky thing about the scattering cross-section

## 22:47

it's effectively like the continuous analog to a matrix right we've got e prime to e well what

## 22:53

we're going to find with the multi-group method is this thing in the integral right this integral

## 22:59

function is going to turn into a matrix where we go from group g prime to group g right and so the

## 23:07

the task now is how do we define those constants okay so the first thing we'll do is is break this

## 23:16

integral up into the uh appropriate sub integrals right uh sum of integrals over each of the groups

## 23:23

and to help myself out i'm going to take these bounds instead of zero and infinity

## 23:29

i'm going to use the upper and lower bounds of integration across my my group structure right

## 23:35

so the highest energy that i have in my multi-group framework is e sub one right that's the the that

## 23:44

would be 10 mev in our case and for the lower bound it will be e sub n plus one which would be

## 23:53

in our case that ten to the minus three okay so once i have it in once i've noted that

## 23:59

then i can take this integral and say hey that's actually e n plus one to e with my

## 24:09

scattering term i won't write the whole integrand just to be a little bit um more compact and then

## 24:16

i would have uh e n e and minus one right so on and so forth for for all the energy groups okay now

## 24:31

in a form that's a little bit easier to tackle and now i can integrate both sides from some

## 24:40

lower bound to some upper bound for group g okay so what i'm going to do is do this for um let's say

## 24:56

g plus 1 e g this will be d e okay so i'm i'm integrating both sides

## 25:06

over

## 25:07

the energy group g, right? Not g prime, g, okay? That means I have to do the same thing over here,

## 25:13

right? So this will be e g plus 1 and e g, okay? And I can kind of block these

## 25:24

off, and that'll be d e, okay? So this thing is formed of n integrals, right, for the n groups,

## 25:34

so I can pick out whatever one corresponds to group g prime. And so the term that I care about

## 25:41

now is this thing that looks like this, e g plus 1, e g, d e, and then e g prime plus 1,

## 25:56

e g prime, and now I'll write out the whole thing, okay?

## 26:17

So this is the...

## 26:18

This is the integral quantity that I'm trying to preserve, right? Before, last time when we

## 26:25

motivated this effective cross-section, we had something that looked like this, right? We had

## 26:30

some product of the cross-section times the flux inside of an integral, and we wanted to replace

## 26:35

that by one effective cross-section times one total flux, okay? Right? So if we wanted this

## 26:41

thing to be, you know, sigma t g times...

## 26:48

One thing I'll... Maybe you caught this. I am not putting the bar on top of the cross-section.

## 26:55

Last time when I introduced the effective cross-section, I made sure to put this bar.

## 27:00

The reason I'm not putting the bar is we have a subscript g, which suggests that we're already

## 27:05

into the multi-group approximation, where all of the things that we're dealing with are, by
definition,

## 27:10

effective cross-sections. So when we're using the multi-group form, I'll skip using the bar,

## 27:16

because I think it just makes it look...

## 27:18

Right? And we'll use the fact that there's an extra g next to whatever the reaction is. So

## 27:23

sigma t, total cross-section, sigma t g, total cross-section for group g, right? So we've got

## 27:30

this sum of all these integrals. What I'm doing is I'm pulling out one term for the contribution

## 27:35

of g prime neutrons to group g, right? So if I wanted to describe this in plain English,

## 27:42

this is now telling me the rate at which neutrons starting between...

## 27:48

These energies, e g prime plus one to e g prime, are scattering into the group whose boundaries

## 27:55

are e g plus one to e g, right? We now have to integrate both parts of the range, the starting

## 28:02

range of energies to the outgoing range of energies. And so, like we did last time, I want

## 28:08

this thing to be set equal to something pretty straightforward. I want this to be a product of

## 28:14

two numbers. I want it to be a product of the group-wise flux.

## 28:18

g prime, right? Because it's those neutrons at g prime that are being scattered into some other

## 28:24

energy group, okay? And this has to be multiplied by the effective cross-section, right? And so

## 28:29

that'll be sigma s g. And if I'm being careful, I'll use an arrow. Hopefully that's legible,

## 28:41

right? So this is sigma sub s, and I have this thing, which is g, a left arrow, g prime, right?

## 28:50

So it kind of...

## 28:50

indicates the direction of energy shifting, right? So I'm going from energies that are in group g

## 28:57

prime to the left to g. Why do I go from right to left? It's consistent with matrix algebra,

## 29:05

right? Ultimately, the scattering cross-section from g prime to g is going to be, like, j to i,

## 29:13

okay? Columns mapped to rows, right? So we'll see that in a little bit. So it...

## 29:19

I think it's the clean way. Sometimes, and actually probably most of the time,

## 29:25

I prefer to write this instead as sigma s g g prime, where I don't put the arrow. It's a little

## 29:32

bit easier to write. So you might see it both ways. Just know that it's the rightmost one,

## 29:39

g prime, is the start group, and then the left-hand one is the final group, okay? So if I have this,

## 29:50

how do I define sigma s g prime, g from g prime? I just divide both sides by the flux. That's the

## 30:03

cool thing about these effective cross-sections. It's like, how on earth do I come up with a

## 30:07

cross-section that'll let me do this? Well, you define what you want. I want one number

## 30:12

times another number to represent this nasty business of two integrals, right? So by definition,

## 30:18

this thing has to be equal to this divided by that flux, okay? And so that means that sigma s, g,

## 30:26

g prime, is equal to g prime plus one d e. Oh, that's not primed, my bad, okay?

## 31:19

Where again, the g prime is the integral flux over that energy group, okay?

## 31:30

Let that sit for just a moment. So at least for cases where we

## 31:54

have pure elastic scattering without any of the thermal effects, we know that sigma,

## 31:59

s, e prime to e is a simple analytic function, right? It's the one over one minus alpha times

## 32:06

e. So if we know what that cross-section value looks like and we have a flux,

## 32:13

get the one over e spectrum, we can actually compute this, right? So one,

## 32:17

there's an old textbook that I had as an undergrad and there was one nasty question in there that
was

## 32:24

define the scattering matrix for hydrogen, right? It wasn't actually that bad, but you have one
over,

## 32:29

e flux and then hydrogen, you have that form and then you make this for a group to group.

## 32:35

I think it was some sort of equal spacing, but you can do that pretty easily for that

## 32:41

pure scattering case. Everything else though, you have to rely on,

## 32:46

let's say heavier duty processing using Monte Carlo or whatever, okay? What about the fission

## 32:52

term, right? So we have the spectrum equation up here and I just ignored fission and other sources.

## 32:59

Okay, what about fission? Well, the fission cross-section is pretty straightforward or even

## 33:05

nu times the fission cross-section is pretty straightforward because that looks just like

## 33:09

sigma x, right? We just substitute that in. But what about chi, right? So in that balance equation,

## 33:15

we would have sigma t e phi of e, okay, is equal to the scattering stuff plus,

## 33:26

now I'll include the fission term, right? We have chi,

## 33:29

chi e, and then we have the total rate at which neutrons are being produced from fission, right?

## 33:35

So it would go from zero to infinity of nu times e, that should be a bar e prime,

## 33:45

sigma f of e prime times phi of e prime, d e prime, okay?

## 33:53

So we've got this product of the chi spectrum, which is the function e, and then the integral,

## 33:59

which has only things that are e prime, okay? If I integrate, like do the same thing that I did

## 34:05

before, if I integrate the entire equation from e g plus one to e g, right? So if I do this,

## 34:17

e g plus one,

## 34:20

right? Defining balance for the g, for group g, okay? If I do that and then I do the same thing

## 34:28

over here,

## 34:29

I'll bring this down then I'm looking at the following I have e g plus 1 to e g d e times

## 34:42

this times e e prime d e prime yeah now what's the what when I make this this integral over

## 35:07

group g right that's for the variable e okay does this impact this integral at all now that that

## 35:19

integral that that I've introduced to for the balance over group g is only applying to chi

## 35:26

right so what is chi chi is our fission spectrum right it's a mathematical model for the probability

## 35:37

that neutrons born from fission show up at some energy e right so it's a probability density so

## 35:42

I

## 35:44

can integrate it just like I can integrate the flux and so what what I can write instead is that

## 35:50

this is chi g right the total probability of neutrons being born in this energy range

## 35:59

defined by group g okay that leaves this this other integral right but we already know how

## 36:05

to handle an integral that looks like that I say that we do nu sigma f g prime

## 36:14

right so this whole double integral right will be this now I have to do the same thing that I did

## 36:26

for scattering where I take this integral from zero to infinity and break it up into each of

## 36:31

those independent things so really what this would be is let me I'll move the chi back a little bit

## 36:44

to give me some time to think about this so I'm going to do this right so I'm going to do this

## 36:45

right I'm going to connect the one to zero trickle right so this integral here is my total

## 36:52

fission production right fission neutron production rate this some represents the same thing right
the

## 37:04

sum because I'm using the total flux in each of those groups times theIB and then I recognize

## 37:12

the integral of one right so I'm normally gonna just but I didn't want somebody asking to ask

## 37:17

me how to solve trying to know how to do this right so again I'm gonna use the integral of one

## 37:19

right and the second thing that we've gotcards now is this integral is being determined by g at

## 37:19

the effective cross section for each of those groups so this is still my total rate at which

## 37:24

neutrons are being produced from fission right total it doesn't matter about group i've integrated

## 37:28

away the energy and so this multiplied by chi g is equal to this this integral right so with this

## 37:36

i have all the pieces that i need to write down the the multi-group balance equation okay so um

## 37:42

that's what we shall do uh a quick question g equal one to n okay if i take this chi spectrum

## 37:59

that i've just sort of chopped up into energy groups what is the sum from g1 g equal one to n

## 38:06

of chi g it would have to be one right because chi of e is a probability density so integrated

## 38:13

over all energy that's equal to one if i've already done that then what would that be

## 38:18

right so as i've already done that then what would that be

## 38:23

i should probably do you the favor of actually writing the definition for kaiji huh

## 38:27

right so that what chi g is just equal to plus one

## 38:36

g right so if that's the case then the sum of all the kaiji should be equal to one right because

## 38:50

all that is is a sum of of the integrals that added up gives me the whole integral yeah

## 38:56

good good good all right so i started to write out some stuff to save us a little bit of time

## 39:09

uh before so this is what we get when we put it all together we start off with that spectrum
equation

## 39:14

right the only thing that i haven't put in this is external sources right because we're

## 39:20

we'll eventually care about uh multiplication so take a look here i think that's everything

## 39:25

i need right so the total number uh the total interaction rate in group g has to be driven by

## 39:33

all of the neutrons uh total loss rate right removal from from group g it has to be balanced

## 39:39

by the number of neutrons going into that group from other groups including self-scattered right

## 39:45

i can have neutrons that scatter from one energy in a group g to another energy in the same group g

## 39:51

and that's captured then by by by sigma s g from g okay and then i also have the vision

## 39:58

uh cross-section so for two groups this uh simplifies

## 40:03

substantially and we end up with a system of two equations right so we have a sigma t

## 40:09

uh one times a phi one equal sigma s one one times phi one plus sigma s one two phi two plus chi one

## 40:28

mu sigma f one phi one plus

## 40:33

chi two nu right so even in two groups it can be kind of a tedious thing to write out all the

## 40:40

terms which is why we'll find a little bit of matrix representation to be useful to you that's

## 41:00

not right uh sigma s two two phi two plus chi two plus

## 41:31

sigma f two phi two oh at least it's sort of cookie cutter all right this is what we have

## 41:40

this could be written in matrix form right so anytime that you can write down an algebraic

## 41:46

uh system of equations you can do it in matrix form so i won't write the matrix well no it's

## 41:52

it's useful maybe to see it for the two group case right so this would be t one uh sigma t1 sigma t2

## 42:01

that's a matrix two by two right and we have a vector of fluxes okay using matrices can make

## 42:09

the scattering significantly cleaner right so we have sigma s one one sigma s two from one sigma s

## 42:20

uh no that's one one from two this is two from one sigma s two two okay also times

## 42:31

phi one phi two fission is a little bit strange looking right because we have that separate chi

## 42:40

that's not inside of the the primed integral right so what this looks like is this chi one chi two

## 42:52

multiplied by nu sigma f1 nu sigma f2 and then this is multiplied by

## 43:01

phi 1 phi 2. you might remember from matrix analysis that this thing here is called an outer

## 43:09

product right where you have one vector so you're familiar with the dot product that takes like a
two

## 43:15

uh two element array with another two element array and it makes one value the outer product

## 43:20

is like going the opposite direction you're kind of expanding the thing so you're going from a two

## 43:24

by one times another two by one thing and you're getting a two by two so this thing is actually a

## 43:29

two by two matrix

## 43:31

the kind of cool thing about that matrix is it's rank one do you remember anything about rank

## 43:39

from linear algebra it basically means in this case that it's not invertible right uh but it's

## 43:46

simple right and if you can take a an n by n matrix and represent it as one vector with another

## 43:52

vector that means that you can simplify things a lot right but uh basically we don't have to talk

## 43:59

about it all right so it's two by two and we we get that you get the two by two matrix and then

## 44:02

you can tell i like linear algebra um this is our our equation so you can imagine in larger groups

## 44:10

or larger numbers of groups that this looks uh it can be easy uh so we might try to cast this in a

## 44:18

slightly different form right we could say that the total cross sections are the uh like a matrix t

## 44:25

and then we have a flux term here and we could have the scattering cross sections in a matrix s
times

## 44:32

flux and then we could have a chi vector times this um new uh maybe try to state kind of with the

## 44:49

uh so i uploaded a supplement that that kind of captures a lot of these equations so chi here

## 44:59

would be a column vector f would be new sigma f also column vector so i'm taking its transpose

## 45:05

right that that gives me that outer product so

## 45:08

what's nice is in this form it doesn't matter what our group structure is it's going to look

## 45:12

exactly like this right all right so this is kind of a mess but because of the physics

## 45:24

we can simplify it quite a bit first things first what is chi two how much of the chi

## 45:33

spectrum lives in energies below 1 eb which is what we're defining thermal neutrons to be

## 45:41

yeah it's zero right so

## 45:44

is equal to zero all right how about our scattering terms we've got these four scattering

## 45:52

cross sections scattering one one and two two those should exist you can always have self scatter

## 45:59

we know that neutrons in group one which are fast will scatter down to group two right that's just

## 46:06

but that's part of our slowing down but what about group two scattering into group one it should be

## 46:17

zero yeah i mean so we talked before about the the thermal neutrons this idea of thermal agitation

## 46:26

what's kt right 0.0253 at room temperature so we saw what that maximum volume looks like we

## 46:34

i gave you some examples of what those scattering cross sections look like that

## 46:37

induce the the the upward uh energy movement above uh about an eb we don't see it so there's

## 46:44

there's a reason that we choose a sort of a thermal cutoff on that order of one eb because

## 46:49

above it

## 46:50

we don't see a whole lot of neutrons going up in energy you don't see a whole lot of neutrons

## 46:54

below that energy creeping up above that energy there will be some small fraction it depends on

## 47:00

the temperature of the system naturally but we usually choose that cutoff so that up scattering

## 47:06

doesn't happen right or if we have multiple energy groups we'll choose a cutoff so that only some

## 47:11

number of groups has this up scattering effect that you can kind of treat it as a separate thing

## 47:16

so what that means here is that sigma s

## 47:20

one from two is equal to zero okay so that's nice because in our equation up here

## 47:30

that means that anything with chi two goes away right that also means that we don't have

## 47:38

our scattering from two to one here okay so that that simplifies things i can also introduce

## 47:46

a removal cross section right and this is uh you'll need this for the homework

## 47:51

it's also something that you find in historical um resources but older books and so forth so

## 47:57

the removal cross section for group g is equal to the total cross section for group g minus

## 48:05

the self-scattered cross section for group g that means neutrons going from group g and still

## 48:12

ending up in group g even though their energies might have changed right so if we do that then

## 48:17

the equation looks like

## 48:28

this r1 v1 equal nu sigma f1 v1 plus nu sigma f2 v2 and sigma a2 v2 is equal to sigma s

## 48:49

two from one two from one times v one there's uh one one other thing that

## 49:00

i'm using these approximations but if chi two is equal to zero what does chi one equal

## 49:06

we only have two groups right so chi one is equal to to one so i don't even write chi one anymore

## 49:14

right so i can put that here chi one equal one okay if i don't have up scatter from group two

## 49:23

to group one then the only scatter that thermal neutrons have is self-scatter group two to two

## 49:29

which

## 49:30

means that the removal cross section for group one is equal to the absorption cross section

## 49:36

because we only have two classes of reactions we have scattering we have absorption absorption

## 49:42

also includes fission but this would be so sigma r2 is equal to sigma a2 right and so these are

## 49:54

the two group equations right when we're dealing only with energy

## 50:00

okay so i'm going to wait to give you sort of the punch line until next time but the question

## 50:06

i have for you is can you solve this system of equations if you look at it you probably start

## 50:18

to feel a little weird because the unknowns show up in both sides right like that you can't you

## 50:24

can't get rid of the unknown so and from this equation you can solve for v1 in terms of v2

## 50:30

or vice versa so let's say that we solve for uh

## 50:34

v2 so v2 is equal to v1 times the scattering cross section divided by sigma a2 so we plug that in

## 50:40

to v2 up here what does that give us we have one equation then that has v1 on both sides so if v1

## 50:49

cancels out so immediately we know that we can't solve for v1 right that's a little weird right and

## 50:55

then we only end up with that balance equation if sigma r1 is equal to nu sigma f1 plus nu sigma f1

## 51:04

f2 times the ratio of these things that we use for getting rid of v2 right so that could be

## 51:12

satisfied but not generally going to be so right because these are just numbers these effective

## 51:18

cross sections they're numbers we get them out of some spectrum averaging right but it could be

## 51:22

some nasty physics that gives us uh that those numbers so in general these things cannot be

## 51:29

satisfied so what we need is some sort of fudge factor something that gives us one

## 51:34

additional degree of freedom okay you can take a guess for what that additional degree of freedom

## 51:40

will be but we'll we'll wrap that idea up on friday so to take a think about that a little

## 51:46

bit you can certainly look at the the supplement and you know find what the answer is right but

## 51:52

we'll pick up with that and extend this to multiple energy groups at least computationally

## 51:59

using open mc all right i will see you fridays

## 52:04

stick around if you have questions i'll be uh wrapping up as i i typically do
