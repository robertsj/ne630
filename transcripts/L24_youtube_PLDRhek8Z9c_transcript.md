# L24 Local Audio Transcript

Course: NE 630

Playlist source: https://youtube.com/playlist?list=PLy481lNHlnHoEO95vM-xYX2bydD25v20L

Video: NE 630 - Lesson 24

URL: https://www.youtube.com/watch?v=PLDRhek8Z9c

Video ID: PLDRhek8Z9c

YouTube upload date: 20231020

Duration: 31:19

Transcript source: Local faster-whisper transcription from YouTube audio.

Whisper model: large-v3; detected language: en.

Generated: 2026-06-28

Note: This transcript is machine-generated from audio and lightly wrapped only. It should be reviewed before being quoted, published, or used as polished lesson text.

Requested language: en

## 00:19

Okay, so I've got to do this again, even though I just had a pretty reasonable live lecture

## 00:24

through Zoom, the recording failed. So I'll try to do this justice a second time.

## 00:32

Today, what we're going to talk about is the linear reactivity model. And this builds on

## 00:37

what we discussed last time related to fuel depletion and the use of the simplified actinide

## 00:44

chain, where we have just the two uranium nuclides and the plutonium nuclide. And we

## 00:50

talked a little bit about burn up and then ultimately the impact on reactivity of this

## 00:55

evolution of the fuel nuclides. And this will lead us into what we discussed today

## 01:01

in the linear reactivity model, where we use the fact that the reactivity does appear to be

## 01:07

a linear function of burn up. So a little bit of review first. So as a function,

## 01:14

of time or fluence, or as we'll see, burn up, the reactivity looks a lot like A's line.

## 01:20

And when we computed rho as a function of fluence using the simplified U and PU model,

## 01:27

it looked something like this, right? So this looks a little different from the slides last

## 01:32

time I adjusted it, but you can see the changes I've made in this notebook, right? I'm not showing

## 01:37

you all of the code, but you can take a look to see what the changes are. Now, this ends up being

## 01:44

overestimate of the reactivity, right? And the reason for that is that we're ignoring some

## 01:49

details like the generation of fission products, which tend to be neutron absorbers or neutron

## 01:54

poisons, right? Sumerium-149, other isotopes of sumerium, neodymium, rhodium, other things that

## 02:02

by the end of the fuel's time in a core tends to reduce the reactivity by about 5% delta K over K.

## 02:12

So rho 0.0.

## 02:14

Or a delta rho 0.05. So if you consider this reactivity shown here in the plot after five

## 02:20

years of fixed flux, we're at 0.10. So we'd be reducing that by a little bit more. Another

## 02:26

factor is the time evolution of the flux. So here we're assuming a flux of two times 10 to the 14th.

## 02:37

Now, that gives us roughly the proper fission rate, which gives us the proper power. And

## 02:44

so forth. But we know that if the fissile content of the core is going down in time because of

## 02:51

depletion, then to have a constant fission rate or a constant power, the flux has to increase to

## 02:58

compensate for that. So if the flux is increasing as a function of time, then the depletion is

## 03:03

actually happening faster, which means that rho would go down faster than what we're seeing here

## 03:07

for the fixed flux, okay? So these are details that can certainly be accounted for in models.

## 03:14

It's just beyond what we're aiming to do at this point, okay? So for a constant fission rate,

## 03:21

the power is constant. Burnup is proportional to time, right? The energy produced is constant

## 03:26

because the power is constant, but the flux will increase, right? And so we'll capture this

## 03:30

in the model that we explore later, the linear reactivity model, right, using the data that we

## 03:36

do. But to make sure that we're all on the same page, I'd like you to explore this example with

## 03:43

me where we come to the point where we're at 0.0. So we're at 0.0. So we're at 0.0. So we're at

## 03:44

0.0. So we're at 0.0. So we're at 0.0. So we're at 0.0. So we're at 0.0. So we're at

## 03:46

So what I've done here is for our PWR unit cell that we've been looking at, I've computed the

## 03:53

effective fission cross-section averaged over the entire spectrum. So the flux we're talking about

## 03:57

is the total flux, not the thermal flux, not the fast flux, but the total flux,

## 04:01

okay? So for a reactor like Wolf Creek, which is very similar to, it has fuel that is pretty

## 04:06

well represented by our unit cell. Wolf Creek is a 3,000 megawatt thermal reactor. So one gigawatt

## 04:13

electric, you assume a 33% efficiency, the power it's producing is 3000 megawatts thermal, right?

## 04:19

So the core volume is about 10 to the 7. And the way that I generate that number, it's a round

## 04:24

number, which I like, but I generate that by remembering a couple things. One, we have the

## 04:29

dimensions of the fuel that we've been using. So say a fuel radius of 0.45 centimeters. I remember

## 04:36

in the back of my mind, this is a number you might remember too, is that the height of the fuel or

## 04:40

the length of the fuel elements is about three meters, so 10 feet or so. Now, if you take that

## 04:45

length and the area, cross-sectional area of the fuel element, and you couple that with the fact

## 04:51

that there are roughly 50,000 fuel elements in the core, you end up with a volume that's very

## 04:56

close to 10 to the 7. So I'm using that as a round number. The effective macroscopic cross-section

## 05:02

of 0.05 inverse centimeters comes out of OpenMC, so it's a pretty reasonable number. And based on

## 05:07

this, I want to compute the total flux.

## 05:10

The way that I would do this is as follows. It's very similar to one of the exam questions where I

## 05:20

asked you to compute a thermal flux, but what you should be trying to balance is the fission rate or

## 05:26

the energy production rate with this thermal power that's given. So the total number of fissions

## 05:32

that are happening in the core should be equal to the volume times the flux times that

## 05:40

are produced per second. So I'm going to multiply this by the energy produced per fission. So this

## 05:45

would give me the number of fissions occurring per second. Now, to get the number, the amount of

## 05:50

energy produced per second, I'd have to multiply this by the energy produced per fission. So that

## 05:56

would be this thing multiplied by, say, 200, where the 200 is MeV per fission. So this gives me the

## 06:03

total energy produced in our reactor per second in units of MeV. And so I'll leave that there.

## 06:10

This has to be then balanced by the core power, right? So we have this equal, this must equal our

## 06:16

3000 megawatts thermal, which that's megawatts. So I'll do times 10 to the sixth to get it into
watts,

## 06:23

which is joules per second. And then this has to be multiplied by some factor that takes me to MeV,

## 06:29

right? So I'll use 1.6 times 10 to the minus 13 MeV per, sorry, joules per MeV, and then take the

## 06:40

data. And so what I'm left with is this equation. Okay. The only unknown here is that flux. And so

## 06:47

if you compute that flux, you should get something like P is equal to 1.9 times 10 to the 14, right?

## 07:00

And that would be in per centimeter square per second, okay right there, if I can spell. Okay.

## 07:06

So that's the flux. And so it's very close to the two-tenths,

## 07:12

to the 14 that I use for the reactivity curve that we just saw, right? About a factor of two more

## 07:17

than what I had used last time. Now, I said that the flux increases in time to compensate for the

## 07:23

depletion of the fissile stuff. The exact amount by which it increases depends on the system, but

## 07:29

sort of a ballpark figure would be about a factor of two. So we'd go from, in this case, a flux of

## 07:35

two times 10 to the 14 up to three, so four times 10 to the 14 as a kind of a crude estimate.

## 07:43

Now, what's the total fuel mass corresponding to that fuel volume that we just used, right? And

## 07:49

we'll assume UO2 at 10 grams per centimeter cubed. All right, so this is pretty straightforward,

## 07:55

right? So we've got our 10 to the 7 centimeters cubed, and then we have our number of grams per

## 08:04

centimeter cubed. So we've got our 10 to the 7 centimeters cubed, and then we have our number

## 08:05

of grams per centimeter cubed, right? So this would be the total mass of UO2. Now, when we talk

## 08:10

about burn up, as we'll do later, we normalize the energy produced in the reactor to the mass

## 08:15

of the initial fuel. Now, fuel could mean UO2, but what is actually meant is the heavy metal

## 08:21

component, so the uranium or other actinides, right? So we have to multiply this by the mass

## 08:26

fraction of UO2 that is the uranium, and that is approximately equal to 238 over 270, right? 270 is

## 08:34

238 plus 2 times 16 from the oxygen. And so what we end up with is this large number, right? So

## 08:43

if we take the, so this is the number of grams. If I take this and divide by 1,000, that's the

## 08:48

number of kilograms, which we'll use for the burn up unit. So that's 88,000 kilograms of uranium or

## 08:55

metric tons of uranium. What is the fuel burn up after one day at that flux that we just saw? So at

## 09:05

that reactor power?

## 09:06

And then after five years. Now, remember that fuel burn up is the energy produced per mass of

## 09:15

the uranium that was originally loaded into the core. So we just saw that there are 88 tons of

## 09:21

uranium. And at the power that we're considering, right, 3,000 megawatts or three gigawatts,

## 09:30

right? And if we have three gigawatts for one day, then the burn up after one day will be

## 09:36

three gigawatts times one day of operation normalized to the 88 tons of the UO2,

## 09:45

88 tons of the uranium as part of the UO2. And what we get then for the fuel burn up after one day

## 09:51

is 0.034 gigawatt days per metric ton of uranium, or equivalently, that is 0.034

## 10:02

megawatt days per kilogram, right? The difference is a factor of 1,000,

## 10:06

0.034 gigawatt days per metric ton of uranium. Now, this is sort of a very much an upper bound

## 10:25

for the burn ups that we see in practice for something like Wolf Creek, the burn ups of the

## 10:29

fuel when it's removed from the cores closer to, say, 50 gigawatt days per metric ton of uranium.

## 10:35

But the burn up after five years is 0.034 gigawatt days per metric ton of uranium. So if I want it

## 10:36

that we're seeing as discharge burn ups, the final total accumulated burn up has been increasing

## 10:42

in time. Part of that is increasing enrichments, right? The more uranium you start with, the higher

## 10:48

the burn up can be. And that just makes some sense, right? But in practice, we see less than

## 10:53

the 62. And part of that is what related to the reactivity that decrease in the reactivity that

## 11:01

we see in practice. Okay, so keep this number 62.

## 11:06

Kind of as an upper bound in mind, right? So what we'll do now is actually look at the reactivity as

## 11:13

a function of burn up. And what I've done is taken a model that was part of a publication called a

## 11:19

nonlinear reactivity method with application to accident tolerant fuels, right? There's a link

## 11:24

to the paper. The paper is uploaded to Canvas. The reason I gave you that paper is because it

## 11:29

was written by me and my colleague, Hitesh Bindra, who was at K-State up until just a couple of
years

## 11:36

ago. But importantly, for undergrad students, right? And so most of the work was done by them.

## 11:42

I kind of put it all together and I guided it because I was a neutronics person. But by and

## 11:47

large, it was these undergrads who helped construct all of the models, did some research and so
forth.

## 11:52

And so all that is put into the paper, a lot of details don't matter. It was all about this

## 11:58

accident tolerant fuel topic, which is looking at fuel that has cladding that is different from

## 12:03

zirconium. And by different, I mean,

## 12:06

possibly better in terms of safety, right? So ceramics or stainless steels that are more

## 12:11

corrosion resistant, things that were of interest following the events at Fukushima back in 2012,

## 12:19

right? So all this stuff is on GitHub, but the major thing that we're extracting from that is

## 12:26

this default reactivity model. And by model, I mean, it's a mathematical expression for reactivity

## 12:32

as a function of burn up. And also, as you see here,

## 12:36

it's a temperature, a coolant temperature and a boron concentration. We don't need to worry about

## 12:41

the temperatures. We'll keep them at their default values and we're not going to worry about boron.

## 12:45

Part of the homework that you're working on though, has you look at how much boron should

## 12:50

be added to the coolant in order to compensate for excess reactivity. So in a PWR, that excess

## 12:56

reactivity is usually not controlled by control rods, but it's controlled rather by adding boric

## 13:02

acid to the coolant, right? So you're increasing the absorption cross-section of the water,

## 13:06

by a huge amount because boron has an absorption cross-section of something like 3,000 barns. So

## 13:11

it's a big deal. Okay. We're not going to use that here. Although you could use this function to

## 13:16

explore things and give yourself sort of a sanity check on what you're doing. Okay. So that's our

## 13:22

function. Let me go ahead and run that cell. I'll explain what this arc tan two is doing. We'll see

## 13:28

where that shows up once I make the plot for the function. So this is the reactivity.

## 13:36

This is the default Zercloy, sort of standard light water reactor fuel element that is similar

## 13:41

to what we've been looking at, you know, for a few weeks now. Okay. It's obviously very linear

## 13:46

with burnout, right? And I've used grid lines here to help guide your eye to certain features,

## 13:53

like at 20, a burnup of 20, it's a reactivity of 0.1 and at a burnup of 50, it's reactivity of

## 14:01

minus 0.1. I've taken the burnup all the way out to that 62 that we just saw. And

## 14:06

Obviously, the reactivity is really negative, and that means the reactor, if it were fueled with
this fuel at that amount of burnup, would be totally subcritical, right?

## 14:17

To be critical, rho has to be zero, and surely we would have excess reactivity, but the core would
no longer be able to operate as soon as we pass this mark right here, right?

## 14:29

I do want to zoom in briefly because if you notice, there's this little blip at the beginning.

## 14:34

And if I look at that blip, we see that we start off with a reactivity peaked at about 0.26, and
then it drops to somewhere between 0.23 and 0.24.

## 14:45

And I ask you, what would be causing this?

## 14:49

What is changing rapidly to bring down the reactivity?

## 14:51

And it's something that we talked about just a couple lessons ago.

## 14:55

It's the buildup of xenon, right?

## 14:57

So as it approaches this asymptotic value and then starts going down as a line, we've hit that
equilibrium xenon.

## 15:04

So if you take a look, that difference in rho of 0.26 down to somewhere between 0.23 and 0.24,
that's a delta rho of 0.02 to 0.03.

## 15:16

That's a 2% to 3% defect in K, right?

## 15:22

So keep that in mind as you're doing your homework because one of the things I ask you to do is
figure out what the reactivity difference due to the xenon buildup is.

## 15:30

And it's about 2% to 3% delta K over K.

## 15:33

Okay.

## 15:34

So I'll get rid of the zoom in feature, okay, and back to our reactivity.

## 15:39

Now, based on the plot here and using the grid lines, where does the burnup go subcritical?

## 15:45

And just kind of using the grid lines, it looks like about 35 megawatt days per kilogram, right?

## 15:51

That's a far cry from the 62 that we sort of estimated.

## 16:00

Now, with this model for the reactivity, this mathematical function, we can actually dive into the
linear reactivity model,

## 16:06

which is based on 4K.

## 16:08

Three assumptions.

## 16:09

First, a reactor core is fueled with N batches of identical fuel.

## 16:14

And to give this a concrete flavor, we'll use a concrete example.

## 16:19

So let's suppose that N is equal to 3, which is pretty similar to how reactors like Wolf Creek are
refueled, right?

## 16:26

But by a three-batch cycle, what we mean is that one-third of the core is replaced with fresh fuel.

## 16:34

One-third is once burned, and one-third is twice burned, right?

## 16:37

So when...

## 16:38

When the reactor is refueled, one-third of the core is going to be all fresh.

## 16:41

One-third will have been in there for one cycle, and then the other third will have been in there
for two cycles.

## 16:47

Now, the fresh fuel is being put in, and it's replacing fuel that has been in there for all three
cycles.

## 16:53

And after that third cycle is for a three-batch core, it's removed, okay?

## 16:58

We say that the reactor is at the beginning of cycle after the refueling.

## 17:02

So when we have that one-third of the core being fresh, that's the beginning of the cycle.

## 17:06

And then at the end of the cycle...

## 17:08

Which, for something like Wolf Creek, is roughly a year and a half, 18 months, we say that we're at
the end of the cycle, right?

## 17:16

So the end of the cycle is defined by the core having no more excess reactivity.

## 17:23

So the reactivity is defined by the reactivity curve that we just saw, and then we usually add an
additional leakage penalty, similar to the P sub NL, or probability of non-leakage that we've seen
with the four-factor formula, okay?

## 17:35

The burn-up...

## 17:36

The burn-up that takes us from the beginning of cycle to the end of cycle is called the cycle
length, and it's given this symbol, B sub C.

## 17:44

And then the burn-up of that thrice-burned fuel that's taken out of the core upon refueling has
accumulated burn-up equal to that cycle length over all three cycles, and is called the discharge
burn-up, right?

## 17:57

So that'll...

## 17:58

In the linear reactivity model, that'll end up being three times B C.

## 18:03

The second assumption in all of this is that the fuel reactivity...

## 18:06

The second assumption in all of this is that the fuel reactivity...

## 18:06

is linear with burn-up, and that's, in fact, what we just saw in that previous plot, with the
exception of the xenon blip at the beginning.

## 18:14

But beyond that, we're assuming a straight line.

## 18:17

I put the infinity here because that's the reactivity that we get out of a unit cell calculation, or
in practice, it's usually like a full assembly, one of these 17 by 17 assemblies that we see for a
pressurized water reactor, or something smaller for, say, a boiling water reactor.

## 18:32

But it's still this infinite reactor, right, of some repeated unit cell.

## 18:36

Or it might be a large unit cell, but still a repeated pattern, okay?

## 18:41

So that's for the fuel itself.

## 18:44

Now, the third assumption then takes the fuel reactivity and couples it with this leakage penalty,
and what we're left with is some weighted average of the batch reactivities for batch one through N,
okay, minus this leakage penalty, and where the weights have to add up to one.

## 19:01

Now, in the simplest linear reactivity model, we set those weights to one over N, so that this is
strictly an error.

## 19:06

So we're left with the arithmetic average of the batch reactivity.

## 19:10

So very simple.

## 19:11

For the homework, I'm having you look at an unequal weighted batching that is a little bit better at
capturing the reality.

## 19:19

When you put fresh fuel in, it's more reactive.

## 19:22

You'd expect the power in that batch to be a little bit larger, right, rather than being the same
power that you have in this twice-burned fuel that has all these poisons built up and all that.

## 19:32

So by properly choosing the weighting, you can capture some more of this.

## 19:36

The physics for what we're doing here will keep it simple and stick with the equal weighted
averaging.

## 19:43

So now, the big thing that we do with the linear reactivity model is to compute the cycle length and
the discharge burn-up, right, and we'll do this for an arbitrary N-batch core, starting with a two-
batch core because that's pretty straightforward.

## 19:56

Okay, so go back to example four, and let's come up with a linear model for the fuel reactivity,
right, and then we'll look at the two-batch core and then compare that to the fuel reactivity.

## 20:06

So let's go to the one-batch, eventually to the one-batch core, and then we'll want to know, is this
two-batch core sort of properly defined if the cycle length is 10 gigawatt days per metric ton?

## 20:19

So going back to example four, we had seen that the reactivity at 50 gigawatt days per metric ton
was minus 0.1 and at 20 was 0.1, okay?

## 20:33

So what we need to do is draw a straight line between those two things.

## 20:36

Okay.

## 20:36

So what I've done here is sketched out the equations, right?

## 20:41

So we have the reactivity is linear

## 20:43

and we can write that as rho naught minus AB, right?

## 20:48

So A is our slope, rho is our intercept, okay?

## 20:51

So when we actually do this,

## 20:54

we end up, the slope will be 0.00667, right?

## 20:58

And the way that we get that is

## 21:01

A must be equal to minus...

## 21:06

0.1 minus 0.1 over 50 minus 20, right?

## 21:15

And that gives us the 0.00667 and change, right?

## 21:21

It's a repeating decimal, right?

## 21:22

That's the slope.

## 21:24

Now with the slope,

## 21:26

actually maybe put these together.

## 21:28

There we go.

## 21:31

With the slope, now we can find what that intercept is.

## 21:34

And so rather than trying to look at the graph

## 21:36

all the way around,

## 21:36

where the burnup is zero,

## 21:38

just take one of the two points

## 21:39

that we've already identified, right?

## 21:40

So we know that the reactivity at 20 is equal to 0.1.

## 21:44

So we substitute our slope

## 21:47

and that burnup into the reactivity equation

## 21:49

and we get that intercept of 0.23 repeating, okay?

## 21:54

Then the beginning of cycle reactivity

## 21:57

for this two batch core

## 21:58

is the weighted average of the reactivity

## 22:02

of the fresh batch, right?

## 22:05

So rho naught minus A times 0.1.

## 22:06

So we get 0 because there's no burnup on that fresh fuel.

## 22:08

And then plus the reactivity of the second batch,

## 22:11

which has already been in there for one full cycle

## 22:13

of 10 gigawatt days per metric ton.

## 22:16

So when we take that average, we get 0.2

## 22:20

and then we have to subtract away the leakage penalty.

## 22:22

So this is something like 0.15, okay?

## 22:27

And then the end of cycle,

## 22:29

which is what we really care about

## 22:31

is the arithmetic average of the reactivities

## 22:34

at the end of cycle.

## 22:35

So 10 gigawatt days per metric ton.

## 22:36

10 gigawatt days per metric ton for the first batch

## 22:39

and then 20 for the second batch.

## 22:41

When you do that,

## 22:42

you end up with a end of cycle reactivity of 0.08

## 22:46

accounting for the leakage.

## 22:47

And so the question is, is this cycle well-designed?

## 22:51

And the answer is no,

## 22:52

because we want to have no excess reactivity

## 22:55

at the end of the cycle.

## 22:56

Because if there's more reactivity,

## 22:58

we could keep operating before refueling, right?

## 23:00

Refueling is an expensive process.

## 23:03

Good rule of thumb,

## 23:04

at least it was taken,

## 23:06

10 to 15 years ago,

## 23:07

but it may be inflation has changed it.

## 23:09

A good rule of thumb is every day

## 23:11

that a nuclear power plant is shut down

## 23:13

costs them $1 million, right?

## 23:18

So not a small number, right?

## 23:20

When refueling takes things up to three to four weeks

## 23:24

or more, of course,

## 23:25

it's usually done in conjunction

## 23:28

with other maintenance and so forth, right?

## 23:30

If it's shut down, you get all your work done,

## 23:33

which can make it take a little bit longer,

## 23:34

but it's expensive to shut down.

## 23:36

A nuclear power plant, right?

## 23:37

Because you're not generating the electricity

## 23:39

and so you can't,

## 23:40

you're not making the revenue.

## 23:43

Now, as a final example,

## 23:45

let's determine the cycle length

## 23:48

and the discharge burnout for the two batch core,

## 23:50

where our discharge, sorry,

## 23:52

where our cycling actually gets us to a reactivity

## 23:55

equal to zero at the end of the cycle, okay?

## 24:00

So we have our slope, right?

## 24:03

I'll write that down here again.

## 24:05

So that was our 0.1 minus, sorry.

## 24:09

Minus 0.1, minus 0.1 divided by 50, minus 20, right?

## 24:16

That was our a,

## 24:17

and then our row not was equal to zero.

## 24:22

Actually, I can just write it down here.

## 24:25

0.233 and change, yep.

## 24:32

Okay, and what we want to do is compute that cycling.

## 24:35

So, kind of, you know, if we just go back here, right?

## 24:36

The one thing that will make us do sorry,

## 24:36

And I'll do it as a Python comment here. What we want is zero is equal to the averaging, so 0.5
times rho naught minus A times B sub C, right? This is our end of cycle reactivity for the first
batch. It's been in there only one time.

## 24:58

And then the reactivity of the second batch, which has been in there two times, so 2 times A times B
C, right, minus our leakage penalty of 0.05, okay?

## 25:11

And so if I rearrange this a little bit, then I have 0.5 times 2 times rho naught minus 3 times A
times B C is equal to 0.5.

## 25:28

And so then I can take 0.05 divided by 0.5 to get that cleaned up. That should be, and then I can do
2 times rho naught minus that will give me 3 times A times B C, right?

## 25:48

I'm doing some things in my head, so hopefully you can fill in some of those steps. And then that
gives me everything I need to find B C, right?

## 25:57

So B C.

## 25:58

So B C is going to be equal to 2 times rho naught minus 0.05 over 0.5 divided by 3.

## 26:08

And so if I do that, so B C is equal to 2 times rho naught minus 0.05 divided by 0.5 divided by 3.

## 26:22

So what is that cycling?

## 26:25

Oh, that's not right. I've messed up somewhere here.

## 26:29

It was much easier when I had all this.

## 26:46

It was a bunch of you.

## 26:47

So let's try to figure this out.

## 26:50

The cycle length would be.

## 26:57

I got another mistake.

## 27:00

You have to redo it for another time.

## 27:07

Right.

## 27:07

So the cycle length should be equal to.

## 27:14

Right.

## 27:14

So the cycle length is this.

## 27:16

The cycle length is 2 over 3 times A.

## 27:20

3 times A times rho naught.

## 27:26

Minus 0.05 for our leakage.

## 27:30

And so what this gives me then is.

## 27:32

So this should actually be a minus.

## 27:36

So 18.33, right?

## 27:38

So that means that the discharge burnup is equal to 2 times the cycle length.

## 27:46

So the discharge burnup is 36.66.

## 27:49

Now, if we go back to the reactivity curve we saw before, it hit zero at 35 gigawatt days per metric
ton.

## 27:56

If we add in that leakage component, it'll have been a little less than the 35, which means that the
fuel in our two batch cycle is actually producing more energy before we put it into storage, right?

## 28:10

By a small amount.

## 28:12

This is important in practice because it lets us get more energy out of the fuel than we would if we
just put it all into the core, burned it, and then took it all out.

## 28:21

And in general, the core end of cycle reactivity.

## 28:26

Is this, you know, average where we have n times rho naught and then A plus 2A plus all the way
through n times A, all times the cycle length, we adjust for the leakage, right?

## 28:38

So we're solving this.

## 28:39

And if you solve for that and then compute the discharge burnup, what you end up with is described
here in the table, which is in the first supplement I gave you.

## 28:50

If we go from one batch to two batches, our discharge burnup increases by a factor of four.

## 28:56

Thirds, right?

## 28:57

If we go to three batches, that factor goes to three halves.

## 29:01

So we're getting 50% more energy out of the fuel than we would otherwise do.

## 29:06

And if you take that all the way to an infinite number of batches, then you get up to a factor of
two.

## 29:13

And so for a plant like Wolf Creek, we're getting something like 50% more energy out than we would
if we had a single batch system.

## 29:22

Up north in Canada, in the can-dube reactors.

## 29:25

They use on.

## 29:26

Line refueling.

## 29:27

So basically they're putting in new fuel every day, every day and taking out old fuel.

## 29:32

And so this is kind of like an infinite number of batches, continuous refueling.

## 29:37

So they're getting a lot more energy out of the fuel than what they would get if we used a single
batch cycle, right?

## 29:45

So what this all does for us in practice is it helps us understand why cycle lengths are what they
are, right?

## 29:52

We have this reactivity as a function of burnup with that.

## 29:56

Along.

## 29:56

With this batching system, we understand why the refueling cycles are the way they are.

## 30:01

The only other part of that is related to things like, you know, weather, the demands of the grid.

## 30:09

So when does a plant like Wolf Creek refuel?

## 30:13

Well, it tends to be in the spring or in the fall when the weather extremes, the temperature
extremes are at a minimum, right?

## 30:19

You don't want to be turning off your big nuclear power plant in the summer when the electricity for
air.

## 30:26

Conditioning is needed and vice versa in winter.

## 30:29

You don't want to deal with the impacts of cold weather, right?

## 30:33

Not that too many of us use electricity for heating, but it is it is definitely an important part of
the electricity usage.

## 30:41

So all this together should provide you a basis for understanding some of the practical parts of
nuclear power plant operations.

## 30:51

OK, next week, we'll be turning to reactor kinetics,

## 30:56

where we

## 30:56

do now consider a d phi dt type term, right?

## 31:00

So we'll be solving differential equations that help us understand how the flux changes in time due
to perturbations in the system, right?

## 31:09

So get started with chapter five, sections one and two for Monday.
