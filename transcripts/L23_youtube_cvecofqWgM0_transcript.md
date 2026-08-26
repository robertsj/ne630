# L23 Local Audio Transcript

Course: NE 630

Playlist source: https://youtube.com/playlist?list=PLy481lNHlnHoEO95vM-xYX2bydD25v20L

Video: NE 630 - Lesson 23

URL: https://www.youtube.com/watch?v=cvecofqWgM0

Video ID: cvecofqWgM0

YouTube upload date: 20231017

Duration: 30:22

Transcript source: Local faster-whisper transcription from YouTube audio.

Whisper model: large-v3; detected language: en.

Generated: 2026-06-28

Note: This transcript is machine-generated from audio and lightly wrapped only. It should be reviewed before being quoted, published, or used as polished lesson text.

Requested language: en

## 00:15

Last time we talked about reactivity control and fission products. Remember, reactivity control

## 00:22

was this idea that we start off with excess reactivity in the core because you need more

## 00:27

fuel than you need right at the beginning because after the first fission, your amount of fissile

## 00:33

stuff goes down. So you need to compensate for that with excess fuel, which leads to excess

## 00:39

reactivity. And we control that with control elements, possibly by dissolving a neutron poison

## 00:46

called a chemical shim in the water of a light water reactor, specifically a pressurized water

## 00:52

reactor. And then as we start to operate at full power, we have additional impacts on the reactivity

## 01:00

from, say, the generation of xenon-135, which we saw has an enormous cross-section. But there are

## 01:06

other fission products like samarium-149, which you should

## 01:09

read about in the book, and others in addition to samarium-149 that we'll see in a little bit.

## 01:17

But all these things impact the reactivity. The other thing that impacts the reactivity is,

## 01:23

of course, the fact that we are depleting the fuel. The amount of U-235 goes down in time.

## 01:30

And what we want to do today is understand how to quantify that, how to model that.

## 01:34

And along the way, we'll discuss depletion and this concept of

## 01:39

burn.

## 01:39

And then how it all impacts the reactivity. And then in the next lesson, we'll take sort of the

## 01:47

last thing that we discuss in this lesson and put it to use to understand why commercial power
plants

## 01:55

are refueled on the schedules that they tend to be refueled, right? And we'll also understand

## 02:00

something about can-do reactors as used in Canada, where the refueling is essentially

## 02:09

continuous.

## 02:09

And we'll see how to understand all of that in the next lesson. It should be pretty fun.

## 02:16

So what is depletion, right? Before we dive into anything, I want to make sure that we're

## 02:21

on the same page. So depletion refers to the changes, which in this case are primarily

## 02:26

decreases in the number of fuel nuclei in the core as a function of time at some power, right?

## 02:32

So it doesn't mean that all the nuclides go down in concentration, right? We do generate some new

## 02:39

ones.

## 02:39

But the overall trend is we have less fissile stuff, less fissioning is going to happen.

## 02:45

And so we have to account for that in some way.

## 02:49

So the fuel is, of course, composed of actinides. And usually those actinides are just the uranium

## 02:57

nuclides, U-238 and U-235. There are some small trace amounts of U-234 and U-236, U-234

## 03:07

specifically from the enrichment process.

## 03:09

But it's always small. It's important to account for it in practice, but for our purposes,

## 03:15

we can ignore it. Also in practice, we can't just assume that uranium is the only thing of

## 03:23

interest. We know that uranium-238 will eventually turn into plutonium-239. And the way that happens

## 03:29

is that uranium-238 absorbs a neutron and that turns into U-239, which then decays to neptunium-239,

## 03:37

which then decays into plutonium-239.

## 03:39

But that's not the end of the line. There are multiple plutonium isotopes and then above

## 03:47

plutonium is americium and then curium. And we can even go further than that. But in practice,

## 03:53

these 25 nuclides are the nuclides that are accounted for in reactor analyses. For uranium-fueled

## 04:02

reactors or plutonium-fueled reactors, we don't really have to go down to thorium. But there are

## 04:07

concepts that are based on these.

## 04:09

The use of thorium-232, which like plutonium-238, sorry, uranium-238 can lead to the

## 04:16

generation of new fissile stuff. Whereas uranium-238 will eventually transmute into plutonium-239,

## 04:25

thorium-232 will transmute through protactinium to uranium-233, which of course you've seen before

## 04:31

as an exam question where I had you write down the differential equations. And in fact,

## 04:37

you'll get to sort of flesh

## 04:39

that completely out as part of the homework. Now, in addition to these 25 actinides that would

## 04:46

normally need to be accounted for in reactor analysis and practice, there are the fission

## 04:53

products. So we talked about xenon-135, right? It has a huge cross-section. So it is definitely

## 05:00

something worth looking at by itself. But there are other fission products and other things beyond

## 05:05

the actinides, the fuel nuclides that have to be accounted for, right? So if you,

## 05:09

take a look at these sort of small decay chains, we have a number of things that are produced

## 05:15

directly from fission, right? That's what this little down to the right arrow is. And then there

## 05:21

are some capture reactions. Hafnium is something important in some control elements. There's boron,

## 05:27

of course. Because even though this is a large number of fission products, there are some

## 05:32

simulation codes that will lump together some of the other ones, some of the smaller ones,

## 05:37

ones with small yields.

## 05:39

And just lump them together with an effective cross-section and an effective decay constant. But

## 05:44

the big players are listed here, right? So gadolinium, europium, samarium, promethium,

## 05:50

neodymium, cesium, xenon, tellurium, cadmium, indium, rhodium. I like rhodium. Actually,

## 05:57

I did some work for my master's thesis related to fission products and their impact on reactivity

## 06:02

or uncertainties in reactivities. And one of my focus nuclides was rhodium-103.

## 06:09

If you have some, it's worth more than platinum related chemically. But anyway, that's just a

## 06:15

factoid. So lots of things that we would have to consider. And if you wanted to do a sort of

## 06:20

complete analysis, you'd have your 25 actinides, you'd have your several dozen fission products.

## 06:26

And what does that look like? It's a massive set of coupled first-order differential equations,

## 06:32

totally doable with computational tools, right? We could use ODE int from SciPy. And as long as

## 06:38

we have the input to the input, we could use ODE int from SciPy. And as long as we have the input to

## 06:39

data, it's fairly straightforward. Some of that data is not super easy to get, right? Because

## 06:45

part of it is cross-sections. And we've already seen that there's an effort to be made to get

## 06:50

appropriate cross-sections. Decay constants, things like that are there. Fission yields are

## 06:55

there. But it's still an effort to get it all together, right? So for our purposes, we're trying

## 07:00

to understand reactive physics at sort of the big picture level. So it's much more useful to whittle

## 07:07

all of this stuff down to sort of the very beginning. And I think that's a really good

## 07:09

idea. And I think that's a really good idea. And I think that's a really good idea. And I think

## 07:09

that's a really good idea. And I think that's a really good idea. And that's what we will be doing.

## 07:13

Okay. So for treating these actinides, the fuel nuclides, we need a simplified depletion model.

## 07:19

And we're going to adopt the one that's in the book. And what that model does is makes several

## 07:25

assumptions that greatly simplify the equations that we ultimately have to solve it up, basically

## 07:31

makes the solution, I would call it trivial. Okay. So the very first approximation is that

## 07:37

we're going to track only the solution. And we're going to track only the solution. And we're going

## 07:39

to track only uranium-235, uranium-238, and plutonium-239. And we're going to ignore their

## 07:46

decay. Their half-lives are very, very large relative to the timeframe of a reactor operating.

## 07:53

So that's the first approximation. The second approximation is that the plutonium-239 is

## 07:59

produced directly and immediately from uranium-238 capture reactions. We saw before in the actinide

## 08:07

chain that uranium-239 is produced directly and immediately from uranium-238 capture reactions.

## 08:09

So that's the first approximation. The second approximation is that the plutonium-238 would

## 08:10

absorb a neutron, turn into uranium-239, which would decay to neptunium-239, which would decay

## 08:17

to plutonium-239. Those decays are important. If we wanted a very detailed picture in a small

## 08:23

period of time, we'd have to account for it. But the half-lives are short enough that it doesn't

## 08:29

really matter when we're talking about months or years, which is sort of the timeframe of interest

## 08:36

when we're doing depletion calculation. So we're going to look at the half-lives. And we're going to

## 08:39

assume that the plutonium-239 is produced directly when the uranium-238 absorbs a neutron.

## 08:46

The third approximation is that the amount of uranium-238 is so large that the losses from

## 08:52

absorption are negligible. Now, this is a pretty significant approximation and one that does make

## 09:00

our life a lot easier. Is it a good approximation? Well, it turns out it's not bad, especially for

## 09:06

light water reactors in the timeframes that we're talking about.

## 09:09

You do lose a little bit of uranium, but uranium is not really contributing to the reactivity.

## 09:15

It's there primarily to produce plutonium when we're doing the transmutation. So this is an

## 09:23

important approximation. It's good. It's essential that you understand that it's being made, but

## 09:29

we'll appreciate it when we get down to solving the corresponding equations.

## 09:35

All right. So what the model looks like after

## 09:39

all these approximations have been made is the following. I've summarized here some of the

## 09:44

equations from the book, where I have arrows on the left going from the differential equation to

## 09:49

its solution in the box. I've also put the equation on the right that represents the

## 09:55

differential equation with an arrow to sort of the final result. And so the equation for uranium-235

## 10:02

is a very straightforward differential equation. We can directly integrate it,

## 10:08

just like we had done for uranium-235. We can directly integrate it, just like we had done

## 10:09

for decay and such. And then for uranium-238, this approximation that its number or number density

## 10:19

is unchanging basically just gets rid of the differential equation in the first place.

## 10:24

And then the more complicated one is the plutonium-239, but you've seen the same kind of

## 10:30

form before. You've solved this kind of equation before. And so a couple of things to note about

## 10:36

these. I've changed the

## 10:39

equation slightly. In the book, the author uses for uranium-235 and uranium-238 the labels

## 10:48

2,5 and 2,8. And for plutonium, he uses 4,9. This is a scheme that was used back in the

## 10:56

Manhattan Project, and it was used primarily for secrecy. And it's just kind of been used

## 11:03

in practice by some folks since that time. I think it's kind of confusing, right?

## 11:09

The reason or where the numbers come from is the 2,5 is the 2 from 92, the atomic number of uranium,

## 11:17

and then the 5 and 8, which are the last numbers of the isotope number or mass number. And then

## 11:22

for plutonium, Z is 94, so you have 4, and then it's plutonium-239, and you take the 9.

## 11:29

It's nice shorthand. It makes it kind of compact, but I don't like it.

## 11:34

So you can use it if you want. I'm going to use something that's a little bit more explicit.

## 11:39

And so I write out U-235 and U-238 and PU-239. The other thing I'll point out are the cross

## 11:46

sections that we're using. When we're talking about the destruction of a nuclide, we use the

## 11:52

absorption cross section with the subscript A. When we're talking about transmutation,

## 11:57

we have to be careful because not all absorption will lead to the transmutation. Absorption

## 12:02

includes fission. So uranium-238 could fission, but when we're talking about its

## 12:09

inversion into plutonium-239, we have to use its gamma cross section. Okay, and that's, that's

## 12:15

why we see that there. So this is the model we're going to use for our uranium-fueled reactors.

## 12:21

And to get going, we'll start with an example. We'll consider 4% enriched U-2 fuel

## 12:28

and we want the number densities of the plutonium and uranium as functions of time. We're gonna

## 12:34

assume a flux of 10 to the 14, and the following cross sections. In fact, if you're doing the

## 12:37

wholeлавium-239 cross-section, you're going to think about the number densities of uranium-239.

## 12:38

And you want to get the number densities of the plutonium and uranium as functions of time. And we

## 12:39

the table. Now, you'll notice that those cross-sections have a lot of digits, right,

## 12:42

which means it's not out of the book, and that's exactly right. I used OpenMC with our unit cell

## 12:49

models to compute these one-group cross-sections. This is an important distinction. When we're doing

## 12:55

the transmutation that we are here, where we're depleting the uranium, we're using a total flux,

## 13:01

right? This is the flux integrated over all energies. That means that the cross-section

## 13:05

that we couple with that flux to get a reaction rate has to be the appropriate

## 13:09

effective cross-section averaged with the corresponding flux spectrum, right, phi and v.

## 13:18

We could use the cross-sections in table 3.2, right, which are given for thermal,

## 13:26

intermediate, and fast neutrons, but we'd have to come up with some way to weight them, right?

## 13:31

We'd have to know what the thermal flux is, the intermediate flux, and the

## 13:35

fast flux, and we did a little bit of that several weeks ago when I had you construct a

## 13:41

flux spectrum using the Maxwellian, the 1 over e, and then the fission spectrum, right? That was
kind

## 13:46

of not a pleasant task when it came down to it, but we could do it. So instead of doing that,

## 13:53

I just used OpenMC, and I averaged the cross-sections over the entire energy, right? And so that's
what

## 13:59

we're using here. Now, keep in mind that that means that these effective cross-sections are

## 14:04

coupled with the total energy. So that's what we're using here. And so that's what we're using here.

## 14:05

When we get to using the four-factor formula, the cross-sections that show up in, say,

## 14:11

thermal utilization or the eta, the reproduction factor, those are thermal cross-section values. So

## 14:17

those are averaged between, you know, 10 to the minus 3 and 1 e v. The cross-sections that we see

## 14:23

here are averaged from 10 to the minus 3 up to 10 n e v, right? It's a big difference, right? And

## 14:29

it's a distinction that you have to keep in mind. That's a very important aspect of reactor physics,

## 14:35

right? We're doing it in practice, real-world problems, or here in the classroom. So once we get

## 14:41

those number densities, we'll plot them over one year of operation, right? So we'll start things

## 14:47

off. We'll get the computational tools ready to go, numpy and matplotlib, and then I'll enter the

## 14:54

cross-sections from that table along with the flux, and then I'll compute the number densities,

## 15:02

right? So we can get these directly from the

## 15:05

composition of the fuel. And once I have that, the number of 235 that I have at any point in time

## 15:15

is something I can write down immediately. And so that's what I have here. The one thing to note is

## 15:21

the cross-sections are given in units and barns, so I have to make sure to put the 10 to the minus

## 15:26

24. Otherwise, my answer is going to be totally wonky, and we don't want that. So let's go ahead

## 15:33

and define this cell. And if I want to get the gamma,

## 15:38

right, gamma, cross-section for uranium 238, I have to make some sort of assumption. Now the

## 15:43

assumption I'm making here is that the total absorption cross-section for uranium-238 is

## 15:48

equal to the capture plus the fission. So I'm just going to subtract away the fission. And with
that,

## 15:57

I can compute the number density of the plutonium 239, right? And that's given here. I really like

## 16:04

the use of these Greek symbols. That's something that I've, in all the years that I've used Python

## 16:11

nuclear stuff with all of these Greek symbols. I never knew that you could do this, right? So

## 16:16

it's super cool that Python lets you use the full set of Unicode characters rather than just Latin

## 16:23

alphabet and numbers and basic symbols. All right. So we have those number densities. And

## 16:30

what I'm going to plot here is actually not the number densities directly. I'm scaling it by the

## 16:35

number density of uranium-238. So what this effectively gives us is sort of like an atom

## 16:42

fraction of actinides, right? Because most of the actinides are the uranium-238. So this just scales

## 16:48

it a little bit. It scales it nicely. And so there it is. We can see that at the beginning,

## 16:56

of course, we have no plutonium-239, and it rises pretty quickly on this log plot. And if you look

## 17:03

closely, the blue curve goes down.

## 17:05

Slightly over that year, right? Now, you can compare this to the figure in the book that

## 17:11

has sort of a similar makeup in addition to some other nuclides, some of the other plutonium

## 17:18

isotopes. Now, compared to that, this blue curve doesn't go down quite as sharply. And part of that

## 17:23

is the cross-sections I'm using, right? It's just the simple unit cell. So it's not necessarily

## 17:29

equivalent to modeling a full reactor core. But the general trend that we're seeing here

## 17:33

is exactly what we see.

## 17:35

Cool. Now, there are other ways to describe transmutation. Time is, of course, familiar. But

## 17:47

there are other quantities that might make more sense. And one of them is the fluence. So as I

## 17:53

said, the author had introduced the fluence for some of the equations we've already seen. And

## 17:57

it's actually pretty straightforward. It's just the integral of the flux as a function of time

## 18:03

from the initial time to some

## 18:05

time right now, right? And so what I could actually do is make a small change here. So

## 18:14

the fluence at some time is equal to the time integrated flux from zero up to that time. Now,

## 18:19

if I have a constant flux, well, then the flux pulls out of that integral. And it's just the

## 18:23

integral from zero to t, which gives me t. So phi times t. That's exactly what we have in those

## 18:29

previous expressions, OK? So that's the fluence. And maybe you've seen the fluence if you've had

## 18:34

radiation shift. So that's the fluence. And maybe you've seen the fluence if you've had

## 18:35

shielding at this point. Fluence is something that I've seen in that context, probably more

## 18:41

often than typical reactor physics, OK? The other thing that we can use is burn up. And burn up is

## 18:49

the energy produced per initial unit mass of actinides, right? So in our case, with UO2 fuel,

## 18:56

we would take the entire mass of the UO2 and then take out just the chunk that's the uranium. That

## 19:02

would be our heavy metal basis. So you'll sometimes see that. And then we can use the

## 19:05

words HM, heavy metal, when talking about fuel and the actinides that make it up. So the units of

## 19:13

burn up that are commonly used are megawatt days per kilogram, or it's per kilogram of initial

## 19:19

uranium for a uranium-fueled reactor. Equivalent to that is the gigawatt days per MTU, where MT

## 19:26

is metric ton. And less commonly used is sort of the direct SI equivalent, the joules per kilogram,

## 19:34

right?

## 19:35

But they're all energy per mass. So they're all equivalent in some sense,

## 19:40

and easily converting. You can easily convert from one to another.

## 19:45

All right. So when we saw the nuclides before, we noticed that uranium-235 does go down,

## 19:54

and that plutonium-239 does go up. In reality, the uranium-238 also goes down,

## 20:01

but it would be very hard to see on a plot like that. So this constant assumption,

## 20:05

over that kind of time frame, is not bad. Overall, though, the impact on reactivity

## 20:11

is to cause it to go down. When we're talking about uranium-fueled light water reactors,

## 20:17

the reactors that we have out there, the fuel reactivity goes down with time. And that's because

## 20:24

we're sort of suffering from a net loss of fissile stuff. So even though we're getting

## 20:29

the plutonium-239, the overall amount goes down.

## 20:35

Now, with those number densities of the uranium-235 and uranium-238 and the plutonium-239,

## 20:43

we can write down the multiplication factor. So this is equation 10.39. I've got some notes

## 20:50

on the bottom, but again, notice the cross-sections that we're using. In this case,

## 20:56

I'm putting the subscript T into these sigmas to indicate that they are averaged over the thermal

## 21:04

spectrum, right?

## 21:05

So because we're using the four-factor formula, all of the fast-spectrum stuff is encapsulated

## 21:11

in these two terms, epsilon, the fast fission factor, and P, the resonance escape probability,

## 21:16

right? So the only neutrons that get past these two terms are the thermal neutrons. So that means

## 21:21

that we have to use the appropriate cross-sections, okay? This gets a little bit confusing with the

## 21:28

notation because in the book on page 244, the author points out that the T subscript is dropped

## 21:33

in all of the four-factor-related stuff.

## 21:35

In, in subsequent sections of that chapter. I'm putting it back in here just to make sure

## 21:41

that we're, you know, like, because I think it's clearer to have them in. So

## 21:46

when we get to computing k of T or rho, the reactivity of T, we have to make sure to use

## 21:52

the appropriate cross-sections, okay? So this is the multiplication factor. Remember, everything

## 21:58

that's happening to these nuclides is impacting the thermal utilization, right? Basically

## 22:04

the fraction of thermal neutrality. So if you've got the thermal neutrality,

## 22:05

neutrons that are absorbed in the fuel, and then the number of neutrons produced per thermal

## 22:10

neutron absorbed in the fuel, right, because our fission cross-section is changing. There would be

## 22:16

small impacts to the resonance escape probability because, if you remember, P, or at least the

## 22:23

expression we've used for P, has the number density of the fertile element or nuclide in there, and

## 22:30

that's the uranium-238. But because we're assuming that's constant, then we can also assume that P

## 22:35

is constant. All right, so here's an example. We'll consider the same depletion that we had

## 22:42

done before, getting those number densities of the plutonium-239 and uranium-235, and what we'll do

## 22:50

is compute the reactivity as a function of fluence over that same time period, right? So it was a
full

## 22:57

year with that flux of 10 to the 14, and we'll turn that into a fluence and take a look at how

## 23:03

the reactivity changes. So, of course, we'll

## 23:05

need different cross-sections. For this, we could go to table 3.2, and I urge you to look at how

## 23:12

these numbers compare to the ones in that table. They're a little bit lower, but that's because,

## 23:19

again, this is averaged over the spectrum of our unit cell from OpenMC, so I would call it

## 23:25

slightly more realistic than the numbers that are listed in 3.2. All right, so given these numbers

## 23:31

in the table, and then given these other parameters, and I'll point out that the

## 23:35

I finally know what this pesky symbol is. There's a reason I didn't recognize it, because it's not a

## 23:42

typical Greek symbol. It's actually the character sigma, right, which we've used for microscopic

## 23:48

cross-sections forever, but apparently in the Greek language, that's the version of sigma that

## 23:53

goes at the end of a word or an end of a sentence or something like that. So if we're doing it in

## 23:59

LaTeX, it's var sigma as opposed to just sigma. Anyway, so my computer is running, and I'm going to

## 24:05

use my computer to do that. So I'm going to use my computer to do that. So I'm going to use my
computer

## 24:05

to do that. So I'm going to use my computer to do that. So I'm going to use my computer to do that.

## 24:06

Confusion wasn't because I'm just uneducated. I might be uneducated, but not in this particular

## 24:11

sense. Anyway, I feel better about it. So with these numbers, let's get the reactivity versus

## 24:17

fluence. All right, here are the cross-sections again from that table, and here are the four-factor

## 24:26

values with those other parameters defined. And what I'm going to do first is define k,

## 24:33

and then I'm going to use k in a separate function for rho to keep it kind of

## 24:37

clean. And so I've defined the numerator of that expression for the multiplication factor,

## 24:43

right? We've got our fission terms, and then we have the four-factor terms that are remaining

## 24:49

along with that non-leakage probability. And then on the bottom, we have all of our absorption,

## 24:53

where I'm making sure to use the full absorption cross-section, not just the captured cross-section.

## 24:58

Okay. And that's that. Okay. So we've got these functions, and

## 25:06

let's go ahead and plot it. So the fluence is easy. We can take the same vector of times that we

## 25:13

produced before, multiply it by the flux. That gives us the fluence. And so the reactivity

## 25:19

as a function of fluence looks like this. And so we see at the beginning, our excess reactivity

## 25:25

is something like 0.3. So that's very reactive. And then by the end of this

## 25:35

time period, we're going to have a function of 0.3. And so we're going to have a function of 0.3.

## 25:37

It has dropped to 0.2 or so. Once we have this, we can actually explore it a little bit more. So

## 25:45

I'll basically redefine times, and I'll say that times now is np then space. And we'll start off

## 25:54

at 0. I'll do 365 days per year, 24 hours per day, 3,600 seconds per hour. Or I could just do

## 26:07

0.3. And then I'll say that times now is np then space. And we'll start off at 0. I'll do 365 days

## 26:07

per year, 24 hours per day, 3,600 seconds per hour. Or I could just do 0.3. And then I'll say that

## 26:07

pi times 10 to the 7. If you didn't know, this number should compute to something like 3.15 times

## 26:13

10 to the 7. So the number of seconds in a year is pi times 10 to the 7. Factoid for your next

## 26:19

cocktail party. But I'll take this and actually expand it over three years. So I'm redefining

## 26:24

times. And so what I want to see is what happens to rho over three years. And we can see that

## 26:32

it goes down below zero. So roughly, where does it hit?

## 26:37

the zero axis? About two years. Now, if you think about it, if this fuel and this reactivity is

## 26:44

even remotely close to what the typical reactivity of, say, Wolf Creek's fuel is,

## 26:51

if we just put it into the reactor and operate it at this flux, which should be close to the

## 26:56

total flux of a system like that, we're going to run out of reactivity after two years.

## 27:02

Okay. Obviously, earlier in the class, I had said that fuel sticks around in the reactor for a total

## 27:09

of five years. So something's obviously a miss here, because if I go down to a reactivity of

## 27:14

zero, there's no way I'm going to keep it in the core, right? I'm not going to be able to

## 27:18

keep my reactor critical, right? If I have no more excess reactivity, there's nothing left for me to

## 27:25

do. This is where the topic that we cover next time comes in, the linear reactivity model.

## 27:32

So

## 27:32

I'll point out is this reactivity curve, it does have a slight curve to it. And the reason it has

## 27:39

more of a curve than, say, a line would suggest is mostly because we're neglecting some of those

## 27:46

other features, right? The buildup of other actinides and the fact that the uranium-238

## 27:52

is decreasing. But to a good approximation, this reactivity as a function of time

## 27:58

will look like a line with a negative slope.

## 28:02

And that's exactly what we'll cover next time. And then with that linear reactivity,

## 28:07

there's a model that lets us understand how the reactivity of a core that is made up of

## 28:13

different fuel batches. And so even though a fuel assembly might go into the core

## 28:19

for, say, a cycle, and a cycle is maybe a year and a half, it's not removed completely

## 28:27

after that time. It's actually kept in for another two cycles, three cycles total.

## 28:32

So which adds up to just about five years. And so by averaging the reactivities of multiple

## 28:38

batches, we can end up keeping the reactor critical for a much longer period of time,

## 28:42

which also increases the amount of energy that the fuel can produce, right? So it increases the

## 28:48

burnup of the fuel, which is good for pocketbooks, as it were, of the producers.

## 28:57

So food for thought. We're not going to go into detail, but I want you to think about this.

## 29:02

If the reactivity is declining, as we see it does, and our fissile nuclides are declining,

## 29:08

what happens to the fission rate in time if our flux is fixed, right? So for our flux of 10 to the

## 29:15

14, we know that the fissile nuclides, uranium-235 and plutonium-239, on the average,

## 29:22

their combined impact is going down, right? Well, that means the fission rate goes down.

## 29:31

And if the fission rate goes down,

## 29:32

the power goes down. And if the power goes down, well, then our reactor is not operating

## 29:37

at a constant power. What does that mean? Well, that means that as a function of time,

## 29:44

as these fissile nuclide densities are decreasing, the reactor flux actually has to increase,

## 29:51

right? And if the flux increases, that compounds in all of this depletion makes it harder,

## 29:56

right? Especially if we're doing it in some sort of nonlinear way. But

## 30:02

there's a little bit more to all of this than just this simple model that we're adapting from

## 30:08

the book, all right? So we'll talk more about this in the reactivity, in the linear reactivity

## 30:15

model in our next lesson. See you then.
