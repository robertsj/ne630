# L28 Local Audio Transcript

Course: NE 630

Playlist source: https://youtube.com/playlist?list=PLy481lNHlnHoEO95vM-xYX2bydD25v20L

Video: NE 630 - Lesson 28

URL: https://www.youtube.com/watch?v=Y9Ma9rpXB00

Video ID: Y9Ma9rpXB00

YouTube upload date: 20231030

Duration: 01:00:29

Transcript source: Local faster-whisper transcription from YouTube audio.

Whisper model: large-v3; detected language: en.

Generated: 2026-06-28

Note: This transcript is machine-generated from audio and lightly wrapped only. It should be reviewed before being quoted, published, or used as polished lesson text.

Requested language: en

## 00:00

I know, like, he gives a speech, and that's how we get people to talk, you know, to the bathroom,
and, like, I listen to him talk, and he's like, oh, you know, I'm going to work hard, and he's like,
I'm scared, and he would vomit, like, I don't know, I can't be sitting in this room.

## 00:18

Okay, so last time on Friday, we had talked about neutron kinetics with delayed neutron precursors,
right?

## 02:15

So adding in this extra beast.

## 02:17

Made the equation slightly more complicated, right?

## 02:21

Today, we'll look at some solutions, kind of continuing on what we did.

## 02:27

I'm a big fan of using numerical methods to get solutions to things that are more realistic than
some of the pen and paper analysis that one could do, right?

## 02:37

There is an importance in being able to do some stuff with pen and paper, and you're doing that
right now, I suspect, for the homework, which is due on Wednesday, right?

## 02:46

And you've probably run into one.

## 02:47

Problem that feels a bit more math-y than typical, I think, anyway, if I'm jumping into your minds.

## 02:55

Maybe you haven't started.

## 02:57

Have you started?

## 02:58

Okay.

## 02:59

Well, we'll have time.

## 03:00

Good honesty, right?

## 03:01

So we'll have time at the end, and hopefully what I've put together will be of some use in that, and
then obviously for the exam.

## 03:11

So for next time, there's just a short reading assignment 5.6, which explains a lot.

## 03:17

It's one example of what feedback does to this whole set of equations, right?

## 03:23

When you start having the impact of temperature through those reactivity coefficients, things
change, okay?

## 03:31

And then that will leave us quite a bit of time, I suspect, for discussing the exam, right?

## 03:36

So I've already started piecing together what I'll put on that, so it should be a useful time, I
hope.

## 03:43

Okay, so let's review a little bit of what we did last.

## 03:49

With the precursors being added to the mix, okay?

## 03:53

One thing that I didn't highlight, but is in the reading from last time, is that when we introduced
the late neutron precursors, the lifetime of neutrons changes significantly, right?

## 04:07

So before we had this L, which is the neutron lifetime or the prompt neutron lifetime, and has
values on the order of 10 to the minus 4, okay?

## 04:18

Okay.

## 04:19

In delayed neutron precursors, with their lifetime, the L sub D, which there's an expression in the
book for that, too, we end up with an average neutron lifetime that is the original on plus this
beta over lambda, where lambda is the average decay constant for the precursors.

## 04:37

And we'll compute that in a moment for the U-235 data that we've seen before.

## 04:44

Beta, of course, is a small number, 0.0065 for uranium-235, and actually smaller for...

## 04:49

The other fissile nuclides.

## 04:51

But because it is non-zero, and because lambda is less than 1, we're actually adding a significant
amount of time to this average neutron lifetime.

## 05:00

So we're going from something like 10 to the minus 4 to something that is, you know, seconds long,
right?

## 05:06

Huge, huge increase.

## 05:08

Even though beta is small, the numbers work out where it has this enormous impact on sort of the
time constant of the system.

## 05:16

Now, we couldn't just take this number and plug it in.

## 05:19

We could plug it into our single kinetics equation from a couple times ago.

## 05:23

You'll remember that if we ignore delayed neutron precursors, there's a pretty simple expression for
dn dt, right?

## 05:31

If we were to put this time constant or this lifetime into that, we would get something that is
closer to reality than if we didn't, but it's still missing a lot of the kinetics of it, right?

## 05:42

The interaction between the neutron density and the precursor concentrations, right?

## 05:47

When you separate those things, right?

## 05:49

The neutrons are evolving very quickly, the precursors evolve very slowly, and if you don't allow
for that, that sort of dual time division, you can't really capture the physics, right?

## 06:01

But this gives us a really good sense of why things do slow down when we have delayed neutron
precursors.

## 06:08

Okay, so as a first example, I want to make sure that we have a kind of a numerical sense for this.

## 06:15

The lambda is the average decay constant for the precursor.

## 06:18

So for uranium-230.

## 06:19

535, what is lambda?

## 06:21

Now, I don't have the expression here, but it is in the book.

## 06:26

And if you have the book, it is equation 534 gives us the one for lambda.

## 06:36

And I brought up the book also so that we have that here.

## 06:44

534.

## 06:47

There it is, okay?

## 06:49

So if you look at this, I mean, there's certain things in the equation you can plug and chug and get
the value for lambda.

## 07:00

I guess a question I have for you, why is this the definition for lambda?

## 07:05

Why isn't it just, say the, why are we weighting the one over lambda, so not the lambdas themselves,
right?

## 07:12

Like doing this weighted average.

## 07:14

This seems, somehow it seems maybe unintuitive.

## 07:34

Any ideas?

## 07:35

No.

## 07:35

Okay.

## 07:36

Is there one thing I can think of that you use more than lambda, more than you use lambda that makes
more sense to calculate that versus the other?

## 07:43

I'm not, I mean, maybe.

## 07:47

Any time, so maybe unrelated to your response and not specific to this.

## 07:52

Anytime we make an average, anytime we've done an average in this class anyway, we're always out to
preserve something, right?

## 08:00

So in this case, what would we want to preserve?

## 08:04

Ultimately, like a number of.

## 08:06

Something or other, right?

## 08:07

A number of precursors.

## 08:10

If we think about this more carefully, remember that one over lambda is the lifetime, right?

## 08:18

It's the mean lifetime.

## 08:20

It's related to the half-life.

## 08:21

So in other words, it's almost like we're preserving a half-life, which if you think about it, maybe
if we weighted too heavily, the small lambdas or large lambdas, which would be weighting the small
lifetimes, then we would have a

## 08:35

decay constant that if we only had one, would basically get rid of too many of our delayed neutron
precursors too quickly, right?

## 08:43

So we're preferentially weighting the ones that have a longer lifetime to preserve that long-time
concentration.

## 08:50

I didn't think too carefully about that before I asked, but it was something that when I looked,
it's like, okay, that's not just a beta-weighted average of the lambdas.

## 08:58

It's the average of the inverses, right?

## 09:00

But it's there for a reason.

## 09:02

So using this.

## 09:04

And given the fact that.

## 09:05

I have some of this stuff here, we should be able to compute this pretty quickly, right?

## 09:10

So we'll say one over lambda is equal to the one over the sum of betas, right?

## 09:22

So when I write beta like this, that means the sum of the delayed neutron precursor fractions,
right?

## 09:27

And so it's one over beta times then the sum of the betas, each one of them independently,

## 09:34

divided by.

## 09:35

The lambdas, okay, and then lambda ABG is equal to one over this thing.

## 09:45

Now, if we look at these, these calf lives, we know that the lambda is log two over that.

## 09:53

I guess I can never do that sort of calculation in my mind.

## 09:56

So we'll just take a look at what this, this average is.

## 09:59

Basically, I was going to say, do you have any sense for what that number is in this case?

## 10:02

It's 0.0766.

## 10:04

Now, if I wanted to.

## 10:05

Print out what these lambdas are, go ahead and do that as well.

## 10:10

So you can kind of compare, right?

## 10:12

So we've got lambdas that range from 0.01 all the way to three, and we're getting a value.

## 10:18

That's obviously in the middle, right?

## 10:20

Cause the betas we're, we're normalizing to the betas on dividing my total beta.

## 10:23

So, um, it is a normalized probability and we're somewhere in the middle of that range.

## 10:29

Okay.

## 10:31

So we'll be using this number as we go along.

## 10:34

I didn't get.

## 10:35

The slides done to upload, uh, beforehand, so you, you won't be able to follow along, but, um,
hopefully in your notes, you can keep track of, uh, any of the logic that we're using here.

## 10:44

Right.

## 10:45

I'll just be the global calculator for us all.

## 10:51

So that's our average lambda.

## 10:54

Now, what we did look at last time was this set of equations, right?

## 10:58

So the model for our reactor under this, this notion of time, uh, dependence.

## 11:05

Went from the single equation for the neutron.

## 11:08

Density or the flux or the power, right?

## 11:10

That's one thing that you should think about if, if we're right now casting everything in terms of
the neutron density, and we know there's a one-to-one relationship between N and the neutron flux,
right?

## 11:22

Fee equal N times V.

## 11:24

And if we know what the flux is, we can compute a reaction.

## 11:27

And if we can compute a reaction rate, we can compute a fission rate in particular.

## 11:31

And if we know that, then we can compute a power.

## 11:33

So anytime that we have D and D T, we could equivalently write the system.

## 11:38

In terms of the flux or of the power.

## 11:41

Okay.

## 11:42

So we'll stick here with, with, uh, just the neutron density and then the precursor concentrations.

## 11:47

But when we have the precursor concentrations in, we get this set of equations.

## 11:51

So Lewis, uh, 45, 47 and five 48, the data that we have, of course, breaks up the precursors into
these six groups.

## 12:00

So this is seven differential equations, their first order.

## 12:04

Okay.

## 12:05

Uh, there are techniques for solving them, I suppose.

## 12:08

By hand.

## 12:08

And of course we saw last time how we can use the ODE and tool from sci-fi to solve them
numerically.

## 12:20

And if we want to, we could take these equations and write it into sort of a more compact matrix
form like this, where things get particularly easy.

## 12:31

If that B term source term goes away, like we assume we start off in steady state.

## 12:35

And if this row of T is not a function of time, right?

## 12:40

It's some constant step in.

## 12:41

Uh, insertion or removal of reactivity, like I drop a control rod into, uh, an otherwise critical
reactor, or I remove a control rod from an otherwise critical reactor, then a is constant.

## 12:52

And this whole thing is considerably easier to solve, whether you're talking about by, by hand or
numerically.

## 12:59

And in that case, we'll get to it later, have a little bit of discussion on it, but if this is
constant and we start off from this, uh, initial condition, all of the solutions for N and for the
precursors.

## 13:11

Are exponential, right?

## 13:13

And because we have seven equations, essentially what each one of these is, is a sum of seven
exponentials, where the argument of the exponential is like time constant.

## 13:24

And that time constant is something that comes out of, uh, basically an eigenvalue problem, right?

## 13:31

It's pretty challenging to do seven by seven matrices and their eigenvalues by hand, but we can
certainly do two by two.

## 13:38

Okay.

## 13:39

Now we'll get into some more of it.

## 13:41

So.

## 13:41

I'm going to talk about some of the solution techniques, but I, I actually dove into what I could
find on your math three 40 class, and it does look like you covered some of these systems of
equations, but not maybe in the same way that I expected you to have seen them.

## 13:56

So just before I forget to ask you, do you remember solving systems of ordinary differential
equations in math three 40?

## 14:05

You do not.

## 14:08

Okay.

## 14:09

So I feel better about not having you really try to solve.

## 14:13

These by hand, um, because one, it takes us away from the physics and two, if you haven't had that.

## 14:18

So at the end of the discussion today, I'll sort of map out a few different ways that you would be
able to tackle this, that I hope latch onto some of the things that you've seen before.

## 14:29

Right.

## 14:29

But in, in the end, it, it doesn't really matter a whole lot for what we're doing here because we're
not aiming to solve them completely by hand, but it's doing that search and what you're confirming
now makes me wonder.

## 14:43

What we're doing with some of our math classes and how, not, not, not to criticize the math class,
but I'm, I'm wondering if this, where I was surprised is similar to how other faculty members are
surprised, right?

## 14:55

If you're not getting what we think you're getting, and then we ask things that are based on things
that you don't know, then everybody gets sad.

## 15:04

Right.

## 15:04

So I'm trying to, uh, trying to, to, to reempt any, any undue sadness.

## 15:09

All right.

## 15:10

So.

## 15:11

When we do solve that.

## 15:13

Equation, we end up with a solution that is obviously not trivial, right?

## 15:17

Um, that's the beauty of numerical simulations, right?

## 15:20

We can very easily set up the, the problem and then give it really any inputs, right?

## 15:26

So in this case, what we're, this was the very last example from last time.

## 15:30

So I, I know I went over about five minutes and people had to leave, but I'll review what we saw
last time.

## 15:34

The, uh, problem started off with a neutron density of 10 to the, uh, eight, right.

## 15:41

With the corresponding initial condition.

## 15:43

And it gave us monthly, the number one answer was that I need to re waktu it.

## 15:49

And so we went over that, but we also did a very similar scenario where we did a very simple
analysis, which had the, uh, the three key, uh, functions for the precursors, right.

## 15:55

It was steady state.

## 15:56

And what, what I was having a model is from zero to one second, the reactor continues on in steady
state.

## 16:03

And the reason that I usually set up problems to look like this, it guarantees that the steady state
actually is steady state.

## 16:09

So if I've done the computation of those precursor concentrations, and I assume my records and
steady state.

## 16:13

mistake in my inputs, right? Maybe I messed up my precursor concentrations, or I have an issue in

## 16:19

my numerical method, right? It could be that I'm using it incorrectly, or maybe it's just not good

## 16:27

enough for the problem that I'm tackling, right? Which could also be the case. These are simple

## 16:31

enough relative to the methods that we have available that we should be able to get a flat

## 16:36

initial condition. But then at one second, I insert a reactivity of 0.001, so pretty small

## 16:44

reactivity relative to beta, but I jump up, right? And then I ride up on a slower time constant.

## 16:51

If you zeroed in on this, this is an exponential increase, right? I don't, I'm not going to zoom

## 16:56

in, but you would actually see it go up on an exponential curve with a time constant that is

## 17:02

very different from the one that governs this shape here during the

## 17:06

1.001.

## 17:06

to 2 seconds, right? So that's the first thing. When you have the, when you have the precursor

## 17:11

equations with the, sorry, the kinetics equations with precursors, because of these different time

## 17:17

scales, your solution will exhibit different behavior in different parts of the time space,

## 17:24

right? So this very first thing, we have something that we'll approximate in a little bit using the

## 17:29

so-called prompt jump approximation, right? We'll be able to estimate without solving differential

## 17:34

equations by how much it increases the time. And then we'll be able to estimate the time

## 17:36

increases from here to here, right? And then similarly from here down to here, okay? And then

## 17:41

as we go up in power, we drop the control rod back in, right? So remove that 0.001 of rho that we
put

## 17:49

in and we're back to rho equals zero. What does rho equals zero mean? What kind of state are we in

## 17:57

if rho is equal to zero? What's that? It's critical. So we're steady, right? So we see that

## 18:02

the population is, even though we've gone back to a critical state, it takes some time for that

## 18:08

population to go back to a critical state. So we're steady, right? So we see that the population

## 18:09

is, even though we've gone back to a critical state, it takes some time for that population

## 18:09

to find itself in its steady state again. But the key thing that I observed, and we all observed

## 18:15

last time, is that if I took this out to like 100 seconds, it'll reach some sort of asymptotic value

## 18:20

of roughly 1.03 times 10 to the 8th, okay? That's not the same thing we started with,

## 18:28

okay? So we've gone up in power. We ride this positive period. We'll talk about that in a

## 18:32

moment. We put the control back in. We end up at a power that is greater than we started with.

## 18:38

Why is this a positive period? Why is this a negative period? Why is this a negative period?

## 18:38

Why is this important for those who were here in those last five minutes?

## 18:43

What practical value does this have? It's the only way to increase power.

## 18:50

Yeah. If we have a reactor like ours, we know that there's some starting source that will give us
that

## 18:55

first little bit of a neutron population. But if we want to take that up in power from like one watt

## 19:02

or whatever the power is that the source can provide us, we have to remove control,

## 19:07

go up in reactivity, right? Greater than zero.

## 19:11

Right up on this positive period until we hit some power that when we put the control back in

## 19:18

leaves us in a steady state with a power that we want. So as this shows, depending on what the

## 19:25

reactivity magnitude is, we'll always shoot up higher in power than we want to be. And we have

## 19:31

to manage things right so that when we drop down back to critical and the power decreases that

## 19:37

we're left in the state and at the power that we want, right? That's a big problem.

## 19:41

That's part of the operations of the reactor. Yeah, question.

## 19:44

Do we see a similar thing if we were to decrease our reactivity below critical?

## 19:53

Would it do that same thing in reverse or how would it?

## 19:57

So like if you were operating at one megawatt, you put in some control, go down in reactivity,

## 20:03

go down in power, and then go back to critical, will you be at a lower state?

## 20:06

Yes.

## 20:07

Yes. Yep.

## 20:08

So that's it.

## 20:09

So basically,

## 20:11

the mechanics that we see here or the kinetics that we see here works in both ways. That's how

## 20:16

we go from one steady state to the other. Of course, if we're up at higher powers like that,

## 20:22

one megawatt, let's say, then it's not quite as simple as this because of the feedback effects,

## 20:27

but the principle is definitely the same, right? We go from one power to another by

## 20:31

doing something that changes the reactivity in time. And so you can imagine that when you have

## 20:36

overshoot like this or in the case of putting in reactivity, you might have

## 20:40

some undershoot.

## 20:41

All that stuff is subject to more robust control mechanisms, right? So I would say historically,

## 20:49

a sequence of nuclear reactor physics courses would include a course specifically on dynamics

## 20:56

and control of nuclear reactors. So all the Laplace transform stuff that you learn in your

## 21:01

controls class or will learn in your controls class would map on directly to everything that

## 21:05

we're doing, right? There's no problem. There's no reason that we can't do all of these kinetics,

## 21:11

and then dynamics with feedback in the not time space, but in the frequency space, right? We could

## 21:17

definitely do that. And there's been a lot of work. I would say that probably a lot of good controls

## 21:23

research came out of the control of nuclear reactors back in the 50s and 60s, right? One can

## 21:28

say that about a lot of things related to nuclear. I would say that nuclear engineering, maybe not

## 21:33

specifically for reactors, but certainly for an understanding of neutron populations for a wide

## 21:39

variety of applications,

## 21:41

led to a lot of the numerical methods that we have and a lot of the computational tools that

## 21:46

we have for implementing those methods, like physical hardware, all the original computers,

## 21:50

the big mainframes, ENIAC, all that stuff, I would say was driven by the Manhattan Project,

## 21:56

right? Because they really needed to know what the bombs were going to do, right? As one example.

## 22:00

And so there's a legacy in nuclear that kind of pervades a lot of sort of technical disciplines,

## 22:11

since that time. Good questions. All right. So why did I have that set up as a separate one?

## 22:23

You have to give me, I guess that would be, no, that's that. Skip. We just looked at that.

## 22:37

All right. So what I've taken out of like the active slideshow is some code that is almost

## 22:43

identical to what we looked at last time, right? I just don't want to have to scroll.

## 22:46

Through it when I go back to the slideshow and what I've done is I've tucked everything

## 22:51

away into one function that takes in a step reactivity insertion. Sorry, not necessarily

## 22:57

a step up, but a function for reactivity and then returns the neutron density,

## 23:02

the precursor concentrations and the time so that we can do some other analysis. Right. So

## 23:06

that's what we're looking here. If I want to take a look at what it's doing.

## 23:10

It looks like that. So I'm just reproducing that image that we saw using this function.

## 23:15

Yeah.

## 23:16

So with that, basically tucking everything together into one functions, we can now kind of move on
to some applications with step reactivities.

## 23:25

Things get a lot easier if we don't worry about that zero to one being steady state, jumping up in a
reactivity or jumping down and then like removing it.

## 23:32

So when I say step insertion of reactivity and like what the book means in Section 5.5 is, hey,
we're at critical.

## 23:40

We have the N-naught and we have the corresponding precursors.

## 23:43

What happens to the population of neutrons and the precursor concentrations if I insert immediately
rho equals something?

## 23:52

And what the magnitude of rho tells us is are we going up in population or down in population?

## 23:59

And then the magnitude of rho relative to beta will tell us essentially how rapidly that's
happening.

## 24:06

What time constant, what period are we going to go up on?

## 24:10

So we'll use these numerical results.

## 24:13

We'll use these numerical results from the ODE and solution in order to understand some of the
approximations that are shown in the book.

## 24:21

So as an example, let us assume that our step insertion of reactivity is beta over two, which for
U235 is reactivity equal to 0.00325.

## 24:34

What I want to do is estimate how much our neutron population increases just about immediately.

## 24:43

After I put in the step insertion of reactivity, right?

## 24:46

So we know at time equals zero, we're at our critical state and we're starting off at whatever
N-naught is, right?

## 24:52

In our case, it was 10 to the 8th.

## 24:54

What I want to do is based on the results of our numerical solution, I want to know how much it
jumps in that very small sliver of time, right?

## 25:04

That I before I called the prompt jump approximation.

## 25:08

So I'm going to go ahead and plot that solution here.

## 25:12

And I've chosen some numbers.

## 25:13

So that it should be pretty easy for us to estimate.

## 25:17

So can you see this in the back reasonably well?

## 25:21

I've tried the grid lines.

## 25:22

I hope guide your eyes.

## 25:23

Usually I'm not a fan of grid lines unless I'm trying to use the graph for some approximations,
right?

## 25:28

So we start off at time zero.

## 25:30

And of course, on this axis, we have one times 10 to the 8th, which is what I've used for my initial
condition.

## 25:36

I don't really care so much about the precursors here, right?

## 25:39

Really the blue curve for the neutron intensity is what I want.

## 25:42

Now, after I.

## 25:43

Insert that reactivity at time equals zero.

## 25:46

There's that initial very, very rapid jump in the neutron density before it goes on this much more
gradual slope, right?

## 25:57

Or I guess it's not a slope because it's an exponential, but it looks fairly linear on the scale.

## 26:03

So I jump from one approximately.

## 26:05

What is my population instantaneously after that insertion?

## 26:11

Just eyeballing it.

## 26:14

Yeah, it's increased by a factor of two.

## 26:17

All right.

## 26:17

Now, the question is, is this even remotely reasonable, right?

## 26:21

And is there a way for us to estimate that without relying on Python and ODE and to make this big,
messy plot, right?

## 26:30

Is there a way that we can go to the math and sort of estimate this a priori?

## 26:36

Well, it turns out that, yes, there is, right?

## 26:39

Because this is exactly what is called the prompt jump approximation.

## 26:43

So in the reading that you did for today, equation 563 gives us this relationship between the
magnitude of the reactivity that we're inserting.

## 26:53

So usually the verb used for these reactivity insertions is to insert, right?

## 26:58

It means we're putting something in to the system.

## 27:01

Now, that seems kind of weird because if I say I'm putting in the control rods, the reactivity I'm
actually inserting is negative.

## 27:08

So am I inserting negative reactivity or am I removing reactivity?

## 27:13

It's almost universally you're inserting negative reactivity.

## 27:18

So insertion of reactivity just means that you are making a change to the reactivity, okay?

## 27:22

It could be positive or it could be negative.

## 27:24

In this case, the n's represent the neutron population before n0, right, our initial condition, and
n1, which is that value that it gets to right after the large jump, okay?

## 27:38

So if we take that approximation, do we get the same?

## 27:43

Do we get the same value or, I guess, in a sense, is it consistent with what we just observed?

## 27:52

Okay, but actually, let's back up.

## 27:54

So is what we just observed consistent with this approximation?

## 27:59

You all estimated for me that n1 was 2 times 10 to the 8th, right?

## 28:06

It starts off at n0 is equal to 1 times 10 to the 8th, n2 is 2 times 10 to the 8th.

## 28:11

Does this make sense?

## 28:13

Does this equation give us that same ratio?

## 28:19

So what was our row?

## 28:23

Beta over 2.

## 28:25

So beta over 2 divided by beta is 1 over 2, right, 1 half, okay?

## 28:32

1 half, 1 half plus 1, is that correct?

## 28:45

That's incorrect because it's our, no, maybe it's 1 half equals 1.

## 28:51

What's that?

## 28:52

It gives you 1 half equals 1.

## 28:53

It gives you 1 half equals 1.

## 28:53

It gives you 1 half equals 1.

## 28:53

It gives you 1 half equals 1.

## 28:53

It gives you 1 half equals 1.

## 28:53

It gives you 1 half equals negative 1 half.

## 28:56

Right, so if this is, so this is 0, that's 1, 1 half, so that's 1 half minus 1 minus 1 half.

## 29:04

Is that correct?

## 29:05

Minus 1 half, and then we have, this is, so the absolute value of row over beta, did I get that?

## 29:18

I think I got that right from the book.

## 29:21

Is that correct?

## 29:22

Did I get it right at town?

## 29:23

Yeah, I put it in the book.

## 29:24

That's 5, 1, 6, 3.

## 29:26

Yeah, that's what I thought.

## 29:29

All right, so if I, let me actually, I thought I thought about this before.

## 29:35

So we'll make this a fragment.

## 29:41

Okay, so we know that the reactivity insertion was a positive beta, right?

## 29:46

So we have a 1 half on the left-hand side, and then we have a 1 over 2 on the right-hand side minus
1.

## 29:54

Where am I getting, why is that?

## 29:57

I'm going to have to look at that.

## 30:11

Wait, what does it say something?

## 30:12

Anyway, the magnitudes are correct there.

## 30:16

That's the important thing.

## 30:19

I wonder where the sign issue is.

## 30:22

I'm going to tuck that in the back of my mind and see if I can come up with the reason, you know, as
we go along, right?

## 30:30

But let's take the same prompt jump approximation and apply it to the opposite case.

## 30:34

So before we're pulling out some control rod, we're adding positive reactivity.

## 30:39

Let's see if the prompt jump approximation can help us when we insert negative reactivity, right?

## 30:45

That's what this example 3 that's coming up.

## 30:48

Okay, so I'm operating the reactor.

## 30:52

I'm sitting there at the reactor on top, right?

## 30:55

Who's been to the top of the reactor where you can look down in the pool, right?

## 30:59

You know, they're always very careful, like, to tell you, please don't drop things in there.

## 31:03

Well, I dropped my borated Android phone down there the other day, and this is what the population
of neutrons look like.

## 31:10

Okay?

## 31:10

So I went from 10 to the 8 neutrons down to, let's say, 0.67 or so times 10 to the 8, right, with
the precursors following suit.

## 31:22

What's the reactivity worth of my borated Android phone?

## 31:30

So without knowing, right, because this is a plot, obviously, that I generated with the same ODE in
stuff, but I haven't told you what my reactivity is.

## 31:39

Okay, so what would it be?

## 31:43

First of all, my initial...

## 31:44

My initial value, right, would be N naught is equal to...

## 31:48

We don't need the 10 to the 8, so it's just...

## 31:50

We'll call it 1.

## 31:51

What's my value after the fact?

## 31:57

Right, 0.6...

## 31:58

I would...

## 31:59

Let's say 0.66666, right?

## 32:03

Something like that.

## 32:05

Okay?

## 32:06

And so what then would be my reactivity?

## 32:13

Right, so I've got an N naught divided by N1.

## 32:20

That's N naught.

## 32:21

Divided by N1 minus 1, okay?

## 32:25

And then the reactivity that I'm inserting would be found by multiplying the right-hand side by
beta.

## 32:31

So my beta is whatever my sum of betas are.

## 32:34

So that ends up being 0.0065, as we've talked about, right?

## 32:38

So what do you all get when you execute that?

## 32:49

Yeah, definitely for these sorts of...

## 32:50

I know that they're in the slides, but I know that I see people with notes.

## 32:53

I'd sketch these down because this is a pretty...

## 32:56

Straightforward problem to answer.

## 32:58

Like, you could...

## 32:59

If I gave you a sheet of paper that had a plot on it,

## 33:02

and you could see the neutron density as a function of time,

## 33:05

and I ask you what reactivity insertion led to this,

## 33:09

this is totally something that you could do with pen and paper during a 50-minute exam, right?

## 33:15

I'm not hinting or anything, but totally, totally fair game.

## 34:01

Do we have a number?

## 34:05

0.03.

## 34:06

0.03.

## 34:08

I get something very close to that.

## 34:10

I get 0.00325.

## 34:13

What fraction of beta is that?

## 34:20

So it's the same reactivity we just saw.

## 34:22

It's in the other direction, though, right?

## 34:23

So we go down pretty significantly in that prompt jump,

## 34:26

and then we ride down on this long-lived tail due to the long-lived precursors.

## 34:41

So what's nice about the prompt jump approximation is you can...

## 34:47

To be able to map this blue curve, right, as an explicit function of time,

## 34:51

requires that we would solve those equations.

## 34:53

Now, what you're doing for the homework is analyzing the single precursor group equations, right,

## 34:58

where you don't have six different groups.

## 35:00

You just have one, like similar to what we would have seen last time with the bromine 87, right?

## 35:05

So with the prompted jump approximation, which is valid for...

## 35:10

From the reading, do you remember where this approximation is valid?

## 35:19

Think of it this way.

## 35:21

The prompt jump, this is a very, very fast time constant.

## 35:26

That has to be related to the prompt neutrons.

## 35:29

The rest of it is related to the delayed neutrons, okay?

## 35:32

And if you zero out far enough in time, whether it's a positive or negative insertion reactivity,

## 35:38

the time constant that this follows, which is called the reactor period,

## 35:41

is largely dictated by the delayed neutron precursor.

## 35:45

So what the prompt jump approximation does is it basically decouples the fast part of the kinetic
changes

## 35:51

and the slow part and lets you sort of do the immediate shift,

## 35:56

after which you can apply the sort of an E to the T over big T, where there's the period.

## 36:02

So it gives you a really, really rapid way to apply very simple approximations to understand the
data, right,

## 36:08

rather than having to go through the full solution.

## 36:10

So it's only valid, though, for some cases.

## 36:14

Do you remember what those cases are?

## 36:20

Where do you think it would be...

## 36:22

For what situations do you think it's true that the reactor primarily operates as though it's...

## 36:30

driven by delayed neutrons as opposed to the prompt neutrons, right?

## 36:35

What the prompt jump approximation is doing is saying,

## 36:38

hey, we know that there is an impact from the prompt neutron, like the fast stuff,

## 36:42

but it's finite, and after that change, we can assume everything is on a much slower timescale.

## 36:49

Where is that possible?

## 36:50

Could you do that if prompt neutrons were a heck of a lot more important than delayed neutrons?

## 36:56

No, right?

## 36:57

Where...

## 36:58

What system would...

## 37:00

In what system would delayed neutron precursors not really matter at all?

## 37:08

Well, you'd have to be just critical, right?

## 37:11

That's a good description.

## 37:15

You have to add one word to critical, one modifier.

## 37:24

A startup is an issue.

## 37:26

So it shouldn't matter about startup or...

## 37:29

Because this can happen at any point in time.

## 37:31

So kind of going on that critical.

## 37:33

So we know that at critical, rho equals zero, we're steady state.

## 37:36

If we go above rho,

## 37:38

we're going to go up on a positive period.

## 37:40

There's a difference, though, in what the magnitude of rho...

## 37:44

If we put in a little bit of reactivity, 0.001 or half a beta,

## 37:48

eventually we're going to go up or down in power based on the delayed neutron precursors, okay?

## 37:53

If we put in a reactivity insertion that is large enough

## 37:58

where the delayed neutron precursors are essentially not needed,

## 38:02

so that prompt neutrons are driving this exponential increase, okay?

## 38:08

That's when this would no longer be an appropriate approximation.

## 38:14

When would we have enough prompt neutrons to drive exponential growth?

## 38:26

Well, remember what k tells us.

## 38:28

K tells us the multiplication from generation to generation, okay?

## 38:32

So if k is equal to one, then we have one after another after another.

## 38:36

If k is greater than one, we'll have more than one.

## 38:38

Now, we know that of those new ones that are produced at every generation, some small fraction,

## 38:43

are the delayed neutrons, right?

## 38:45

What we would need then is if we go from one generation to n new ones, right?

## 38:52

Let's say k is 1.01, okay?

## 38:55

We know that we have 0.01 more neutrons than we started with.

## 39:00

We have to peel off some delayed neutrons, right?

## 39:02

Because they don't actually show up right away.

## 39:04

They're going to show up in the future, right?

## 39:06

Because we're starting at steady state, but we've done something now.

## 39:08

We're going to go up exponentially.

## 39:10

So if we peel off the delayed neutron precursors, which have...

## 39:13

A fraction of what?

## 39:17

0.006 and change, right?

## 39:20

If my k is 1.01, which means my reactivity is about 0.01,

## 39:25

then 0.01 minus the delayed neutron precursor fraction still leaves me with something like 0.03.

## 39:35

That means that the delayed neutron precursors, even though they'll contribute,

## 39:38

aren't necessary to keep going, because I can still move forward increasing exponentially

## 39:43

if I have...

## 39:44

If I have...

## 39:44

If I have...

## 39:45

If I have k equal 1.03 or reactivity equal 0.03, right?

## 39:49

So that means that if the reactivity I insert is greater than beta,

## 39:53

then I am self-sustaining this exponential growth based on prompt neutrons alone.

## 39:59

And if I'm doing it with prompt neutrons alone,

## 40:01

I don't care about the delayed neutron precursor lifetimes.

## 40:04

And their impact on time is no longer relevant.

## 40:09

So I go up on a period that looks a hell of a lot like the prompt neutron lifetime.

## 40:14

So when you...

## 40:15

When you say critical, you're right.

## 40:16

It's the difference, though, between critical, as we've talked about in class,

## 40:20

for steady state, you know, sort of reaction rate analyses.

## 40:23

In this time domain, there are two steps of criticality that we can define.

## 40:27

One is delayed critical, and one is prompt critical.

## 40:31

Prompt critical means that you can go into exponential growth without...

## 40:36

Like, you could just delete beta.

## 40:37

You could say, hey, all these delayed neutron precursors, I'm putting a curse on you.

## 40:41

You can't come out anymore, right?

## 40:44

So you're necessarily...

## 40:45

You're modifying new bar, right?

## 40:48

You're reducing new bar if you do that.

## 40:50

New bar is part of the definition for K.

## 40:53

So in order to be prompt critical, you have to be K greater than 1 with that adjusted new bar,

## 41:01

or what we call new bar sub P, the prompt new bar, right?

## 41:04

That's what will get you to prompt critical.

## 41:06

So it's only in those cases where your reactivity is between 0 and beta,

## 41:12

where something like the prompt jump approximation would...

## 41:15

Even possibly be valid.

## 41:17

And I would say that it's actually for betas that are...

## 41:19

Sorry, rows that are quite a bit smaller than beta, right?

## 41:22

Here, it seems to be working pretty well, even though our row is half a beta, right?

## 41:29

That's a fairly large chunk of beta.

## 41:32

And we're getting a number that is accurate, right?

## 41:35

Because that's what I use.

## 41:36

So if I increase that from half a beta to, say, 90% of beta,

## 41:40

we would still get a reasonable approximation,

## 41:43

but it would be less...

## 41:45

And if I went all the way to row equal beta,

## 41:48

well, then I don't really have a prompt jump anymore

## 41:51

because I'm going immediately into fast exponential growth, okay?

## 41:55

For positive, right?

## 41:56

If we're doing negative, you're always limited by the delayed neutron precursors.

## 42:04

All right.

## 42:05

Another topic that shows up in the book is the reactor period.

## 42:10

So remember, the reactor period represents the time constant such that we go from...

## 42:16

Basically, we go from...

## 42:17

Basically, over one period, your population changes by a factor of E, right?

## 42:24

It could be...

## 42:25

And usually, period applies...

## 42:27

We don't care about periods when we're going down in power.

## 42:29

We only care about periods as we're increasing in power.

## 42:32

So the reactor period T is the time it takes for the neutron population

## 42:36

to increase by a factor of E, okay?

## 42:40

So in the book, there are two approximations for the period

## 42:43

depending on the amount of reactivity that we insert.

## 42:46

So if we put in a very small...

## 42:47

If we put in a very small amount of reactivity,

## 42:48

then we expect to ride along a period that is dictated by the delayed neutron precursors.

## 42:55

If we put in a large amount of reactivity,

## 42:57

then, like I just said, we don't care about the delayed neutron precursors

## 43:00

and we go up on something that looks a lot closer to the prompt neutron lifetime.

## 43:04

So if I put in a reactivity of 0.001, right?

## 43:07

That's pretty small compared to beta.

## 43:10

What would my period be based on this plot?

## 43:16

All right.

## 43:16

So we'll take a look at that.

## 43:17

And hopefully, I've made things right.

## 43:23

Let me get rid of that, okay?

## 43:26

So what does the period look like based on this plot, right?

## 43:30

So if I...

## 43:32

Can you see it in the back?

## 43:35

I think this might be a little bit smaller than the other one had been.

## 43:38

So I'll zoom in a little bit, okay?

## 43:40

So I start again at 10 to the 8th.

## 43:42

I jump up immediately.

## 43:44

And then I ride what appears to be a fairly long period of time.

## 43:47

And then I ride what appears to be a fairly straight line, right?

## 43:48

It helped along by the fact that I'm on a log scale, okay?

## 43:52

So this works out pretty nicely because at 40 seconds,

## 43:56

I cross one of these grid markers.

## 43:58

And then at 100 seconds, I also cross one of the grid markers.

## 44:01

So that means that between 40 seconds and 100 seconds,

## 44:05

I am going from...

## 44:06

See, this is 1, 2, 3.

## 44:09

So 3 times 10 to the 8th up to 4, 5, 6, 7, 8, 9, right?

## 44:15

So I'm going from 3 to 9.

## 44:17

And 9 over a span of 60 seconds.

## 44:22

So what does that mean my period is?

## 44:26

Just based on those numbers.

## 44:41

How would I use those numbers?

## 44:52

Any ideas?

## 44:55

Clay?

## 44:56

The slope of the line would be...

## 45:01

The log of the slope or the...

## 45:04

If I took the neutron population and the logarithm of the neutron population,

## 45:10

then I would have an exponential constant turn.

## 45:12

I would have an exponential constant to the slope, right?

## 45:13

So mathematically, how do I model this?

## 45:18

What am I looking for?

## 45:19

I have an initial population.

## 45:21

I have a final population.

## 45:23

I have an initial time and I have a final time.

## 45:26

What relationship, mathematical relationship,

## 45:28

should these four quantities satisfy?

## 45:31

If I'm to find the period.

## 45:34

Would you agree that it should satisfy something like

## 45:38

I have n at 100,

## 45:42

is equal to n at 40 seconds times e to the 100 minus 40 over t.

## 45:55

I should put my other dollar sign.

## 45:58

Do you believe that, right?

## 46:01

If this is exponential growth,

## 46:02

but the period is only telling me how it's like

## 46:04

once I'm on an asymptotic curve, right?

## 46:08

That's an important term that's used in the book.

## 46:10

You'll always have some kinetic,

## 46:12

wiggle, right?

## 46:13

Because we've got seven different unknowns

## 46:15

that are evolving in time that drive the solution, right?

## 46:17

It's only after a certain amount of time

## 46:19

that things sort of die away.

## 46:21

The higher order terms die away

## 46:23

and you're left on this one single asymptotic positive period.

## 46:28

So obviously things are wiggling around here, right?

## 46:31

We have changes in the precursors

## 46:33

and they only start to look sort of,

## 46:35

I don't know, constant right around that 40 second mark.

## 46:38

So it's a good coincidence

## 46:40

that that's one of the points that we have, right?

## 46:42

Everything after that looks like it's going up

## 46:44

sort of in a steady period, okay?

## 46:47

So yes, this is the equation that we would want.

## 46:50

So where you say slope plate,

## 46:52

it's by taking the log of both of these things.

## 46:55

So I could take, let's see,

## 46:58

the log of n over 100, n of 140.

## 47:03

This would give me this quantity here, okay?

## 47:10

And then I can solve for t,

## 47:12

t with that.

## 47:13

So can somebody do that for me?

## 47:15

Take that balance equation

## 47:17

and tell me what t must be.

## 47:29

What is e numerically?

## 47:35

Right, so circa three for my simple neurons.

## 47:40

So if I'm in 40 to 100 seconds, that's 60 seconds.

## 47:43

So 60 seconds to go up by a factor of e.

## 47:50

So I'm going from three to nine.

## 47:56

That is roughly two of these exponential terms.

## 48:00

So I would, just thinking of it that way,

## 48:02

I would expect a period of something like 30 seconds,

## 48:06

but I could be wrong.

## 48:08

What do you get numerically?

## 48:11

Well, 54.

## 48:12

54 seconds?

## 48:27

Anybody get something different?

## 48:31

In this case, let me do mp log of,

## 48:34

see, it's nine over, what was it, three.

## 48:39

And that gives,

## 48:40

and then 100 minus 40,

## 48:43

that gives me one over t.

## 48:44

So I have to take one over this whole thing.

## 48:47

And I get, yeah, so 54 and change.

## 48:51

Right, so my mental math is not,

## 48:53

that's the problem when you're dealing with exponentials,

## 48:55

but you can't think linearly.

## 48:56

That doesn't work out like that.

## 48:58

So anyway, 54 seconds.

## 49:00

Now, what do we get if we use the approximation from the book?

## 49:07

Approximation in the books of beta would be my 0.0065.

## 49:11

Okay.

## 49:13

And then I'm adding reactivity at 0.001.

## 49:16

And then my lambda,

## 49:18

what was our effective lambda from earlier in the slides?

## 49:22

You write that down?

## 49:25

0.076.

## 49:26

0.776?

## 49:29

No, 0.766.

## 49:30

0.766?

## 49:32

Yep.

## 49:32

That's right.

## 49:34

Okay.

## 49:34

If I do that, that's 84 seconds.

## 49:37

So I was actually surprised.

## 49:39

So I had computed these numbers as I was prepping the slides earlier.

## 49:42

So I had computed these numbers as I was prepping the slides earlier.

## 49:42

So I had computed these numbers as I was prepping the slides earlier.

## 49:43

Certainly, I've seen that approximation 557 before,

## 49:47

and the one that is in the next slide.

## 49:49

Obviously, 84 seconds is bigger than 54 seconds, right?

## 49:53

Right order of magnitude.

## 49:55

But it tells you very clearly that this is an approximation, right?

## 50:00

Now, maybe it would be if I took this out longer, right?

## 50:04

So I'm only taking this out to about 100 seconds.

## 50:07

We know that the half-lives of the longest-lived precursors,

## 50:10

like bromine 87, have a half-life of 50 seconds.

## 50:12

We know that the half-life of 50 seconds.

## 50:13

So if I am out to this point, it could be the case that the longest-lived precursors

## 50:22

haven't actually reached their asymptotic values yet.

## 50:25

Whatever change they're going to make is still pretty small, right?

## 50:29

So the precursor, that C1 here, I believe that's that V curve.

## 50:33

So maybe it just hasn't reached its asymptotic value yet.

## 50:36

If I took this out further, maybe I would get something closer to 84.

## 50:40

Now, this approximation, given their,

## 50:42

in 557, is only, like, exact in the limit that rho goes to zero, right?

## 50:50

Where we're just slightly off steady state, right?

## 50:55

So it's an approximation, but I don't know.

## 50:59

Somehow, they seem consistent, okay?

## 51:02

Same thing is true for the long, so the other approximation,

## 51:07

where things ride up much more quickly.

## 51:08

So same thing.

## 51:11

I'm riding up on a positive.

## 51:12

Period.

## 51:13

But now my rho, my reactivity, is greater than beta, right?

## 51:17

This is the 0.01 that I'm talking about.

## 51:19

If I look at this, I've started off at my 10 to the 8,

## 51:23

but the very first horizontal line is 10 to the 10, 10 to the 14,

## 51:26

all the way up to 10 to the 30, okay?

## 51:30

0.01 is not that much bigger than beta, but because it is bigger than beta,

## 51:35

I don't need the delayed neutron precursors.

## 51:37

They're not slowing me down anymore.

## 51:38

I'm riding up on a period that is governed

## 51:42

by my precursor.

## 51:43

I'm riding up on a period that is governed

## 51:44

by the prompt neutron lifetime, or the generation time, big lambda, okay?

## 51:48

So if I take a look at this, I could do the same sort of, you know,

## 51:51

approximation work at 0.7 seconds.

## 51:54

That's the other thing here.

## 51:55

I'm going up in a large amount, and it's over a very short amount of time, right?

## 51:59

So at 0.7 seconds, I'm at 10 to the 30.

## 52:02

At 0.3 seconds, I'm at 10 to the 18.

## 52:06

10 to the 30, 10 to the 18, that's 12 orders of magnitude

## 52:11

in the span of 0.4 seconds.

## 52:12

Without even doing the math, we know that that is an incredibly short period.

## 52:19

It doesn't take much time at all to increase by this factor 2.71 or whatever, right?

## 52:23

Because we have to do that so many times to get up to 12 orders of magnitude, 10 to the 12, okay?

## 52:28

So I'll let you plug in those numbers and see for yourself what that looks like.

## 52:33

I do want to say just a little bit about the problem that you're tackling in the book.

## 52:41

This is what you're tackling.

## 52:42

In problem 5.10, it's the precursor equations with one precursor.

## 52:47

So it's the same form, right?

## 52:49

It's just now we don't have the sum i, okay?

## 52:52

There are a variety of ways that you can solve this, but the basic procedure is the same,

## 52:59

right?

## 53:00

Of course, write down your equations and then identify the type and any special features.

## 53:05

Finally do the integration, right, which basically means find what the solution form is.

## 53:11

Okay.

## 53:12

So that's the first step, right?

## 53:13

Because once you have that, then you can figure out how to apply the initial conditions, okay?

## 53:19

So for a system of equations like the one we have, there are three options.

## 53:24

One is you can go to higher order equations.

## 53:27

So I know you've solved second order equations before.

## 53:31

Now remind, I guess, tell me if I'm right about what you would have done.

## 53:35

You have a second order equation, and then you end up finding something called the indicial
equation.

## 53:42

Basically, it's a second order algebraic equation, so quadratic.

## 53:46

It's quadratic, and you find two roots, and those roots are the constants inside of exponentials.

## 53:52

Does that sound vaguely familiar?

## 53:55

I think we call it the indicial equation, maybe the characteristic equation.

## 53:58

But whatever it is, you get two roots.

## 54:01

And if you get a shared root, like you get the same value of the root, then you have

## 54:05

to modify one of the functions, and now it's like t times e to the something t.

## 54:09

Does that ring a bell?

## 54:11

Okay.

## 54:12

We shouldn't have that issue.

## 54:14

Those roots of that equation that you probably remember doing, that's the same thing as taking

## 54:19

the matrix A that I've shown for the system of equations, finding its eigenvalues.

## 54:23

Same roots.

## 54:25

In this case, the integration of the equation is basically writing down the fact that the

## 54:30

solution is a sum of exponential terms, right, where the constant in each of the exponentials

## 54:36

comes from some quadratic equation or equipment.

## 54:40

Okay.

## 54:41

I took a look, and this is why I was asking at the beginning.

## 54:43

I took a look at Dr. Bennett's notes.

## 54:47

Anybody have Dr. Bennett for 340?

## 54:50

Did you use his online textbook?

## 54:54

It was during Zoomland, so I'm not really sure.

## 54:58

Yeah.

## 54:59

I put that in the recesses of my memory too, Zoomland I'm talking about, right?

## 55:04

So looking at his book, he doesn't talk about the matrix stuff specifically because he's

## 55:10

like, God.

## 55:11

This requires some math, some matrix analysis, 551, which I know you've also had, or most

## 55:16

of you would have that by now.

## 55:17

So instead of doing it the way that I would have done it, he uses Laplace transforms,

## 55:22

right?

## 55:23

And you can do that.

## 55:24

And in the end, it works out the same way because what are you doing in all of these?

## 55:28

You're solving for the eigenvalues of a two by two matrix, whether or not you want to

## 55:33

call it that, right?

## 55:34

So with the Laplace transform, you get it into the S space instead of the T space.

## 55:40

You end up with a Laplace transform.

## 55:41

You end up with a linear system of equations, and then you have to do some inverse transforms.

## 55:45

I don't remember Laplace transforms well enough to just write down the equation and go at

## 55:50

it, but it seemed reasonable enough.

## 55:52

So what you're doing for the problem is either just assuming the exponentials, right?

## 55:58

So you can assume, for instance, that N is equal to E, we'll call it some constant A.

## 56:06

So A times E to the alpha one E to the alpha one, right?

## 56:07

So that's what you're doing, right?

## 56:08

So you're assuming the exponentials, right?

## 56:09

So you can assume for instance that N is equal to E, we'll call it some constant A. So A times

## 56:10

E to the alpha one T plus B times E to the alpha two T, right?

## 56:15

And for the precursor, it'll be something similar.

## 56:17

It'll be C is equal to, let's say, A prime E to the alpha one T plus B prime E to the

## 56:25

alpha two T, right?

## 56:26

Where the A and the A prime and the B and the B prime, those are the constants that

## 56:32

you don't know right away.

## 56:34

That's where you apply your initial conditions.

## 56:35

And then you get, obviously in this case, you'd get a system of equations that would

## 56:39

let you solve for A, B, A prime and B prime, okay?

## 56:44

So you can take these solutions, plug it right into the single group precursor equations,

## 56:50

and you'll end up with something for alpha, right?

## 56:54

You'll have some quadratic equation that looks like A alpha squared plus B alpha plus C,

## 57:02

right?

## 57:03

So if you plug in E to the alpha T to those equations, you'll end up with a quadratic.

## 57:08

Okay.

## 57:09

So if you plug in E to the alpha T to those equations, constants alpha, that's when you

## 57:12

can start to make the approximations that the problem statement tells you to do, right?

## 57:16

You could take it all the way and it's just, it's a messy looking solution.

## 57:20

What the book problem is trying to have you do is make some good approximations at that

## 57:25

point before you substitute the alphas back into the exponentials and you get a simpler,

## 57:30

a simpler solution.

## 57:32

And I think they, does he write it down?

## 57:37

Where is it?

## 57:39

Problems.

## 57:40

So problem five, 10.

## 57:41

Yeah.

## 57:42

So this is the solution that you'll end up with.

## 57:45

This is not the exact solution, right?

## 57:47

If I were to take like, and solve this like fully, it's going to be some ugly looking

## 57:53

expression, right?

## 57:54

And that's because they're, they're tightly coupled.

## 57:56

The neutrons depend on the precursors, the precursors depend on the neutrons.

## 58:00

This is different from when we had a activation where we had something like uranium, I see

## 58:06

that the thorium problem, right?

## 58:07

So thorium absorbs neutrons.

## 58:08

Neutron turns into protectinium, turns into uranium, that protectinium doesn't depend

## 58:14

on the uranium.

## 58:15

The thing it decays into, right?

## 58:16

The uranium depends on the protectinium, not the other way around.

## 58:20

That means that the matrix that would look like the matrix we have is lower triangular,

## 58:26

which basically means that you can solve the first one and solve the second one and each

## 58:31

of the other ones, right?

## 58:32

Because it's a one way direction in decay land for this set of equations, the precursor

## 58:38

is drive the neutrons, the neutrons drive the precursors.

## 58:42

So it's necessarily more challenging, right?

## 58:46

This approximation makes it a little bit easier, right?

## 58:50

So that this, the solution here will be, it'd be pretty good for a reasonable range of values

## 58:58

of rho, where rho, you know, should be less than beta and then has you think about that

## 59:03

a little bit more.

## 59:04

So it's a challenging problem, but hopefully this gets you.

## 59:07

Yeah.

## 59:08

Taking a step in the right direction for that, right?

## 59:10

Because I understand that you probably can't just sit and write down the full solution,

## 59:15

right?

## 59:16

This gives you something that you can't manage.

## 59:17

Does that make sense?

## 59:20

In principle, I know it was like the solution that you're looking at won't make sense until

## 59:23

you get to it, but hopefully this helps.

## 59:27

Okay.

## 59:28

Well, thanks for accepting a little bit more of my time for free.

## 59:33

Again, I'll send you a bill later, if you're not kidding.

## 59:37

We'll pick up on it next time.

## 59:39

We'll finish up anything that you have questions on.

## 59:42

I will have the homework solution for what was due last night ready to go.

## 59:48

I have it ready.

## 59:49

I just have to post it.

## 59:50

And then I will have the solution to this homework ready to go right away when you submit

## 59:55

it on Wednesday.

## 59:56

Right.

## 59:57

So I'll have it automatically posted at midnight, which means that you have to submit it by

## 01:00:00

Yeah.

## 01:00:01

The post the time, right?

## 01:00:03

That way you have a full, you know, you're going to be able to submit it by the end of

## 01:00:06

the week.

## 01:00:07

So it's going to be a full day and a half or so to review the solutions to that.

## 01:00:11

But I would say that for the exam, the stuff that we do in class, the sort of engineering

## 01:00:15

judgment is probably the most important thing to focus on.

## 01:00:21

Thank you.

## 01:00:22

Thank you.

## 01:00:23

Thank you.

## 01:00:24

Thank you.

## 01:00:25

Thank you.

## 01:00:26

Thank you.

## 01:00:27

Thank you.

## 01:00:28

Thank you.

## 01:00:29

Thank you.

## 01:00:30

Thank you.

## 01:00:31

Thank you.

## 01:00:32

Thank you.

## 01:00:33

Thank you.

## 01:00:34

Thank you.

## 01:00:35

Thank you.

## 01:00:36

Thank you.
