# L39_02 Local Audio Transcript

Course: NE 630

Playlist source: https://youtube.com/playlist?list=PLy481lNHlnHoEO95vM-xYX2bydD25v20L

Video: NE 630 - Lesson 39

URL: https://www.youtube.com/watch?v=akfZqLH-l20

Video ID: akfZqLH-l20

YouTube upload date: 20231204

Duration: 53:43

Transcript source: Local faster-whisper transcription from YouTube audio.

Whisper model: large-v3; detected language: en.

Generated: 2026-06-28

Note: This transcript is machine-generated from audio and lightly wrapped only. It should be reviewed before being quoted, published, or used as polished lesson text.

Requested language: en

## 00:24

all right so is everyone feeling sufficiently dead for dead week yes yeah that makes 23 of us

## 00:33

i am definitely ready for uh it's being done i'm so frustrated with this math class that i keep

## 00:41

talking about like it was yet another sunday where i'm sitting down because i put off the

## 00:46

homework and i have to sit down to do the homework and it's like the hell does this have to do with

## 00:49

anything and i know that it's really um sometimes funny that the instructor at the front of the room

## 00:58

would say that because i'm sure but i mean we can talk specifically about that like if you if you

## 01:06

actually have to have a time where you're like thinking maybe something similar to what i just

## 01:11

uh shared then that's something that i want to know because i have already started writing a

## 01:17

novel for my own t of alice

## 01:19

to give to them mostly because you know i i look at this as i mean one somebody's paying money

## 01:27

somehow for me to take the class i'm not paying it's free for the employees and employee spouses

## 01:32

and things like that uh but you know what does it take for me to actually sit down and enroll in a

## 01:38

class personal interest right i don't i'm not looking for a degree that's not the point here

## 01:44

like i i have degrees i'm gainfully employed it's purely

## 01:49

intellectual interest like lifelong learning i hope many of you will be lifelong learners

## 01:54

but then when i find myself engaged in the material line it's like roadblock after roadblock

## 02:00

it starts to get unfun and when that happens learning goes down the drain right there's

## 02:07

there's a huge um there's something to be said about learner motivation and so i'm incredibly

## 02:14

sensitive to that concept that does not mean that i am the greatest at

## 02:19

ensuring learner motivation but i'm aware of it right and so because i'm aware of it that means

## 02:25

i'm receptive to that i recognize that there are probably times when learning motivation has been

## 02:31

maybe not as strong as i want it to be and the only way that that's going to change going forward

## 02:37

is if i know when that's happening and have feedback i mean that that's not to say that

## 02:43

there shouldn't be hard work right but sometimes work is harder than it should be there's a very

## 02:48

important nuance

## 02:49

there right so as an example sometimes playing with vessel functions is harder than it should be

## 02:55

if you don't know a specific trick and uh so we'll we'll touch on on that so that that's just a very

## 03:03

like simple example right and it's timely because you're all playing with uh vessel functions um so

## 03:10

anyway why don't we dive in um to to the stuff today and uh i'll give a just a an overview of

## 03:19

what we'll do next and then we'll move on to the next slide

## 03:19

we'll move on to the next slide

## 03:19

this week this week should be pretty light yeah didn't we have so we're due today

## 03:23

no okay right uh so i i had so originally i had in canvas notes for this week then i deleted it

## 03:30

because this is there's nothing specific that you were supposed to prepare for today okay i think i

## 03:35

asked you to read 6.6 or something on the diffusion validity right and we'll look a little

## 03:41

bit at that today um and certainly we can we can talk in more depth than maybe i even planned if

## 03:49

there are

## 03:49

uh pertinent questions so last time we talked about reactor control and specifically

## 03:56

how we can model the impact of control insertion using perturbation theory right so the section

## 04:04

itself didn't really describe a whole lot about what certain control elements might look like

## 04:09

but what it did describe is how mathematically or computationally some combination of both of them

## 04:16

you would be able to estimate the impact of control now

## 04:19

why is that important to you i don't know i don't know i don't know i don't know i don't

## 04:19

know i don't know i don't know i don't know i don't know i don't know i don't know i don't know

## 04:19

why is that picked out as something specific to to consider well use of control is sort of all the

## 04:26

time in reactors right i've said this before you always have excess reactivity so you always got

## 04:32

to balance uh the the reactivity and the way to do that is with control and so uh one way to do

## 04:39

that is to just resolve everything for every perturbation but as you probably saw from the

## 04:45

notes from last time because i uploaded some new slides i took the slides that we had and i put them
in the

## 04:49

chat that we used last time and i added a bunch of stuff at the end of it as i said i would and it

## 04:55

you know it sucks to resolve the problem so it's nice to be able to make a simple um change using

## 05:02

perturbation theory or see what the impact of simple changes right so that's what we did last

## 05:06

time and i'll review that in a moment today we're going to look at some results from numerical

## 05:11

solutions to answer really two questions like what what does the flux look like in this two group

## 05:17

problem you saw possibly

## 05:19

An approximation for that in the material from a couple of times ago, right?

## 05:23

Using the one and a half group theory, there's an approximation that gets rid of that thermal

## 05:27

flux equation, but that also gives you a way to define what phi sub two is, the thermal

## 05:33

flux.

## 05:34

It's not a perfect approximation, but as we'll see in an asymptotic sense, it's not bad.

## 05:39

And then we'll also see when is diffusion theory good, right?

## 05:42

We've seen solutions to the diffusion equation, but we have no basis to compare it to like

## 05:47

reality.

## 05:48

Like what does reality look like for these same model problems?

## 05:51

We'll stick with slabs, right?

## 05:52

Because slabs are easy to see because it's 1D.

## 05:55

And then really for the next two times, and even as part of today, we'll just do review

## 06:00

and practice.

## 06:01

I have yet to write the final exam, but I think based on some of the stuff we do this

## 06:07

week, I'll have pretty good ideas of what we ought to include in it because I want to

## 06:11

make sure that you all have a final chance to show me all of that learning that you've

## 06:16

done.

## 06:18

All right, perturbation theory.

## 06:22

One of the things I added to the slides last time was a bit on how we would do perturbation

## 06:28

theory without the form that's in the book.

## 06:31

Okay.

## 06:31

And it went back to this basic expression for K is gains to losses, right?

## 06:36

So we have some generation of vision neutrons divided by losses from absorption and leakage,

## 06:41

right?

## 06:42

So if we know what the flux is, we know what the cross sections are, and we know what the

## 06:47

leakage is, which really comes from the flux and cross sections, then we know what K is,

## 06:52

right?

## 06:53

That's just, you know, you insert the right-hand side and you get the left-hand side.

## 06:56

We assume we've already found the critical width or buckling or whatever it might be,

## 07:01

and we get K.

## 07:03

Now, if we have this perturbed cross section, right, we insert the control element just

## 07:07

a little bit into the core, right?

## 07:09

We're not increasing it by a factor of three or something, just a small percentage change.

## 07:15

The sort of basic question is, how do we do that?

## 07:17

The question is, what happens to K, right?

## 07:20

How much does our reactivity change?

## 07:22

And the naive approach, which we had sketched on the board, was, hey, why don't you just

## 07:27

take that flux that you have and insert it into that perturbed cross section into that

## 07:34

equation we just saw?

## 07:35

And if you work it out, the difference between your original K and your new K, which is represented

## 07:41

by this delta rho, is given by this expression, right?

## 07:44

And really, if you look at it, it's just that it's a statement.

## 07:47

It's a statement that says, hey, I'm going to add up all the change in absorption and

## 07:52

divide that by the number of neutrons I'm generating, right?

## 07:55

Of course, there's a negative sign.

## 07:57

We know reactivity will go down if this thing is positive, okay?

## 08:00

And that's just a statement of, let's use our original flux and put in our other cross

## 08:05

sections to this balance equation.

## 08:06

And it seems reasonable, right?

## 08:08

It's still gains to losses.

## 08:09

Now, our gains are staying the same.

## 08:11

Our losses are perturbed just a little bit.

## 08:13

And we get this.

## 08:15

Now, is that a good?

## 08:17

Approximation?

## 08:19

It'll probably be in the right direction, right?

## 08:21

As long as that flux, as long as the perturbation in the cross section doesn't change the flux

## 08:26

too much, you'd expect this to be reasonably good, okay?

## 08:30

And as the numerical results in the slides that I uploaded show, you know, it's not terrible.

## 08:36

But the thing that we can do with this first order perturbation theory is instead of just

## 08:41

taking these integrals as they are, we instead weight things, right, with this thing called

## 08:47

the adjoint flux.

## 08:49

And what we found from the book is this thing is actually equal to the flux.

## 08:53

We're talking about one group theory.

## 08:55

And actually, I shouldn't have this, but we're not caring about the change in the fission

## 08:59

cross section.

## 09:00

But that's the first order perturbation estimate for it.

## 09:03

It's the same thing, only now we have P star inside the integrals.

## 09:08

And again, for one group diffusion theory, that's just equal to the flux.

## 09:11

All we're doing is weighting the change in sigma A, that delta sigma A.

## 09:16

We're weighting it.

## 09:17

We're weighting it where the flux is largest.

## 09:19

And if we're talking about, like, let's say, a slab reactor, the flux, assuming vacuum

## 09:27

on the sides, is going to be largest in the middle, right?

## 09:29

So that means that more fission is happening in the middle.

## 09:32

That means that if your delta sigma A is happening in the middle, it should have a bigger impact

## 09:37

on the neutron population, right?

## 09:40

Because those neutrons aren't going anywhere.

## 09:42

They're causing fission.

## 09:43

They're not near the boundary where they could be leaking, right?

## 09:46

Right.

## 09:46

And it was all about that concept of importance, okay?

## 09:51

I'll point out that this idea of this adjoint flux, the importance, is pretty important

## 09:58

in the development of something called the point kinetics equation.

## 10:03

So when we did neutron kinetics before with the neutron density and then the precursor

## 10:08

densities, we just sort of, like, ad hoc wrote down those equations, right?

## 10:13

There was not a whole lot of formal derivation.

## 10:16

If you want to formally derive those equations, you have to do it using the adjoint, right?

## 10:21

And that will give you all sorts of these weighted expressions, right, like integrals

## 10:27

over absorption, integrals over fission, and those lead to things like big lambda, the

## 10:32

mean generation time, the reactivity, right?

## 10:36

All those parameters that show up in those equations you can formally derive from, like,

## 10:41

the multi-group diffusion equations with this concept of adjoint, right?

## 10:45

That's beyond.

## 10:46

That's beyond our scope and would be something that we'd cover in, say, neutronics or something

## 10:50

at the grad level.

## 10:54

Any questions about that stuff, the perturbation theory?

## 11:00

Sort of an isolated topic, right?

## 11:03

But I think it's an important one.

## 11:07

First of all, the homework, I'm extending it to Wednesday.

## 11:10

There's no point in having it due tonight.

## 11:13

I think I saw a couple folks had uploaded it.

## 11:16

If you need to revise, go ahead.

## 11:19

Definitely check out the slides from last time.

## 11:22

And then anybody get to this point and find themselves stuck?

## 11:28

Yeah.

## 11:29

Did you get past it?

## 11:30

I mean, maybe I cheated.

## 11:32

I used Python.

## 11:33

I used SymPy.

## 11:34

SymPy, yeah.

## 11:35

And SciPy.

## 11:36

Yeah.

## 11:37

So you can do that.

## 11:38

I mean, so you've all been trying to use SymPy and sometimes abusing it, right?

## 11:43

But to evaluate an integral, it's totally fine to do.

## 11:46

I guess now that it's been.

## 11:47

Suggested, we could do that.

## 11:49

Well, first of all, if we take this integral, I mean, you recognize it's U, V, integral, V, D, U.

## 11:59

What is that concept?

## 12:01

By parts, right?

## 12:03

So if you do that, then you get this term and then you get this.

## 12:06

Then you would have to take this integral, do integral by parts once more.

## 12:10

And as it's fairly common, I think, in these integration by parts, you end up when taking.

## 12:17

This one and doing integration by parts, you end up with the same integral, right?

## 12:21

With a reverse sign.

## 12:23

And so you bring it over and it's two times that integral equals something.

## 12:26

So that's something divided by two is given this.

## 12:29

And as it turns out, it looks exactly like this only it's with J one, right?

## 12:35

And the only thing you need to do to do these integration by parts are the rule that I gave as a
hint.

## 12:41

And then the previous rule for differentiation of J zero, that was in, I think the lesson.

## 12:47

In 35 stuff, okay, but if we want, we could certainly, um, let's see where do, do, do, do, do, do
what fragment here?

## 13:09

Okay.

## 13:09

Yeah.

## 13:09

So if I want, uh, imports in PI as S Y X equals side at symbols X, and then side dot, uh, integrate.

## 13:23

X times side dot vessel J zero and X where that, and what I end up with is that if I can blow that
up just a little bit, it's not going to let me scroll, is it?

## 13:39

Oh, well show math as tech commands, take that, and then I'll say that this is equal to that.

## 13:54

Okay.

## 13:56

Boom.

## 13:57

So that's something where simply is totally appropriate, right?

## 14:00

Cause when I wrote this problem statement, I assumed it was totally doable with the hint that I
gave.

## 14:06

It was like one of those sort of engineering judgment things where it's like, I hope for the best
and I wasn't wrong.

## 14:13

You can get it without looking up any other properties, right?

## 14:16

The vessel functions, like many other things have a whole bunch of properties, recurrence
relationships.

## 14:21

So you can go from J zero J one to J two, so on and so forth.

## 14:24

Like the genre polynomials, I suppose, similar to things like signs and co-signs with double angle
addition, all that kind of crap that these special functions have, um, you didn't need anything
special like that.

## 14:37

So don't be afraid one to use tools like SimPy, um, for things like this, but I do notice that there
is a difference between this.

## 14:46

And then some of the other stuff I've seen is you've been using SimPy where I've been using SimPy
sort of like the, here's the model let's apply it to this.

## 14:54

Okay.

## 14:55

Similar problem.

## 14:56

This is something that's a little bit unknown, right?

## 14:58

So you've got to remember sometimes that the tools that you're picking up along the way, you don't
have to use them in exactly the same way that you learn them, right?

## 15:07

The purpose of a hammer, of course, is probably to hit a nail in, but I can definitely use it to,
uh, break up an old fax machine that caused me grief, right?

## 15:17

So be, be, be willing to, to, to, to go nuclear on, on things with the tools that you have.

## 15:24

All right.

## 15:25

Any other questions related to that?

## 15:30

Hopefully that, that gets you in the right direction.

## 15:34

Um, and so you're, you said you're finished, you got this and do you have numbers that made sense?

## 15:40

Yeah.

## 15:42

Good.

## 15:42

Good, good, good.

## 15:45

All right.

## 15:46

So next thing is the two group diffusion stuff.

## 15:51

Now we didn't cover how to solve the two group diffusion equation directly.

## 15:57

Except for that one case of the bear slab where we have the zero flux condition.

## 16:03

And remember, I, the reason why that worked out pretty simply is because the spatial shape of the
flux is the same for both groups.

## 16:12

In that case, they share the same buckling, right?

## 16:14

They both have to go from a peak at the middle down to zero, which means it has to be the same
cosine shape.

## 16:21

That is not true for other boundary conditions, right?

## 16:25

Where the, basically the.

## 16:27

The leakage would be different in each group, which means that the buckling term would be different
in each group.

## 16:32

Effectively, but you still have two independent solutions.

## 16:36

Those independent spatial solutions would be used for both the fast group and thermal group.

## 16:41

You can identify one of the quasi buckling terms is like the fast buckling term, which has to be
positive because of the multiplication.

## 16:48

And then there would be another term that would be sort of like our, our diffusion, right?

## 16:53

Where we would have a hyperbolic science and co-science instead of the.

## 16:57

Side.

## 16:57

And co-science, right?

## 16:58

That's kind of beyond our pay grade.

## 17:00

You can look at the solution for the problem due last night, right?

## 17:05

So the solution is there.

## 17:06

And I talk a little bit about the two group equations, right?

## 17:10

It's not a terrible leap, but it just, you know, it would take us another week.

## 17:14

And frankly, we're in dead week.

## 17:15

We don't have another week to, to do that.

## 17:17

Right.

## 17:18

But what you do have from the, from the modified one group equation of what is sometimes called the
one and a half group equation, right?

## 17:25

That term was.

## 17:27

Uh,

## 17:27

Discussed in, in Duterstadt and Hamilton is this, right?

## 17:30

So how do we get to this expression or we relate the thermal flux to the fast flux as a ratio of
this downscatter cross-section to the absorption cross-section.

## 17:41

We talked about this briefly last time.

## 17:43

What do we have to assume to get to this starting from the two group equations?

## 17:50

Yeah.

## 17:51

So the derivative term in the thermal diffusion equation goes to zero, right?

## 17:55

So you get rid of that and you're left with just the absorption cross.

## 17:58

Cross-section times fee two is equal to the downscatter source from the basket, right?

## 18:03

So you solve for P two and that's it.

## 18:05

You plug that into the fast group equation to account for the thermal neutron induced vision, and
you have a nice, simple equation.

## 18:13

So the flux that you're actually solving for in that one and a half group equation is really the
fast flux.

## 18:18

And the only way that you can get the thermal flux is to substitute that.

## 18:23

And so if we use that approximation in the.

## 18:27

The reflected what was it, this was a slab reactor with a like a roughly 20 centimeter reflector on
the outside, this black curve represents the solution that you should have found right for the
faster and you can see flux continuity from the solid to the dash from the fuel to the moderator,
right?

## 18:51

But if you use that fast group approximation along with the thermal approximation we just saw, then
the red curve.

## 18:58

Right?

## 18:58

Yeah.

## 18:58

The red curve should be our fee two.

## 19:00

Now you can see here something is grossly out of whack.

## 19:06

And if you saw this, you would be like, somebody made a huge mistake.

## 19:10

Well, it turns out that the, the red curve outside of the obvious glitch in the middle at this
interface condition is really not so bad in terms of magnitude.

## 19:19

It took, we would expect that the fast thermal flux is something like, you know, eight or so.

## 19:26

Right.

## 19:27

And if you do the, if you look at this as like.

## 19:30

I don't know, maybe a point one, two, five, and this one, and so that would be the, the, the right
ratio, that ratio that we've talked about though, is only for fuel, right?

## 19:41

That's what we get when we average over like a unit cell in open MC, which is effectively the, what
we get from the fuel and the moderator, though, we can have significantly larger thermal fluxes,
right?

## 19:52

Because all the fast neutrons that dump out of the fuel are going to be slowed down, scattered,
right?

## 19:59

To lower end.

## 20:00

And so that thermal neutron population is going to grow.

## 20:03

And so even though this junction here is totally wrong, right?

## 20:08

Because we can't have this, this, this continuity in the book.

## 20:12

If you kind of eyeball it and imagine, Hey, I'm going to take this red curve, which does have some
shape, right?

## 20:17

It does look a little bit like this, this coast, it is a coastline, right?

## 20:21

It's just the magnitude is so small.

## 20:23

We can't see it so well on, on this plot, but if you imagine taking this red curve here and like
averaging it in.

## 20:30

Some way as a function of distance from, from, uh, the, the interface, then you'd have something
that looks like that, okay.

## 20:38

Where you have some sort of peak in the moderator.

## 20:41

Now, you shouldn't know that off the top of your head, you might be able to reason it out, like
saying, Hey, if I've got all these fast neutrons from the fuel going into this place that slows them
down.

## 20:51

Yeah, maybe I should have more thermal neutrons on the outside.

## 20:54

Now, if we take a numerical solution of the same equation.

## 20:58

Or for the same.

## 20:59

Model get this here, right?

## 21:03

This is what we find, right?

## 21:05

So I used a numerical tool to solve the diffusion equation.

## 21:09

You, like I said, you could do this analytically too.

## 21:11

I just, I didn't want to, and you can understand why, because it's just sort of ugly.

## 21:17

Okay.

## 21:17

But I, I'd solved it using, uh, essentially a finite difference method, and this is the solution
that we get.

## 21:23

Now, if you look.

## 21:25

The black curve starts at one, the red curve starts at roughly 0.125.

## 21:29

And everything else is basically the right order to make it.

## 21:32

So same, same data.

## 21:33

Okay.

## 21:34

It's the same problem, but now explicitly the fast and thermal neutrons are accounted for.

## 21:39

And in effect, that red curve that we saw up here, if you took this in and brought it down, forced
it to come down to meet the one in the fuel, that's exactly what you get.

## 21:48

So this interface is right about here.

## 21:51

So you can see that even in the fuel, we're starting to see an uptick in the thermal neutron flux,
right?

## 21:57

And this is actually a real effect.

## 21:59

The effect that we observed, if you take a, a, a fuel element, okay.

## 22:03

And you, if we were like, let's say we went back to the open MC results again, we divvied up the
regions into like the fuel and the moderator regions into very small slices of the cylinder, and
then kind of take those out to the moderator.

## 22:18

If we plotted the thermal flux as a function of radius from the middle of the fuel element, we would
actually see that it peaks slightly toward the edge of the fuel element.

## 22:28

For this.

## 22:29

That's the exact reason, right?

## 22:30

Because we have fast neutrons going into the moderator and then they would be flowing back into the,
the fuel, right?

## 22:36

But because the thermal neutron cross section is so large, it essentially attenuates, right?

## 22:43

Because the mean free path, the thermal neutrons in fuel is very, very small.

## 22:46

So those thermal neutrons that come in, they're going, they won't get so far, right?

## 22:53

And that, that's that effect.

## 22:55

Anybody remember what that effect is called?

## 23:00

You've got so much of this.

## 23:01

High Sigma a material in the fuel element.

## 23:04

So that neutrons that come back in can't really make it all that far on the average, right?

## 23:09

So they peak kind of at the periphery and they can't enter that spatial self shielding, right?

## 23:17

That's a term that came up.

## 23:20

I would have been chapter four in the book, not, not a, not a topic that we considered in depth
because we didn't, we still really don't have the tools to analyze it now.

## 23:30

Finally, at the end, we have more.

## 23:31

But this is what would set us up for a follow on courses.

## 23:35

So at any rate, this is, this is what you would expect for a core with a reflector.

## 23:40

And if you zeroed in on an individual fuel element with the surrounding moderator, you would see
something somewhat similar, right?

## 23:47

The length scales that are a little bit different, the boundary conditions would be different,
right?

## 23:50

Because if this were a fuel element, we would model this as we did an open MC as pure reflection on
this side and pure reflection over here, right?

## 24:00

Because we would have this.

## 24:01

This sequence of fuel, moderator, fuel, moderator, right?

## 24:06

And what we do in an open MC is we take one of those unit cells, analyze it by itself, subject to
reflection, to, to map, to mimic the entire array of them in the core.

## 24:21

Any questions about this?

## 24:25

Is this surprising to you?

## 24:28

Now, I haven't looked at what folks had submitted, right?

## 24:30

Because it was just due last week.

## 24:31

It was due last night, but, uh, I expect many of you would have gotten this blacker.

## 24:36

And then what we talked about last time on Friday, as I said, like, you haven't seen the two group
solutions.

## 24:41

So, you know, just make a good effort.

## 24:44

Did anybody try to use the, the expression that led to this image, right?

## 24:50

With this discontinuity.

## 24:52

Okay.

## 24:53

So I'm guessing if you did, you probably saw it as like, no, I don't want to use that.

## 24:56

That's wrong.

## 24:57

So I'll just do something else, which is fine.

## 24:59

I'm not, I'm not looking.

## 25:01

Uh, for anything special for that problem, but now you know what it is.

## 25:04

So on the exam, I say, Hey, what would this look like?

## 25:07

What does the thermal flux look like?

## 25:10

Uh, you'd be able to give an estimate and I think that there's more on here that I would want.

## 25:19

How would this change if I made the right-hand side, peer reflection, do you think this would change
fundamentally?

## 25:46

So this is a reasonable question, right?

## 25:48

So if I have my junction.

## 25:51

It's here, right?

## 25:52

Where are my source?

## 25:53

Where's my source of neutrons here, right?

## 25:58

And what group are those neutrons fast, right?

## 26:03

So if I'm over here in the reflector, I mean, yeah, I know that this is nominally a critical
reactor, right?

## 26:09

All my source neutrons are coming from the fast group and from the fuel.

## 26:12

But if I'm talking about the reflector reflector really doesn't care what's happening in the core.

## 26:17

All it knows is that I have an influx or an incoming current of fast neutrons.

## 26:22

Right?

## 26:23

Uh, some thermal neutrons, but you know, that not nearly as many as fast neutrons.

## 26:28

So I'm always going to have a solution over here that looks like hyperbolic signs and hyperbolic
cosines, right?

## 26:36

My basically attenuation as I go from left to right now, if I have reflection, obviously that's
going to reduce any leakage over here.

## 26:45

Cause over on this side, do you remember what the boundary condition was?

## 26:51

It was a zero flux, right?

## 26:52

So if you look over here.

## 26:54

Here by map over here, you can see it's not quite zero.

## 26:59

That's because my computer code makes it hard to do zero flux boundaries because zero flux
boundaries are not usually used.

## 27:07

They're good for pen and paperwork, but, uh, but at any rate, like, so rather than being strictly
zero, it is just very, very low, but that means I have zero incoming current.

## 27:17

If I were to make this reflective, I guess that the overall shapes would be basically the same.

## 27:23

It would just be raised.

## 27:24

Up a little bit.

## 27:25

Now that would change if this thicker, uh, the thickness of the reflector were smaller so that the
overall magnitudes would be, um, you know, larger, right?

## 27:36

So if I instead went from having a thickness of 20 centimeters to a thickness of say, just a couple
centimeters, then I would probably guess that this red curve would flatten out so that then it's
derivative would be zero, you know, wherever the edge is.

## 27:51

Uh, and then the black curve too, would, would.

## 27:54

I'm going to sort of converge onto having a flat, um, shape, right?

## 27:59

But question.

## 28:01

So you're saying for a thinner reflector, you're going to have a higher magnitude for thermal books.

## 28:09

If it were reflected on like a reflecting boundary condition, right.

## 28:13

If we were modeling a fuel cell, right.

## 28:15

Of repeating array.

## 28:16

Yeah.

## 28:16

If, if this were, if the reflector were only a few centimeters thick and had the vacuum condition of
the zero flux condition, then.

## 28:24

The peak here would be squashed essentially, and it would look much closer to, you know, just to
decaying curves.

## 28:32

I guess I think thinner black bear.

## 28:34

And then I think leakage because like, right.

## 28:36

So, so, so basically if you have the thinner reflector, you would have a whole bunch of leakage,
which is going to deplete your, your neutron population and hence your flux.

## 28:46

So it would just die down.

## 28:48

So you've got to have enough.

## 28:49

In fact, you can see here, if this is, if this is where the interface is.

## 28:52

So at just like.

## 28:54

The peak in the moderator is not too many mean free paths beyond that, right?

## 29:01

So you've got to have a, like, if you want a reflector to do its job, you really need it to, to be
thick enough so that you can resolve this, this peak, right?

## 29:11

That's, that's where you'll probably get the best bang for your buck in terms of a reflector
savings.

## 29:17

Right.

## 29:17

You could probably show that mathematically, but you know, like basically that 90% of your
potential.

## 29:24

Savings is gotten by the first, I don't know, three or four mean free paths of, of reflector
thickness, right?

## 29:30

Beyond that, you don't gain a whole bunch and because you don't gain much, it doesn't change things,
which is why that thick reflector approximation is sort of useful, right?

## 29:38

Cause it's much simpler than a finite reflector, but yeah, lots of these sorts of problems would be
very useful to solve with numerical methods.

## 29:52

I'm not sure where that would fit.

## 29:54

Best in a course like this, or if that actually fits in a, you know, follow along course, I guess
we'll have, we'll have the opportunity to explore a little bit of this in the reactor laboratory as
part of help, helping us to understand what we see in, in certain experiments.

## 30:11

All right.

## 30:12

So I think that's all I wanted to say about the two group flux.

## 30:17

Of course, with this sort of information, like if we were able to solve this.

## 30:24

Sort of, if we have the analytic tools to do this and the time in which to do all that, given this,
this flux across the domain, we're able to compute some things that weren't accessible before,
right?

## 30:39

With the fast and thermal flux, we can actually compute the fast non-leakage probabilities, the
thermal non-leakage probabilities.

## 30:47

We can compute things like what's the average reflector flux in the thermal group?

## 30:53

Compared to the average fuel flux in the thermal group, right?

## 30:56

Now, if we shrunk this down to centimeter scale, or we're talking about an individual fuel cell,
that would give us things like the disadvantage factor, which you remember is that ratio of the
moderator to fuel flux that shows up in the thermal

## 31:10

utilization F, one of the four factors, right?

## 31:13

Usually that was just a number that was specified, but now this is how you would actually compute
that.

## 31:23

All right.

## 31:24

The last little bit.

## 31:26

We're on the.

## 31:26

Validity of diffusion.

## 31:28

So hopefully you did the reading and have a sense for what the author was going for.

## 31:35

I'm going to tackle it from a slightly different point of view by using actual numbers, right?

## 31:41

So we'll kind of like, we'll look at it as a numerical experiment.

## 31:45

So first of all, it helps to understand what was our approximation when defining the diffusion
equation?

## 31:53

Because if you remember back in lesson 31, I think.

## 31:56

It was, we developed this equation first, right?

## 32:01

Where we took a box in three-dimensional space, and we assume that we had some number of neutrons
being born.

## 32:09

We surrounded that with, you know, this box with the six surfaces.

## 32:14

We know that a certain number are absorbed and that volume contained by the, the surfaces.

## 32:20

And we know that a certain number of neutrons go through those surfaces, right?

## 32:24

And so what that led to in.

## 32:26

The.

## 32:26

Limit of a very small box with this thing where J is our neutron current.

## 32:31

Okay.

## 32:32

But we made this jump to equation six 12, which of course is the diffusion equation where we no
longer express things in terms of J, but rather we express it in terms of fee.

## 32:43

What was the fundamental approximation?

## 32:48

Fixed law, right?

## 32:49

I mean, if somebody can, somebody say what fixed law means in plain English, what does it mean?

## 33:02

So what are we?

## 33:03

Eliminating here, we're saying that this J, which we know is the net current, right?

## 33:09

It's the net current vector.

## 33:10

So it tells us the net flow of neutrons in any particular direction for in Cartesian coordinates.

## 33:16

We would have an I, J and K component, right?

## 33:20

In one D, which is where we've lived a lot of our, our, our lives in this class, it tells us the net
number of neutrons going to the left or to the right.

## 33:30

Okay.

## 33:30

So we could have J equals zero, which means.

## 33:32

Okay.

## 33:34

There is no net flow.

## 33:35

Doesn't say anything about the flux.

## 33:36

If we could still, we could have a billion neutrons going to the right and a billion going to the
left, but the current is still zero.

## 33:42

So it says nothing about the magnitude of the flux or of the neutron population.

## 33:47

It only says something about the flow.

## 33:49

So what we're doing is saying, Hey, this current is actually equal to the gradient of the flux times
the diffusion coefficient with a minus sign, right?

## 33:59

So it's saying that that net flow that I just described is proportional.

## 34:03

To the derivative of the flux and really minus the, it's, I guess it's, it's accurate to say it's
proportional to the derivative of the flux that constant proportionality is negative and the
magnitude of it is the diffusion coefficient, right?

## 34:22

So it's the same thing that we use in Fourier's law of conduction.

## 34:27

We say that the flow of heat is proportional to the derivative of the temperature, right?

## 34:33

And that,

## 34:33

constant proportionality is the conductivity.

## 34:36

Okay.

## 34:36

That's fixed law.

## 34:39

When is that valid is really the question to answer.

## 34:43

If we want to understand when diffusion theory is valid.

## 34:47

Okay.

## 34:48

And so let's take a moment.

## 34:51

We've got about 15 minutes left.

## 34:52

So I thought it would be useful to spend some time on review.

## 34:58

And it's that time of year.

## 34:59

So let's review, let's consider our favorite slab.

## 35:03

We're going to say it's 10.

## 35:04

Centimeters wide.

## 35:06

We've got a total cross-section of one centimeter and an absorption cross-section of 0.5 centimeter,
right?

## 35:12

We could vary that if we want and a uniform source of strength, one centimeter, one neutron per
centimeter cube per second slab is subject to vacuum and we want to find the flux.

## 35:34

So I think for this,

## 35:36

all is good.

## 35:38

So this thing has been in here forever.

## 35:41

I'm not using it because that chalk that I got was cheap rail chalk.

## 35:48

I don't even know what that's all for, why, where the name comes from, but it was so brittle.

## 35:52

Like I broke it almost immediately.

## 35:55

So I, it probably helps to define something first, given this data, notably we're missing what, if
we're going to solve the diffusion equation.

## 36:07

Yeah.

## 36:07

So usually I've given you some, the diffusion coefficient as part of the, you know, part of a
problem statement here.

## 36:15

We don't have it.

## 36:15

So the very first thing we'd want to do is define what deed is and what is the, in this case,

## 36:25

one of the three times the removal from section, a good guess, not removal total, right?

## 36:35

If I had given you a separate quantity, it could have been the transport cross-section, right?

## 36:40

And you'll remember that, or maybe I'll remind you, this is the total cross-section if the transport
cross-section were.

## 36:47

Yeah.

## 36:47

Given that would account for an isotropic scattering.

## 36:51

Right.

## 36:51

But if we only have Sigma T then D will always just be taken as three times Sigma T.

## 37:01

Okay.

## 37:03

All right.

## 37:04

So we've got D we've got the source term.

## 37:08

We have Sigma a, which is the other piece that we would need.

## 37:11

Let's write down the equation.

## 37:13

I take just two minutes, three minutes.

## 37:16

I want you to.

## 37:17

Write down the equation.

## 37:18

I want to look at it, make sure that it's there, but you can't write down the diffusion equation.

## 37:25

You need to learn how to write it down because I said, fine.

## 37:39

You're getting quicker.

## 38:10

Yeah.

## 38:10

Remember if you're thinking about how to write down the diffusion equation, you should maybe go back
to the basics to help jog your memory.

## 38:19

What, what is the diffusion equation?

## 38:21

A statement of the statement?

## 38:24

A statement of neutron balance.

## 38:25

You have losses on the left and you have gains on the right.

## 38:28

Your losses come from leakage diffusion.

## 38:34

And so you have, you can call it leakage.

## 38:37

Then you have interaction or absorption, and this has to be balanced by your gains for a problem
like this, where we have a source driven system without vision, that would just be your source.

## 38:53

So if you remember this, then you can start to piece together.

## 38:58

What would my losses by absorption look like for this differential balance would have to be a flux
times an absorption cross section and your gain term is going to be the source of neutron, right?

## 39:12

So this is stigma a times speed, and this is our source term s.

## 39:17

Remember s I was given in volumetric source, right?

## 39:20

So neutrons per centimeter cubed.

## 39:23

Per second.

## 39:25

Our flux has units of what?

## 39:28

Per centimeter squared per second.

## 39:29

Per centimeter squared per second.

## 39:33

And our cross section has units of what?

## 39:36

Per centimeter.

## 39:36

Per centimeter.

## 39:37

So it's always, I think, gratifying when units match on either side of the equation.

## 39:43

So inverse centimeter times one per centimeter squared per second gives me a volumetric reaction
rate.

## 39:52

So that's cool.

## 39:53

That's the same thing that I have here.

## 39:54

Source particles per centimeter cubed per second, which means that this leakage term, right?

## 40:01

It's not really leakage in the sense that I'm counting the number of neutrons through a boundary,
but it's the process that causes being here.

## 40:08

Right?

## 40:09

What is that term?

## 40:11

You should remember that it involves that huge spatial diffusion of the time, so we ought to have
the D.

## 40:18

OK, and then I said that this this term is related to the.

## 40:23

Derivative of the flux, and so we have a minus D, and the current was the derivative of the flux
times D, and then we have the derivative of the current, so this will be where the X.

## 40:39

What's the unit of the diffusion coefficient?

## 40:46

What is it?

## 40:49

OK, what's the unit of the second derivative of the flux?

## 41:14

Yeah, it's one over centimeters to the fourth to the second, right?

## 41:18

Because the flux has one over centimeter squared per second, the spatial derivative.

## 41:24

So D D X that X carries a unit D D X is one over centimeter D squared D X squared is one over
centimeters squared.

## 41:33

So you get centimeters to the fourth, but one of those is canceled out by the diffusion coefficient,
and we're left again with one over centimeter cubed per second.

## 41:42

So get good at that.

## 41:43

It's.

## 41:44

Not just this class, if you're doing heat transfer, whatever, anytime you're trying to remember
exactly how the equation goes together, units can be a guide.

## 41:52

I've saved myself many a time just by balancing units.

## 41:58

Right, so that's the diffusion equation.

## 42:00

OK, now we've often organized the equation slightly differently to make it a bit easier to solve,
right?

## 42:13

Do you remember what substitution we make for the data?

## 42:16

So rather than using D and Sigma A explicitly, we've used this additional term, L, right?

## 42:23

So what is L?

## 42:26

D over square root of the unit D, right?

## 42:30

So L is equal to the square root of D over Sigma A.

## 42:35

And this is called the diffusion length, which means as the name implies, it has units of?

## 42:46

Simultaneous.

## 42:50

OK, cool.

## 42:51

Now, with this, we can write the diffusion equation as follows.

## 42:55

We can say that we have the second derivative of the flux plus 1 over L squared times B of X is
equal to whatever our source term is.

## 43:10

But because we divide it through by D, we'll have S over D.

## 43:17

OK, the boundary conditions are.

## 43:20

Vacuum.

## 43:21

Now, we could choose to do the zero flux condition or the extrapolated boundary condition.

## 43:26

Doesn't really matter too much to me, but why don't we do?

## 43:32

Let's do the zero flux condition just to make it easy, right?

## 43:36

So we've got B at.

## 43:40

Well, what are our boundaries?

## 43:44

So this thing is 10 centimeters wide.

## 43:47

We can choose any any way to situate.

## 43:50

The slab, right?

## 43:50

We can choose the origin to be at the center of the slab or at the left or at the right.

## 43:54

I think everything we've done so far has gone for symmetry.

## 43:58

And because this source is uniform, it's a symmetric source.

## 44:04

So I see it as beneficial to choose the origin at the center.

## 44:09

OK, so that means that B at minus five is equal to B at five is equal to zero.

## 44:17

Right. And again, we could put extrapolate.

## 44:20

Conditions, which would be an approximate vacuum.

## 44:23

We could use the actual vacuum, but to sort of expedite our word time here and we'll keep that.

## 44:29

OK.

## 44:30

And so getting from the problem statement to this point is pretty darn critical, right?

## 44:41

You're not going to get very far in a problem if you can't write this down.

## 44:45

So please, please.

## 44:48

Study that, be able to get to that point, I've said it multiple times, I do not like

## 44:53

memorization.

## 44:54

I don't want you to think about this as something to memorize.

## 44:57

I want you to think about the process we use to get here.

## 45:02

Right.

## 45:03

Remember, the thing you can memorize is the fact that the diffusion equation is a statement

## 45:06

of balance.

## 45:07

Right.

## 45:08

That's that's something to memorize because that's a concept.

## 45:11

Memorize concepts, not equations.

## 45:14

It helps sometimes if you use it enough where it's just there is it's like a muscle membrane.

## 45:20

Right.

## 45:20

But that's that's different.

## 45:22

Then.

## 45:22

That's a concept of memorization.

## 45:24

All right.

## 45:24

So we've got that.

## 45:26

What's the next step?

## 45:26

This is like step one.

## 45:28

If you go rewind all the way back to when we started talking about step one is write

## 45:32

down the equations, including boundary conditions.

## 45:36

What's step two?

## 45:37

What was the general point for the first?

## 45:41

Yeah.

## 45:42

So we've got to come up with with with the full solution.

## 45:45

Right.

## 45:46

So that's a combination of two terms that we need to take in order to get the general

## 45:50

solution or the full solution.

## 45:52

We need to get two parts.

## 45:54

First thing is the homogeneous solution, which I think the book actually calls the

## 45:58

general solution.

## 45:59

I prefer to use general for like the whole thing.

## 46:02

So we need to get the solution to the homogeneous equation, which means set the right hand side

## 46:07

zero and then find out what form satisfies that.

## 46:11

Okay.

## 46:12

So what we need to do is write B double prime.

## 46:17

Plus one square.

## 46:19

The next zero subject.

## 46:22

So.

## 46:23

We can see.

## 46:24

All right.

## 46:25

So.

## 46:26

What function satisfies?

## 46:27

And there should be a minus.

## 46:28

And that shouldn't be.

## 46:29

Yeah.

## 46:30

So what?

## 46:31

What?

## 46:32

What solution satisfies this?

## 46:35

What form of B?

## 46:36

Yeah.

## 46:37

What's that?

## 46:38

So we could do siding cosines.

## 46:39

But I caution you when you have a minus sign here and a plus here.

## 46:40

What's that?

## 46:41

Cosine.

## 46:44

Cosine.

## 46:45

Cosine.

## 46:46

Cosine.

## 46:47

Cosine.

## 46:48

Cosine.

## 46:49

Cosine.

## 46:50

Cosine.

## 46:51

Cosine.

## 46:52

Cosine.

## 46:53

Cosine.

## 46:54

Cosine.

## 46:55

Cosine.

## 46:56

Cosine.

## 46:57

Cosine.

## 46:58

Cosine.

## 46:59

Cosine.

## 47:00

Cosine.

## 47:01

Cosine.

## 47:02

Save the.

## 47:03

And we assume that L squared is positive, which if we have Sigma, A and D being positive,

## 47:16

then the signs and cosines that we get would have a magistrate audience.

## 47:20

It would be sign of the icon, something Túoso video

## 47:24

And because I advise I have some wildly continuity time,

## 47:27

which is what we get when dealing

## 47:29

with the criticality problem, right?

## 47:31

Because then we go from the one over L squared

## 47:34

to the same K infinity minus one over L squared,

## 47:37

which we call the buckling.

## 47:39

So for a positive buckling,

## 47:40

then sine and cosines are like,

## 47:43

those make it pretty straightforward.

## 47:45

Here, we can go back to the very first solution

## 47:48

that we talked about, which was just exponential, right?

## 47:52

Sine and cosines are exponentials

## 47:54

with or without the imaginary, right?

## 47:56

You can get sine and cosines from exponential,

## 47:58

but you can also get the sine and cosines

## 48:00

for their analog, which is the hyperbolic functions, right?

## 48:05

So in this case, I think rather than sine and cosines,

## 48:08

let's use the hyperbolic versions, right?

## 48:12

Which themselves are really,

## 48:14

they're just exponentials in disguise,

## 48:15

but they can help.

## 48:18

And actually, if you remember,

## 48:19

remember when I did the series solution

## 48:22

in lesson 35 to motivate

## 48:24

where the Bessel function comes from?

## 48:26

I started off with an example from slab lab, right?

## 48:30

And what we got was that the series solution

## 48:33

led first to the hyperbolic cosine.

## 48:38

And then of course you'd get the other one

## 48:39

as the hyperbolic sine.

## 48:40

So in that sense, you'd be in series solution.

## 48:42

It seems in a sense that the hyperbolic cosine

## 48:46

and the hyperbolic sine are actually more natural things.

## 48:49

So anyway, what we would have here is B of X

## 48:53

is equal to C1 times the,

## 48:56

hyperbolic cosine of X over L

## 49:00

plus C2 times the hyperbolic cosine of X over L.

## 49:06

Now, symmetry here is useful

## 49:09

because what kind of function is the hyperbolic sine?

## 49:16

There's a certain math descriptor I've used for that.

## 49:24

It's the same thing that differentiates cosine and sine.

## 49:27

When we talk about being with respect to the origin,

## 49:32

you remember odd versus even functions,

## 49:38

if you put in a negative value to sine

## 49:40

that's equal to minus sine of the positive value,

## 49:42

same thing happens here with the hyperbolic sine.

## 49:45

If we have a positive value of X so at X equal five,

## 49:50

this sine, the hyperbolic sine will be a positive value.

## 49:53

And if I put in the negative value,

## 49:56

I'll get a minus negative value of the hyperbolic sine.

## 49:59

That means on either side of the slab,

## 50:00

any positive value the sine will be equal to minus the sine.

## 50:01

And it means on either side of the slab, any positive value,

## 50:02

any positive value of the sine,

## 50:02

the value given to the hyperbolic sign will have opposing signs if it has opposing signs

## 50:08

it's not symmetric right the only option we have is the hyperbolic cosine we get the same thing

## 50:15

if we want if we set the um if we set the gradient to zero at the at the center of the slab right

## 50:23

enforce symmetry that way but this is our our homogeneous solution right and we can do that now

## 50:30

i know that we're just about out of time so i want to wrap up with the particular solution we

## 50:35

can pick this up uh next time which i kind of planned on doing what do we get for the how do

## 50:40

we get the particular solution there's a trick this is sort of a heuristic approach if you have

## 50:51

a right-hand side what do you choose the particular solution to look like it doesn't look like the

## 50:58

right answer yeah so in this case if we know the right-hand side our forcing function our source

## 51:04

term

## 51:05

is a constant then we would assume that our particular solution as a function of x

## 51:13

is actually also equal to some constant right that will almost always work

## 51:20

and in problems like this you'll almost always have a right-hand side

## 51:23

where this this approach is the right the other things that you can do are um so this

## 51:30

this approach is called the variation of parameters the more robust way to do it would

## 51:34

be to use something called an eigenfunction expansions now that sounds terrible in a

## 51:42

previous version of this class that was a big um focus and it's a big focus in the old marsh

## 51:50

book it's a cool math technique but my goodness the amount of time spent on the map with physics

## 51:56

would make our little bit of issues with vessel functions like a walking park a thing it's all

## 52:04

relative to it so that's a little bit of an example of what we're going to do next time we're going
to

## 52:04

go anyway so we would choose this this particular solution to be c3 and if we plug this into the

## 52:11

original diffusion equation this particular solution would be uh deleted by the derivative

## 52:18

and we end up then with uh c3 over l squared is equal to our right hand side which means that c3

## 52:28

would equal to uh l squared i believe so that gives us c3

## 52:34

we plug that in now we have our full solution which would be b is equal to b h plus b p okay with

## 52:44

these constants we still have c1 and c2 that's then where the boundary conditions would play a

## 52:50

role and i will what we find from symmetry is that c2 goes away and then we'll figure out what c1 is

## 52:57

but we'll take that to next time where we'll then look at the numerical solution of the equation and

## 53:04

it really is a little bit more complicated than what we're going to do next time we're going to

## 53:04

kind of take away from the class everything that we've done with uh kind of a look at the things

## 53:11

that that we could do better in terms of the modeling which means going from diffusion to

## 53:16

full transport and so forth and then on friday uh depending on interest we can just continue

## 53:21

this sort of stuff where we solve problems and talk all right i will see you on wednesday

## 53:30

on

## 53:40

wednesday
