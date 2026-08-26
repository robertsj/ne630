# L07 Local Audio Transcript

Course: NE 630

Playlist source: https://youtube.com/playlist?list=PLy481lNHlnHoEO95vM-xYX2bydD25v20L

Video: NE 630 - Lesson 7

URL: https://www.youtube.com/watch?v=s5FG1SCtMbU

Video ID: s5FG1SCtMbU

YouTube upload date: 20230906

Duration: 41:39

Transcript source: Local faster-whisper transcription from YouTube audio.

Whisper model: large-v3; detected language: en.

Generated: 2026-06-28

Note: This transcript is machine-generated from audio and lightly wrapped only. It should be reviewed before being quoted, published, or used as polished lesson text.

Requested language: en

## 00:04

So I'll take a moment and there's I was grading the homework site notice, especially in the last
problem.

## 00:39

That folks but I would say about half of you got it sort of completely, which is good.

## 00:46

And then some folks I I think it was you resorted almost to the you know the cookie cutter approach
where it's like you see something that looks kind of like the problem.

## 00:53

And you paste in, you know, a form for the solution and so forth, without maybe turning the crank as
much as you might need to.

## 01:01

Right. So what i'd like to do is just very quickly go over those problems.

## 01:07

So the first one was the same with thorium 232 right so I can repeat the reaction here 232 thorium
plus a neutron goes to thorium 233,

## 01:21

which decays to

## 01:23

Protactinium 233, and then that finally decays to uranium 233, which, like uranium 235, is a great
fissile

## 01:36

Nuclide. Now to do this in practice there's more that goes on right because you have absorptions and
other things that a lot of the reactor physics that we haven't quite touched on yet.

## 01:45

But with at when formed as a strictly decay problem.

## 01:49

This is a one that's within our wheelhouse.

## 01:53

As it were right. So we have a beta minus decay here beta minus decay here.

## 01:57

I didn't give you half lives or anything all I said was, Hey, we've got lambda for the thorium and a
lambda for the protactinium.

## 02:05

Now uranium 233 like uranium 235 and 238 is radioactive, so it will, you know, decay away.

## 02:12

But for this sort of problem it's half life is so long compared to the time scales that we care
about that we can ignore it.

## 02:20

Right. So I didn't even mention that in the problem statement.

## 02:22

So that you can focus on what you need to do so.

## 02:25

What I said is, hey, we've got this process in a reactor and we have a chunk of thorium 232 we're
radiating it with neutrons.

## 02:32

This is called the breeding process so you can have a thorium breeder reactor we'll talk about that
later on.

## 02:38

Possibly, but the main thing is, you've got this thorium 232 eating up neutrons and you're producing
thorium 233 at some rate.

## 02:47

So if we assume that that's a fixed rate.

## 02:50

Okay.

## 02:51

So we have both decay and production for uranium for thorium 233 right so if we need to get these
three equations right we're going to get the number of thorium protectinium and uranium so we start
with the thorium so D and thorium DT.

## 03:09

Okay, because there's decay we can always start with decay, right if you remember that part of the
cookie cutter approach, you can use it right so we have the thorium decaying.

## 03:20

Okay.

## 03:21

Right.

## 03:22

And we have the thorium function time but it's also being produced.

## 03:26

And I said, at a constant rate, right so this looks a little bit like that's final homework problem
where you have some vision product being produced.

## 03:35

Okay.

## 03:36

Well, when that thorium decay is what does it decay into the protectinium right so if we want to do
the balance for protectinium DT.

## 03:48

Okay.

## 03:49

If we want to keep things symmetric.

## 03:51

So we'll put its decay.

## 03:53

And then it's production which is just from the decay of its parent thorium.

## 04:04

And then finally when that protectinium decays, we get the uranium 233.

## 04:14

Okay, so we have you.

## 04:18

T. Okay. Now I haven't given you a lambda here, right so our assumption for this model is that it's
not decaying so the only thing that's happening to it is it's being produced.

## 04:27

Right.

## 04:28

So that production rate will be equal to all the protectinium that's then decaying into it.

## 04:36

Okay, and that's the three equations that I was looking for so any questions about that.

## 04:49

It's just that it's always a reasonably straightforward statement of gains and losses, you just have
to be aware from problem statements or whatever other resources you're given, what are the possible
sources of gains production terms.

## 05:01

Here, I'll give you a number, or a letter, like our, when we get further into the course where we
model something that might be this exact problem.

## 05:09

The production rate will be a flux times a cross section, I don't be a neutron flux times and
absorption cross section of your aim of thorium 232 in this case right so we'll get absorptions per
second per centimeter cube, right and then maybe we'll have to scale

## 05:25

it by the volume of the reactor but we're not there yet.

## 05:27

But that doesn't change this.

## 05:29

All that would do is change.

## 05:30

What this number is, and maybe it changes in time, whatever.

## 05:34

We know how to write down the equation.

## 05:36

If you can't write down the equation.

## 05:38

Any math class that would have showed you how to solve the equation has no meaning.

## 05:43

Right. If you if you don't know what the problem is the tools you have to solve the problem, or
it's, you know, it doesn't matter, right so you've got to be able to define the problem.

## 05:59

Using the information.

## 06:00

That you're given.

## 06:01

I would say that's a huge part of what being an engineer is, if we equate engineer to problem
solver, right, you've got to be able to set up the problem before you can even think about solving
it.

## 06:13

Okay.

## 06:14

Also, I guess related to that homework while I'm here.

## 06:17

If, if I were to ask you what n at infinity is for any of this stuff right what what does that mean.

## 06:25

If, if we're talking about something at infinity yeah it could be that everything goes to zero but
usually.

## 06:29

That's not what happens right we wouldn't care about what happens at infinity if we think it's going
to go to zero.

## 06:34

So what you can do is remember that at any equal infinity if we're looking for some sort of stable
state.

## 06:41

That means that the time derivatives ought to go to zero right we've hit some sort of equilibrium
right maybe saturation activities if you remember that word, or we could have secular equilibrium,
where everything basically all the activities equal, whatever

## 06:57

your production rate started with.

## 06:58

So, if I take all these things, and I set them equal to zero.

## 07:02

Okay, what would happen to them. I don't know if we would actually get that because right now we're
assuming that we have this, this constant production rate right if this thing is not the king, the
number of uranium 233 is going to keep rolling

## 07:16

right so if we wouldn't be able to do that for, for this case but if this had a lost term, then you
would expect some sort of secular equilibrium, right.

## 07:26

In order to have equilibrium.

## 07:27

There has to be.

## 07:28

There has to be a gain and a and a loss that balance for each of your, your equations.

## 07:35

Second problem.

## 07:38

What was this one.

## 07:40

The probability that a neutron at x equals zero traveling along the x axis will have its next
collision blah blah blah blah blah right. So, the, the key thing here is that I have p of x is equal
to sigma times e to the minus sigma x.

## 07:54

The model of this problem that I'm looking at it.

## 07:57

Is a beam of neutrons that starts off at x equals zero makes it to some point x, or some, some
sliver between x and x plus delta, right, delta or dx right so I want to know what's the probability
that I make it to x and then have that first collision

## 08:20

in that little slab. Right. And that's exactly what this thing tells me.

## 08:24

Okay, so if I have a probability density function or distribution.

## 08:27

Right.

## 08:28

For random variable x in this case the distance that I traveled by start at x equals zero. Well,
what is the expectation value.

## 08:37

Right. Remember any function g of x. Okay, if I have this this probability density p of x this is
something that we talked about on Friday, that for any function g of x, the expectation value right
of g of x, or what we might in some cases called g bar.

## 08:56

Right. You've probably seen that kind of notation before.

## 08:57

Right. You've probably seen that kind of notation before.

## 08:59

Right. You've probably seen that kind of notation before.

## 09:01

But this is going to be the integral over the entire range of interest so the neutron starts at
zero, in a worst case scenario it immediately has its interaction so it goes, zero distance.

## 09:11

Now, with that distribution Sigma e to the minus Sigma x. What's the farthest a neutron can go.

## 09:19

Conceptual, hypothetically, what's that .

## 09:23

What's that ?

## 09:25

The X plus delta, we don't have a number there, right?

## 09:28

Because there's an infinite number of Xs and then X plus deltas, right?

## 09:31

So if I'm a neutron and I'm shooting into some chunk of material, we know that in practice,

## 09:39

that neutron is going to interact.

## 09:41

But the math suggests that we could go how far?

## 09:45

All the way through to infinity.

## 09:48

I don't know if we can go beyond infinity, but the bound is infinity, right?

## 09:51

We can go from zero up to an infinity.

## 09:53

Will we ever get to infinity?

## 09:55

In practice, no, right?

## 09:57

Because the probability becomes vanishingly small, right?

## 10:00

Because remember, this thing looks like, well, it's just an exponential.

## 10:05

So the further out you go, the less likely it becomes.

## 10:08

All that means, though, is that our bounds here are zero, infinity.

## 10:13

And then we are taking G of X.

## 10:15

Well, what's the thing I want the expected value of?

## 10:18

X itself, the distance, right?

## 10:20

X is our distance that we travel.

## 10:22

I want to find out what's my?

## 10:23

Expected distance of travel, right?

## 10:25

What is my mean free path in essence, right?

## 10:29

So if I take that, that's my G of X.

## 10:33

Well, actually, let me back up.

## 10:37

We'll put the formal thing here, right?

## 10:42

That's in this case, the kind of what I was looking for.

## 10:46

Now, if you wanted to, you could plug in the explicit function for X, right?

## 10:52

This could be X.

## 10:53

And then this would be the sigma E to the minus sigma X DX, okay?

## 10:59

So when I say that there's an integral in your expression, that's what I'm looking for.

## 11:04

That's the distance.

## 11:05

And when you evaluate that, I didn't ask you to evaluate it.

## 11:08

But when you do evaluate it, what do you think pops out?

## 11:11

X bar should be equal to what?

## 11:14

If we know X bar is the mean path to a collision,

## 11:18

what do we already know is related to that?

## 11:23

One over sigma, right?

## 11:26

Sigma is our macroscopic cross-section that has units of one over centimeters.

## 11:29

You flip that around, you get the mean free path.

## 11:32

So go ahead, write this down in your notes and then evaluate it.

## 11:36

And what should pop out is one over sigma.

## 11:38

I didn't care for you to do that.

## 11:39

I just, again, I want you to write down.

## 11:41

These are, think of these as equations in the book.

## 11:44

You should be able to write them down for the application for the problem that you have at hand.

## 11:49

Okay.

## 11:50

Any questions about?

## 11:53

This now based on sort of the hand count.

## 11:58

I don't often in a situation like this, we're less confident than we should be when we raise our
hands.

## 12:04

But still, I looking at some of this stuff, there's some of you weren't too sure about it.

## 12:10

So it's time to be sure about some of these things.

## 12:13

And if you have questions about it, don't wait till after the homework is turned in to ask them, ask
them beforehand.

## 12:19

Make sure that you're on top of this stuff.

## 12:21

Okay.

## 12:22

Because we won't be able to do some of this.

## 12:23

Stuff I'd like to do later on if we don't have some of the basics, right?

## 12:27

And again, I'm not asking you to be able to do the math as it were, right?

## 12:31

Math tends to be a sticky point for a lot of students.

## 12:33

You feel, I can't do it.

## 12:35

You know, I can't, I can't even start because the math is too overwhelming.

## 12:39

And something like this, I'm not asking you to do the math.

## 12:43

I'm asking you to use the language of the math to write down the equations, right?

## 12:47

There's a difference, right?

## 12:48

From being able to write down a system of equations and then solving it.

## 12:52

Huge difference.

## 12:53

I think it's valuable to be able to solve the system, but it's more important, I think, to be able
to write it down in the first place.

## 13:06

All right.

## 13:07

So on to the stuff of today.

## 13:19

Okay.

## 13:20

So there was only one section in the book, but I also gave you some additional reading in a
different reactor physics book.

## 13:28

That's quite, quite old.

## 13:30

Like many of them tend to be from the mid seventies or so.

## 13:33

When, when I would say nuclear engineering education was sort of like first formalized as a
discipline where you could kind of go to a university and have a, a pretty well organized plan.

## 13:46

So what this chapter or a section of chapter two is 2.5 is all about neutron scattering.

## 13:53

Now for any reactor type, but thermal reactors, specifically the scattering of neutrons from high
energies to low energies is what drives them.

## 14:03

So we can see that those neutrons are very important.

## 14:04

And in the first place, it's the magic as a word, right.

## 14:05

For thermal neutron based reactors, you know, where fission is happening based on neutrons at, you
know, 0.025, three EV, we've got to get them down to slow energies, low energy, slow speeds in the
first place.

## 14:18

And the way that we do this through some sort of scattering interaction, primarily elastic scatter,
right.

## 14:24

Usually with light nuclei like hydrogen.

## 14:28

Deuterium carbon.

## 14:30

Right.

## 14:30

Some of these lighter things where neutrons lose a lot of energy, make it.

## 14:33

without absorbing okay fast reactors it's kind of the flip uh side we don't want neutrons to

## 14:40

scatter down and land in the resonance regime um and so no matter what the the concept of

## 14:47

scattering is going to be important and then we'll see next week um a little bit starting for friday

## 14:53

i'll get the that uh reading up pretty soon but then next week we're going to see what the energy

## 14:58

distribution of neutrons in all reactor types look like right both thermal and fast reactors

## 15:04

and that'll be sort of our first little bit of reactor physics where we can actually dive in

## 15:09

and start making estimates about things that we've sort of hinted at before i'll bring up the the

## 15:14

letter k again the multiplication factor next week we'll we'll do our first little bit testing

## 15:20

what that could be for a realistic system right without touching space right which uh is an

## 15:27

important but separate topic

## 15:28

we'll deal only with the energy okay so from the book uh and me maybe i showed it one other time

## 15:38

too right the probability that a neutron of energy e scatters to energy e prime is given by

## 15:45

this expression okay p from e to e prime is equal to one over one

## 15:56

minus l

## 15:58

alpha

## 16:01

e values of the outgoing energy that are bounded by these values in fact if i can put

## 16:16

this okay so this nomenclature is useful for presenting it in this context right we've got

## 16:27

the probability that a specific energy e goes down to e prime following a collision

## 16:34

and that's this thing here now a probability density

## 16:36

function is not usually written with this as its argument usually you know p of x is just p of x

## 16:41

there's no x to x prime or anything like that so what this is really telling us is the probability

## 16:48

density for e prime where e the initial energy is like a parameter right that's a constant for the

## 16:54

prime e prime is the variable here that's the thing that we're trying to characterize e is given

## 17:00

for a particular collision if we have a collision the neutron already has an energy e what we're

## 17:04

we're talking about is what's the probability that it's outgoing energy is whatever given

## 17:09

these conditions that it has an energy e that it is scattering with something that has a mass

## 17:16

number a where a then feeds into this alpha term right this is alpha here is equal to a plus one

## 17:26

over a minus one squared okay and what this is also saying is that unless e prime is between

## 17:36

these two values right my initial value or alpha times e then the probability is zero right all

## 17:42

this is saying is that the energy the outgoing energy has to be between these bounds okay now

## 17:48

because e is not a variable e is a fixed thing here a is fixed so alpha is fixed that means that

## 17:55

this probability is equal to a minus one over a minus one squared okay and what this is also

## 17:56

saying is that the probability density is what kind of distribution from the ones that we talked

## 18:01

about last week friday we talked about three distributions i listed three distribution

## 18:07

what's the easiest one uniform is this uniform yes yeah right because this is just a number

## 18:17

one over one minus alpha e that's just a number for the for the particular collision

## 18:22

this is just a number so any of these energy any energy

## 18:26

which is a number which is a number which is a number which is a number which is a number

## 18:26

within the range alpha e to e is is equally probable okay so that's nice now with this

## 18:34

distribution we can do some things we just saw reviewed on on this little quiz what an expectation

## 18:41

value is okay so why don't we go ahead and compute the expected outgoing energy e prime right so if

## 18:49

we have a neutron enter input ingoing energy e collides off of something that has mass number a

## 18:55

or alpha

## 18:56

but i want to know what its outgoing energy is on the average okay so how do i do that

## 19:04

well what i want is the expected value of e prime okay and because it's an expectation i have to

## 19:17

take some sort of integral right that's the integral expression i was looking for in this

## 19:20

little quiz so i'm going to have an integral what are the bounds of this integral what are the in

## 19:29

other words what are the possible what's the lower bound of this integral what are the possible
what's

## 19:31

the lower bound of this integral what are the possible what's the possible what's the lower

## 19:32

bound of this integral what are the possible what's the lower bound for e prime and what's the upper

## 19:33

bound for e prime yeah alpha e to e right so My lower bound is Alpha e to e right i'll

## 19:44

put this thing here again uh the expected value of g of x is equal to g bar is equal

## 19:53

to i'll put a to b g of x p of x dx okay think of that that's just kind of a shorthand for devenir

## 20:00

think of that that's just kind of a shorthand for the emerging power to dripping clean Burkhead

## 20:01

that's and the only answer we can come up with would be MI is the function by which our

## 20:02

function is 1988 D X so thought over modulating d rises to m suar that changes to pot fly right

## 20:03

the expected value stuff that we're doing, okay?

## 20:06

So in this case, what I need is the function

## 20:08

that I'm actually trying to find the expected value for, right?

## 20:12

It's some function of E prime.

## 20:13

And in this case, it's just E prime itself, okay?

## 20:16

So I want to find the expected value of E prime.

## 20:19

That means I have to weight it then by the density, right?

## 20:24

And the density here is the one that we just saw above.

## 20:27

And so that'll be 1 over 1 minus alpha E, right?

## 20:33

Okay, and because we're integrating over the range,

## 20:37

I mean, that's it.

## 20:38

That's the number that we have.

## 20:39

And so multiply it by D E prime.

## 20:46

And of course, whenever I do my own math

## 20:48

on the electronic board as it were,

## 20:51

if you see me make any mistakes, please holler

## 20:53

because I definitely make mistakes, okay?

## 20:57

All right, so if we look at this inside of the integral,

## 21:00

the only thing that's varying is the E prime.

## 21:03

Everything else is just a constant, okay?

## 21:05

So I can pull everything else.

## 21:06

I've got a 1 minus alpha E, okay?

## 21:14

And then I have the integral of the E prime.

## 21:17

Well, what's the integral of E prime?

## 21:20

E prime squared over 2, right?

## 21:23

So I can take the E prime squared over 2.

## 21:31

This whole thing is then evaluated at the integral bound.

## 21:35

Minus alpha.

## 21:45

E, okay?

## 21:49

And if I take this, I can pull out the one half.

## 21:53

And then I'm left with E prime squared at E.

## 21:58

So E squared.

## 22:00

And then I have alpha E squared.

## 22:04

So alpha squared minus E squared, okay?

## 22:12

And then do you know how this factors?

## 22:21

The E squared minus alpha squared E squared?

## 22:24

I mean, as written, we could do it,

## 22:28

but sometimes it's nice to tidy up and get things in kind of the simplest form.

## 22:33

So we have an E squared minus alpha squared E squared.

## 22:36

This is E minus alpha E times E plus alpha E.

## 22:47

Do you agree?

## 22:52

Does that check out?

## 22:52

I think it does, right?

## 22:54

And so once we have that,

## 22:56

then the E minus alpha E,

## 23:00

E cancels out with the one down here, right?

## 23:02

So I can change colors here.

## 23:04

So I can cancel these out.

## 23:07

And what I'm left with then

## 23:09

is one half times E one plus alpha.

## 23:24

Okay, so that's my,

## 23:27

where'd my cursor go?

## 23:28

E prime bar, okay?

## 23:37

So just some,

## 23:39

a couple of numerical examples.

## 23:41

What if we have hydrogen one?

## 23:44

What's my, if I have hydrogen one,

## 24:00

what would be given an input energy E,

## 24:02

what's my expected outgoing energy?

## 24:07

What's that?

## 24:08

Yep.

## 24:13

Where do you get that from?

## 24:15

For the alpha A minus one.

## 24:19

Yeah, for hydrogen.

## 24:21

So there's kind of an assumption that I think is pointed out.

## 24:25

But we often just never think of it.

## 24:28

Everything in the book,

## 24:29

all these simplifications for alpha

## 24:31

is based on masses that are identical to mass numbers, right?

## 24:36

So a neutron, we say has a mass number of one.

## 24:39

So does a hydrogen, right?

## 24:40

Because that is a single proton.

## 24:41

Well, we know that neutrons and protons

## 24:43

aren't exactly equal in mass, right?

## 24:46

So all of these equations,

## 24:47

all the equations are fine

## 24:49

if we were to substitute in the actual masses.

## 24:53

I point this out, right?

## 24:54

It's probably one part in 10,000.

## 24:55

One part in 1,000 difference.

## 24:58

But yeah, so for hydrogen,

## 25:00

A is equal to one.

## 25:01

So alpha, go back up to the definition, is zero.

## 25:04

So the expected outgoing average is E over two.

## 25:09

I'll let you fill in the ones for these,

## 25:11

but it won't be as drastic.

## 25:14

Now for hydrogen,

## 25:15

if its expected outgoing energy is E over two,

## 25:19

do you remember what the maximum energy

## 25:21

that it could have is?

## 25:25

Right, if I have a scattering event,

## 25:26

the maximum energy,

## 25:27

I can take away is all the energy I started with, right?

## 25:29

That's effectively not having had a collision at all.

## 25:32

It's a bounding case.

## 25:33

But what about hydrogen?

## 25:34

How much can it lose?

## 25:36

What's the maximum amount of energy it can lose

## 25:38

or the least energy it can take away?

## 25:44

Well, remember the lower bound is alpha times E, right?

## 25:48

So if I go in with one MeV,

## 25:49

if alpha is equal to zero,

## 25:51

that means that I could end up taking away zero.

## 25:54

So neutrons and hydrogen,

## 25:56

because in this case, we're assuming equal mass,

## 25:58

the energy range is huge.

## 26:01

It's the entire energy range.

## 26:03

So if I go in with an energy E,

## 26:04

if I bounce off a hydrogen,

## 26:06

I can lose all of my energy.

## 26:08

That's one of the reasons why hydrogen

## 26:10

is so good for moderating neutrons,

## 26:12

meaning taking them from fast energies

## 26:14

and slowing them down.

## 26:16

So other light nuclei will give you pretty big ranges,

## 26:19

but only hydrogen has that property, okay?

## 26:23

You could also do an expectation value

## 26:26

for the expected energy loss.

## 26:28

So this is telling us

## 26:29

what's the expected energy that's coming out.

## 26:31

Well, if we go in with energy E,

## 26:34

E minus this expected outgoing energy

## 26:37

would be the expected energy loss, right?

## 26:40

And so you could look at isotopes in that same way.

## 26:45

So in the book, I don't know if you caught this,

## 26:53

Lewis hand waves a little bit by saying,

## 26:55

hey, this distribution that we have

## 26:57

for the outgoing energies,

## 26:59

it comes from some fancy analysis

## 27:01

in other textbooks, blah, blah, blah.

## 27:03

Isotropic scattering.

## 27:04

Well, I think it's actually important to see that

## 27:08

because it impacts significantly

## 27:11

the diffusion of neutrons later on.

## 27:13

We don't need it for this energetics, right?

## 27:15

But we have to have a picture

## 27:16

of what isotropic scattering is,

## 27:19

where that applies,

## 27:21

how it leads to this energy stuff

## 27:24

in order to understand some of the impacts

## 27:25

on the space of the diffusion of neutrons later on.

## 27:28

So I'm not gonna derive anything here.

## 27:30

I'm just gonna kind of summarize the things,

## 27:32

but the pictures,

## 27:33

the images that we're looking at

## 27:34

are the following ones, right?

## 27:37

So in the lab system,

## 27:39

the lab system, if you don't remember what it is,

## 27:41

it's the system in which you live, right?

## 27:43

If I'm playing billiards on a local billiard table,

## 27:47

the kinematics that I see firsthand,

## 27:50

that's the lab system, right?

## 27:52

So I could have a neutron that comes in,

## 27:55

hits its target, right?

## 27:56

And then it goes off at some angle.

## 28:00

I'm gonna call that angle theta,

## 28:03

and I'm gonna give it a subscript L

## 28:05

for laboratory system, right?

## 28:06

That's the scattering angle.

## 28:08

So if I say scattering angle,

## 28:10

that's what I mean, okay?

## 28:12

Often, in many cases,

## 28:15

I won't deal with theta directly.

## 28:17

In fact, I'll often use something called mu,

## 28:23

which is just the cosine of that angle, right?

## 28:28

There are reasons that we'll deal with the cosine,

## 28:30

but in most cases,

## 28:31

it's easier to deal with it.

## 28:33

At least I can write fewer characters, okay?

## 28:35

Now, over in the right-hand side,

## 28:38

we have the center of mass system.

## 28:39

Center of mass is where there is no momentum, right?

## 28:44

You've changed your reference frame

## 28:46

so that something that was at rest is now at motion.

## 28:50

The details, you can go back to your physics one

## 28:52

or physics two classes,

## 28:53

or maybe even your dynamics class,

## 28:55

if I recall correctly from the curriculum.

## 28:57

This has a separate scattering angle

## 29:00

that I'll call...

## 29:03

Theta Cm, right?

## 29:04

And then I can also do mu Cm is equal to cosine of theta Cm.

## 29:12

Okay?

## 29:13

So this is the frame that Lewis was talking about

## 29:18

for the isotropic scattering, the center of mass system.

## 29:21

All that means is that for a neutron with its given energy

## 29:24

hitting a nucleus of mass number A,

## 29:27

the probability that it's scattering cosine, right?

## 29:32

Okay?

## 29:32

Okay.

## 29:32

Okay.

## 29:32

Okay.

## 29:32

Okay.

## 29:32

Okay.

## 29:32

Okay.

## 29:35

Okay.

## 29:35

Okay.

## 29:35

Okay.

## 29:35

Okay.

## 29:35

Okay.

## 29:35

Okay.

## 29:35

Okay.

## 29:35

Okay.

## 29:35

Okay.

## 29:35

Okay.

## 29:35

Okay.

## 29:35

Okay.

## 29:35

Okay.

## 29:35

Okay.

## 29:35

Okay.

## 29:35

Okay.

## 29:35

Okay.

## 29:35

Okay.

## 29:36

Okay.

## 29:36

Okay.

## 29:36

Okay.

## 29:36

Okay.

## 29:36

Okay.

## 29:36

Okay.

## 29:36

Okay.

## 29:36

Okay.

## 29:36

Okay.

## 29:36

Okay.

## 29:36

Okay.

## 29:36

Okay.

## 29:36

Okay.

## 29:36

Okay.

## 29:37

Okay.

## 29:37

Okay.

## 29:37

Okay.

## 29:37

Okay.

## 29:37

Okay.

## 29:37

Okay.

## 29:37

Okay.

## 29:37

Okay.

## 29:37

Okay.

## 29:37

Okay.

## 29:37

Okay.

## 29:37

Okay.

## 29:37

Okay.

## 29:37

Okay.

## 29:37

Okay.

## 29:37

Okay.

## 29:38

Okay.

## 29:38

Okay.

## 29:38

Okay.

## 29:38

Okay.

## 29:38

Okay.

## 29:38

Okay.

## 29:38

Okay.

## 29:38

Okay.

## 29:38

Okay.

## 29:38

Okay.

## 29:38

Okay.

## 29:38

Okay.

## 29:38

Okay.

## 29:38

Okay.

## 29:52

Okay.

## 29:52

but you end up with the differentials of sine theta d theta because i don't know if that rings

## 29:58

bell that's where it's from we don't have to get into that so just know that when when we say

## 30:02

isotropic scattering in the center of mass system it means that this thing is uniform and
specifically

## 30:08

it's one half for mu from i guess i should sorry not negative one this would be minus one less than

## 30:19

mu cm less than one okay that's all it means now because there is a one-to-one relationship between

## 30:28

this scattering angle and the energy that the neutron loses and because there is a way to

## 30:35

convert a probability density from one variable to that of another variable through some sort of

## 30:41

transformation we can actually formally derive the the thing that is in lewis right i'm going to
state

## 30:48

this thing

## 30:49

here okay what do i mean by transformation if i have a probability density right i have a random

## 30:55

variable x and i have its density if i have another random variable that is a function of x

## 31:00

then the probability density for y is equal to the probability density for x times this

## 31:08

derivative term if you've ever heard of the term jacobian of transformation

## 31:16

from a nasty class that you've had in your past

## 31:19

that's exactly what this is a little bit easier here because it's just one dimension usually you

## 31:23

have to use a jacob jacobian usually means multiple dimensions so you would have something that
looks

## 31:29

like this to go from say cartesian coordinates to spherical coordinates or some other system

## 31:33

this is one variable that's easy to to compute the the derivatives right so as a specific example
and

## 31:45

i'll just write this down

## 31:50

this is basically this is right from that the other reading so in case you didn't skim uh as

## 31:55

thoroughly as you you might have let me go back to a white font okay right the energy the outgoing

## 32:04

energy uh in terms of the center of mass scattering cosine is this expression and then we can also

## 32:26

relate the the laboratory cosine to the

## 32:29

center of mass

## 32:38

if you had me in 495 you saw the first one or something very close to it when we talked about

## 32:45

scattering uh i'm not sure that dr mcneil would have done the same thing but the the relationships

## 32:51

are are reasonably straightforward they can be kind of a beast to work with this one especially

## 32:56

uh this one if i wanted to i could say hey i've got a function for e prime and i can move the

## 33:01

e over here that means i have a function or e prime is now a function of this thing right that's mu

## 33:07

cm

## 33:08

and i can do that transformation right just take the derivative move things around and lo and behold

## 33:12

what you'll get is what's in in the book so i'm not going to waste your time and do that i will

## 33:18

take a look at this computationally for a moment i can do the same thing i have a relationship

## 33:23

between the laboratory cosine and this cosine that's a little bit trickier to do i mean it takes

## 33:30

probably a couple pages probably to work it out cleanly but there is an important thing i'd like

## 33:36

to show you graphically i'm going to show you graphically graphically graphically graphically

## 33:38

graphically graphically graphically graphically graphically graphically graphically graphically
graphically

## 33:38

okay where is my there we go okay so what i've done here is i've worked it out this is what it

## 33:47

uh looks like okay and remember in the center of mass system all the scattering is isotropic

## 33:56

right that's where i say p of mu cm is equal to 1 over 2 and then you can use that to find the

## 34:02

energy probability density that's exactly what's already in your textbook but when you do it for to

## 34:08

be a distribution for the scattering angle in the laboratory system things look really different

## 34:14

so rather than being that flat line the one half from negative one to one we get a wide range of

## 34:21

shapes depending on what the mass of the target nucleus is and in particular this blue curve we go

## 34:28

flat at zero until we get to the halfway point and then it jumps up that's for hydrogen now
isotropic

## 34:34

means flat does that hydrogen curve look flat

## 34:38

no so the key observation to make here is isotropic in the center mass system does not mean

## 34:44

isotropic in the lab system remember these things that are moving around they're moving around in

## 34:49

the lab system so when we make observations or write balance equations for how they move around

## 34:54

the world they're going to be following the laboratory system distribution so that means

## 34:58

when we get to neutron diffusion and we want to know how neutrons are propagating out like suppose

## 35:03

you have a point source and you want to know how they're going through the material whether or not

## 35:07

something exhibits isotropic scattering is going to make a big difference because if

## 35:11

if i'm hydrogen what direction is most likely well mu one what does that mean if i'm having

## 35:20

a scattering event remember the the angle is relative to my initial direction if i have a

## 35:26

mu value one that means the cosine is one what does that mean for the angle

## 35:30

what's my what angle leads to a cosine of one zero does that mean that i've changed my

## 35:37

direction

## 35:37

at all no that means that neutrons when they collide with light nuclei tend to be forward

## 35:43

scattered which means that if i have a point source of particles and they're diffusing away

## 35:47

if i have this anisotropic scattering this forward peak scattering they're going to travel way
further

## 35:52

in space than they would if the scattering were isotropic now if you look at this curve as i

## 35:59

increase a the things flatten out so as i get to something like a equal 238 right heavy uranium

## 36:05

then the scattering actually does

## 36:07

look pretty isotropic okay so to assume isotropic scattering in the lab is not bad for things that

## 36:14

are say over a equal probably a equal 10 and even for a 16 it's pretty straightforward now this

## 36:22

this um picture actually describes one of the chief difficulties in in neutron simulation

## 36:29

all the data that we have from those cross-section libraries represents the scattering in the center

## 36:37

of mass

## 36:37

system it does so using something called the genre polynomials right it basically

## 36:42

breaks it into a flat a line a parabola all that stuff when you go from the center of mass

## 36:47

system to the lab system you need a lot more terms to capture that nastiness right and so

## 36:52

that that makes simulation pretty challenging uh based on some of the tools that have been used

## 36:58

classically okay all right so the last thing that i want to do is show you just uh a kind of

## 37:07

a neat little simulation you've probably read about something called the slowing down decrement

## 37:13

okay all that is is the uh expected logarithmic energy loss for neutrons right you can look at

## 37:21

the expression but the chief thing that it gives us is an ability to estimate the number of

## 37:26

collisions that a neutron needs to have to go from some upper energy to some lower energy okay and
so

## 37:32

what i've done here is made a simulation for figuring out if that expression is true so for

## 37:37

for the case of water the effective slowing down decrement is 0.924 right that's something from

## 37:43

the very end of the reading that you did so i'm going to go from 2 mev down to 1. the number of

## 37:48

collisions that i'd expect that to require is you know between 15 and 16. okay now what i'm going to

## 37:55

do here is simulate that so i'm going to go for 10 000 neutrons i am going to keep track of all

## 38:02

the counts that it takes to go from 2 mev to you know one ev okay so what i'm going to do

## 38:07

is this i'm going to start my initial energy at 2 meb and then while my energy is greater than that

## 38:13

lower energy i'm going to pick a random number okay between zero and one i'm going to use this

## 38:19

to choose between the two scattering nuclei if i'm doing water that means i have both hydrogen and

## 38:24

oxygen so i'm going to use the ratio of their scattering cross-sections just like in the

## 38:29

textbook to decide which one i'm scattering with okay so more likely than not it's going

## 38:34

to be hydrogen right because it has 20 barns for a wyd and i'm going to calculate that as well

## 38:37

cross section there are two of them so that's 40 barns over the 40 barns plus 3.8 okay so it'd be

## 38:44

very unlikely that i scattered with oxygen but you have to account for both okay given which a

## 38:48

i choose i'll compute my alpha and then i'll choose another random number and this will give

## 38:53

me the random number that picks which which energy in that range from alpha e to e my new energy
will

## 39:00

be right and so then i get my e prime and then i add my count and then i set e to e prime because

## 39:06

my outgoing energy is my ingoing energy for the next collision that i have and i cycle back and

## 39:12

as long as my energy hasn't gone below that threshold i'll keep doing it okay so if i do this

## 39:17

this 10 000 times okay it takes just a

## 39:24

a moment to do that okay but this is what i get the mean number of collisions i get is 16.78 and

## 39:33

there's a distribution so this is one thing when when we

## 39:36

you

## 39:36

you

## 39:36

with the math and we end up with these expected values it's sometimes really easy to forget that

## 39:43

it's just an expected value that characterizes a distribution okay so in reality we would see

## 39:51

neutrons that take five collisions all the way up to 30 collisions to get down from

## 39:57

fast energies to these uh lower energies on the average though the little tool in the book gives

## 40:03

us a pretty good answer one thing that confused me and i'm not sure that i have a great explanation

## 40:08

for it but i have an intuition for it it says 15.7 here but after running 10 000 and i could

## 40:16

do a million i get the same basically same number it's 16.7 it's one additional collision

## 40:23

right the only thing i can think of is this number gets you all the way to that edge but

## 40:28

in reality these are discrete events right you either have

## 40:33

17 collisions or 18 collisions and you need one additional collision to actually pass that so

## 40:38

that the algorithm says hey i i'm done right that that's my sort of hand waviness uh for that but

## 40:45

you can use this sort of simulation always uh to do sanity checks on these results uh it's it's

## 40:52

one thing to be able to drive it through the math or you know plug some numbers in and chug some

## 40:57

answers out but to be able to do some some simulation like this i think can be valuable so

## 41:02

uh i'll make sure that this is a

## 41:03

available i'm not asking you to use this or anything for the homework uh the homework will

## 41:07

be more kind of in line with the by hand examples so i've taken just a couple minutes extra of your

## 41:14

time i guess we spent maybe more time on that quiz than i thought uh for friday you'll be going into

## 41:20

chapter three we're going to start diving into the energy distribution of neutrons using this

## 41:24

as kind of like a springboard all right so i will see you then and feel free to come up ask

## 41:29

questions as i'm packing up
