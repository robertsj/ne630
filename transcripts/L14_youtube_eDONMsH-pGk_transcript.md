# L14 Local Audio Transcript

Course: NE 630

Playlist source: https://youtube.com/playlist?list=PLy481lNHlnHoEO95vM-xYX2bydD25v20L

Video: NE 630 - Lesson 14

URL: https://www.youtube.com/watch?v=eDONMsH-pGk

Video ID: eDONMsH-pGk

YouTube upload date: 20230922

Duration: 54:22

Transcript source: Local faster-whisper transcription from YouTube audio.

Whisper model: large-v3; detected language: en.

Generated: 2026-06-28

Note: This transcript is machine-generated from audio and lightly wrapped only. It should be reviewed before being quoted, published, or used as polished lesson text.

Requested language: en

## 00:14

all right okay so happy friday anybody doing anything fun this weekend

## 00:45

sleeping sleeping yes okay homework all right homework god anybody

## 00:52

yeah well it's in part that's um so i i think the the question where i'm asking you to uh

## 01:03

produce that spectrum it's a an okay question but i realized as i was working through my own

## 01:10

solution um that it was more open-ended than i had figured so i made some adjustments to

## 01:17

the statement which is really why i extended it and i think that those

## 01:20

clarifications closed some of the gaps that you would have had to to fill

## 01:26

but even then i'm not super satisfied with the result assuming i did it right which

## 01:31

i'm pretty

## 01:33

sure i did it right uh and it kind of ties together what we what we did before and what

## 01:38

we're doing today and it highlights that the simple-ish approximations in the book sometimes

## 01:45

when you put it all together and try to make it look like a formal solution like a you know but

## 01:50

the real answer it's going to fall short right uh if you try to view it all together and use it

## 01:55

uh in the way that maybe i would want to for computing things like these effective cross

## 02:02

sections so

## 02:02

hopefully

## 02:03

today we'll highlight at least parts of why it will look a little odd right when you actually

## 02:09

put together so i'll show you um that that solution actually maybe before i forget i'll

## 02:15

just go ahead and uh try to show that um so i had started putting together a solution for that

## 02:23

problem and i'll walk just very briefly through some of the things that you ought to think about

## 02:29

um right so this is let's see

## 02:33

right so this is what i'm asking you to to use as the flux spectrum right where we have this

## 02:40

fasting chi over sigma t and then we have the one over e and then we have uh max volume um and the

## 02:47

thermal regime and what i'm asking you to do is use what's in the book in order to define

## 02:54

the the two constants that that kind of normalize everything so that we do two things one we have

## 03:01

this fast to, or let's say non-thermal to thermal flux ratio of one to one, right? That means the

## 03:07

integral of the flux above one eV is equal to the integral of the flux below one eV. That's a

## 03:14

reasonable ratio for a thermal spectrum reactor. Of course, that would be nonsense for a fast

## 03:20

reactor. I think our trigger reactor tends to have a much higher thermal flux. So it might actually

## 03:26

be a one to four type ratio for fast to thermal, but for something like a typical light water

## 03:31

reactor, power reactor, one to one is in the ballpark of reasonable, right? So that's one of

## 03:37

the constraints that you need for the constant. And that's really what we'll use for CT. For CI,

## 03:44

what I'm asking you to do is use the slowing down density, right? So we talked before about the

## 03:50

slowing down density is equal to the number of neutrons passing by a certain energy. Well, with

## 03:55

the

## 03:56

assumption we made for that fast flux, that means that all of the fission neutrons are passing by

## 04:00

that 0.1 MeV. It doesn't matter where they were born. We're just neglecting any scattering,

## 04:05

any reactions within that fast region, and they're all streaming past 0.1, right? So that

## 04:10

gives us what Q is. So S F triple prime, this fission neutron rate is equal to Q. And in the

## 04:20

book, there's an expression for our one over E flux that has the proper normalization. It was

## 04:26

Q over C times E times sigma S, right? There was always this, the Q over C, the slowing down

## 04:34

decrement, and then this scattering cross-section. So it's in there. I don't know which equation it

## 04:41

is. Actually, you have the book here? Yeah, there you go. All right. So in the book, it's,

## 04:52

oh, we're staring at it again.

## 04:54

What's the equation?

## 04:56

I'm not sure.

## 04:57

So this would be like equation 3.26, right? It's Q over the slowing down decrement times sigma

## 05:11

S would be times E, right? If we assume that sigma S is constant, which it is fairly constant

## 05:18

through that resonance region, then that's just another constant, right? So to a pretty good

## 05:23

approximation in that slowing down regime, the flux is just one over E, right? And all they're

## 05:28

doing in that equation,

## 05:30

is adding in the number of neutrons with the slowing down decrement, right? It's an approximation.

## 05:35

And so 3.26 is what gives you that. And so that's like the fact that you have what Ci is given the

## 05:45

number of neutrons. Well, if you look at the fast flux I've given you here, in the book, it's chi

## 05:52

over sigma T times S sub F triple prime, like the number of neutrons being born from fission. I
don't

## 05:59

have that here.

## 06:00

That means that my fission rate is one, okay? So that means Q, my slowing down density,

## 06:06

the number of neutrons passing by 0.1 MeV, is also one. That means then that Ci should

## 06:12

be equal to one over that slowing down decrement times whatever the scattering cross-section

## 06:18

is at that energy. Yeah?

## 06:20

For microsecond work, it came to the problem statement, but…

## 06:27

Okay, so go ahead.

## 06:29

In the problem statement, you have… How would you use that?

## 06:32

How would you use the system to save 50% or 50-50 mixture of UO2 and H2O, and that's not given in
the

## 06:42

problem statement on the actual homework page?

## 06:45

Oh, I think I was… Yeah, so in the homework, I said to use the, what, the 100 to 1 ratio, right?

## 06:53

So this is… I think when I wrote it, I was originally thinking this because that's what I…

## 06:58

That 50-50 mixture is what I have in the homework problems for this week.

## 07:02

So I was, like, piecing together things that I was expecting.

## 07:06

So the 50-50, don't worry about that. This was me sketching out a solution.

## 07:11

The process is the same for both of them.

## 07:13

In fact, what I gave you for the material composition makes this a little easier,

## 07:16

because then there's less going on to compute the cross-sections, right?

## 07:19

You only have to use what you had already done.

## 07:21

Also, K is not given in the problem statement on the work item.

## 07:26

K. That's just… That's the Boltzmann concept. Yeah, so that's in the…

## 07:29

Well, it's… In the problem statement, it's weird that you…

## 07:33

It says where C i and C t are constants, and then in brackets, it says e v for k, and then t equals
k, 300 k.

## 07:41

Like, that's supposed to be in the statement, but it's not there.

## 07:44

I think that's… I think that's a Canvas issue with my math.

## 07:49

So I write… I use Markdown.

## 07:51

It's, like, the same thing that is in the Jupyter Notebook.

## 07:53

So you see me do some math equations, and I export that to HTML, and sometimes that gets messed up.

## 07:58

So if you could…

## 07:59

I'll take a look and see.

## 08:03

In fact, maybe…

## 08:07

Where is…

## 08:10

I… Yeah, I got the Boltzmann concept, but it's just…

## 08:13

It's, like, in the actual problem statement, it's missing it if it was supposed to actually be in
there a bit.

## 08:22

Let's see assignments.

## 08:31

So assignment three.

## 08:39

Week four.

## 08:41

Oh, come on now.

## 08:58

Oh, yeah.

## 09:01

Yeah, so that's…

## 09:02

Somehow it dropped the k equal, because that must have been in math.

## 09:08

So I will go ahead and fix this now.

## 09:16

Does it actually have it there?

## 09:17

Yeah, see?

## 09:21

Canvas for the win.

## 09:24

k is equal to 8…

## 09:27

What is it?

## 09:27

8.7.

## 09:28

617e minus 5.

## 09:35

I'll just leave that.

## 09:36

I don't like that notation, but at least it'll be there.

## 09:40

Yeah, if you find anything like that in any of the documents, let me know.

## 09:45

I spent quite a bit of time kind of automating that process, but I think something has changed from
when I first did it.

## 09:51

And so it's not as reliable as it once was.

## 09:53

I try to catch them when I…

## 09:55

I look at it and iterate, but, you know, I've obviously missed some things.

## 09:59

Okay.

## 10:00

So, yeah, that's what I'm looking for for the homework.

## 10:06

And the major thing I want to point out is that after you do that…

## 10:11

So I think I've done it here for the more complicated mixture, but the process will be the same.

## 10:16

The key thing is you might end up with something that looks like that as your pieces.

## 10:22

So if I am…

## 10:23

I have the Maxwellian at that low temperature.

## 10:26

I'm diving down well before the…

## 10:28

Well before the 1EV, right?

## 10:30

And so I've said before that we can increase the temperature to make it absorption.

## 10:34

But there's…

## 10:35

Physically, there's nothing that splits this Maxwellian spectrum or the thing that looks like the
Maxwellian spectrum from the 1 over E.

## 10:42

There's not a hard deadline.

## 10:43

Like, neutrons don't get to some door and knock.

## 10:45

It's like, hey, can I enter the Maxwellian zone now?

## 10:48

It's not as simple as that, right?

## 10:50

It's a nice way to look at the physics.

## 10:53

We know that there's some energy below which upscattering is really not affecting the spectrum.

## 10:58

Right?

## 10:59

It's on the order of an EV.

## 11:00

It's a little less than that.

## 11:01

Right?

## 11:02

But it's a soft cutoff.

## 11:03

It's not a hard cutoff.

## 11:04

So we will have neutrons that continue to fly down to the lower energies from 1 over E type elastic
scattering stuff.

## 11:11

So there will be a softer connection.

## 11:13

And you can sort of visualize that.

## 11:15

It's like, huh, I kind of suspect the spectrum should look like a smooth function.

## 11:18

So I bet there's some nice mixing that would let me make that smoother, which is kind of what I did
in class the other day.

## 11:24

Okay?

## 11:25

So just use it as is.

## 11:27

Right?

## 11:28

Or plot it as is.

## 11:29

And then for the fission, when you do that normalization for C sub I, I end up with something that
looks like this.

## 11:36

Right?

## 11:37

Where the chi spectrum shape is quite a bit lower than it would be if it were 1 over E all the way.

## 11:42

And I thought more about that.

## 11:44

And it dawned on me that there's still scattering at those high energies.

## 11:50

We're just, again, breaking it up as kind of a nice way to understand what the driving force is.

## 11:56

But if you think about it.

## 11:57

If I'm a neutron being born from that chi spectrum at 10 MeV or 1 MeV, I'm still driving a 1 over E
type slowing down process.

## 12:06

Right?

## 12:07

And so what you can actually do is view all of the energies of the chi spectrum.

## 12:11

Break it up into a bunch of delta functions.

## 12:13

You know, the direct delta, the impulse function.

## 12:18

Does that ring a bell from other classes?

## 12:20

Right?

## 12:21

So you can imagine that each one of those energies in the chi spectrum is driving a 1 over E.

## 12:26

So you could actually take that and add a 1 over E flux starting from each energy of the chi
spectrum on top of each other.

## 12:33

And that means that you'll have more at the peak.

## 12:36

And what you'll end up with is a spectrum that kind of rounds out and then falls off like that,
which is quite a bit closer to reality.

## 12:43

And we'll see at least something that looks a lot like reality when I show you some OpenMC stuff.

## 12:49

So bottom line, if you end up with something that looks a little grotesque, as I think of this,
you're fine.

## 12:54

That's a limitation of the approximations that we're trying to use from the book.

## 13:01

Okay?

## 13:02

There are better ways to do it in practice, but they take us away from sort of a good understanding
of the individual physics.

## 13:08

And then we're into the cranking the black box machine and getting something out.

## 13:12

Right?

## 13:13

We know we have to know this sort of stuff to interpret what the machine is giving us.

## 13:17

Right?

## 13:18

The program, the software, the Monte Carlo, whatever.

## 13:21

But the Monte Carlo solution will smooth that out.

## 13:23

Right?

## 13:24

It will smooth over these things and give us something that's more realistic.

## 13:27

Right?

## 13:28

And we'll see examples of that.

## 13:29

So hopefully this clears up a little bit about what we're doing with that problem.

## 13:35

Okay?

## 13:36

Sorry for the math notation getting a little wonky.

## 13:39

Right?

## 13:40

But at the end of the day, it's still you're stating some assumptions.

## 13:44

You're making some assumptions.

## 13:45

You're filling gaps.

## 13:46

So if I haven't told you which material to do, you have to pick a material.

## 13:50

Is that asking too much of you?

## 13:51

Yeah.

## 13:52

You're probably then like, what is he asking?

## 13:53

What is he asking for?

## 13:54

Right?

## 13:55

Which reminds me of kind of my own thought process as I was doing it.

## 14:00

It's like, well, shit, this is kind of a stupid problem statement as written, which is why

## 14:04

I filled it in.

## 14:05

But then I'm thinking, you know, as an engineer, sometimes you're given somewhat uncomfortable

## 14:10

problem statements, like where you feel like, oh my goodness, like what do I need to do?

## 14:15

So sometimes you should just like be a little brave.

## 14:19

Yeah.

## 14:20

Yeah.

## 14:21

And then you can just go back and make some assumptions.

## 14:23

Right?

## 14:24

See if you can get forward on something.

## 14:27

If you make a clever assumption, cool.

## 14:29

If you make a stupid assumption, and by stupid, I mean something that you can go back later

## 14:33

and say, that's actually not physical or something like that, then you can go back and correct.

## 14:38

But don't be afraid to make assumptions.

## 14:40

That's actually one of the most important things that you can do as an engineer.

## 14:44

I would say it's just a technical thinker as well.

## 14:47

Right?

## 14:48

I relish in problems like the so-called Fermi problem.

## 14:50

Like how many piano tuners are there in the city of Chicago?

## 14:55

I mean, why the hell would anybody care?

## 14:57

But it's an interesting problem.

## 14:59

Right?

## 15:00

Because you can actually then start to make some observations about your own life and

## 15:04

kind of extrapolate and come up with probably a pretty reasonable answer.

## 15:07

Right?

## 15:08

So it's similar.

## 15:09

Just get comfortable with making assumptions and then fleshing out a solution based on

## 15:15

those assumptions.

## 15:16

Okay?

## 15:17

That's not what I want for most of our homeworks to be.

## 15:19

I'm not opposed to it happening sometimes.

## 15:21

Right?

## 15:22

To exercise that part of your thinking machinery.

## 15:27

Okay?

## 15:28

So, yeah.

## 15:29

That's anyway.

## 15:30

My final thought is that looks terrible.

## 15:33

And if I go ahead and I do this other thing where I use this thing where basically I'm

## 15:39

convolving it.

## 15:40

Right?

## 15:41

So I have the narrow resonance spectrum.

## 15:43

Right?

## 15:44

So I could do it one over eight.

## 15:45

But I'm choosing to use the narrow resonance.

## 15:47

I'm going through.

## 15:48

I'm going through and just adding it over and over again.

## 15:50

So eventually I'll put this notebook, you know, after you've turned everything in.

## 15:55

But this is a more reasonable spectrum.

## 15:58

Right?

## 15:59

If I didn't use one over eight, this stuff would go away.

## 16:01

But I still have this kind of nice smooth thing.

## 16:03

But what it doesn't have is this like a bump.

## 16:06

It doesn't have like an elevated flux in that fast region that takes, you know, the shape

## 16:14

of the chi spectrum.

## 16:16

And the reason for that, at least part of the reason for that, will become a little

## 16:20

clearer by the time we look at some of the OpenMC examples.

## 16:23

And we put into this whole thing the concept of multiplication and multiplication factor.

## 16:29

Yeah.

## 16:30

So I'll go ahead and close that out.

## 16:34

I'll get rid of some of my other stuff.

## 16:38

Okay.

## 16:39

I don't have anything more there.

## 16:42

All right.

## 16:44

So what we had talked about last time was the multi-group approximation where we take

## 16:49

the energy domain and we break it up into little intervals.

## 16:52

Right?

## 16:53

Each of those intervals is called a group.

## 16:55

And in order to do balance across those groups, we need effective cross sections over those

## 17:00

groups.

## 17:01

Right?

## 17:02

And so as an example, right, if we have the energy domain here, okay, we break it up into

## 17:11

individual things.

## 17:12

And for group G.

## 17:13

We have some bound that is G plus 1 and EG.

## 17:20

Okay.

## 17:21

So on and so forth.

## 17:23

And then for some reaction X, the G-th effective cross section would be the integral from EG

## 17:32

to EG plus 1 DE sigma X G E TE.

## 17:42

All over phi sub G, where phi sub G is the total or integrated flux over that same energy

## 17:55

domain.

## 17:56

Okay.

## 18:00

And there's a slightly more complicated form for the scattering cross section.

## 18:04

You can go back to the notes for that, but it's similar.

## 18:08

It just has two integrals.

## 18:11

Okay.

## 18:12

So once we've broken down the continuous energy domain into the energy domain, we're going

## 18:16

to go from the continuous energy domain into these groups.

## 18:20

We go from a continuous slowing down or spectrum equation to one that forms some sort of linear

## 18:27

system.

## 18:28

Okay.

## 18:29

Right now, we don't know what kind of system that is.

## 18:31

In fact, there are two kinds that we'll be able to use.

## 18:34

Right.

## 18:35

But let's take a little bit of extra time and finish what we started with.

## 18:40

Or if we'll start with what we finished with last time.

## 18:47

If you remember, once we do the two group approximation, where we make that split of

## 18:52

energies at the same one EV boundary, we end up with a balance equation that looks like

## 18:57

this, right?

## 18:58

We have the interactions on the left-hand side.

## 19:01

This is sigma R1.

## 19:03

That's the removal cross section.

## 19:05

So that's the total cross section minus the self-scatter.

## 19:08

Remember, when we go to this group-wise representation, we can have neutrons that start in one group

## 19:15

and end in the same group.

## 19:16

They might still be effectively losing energy, but because there are multiple energies in

## 19:23

a given energy group, they can stay within the same group.

## 19:26

Okay.

## 19:27

So this is what we had last time.

## 19:29

And what I claimed is this is probably not going to be solvable.

## 19:32

Right?

## 19:33

We can make some progress.

## 19:34

So let's go ahead and see if we can find phi 1 and phi 2.

## 19:38

I'll start off with phi 2.

## 19:41

So from equation 2, phi 2 has to be equal to phi 1 times the self-scatter.

## 19:45

So phi 1 times the scattering from group 1 to 2 divided by the absorption cross section

## 19:50

in group 2.

## 19:51

So that's pretty straightforward.

## 19:52

That's going to scale with phi 1 and sigma S2 from 1 over sigma A2.

## 20:00

Okay.

## 20:01

Boom.

## 20:02

We call that equation 3.

## 20:04

Now, if I want to get phi 1, I can take this phi 2 expression, plug it into equation 1,

## 20:12

and then see if I can get phi 1 out of it.

## 20:14

Right?

## 20:15

So if I do that, I take this thing and I substitute it into equation 1.

## 20:21

Okay.

## 20:22

That leaves me with sigma R1 phi 1 is equal to nu sigma F1 phi 1 plus nu sigma F2 and then

## 20:37

phi 1 sigma S2 1 sigma A2.

## 20:43

Okay.

## 20:44

Now, what's the problem with this?

## 20:47

If I want to get the second unknown flux, am I able to do that?

## 20:52

Right?

## 20:57

Because on both sides, I have things that are multiplying phi 1.

## 21:00

Right?

## 21:01

So I'll use red, and I can cancel them out.

## 21:04

Well, that's interesting.

## 21:07

Does that mean phi 1 is 0?

## 21:09

Does it mean that it's impossible to find?

## 21:12

I would argue maybe either of them.

## 21:15

What this...

## 21:17

That we've eliminated phi 1.

## 21:18

That we've eliminated phi 2.

## 21:20

And phi 1 cancels out.

## 21:22

The only way that this equation...

## 21:24

There are two options.

## 21:25

If phi 1 is 0, then this equation is satisfied.

## 21:29

Would you agree?

## 21:30

But if phi 1 is 0, what is phi 2?

## 21:35

That's the 0 solution.

## 21:37

In math, 0s are never interesting.

## 21:40

Right?

## 21:41

Because if we have 0 flux and we have 0 fissions, we don't have a reactor, we can go home early.

## 21:46

Actually, in fact, that's...

## 21:47

No.

## 21:48

So that's not what we want.

## 21:49

So we want phi 1 to be non-zero, which requires then that sigma r1 is exactly balanced by the rest
of the stuff on the right-hand side.

## 21:59

And we know that these cross-sections come from the back of the book.

## 22:03

They come from NNDC.

## 22:05

They come from this cross-section homogenization or condensation.

## 22:09

Somehow, they're just numbers.

## 22:12

So even though they are correlated, the physics is driving their definition.

## 22:18

I can't say in general that that will be satisfied.

## 22:22

So in general, this thing can't be solved.

## 22:25

What we can do, though, is modify it a little bit.

## 22:28

What I'm going to do is introduce a fudge factor, a tuning parameter, an extra degree of freedom
that might get us moving along.

## 22:36

And that is going to look like the following.

## 22:42

I'm going to take this whole right-hand side.

## 22:44

And I'm going to divide it by a number.

## 22:46

I'm just going to call it k.

## 22:53

And maybe you'll get a sense of where we're going with this.

## 22:57

So I'm going to go ahead and do that.

## 22:59

Now, the right-hand side, all these numbers would add up to be something.

## 23:04

The left hand will be something else.

## 23:06

I can certainly pick some number, k, so that the left-hand side is equal to the right-hand side.

## 23:10

Would you agree with that?

## 23:12

Now, it's not obvious where this is going to or how this is going to help us.

## 23:15

But if I do that, let me then define what k is, right?

## 23:22

That's fairly straightforward.

## 23:24

I just kind of move things around.

## 23:26

So what this would mean is that k is equal to nu sigma f1 plus nu sigma f2 times scattering from 1
to 2 over sigma a2.

## 23:44

Okay.

## 23:46

Scroll up just a little bit.

## 23:48

Okay.

## 23:49

All that stuff divided by sigma r1.

## 23:58

Not super heavy math.

## 23:59

I'm just switching sigma r1 with k.

## 24:04

Now, the question is, is this k similar to, equal to, different from any other k that we've dealt
with, right?

## 24:18

Can we identify?

## 24:19

Can we identify?

## 24:20

From this stuff right here, right, which I guess I'll call that equation 4, right?

## 24:27

Is equation 4 consistent with this idea of k infinity being gains to losses?

## 24:33

Who thinks yes?

## 24:36

Can you see gains to losses?

## 24:39

Who thinks no?

## 24:43

All right.

## 24:44

Brave.

## 24:45

Who thinks we should have just stuck with phi equals 0 and gone home?

## 24:50

All right.

## 24:51

Fair enough.

## 24:52

Okay.

## 24:53

So.

## 24:54

Why don't you divide it by k on both sides so it's still the same?

## 25:01

So if I divide it by k on both sides, then I'm stuck with the same left-hand side not equaling the
right-hand side in general, right?

## 25:09

So if I do that, if I scale both sides, I'm not adding a degree of freedom.

## 25:14

So you're right.

## 25:15

I'm taking what might have been a balance and I'm breaking it.

## 25:18

Like, I'm breaking the math, right?

## 25:20

But I'm doing it in a way that.

## 25:21

I'm doing it in a way that will recover something that we've actually seen before.

## 25:25

Okay.

## 25:26

So the challenge is when we wrote down the two group equations the way we did, we were making an
assumption, right?

## 25:33

The only way that they work out is if all those numbers exactly balance.

## 25:38

And if they exactly balance, then we don't need a fudge factor, right?

## 25:42

Or our fudge factor in this case, k, would be equal to 1.

## 25:46

And we all know what k equal 1 is.

## 25:49

Steady states.

## 25:50

Gains exactly balanced by losses and so forth.

## 25:54

So the only way that that balance equation is balance is if gains precisely are balanced by losses,
which is exactly what k equal 1 is.

## 26:02

So what we have to what we're doing now is, how do we quantify the case where the cross sections,
the reaction rates aren't balanced?

## 26:11

And that the degree of imbalance is exactly what we use k to measure.

## 26:16

Right?

## 26:17

And so.

## 26:18

Does this.

## 26:19

Tell us about gains to losses?

## 26:21

Well, yes, I claim.

## 26:23

Yes.

## 26:24

So what we're going to do is take this equation for, and we're going to multiply the top and bottom
by fee 1.

## 26:28

So i'm going to do a bunch of things that aren't changing anything at this point.

## 26:31

I'm going to leave k there, but i'm going to start changing things so that it looks a little bit
different.

## 26:36

So we're going to start with 4, and we're going to multiply by fee 1 on the top and bottom.

## 26:47

Okay.

## 26:48

So what we end up with is k is equal to fee 1 times new Sigma F.

## 26:57

1 plus fee 1 times new Sigma F.

## 27:02

2 times Sigma S.

## 27:04

2, 1 Sigma A.

## 27:06

2 and fee 1 times Sigma R.

## 27:12

1.

## 27:13

Now fee 1 times Sigma S.

## 27:16

2 1 over Sigma A.

## 27:18

2.

## 27:19

Well, that was our equation up here for feet, too, right?

## 27:23

So fee 1 times this ratio of the scattering cross-section to that absorption cross-section.

## 27:28

That is fee 2, right?

## 27:30

So I can take this and multiple cancel that, and instead say that that's feet, too.

## 27:36

All right. Now, can somebody remind me what the removal cross-section is?

## 27:43

This thing right here.

## 27:52

So the English description is it's the cross-section that represents removing neutrons from a group.

## 27:56

Not necessarily absorption, just taking them away.

## 27:59

So there are two things that remove neutrons from a group absorption and scattering to other groups,
right?

## 28:05

So for our case where we are two group case, this thing is equal to Sigma A.

## 28:12

1 plus Sigma S.

## 28:16

From 1 to 2, right?

## 28:18

Because if I'm scattering to group 2, I'm being removed from group 1.

## 28:21

All right, cool.

## 28:23

Now.

## 28:24

So let me.

## 28:25

I'll write it.

## 28:27

Everything again to kind of clean things up, and I'll reorder things to make it look a little bit
more similar to what we've seen before.

## 28:34

Right?

## 28:35

So I've got my fission cross-section with new times fee 1, right?

## 28:39

I've gotten rid of my fee 1 and this ratio here.

## 28:43

So I'm down to fee Sigma F.

## 28:46

Sorry, new Sigma F.

## 28:47

2 times fee 2.

## 28:49

Okay.

## 28:52

Then on the bottom I've got Sigma A.

## 28:55

1 times fee 1.

## 28:57

Plus Sigma S.

## 28:59

2.

## 29:00

1 times fee 1.

## 29:02

Okay.

## 29:03

Now, if I go back to my two group equations, the second equation relates fee 2 to fee 1.

## 29:13

So fee 1 times the scattering cross-section from group 1 to 2 is exactly equal to fee 2 times its
absorption cross-section.

## 29:23

Right?

## 29:24

So I have this thing in my current.

## 29:25

In the equation I'm writing.

## 29:27

This is in my denominator.

## 29:28

I can switch it with this.

## 29:31

Right?

## 29:33

So I can take this and write it as a 2 fee 2.

## 29:39

Right?

## 29:40

Which means that I have K is equal to new Sigma F.

## 29:46

1 fee 1 plus new Sigma F.

## 29:50

2 fee 2.

## 29:52

Divided by.

## 29:56

Sigma A.

## 29:57

1 fee 1 plus Sigma A.

## 30:00

2 fee 2.

## 30:08

Interesting.

## 30:09

Right?

## 30:10

Because what is that?

## 30:19

It's a ratio of 2 quantities.

## 30:21

What's the top quantity?

## 30:23

What's my numerator?

## 30:25

What's that?

## 30:26

Yeah, it's gain.

## 30:27

So losses.

## 30:28

I have new Sigma F.

## 30:29

For group.

## 30:30

Each group times the respective cross-section.

## 30:32

Right?

## 30:33

So this is the rate at which neutrons are being born from vision due to neutrons in groups.

## 30:38

1.

## 30:39

This is the rate at which neutrons are being produced from vision due to neutron in room 2.

## 30:45

Right?

## 30:46

Add them together.

## 30:47

That is the total rate at which neutrons are emerging from vision.

## 30:50

Right?

## 30:51

Per centimeter.

## 30:52

Cubed per second.

## 30:53

That's my production rate.

## 30:55

That's my gains on the bottom.

## 30:57

I have Sigma A times fee 1.

## 31:00

That's the rate at which neutrons are being absorbed in group.

## 31:04

1.

## 31:05

Likewise.

## 31:06

The rate at which neutrons are being absorbed in group.

## 31:07

2.

## 31:08

You add them up.

## 31:09

That's the total rate at which absorptions are happening.

## 31:11

Per centimeter cubed.

## 31:13

That's my losses.

## 31:14

Gains to losses.

## 31:15

So what we did by adding that fudge factor is account for the imbalance in gains to losses.

## 31:21

Right?

## 31:22

So it's a not it's a it's moot if everything were in balance.

## 31:27

Right?

## 31:28

If this is if K is equal to 1, it's as though we didn't put a fudge factor in.

## 31:32

All we're doing now is saying that we can measure the deviation.

## 31:36

The deviation from balance.

## 31:39

We can say that a system has non-unity multiplication.

## 31:46

Right?

## 31:47

So if I were just to take a pile of nuclear materials, put it together, and then model it right, I
can guarantee that the probability that it comes together as being perfectly critical is 0.

## 32:01

Right?

## 32:02

But if I want to understand how close to critical I am and model it.

## 32:05

I'm going to have to find a way to measure or compute K.

## 32:09

And that's what this is right that's the multiplication factor gains to losses.

## 32:14

So this cave is fudge factor that we put in is our K.

## 32:20

Infinity.

## 32:21

So now that we know that this fudge factor is our multiplication factor, we can go back to those
original equations and introduce it.

## 32:35

You'll notice that where I I put it.

## 32:37

To fix our problem was underneath the right-hand side.

## 32:43

And if you look closely, I'm effectively scaling the fission generation rate.

## 32:49

Right?

## 32:50

The the number of neutrons produced from fission by putting K.

## 32:53

Where I've done it's as though I I took new bars or the Sigma.

## 32:58

But for each group or or the combination and scaled them by K.

## 33:03

If K is greater than 1, I'm reducing them.

## 33:05

K is less than 1.

## 33:06

I'm increasing them.

## 33:08

Makes some sense, right?

## 33:09

If I have too little fission, I should increase him.

## 33:12

One way to do that is divide by a number that's less than 1, and vice versa.

## 33:16

Right? So K is impacting my vision rate.

## 33:25

So back to the 2 group equations.

## 33:27

I have Sigma R.

## 33:29

1 P. 1 is equal to 1 over K.

## 33:33

I'll put the infinity here times.

## 33:36

My new Sigma F.

## 33:38

1.

## 33:39

P. 1 plus new Sigma F.

## 33:43

2 P. 2.

## 33:45

And then I have Sigma A. 2 P. 2 is equal to the scattering from 1 to 2.

## 33:57

Okay, and I can take this and write it in matrix form, right?

## 34:04

So I have a matrix.

## 34:06

That would be Sigma R. 1.

## 34:08

I have minus Sigma S. 2.

## 34:13

1.

## 34:14

I have 0 here, and I have Sigma A. 2 here.

## 34:21

P. 1 P. 2.

## 34:24

This is equal to 1 over K.

## 34:28

Infinity times.

## 34:33

New Sigma F. 1.

## 34:43

Sigma F. 2.

## 34:45

P. 1.

## 34:49

P. 2.

## 34:50

It's not obvious here, but remember that this is actually our multi-group chi vector.

## 34:56

It's 1 for fast neutrons.

## 34:58

It's 0 for thermal neutrons.

## 35:00

It would look a little different if we had more energy groups, right?

## 35:03

But if I want it in this matrix form, I've got to write this sort of silly vector of 1 and 0.

## 35:09

Okay?

## 35:11

Remember that the the removal cross section is the total cross section.

## 35:13

Minus the self scatter.

## 35:16

So I could actually write this as my total cross section minus the

## 35:27

See 1, and so this would be 1 1.

## 35:30

This is S. 2.

## 35:32

1.

## 35:34

Before we had said that the scattering cross section from group 2 to 1 is 0.

## 35:39

I'll write it back again.

## 35:41

Just to be sort of clear about it.

## 35:46

And then this is 2 minus Sigma S. 2.

## 35:51

2.

## 35:54

P. 1.

## 35:55

P. 2.

## 35:57

Equal 1 over K.

## 35:59

Infinity.

## 36:01

In fact, all that stuff is equal.

## 36:04

If this is my chi vector.

## 36:08

And this call this my new.

## 36:12

Actually, i'll just call this f transpose right that's a vector.

## 36:19

What I can do is write this whole thing is a matrix system, and by doing that we'll have a common
format that we can use for 2 groups for 3 groups for 100 groups, whatever, and that'll help make
what we do with a little bit of

## 36:32

jupiter notebook stuff a little bit more obvious.

## 36:35

So I can put all the total cross sections into a matrix T.

## 36:38

It'll be a diagonal with just the Sigma T. part.

## 36:41

Right that this thing here, this thing here.

## 36:45

Okay, and then I can subtract the scattering matrix.

## 36:49

That's all these elements right Sigma S. 1 1 Sigma S. 2 from 1.

## 36:54

Okay, and then I have my fee vector.

## 36:59

This will be equal to 1 over my multiplication factor times.

## 37:06

This chi vector times.

## 37:09

This new Sigma F.

## 37:10

Vector with its transpose times fee.

## 37:16

Okay, and to make things even a little bit cleaner looking i'll take this outer product.

## 37:23

Remember this vector. I have a column vector multiplied by a row vector in this case.

## 37:27

Right. So 2 by 1 times 1 by 2. Well, you work out the dimensions.

## 37:31

It should be 2 by 2. Okay, so i'll call this whole thing.

## 37:35

The matrix F. right.

## 37:38

So what I end up with is T minus S.

## 37:44

Fee is equal to 1 over K.

## 37:47

Infinity times F times fee.

## 37:52

Okay, and I can do one last thing to get this into a form that maybe will look familiar to you from
your course.

## 38:02

5, 5, 5, 5, 1 matrix analysis.

## 38:05

Okay.

## 38:06

I know it probably gives you the heebie jeebies.

## 38:08

Please have faith that matrices are are your friend in this in this case.

## 38:15

Okay. So what I can do here is switch things around.

## 38:20

I'm what I want to do is get K infinity to the left hand side.

## 38:24

So i'm gonna have K infinity times fee.

## 38:28

Okay, but I want that so i've got to get T minus S.

## 38:34

To the other side.

## 38:36

I can't divide by a matrix.

## 38:39

What's the equivalent of divide by for matrices?

## 38:46

Yeah, the inverse of a matrix, right?

## 38:48

So I multiply both sides of this expression by the the inverse of this thing, right?

## 38:54

And what I end up with then is T minus S.

## 39:01

Spoot this over a little bit.

## 39:04

Okay.

## 39:05

To the minus 1.

## 39:06

It's inverse times F.

## 39:09

Right?

## 39:12

If I want, I could call this whole thing the matrix A.

## 39:17

If I want, I could call this K infinity lambda.

## 39:22

And if it makes you feel better, I could call fee X.

## 39:27

And if I do all that, then what i'm dealing with is a problem that looks like this.

## 39:33

Anybody solve a problem like this before?

## 39:40

Seen a problem like this before?

## 39:42

It's what we call an eigenvalue problem.

## 39:52

So what it means is that in at least in this multi-group approximation, our friend, the
multiplication factor is nothing more than an eigenvalue.

## 40:07

When we turn those balance equations into this form where we don't have a forcing function.

## 40:13

This is called a homogeneous problem where we have the solution on both sides and nothing that isn't
the solution.

## 40:19

Right?

## 40:20

An inhomogeneous problem would have some forcing function.

## 40:23

Right?

## 40:24

A source of neutrons that is just injected into the system.

## 40:27

Okay?

## 40:28

So for eigenvalue problems, so in 551, who did not have 551?

## 40:34

You did not have 551.

## 40:36

All right.

## 40:37

So not an issue.

## 40:38

Right?

## 40:39

Because I'm not asking you to do anything by hand.

## 40:41

In fact, I won't even ask you to do anything that would require that course.

## 40:48

That goes beyond what I'm giving you as an example.

## 40:52

But so for those of you at 551, did you cover a little bit on eigenvalue problems?

## 40:57

Right?

## 40:58

You probably did things like determinants and characteristic polynomials and finding the roots and
all sorts of, I don't know, it's not wasted time, but it seems a little.

## 41:10

Anyway, we won't do that.

## 41:12

We're going to go ahead and just dive into some numerical examples.

## 41:16

So that's basically what it is.

## 41:17

That's basically what I wanted to say about the two-group approximation.

## 41:21

But what we've done here with this sort of matrix representation, these matrices don't care if it's
two groups, three groups, 100 groups, whatever.

## 41:30

So we can use the same thing to analyze a system.

## 41:34

Right?

## 41:35

If we have the appropriate multi-group cross sections.

## 41:37

Right?

## 41:38

In theory, you know now how to take an approximate spectrum and compute all of these cross sections.

## 41:44

So in theory, you could go to the NNDC.

## 41:46

Use your crappy-looking spectrum from the next homework that we just talked about before or fix it
up a little bit.

## 41:53

Right?

## 41:54

And you could compute these cross sections.

## 41:56

You could put it into matrices like that.

## 41:58

And if you have the tooling from 551 to solve an eigenvalue problem, you could compute the
multiplication factor.

## 42:06

And if you go back to the very early part of the class, one of the things I said is a good part of
what we do in this class is figuring out how to estimate what that multiplication factor is.

## 42:15

Right?

## 42:16

This is step one in that process.

## 42:18

What are we missing?

## 42:19

Well, we're missing the fact that real reactors aren't infinite and homogeneous.

## 42:23

Okay?

## 42:24

But in this context of only energy, getting to this point of having this eigenvalue problem is a lot
easier than if we tried to build in all the spatial stuff.

## 42:34

Believe me, you can do it.

## 42:36

You can build in the spatial stuff, too.

## 42:38

It's just a little bit harder.

## 42:40

And we'll kind of pump that toward the later part of the course.

## 42:43

So at this stage.

## 42:44

Okay.

## 42:45

You've got some serious tools available to you.

## 42:50

You might not feel like that.

## 42:51

And you would certainly need to practice it to, you know, maybe build a reactor like Fermi did way
back when.

## 42:59

But it's not as large a leap as it might have seemed at the beginning of the course.

## 43:06

All right.

## 43:07

So let's go ahead and take a look at just a couple things.

## 43:14

So there's this tool called OpenMC that I've talked about.

## 43:18

I've given you a link to a GitHub repository.

## 43:21

It's just an online repository that has a bunch of Jupyter notebooks that I believe are in their
executed state so you can see what's going on.

## 43:28

I'm not going to try to go through everything, but I'll kind of piece together the sequence that
I've used.

## 43:35

There's one notebook that produces materials.

## 43:38

Right?

## 43:39

OpenMC takes a bunch of text files as input.

## 43:42

Right?

## 43:43

There's one for materials, one for geometry, one for some parameters and so forth.

## 43:47

The details aren't important.

## 43:49

Just know that here I'm producing some materials.

## 43:52

It's UO2 and water and a mix of that stuff.

## 43:55

Right?

## 43:56

And then I compute or produce this text file.

## 43:59

It's an XML.

## 44:00

Right?

## 44:01

Extended markup language.

## 44:02

All right.

## 44:03

So then I can actually use that in a slowing down problem.

## 44:09

Right?

## 44:10

So I'm loading materials.

## 44:11

I can define a geometry.

## 44:12

I can put a source in.

## 44:13

This is going to be a single point source at 10 MeV.

## 44:17

So all my neutrons are born at 10 MeV.

## 44:19

So similar to our slowing down problem.

## 44:21

It's just explicitly here you have to do that.

## 44:24

And I define some tallies, which if you're in McNeil's class, you probably know what a tally is by
name.

## 44:30

It's just a statistical estimate.

## 44:32

You're computing some mean value.

## 44:34

Right?

## 44:35

You're doing a simulation and coming up with an expectation value.

## 44:38

All right.

## 44:39

So I'm doing that.

## 44:40

There's a whole bunch of stuff that you see.

## 44:41

There's a bunch of stuff that you see from the output.

## 44:43

But then this is the output that I get.

## 44:47

And the black curve here is using the kind of underlying data with the narrow resonance spectrum.

## 44:54

Right?

## 44:55

So you've played around at least with the NR approximation a little bit.

## 44:59

This blue curve is what I get out of OpenMC.

## 45:02

Right?

## 45:03

So this is using Monte Carlo with the true underlying data, which includes the stuff happening at
thermal energies where I have thermal neutron up scattering.

## 45:10

From the thermal agitation.

## 45:12

But if you look in closely, the peaks and such that the black curves have line up with the blue one.

## 45:18

Right?

## 45:19

The blue one looks a little fuzzy.

## 45:21

And the reason for that is it's Monte Carlo.

## 45:23

It's stochastic.

## 45:24

I'm simulating, you know, several million neutrons.

## 45:28

And at each point in energy, I have an estimate.

## 45:31

Well, that estimate is really only like the true value to within some bar.

## 45:38

So you will have some natural variation.

## 45:40

And that variation is going to be quite a bit bigger than you get with the NR approximation.

## 45:45

Right?

## 45:46

But lo and behold, it looks pretty good.

## 45:48

One thing that you can see here is the blue curve tends to kind of like lean down as we go from
right to left.

## 45:56

That's due to the fact that neutrons are absorbed in the resonance region.

## 46:02

Right?

## 46:03

The whole point of the narrow resonance approximation is to account for all that resonance
absorption.

## 46:07

But the spectrum that we get out of the approximation, the NR flux, it doesn't have that absorption.

## 46:14

So remember we talked about the resonance escape probability?

## 46:17

That quantifies the number of neutrons lost.

## 46:20

But the spectrum itself doesn't.

## 46:22

So we see the narrow resonance looks a lot like 1 over E with the superimposed forest of resonance.

## 46:28

And the blue curve from the simulation looks kind of like 1 over E, but it leans a little bit.

## 46:34

It's not quite 1 over E.

## 46:35

Right?

## 46:36

So we've got a little bit of deviation at the high energies.

## 46:39

But that's, you know, so the narrow resonance approximation does a pretty good job for a good part
of that energy domain.

## 46:46

Okay?

## 46:47

The other thing that we can do with OpenMC is to produce cross sections.

## 46:52

So I can use that same infinite medium material with the geometry, with some slowing down.

## 46:57

Now I'm going to use an eigenvalue approach.

## 47:00

So I can solve it, and I can see what my eigenvalue is for this particular mix.

## 47:05

So I believe this 50-50 mix of UO2 and water is the same one that you would have seen me in my
solution sketch.

## 47:12

And it's possibly the same one that's in some homework now.

## 47:16

But it's just, you know, a homogeneous reactor.

## 47:19

And I've set it up here to give me a two-group approximation where I'm splitting it at 0.625 eV.

## 47:27

Right?

## 47:28

And it dumps out total cross sections or absorption cross sections or the scattering cross sections.

## 47:34

And any group structure that you want.

## 47:36

Right?

## 47:37

So that's kind of neat.

## 47:39

Hopefully I can get a system set up.

## 47:42

I looked at it again, and it's going to take a lot of my time to get things set up where you can
just log into a, you know, Jupyter notebook and be able to do it.

## 47:51

But in several cases, I can just give you the output.

## 47:54

So if we look at this folder, which I've linked to in Canvas, there are a number of files with the
extension .p.

## 48:03

Okay?

## 48:04

So that's for pickle.

## 48:06

So pickle is a Python module that lets you take just any sort of data structure and dump it onto
file.

## 48:12

So in my case, I'm using a Python dictionary.

## 48:15

Right?

## 48:16

Anybody familiar with a Python dictionary?

## 48:19

Right?

## 48:20

It's where you have a key that matches to some elements.

## 48:23

That's the way I'm transmitting that data.

## 48:26

And what's neat is I can take that data and load it.

## 48:31

Right?

## 48:32

So I'm going to use this three-and-a-half.

## 48:33

I'm going to use this 361-group cross-section file.

## 48:36

I'm going to load it.

## 48:38

And, you know, for instance, it has the chi spectrum.

## 48:44

Right?

## 48:45

So that looks like the chi spectrum to me.

## 48:47

I could also look at cross-sections.

## 48:49

So if I want to look at the total cross-section from this.

## 48:52

So I'm using the same sort of mixture of water and uranium.

## 48:55

Instead of doing two groups, I'm doing 300-something groups.

## 48:59

So if I look at the total cross-section, I see something like this.

## 49:02

The group edges, this colon minus one, that's reversing it.

## 49:05

Right?

## 49:06

Because remember, our group indexing goes in the wrong order.

## 49:09

And so to get it to plot nice, I have to do that.

## 49:13

This is the total cross-section of that mix.

## 49:15

It looks sort of sensible.

## 49:17

Like I've got some water and stuff, but I've also got those things with resonances.

## 49:21

Do you see all of the resonances that you're used to?

## 49:25

No.

## 49:26

Why?

## 49:27

Because I don't have 200,000 energy groups.

## 49:30

I only have 361.

## 49:31

So necessarily, I'm going to wash over some of those resonances and get kind of a smoother-looking
cross-section.

## 49:38

But the energy group structure that I'm using, 361, does have energy groups that capture some of the
lower but bigger resonances of things like U238.

## 49:51

So that first resonance at 6.67 eV, if you looked at that cross-section closely, that's the largest
cross-section or maybe second largest cross-section value.

## 50:00

And that's not a cross-section value in the entire spectrum of energies, right.

## 50:02

So that's a huge one, right.

## 50:04

Because if neutrons have lived most of their life getting down to 7 eV, capturing what that 6.67 eV
resonance does is super important to be able to accurately know how many neutrons get past it down
to the thermal energies that cause the fission that drive these

## 50:22

thermal spectrum reactors.

## 50:24

So in many of these group structures, they take great care to resolve the details at those lower
energies.

## 50:29

That's great.

## 50:30

okay and once we have all that cross-section data we can load it put it into the same matrices that

## 50:38

i just sketched out on the board and we can put it into numpy's eigenvalue solver and so we can

## 50:46

get the eigenvalues and the eigenvectors and it turns out in this case that the first eigenvalue

## 50:51

is k infinity in this case it's 1.3 which is very similar to what we saw from the openmc output if

## 50:58

you caught that so is it one no if we didn't have this k our system would be in balance right we

## 51:06

wouldn't be able to solve it so that fudge factor that lets us do it and if we plot it the spectrum

## 51:13

on this 361 group structure we see the spectrum and for the most part it looks a lot like what

## 51:19

we just saw with the slowing down or narrow resonance except now we also have the max volume

## 51:25

but we get this thing here

## 51:27

and

## 51:28

and

## 51:28

and

## 51:28

if you think about what's happening here depending on what k is the amount of the

## 51:36

chi spectrum that shows up will be greater or smaller if you have a system that is incredibly

## 51:40

subcritical meaning that k is less than one by putting k less than one below the fission term

## 51:49

you're going to increase the presence of that chi spectrum right so if you're just doing a

## 51:58

from the thermal region up back to the fast neutrons that that thermal induced fission

## 52:03

causes you're going to have a much lower fast flux than than you would expect right and so you've
got

## 52:10

to normalize it with k so this is sort of in a at least a part explanation for why our approximate

## 52:17

spectrum doesn't look good it's not a critical eigen spectrum it's not the spectrum that we

## 52:23

would get if we actually set up the balance equation what it does do is it gives us a pretty

## 52:28

good shape of the spectrum and it's not a critical eigen spectrum it's not the spectrum that we
would

## 52:28

over finite regions of energy right so if we were to use our fake spectrum and use it with a like

## 52:35

kind of a finely diced energy group structure it would probably not be so bad but it looks pretty

## 52:41

bad if we were to average it over the entire energy spectrum right which is what i'm having

## 52:45

you do for the homework associated with this week to compute k infinity right so just be aware of

## 52:52

that that you know significant limitation in the approximations if we want to do better we'd have

## 52:58

to resort to things like this right so if we were to do better we'd have to resort to things like

## 52:58

this which we have access to uh it's just by the time we get to this it's now we're playing with

## 53:04

the programming the the sort of the technical details and not so much the physics right so i

## 53:09

don't want to spend too much time on this if you guys are all interested in learning more about

## 53:13

this we can spend more time especially toward the end of the class right we can definitely

## 53:18

choose to spend more time on one thing or another i'm happy to uh do it but if there there is a

## 53:23

little bit of technical uh there's a learning curve right a learning curve in a like let's

## 53:28

let's say a technology curve that we'll have to climb in order to make that happen so any

## 53:34

questions sorry i've stolen a few minutes of your time um see we could have gone home

## 53:41

flux equals zero right anyway all right have yourselves a good weekend and we will uh be back

## 53:49

here on monday i'll try to get the page up for the lecture but start reading chapter four it's

## 53:54

pretty um at least the first section is pretty light-hearted it's kind of just a picture of what

## 54:00

some reactor systems actually look like we've dealt only with energy but as we try to bring

## 54:07

in some spatial stuff we've got to see what reactors actually look like right
