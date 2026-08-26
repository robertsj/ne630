# L40 Local Audio Transcript

Course: NE 630

Playlist source: https://youtube.com/playlist?list=PLy481lNHlnHoEO95vM-xYX2bydD25v20L

Video: NE 630 - Lesson 40

URL: https://www.youtube.com/watch?v=jVAzwndCmps

Video ID: jVAzwndCmps

YouTube upload date: 20231206

Duration: 55:07

Transcript source: Local faster-whisper transcription from YouTube audio.

Whisper model: large-v3; detected language: en.

Generated: 2026-06-28

Note: This transcript is machine-generated from audio and lightly wrapped only. It should be reviewed before being quoted, published, or used as polished lesson text.

Requested language: en

## 00:00

Okay.

## 00:02

So,

## 00:04

I've been ready to take time to.

## 00:06

Yeah.

## 00:08

Indoor outdoor day.

## 00:10

I would say that all your locker.

## 00:12

I mean,

## 00:14

I mean,

## 00:16

Yeah.

## 00:18

Yes.

## 00:20

Okay.

## 00:22

What's this?

## 00:24

Yeah.

## 00:48

All right.

## 00:51

So.

## 00:53

We left off last time.

## 00:55

Just having talked about the validity of.

## 00:57

Neutrons.

## 00:59

And then right after this,

## 01:01

we started a sample problem,

## 01:03

but I wanted to go back to this slide.

## 01:05

Because we heuristically.

## 01:07

Came up with this equation 610.

## 01:09

Right.

## 01:11

This was just balancing neutrons in a box.

## 01:13

Pretty straightforward.

## 01:15

We didn't have to make many assumptions at all.

## 01:17

The assumption that we made to go from here to here was of course,

## 01:19

this expression,

## 01:21

which we know as fixed law.

## 01:23

Right.

## 01:25

And what it's saying is that the net flow of the neutrons.

## 01:27

Is due only.

## 01:29

To the change in concentration of the neutron.

## 01:31

Right.

## 01:33

So that means neutrons are bouncing back and forth.

## 01:35

In a way.

## 01:37

It just,

## 01:39

the only thing driving this is the difference in the number of

## 01:41

neutrons here,

## 01:43

the number of neutrons here.

## 01:45

Right.

## 01:47

And that constant proportionality,

## 01:49

the thing that gives you that,

## 01:51

that decline is the diffusion coefficient.

## 01:53

Right.

## 01:55

And that works out pretty well for a lot of physical phenomena.

## 01:57

Right.

## 01:59

So what I want to do is.

## 02:01

I use some numerical results to show you.

## 02:03

Where this approximation essentially breaks down.

## 02:05

Right.

## 02:07

And if you were to go on to.

## 02:09

To.

## 02:11

Use.

## 02:13

Neutronic tools and such.

## 02:15

You would have to be aware of the limits of your model.

## 02:17

Right.

## 02:19

Diffusion theory is effectively a mathematical model.

## 02:21

For what neutrons do.

## 02:23

And in order to use it.

## 02:25

And not a single electron.

## 02:27

You have to know where,

## 02:29

where it's valid and where it's not.

## 02:31

And when it's not valid,

## 02:33

you have to figure out what,

## 02:35

what to do.

## 02:37

Okay.

## 02:39

So what we had done last time was start off with a review problem.

## 02:41

Now I've changed a couple of the numbers so that everything will be

## 02:43

consistent with the numerical results that,

## 02:45

that are to follow.

## 02:47

But the numbers don't matter.

## 02:49

Because we would come up with this general form.

## 02:51

And that that's what we would have gotten from the.

## 02:53

Sort of pen and paperwork.

## 02:55

Okay.

## 02:57

So what we had started with last time.

## 02:59

Was the diffusion equation, right?

## 03:01

Maybe we started with D over here.

## 03:03

Sigma a over here, but if you divide through,

## 03:05

this is what you get.

## 03:07

And I think we got to this point where we have the flux in terms of

## 03:10

the hyperbolic.

## 03:11

Cosine and sign. Is that correct?

## 03:13

Right. And so.

## 03:15

What we wanted to do is actually generate those.

## 03:19

Those coefficients C1 and C2.

## 03:22

And here, I think we're going to use simple.

## 03:24

We'll go ahead and stick with that.

## 03:27

Okay.

## 03:28

So rather than write all this out again,

## 03:31

as I was doing last time,

## 03:33

we just can write down these boundary conditions.

## 03:35

So if we have the, the flux represented as.

## 03:38

Hyperbolic cosine and sign, then at the right boundary condition,

## 03:42

we have this and at the left boundary condition, we have this.

## 03:45

I had mentioned,

## 03:47

we set up our problems specifically to be from negative a over two

## 03:50

to a over two.

## 03:51

And because the source is symmetric,

## 03:53

we'd expect.

## 03:54

The flux to be symmetric.

## 03:56

And I said right away,

## 03:57

you could probably just get rid of that hyperbolic sign term.

## 04:00

Right?

## 04:01

Because that's going to be positive on one half and then negative on

## 04:04

the other half, because it's an odd function.

## 04:06

Okay.

## 04:07

If you didn't know that or didn't feel comfortable making that sort of

## 04:10

assumption, say on an exam,

## 04:12

you could write out the full equations like this.

## 04:15

And then once you actually plug in the numbers, you know,

## 04:18

that.

## 04:19

Hyperbolic sign of negative a over two is the same thing as hyperbolic

## 04:22

sign at a over two.

## 04:23

Right?

## 04:24

So you'd have to know that.

## 04:26

A over two.

## 04:27

With the minus sign popping out, right?

## 04:29

That's the property of an odd function.

## 04:31

So you'd have to know that property of the hyperbolic sign in order

## 04:34

to write it like this, but.

## 04:36

The assumption is you can do that with these functions and with the

## 04:39

signs and cosines.

## 04:40

If you don't feel super comfortable with these, right.

## 04:42

Write them down on your, on your note sheet.

## 04:44

Right. That that's totally fine.

## 04:46

I mean,

## 04:47

it might be the case that I'd put something like that on the exam,

## 04:49

but I say, just put it on your note sheet.

## 04:51

If you,

## 04:52

if you look at this,

## 04:53

you can put it on the test.

## 04:54

And you can put it on the test.

## 04:55

So you can put it on the test.

## 04:56

So if you look at this,

## 04:57

we've got a C one time to code the cosh C one times the cosh.

## 05:00

We have the plus C2.

## 05:01

Cinch minus C2 cinch.

## 05:03

So the obvious thing to me, maybe it's not obvious to you,

## 05:06

but you can kind of remember this straight.

## 05:08

Just add these two equations.

## 05:10

Or subtract these two equations.

## 05:12

Right.

## 05:13

And so if you take this equation and you subtract from it,

## 05:16

this equation.

## 05:17

The cost term go away.

## 05:19

The source terms go away.

## 05:20

And what you're left with is two times.

## 05:22

The cinch term.

## 05:26

Zero.

## 05:27

And that means that C2 is equal to zero, right?

## 05:29

So we get back just this.

## 05:31

Symmetric form that, that we sort of expected from the get go.

## 05:34

Right.

## 05:35

So it's good to build some of that intuition because it really

## 05:37

connects, but I, your problem solving.

## 05:39

In general, this is a trick that you can do.

## 05:42

For, for this class, for other classes, for.

## 05:44

You know, life ahead of you.

## 05:46

Et cetera.

## 05:47

Right. And once you have C2 is equal to zero.

## 05:49

You can go back and get C1.

## 05:51

And voila.

## 05:52

You get the same solution that we probably saw in less than 33.

## 05:56

Or something like that.

## 05:57

Okay. For the same problem. So I haven't substituted any numbers yet.

## 06:00

We don't need.

## 06:02

The numbers to write this down. And in fact, on an exam.

## 06:05

I'm probably not super interested in numbers, right?

## 06:07

Cause it's, it's more about the problem solving interpretation.

## 06:10

Of it.

## 06:12

So, yeah.

## 06:13

Any questions on, on this? I purposely put this review.

## 06:18

Problem in, right. Cause it's about two or three weeks old at this point.

## 06:21

And it definitely represents something that you should knock out a hundred

## 06:24

percent on the exam.

## 06:26

Okay.

## 06:27

And.

## 06:28

So heads up.

## 06:29

Right. That that's something like this.

## 06:31

We will easily be on there.

## 06:33

Okay. And this is for the case of fixed source.

## 06:36

And here it was not multiplying.

## 06:38

We could certainly add multiplication in the solution.

## 06:41

Technique is the same.

## 06:43

As long as we assume the system is sub critical,

## 06:46

because the minute that we get to a point where there's more multiplication

## 06:49

than absorption.

## 06:50

Then we're in a situation where we could have K.

## 06:55

Greater than one.

## 06:56

Right. And then it wouldn't be soluble anymore.

## 06:58

Right. We saw that in one of the homeworks.

## 07:00

Obviously doing something like that,

## 07:02

where you're looking at an approach to criticality,

## 07:04

you can't do that with pen and paper. Right.

## 07:06

But if I give you a problem that has no multiplication.

## 07:09

And source it's source driven.

## 07:11

This is the way we do it. There's going to be a homogeneous solution,

## 07:15

a particular solution.

## 07:16

If we're doing an eigenvalue problem and we'll do this next time.

## 07:19

Right.

## 07:20

We have one more lesson that we can do some practice problems.

## 07:23

If we're doing a,

## 07:24

a problem where we're trying to come up with the criticality condition,

## 07:27

either K or the critical width or something like that,

## 07:30

then we won't have a source term.

## 07:32

We won't have what we call a particular solution, right?

## 07:35

Cause it's always just going to be the homogeneous solution.

## 07:38

And then there are different, different things that we do with,

## 07:41

with the flux form.

## 07:43

And here we get the explicit flux magnitude and everything we can plot

## 07:47

it by substituting in numbers. And so,

## 07:49

and so forth.

## 07:50

Okay.

## 07:51

So what I want to do is take this and start to compare it to some,

## 07:54

some results from.

## 07:56

A numerical method. Okay. So first of all,

## 07:59

here is that plot.

## 08:01

For the flux that we just got.

## 08:03

And specifically I am doing it for a is equal to 20.

## 08:07

I think that's what I had before.

## 08:09

And then I've got Sigma equal 0.01.

## 08:13

My D is one over three. I'm assuming Sigma T was equal to one.

## 08:16

And my source term is one, right?

## 08:18

So that's it.

## 08:20

Pretty straightforward. It's.

## 08:23

Because the scattering cross-section is so large relative to the total

## 08:27

cross-section.

## 08:29

In other words, the absorption cross-section is very small.

## 08:33

Right.

## 08:35

In the book,

## 08:36

when you read the section on the validity of the diffusion coefficient,

## 08:39

there was this,

## 08:40

this new symbol C that represented the so-called scattering ratio,

## 08:44

which is Sigma S divided by Sigma T.

## 08:47

And what the book says is that the fusion theory tends to break down.

## 08:51

If C is less than about 0.7.

## 08:54

This is much larger than 0.7. This is 0.99, right?

## 08:58

If my scattering cross-section is 0.99 or Sigma is 0.01.

## 09:02

And Sigma T is one, then this is a pretty high scattering ratio.

## 09:06

Which means that on the average,

## 09:08

we're not losing very many neutrons on the inside of the slab.

## 09:11

Really our losses are driven by neutrons.

## 09:14

Simply diffusing out of the slab.

## 09:16

Right.

## 09:17

Which is why we see this turn down.

## 09:19

And of course we're forcing that to happen because even more,

## 09:22

because we're setting the flux to be zero.

## 09:24

So we're,

## 09:25

we're forcing those neutrons to leave the building as a word.

## 09:29

All right.

## 09:30

So what does this look like if we were to use the vacuum conditions?

## 09:35

Right.

## 09:36

Actually,

## 09:37

do you think you could predict what this curve would look like if we

## 09:40

went to the zero incoming current conditions?

## 09:43

I think the overall shape is going to change much.

## 09:45

Who thinks the shape is going to change a whole lot.

## 09:51

Who thinks it won't change very much.

## 09:56

Okay.

## 09:58

All right.

## 09:59

Why don't we see.

## 10:01

What this looks like.

## 10:05

So here's a whole bunch of code.

## 10:08

That is based on a transport solver that I wrote many years ago called

## 10:13

D Tran, because I'm very clever.

## 10:15

It's for deterministic transport.

## 10:18

Deterministic meaning.

## 10:19

Solving equations as opposed to.

## 10:21

Simulating things with Monte Carlo, right?

## 10:24

So there are two classes of simulation techniques or modeling techniques.

## 10:27

Deterministic where you take your underlying equation.

## 10:30

Like the diffusion equation or a transport equation,

## 10:32

something that you can write down with pen and paper,

## 10:34

and then you implement it numerically.

## 10:37

Basically end up with like a linear system of matrix, right? Every, every.

## 10:41

Diffusion problem that we've seen, like.

## 10:44

With a source term that's equivalent to a X equal B.

## 10:47

If we're doing the idea.

## 10:48

If we're doing the eigen problem.

## 10:50

That's a X equal Lambda X, right?

## 10:52

It's all linear algebra at the end of the day.

## 10:54

It turns out like the calculus it's good for writing down the equations,

## 10:57

but the actual numbers that we get comes from linear algebra.

## 11:00

So it's sort of a,

## 11:02

but just an interesting observation I've had over the past several.

## 11:06

Not quite two decades, but close to it.

## 11:09

Anyway, so this is just some stuff to get.

## 11:12

The model set up, not relevant to you, but I need it in here to,

## 11:16

to generate.

## 11:17

The numbers.

## 11:19

And so this is what we get.

## 11:22

The very first curve that you see is this.

## 11:24

Green one. That's exactly what we saw a moment ago.

## 11:27

That's the neutron flux for the slab problem.

## 11:30

When we set the flux to the zero at the boundaries.

## 11:33

Now we're all right.

## 11:35

The shape doesn't change significantly,

## 11:37

but you'll notice something about the absolute magnitude.

## 11:40

Of this green curve relative to the other curves.

## 11:43

What do you see?

## 11:45

Is the peak the same?

## 11:49

No.

## 11:51

It's dropped by a little bit. Now,

## 11:53

when I first looked at that,

## 11:55

because even I sometimes will question what,

## 11:57

what I get out of model, it's good question.

## 11:59

It's like, did I get something wrong?

## 12:01

Shouldn't it approach the same.

## 12:03

Value in the middle. And in fact,

## 12:05

do we have any sanity check for what would happen in the middle of

## 12:08

this lab?

## 12:10

There was a trick. I, I showed you.

## 12:15

A couple of weeks ago when we were looking at diffusion solutions,

## 12:19

the diffusion equation.

## 12:20

Right.

## 12:21

We were looking at,

## 12:22

we were looking at the diffusion equation.

## 12:24

Right.

## 12:25

Sanity check on, on, on sort of magnitudes that we get.

## 12:28

If you remember the diffusion equation, I'll write it in, in this way.

## 12:32

If we have G C.

## 12:34

Double prime plus Sigma.

## 12:36

A B.

## 12:38

Is equal to S our source term.

## 12:41

If we're away from the boundaries and everything is homogeneous.

## 12:45

And our source term is uniform.

## 12:47

Meaning that there's no change.

## 12:49

Outside of, you know,

## 12:50

whatever our neutron population is doing the materials and the source

## 12:53

spec are constant.

## 12:55

That means away from the boundaries where the leakage is driving this,

## 12:59

this gradient of the flux,

## 13:01

we can sometimes assume that there is no spatial rate of change,

## 13:05

which means that far away from, from,

## 13:08

from things that would drive a flux gradient, we would say, Hey,

## 13:11

this goes to.

## 13:12

To zero.

## 13:13

And we would have.

## 13:15

We could call this fee.

## 13:17

A S Y for absolute.

## 13:19

Mass.

## 13:20

Segment.

## 13:21

To the S over the Sigma.

## 13:23

Right.

## 13:24

And we, we saw this work out in a problem here.

## 13:27

It does.

## 13:28

And it seems to work.

## 13:33

What would what?

## 13:34

What what's our Sigma a, for this problem.

## 13:36

Yeah, so.

## 13:40

In our sources, what one.

## 13:41

Right. So what would we expect the flux to be kind of at a maximum?

## 13:44

Right.

## 13:45

At a maximum in the middle.

## 13:47

Where.

## 13:49

A hundred, right.

## 13:50

Obviously it's pretty large.

## 13:52

Right.

## 13:53

We have a source term of one, like certainly, and a lot of the homeworks I'll often use

## 13:58

like sigma A is equal to 0.1 or 0.5, and we don't get a huge increase in the flux relative

## 14:03

to the source, but here we do.

## 14:06

Now, the question is, is there a bug?

## 14:07

Is there a bug between this green curve and the black and dotted blue curves?

## 14:13

Like, shouldn't this be closer to 100?

## 14:15

Well, let's take a look back at this expression or this numerical evaluation.

## 14:24

So this is the zero flux case.

## 14:27

We know that this is a little bit lower than the numerical estimates, okay?

## 14:30

So if I wanted to see this thing blow up, then what I can do is get closer to a situation

## 14:37

where I should be able to do this, and that means I have to make the slab bigger, right?

## 14:43

I need the volume to be bigger relative to the amount of leakage I have.

## 14:47

So the easiest way to do that is just increase A, and I can do it here because this is all

## 14:52

just, I'm plugging it into one expression.

## 14:53

So why don't I make this 200, and now that flux does appear in the middle to grow to

## 15:03

its asymptotic value of 100, okay?

## 15:06

So even though it looks like it was a step down from these other things, we know that

## 15:11

the fact that it has this forced leakage from the zero flux boundary condition probably

## 15:16

does lower it a little bit, and because it's not a large enough slab to see this asymptotic

## 15:21

value, that's kind of why it looks a little tricky.

## 15:25

Why I would, you know, sometimes second guess myself, but it turns out that everything is

## 15:30

hunky-dory, as it were, and this is the right answer.

## 15:34

If I were to take this numerical solve and increase the width, I would also see it rise

## 15:40

up to that asymptotic value.

## 15:42

So what this means is if you're in a leaky slab, as we are here, where there's a lot

## 15:48

of neutrons leaving the slab, if you've got the zero flux condition, one, that's going

## 15:52

to put a huge bias, which is why I've said all along, I don't like this.

## 15:55

The zero flux condition, super easy for pen and paper, but it will give you, you know,

## 15:59

wrong result.

## 16:00

Now, the question is, between the transport problem, which is the blue curve, and the

## 16:05

black diffusion with vacuum conditions, is there an error?

## 16:08

Well, you can see a little glitch at the boundary, and so it helps if we get rid of this zero

## 16:15

flux condition, okay?

## 16:19

And we can blow that up a little bit, and still the glitch is there.

## 16:25

The transport.

## 16:26

Solution, if you look, is just slightly higher than the black curve all the way through.

## 16:31

The black curve is a little bit higher than the transport solution on the edge, but it

## 16:36

doesn't seem like it's terrible, right, from this.

## 16:39

But what we can do instead is plot the error in this, okay?

## 16:45

And so what I'm doing is I'm taking the diffusion solution, subtracting the transport solution,

## 16:50

and then dividing by the transport solution.

## 16:52

So what I'm getting is the relative error in the diffusion flux.

## 16:56

Relative to the transport solution in percentage, okay?

## 17:01

And if you look at that, near the boundaries, oh, is this, that's not the, is that the right

## 17:10

thing?

## 17:12

That's not the right.

## 17:16

I've got to, I think I had run something, and oh, I've got to go back and change that.

## 17:27

See, this is the problem when you change a Jupyter notebook, things get all wonky unless

## 17:33

you go back and.

## 17:34

There we go.

## 17:42

And there we go.

## 17:45

That's what I want to see.

## 17:52

All right.

## 17:53

So in the middle, the error tends to go to zero.

## 17:58

At the boundaries, the diffusion solution, even though it didn't look like a huge difference,

## 18:04

is actually off by close, well, over 10%, okay?

## 18:09

So the first observation that we can make, just based on these results, is that diffusion

## 18:14

theory tends to.

## 18:16

Fail by vacuum boundary conditions, right?

## 18:18

Even though we're using this sort of self-consistent way to say, hey, no neutrons come in.

## 18:23

You might question, where do those expressions for partial currents come from?

## 18:27

I think you would ask, like, I'm not really buying this at the back of the book, right?

## 18:31

We'll talk about that a little bit at the end of the class today.

## 18:34

But it is self-consistent.

## 18:37

When we derive diffusion theory, those partial currents are the right way to say, hey, we

## 18:42

have no neutrons coming in.

## 18:44

But relative to full transport.

## 18:45

Obviously, there's some issue here, okay?

## 18:49

That's one observation, right?

## 18:51

Near vacuum boundary conditions.

## 18:54

And one could generalize that to be near interface conditions where things are very different

## 18:59

on either side.

## 19:00

Vacuum is obviously very different from having a material with a scattering cross-section

## 19:04

and such.

## 19:05

So that's the first thing that we can do.

## 19:08

So the other thing that we can do is look at a localized source with reflecting conditions.

## 19:13

So what you can see here is.

## 19:15

I'm defining something called a source map.

## 19:17

I've broken up our slab into 20 equal-sized regions.

## 19:20

And what I'm doing is I'm saying, hey, I'm going to put a source in the very first region,

## 19:25

right?

## 19:25

So this was 20 centimeters wide.

## 19:27

So I've got a source term in the very first centimeter worth of the slab.

## 19:31

Then the material map.

## 19:32

I've got several materials.

## 19:33

We can talk about what those are.

## 19:35

It's just homogeneous with the scattering cross-section of 0.99.

## 19:40

And this is what we get for the flux.

## 19:43

Now, on this plot.

## 19:44

We can actually see more apparently the difference between transport and diffusion, right?

## 19:49

The transport result is higher and then dips down a little bit below the diffusion overall

## 19:56

on the average.

## 19:57

And here the error is more pronounced.

## 20:05

Okay.

## 20:05

So the diffusion theory in this case under predicts by a significant margin, right?

## 20:11

So 3% and it goes for quite a while.

## 20:14

And then.

## 20:14

And then as we get away from the source, right, it will then ultimately go to zero, right?

## 20:22

Which says that the way that this like kind of a corollary that we get from this is diffusion

## 20:26

theory is giving us a flux that is very close to the transport solution.

## 20:31

When we're far away from this nasty business of vacuum conditions or the localized source

## 20:37

term, right?

## 20:38

When we're in this sort of region where as we could do this with the transport equation

## 20:43

to make an assumption.

## 20:44

Where spatial rates of change go to zero, we'll still get this asymptotic form.

## 20:49

So diffusion transport super consistent in the region where things aren't changing in

## 20:54

space, right?

## 20:55

But how many practical applications are there where things aren't varying in space?

## 21:00

Not too many, right?

## 21:01

And then it becomes a question of how much is something changing in space and how good

## 21:06

is diffusion for that, that, that gradient.

## 21:09

Okay.

## 21:09

So second observation, if you diffusion fails.

## 21:14

By.

## 21:14

Localized sources and, but by localized, I mean finite, it's not homogeneous over the

## 21:19

entire region.

## 21:20

And you'll notice for this, I use reflecting conditions so that we don't have any issue

## 21:24

with a vacuum battery, right?

## 21:25

We're looking at the impact of having a source term in one region of space and nowhere else

## 21:30

all by itself.

## 21:32

Okay.

## 21:34

So a final example is let's take a localized absorber with a uniform source.

## 21:41

We've got to have neutrons coming from somewhere.

## 21:42

We're not going to do an eigenvalue problem.

## 21:44

We're going to do an eigenvalue problem.

## 21:45

We're going to do an eigenvalue problem.

## 21:46

So what I'm going to do is I'm going to take that same slab and right in the middle of

## 21:50

the slab, I'm going to put a region one centimeter wide region where Sigma a is significantly

## 21:55

larger than 0.01, right?

## 21:58

So I'm going to increase it to 0.5.

## 22:00

So the scattering ratio goes from 0.99 to 0.5, right?

## 22:07

Which is below that 0.7 cut, cutoff that Lewis identifies in the book as being, Hey, diffusion

## 22:13

theory is not going to work for that.

## 22:14

Okay.

## 22:15

And in fact, we can see, right?

## 22:17

So I put that, that little blip, right?

## 22:20

So it's because I have 20 slabs, I can't have a perfectly symmetric solution here.

## 22:24

So it's right to the left of the center mark.

## 22:27

That's where my high absorption is.

## 22:28

You can see that it really has a big impact on the flux, right?

## 22:32

So we had a flux that was, you know, converging very close to the asymptotic value, right?

## 22:38

And by putting in this, this absorber here, I'm totally depressing the flux, right?

## 22:44

Causing.

## 22:44

This huge gradient.

## 22:45

So not only do I have to localize absorption here, but that's caused now a gradient that

## 22:50

propagates throughout the slab.

## 22:52

So this is maybe the most, like the wildest error that we see in terms of its impact across

## 22:59

the entire slab, right?

## 23:01

And so we're seeing errors close to 10% again, okay.

## 23:05

Huge, right?

## 23:06

Especially if you, you know, you're trying to compute a reaction rate to within 1%, which

## 23:11

is kind of like a, that's a good rule of thumb.

## 23:13

If you're in real world.

## 23:14

Real world reactor analysis, if I want to get the fission rate estimated either from

## 23:19

a measurement or from simulation or a combination of both, I want to be able to resolve pin

## 23:24

powers to within 1%, which means that I've got to get the, the diffusion based or the

## 23:30

transport based flux also to within about a percent, right?

## 23:34

Cause then it's that multiplied by cross sections, et cetera.

## 23:37

So this would be a total no-go for a real world application, right?

## 23:42

You'd have to do something.

## 23:44

To account for this junction between high scattering and high absorption, right?

## 23:49

Diffusion theory alone wouldn't be able to do that.

## 23:53

So summary of observations, and these are totally consistent with what's in, in the

## 24:00

book.

## 24:01

Diffusion theory breaks down when we have vacuum conditions, localized sources, localized

## 24:07

changes in absorption, right?

## 24:09

So basically anything that is driving a spatial rate of change in neutrons.

## 24:15

Right?

## 24:16

Causing, causing that gradient to be driven by something that is not just from concentrations

## 24:22

of neutrons alone, right?

## 24:24

If I put a, a bunch of neutrons here, have them scatter through a diffusing medium,

## 24:29

diffusion theory is pretty good.

## 24:30

But if I'm putting things into that medium that cause the neutron population to change

## 24:35

faster than they would just by diffusing alone, well, then diffusion theory has to break down,

## 24:41

right?

## 24:42

So what the heck is transport?

## 24:47

Theory doing that?

## 24:49

What is it that we're using out in diffusion theory, right?

## 24:54

When we derived it, our first, like the first equation we got in terms of the current vector,

## 25:01

right?

## 25:01

Before we applied fixed law, that was all fine.

## 25:04

Diffusion theory is really equivalent to inserting fixed law, relating the current to the derivative

## 25:12

of the flux or the gradient of the flux, right?

## 25:15

So what is that?

## 25:17

Getting rid of, like, what, what is the missing piece?

## 25:22

Think about neutrons.

## 25:23

They're, they're, they're particles, right?

## 25:25

How would you describe a particle?

## 25:27

I know we talked about this a little bit after class last time, right?

## 25:30

And so I'm going to continue on a little bit more formally here for everyone.

## 25:33

If I were to describe a single neutron out in the wild, okay, one of many in a nuclear

## 25:39

reactor, what are the things that I can assign to it?

## 25:41

What are its properties?

## 25:43

So actually, that's, that's, that's, it's the missing key here, right?

## 25:47

So we've, so far.

## 25:48

We've talked about neutron density in terms of a location, right?

## 25:52

Either VETR or, you know, slab case that's at a position X in the slab.

## 25:56

We've talked about neutrons having energy, right?

## 26:00

We did a whole bunch of reactor physics using cross-sections early on in the course and forgot about
space at that moment that had energy.

## 26:07

Then we used this energy, we, we had all the energy stuff.

## 26:12

We were able to take that and then boil it down to say single energy or a single speed.

## 26:16

And we did some time dependent stuff.

## 26:18

Right?

## 26:19

So we know that we already knew that neutrons have a location.

## 26:22

They have an energy, they have a speed, but what we didn't account for is that speed and energy
really represent three components of velocity.

## 26:31

So you can either treat it as three velocity components, or you can treat it as an energy with two
directions.

## 26:37

And what are the directions?

## 26:38

Well, if I choose my straight up vertical as my polar axis, then I have an angle relative to that.

## 26:45

But then in the X, Y plane, I have an azimuthal angle.

## 26:48

So there's.

## 26:48

There are two degrees of freedom for direction if you want to use energy or, or the speed magnitude
is that third degree.

## 26:55

So either one is, is fine.

## 26:57

So what transport theory is accounting for is that direction.

## 27:01

It's not to say that the fusion theory is totally ignoring direction.

## 27:06

It's just that in our discussion of diffusion theory, to this point, there has been no discussion of
direction, right?

## 27:12

I'd said early in the class that we're not going to touch direction.

## 27:15

I feel in this last week where we're all just kind of relaxing a little.

## 27:18

But I can talk a bit about it.

## 27:20

This stuff won't be on the exam.

## 27:22

Obviously, maybe some, some things about validity of diffusion, because that, that is part of the
book, but doing anything to do with transport theory is at that worst, an extra credit question.

## 27:33

Okay.

## 27:34

So what is transport theory doing differently?

## 27:37

And it's all about this direction, right?

## 27:38

So we've talked before about the neutron density.

## 27:43

Where's this big stick.

## 27:47

This one.

## 27:48

And then we've talked about the neutron density.

## 27:50

And then we've talked about the neutron density.

## 27:51

So what we'll do is we'll, we'll, we'll look for a new unknown, right?

## 27:55

So we've already talked about the same end, the neutron density.

## 27:59

The way we've talked about it though, has been only with respect to spatial position and then
energy.

## 28:05

What we're doing now is saying, Hey, let's forget about energy.

## 28:08

Let's just say that the neutrons have a direction because you can still quantify neutrons in that
way, right?

## 28:12

You could have a mono energetic source of neutrons, right?

## 28:15

All neutrons are 0.0253 EV.

## 28:18

Or maybe.

## 28:18

Either 10 MEV from a neutron generator, whatever it might be.

## 28:22

We can ignore energy and still have this discussion.

## 28:24

So now our neutron density is going to be written like this.

## 28:27

And what that's going to tell me is something like the average number of neutrons at this point in
space in some sort of differential volume going in some direction, right?

## 28:38

And if I wanted to surround it by a unit sphere, I could say, Hey, some, some small region on the
surface of the unit sphere is the directions that we're talking about.

## 28:48

So different.

## 28:48

Right.

## 28:49

So the extreme top.

## 28:50

At 0.3.

## 28:50

At 0.3.

## 28:51

At that point, the intersectional.

## 28:53

We're going to be writing a number of neutrons at this point in time of the

## 29:07

It's not going to say how many neutrons are actually in one place, but it will say how many it's
going to be."

## 29:13

So now we're talking about the Earth going from zero to a neutron density, right?

## 29:16

And 0.3 is 0.3.

## 29:17

0.3.

## 29:17

0.3.

## 29:17

0.3.

## 29:18

0.3.

## 29:18

0.3.

## 29:18

0.3.

## 29:18

0.3.

## 29:18

this angular flux we can define some quantities that we are familiar with if i integrate this

## 29:25

angular flux over all angles which in this case is all angles on the all the area of the unit

## 29:31

sphere right at four pi who who is familiar with four pi steradians and so certainly this is

## 29:39

something that is covered in shielding right things like um what are the terms is the term

## 29:47

view factor is that that's actually in radiative heat transfer i think but anyway you view you do

## 29:52

solid angle calculations and so the four pi is what i'm talking about here so if i integrate

## 29:56

over all angles i get the same flux that we've talked about before so if this thing didn't have

## 30:02

any dependence on angle then we would be able to relate it directly to the flux it would be if

## 30:07

it would be the flux divided by four pi right is an isotropic so everywhere in every angle

## 30:14

equal angular flux but in general it's not

## 30:17

and then we can also take that flux multiply it by the direction integrate over all angles and we

## 30:23

get the current right if you think about it this way if i've got a neutron density forget about

## 30:28

speed for a moment and they're going in every direction this is effectively taking taking that

## 30:34

uh direction dotting it with the surface of whatever thing i'm enclosing it in and getting

## 30:39

the net flow right it's the same thing we did with this this box and around a volume for the

## 30:47

right it's now coming directly though from this quantity that we define so these are exactly what

## 30:52

we've talked about before now they're just being defined in terms of this new quantity the angular

## 30:58

flux all right so in slab geometry where we've been spending our time this stuff reduces to

## 31:07

significantly simpler expressions right so if we are only considering dependence on x we can

## 31:15

choose that to be our polar angle and so if we lose one of our degrees of angular

## 31:20

freedom right so rather than treat the xy plane we're going to take neutron travels to be along

## 31:26

z but because x y z are all totally um arbitrary we're just going to choose x to be our our polar

## 31:33

directions and so the polar angle is theta and its cosine is mu and so we can actually quantify

## 31:47

everything if neutrons are traveling along this this axis

## 31:50

they make a range of directions of travel relative to that axis but we can quantify

## 31:56

everything in terms of the cosine right because the cosine takes that angle of travel and projects

## 32:01

it down onto the x-axis so a neutron going at 45 degrees at some speed is going to be making less

## 32:09

distance along the x-axis right because it's spending some some of its time moving upward

## 32:13

right but we've ignored uh that other stuff so at any rate we have these definitions for phi and j

## 32:20

in slab geometry and by changing from theta to mu then we the cosine of course ranges from negative

## 32:28

one to one so going in the reverse going all the way to going completely forward okay

## 32:34

anyway with this this new psi of x and mu this is what the transport equation is now

## 32:41

it wouldn't take a whole lot of effort to drive it basically the same way that we did

## 32:46

the diffusion equation it's just a statement of balance

## 32:49

in 1-D it's a

## 32:50

it's pretty easy to explain. Imagine that we've got neutrons moving along this x-axis. Choose any

## 32:57

mu, right? Maybe it's straight ahead. Call mu equal 1, and we're talking about balance of

## 33:01

neutrons along 1. So if I start off with neutrons going in this positive x direction, what are the

## 33:07

things that are going to cause them to leave this differential volume? Well, if there's a spatial

## 33:13

rate of change, that means neutrons are leaving, right? So they're exiting this little sliver dx

## 33:18

just because there is a spatial derivative. As they move through that little sliver of dx,

## 33:24

they're going to interact, right? Any interaction is going to take them out of that angle, right?

## 33:30

Because if it has a scatter, it'll go in some new direction, right? If you end up in the same

## 33:34

direction, have you actually scattered? It's the same thing we talked about with energy, right?

## 33:39

If you could end up with the same energy after a collision, but is that really a collision,

## 33:45

right? That's the bounding case, okay? And if you have an absorption,

## 33:48

you're also going to be gone. So any reaction interaction that neutron has in a sliver dx is

## 33:55

going to remove it from that part of phase base. By phase base, I mean location and angle. And so

## 34:01

really what I'm talking about is it removes it from that direction, okay? So that's why I have

## 34:06

sigma t here, not just sigma a, right? Because any interaction is going to take it out. Those are my

## 34:10

loss terms, right? But how else am I going to get neutrons to enter that region at x in the angle

## 34:17

that I'm doing?

## 34:18

For us right now, it's going straight ahead. Well, I can have scattering, right? And we already

## 34:22

know that the number of neutrons scattering is sigma s times phi of x, right? That's my scattering

## 34:27

rate. The divide by two accounts for the fact that if I'm scattering, I can go in any of these

## 34:34

directions between negative one and one, right? Or the directions that correspond to cosines going

## 34:39

from negative one to one. And that's because this expression is isotropic scattering. Isotropic

## 34:45

scattering means that for a neutron going in at one,

## 34:48

the chance it goes out in any other direction is uniform, right? Now, is this actually true?

## 34:58

Do we remember anything about isotropic scattering? So remember, there are two frames of reference.

## 35:07

There's the center of mass and the laboratory. Which frame do we live in? Huh? The lab system,

## 35:16

right? Because if we're doing a laboratory experiment right now, like hypothetically,

## 35:20

the center of mass system is not a real system in the sense that that's not what

## 35:24

we observe. But a lot of analysis is a lot easier in the center of mass system. And so from the

## 35:31

theory, we know that a lot of scattering tends to be isotropic in the center of mass. But because

## 35:36

of that, this transformation from the center of mass system to the lab system takes those isotropic

## 35:42

scattering laws, makes them incredibly anisotropic. Think of it this way. If we know that

## 35:50

neutron scattering off of hydrogen is isotropic in the center of mass system,

## 35:54

which it is, you know, to a very large degree for neutron energy is less than, say, 2 MeV.

## 36:00

When we go to the lab system, it's incredibly anisotropic. And the easiest way to describe

## 36:05

that is to think of billiards. And Dr. Bahaduri and I just shot pool last Friday, which was cool.

## 36:11

Well, it was cool in the sense that I got to play pool. It was not cool because I lost miserably,

## 36:16

right? I can talk about billiards. I can't play. But if I take the cue ball and I hit some other

## 36:21

ball dead on, what happens to the cue ball?

## 36:24

It stops. What happens to the other thing?

## 36:27

It takes on.

## 36:28

Right. And if I don't hit it dead on, then what happens to the cue ball?

## 36:35

It keeps moving. And generally by what we mean when we say keeps moving, keeps going away from

## 36:42

me, right? If I'm hitting it, the only way that I get the cue ball to scatter back is if I hit

## 36:47

something like the wall or if I hit something that has a lot more mass, like the entire set of balls

## 36:53

when I break all of them.

## 36:54

Right.

## 36:54

Right.

## 36:54

You know, you set up all nine to nine and I don't know what you basically when you're breaking,

## 37:00

of course, you can have the cue ball come back. Right. That's the same thing that would happen

## 37:05

if I take my neutron and I scatter off a uranium 238 nucleus in the lab system, I can have that

## 37:12

neutron bounce back. And so in the limit that the target mass goes to infinity, then I do have

## 37:18

isotropic scattering in the laboratory system. Right. And that's the same thing I would get if

## 37:23

I took a cue ball and I bounced it off.

## 37:24

I could have it scatter off into any angle. Okay. So when I write something down like this,

## 37:31

or if we're talking about isotropic scattering in terms of diffusion or transport, it always means

## 37:36

the lab system. And you always have to remember where is that approximation valid? It's really

## 37:41

only valid if we're talking about scattering targets that are much more massive than the

## 37:46

neutron for things like water or pure hydrogen, totally not right because scattering tends to be

## 37:52

forward biased.

## 37:54

Which means that on the average, if I have a neutron going in dead ahead into the hydrogen,

## 37:58

I have a very low chance of, I have a zero chance of going backwards, right? Because the worst that

## 38:04

can happen is my neutron can stop. And that mathematically is like a 90 degree angle, right?

## 38:10

I can never backscatter if I have equal masses colliding right in the lab system when one is at

## 38:15

rest. So I will always have forward peaked, right? We quantify that by mu bar, right? The average

## 38:23

cosine.

## 38:23

Right. The average cosine. Right. The average cosine. Right. The average cosine. Right. The

## 38:24

average cosine. Right. The average cosine. Right. The average cosine. Right. The average

## 38:24

cosine. Right. The average cosine. Right. And then we calculate the scattering ratio and we

## 38:25

remember that that shows up in diffusion through the diffusion coefficient, right? Because sigma TR,

## 38:32

the transport cross section is adjusted by taking sigma T and then subtracting out some part related

## 38:39

to that scattering angle, okay? So diffusion theory all along has been able to account for

## 38:45

something related to angle, right? But that's the only place that it shows up, okay?

## 38:51

Anyway, so our scattering is isotropic, meaning

## 38:53

meaning that neutron scattering

## 38:55

are going in any of these directions,

## 38:57

which is why there is no angle here.

## 38:59

And then the same thing is true for our source term.

## 39:01

I'm assuming an isotropic source,

## 39:02

meaning that neutrons are spit off at that point in X,

## 39:06

B to the left, to the right with equal number, okay?

## 39:09

So that's our equation.

## 39:12

And if you look at it, it seems benign,

## 39:15

but even in 1D slab land, there's a lot here.

## 39:19

Because if you look at this, we have two unknowns.

## 39:21

We have psi and we have phi.

## 39:23

Well, they're not really independent, right?

## 39:26

Because phi is equal to this integral of psi, right?

## 39:29

So this is bizarre.

## 39:30

This is probably the first time that you've encountered

## 39:33

probably an equation that looks like this,

## 39:35

where we have a derivative and an integral

## 39:40

all in one equation.

## 39:42

And this is a special class of equations

## 39:44

called integro-differential equations.

## 39:47

And those are nasty beasts,

## 39:49

and they take a lot more math than you had

## 39:52

to really dive in and solve,

## 39:53

which is why this is not an undergrad topic

## 39:55

to pursue beyond a lecture like this, okay?

## 40:00

So also it's a first order differential equation

## 40:05

if we just zero in on the derivative part of it,

## 40:08

which means that the boundary conditions

## 40:11

aren't quite the same as they are for diffusion theories.

## 40:13

This is second order.

## 40:15

So if we're in slab land, we need two boundary conditions,

## 40:18

one at the left and one at the right.

## 40:20

Well, we also need that for the transport equation, but,

## 40:23

because it's partial differential,

## 40:26

there will be some dependence on mu.

## 40:29

So at the left boundary condition, we're gonna say,

## 40:31

hey, it's gonna be some known angular flux

## 40:34

at that left condition for mu values greater than zero.

## 40:39

What does mu greater than zero mean

## 40:41

about the direction of travel?

## 40:43

If this is my boundary and I'm looking at the boundary,

## 40:47

which way is mu greater than zero?

## 40:49

This way or is it this way?

## 40:52

It's forward.

## 40:53

right that makes sense if i have neutrons on my left boundary i need to define the neutrons going

## 40:59

in the right direction into that left boundary right into the slab going to the right same thing

## 41:05

at the left or at the right boundary then i care about neutrons that are going along the negative

## 41:10

x uh x-axis right so you you've got to split it up in terms of angle right that's just another

## 41:15

feature of this equation that makes it different from what we've done before and if i set these to

## 41:21

zero that represents a true vacuum condition right i'm now saying that as a function of angles there

## 41:27

are no neutrons coming in to this slab at that location x right that that is the true vacuum

## 41:34

condition as opposed to the diffusion vacuum condition which just says the partial current

## 41:39

is equal to zero well what does the partial current mean it just means the total flow in that

## 41:44

direction it's it's basically giving you one degree of freedom for neutrons that go to the left

## 41:49

and neutrons that go to the right and neutrons that go to the left and neutrons that go to the right

## 41:51

right. This is accounting for all possible directions. All right. So it's this mu that

## 42:01

makes this a challenging beast, right? Because one, it makes it a partial differential equation.

## 42:08

We have that integral, which makes it integro differential. And so treating mu is the one thing

## 42:14

that makes this a hell of a lot different from our diffusion equation, which has only this

## 42:19

dependence on X. So I like to do things kind of simply. And, you know, if I were to take that

## 42:26

equation with this unknown size, a function of X and mu, one thing that would seem reasonable to me

## 42:33

is to say, Hey, what, what happens if I just make it the simplest possible function of mu,

## 42:39

right? In a sense, this is like separating the variables, right? And then assuming some sort

## 42:44

of form for one. I'm, I just want to see what happens. Let's just assume that psi,

## 42:49

has a dependence on mu, but it is only linear, meaning I have these two degrees of freedom. I

## 42:54

have this constant part, and then I have the slope essentially. Okay. And the constant part in the

## 42:59

slope are separate functions of X, right? So I still, I still have these two unknowns, right?

## 43:05

And so I'm making my life slightly harder because I've got to come up with an equation for two

## 43:10

unknowns, but we'll find that the result is I think satisfactory. Okay. So let's go ahead and

## 43:17

do that. So if we say that,

## 43:19

psi is equal to a constant term. And when I say constant, I mean, relative to mu,

## 43:23

and then the linear term, something that has the slope. Okay. We can immediately put this back into

## 43:28

the integrals from the last slide, if you trust them. And we see that there's a relationship

## 43:33

between psi zero, the constant part in our flux, and then the current vector and psi one, right?

## 43:39

So that's just an observation that, that we can use in a moment. But if I put this approximation

## 43:44

into the neutron transport equation that we just saw, I get this nasty thing, right? So I've made

## 43:49

something that was actually kind of, I don't know, compact into something that looks really messy

## 43:54

that now has like mu squareds and things like that. So this alone wouldn't help me at all. But

## 43:59

the next thing you can do is to produce two equations for the two unknowns. One way to do

## 44:05

that, and you see this all the time in mathematical physics, you integrate the equation, right? And
so

## 44:12

in this case, I can take this equation two, and let's just integrate it over all angles. Remember,

## 44:17

it's the same thing that we've done with the two unknowns. So I can just integrate it over all
angles.

## 44:19

The diffusion equation, if you integrate the diffusion equation over a region of space or a

## 44:25

region in energy, it still should be balanced. If you have a balanced differential equation,

## 44:31

integrating it in any way over the independent variable should still leave you with balance.

## 44:37

Does that make sense? Raise your hand if, if that does not make sense to you. Raise your hand if

## 44:46

it does make sense to you. If you have a differential equation, and you plug in the

## 44:50

actual solution to it, where you assume you have the solution, you integrate it in any way over the

## 44:54

unknown x, maybe, you will still have a balance equation, okay? And if you use that fact, we can

## 45:02

take this and integrate it over mu, mu from negative one to one, and we get something quite

## 45:11

a bit simpler. All right, that's cool. Now, the problem is we still have two unknowns. We have

## 45:18

psi zero and psi one.

## 45:20

Okay, how can we get another equation? We need two equations. I've just, I've taken this original

## 45:27

equation, I've integrated it over mu. What's something else that I could do? Another trick

## 45:36

that follows in this, this kind of path that you see a lot in mathematical physics is

## 45:41

multiply both sides of the equation by something, and then integrate it again.

## 45:45

You choose something wisely. In this case, the wise thing to multiply by is mu. So if we take

## 45:53

this equation, and we multiply through by mu, and then integrate again over mu. Now, this, I'm not

## 46:00

saying that this should be an obvious thing to do. I'm saying this is a common technique that is
used,

## 46:06

right? But if we do that, take equation two, multiply it by mu, and then integrate again,

## 46:12

then we get this, which is actually even simpler than this. Okay, what's cool about this equation?

## 46:21

This one's important.

## 46:23

Because this equation four now gives me a direct relationship between the two unknowns. I have

## 46:29

psi one is somehow related to the derivative of psi zero. Well, if you kind of look upwards,

## 46:38

if we know that psi one is just a constant times j, right? So psi one is effectively our current,

## 46:44

right? It's off by a constant. And we know that psi zero is related to our flux.

## 46:53

Can we see where this is headed? This is fixed law in disguise, right? We haven't seen it all the

## 47:01

way through yet, but this is coming up with fixed law. And it starts with this assumption that

## 47:07

our angular dependence is the simple linear approximation. Okay, so equation four gives us

## 47:15

our unknowns, a relationship between unknowns. And so if we take four, then we solve for psi one.

## 47:23

and if we use our previous relationship between psi 1 and j and then psi 0 and the flux and voila

## 47:31

that's exactly Vick's law for this 1d case although the same thing can be done in in

## 47:37

multiple dimensions and if you put that all back into our uh the the first of our projected

## 47:43

equations the first result we got when integrating over mu it's this thing right which kind of looks

## 47:49

familiar to our diffusion equation but when you substitute everything in we end up with this where

## 47:54

d is 1 over 3 times sigma t now the one detail that's not included here because I didn't want

## 48:01

to add even more is the fact that if we chose to have a scattering source that was not isotropic

## 48:09

but one that included linear anisotropy right one that said that hey scattering does not lead to

## 48:15

uniform spread over all angles but will

## 48:18

you

## 48:19

have a linear dependence which accounts for some forward peaking you can account for that exactly

## 48:24

in the same approach and we what you would end up with then is that d is not just 1 over 3 times

## 48:31

sigma t but it would be 1 over 3 times sigma t with this additional adjustment from from uh
scattering

## 48:36

so what this all means is that diffusion theory is a good approximation to the transport of neutrons

## 48:49

because uh the

## 49:15

okay

## 49:16

what on our line isso force sum b we wouldn't have an 처� .

## 49:18

Actually, we could have a source term, right?

## 49:20

But if we have this equation

## 49:22

and we look at the homogeneous solution to it,

## 49:25

what is the homogeneous solution?

## 49:32

If I were to have no absorption in my diffusion equation,

## 49:40

then the sigma A times V goes to zero, right?

## 49:43

If I ignore source terms for the moment,

## 49:47

what is the solution to this equation, right?

## 49:49

That the only thing I have left is that fusion.

## 49:51

What is the equation?

## 49:52

What is the, what is V in this case?

## 49:58

What kind of function has a second derivative

## 50:00

that's equal to zero?

## 50:06

A line, right?

## 50:07

This would be V of X is equal to C1 plus C2 times X, right?

## 50:15

So if I have something that is very linearly in space,

## 50:19

then the only thing that's causing the flow

## 50:22

is going to be its concentration from one point to another.

## 50:25

So if I could define boundary condition

## 50:27

and get my values,

## 50:28

for C1 and C2, right?

## 50:30

In this diffusion equation

## 50:31

where we don't have the sigma A times V,

## 50:35

well, that's a lot closer

## 50:36

to that heat conduction equation, right?

## 50:38

Because heat conduction,

## 50:40

the flow of heat doesn't have the self-interacting term.

## 50:43

The exception is when you get to the radiative heat transfer,

## 50:47

right?

## 50:48

Where you do have heat that interacts from the media.

## 50:54

A hot medium emits what?

## 50:56

I think black volume radiation, right?

## 51:00

So if you're trying to tackle radiative heat transfer,

## 51:03

that's all about the transfer of photons,

## 51:05

but you know, all heat is photon.

## 51:06

Everything is electromagnetic radiation, right?

## 51:08

So when you get to that, then you will have interactions,

## 51:11

but for basic conduction and per Poirier's law,

## 51:15

you'd have this and your solution in the slab

## 51:17

would be linear.

## 51:18

So in that case, fixed law is totally fine,

## 51:22

which is equivalent to saying that we don't have something

## 51:26

that is causing it to go away from being linear.

## 51:29

You put in absorption, absorption leads to attenuation.

## 51:34

And when we think of attenuation,

## 51:36

we always think of what function?

## 51:39

What kind of attenuation?

## 51:41

Exponential attenuation.

## 51:43

Is exponential linear?

## 51:44

Absolutely not.

## 51:45

So if you put in any bit of absorption that is localized,

## 51:48

you can have absorption in the slab,

## 51:52

but even if you put that in a slab

## 51:54

that has boundary conditions, you're going,

## 51:55

you'll have that.

## 51:56

The exponential attenuation and you break this, right?

## 51:59

So it's really in sort of in the limit

## 52:02

that you have zero absorption, zero localized sources

## 52:05

that fixed law is exact.

## 52:07

You can use fixed law in many other cases

## 52:11

that it's pretty flexible,

## 52:12

but this is kind of telling you the whole story.

## 52:14

So anyway, that's fixed law in a nutshell,

## 52:18

in the 1D slab land.

## 52:19

What we'll do next time will be driven, I guess,

## 52:22

by maybe what I'll have you do is,

## 52:26

send me specific requests for the type of problems

## 52:29

that you would like to review next time, right?

## 52:33

You know me, I'm pretty good at just shooting from the hip.

## 52:34

So I'll fill the time, no problem with that.

## 52:37

But if you want it pointed about certain problems,

## 52:40

how to solve problems,

## 52:41

going back to some of the homeworks that we've had,

## 52:43

understanding where things went wrong.

## 52:45

If you still got this burning question

## 52:47

about why the answer was this

## 52:51

and not what you submitted or whatever,

## 52:53

tell me and we'll tackle that, right?

## 52:55

Because then the final answer, right?

## 52:56

The final exam is on Tuesday.

## 52:58

And because I have a strong desire to be on the road,

## 53:03

probably Monday,

## 53:05

I am leaning toward making it a take-home exam

## 53:08

that would be released on Monday at roughly noon-ish

## 53:11

or whatever our time is,

## 53:12

and then due at the end of our scheduled exam time.

## 53:16

Raise your hand if that sounds more favorable

## 53:19

than sitting in here.

## 53:23

Matt, you are ambivalent or it doesn't matter one way,

## 53:28

really, or the other.

## 53:29

Okay, I'm seeing many more hands.

## 53:31

So if that doesn't sound appropriate,

## 53:34

let me know too in your email,

## 53:36

but you don't have to send me emails,

## 53:38

but if you have specific things that you'd like to work on,

## 53:41

go ahead and do that.

## 53:45

I will see you Friday.

## 53:58

We are sort of kind of running out of time,

## 54:01

I think.

## 54:02

We're starting with whatever.

## 54:03

Or we can go right, go ahead.

## 54:04

Yes, go ahead.

## 54:05

It used to be like electronics or any of those?

## 54:09

And it's new electronics.

## 54:11

I say it depends on who's audit,

## 54:14

but we normally went through derivation at .

## 54:21

I can't remember if I made the formal derivation

## 54:25

of like using here.

## 54:27

I think I...

## 54:28

I've only caught it on a numerical transport class as a sort of like a special concept

## 54:36

on reflection I realized that what I was doing in that class actually shouldn't just be

## 54:41

but yeah you're absolutely right this this stuff would be

## 54:46

yeah it's cool stuff at least a relation you know yeah it's yeah it's um yeah it's nice

## 54:54

nice to make connections so right yeah see where the simple stuff can lead you yeah yeah
