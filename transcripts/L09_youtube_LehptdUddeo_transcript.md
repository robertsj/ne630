# L09 Local Audio Transcript

Course: NE 630

Playlist source: https://youtube.com/playlist?list=PLy481lNHlnHoEO95vM-xYX2bydD25v20L

Video: NE 630 - Lesson 9

URL: https://www.youtube.com/watch?v=LehptdUddeo

Video ID: LehptdUddeo

YouTube upload date: 20230911

Duration: 56:01

Transcript source: Local faster-whisper transcription from YouTube audio.

Whisper model: large-v3; detected language: en.

Generated: 2026-06-28

Note: This transcript is machine-generated from audio and lightly wrapped only. It should be reviewed before being quoted, published, or used as polished lesson text.

Requested language: en

## 00:00

Those slides, she said she could go up and I don't know what we're going to do.

## 00:07

The answer is don't have any problems for like 30 minutes.

## 00:15

That's impossible.

## 00:16

Like 30 minutes.

## 00:17

That's impossible.

## 00:18

Whatever, go to the house.

## 00:19

Yeah.

## 00:22

Alex might hope that.

## 00:29

That one, I took advantage of that one.

## 00:32

All right, let's go ahead and get started.

## 01:07

Last week, Friday, we had discussed the first bit of chapter three in the textbook, which was our
discussion anyway, was primarily focused on this quantity data, which I had called, at least in
passing, the reproduction factor.

## 01:26

But what it represents in plain English is the expected number of neutrons emitted from fission per
neutron absorbed.

## 01:36

Specifically for neutrons at a particular.

## 01:38

Value of E, right?

## 01:40

Neutrons with certain energy.

## 01:41

So what we saw from that, the image of that from the cross-section data is that thermal spectrum
reactors rely on slowing the neutrons down to where this factor eta is large in the thermal region,
right?

## 02:00

Where the fission cross-section of uranium 235, for instance, is quite large.

## 02:04

Fast spectrum reactors.

## 02:06

Also want to avoid the resonance.

## 02:09

Regime, right?

## 02:10

This, this epithermal energy range between about one EV and 0.1 MEV, right?

## 02:16

Where we have all these large resonances and it does so a fast spectrum reactors do so, or those
designs do so by avoiding scattering as much as possible in the first place.

## 02:25

Okay.

## 02:25

They're very different ways to avoid the resonance.

## 02:29

One is just not to go through it at all.

## 02:31

And then, uh, thermal spectrum reactors are let's get through it, but as quickly as possible, right?

## 02:37

And this few collisions as possible.

## 02:39

All right.

## 02:39

So all of this discussion so far is in the context of what I called an infinite homogeneous reactor.

## 02:45

The easiest analysis that we can do with the data that we have in a class like this is to ignore as
much of the physics as possible, right?

## 02:55

Keeping just the bits that we need to, to really understand what's happening, um, in this case, in,
in terms of energy, right?

## 03:03

So what we're doing is eliminating anything to do with space, anything to do with time.

## 03:08

We've already sort of just eliminated everything to do with the angle you'd have to take my 800
level of neutronics class.

## 03:16

If you want to talk about neutrons, if you think about a neutron, it's going through life with an
energy, right?

## 03:20

Well, it also has a speed, but you could combine those two and you have a velocity.

## 03:24

And so that means that not only has a position as an angle, right?

## 03:27

And there are ways to quantify that for our purposes.

## 03:31

We're just going to pretend I never talked about angle, right?

## 03:34

And so for today, and then for the next few days, all we're going to care about.

## 03:38

Okay.

## 03:38

Are, uh, the dependencies on energy.

## 03:41

Okay.

## 03:42

And so what we'll do today is, uh, review a little bit about reaction rates.

## 03:47

That's the concept of reaction rate should be familiar to you.

## 03:50

We're going to use that along with something called the slowing down equation to, uh, provide an
approximation for the bass spectrum.

## 03:58

And then also for the spectrum of neutrons in a thermal spectrum reactor in that nasty range with
resonances, only are we going to do it the simplest way possible?

## 04:08

We're going to skip the fact that there are resonances there at all.

## 04:11

So all we're going to care about are the physics of the neutrons slowing down.

## 04:14

And we already have the tools for that because we know all about the probability that a neutron
elastically colliding with a nucleus will go to some other energy.

## 04:22

We're going to let that happen over and over again, and kind of build up a picture of what the
neutron density or really the neutron flux looks like between say an EV and 0.1 MeV.

## 04:34

What we'll do then next time is bring back the resonance absorption.

## 04:38

We'll talk about something called the resonance escape probability, which is, if you remember from
my 495, anyway, one of those important four factors in the classic four factor formula.

## 04:49

All right.

## 04:49

So, uh, any questions from last time I did, uh, propose sort of, uh, an informal homework or
intellectual exercise or something for those who are here.

## 05:05

Anybody remember what I asked the very tail end?

## 05:10

The very last.

## 05:11

Thing that we were talking about were moderators, right?

## 05:13

And we had already covered the, the idea of moderation in the previous, uh, chapter with this C, the
Greek letter C, the average logarithmic energy loss, right?

## 05:25

Um, moderators in general for thermal spectrum reactors have to be good at doing what?

## 05:33

Slowing down, slowing down neutrons.

## 05:35

And it's not just about the energy loss.

## 05:37

And you also have to have a large cross section so that the interaction rate is high.

## 05:41

But then you also need a low absorption cross sections so that if a neutrons, uh, interacting with
the thing that scatters well, it's not going to suffer absorptions at a high fraction, right?

## 05:52

So you, you want to have low absorption, high scattering cross sections, so that interaction rates
are high and then also a large energy loss, right?

## 06:00

That, that makes the perfect, uh, moderator.

## 06:03

So most common one is it's hydrogen by way of regular old water.

## 06:08

Why it's cheap.

## 06:10

We know it.

## 06:11

It's a.

## 06:11

It's a good engineering fluid, right?

## 06:15

It's it's good.

## 06:16

I mean, like when you, what normalized the cost, it's great.

## 06:19

D two O deuterium, heavy water is even better, right?

## 06:24

Because the absorption cross section of a deuteron is significantly less than for hydrogen, right?

## 06:29

Graphite is also good because it has a low absorption cross section.

## 06:33

It turns out that D two O and graphite with those moderators, you can create a reactor based on.

## 06:40

On.

## 06:41

In.

## 06:41

Enriched few, uh, fuel, right?

## 06:43

So you dig uranium out of the ground, you get it into its metallic form, make it UO two.

## 06:47

You can make a reactor with D two O and graphite, either one of them, but not with water, right?

## 06:53

And the reason is the water just absorbs too much of the neutrons itself, right?

## 06:59

It's not a huge amount, but it's just a sliver, right?

## 07:01

So you can never hit criticality.

## 07:03

But what I ask you to do is think about, look at the periodic table, think about the things that
make good moderators.

## 07:11

In general, if you want, uh, large energy loss, what, what does that say about the mass of the
moderating nucleus?

## 07:19

The opposite, right?

## 07:21

Yeah.

## 07:22

You don't want to use a big billiard ball or I, sorry, I like U two 38 because the billiard ball
kinematics would be like, what happens if I hold a basketball and I throw a golf ball at it?

## 07:33

What happens to the golf ball?

## 07:37

It flies back in your face, right?

## 07:39

That's what would happen with a neutral.

## 07:40

You throw it at.

## 07:41

With a certain energy, it's going to bounce back at you with just about the same energy.

## 07:44

That big old basketball is not going to take our bowling ball, right?

## 07:48

Not going to take away a lot of energy.

## 07:49

That's the key thing here.

## 07:52

Whereas on a billiards table, you hit the cue ball, you smack it right into the four ball dead on
what happens to the cue ball?

## 08:01

It stops.

## 08:02

That's a neutral on losing all of its energy interacting with hydrogen also of equal mass, right?

## 08:06

So that's a good, good graphical picture.

## 08:08

So you want light things.

## 08:10

So if you go through the.

## 08:11

Periodic table, we have already got hydrogen, right?

## 08:15

And it's deuteron, okay?

## 08:17

You go next on the periodic table, you have helium while helium is good.

## 08:20

But what's the problem with helium?

## 08:23

Yes, it's a gas, it's expensive.

## 08:25

It's a gas.

## 08:26

And even though it, it would lead to a good energy loss per collision and maybe it's microscopic
cross section for scattering is not bad.

## 08:36

It's macroscopic cross section is going to be low because it is a gas.

## 08:41

You cannot make the density of helium large enough for it to be a useful scatterer, right?

## 08:47

And then you go circle back to the number three.

## 08:51

What's number three on the periodic table?

## 08:54

Lithium. Lithium is nasty.

## 08:57

Lithium also has a large cross section.

## 08:59

Lithium is a great way to to to sense thermal neutrons because you get this.

## 09:06

It's I believe it's an alpha reaction, right?

## 09:08

So pretty big absorption cross section.

## 09:10

So that deletes it.

## 09:11

What's the next one over?

## 09:13

Brilliant. So brilliant meets all the requirements.

## 09:17

It's pretty low in mass.

## 09:19

It's better than graphite in that sense.

## 09:21

Okay, so you lose a lot of energy.

## 09:23

It has a pretty good scattering cross section.

## 09:25

It's absorption cross section is low and it's a fairly stable metal with a high melting temperature.

## 09:32

It's often found in something called barrier, the brilliant oxide.

## 09:37

Okay.

## 09:37

It was looked at in the fifties for.

## 09:40

Nuclear propulsion, like for space propulsion and stuff, right, because it could be cast in these
forms that were really good for temperatures, to be completely honest, I have no idea why research
on it kind of went on, went away, right?

## 09:54

Why it hasn't like I know it's been used or proposed in designs, but it never took off in the same
way that heavy water graphite and regular water did.

## 10:02

So if you're curious about it, look into it and school the rest of us, right?

## 10:07

Anyway, enough about that.

## 10:09

Let's move on to what?

## 10:10

Today's topic is all right, so there are a number of definitions in this particular chapter, and in
our reading for today that I want to make sure that we're all on the same page.

## 10:23

The notation is not necessarily universal right in the sense that you might go to another textbook,
and it might be labeled a little bit differently.

## 10:30

For instance, Lewis uses the triple prime for a volumetric quantity for these densities.

## 10:37

It's similar, I suppose, to what we would see in a.

## 10:40

Typical mechanical classes where a triple prime will mean like you would use that for like a heat
generation rate or something, a volumetric heat generation rate.

## 10:48

But in any case, when you see the triple prime, I think we're supposed to think that that's like a
centimeter cubed sort of volumetric density in general.

## 10:58

He has a tilde here on this one, and I think that associates with it being a function of E, where
this one is just a number.

## 11:06

Okay, So what are these things?

## 11:09

The very first.

## 11:10

The very first one is what is called the neutron density distribution.

## 11:25

Okay, what units does this have?

## 11:37

So it's a density.

## 11:40

Yeah, so we're going to have so I'll be explicit I'll put neutrons per centimeter cubed.

## 11:46

Okay.

## 11:48

What else do densities have a time dependence.

## 11:53

Okay.

## 11:54

No, it's like a snapshot in some some unit volume of the number of things that we're keeping track
of.

## 12:01

Okay, so it's centimeters cube, but specifically because this is a function of energy.

## 12:06

It's also per TV.

## 12:10

So that's where the distribution in its name comes from so it's neutrons per centimeter cube per EV
right so usually in a class like this, and it's certainly in later ones.

## 12:22

Right.

## 12:23

And so we're going to have to discuss things in terms of a phase space, but we're used to geometric
space Cartesian space where we're in a DX or in a DV.

## 12:34

When we're in this land and we have multiple variables, potentially in play like energy, then we
also have to talk about the energy, part of that base space like I know that I have a certain number
of neutrons between x and D, x plus dx, but now I have to care about

## 12:47

the neutrons between energies, e and energies, e plus de.

## 12:50

Right.

## 12:51

So it's the same thing for angles we care about angle for time if we cared about time, etc.

## 12:57

So, this is the neutrons per centimeter cubed per TV.

## 13:01

All the.

## 13:03

This one represents is the neutron density that has been integrated over all the energies right so
that would actually be closer to our number density for the number of atoms in a table, right we've
integrated over energy and so the units would have to be neutrons.

## 13:24

Right.

## 13:25

So, this is the neutrons per centimeter cubed.

## 13:27

Remember I'm being pedantic here.

## 13:30

Most often I wouldn't bother writing the neutrons, I would just have one per centimeter cubed, etc.

## 13:37

Okay.

## 13:38

What is this thing.

## 13:44

The flux.

## 13:46

Right.

## 13:48

Make sure I get all the nomenclature in the book.

## 14:00

So, this is the neutron.

## 14:02

Flux.

## 14:05

In the book, I believe he also adds on distribution to that, which is something that I probably
won't because I'm just so used to calling it the neutron flux can call it the neutron flux spectrum,
as well, where spectrum or distribution indicates that there's a dependence

## 14:23

on E. So usually these functions of E, that will be discussing today we're trying to get the fast
spectrum the intermediate spectrum of neutrons in the reactor.

## 14:32

Okay.

## 14:33

So, spectrum is just the probability distribution of neutrons as a function of energy so when I say
spectrum, you can think of it as being distribution.

## 14:41

Okay, so got that and what are the units of the flux.

## 14:45

When written like this as a function of energy.

## 14:53

Okay, what's the first one that you think of for a flux.

## 14:57

The spatial component.

## 15:00

Yep.

## 15:01

You know, per area.

## 15:03

Okay.

## 15:04

Flux means time dependence right so it's things per.

## 15:06

Things per area per time and then this would also have to have the EV dependence.

## 15:14

Okay.

## 15:16

And then,

## 15:26

tried looking up how to make this cursor bigger but there's apparently no way to do it.

## 15:33

Okay. So, we've also got this in which you'll find is not used in the book but I'm going to
introduce it to help keep everything clean.

## 15:41

When I say r sub x.

## 15:43

What I mean is a reaction rate for some reaction x for x you can substitute in any of the reactions
that we've talked about right so x could be.

## 15:53

It could be scattering, where, if I use as I'm probably referring to elastic scattering, at least in
the energy range that we care about today that's the only thing that will worry about.

## 16:04

It could be an gamma, right.

## 16:07

Radiative capture fission, etc.

## 16:09

So it's any of these reactions, or I could be talking about the total interaction.

## 16:11

Right.

## 16:12

Which I would have.

## 16:16

A T.

## 16:18

Right, and we'll see that in a little bit.

## 16:20

So, this is a reaction.

## 16:24

Right.

## 16:26

And because it is a function of E, this would be reactions of type x per centimeter cubed.

## 16:40

Per second per.

## 16:42

Okay.

## 16:46

What is the definition, or how do I construct a reaction rate.

## 16:50

Do you remember what product represents a reaction rate.

## 16:58

If you look at this thing here per centimeter squared second Ev.

## 17:02

There's only one factor of centimeters that's, you know, making the difference, where do we get that
from.

## 17:10

Yep.

## 17:12

Right, so this is equal to a flux.

## 17:16

In energy times, whatever the reaction cross section is right and so this has units of per
centimeter.

## 17:29

Alright so it is very very important that you keep these these symbols the mathematical symbols and
their interpretation along with their units straight. Okay. So, most often in reactor analysis, we
use the flux because it is the most natural way to react.

## 17:47

The physical quantity.

## 17:49

Right, a flux is not a physical quantity right it represents something about a physical quantity the
physical quantity, or the number of neutrons in some region of space space right the density of
neutrons, but it's much more convenient to use the flux.

## 18:03

And just to kind of get our juices flowing a little bit anymore. Let's, let's take a look at
converting between a flux and a density.

## 18:17

So, let's suppose that.

## 18:19

We have some neutron flux in a reactor and specifically at an energy of 0.0253 Ev.

## 18:25

The flux is 10 to the 12.

## 18:27

What I want is the corresponding density of neutrons at that energy.

## 18:33

I worked out the a little bit of the math for you.

## 18:37

The velocity or speed as a function of energy is approximately given by this thing.

## 18:42

Okay, so go ahead and spend just a couple of minutes and figure out what n must be.

## 18:47

Now.

## 18:49

And then I'll work through it myself.

## 18:58

Although pull of hands anybody know what that speed ought to be.

## 19:07

Yeah, right.

## 19:09

I mean with my approximation, it'll be off by a decimal point or something like that but yeah that
that's the is equal to 2200 meters per second, or, or 2200 add two zeros centimeters per second
because that is a little bit more.

## 19:27

A little bit more useful so good.

## 19:30

That's the easy one to remember, right, because it corresponds to that energy point 0253 Ev, which
is the energy of a neutron and thermal equilibrium as room temperature, which is something that
we'll talk more about on Friday.

## 19:54

Anybody have that density value.

## 19:58

Because you need a calculator for that.

## 20:01

Actually took out my hand calculator this weekend because I'm sitting away from my computer.

## 20:05

I was so pissed. I have this computer at home I take it back and forth, but I set it up with a
keyboard and mouse, or whatever reason my mouse was glitching.

## 20:14

And so I ended up having to use this wireless keyboard that has built in track that or you know how
track that's socket right so like I just walked away I couldn't handle it.

## 20:23

Right, so that density in check.

## 20:30

0.0253 Ev is equal to what my flux is 10 to the 12.

## 20:36

10 to the 12 over the 2.2 times 10 to the five centimeters.

## 20:43

I get that right 245 Yep.

## 20:46

And this is approximately equal to 4.55 times 10 to the six per centimeter cubed per Ev.

## 21:02

Thanks.

## 21:08

There's something that should be clear.

## 21:10

Is if I have that same.

## 21:10

Flux value at a different energy, the corresponding density will be different.

## 21:16

Right. So if I were to go from if I had this flux of 10 to the 12 instead of being at this thermal
energy.

## 21:24

If I had it instead at one Mev or something like that, the of course, going up in what would that
assist?

## 21:32

That would be about 8 orders of magnitude and energy.

## 21:36

The square root will take care of 4 of those orders of magnitude.

## 21:40

But the density will be different by 4 orders of magnitude.

## 21:44

So when you get to the final exam, and I ask a question like, here are the thermal and fast fluxes
in our trigger reactor.

## 21:52

How many thermal neutrons are there in the reactor versus how many fast neutrons are there right?

## 21:58

It's easy enough that the fluxes tend to be roughly the equal right?

## 22:02

It's not quite one to one for fast to thermal.

## 22:06

But the numbers of neutrons at those.

## 22:08

In those energy regions differs considerably right because of this speed.

## 22:14

So keep that in mind. All right.

## 22:19

So now we know about the fluxes, the densities, reaction rates, and so forth.

## 22:26

Our goal now is to come up with a balance equation that represents neutrons in this infinite
homogeneous system.

## 22:35

Right. So certainly in the context of the latter part of today and next time,

## 22:40

the equation is probably best called the slowing down equation.

## 22:44

That doesn't mean that the only process we care about is slowing down, at least for today.

## 22:48

And then when we get to Friday, a better way to describe the equation that will come up with might
be the neutron spectrum.

## 22:59

Equation right where we are aiming to find a fee as a function of energy.

## 23:05

Right. But in the book it's called the slowing down equation.

## 23:08

So I'll use that as well.

## 23:10

So at the end of the day, what we're looking for is how does the density as a function of energy
change in time?

## 23:19

Ultimately, we don't want it to change in time.

## 23:21

We want a steady state balance. But when we come up with these conservation laws,

## 23:25

it's almost always represented first as a time rate of change where we have gains balanced by loss.

## 23:31

And if this is zero, then we have gains exactly equal to the loss.

## 23:35

It's not driving some change. So when we have these gains and losses,

## 23:39

they'll show up as some sort of reaction rate.

## 23:45

Why reaction rate? Well, if we're an infinite system, we don't have boundaries.

## 23:50

So we don't have neutrons that are just leaving the system.

## 23:54

Right. Which is a way of losing neutrons. That is a loss rate.

## 23:57

And we will find a way to mathematically describe that in the last third of the course when we do
spatial diffusion.

## 24:03

So everything else, though, is just going to be a reaction.

## 24:08

We're not going to have things decaying away. We're not going to care about time right now.

## 24:12

So everything is just going to be some sort of reaction.

## 24:14

So it would be a flux times a cross-section, possibly integrated over some range of energy.

## 24:19

You can imagine neutrons at one energy will come to our energy of interest.

## 24:24

And there are lots of those other energies. So we'll want to maybe integrate over it.

## 24:28

But losses and gains, the losses is actually the easiest one to do.

## 24:34

If I care about a neutron or the neutron density at an energy,

## 24:38

if I'm a neutron at that energy in my infinite system,

## 24:43

what are the ways in which I can be removed from that E to E plus D E range?

## 24:50

If I'm at energy E, what sort of process takes me away from that energy,

## 24:55

therefore being a loss from the number of neutrons that sit at that energy?

## 25:00

What's that? Really? Any interaction? Any interaction.

## 25:03

That's why this is easy, because we have a nice product of two things.

## 25:07

That represents the rate at which neutrons are interacting at all.

## 25:12

It's a flux, of course. So the losses will be a flux.

## 25:20

And because this is a reaction rate, we need a cross-section that represents any possible reaction.

## 25:30

What cross-section is that? The total, right?

## 25:34

The rate.

## 25:42

The rate at which neutrons are interacting and thus leaving the energy E.

## 26:04

There are, of course, boundary cases. If I'm elastically scattering,

## 26:07

we know that the range of possible outgoing energies from an elastic scattering event is alpha E all
the way up to E.

## 26:15

So I could, as a neutron, come out of an elastic scattering event

## 26:18

with my energy unchanged.

## 26:20

But then conceptually, you have to think, well, if I didn't lose energy, did I actually touch the
target nucleus?

## 26:27

Right. But it's also an edge case.

## 26:29

And we know that the probability of a single number when we're dealing with a continuum is actually
zero.

## 26:35

So it becomes a non-issue.

## 26:37

So any interaction at all must remove neutrons of this energy from that energy.

## 26:43

Now, of course, some of those interactions won't remove the neutron from the system.

## 26:48

Entirely. It'll just kind of redirect it, put it into a different energy.

## 26:52

That's exactly what elastic scattering does.

## 26:54

So think of that when we get to gain.

## 26:57

What are the what are the ways that we can get neutrons into the system at this energy E?

## 27:02

A fission interaction that gives you a couple more neutrons.

## 27:05

Yeah. So this could be we could get from fission.

## 27:09

Right. So I could have my new.

## 27:13

And I'll put primes here because we won't be quite done with it yet.

## 27:16

Right. OK.

## 27:22

So as written here, we have sigma f times phi.

## 27:26

That is the rate of fissions happening at E prime.

## 27:30

When I multiply it by new E prime, that's the number of neutrons being produced from fission due to
neutrons at E prime.

## 27:38

OK, so that that's that helps. But does that say what energy those neutrons are going to?

## 27:46

Now, when we have neutrons born from fission, they usually emerge at one to two MeV.

## 27:51

But we have a function that represents the actual distribution.

## 27:55

Right. The probability that a neutron born from fission emerges at energy E.

## 28:00

What is that function? Yeah, it's the one that you had to do some nasty numerical stuff with for the
homework due last Friday.

## 28:08

Right. So that that function is chi.

## 28:14

OK, now what chi does is it says, hey, if you're a neutron that's born from fission,

## 28:19

this is the distribution of your energies. So that means that we have to take all of the neutrons
everywhere.

## 28:26

That are inducing fission, take all those neutrons produced from the fission, and then we spread
them out according to the chi spectrum.

## 28:34

So this thing here, the new sigma f phi is only the rate at which fissions are happening at this E
prime.

## 28:42

What do I have to do to this triple product in order to capture all of the fissions happening?

## 28:48

Across all of the energies we integrate over all energies.

## 28:57

Right. So. So we can go from zero to it.

## 29:04

We could do it. I'll keep it sort of simple here. Zero to infinity.

## 29:09

D infinity. Right. So. I'll annotate this.

## 29:13

So this integral is the fission rate.

## 29:17

And then this is the the outgoing.

## 29:26

Going energies. OK, so together, the product of chi times the total fission rate across all energies
gives us the rate at which neutrons born from fission are showing up at this energy E where we're at
defining the neutron balance.

## 29:45

All right. So that's fissions. What else?

## 29:48

What else could take a neutron from one energy to another energy scattering?

## 29:56

Right. And so.

## 29:58

I can write the same basically the same same thing here.

## 30:02

I'll move this over a little bit. OK, so I'll have a scattering cross section and I'll keep it
generic where I'm going from E prime.

## 30:12

So I'm a neutron scattering from E prime to E.

## 30:15

That means my flux has to be at E prime.

## 30:19

Right. OK, so.

## 30:22

For a neutron of E prime, this is going to be the sort of the rate at which I'm scattering the E.

## 30:27

But there are a lot of energies E prime that could land.

## 30:30

Me at energy E. In fact, for now, I'm just going to pretend that all of the energies out there could
lead to energy.

## 30:37

And so I have to do the same thing that I've done here for fission and integrate zero to infinity.

## 30:45

Now, all of these things, they are things that you've seen before.

## 30:57

But you know what chi E is. We talked about nu last time.

## 31:01

And with sig map is just a cross section. We know what a flux is now.

## 31:06

The scattering cross section.

## 31:07

We've dealt with this concept.

## 31:08

We've dealt with this concept of going from one energy to another.

## 31:11

Right. This is if I wanted to break this up into a product, it would be I have a total scattering
cross section for neutrons at energy E prime.

## 31:22

And this would be multiplied by that probability that takes us from E prime to E.

## 31:28

I could do that, too. And I think the book uses that that breakdown.

## 31:31

But it doesn't really matter if you do it this way or this way.

## 31:35

Eventually, we're going to have to invoke that from.

## 31:37

Elastic scattering.

## 31:39

We'll do that in just a little bit.

## 31:41

Okay.

## 31:42

So these are our gains.

## 31:43

Are there any other ways that we can get neutrons into the system at this energy?

## 31:47

The ones that we have so far depend on neutrons that are already in the system, right?

## 31:59

Either a neutron is caused fission.

## 32:01

We get neutrons out of that.

## 32:02

But it started with having a neutron in the system.

## 32:05

What if we put neutrons into the system from some other source?

## 32:12

You could have an external source.

## 32:13

I could put an ambi source into my system and have a constant stream of neutrons entering in.

## 32:18

Right.

## 32:19

So the other thing that we have is some sort of external source at energy.

## 32:25

Right.

## 32:26

So these are our gains and losses.

## 32:28

And when you put them together, you get the slowing down equation.

## 32:32

Okay.

## 32:33

The thing that we'll really care about is, what does this equation look like if things are in steady
state, if things are exactly balanced?

## 32:41

In that case, we would have our total interaction rate balanced directly by my – I'll put scattering
first.

## 33:36

Okay.

## 33:37

So this is my slowing down equation or my spectrum equation.

## 33:44

Now, what I'd like you to do on your time is go back to that course introduction page.

## 33:50

I had a pretty nasty-looking equation on there.

## 33:53

That was the energy-dependent, time-dependent neutron diffusion equation.

## 33:58

What I'd like you to do is take that equation on that page and make the assumptions that we had to
make for this infinite medium reactor, this infinite homogeneous reactor where I said there's no
space.

## 34:10

So if there's no spatial dependence, what does that mean about the argument R, right, the location
of space?

## 34:17

Well, it goes away.

## 34:18

What happens to spatial derivatives like the nabla, right?

## 34:22

The time dependence, the divergence, and divergence, all that kind of stuff, those go to 0, right?

## 34:26

So you get rid of a big chunk of that equation.

## 34:29

And if you don't have time dependence, meaning that you're in steady state, you get rid of the time
derivative.

## 34:35

And what you end up with if you get rid of the R variable in all the quantities, the time where it
shows up, is this equation, right?

## 34:44

So this comes directly from sort of the full-blown representation.

## 34:47

If you remember, one of the key things that we do in a class like this is whittle things.

## 34:51

Is whittle things down to the simplest possible representation that tells us the story that we want.

## 34:56

I want to know how neutrons start off at fast energies and go to slow energies.

## 35:00

I don't need the space.

## 35:01

I don't need the time.

## 35:02

I just need the energy.

## 35:03

And I can do that.

## 35:04

I can either start with the big thing and whittle it down, or we can kind of build from the ground
up like this based on reaction rates.

## 35:10

Although I'd say the same thing is done if you try to build up the whole equation, too.

## 35:15

We just don't have to do that here.

## 35:17

I've got a question.

## 35:18

Yeah.

## 35:19

So.

## 35:20

That external summation you have there at the end of that equation.

## 35:27

This one?

## 35:29

Yeah.

## 35:30

Sorry.

## 35:31

Yeah.

## 35:32

So external sources.

## 35:33

Yeah.

## 35:34

That's the EXT.

## 35:35

Oh, yes.

## 35:36

That's okay.

## 35:37

What would be, like, some examples of that in a power reactor?

## 35:40

Like, I know, like, in our reactor, we have a startup source, which I would assume maybe, like,
that's what you're trying to capture with that.

## 35:48

But what about your power reactor?

## 35:49

Do they have external sources, too?

## 35:51

Yeah.

## 35:52

What would, like, what would be an example of some of those?

## 35:56

I mean, their external source or startup sources could be the same thing that we use.

## 36:01

It could not be, like, an alpha neutron.

## 36:03

So it would mainly just be, like, the startup sources, then?

## 36:06

Yes.

## 36:07

So in a power reactor, in a reactor that we normally want to operate at steady state, that term
doesn't show up.

## 36:15

Okay.

## 36:16

So, yeah.

## 36:17

In the case of a nuclear reactor, what we would have is this thing goes to zero, because if you were
in a critical system, if you keep piling new neutrons in, your population just keeps going up.

## 36:27

That's something that you get to explore firsthand experimentally in a reactor lab.

## 36:33

What's neat is even though this class is about reactor theory and we care primarily about the steady
state operation of nuclear reactors, the mathematics, the models, the physics involved can be used
to model radiation.

## 36:45

So you can just go to a nuclear reactor, and you can see the radiation, the radiation interactions
in basically many other things.

## 36:54

It doesn't even have to be neutrons, right?

## 36:56

The same sort of framework.

## 36:58

This scattering term, this works totally fine if this is not a neutron flux but a gamma ray flux.

## 37:02

The cross sections come from different sources.

## 37:05

They look a lot different, right?

## 37:07

But it works the same way.

## 37:09

For high energy, like the gamma rays that we care about in shielding, it would look a lot like this.

## 37:13

Of course, in gamma rays, they're not the same.

## 37:14

Right.

## 37:15

We don't have efficient term, right?

## 37:17

But we could also extend this.

## 37:19

We could have an equation that accounts for photonuclear effects where you have photons interacting
with the nucleus to produce new neutrons.

## 37:26

And then you have this coupling term.

## 37:28

So you have two equations, one for the flux of neutrons, one for the flux of gamma rays.

## 37:33

It could be driven by sources.

## 37:35

So I would say that for reactor purposes, this is typically zero.

## 37:39

But you can definitely have neutron shielding calculations where all of the stuff that we're talking
about is actually zero.

## 37:44

All of the stuff happening is driven by some vector.

## 37:47

That makes a lot more sense.

## 37:48

Yeah.

## 37:49

Good question.

## 37:55

All right.

## 37:56

So for the fast spectrum, which is sort of at least we'll go with the book and say that this is for
neutrons greater than 0.1 MeV in energy.

## 38:13

And for all practical purposes, we can care about neutrons going up to about 10 MeV.

## 38:19

The exact upper bound used in practice depends on the practitioner, right?

## 38:25

So there are computer codes that use 10 MeV.

## 38:28

I think that the scale suite out of Oak Ridge uses like a 25 MeV upper bound.

## 38:35

It only matters sometimes when we have to explicitly make integrals over the energy.

## 38:41

So the fast spectrum neutrons are in this faster range.

## 38:45

So some simplifications to the slowing down equation that we just wrote.

## 38:49

If we have neutrons at that energy, are we going to have many neutrons that are scattering and
staying within that energy range or scattering at all?

## 39:03

Not really.

## 39:04

Certainly, we're not going to have many.

## 39:06

Like if a neutron scatters at one of those high energies, that neutron is basically lost, right?

## 39:11

There's some small fraction.

## 39:13

If I'm a 1 MeV neutron scattering with hydrogen, yeah, I could end up at 0.8 MeV and still be in
this range.

## 39:20

Right?

## 39:21

But the average energy loss is going to have me down to like 500 MeV.

## 39:26

So I'm way out.

## 39:27

On the average, neutrons that scatter at all in this range have left the building.

## 39:31

So they're just sort of lost already in that total interaction term.

## 39:34

We don't have neutrons that scatter from lower energies to higher energies until we get to the
lowest energy, the thermal energy range, which is what we'll talk about Friday.

## 39:44

And so, really, this thing simplifies considerably.

## 39:50

So that we have a sigma T, the phi of E, and this is balanced by the emergence of fission neutrons.

## 40:06

Right?

## 40:07

So we have chi of E, and we have the fission rate.

## 40:16

Right?

## 40:17

So I'll be explicit here, 0.1 MeV to, say, 10.

## 40:22

Then this is our new, our sigma F, E prime, phi of E prime, dE prime.

## 40:40

Right?

## 40:41

So we're going to ignore any scattering.

## 40:43

So the only things that we have are the neutrons emerging from fission.

## 40:48

Now, in the book, this whole thing is just called, I think, S sub F.

## 40:56

Right?

## 40:57

For the fission neutron generation rate.

## 40:58

Right?

## 40:59

And so if we take that and just leave it as a single number, then we can solve for the neutron flux,
which is pretty straightforward here.

## 41:20

We just divide through by sigma T.

## 41:22

So in the fast domain, right?

## 41:25

So for neutrons above 0.1 MeV, we say that the fast spectrum is approximately chi.

## 41:35

So we have a total fission rate of 0.1 MeV times whatever our fission, total fission rate is,
divided by the total cross section.

## 41:53

And if the total cross section is roughly constant, which may or may not be true at those high
energies, then the fast spectrum flux goes pretty much as the chi spectrum that you've gotten
somewhat familiar with already.

## 42:07

so this is an approximation right there is some scattering that we're ignoring that would take us

## 42:14

that would keep us in like it would scatter at these high energies and remain at these high

## 42:19

energies but it's not a large fraction of neutrons okay so this is a useful way to approximate what

## 42:25

happens or what the neutron flux looks like above about 0.1 mev okay it's the simplest part of the

## 42:33

spectrum i think to approximate the next part the epithermal is a little bit more challenging

## 42:40

and so we make some approximations uh there as well okay so simplifications just to put them

## 42:50

here for posterity no scattering uh scattering into the fast range uh i think that that's really

## 43:20

the only one that i need to write down

## 43:21

so one one point if we were actually trying to find an absolute value for the fast spectrum flux

## 43:35

this leads to open the question for what this fission rate is right this seems to be like an

## 43:41

arbitrary normalization constant when written like this but it's not arbitrary how would we

## 43:47

normalize this how would we define this fission rate for our trigger reactor for a power reactor

## 43:54

what what

## 43:55

what

## 43:55

the thing about the reactor must set this in some way if i'm a thousand gigawatt electric

## 44:05

about one gigawatt electric that means i have a certain thermal power that thermal power comes

## 44:10

from what the energy released from fission right so if you know what your total thermal power is

## 44:19

that has to be the total energy produced by fission if you know how much energy comes from

## 44:23

fission which you do right roughly 200 mev then you can come up with what that rate must be

## 44:30

either for the whole plant or down to you know per unit um falling okay so we have a way to do that

## 44:36

here is just kind of easy enough to write it like that but we have everything that we need um to

## 44:41

define that more i guess clearly okay so in the intermediate range from this is say 1 eb less than

## 44:55

e less than 0.1 m eb okay some simplifications i think are the same but the one i'm going to focus
on

## 44:59

simplifications that we're going to make. No upscatter. Remember, when I had that scattering

## 45:09

integral, I said, hey, let's go for all energies E prime that lead to E, where E prime could be

## 45:14

zero up to infinity. Now, I will only care about neutrons that have a higher energy than my target

## 45:22

E, right? So only neutrons of energies greater than E are going to be able to scatter to energy

## 45:28

E. That makes sense. For energies beyond, say, an EV, there is no way for neutrons to scatter

## 45:37

and gain energy, or at least appreciable energy that we would care about. So there's no upscatter.

## 45:44

Because we're caring about neutron energies below 0.1 MeV, do I have to care about fission?

## 45:49

Do I have fission neutrons being born into energies between 1EV and 0.1 MeV? Your homework

## 45:59

last week asked you to define...

## 46:01

Or compute the traction of neutrons born from fission that show up with energies less than

## 46:06

0.1 MeV. Is that correct? What was that number? Like vanishingly smaller? So it's a reasonable

## 46:16

assumption to exclude fission neutrons as being a source for the intermediate spectrum,

## 46:23

right? So no fission neutrons, okay? So what that means is we have our total

## 46:36

power flux, and now all we have is scattering, right? So in order for me to scatter down into

## 46:46

energy E, my lower bound must be E. That's like that edge case that says I'm a neutron of E and

## 46:51

I'm going to scatter into E, which is really not scattering at all, okay? And then I can go up to

## 46:55

an upper bound. In this case, that will be 0.1 MeV. That's a good guess. Remember, though, when

## 47:04

we ignored scattering...

## 47:06

And the high energy, it's because we didn't expect many of those neutrons to stay above

## 47:12

0.1 MeV. But if I'm a 1 MeV neutron that scatters with hydrogen, my expected outgoing energy

## 47:19

is 500 KeV. Is that in this range? Yeah. So the neutrons that could show up here can go

## 47:26

all the way up to my system maximum, which would be, you know, say, 10 MeV, okay? So

## 47:35

I've got my scattering.

## 47:36

And I could have an external source here if I wanted, but I'm going to ignore that, right?

## 47:51

So this is sort of like the first step. Now, I could tackle this problem, and we'll do this

## 48:01

certainly next time, but it's easier if I, for a moment, forget about absorption.

## 48:07

Right? Let's assume that neutrons, once they get down to below 0.1 MeV, or we're having

## 48:13

interactions there, no longer suffer absorption. So we're going to ignore all the nasty resonances

## 48:19

that this treatment is going to let us handle next time.

## 48:22

So if I say that there is no scattering and that the... Sorry, that there is no absorption,

## 48:27

then that means my total interaction rate at this energy range should only be from scattering.

## 48:34

So I can actually change this.

## 48:37

And make that scattering.

## 48:40

But we're going to leave that there for a moment and possibly return to it on that.

## 49:04

But the one thing I want... Well, actually, no. I'll leave the slowing down density for

## 49:12

you to digest, and we'll actually pick that up next time. But I do want to take a look

## 49:17

at this.

## 49:19

Okay.

## 49:21

Let's assume that our scattering is only for 1 MeV.

## 49:24

It could be hydrogen.

## 49:26

It could be deuterium.

## 49:28

Okay?

## 49:29

So what I can do is replace this for 1 MeV of mass a.

## 49:40

If I make this assumption, then this integral changes.

## 49:48

If I'm scattering down to energy e, my upper bound...

## 49:51

The energy is that the height.

## 49:52

And it's soon top constant.

## 49:53

Right?

## 49:53

And it changes.

## 49:54

Exactly.

## 49:54

All right.

## 49:54

There we go.

## 49:54

could lead to energy e is no longer this upper limit of 10 meb right if i have only one nuclide

## 50:01

and has a mass number a do you remember what the what the range is so if i have an if i i'm a

## 50:07

neutron of energy e prime i scatter with this thing of mass number a which has a corresponding

## 50:14

alpha what is the range of outgoing energies that i can be so my starting energy down to alpha times

## 50:22

my starting energy right so we have to kind of flip that if my lowest energy is going to be e

## 50:28

what would my upper energy be so good good guess alpha e is smaller than e here so i actually have

## 50:39

to do something different with alpha it's not multiplied it's not e times alpha it's e

## 50:45

divided by alpha okay

## 50:47

okay so when i do this

## 50:56

okay

## 50:56

in fact let me i'll write it now like this where i have p e prime to e

## 51:04

p of e prime d e prime right so let me just say that a little bit again if i'm a neutron of energy

## 51:15

e prime okay what i'm doing is trying to get a balance for energies of e so i i don't care about

## 51:21

neutrons that go past e right i want to know what neutrons can get to e so if i'm at e prime

## 51:27

i'm getting a balance for e so i'm going to get a balance for e so i'm going to get a balance for

## 51:28

e the only range of neutrons energy z prime the range that e prime has to be has to be between e

## 51:35

up to e over alpha okay that is the largest energy that i can have a scattering event

## 51:43

with the nucleus with this alpha that brings me in this range does that make sense

## 51:49

so if i write this and then do you remember what this thing looks like this is one of the

## 51:59

over one minus alpha over e okay and so what i have for my final expression

## 52:09

is sigma s phi of e is equal to the integral from e to e prime sigma s of e prime phi of e

## 52:29

prime d e prime over one minus alpha e okay now okay this is basically the the last little bit

## 52:51

this equation here is an integral equation there's no derivative it's just an integral

## 52:56

okay it's one of those equations that was studied from 1946 on through a couple decades

## 53:05

i have lots of reactor physics textbooks there's a lot of really cool or maybe uncool math that lets

## 53:13

you come up with some solutions that are kind of complicated but are otherwise irrelevant to

## 53:20

practice i wasted about 10 hours of my weekend going through this it's something i had done as

## 53:26

a grad student but i wanted to go back and refresh my my memory and it dawned on me there's a reason

## 53:31

that nobody gives a shit because it doesn't impact

## 53:35

things in practice what does impact things in practice is what the solution of this equation

## 53:40

looks like asymptotically away from things that perturb the piece as it were what i mean by that

## 53:48

is the solution to this thing and you should verify this you'll have to because it's one of

## 53:53

your homework problems is that phi of e is proportional to one over e times sigma s of e

## 54:09

and in the case that the scattering cross section is constant which we saw is true for things like

## 54:14

hydrogen and the other moderators that we care about then this means that the flux is

## 54:20

proportional to 1 over e which is the very well known 1 over e spectrum exhibited in thermal

## 54:28

spectrum reactors in this range of energies between the vast neutrons born from fission and

## 54:34

the thermal neutrons that are causing all the the magic the one over e times i'm going to call it
the

## 54:38

the one over e times i'm going to call it one over e times the physical chicks which is the one over
and

## 54:39

e-spectrum comes out of this equation you can plug it right back into the equation evaluate it and

## 54:44

show that it works the things that are ignored are the things that if you think about it in order to

## 54:49

solve this equation somehow there has to be a forcing function shows up as a boundary condition

## 54:54

right maybe we have some number of neutrons showing up at energy 0.1 mev right turns out

## 55:01

between 0.1 mev and say 0.99 mev now 0.1 and then 0.099 that little bit before the boundary

## 55:10

there's some wiggles that aren't one over e called plot check functions for the famous guy

## 55:15

who in 1946 did the analysis right but beyond that little sliver next to the boundary it looks

## 55:22

like one over e and that's where we'll pick up next time where we use this basic equation

## 55:27

add back in the absorption we totally ignored and we'll come away with a spectrum that

## 55:31

you'll see in the next video.

## 55:31

is one over E, but also captures all the details

## 55:37

that the resonances lead to, right?

## 55:40

I will see you then.
