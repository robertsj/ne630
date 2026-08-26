# L18 Local Audio Transcript

Course: NE 630

Playlist source: https://youtube.com/playlist?list=PLy481lNHlnHoEO95vM-xYX2bydD25v20L

Video: NE 630 - Lesson 18

URL: https://www.youtube.com/watch?v=ifSflrLzm-w

Video ID: ifSflrLzm-w

YouTube upload date: 20231006

Duration: 46:41

Transcript source: Local faster-whisper transcription from YouTube audio.

Whisper model: large-v3; detected language: en.

Generated: 2026-06-28

Note: This transcript is machine-generated from audio and lightly wrapped only. It should be reviewed before being quoted, published, or used as polished lesson text.

Requested language: en

## 00:00

My bad. It's Friday.

## 00:06

All right. So get yourself fired up.

## 00:10

I'm doing it locally on my machine because despite my efforts, whatever the JupyterHub system that
they're using doesn't allow me to do the slideshow.

## 00:18

And I much prefer to have it blown up as slides.

## 00:22

So I believe we got through these first few slides last time.

## 00:27

And what you should have is the unit cells, utils imported.

## 00:36

Don't worry about this. This is for my own benefit.

## 00:38

You do need something that looks like this.

## 00:40

We should have all the permissions issues figured out.

## 00:45

It was, you know, as it goes sometimes with these tech issues, it was actually a compounding of
silly errors.

## 00:53

Some of them on my part, some of them just timing.

## 00:57

But we should be there.

## 00:59

We've got the SFR unit cell.

## 01:01

These are the inputs.

## 01:02

And then we wanted to produce the plots.

## 01:14

And I think this is where we got because if we couldn't, we couldn't run it because you didn't have,
this is where you got the issues with the cross sections, right?

## 01:24

So to run the simulation is whatever your object is.

## 01:29

In this case, it's SFR for sodium.

## 01:31

Cool.

## 01:32

Fast.

## 01:32

Reactor cell.

## 01:33

The function that we want to use is the run function.

## 01:37

Okay.

## 01:38

This has a couple of inputs that you can use the defaults for.

## 01:42

But if you want to resolve some of the uncertainties, as you'll see, OpenMC dumps out some
information when it runs.

## 01:48

And it tells you something like the uncertainty in the eigenvalue, K effective.

## 01:53

And if you want that to be smaller than the 0.001 or whatever it tends to be for these numbers, you
can increase it.

## 02:00

But if you're on.

## 02:02

The on-demand that you only have one core, I don't recommend changing it.

## 02:06

It'll take a little bit.

## 02:07

But there are only two OpenMC runs that we do here.

## 02:10

So even if they both take a few minutes each, most of the time will be spent looking at the results.

## 02:15

Okay.

## 02:15

So go ahead and run that simulation.

## 02:19

Right.

## 02:20

So your work here should be changed to SFR.run.

## 02:24

And you should see stuff that looks a little bit like this.

## 02:30

Yeah, I think we're on the attribute errors.

## 02:53

Yeah.

## 02:54

I couldn't find it.

## 02:56

That's the part I can't.

## 02:58

Let me just see what you did.

## 03:01

I didn't even know.

## 03:01

I didn't even know.

## 03:03

Thank you.

## 03:05

This is.

## 03:09

This one is.

## 03:10

I don't want to.

## 03:11

I don't want to.

## 03:13

I did a great work.

## 03:15

I didn't even see that on the list.

## 03:18

Um.

## 03:18

I didn't even know.

## 03:19

I didn't even know.

## 03:19

I didn't even know.

## 03:19

I didn't even know.

## 03:49

I didn't even know.

## 03:51

Oh, boy.

## 04:00

So the issue is.

## 04:09

I get the generic issue is OpenMC is an actively developed research code.

## 04:14

And so they've had some things change in their API, the function names and such that you can call.

## 04:20

I thought I'd.

## 04:21

I know this one.

## 04:23

And it's basically we have to go from.

## 04:25

Independent source to something slightly different.

## 04:29

Um, I thought I had fixed that.

## 04:50

Let me see if I have the same error when I run it.

## 05:14

Three, two, two.

## 05:17

Oh, I wish Zoom would just move its stuff out of my way.

## 05:22

Two times zero point four nine three five.

## 05:26

I said it did it as far unit cell unit.

## 05:29

So.

## 05:32

Oh, it did.

## 05:33

I see what happened there.

## 05:35

Yeah.

## 05:36

When you're on the system with its legs sometimes.

## 05:40

Um.

## 05:42

Yeah, yeah.

## 05:42

Yeah.

## 05:43

All right.

## 05:43

So we've got that.

## 05:44

We've got this.

## 05:51

Our.

## 05:53

One.

## 05:56

Okay.

## 05:56

So I've got that same thing open.

## 06:10

Let me see if this will work.

## 06:13

Um,

## 06:14

that means.

## 06:15

Oh, well, let's be.

## 06:16

Okay.

## 06:16

Hmm.

## 06:17

Hmm.

## 06:17

Hmm.

## 06:18

Hmm.

## 06:18

Hmm.

## 06:18

Hmm.

## 06:18

Save. Restart. Hopefully this will change and be what I need it to be. Okay. So what I did was,

## 07:02

so when you log into the session, you should see this file browser, right? When you first go into

## 07:08

on-demand, what you need to do is go down, find where that unit cell utils.py is. You click on

## 07:17

that. It'll open up a Jupyter-based text editor. What I need you to do is go down to the function

## 07:24

setup settings on line 141, and you'll change the source definition on 143

## 07:35

to be OpenMC.source. So the new version of OpenMC calls it independent source. And the reason for

## 07:41

that is to make it unambiguous, or probably to basically,

## 07:46

to make it unambiguous, or probably to make it unambiguous, or probably to make it unambiguous,

## 07:47

to make it more specific to what is being used. Yeah. So you'll have to restart the kernel.

## 08:01

That's one thing I don't like about Jupyter notebooks by default, is if you import a module

## 08:07

and you change the module on disk, like outside of the Jupyter notebook, it has that in memory.

## 08:15

You have to restart it for it to load it back in. It worked? Okay, good. Yeah, I thought I

## 08:29

had tested that out, but I think the issue was I had a different version of OpenMC installed before

## 08:35

I was resetting everything to test for folks, and then I never got to run through the whole

## 08:40

notebook on the on-demand. So while I have this up, I can say something a little bit about what

## 08:54

this setup is doing. Anytime that you run a k-eigenvalue simulation, where we're trying to

## 09:01

find the multiplication factor, remember what we're doing is trying to get an estimate of gains per

## 09:05

losses or not. So we're trying to find the multiplication factor. So we're trying to find the

## 09:06

number in one generation to number in a previous generation. The generation has to start from

## 09:12

somewhere. So if you remember the cartoon I had about describing the generations, we have one

## 09:19

neutron that goes in, causes other ones. You have to describe what that first neutron is. Here,

## 09:26

what I'm doing is saying that it's a point source in the middle of the pin cell, right? Yeah.

## 09:32

So when I made that change and I ran the plot again,

## 09:34

the plot can move up.

## 09:36

The plot broke?

## 09:39

Yeah, I actually ran a spart plot when doing the pre-prep with spart plot.

## 09:43

That's when I recently ran it all the same. And now it's telling me that spart plot.

## 09:48

This part works.

## 09:51

Let's see if I can get an error.

## 09:54

Yeah, make sure that...

## 10:02

Yeah, so the plot depends on the material being set.

## 10:07

So you've got to make sure that... Yeah, so the plot depends on the material being set. So you've
got to make sure that...

## 10:07

Yeah, so the plot depends on the material being set. So you've got to make sure that...

## 10:11

So anyway, yeah. So it's a point source in the middle of the pin cell.

## 10:16

It's isotropic in angle so they can go anywhere and in any direction.

## 10:21

And then the energy is being sampled from something called the watt spectrum.

## 10:24

This is one name that's assigned to the chi spectrum that we saw in the book.

## 10:29

There are several mathematical models for what that vision energy distribution looks like.

## 10:33

The watt spectrum is one of them. And I believe that's the one that we have in the book.

## 10:35

And I believe that's the one that we have in the book.

## 10:37

But that's sort of like almost like a historical detail.

## 10:55

All right.

## 10:55

So everybody should have something running.

## 11:12

I don't know if it's going to play over the bug in here.

## 11:20

It's going to play over the bug.

## 11:22

Yeah.

## 11:24

They did it, but I don't know.

## 11:29

Basically, if we keep running some of the same functions over and over,

## 11:33

it's going to write different tally files out

## 11:36

and it's going to be implementing the internal ID to them.

## 11:40

But as long as it's run, then we're good.

## 11:45

Alex?

## 11:46

For some reason, it won't take the change.

## 11:49

Like when I can't get a source and save it,

## 11:52

you're done with the phone.

## 11:53

I think it's uploaded, but just in case, I do that.

## 11:59

You can restart the kernel.

## 12:00

I did right here, and then you can just do that, right?

## 12:04

Restart and clear, or restart and run.

## 12:06

Oh, yeah.

## 12:08

Go ahead and do that.

## 12:09

Okay.

## 12:10

Yeah.

## 12:10

I'm going to do that.

## 12:11

I'm going to do that.

## 12:12

I'm going to do that.

## 12:14

Yeah, we're good.

## 12:15

We're good.

## 12:16

After it's doing something, scroll up,

## 12:18

and then I'll scroll up, and we'll have the same thing.

## 12:21

Which is still going to be in the source.

## 12:22

So it's like it's not getting a change when I save it.

## 12:25

All right.

## 12:26

But to that, I'm going to do it again.

## 12:28

So I know that one page, please.

## 12:30

So let's refresh this.

## 12:32

So this is on demand.

## 12:36

Thank you.

## 12:38

Yeah.

## 12:38

Also, I don't have any.

## 12:42

Oh, okay.

## 12:43

So that maybe goes out of this.

## 12:44

I'll continue to walk around with it.

## 13:04

That should do it now.

## 13:05

That's okay.

## 13:06

I already did some of the push-and-droping.

## 13:07

You can see.

## 13:08

Yeah.

## 13:08

Oh, I think that's the next issue.

## 13:09

Yes, I'm just having to turn it off and on.

## 13:11

I'm going to start it right again.

## 13:12

All right.

## 13:13

We're going to get a.

## 13:15

Let's see.

## 13:17

I'm going to go on that thing.

## 13:20

Fantastic.

## 13:21

So.

## 13:22

Yeah.

## 13:25

And now we'll try the.

## 13:31

Yeah, I don't know what.

## 13:32

I don't know what happened.

## 13:36

Are we getting it to run?

## 13:38

Yeah.

## 13:39

I was supposed to.

## 13:39

We go like that.

## 13:40

Yeah.

## 13:41

And here.

## 13:44

This was.

## 13:48

That's going to be.

## 14:00

We've got to put an s on it.

## 14:02

Oh, wait.

## 14:04

An uncommon.

## 14:08

OK.

## 14:09

Good.

## 14:11

More.

## 14:12

I don't save it as an independent source.

## 14:15

I don't have it there, so it's not good.

## 14:18

But that's why I didn't file save.

## 14:21

As soon as you change the thing in that file,

## 14:24

you can write the code you're finding.

## 14:27

And that's going to get it to go in there.

## 14:57

And that's a hard thing.

## 14:59

The import has a hard thing to do.

## 15:01

The RADI is .

## 15:04

And now, what happens to this piece now?

## 15:07

This needs to come down here.

## 15:09

Yeah, it's a little pokey.

## 15:13

All right.

## 15:15

I don't know if somebody would want to get the old one.

## 15:18

This is the one that's been loading.

## 15:20

Oh, yeah, no, that one's the best one.

## 15:22

But I always thought it was the best one.

## 15:24

That's right.

## 15:25

It's so weird.

## 15:26

My house is .

## 15:27

I don't want to fade out.

## 15:28

What am I saying?

## 15:29

What am I doing here?

## 15:30

I don't know.

## 15:31

I'll make a default check.

## 15:32

And you have more than that.

## 15:33

It's all my business.

## 15:34

I'll make a default copy for you.

## 15:35

You can say that.

## 15:36

I'm like, yeah.

## 15:37

That shouldn't stand out.

## 15:38

Oh, then it wouldn't work.

## 15:39

Yeah.

## 15:40

Yeah.

## 15:41

Well, it's .

## 15:42

.

## 15:43

.

## 15:44

.

## 15:45

.

## 15:46

.

## 15:47

.

## 15:48

.

## 15:49

.

## 15:50

.

## 15:51

.

## 15:52

.

## 15:53

.

## 15:54

.

## 15:55

.

## 15:56

.

## 15:57

.

## 15:58

.

## 15:59

Yeah.

## 16:00

That wasn't a good going.

## 16:01

If you keep going .

## 16:02

Don't stop yourself from moving along with it.

## 16:03

Okay.

## 16:04

I got it back toだから.

## 16:06

ay.

## 16:07

Yes, that's .

## 16:09

It's right.

## 16:10

It wouldn't log out .

## 16:11

No.

## 16:13

Hi.

## 16:14

Yes.

## 16:15

Oh.

## 16:16

.

## 16:17

Hey Dino, .

## 16:18

No.

## 16:19

Don't.

## 16:20

I just .

## 16:21

.

## 16:22

.

## 16:23

.

## 16:24

.

## 16:25

.

## 16:26

.

## 16:27

All right. So we've got the output. By default, if you run the problem, the only thing that you

## 16:41

ever see is the eigenvalue, right? Which can be useful. But it turns out that all the stuff that

## 16:47

we're computing lives in the state point dot 10 dot H5. H5 is the extension often used for HDF5.

## 16:54

It's just a file format for storing data. So what's done behind the scenes

## 17:01

is that state point is loaded. It has things like the spectra. It has things like the multi-group

## 17:13

cross-section. So by default, what these unit cell classes do is it produces a spectrum on

## 17:18

some sort of fine energy grid. And then it computes cross-sections on whatever your

## 17:22

course group boundaries are. The default for the SFR is just the one group, right? So from

## 17:28

1EV up to 2MEV or something like that, right? So you just get single cross-section values.

## 17:34

It's different for the PWR that we'll see in a moment. But the spectrum that we want

## 17:38

can be gotten by the plot spectrum, right? So if I... It's been a while since I've used these

## 17:46

notebooks. So plot SFR dot plot spectrum. Learn how to type, right? And so we get an image that

## 18:00

looks a little bit like the one that...

## 18:03

We've seen before, okay? And remember, our point in doing this SFR problem was to repeat this sort

## 18:10

of sanity check that we saw last time or last week, which was, is the spectrum actually spatially

## 18:16

independent? And this isn't like a mathematical proof or anything like that. In fact, you couldn't

## 18:22

do that because, sure, there will be a little bit of spatial variation. But in practice, if you zero

## 18:27

in on the spectrum, the shapes... What I mean by shape is the dependence on energy

## 18:33

of the spectrum. So if you zero in on the spectrum, the shapes are the same in all three

## 18:35

of the regions. So yes, we can say that in practice, we can sort of ignore those spatial

## 18:40

effects. The other thing that you can do with this plot spectrum based on this argument here

## 18:46

is to plot the flux per unit lethargy. And so if I change this to be true, we get a slightly

## 18:53

different looking spectrum. And actually, this is the one that looks more like the one in the book.

## 19:01

Because in the book, it's the plot spectrum. And so if I change this to be true, we get a slightly

## 19:03

different plot of E times phi of E, which is equivalent to the flux as a per unit lethargy.

## 19:10

So that's all I want to say about the SFR stuff. We can certainly go into... You can certainly use

## 19:19

it to compute some other things. But let's dive into the PWR stuff. So unlike the SFR, we can't

## 19:26

assume that the spatial dependence is negligible. That means that the shape of the flux spectrum,

## 19:32

phi is a function of E.

## 19:34

It's going to depend on which cell we're in. It won't be a huge shift, but it'll be a meaningful

## 19:42

one that'll definitely need to be accounted for if we want to get K infinity right. So

## 19:49

what we need for K infinity are the integral of the fission rate and then the integral of the

## 19:56

absorption rate. We can still break up the reaction rates into their separate regions.

## 20:02

So we take the integral over all the space that lives in the fuel and then in the moderator,

## 20:09

we pull out the volume, and then we get these integral expressions. So if there is some sort

## 20:16

of spatial dependence, then what we're effectively doing is defining a region average flux spectrum

## 20:23

using this equation. And if you look here, what we're doing is saying, hey, I've got a volume

## 20:30

times this flux spectrum.

## 20:32

Equal to the integral of the space-dependent flux spectrum over R.

## 20:39

This is the same sort of equivalence that we were doing with the effective cross-sections.

## 20:44

Only now the integral is not the energy integral, it's the spatial integral.

## 20:48

And in general, effective cross-sections can be defined relative to energy, relative to space.

## 20:56

You could do angle as well, right? I would say that in practice,

## 21:01

a huge chunk of reactor physics is all about producing cross-sections that represent the system of
interest.

## 21:10

And the reason why generating cross-sections is important is, for many years, and even now,

## 21:16

Monte Carlo, using the continuous energy data that we're using right now, it's too expensive for
routine analyses.

## 21:23

In fact, I would say that it's only really useful for the large-scale sort of heroic types of
analysis,

## 21:31

of models like the like final sanity check on a design but for routine design iterations things

## 21:37

where you need quick turnaround monte carlo is still not yet doable it might be for smaller

## 21:43

reactors you've probably heard small modular reactors in the news and such so for smaller

## 21:48

plants yeah monte carlo might be useful for design iterations for a reactor like ours which is the

## 21:55

size of a garbage can as long as we have a big enough computer sure monte carlo could be used

## 21:59

for that as well but the historical practice has been go from the continuous energy down to

## 22:05

several energy groups right it could be hundreds and then whittled down to maybe even as few as two

## 22:11

right for a lwr analysis which is what we're heading into now so anyway this notion of

## 22:16

equivalence of preserving reaction rates is something that we saw early on and uh it's

## 22:21

gonna it's gonna be with us um for the for the rest of what we do okay all right so let's create

## 22:27

a pwr unit

## 22:29

you

## 22:29

using the lwr unit cell class and it looks almost identical to what we did with the sfr stuff it's

## 22:36

just now using slightly different um well different class but we call it in the same way so we can

## 22:43

give it the 0.41 0.48 and pitch of 1.62 okay we've got that and i think we want to plot it then

## 22:56

right so if i want to do the plot of the cell

## 23:00

we'll get something that looks like this right so the lwr unit cell is on a square lattice as

## 23:08

opposed to the sfr which is on the hex lattice so the the outer shape looks a little bit different

## 23:12

but otherwise it's a three region unit cell right and we'll be able to run it the same way that we

## 23:17

did the sfr okay so i'll go ahead and run this you can go ahead and do that too if you haven't
already

## 23:28

and you'll notice um that when openmc is running the very first things it does after it's sort of

## 23:37

logo and copyright stuff is it shows you what data it's loading okay for our purposes uh we don't

## 23:44

have a like a very large number but for instance when i define the cladding material behind the

## 23:50

scenes i'm using elemental zirconium right so most pwr cladding the little the metal sheath

## 23:56

around the fuel is metallic and it's usually some sort of zirconium

## 24:00

alloy zircoloi um i think there's zircoloid it's numbered zircoloid one two three four i think

## 24:07

it's zircoloid four which is most common i don't remember off the top of my head what the alloying

## 24:12

uh agents are so i'm just using natural zirconium right um either way all of the zircoloid

## 24:19

uh alloys are chosen because they are relatively um invisible to neutrons like the cross sections

## 24:29

are pretty low

## 24:30

right

## 24:30

remember what we want in a light water reactor are light mass things to slow the neutrons down

## 24:35

we don't want unnecessary resonance absorption right some isotopes of chromium for instance

## 24:41

uh iron and such make things like stainless steel a little bit worse for neutron economy right so

## 24:48

if you put in stainless steel you'll automatically get a hit to k infinity because you are losing
some

## 24:54

of neutrons to that cladding for any cladding material you're going to lose some neutrons it's

## 24:59

minimized when you

## 25:00

choose something like zirconium okay all right so by default the two group parameters are produced

## 25:08

um and then what we'll do is come up with a slightly different form for k infinity where

## 25:16

instead of having the three regions that we have in open mc we're going to whittle it down to two

## 25:22

regions which is consistent with the book a moderator and fuel the one change i'm going to

## 25:27

do my notation of them instead of calling it the moderator i'm going to call it non-fueled

## 25:31

because what i've done behind the scenes is i've taken the cross sections the fluxes the volumes of

## 25:36

the cladding and the coolant regions and i've combined them together so that reaction rates

## 25:42

are preserved okay you can go and look at how i'm doing that but it's basically just a statement of

## 25:46

this non-fuel volume times this non-fuel flux times this non-fuel cross section has to be equal

## 25:52

to the sum of the individual reaction rates okay and that that's this notion of equivalence theory

## 25:57

right so um anyway if we want to see

## 26:01

what the two region data are we've got the fuel flux absorption cross-section and the single volume

## 26:11

right so a question i would ask is which of these is the thermal flux you said hopefully the first
one

## 26:26

why

## 26:29

pwr needs to be having visions of their thermal spectrum so you don't get highest flux at that point

## 26:36

that's

## 26:37

that's not a bad way to reason it right so suppose it were not the case that 26 is our thermal flux

## 26:44

what else do we have going for us in terms of cross sections kind of related to the sfr like

## 26:52

this notion of uh spatial independence right what happens to the cross sections at thermal

## 26:57

energies compared to fast energies are they bigger or smaller bigger they're bigger right so

## 27:04

specifically for fission right which is we want the high fission we know that the fission cross
section is

## 27:10

500 barns for new 235. so the fission cross section actually cross sections in general tend to be

## 27:16

larger so this is actually the fast flux right so the way that this is indexed is zero and one it's

## 27:24

like the python these are python array but numpy arrays uh and so group one our fast group is index

## 27:31

zero group two our thermal group is index one okay i'll try not to use the index number in terms of

## 27:39

of the groups i'll do group one and group two just have to be careful about how to index it

## 27:43

so yeah it seems maybe unintuitive that the fast flux would be bigger but remember when you did

## 27:49

your homework from last week i had you compute phi 1 over phi 2 and k infinity so you all met

## 27:56

most of you got that one uh right and what you found is that the flux ratio was something like

## 28:02

eight point something and change okay if you take 26 and you divide it by 3.7 you get something that

## 28:08

looks pretty close to that right um off the top of my head i always remember the the faster thermal

## 28:15

ratio being somewhere closer to four for a pwr here we can actually just do it right so if i if

## 28:22

i want um pwr flux fuel zero that's my fast flux and then i can do the equal one okay that gives me

## 28:36

something like seven so not super far off

## 28:38

from four it's a little less than 10 which i think was the answer for the exam right so it um

## 28:45

for a reactor like ours it'll be closer to one to one and maybe two to one okay right but just

## 28:52

because it is significantly larger doesn't mean that we're weighting the fission to the fast group

## 28:57

because the cross sections at thermal energies are so much larger right so the overall reaction

## 29:02

rate at thermal energies is is larger okay and you can see that from the absorption cross section

## 29:07

absorption cross section

## 29:08

is much larger at thermal energies and the fission cross section would be even larger relatively

## 29:13

okay all right so a bit on notation the the book uses this uh bar notation to represent the group

## 29:21

flux what i mean by that is integrated over energy right over the energy range either thermal

## 29:26

intermediate or fast i don't really like that i figure if i write the flux and i don't put

## 29:31

parentheses e as though it's a function of e i'm indicating it's it's a total flux that's how i've

## 29:36

done it before anyway uh anytime i would

## 29:38

write something like phi sub g and the multi-group framework that means a groupwise flux so

## 29:43

integrated over the corresponding energies right so i think in the notation i have i'm being

## 29:49

consistent with the book if i deviate uh i don't think it's intentional but i think i think from

## 29:56

context we should be good on what what each of these um subscripts or superscripts means

## 30:03

okay so uh where i say double click and put your answers here i literally mean

## 30:10

go like this and then put the which flux is thermal and why right so don't let me just be a talking

## 30:17

head that goes in one ear and maybe out the other ear write it down in your your notebook okay all

## 30:31

right so in the book as i said they use three different energy groups fast intermediate and

## 30:36

thermal uh and then the two regions fuel and the moderator i've already said that we're going from

## 30:42

moderator to nf to include all non-fuel stuff and we're going to go from the moderator to the

## 30:48

to lump together the intermediate and fast ranges. Because remember, our group structure here for
the

## 30:54

two groups is everything below an EV is thermal. Everything above an EV is non-thermal, what I'm

## 31:00

calling fast. So that includes the I and F that's discussed in the book. So what I'd like you to do

## 31:07

is using those small changes, adjust the notation of the four factors, which I've reproduced here

## 31:14

directly from the book. So this is equation 4.49 from the textbook. It's the reproduction factor

## 31:20

eta sub t, and it is the ratio of the effective fission cross-section times nu over the effective

## 31:26

absorption cross-section, both in the fuel and both at thermal energies. So we're keeping fuel.

## 31:33

We can keep thermal as one of our energy groups. So this one is actually fine, right? Everything

## 31:39

that we're getting out of OpenMC, we can define this without having to change it.

## 31:44

Okay. For the thermal utilization, again, we have only thermal values of the cross-section,

## 31:55

so that's good. But the notation is a little different from what we're using because it uses

## 32:00

the moderator subscript M or the superscript M on the cross-section. So what I'd like you to do

## 32:06

is take this and replace those M's with the Ns, okay? This is giving you a little bit of practice

## 32:13

of diving into a latex expression, right? So

## 32:17

when you double-click on this, you should be able to see the bits and pieces that lead to the

## 32:22

symbols that are ultimately displayed, right? So if this is my M, if you want to put two letters,

## 32:29

you actually have to enclose it in the curly braces. I should have done that for you. I apologize,

## 32:34

right? But I can do that, and now I have NF instead of the M. And where else is the M?

## 32:41

There's also an M right here, so I can change that on the volume. And then finally, the flux,

## 32:49

thermal disadvantage factor, which is just the ratio of the moderator to the fuel flux,

## 32:54

has that M, so I'll go ahead and change that as well. So now these become starred equations. You

## 33:07

can either do it right in place like this, or you can move it further down, right? Okay, and then

## 33:23

finally, no, not finally, but next, the resonance escape probability. So in the book and in some of

## 33:30

the notes that I have, I'm going to show you a little bit of the resonance escape probability.

## 33:31

From a couple times ago, the resonance escape probability was given in terms of a resonance

## 33:37

integral, which had an exponential. That was what I had called a correlation, something that was

## 33:44

developed from experimental measurements of lattice cells with uranium oxide. If we're

## 33:50

sticking with the two group, or in the book's case, the three group approximation, you can also

## 33:56

write down the resonance escape probability in this way. What this is saying is, hey,

## 34:01

we start off with however many neutrons that we do from fast energies. We'll call it just one

## 34:06

neutron, right? So if I take that one neutron, if I didn't have any resonances, the probability that

## 34:13

it gets down to thermal energies is going to be one, right? But we know that's not the case. So

## 34:16

if we've done the computation with OpenMC and we have fluxes, then what I'm doing here is taking

## 34:22

one and I'm subtracting from it the ratio of the absorptions in the intermediate domain, right,

## 34:29

the resonance absorption rate,

## 34:31

divided by the resonance absorption rate. Where did that go? Here. Did I? Oh, I copied that

## 34:43

twice. See, that's a bug. That and that are the same, but it shouldn't be because this one should

## 34:50

be the I, okay? Right? So this is the resonance absorption subject just to the fuel. The

## 35:01

assumption here made in the book that's maybe, I don't know if it's explicitly called,

## 35:05

is that there is no resonance absorption in the moderator or non-fuel region. Does that make

## 35:10

sense? If I'm an intermediate energy neutron, so say a thousand EV, can I be absorbed in the water?

## 35:26

Hydrogen have an absorption cross-section? Does it magically vanish at those energies?

## 35:34

No, it's just relatively speaking, it's a much smaller value than it is in the fuel at the same

## 35:39

energy. So it's an assumption, right?

## 35:41

And we actually have the tools that we can see if that's the appropriate assumption. So

## 35:45

basically what this ratio is, all of the absorptions happening above one EV, divided by

## 35:52

all of the absorptions happening everywhere. And if you think about it, in our infinite medium

## 35:58

system, right, it's an infinite medium. It's heterogeneous. It's not homogeneous. But in

## 36:02

our infinite array of PIN cells, if a neutron is born at PIN energies, what are its pathways to

## 36:08

death? Absorption. Absorption at PINs. Absorption at PINs. Exhaustion at PINs. Exhaustion at PINs.
Exhaustion

## 36:11

at fast energies intermediate energies or thermal energies here we're assuming nothing happens in

## 36:17

the fast region it's only the intermediate region but one minus the intermediate relative to the

## 36:22

total gives us the fraction of neutrons that makes it to those thermal energies right measured by

## 36:28

the thermal absorption rate okay so with this you can change uh you can do the same adjustments to

## 36:34

to include the fast energy region um and then the fast fission factor

## 36:42

which is something that without having the two group data is really hard to describe right what

## 36:48

is the fast fission factor and if you look at it here it's the ratio of all of the fissions

## 36:53

happening everywhere divided by all the fissions that are happening due only to thermal neutrons

## 36:59

right so it's a ratio of total fission to thermal fission i said before that maybe epsilon would be

## 37:04

something like that but if you look at the fission factor it's the ratio of total fission to thermal
fission

## 37:04

like 1.05 turns out for pwrs it is substantially larger than that it's something like 1.2 to 1.3 and

## 37:11

we'll see that um in a moment okay so in those expressions they are all still integrals over the

## 37:22

um the energy so what we need to do is simplify them to be in terms of the effective cross-section

## 37:28

right because the effective cross-section is what we get out of openmc the flux for each of the two

## 37:34

groups is going to be the fission factor which is going to be the fission factor which is going to

## 37:34

be the fission factor which is what we get out of openmc and we have the volume so we can take this

## 37:39

expression and use it as kind of a cookie cutter and then simplify the resonance escape probability

## 37:45

and eta so go ahead and and change these two now i i understand that some of this stuff you maybe we

## 37:52

don't have the time to do it in seven minutes but uh i'd like you to to work on on getting those

## 37:58

because you'll need that then for the homework that will be assigned for next week okay so maybe

## 38:03

don't necessarily want to do it in seven minutes but i'd like you to to work on on getting those
because you'll need that then for the homework that will be assigned for next week okay so maybe
don't

## 38:04

necessarily worry about it for what you turn in as part of today's homework but keep in mind that

## 38:08

we will be building on that okay so just as an example for how you would get going with the

## 38:17

four factors we need for eta the fuel volume sigma a thermal for the fuel and a new sigma f

## 38:27

for the fuel and the flux for the fuel but the flux will cancel out so really it's just the the

## 38:34

two things so rather than try to use the the object pwr and use the methods to get out everything

## 38:42

i find that it's a little bit easier to use a bit of shorthand right so if i want to get the fuel

## 38:47

volume for instance i i could say hey bf is equal to pwr dot volume and i give it fuel right right

## 38:56

it's so behind the scenes volume is a dictionary and it has four entries the fuel moderator

## 39:02

cladding and then non

## 39:04

fuel okay so if i want to get new sigma f new sigma f for the thermal energy then i would say

## 39:17

hey this is equal to pwr dot new sigma f and give it fuel

## 39:28

and because this is the thermal energy which of the two values do i want zero or one

## 39:36

right okay and then i can copy this to save a little bit of typing get rid of this and

## 39:48

this okay and once i have these then i have um well really i just need eta t is equal to

## 40:00

nu sigma over sigma at and i get an eta of 1.87 now one thing that i didn't do and i could have

## 40:18

is found a way to keep uncertainties tracked right so because openmc is a monte carlo tool

## 40:26

every single value that it gives us k infinity the cross sections and such are estimates that

## 40:33

have uncertainties so it's k

## 40:35

effective as 1.3 plus or minus some smaller number right ideally that number is so small

## 40:41

that we don't have to care about it but in our case it's actually not a like a negligible amount

## 40:47

and it would propagate through to these things so we don't have time to worry about unsun
uncertainty

## 40:53

propagation in this class that's kind of outside of our purview so hopefully the statistics are

## 40:58

tight enough where these numbers won't like jump all over the place in a way that's unphysical

## 41:03

this number seems reasonable 1.87 it's similar to the

## 41:05

best number that we've ever seen so we're going to go ahead and do that and then we're going to

## 41:05

look at the values that we've seen before um okay one thing that i will do here because i thought to

## 41:13

try it out and it actually works uh is if you go to the um to the modules underneath this lesson

## 41:23

i gave a link to greek letters in plain text

## 41:28

so this hasn't always been the case but at least in in recent times python accepts

## 41:35

the use of unicode characters right so you might be familiar with the latin alphabet

## 41:40

uh you know like uh ascii and things like that we can actually take these greek letters copy and

## 41:47

paste them into the code and shorten what like kind of like the what we write out for variable

## 41:52

names so for instance i can take the sigma here copy that and i can go back to my thing here and

## 42:01

let me go ahead and do that okay

## 42:05

so i'm just replacing all of where i type out capital sigma with this copied and paste sigma

## 42:12

character right and oh that's because i didn't do that inside my bed getting to beyond myself here

## 42:26

ah right we can do it to define our new variables that it doesn't change what i've done in in the

## 42:32

pwr unit cell code right but and then you could do it with new and you could do it with with the

## 42:37

other parameters

## 42:38

that as you see fit it's just a little nicer to look at and then when you actually compute

## 42:43

things for the four factors it looks a little bit more like what the mathematical equation

## 42:48

does right so you can do that if you want it's just something i thought i'd point out

## 42:53

you can do the same thing then for each of the other three factors but

## 42:56

uh i i think at this point i've said basically everything i want to you can sit and tinker with

## 43:03

it uh define uh the volume for the the non-fuel i i guess just to make sure that we're on the same

## 43:08

page about

## 43:09

that if i want to get the the volume for the non-fuel it would be pwr dot volume

## 43:16

non-fuel right and then i can print that out in 1.05 right so all of the stuff for the non-fuel

## 43:24

will have this key to get it so it'll be the sigma a for um the absorption at for both index zero
and

## 43:32

one um and such but with that you have everything that you need to actually compute these things at

## 43:39

you know i had a bunch of things um working with all the different Mitsubishi

## 43:52

stochastic numbers that i'm getting but i just pulled it out without them

## 43:58

i put it with certain numbers on it and and i think what you'll want um to do is kind of

## 44:04

write it with expendum 웃 g infrastructures and then be able to wrap up the für and j together

## 44:08

and see how it works out and you'll contribute to what you need to do if you actually think this
that

## 44:08

is you know for people that um automatically put things together in their you knowisher stand up for

## 44:09

really what i wanted this exercise to be for this week is to verify that you're all on the system

## 44:15

and you can run these things okay we will be using this these tools next week when we when we start

## 44:21

to look at the uh design stuff and at that point you will need to compute the floor factor so you

## 44:26

might help yourself now by actually just getting it done um but you don't have to for what you

## 44:31

submit today okay we'll return to this notebook uh for similar ones that that you can use some

## 44:36

of the same expressions but what is that because you wanted to submit for this everything for

## 44:42

today is due at five o'clock i mean like the notebook though yeah so basically whatever you

## 44:48

have done right now as long as you have a notebook that has something done from within class go
ahead

## 44:52

and save it uh that's one thing to to know uh so so you you can you can uh either print preview

## 45:02

depending on your browser and then uh control p to

## 45:06

print

## 45:06

print as a pdf if if that doesn't i prefer pdf because that loads right away then in the

## 45:12

uh canvas but if it doesn't work for you go ahead and do the uh the jupiter notebook file too

## 45:18

right as a separate file to the upload right so upload your solution to the

## 45:23

homework problems as one file and then upload this as the second one okay

## 45:29

any questions on this was everyone able to get it to to run or did we still have so i

## 45:36

think i'll read through it here all right so one of the things that we did in the last five years uh

## 45:36

I think you were still installing it before.

## 45:39

Oh, no, you had the cross-section issue.

## 45:40

So, good.

## 45:41

Anybody not get something to run?

## 45:44

I just got it to work like two minutes ago.

## 45:47

What was that?

## 45:49

It was really annoying.

## 45:51

The only way I was able to solve it

## 45:53

is I deleted lesson 18,

## 45:54

deleted the other Python thing,

## 45:58

edited it on Notepad++,

## 46:00

re-uploaded it,

## 46:01

then downloaded lesson 18 again.

## 46:03

All right.

## 46:04

Well, I mean, you did look a little grumpy over there,

## 46:07

so I wouldn't have had to get that.

## 46:08

He kept resaving the utils file,

## 46:11

and he kept referring it back to the independent source.

## 46:15

Okay.

## 46:16

I don't know more.

## 46:18

Sorry.

## 46:19

Okay.

## 46:20

All right.

## 46:21

Then class is over.

## 46:24

Get that thing submitted,

## 46:26

and then enjoy the weekend.

## 46:28

You shouldn't really have a whole lot to do for me

## 46:30

over the weekend,

## 46:30

which is probably nice, right?

## 46:32

Okay.

## 46:33

Question.

## 46:33

Yeah.

## 46:34

Yeah.

## 46:34

That was good.

## 46:35

Yeah.

## 46:35

Yeah.

## 46:36

Sure.

## 46:37

Yeah.

## 46:37

I'll go ahead and stop this for now.
