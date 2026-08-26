# L31 Local Audio Transcript

Course: NE 630

Playlist source: https://youtube.com/playlist?list=PLy481lNHlnHoEO95vM-xYX2bydD25v20L

Video: NE 630 - Lesson 31

URL: https://www.youtube.com/watch?v=dCeRWmcJYyc

Video ID: dCeRWmcJYyc

YouTube upload date: 20231108

Duration: 53:25

Transcript source: Local faster-whisper transcription from YouTube audio.

Whisper model: large-v3; detected language: en.

Generated: 2026-06-28

Note: This transcript is machine-generated from audio and lightly wrapped only. It should be reviewed before being quoted, published, or used as polished lesson text.

Requested language: en

## 01:00

So raise your hand if you spent a little bit more time reading than you normally do.

## 01:05

I'm unsurprised by that.

## 01:11

Hopefully you found that it was useful, right?

## 01:14

And not just some labor for the sake of reading.

## 01:20

I had a conversation with one of you yesterday about the book, and I was in agreement.

## 01:27

The book is good.

## 01:29

I mean, there are a lot of textbooks out there.

## 01:31

And I would say that most textbooks that any of us faculty would assign to you have value.

## 01:37

You know, the reading that we do is not, I mean, I'll be honest, as an instructor, it's

## 01:42

sometimes easy to say, hey, this is a class in reactor physics or heat transfer or something.

## 01:46

It's like, I've got these 30 to 40 topics, and we put them here.

## 01:50

It's like, I look at the book.

## 01:51

All right, that's the section that goes to this stuff, right?

## 01:54

Have I gone through the reading and done a detailed set of notes?

## 01:58

Maybe not in the past.

## 01:59

I do more for this class.

## 02:01

As I've said, it's the second time I've taught it, and last time was so bizarre that it's kind of a
first time really trying to leverage the book.

## 02:14

And so there's value in it, right?

## 02:16

Because there's only so much information that I can spill out in 50 minutes.

## 02:21

And to be honest, spilling out information is not the best use of my time in a lecture.

## 02:26

The information is something that is static.

## 02:31

Information is static, which means that the active part of it is you absorbing it.

## 02:36

And if all the information is coming to you in 50 minutes, then the total amount of absorption, to
use terms from our class,

## 02:44

depends on the rate at which each one of you is absorbing, right?

## 02:48

Everyone reads differently.

## 02:50

You all have different reading, basically experience, right?

## 02:54

Some of you read more for fun than others.

## 02:55

Some of you don't.

## 02:56

I find that, I mean, I am a late life ADHD.

## 03:01

I'm an ADHD diagnosie, right?

## 03:03

So I take a pill.

## 03:04

I can concentrate a little bit better than I used to.

## 03:07

But unless I'm super interested in something, it's really hard.

## 03:11

So when I have to read this tome on network analysis for this math class, when I absolutely hate the
language use of this guy,

## 03:18

it's like a highfalutin type of thing where it's 100 words for 10 words equivalent.

## 03:23

It just drives me nuts.

## 03:25

So it takes a lot of effort to really dive in and do that.

## 03:28

This book that we have, I don't think it suffers.

## 03:31

I think that the English is pretty plain spoken or written.

## 03:35

And there's a lot of value code word on it.

## 03:39

And so I've tried as I can to highlight some of the important things, but really the work has to be
done by you with the book and the notes.

## 03:49

Reading is passive in a sense.

## 03:52

Writing notes, critically reviewing what you're reading, that's the active part.

## 03:59

Anybody ever hear of this notion of?

## 04:00

Active learning being the right way to do that's the active part you sitting, listening to the head
talking at the front of the room that's passive reading the book by itself without critically
thinking that's passive you want the active part you've got to be active right there's only so much
that we can do in 50 minutes and none of that matters unless you've done some of the prep work right
otherwise it's like lost it's like you see equations you can hear me say numbers you plug it in you
get a number out what the hell does it all mean.

## 04:28

So anyway.

## 04:30

Hopefully, we will see some improvement and all have learned some lessons and you'll have learned
some lessons on the way to conduct our ourselves when prepping for this.

## 04:41

For the material getting through the material Okay, so I did scan through so thank you for those who
got right on to the reading and then notes taking yesterday, so I was able to look at probably half
a dozen of you, even before going home yesterday, so I have some.

## 04:57

I responded to several of you in campus i'm not.

## 05:00

going to be able to do that for everyone, every time, especially if you're submitting something
right at the buzzer I told you 1pm is fine right that gives me at least 10 to 15 minutes that I can
buzz through and see if there are any.

## 05:15

themes right, and so I saw that in the first batch that came through.

## 05:20

And certainly, if you have sort of burning questions right, you can always post them to the message
boards, I think you had sent me a question on one thing.

## 05:30

That I can clarify here use message board, I mean if you've got questions, maybe others have been or
maybe to.

## 05:37

pique the interest of others and they'll doing it i'm not going to require discussion sex I hate
that kind of task.

## 05:44

Right, because I have to separate to in this networks class I hate the forced discussion thing you
can do it if you want, if you feel like it's something where you're engaging and it just feels like
the.

## 05:56

interesting to do then do it, I encourage it, but I will never force that sort of thing that's.

## 06:01

That feels like kindergarten or something I feel like it's enough to force quote unquote you to read
the book and write me some notes okay so we'll adapt that on the fly as necessary over the last
roughly month of the course and yeah.

## 06:20

Okay, so today we turn to a completely different topic, which is basically the same thing I said
when we started Chapter five right the time dependence of the neutron.

## 06:30

Right, the one thing that we've been avoiding and i've been trying to just keep it away as much as
possible is the spatial.

## 06:40

diffusion of neutrons right how neutrons move around we've seen insipid a little bit when we did
some of the unit cell analysis right there's this one factor, the var Sigma.

## 06:53

The disadvantage factor that ratio of the moderator flux to the fuel flux right that's necessarily a
space.

## 07:01

component so you're saying that the flux varies in these two spatial regions right it's not saying
anything about how it varies within the spatial region will be able to do that as part of what we do
in this chapter and then in Chapter seven which is like the last thing that we're doing in the
course.

## 07:15

So we've seen it and being able to take the results and apply them to the equations, as we do in the
four factor formula like that that's let us do some of that stuff so, in a sense, I would say that
we've covered all of the relevant reactor physics.

## 07:30

That we're going to.

## 07:31

cover in this class already Okay, why do I say that well when we go to the spatial part what we're
doing is just filling in some of the detail that was already sort of there by using the unit cell
analysis and so forth, and we'll be able to solve a wider variety of problems.

## 07:47

We can do things that are kind of consistent with shielding we can do things like look at very
different geometries right, but the basic physics of it all, and when I say physics, I mean the
connection.

## 08:00

From what we see in the real world or in the applied space, which is like a reaction rate.

## 08:04

Why do I say that's what we see in the real world, because if I put a neutron detector into the
core, I am measuring a reaction rate and so that's the thing that I can sort of get it close to
right in the in the laboratory and that is our connection to the underlying physics.

## 08:20

what's driving all of this what's the like the most fundamental thing that you need for reactionary
there are really two components, but there's one that.

## 08:31

is hiding a whole lot of.

## 08:32

physics cross sections, the nuclear physics is embedded in the cross section, so when we call talk
about nuclear reactor physics or nuclear reactor theory or talk about nuclear reactors in general.

## 08:49

don't forget that the nuclear means that there's a hell of a lot of nuclear physics involved.

## 08:55

We don't have to solve the nuclear physics problems that's for the physicists, but what do we get
out of it, the cross sections, the cross sections thing, combined with the slugs gives us the
reaction rate as nuclear engineers, we care about.

## 09:07

reaction rates right if there's one thing in this class that we should be able to understand is
reaction rates.

## 09:15

we're adding the one piece of the puzzle that sort of completes it here and that's things like
leakage and so forth, but.

## 09:21

I would say the physics, the connection to the physics is kind of in the rear view mirror now now
now now we're just filling out the details and I hope sharpening some of your math skills and
filling in some gaps that you might have had in past things and then.

## 09:37

Really.

## 09:37

I guess cranking out some new applications with with some of the stuff that you've seen in
differential equations.

## 09:44

So we'll be taking so, even though there are only two chapters left for this entire month we're
going to be like it seems like not a whole lot of.

## 09:51

pages for the time that we have left we're going to be going through it slowly right so as I said
that the book is pretty high value per word for this spatial diffusion stuff it's pretty short, so
you saw even today the reading was.

## 10:07

What.

## 10:07

Three four pages or something like that and there's a lot there right, not a whole lot of like doing
the math right we'll do a little bit of that today and i've suggested some problems and we can work
on those if there's time at the end.

## 10:21

But then, as we go into the next section so, for instance, you'll be reading sections 6.3 I think
that's like two or three pages right it's very, very short we're going to study it.

## 10:33

And then you look basically look at solutions of the diffusion.

## 10:38

For the very simplified case that is covered in there, and then for Monday thereafter you'll read
6.4 which is about boundary conditions and interface conditions right the words that you've probably
certainly boundary this you've heard before and it's the same thing as an initial condition it's
just now we're talking about space.

## 10:58

And the variety of the boundary conditions are important for the modeling of neutron diffusion
because.

## 11:06

Each.

## 11:07

Boundary condition type represents something completely different and remind me one more time who's
in heat transfer or has had heat transfer.

## 11:16

So what would the nice thing for you folks is the diffusion equation is a heck of a lot like the
heat induction equation and so any time that you spent doing the reading in that class or hearing
the instructor talk about things in that class will have relevance here for the neutron diffusion
equation.

## 11:37

genesis super going on i'm going to give it to you guys.

## 11:40

Go to the butch.

## 11:41

Arne Dun chairs one two three four

## 11:46

Don marshal

## 11:48

You got a bunch of sensible things that are going on down there and you've got much more detail to
show you guys i've been

## 12:05

Right.

## 12:06

All right.

## 12:06

go to.

## 12:06

as we talk about the diffusion equation today.

## 12:08

It is not the end of the line

## 12:10

for nuclear engineers in general.

## 12:12

The diffusion equation for an undergrad

## 12:14

in nuclear engineering,

## 12:15

that is the end of the line, right?

## 12:17

We don't go past it.

## 12:20

All right, so talked about the reading and notes,

## 12:24

office hours, explicit office hours now,

## 12:26

not just by appointment,

## 12:27

although I've been around today

## 12:30

and then Wednesdays three to four

## 12:32

and Thursdays 1230 to 130.

## 12:34

I'm hoping that covers most of you.

## 12:36

I know not all of you are going to be interested

## 12:38

in office hours anyway,

## 12:39

but I hope that those who would come and see me,

## 12:43

those hours work.

## 12:44

And if not, send me a message.

## 12:46

And if I have to add a time or change a time,

## 12:48

I'm happy to do that.

## 12:49

I'm giving this the first stab

## 12:51

rather than trying to do the doodle poll

## 12:53

that I was suggesting I might do, okay?

## 12:56

And then the other part of the war reparations will be due.

## 13:01

Now, for those who weren't here on Monday,

## 13:02

of course, war reparations

## 13:03

are the after the war payments

## 13:06

that Finland had to make to Russia

## 13:08

following the end of World War II.

## 13:11

I learned Finnish as an undergrad

## 13:13

and our Finnish professors made us do test corrections

## 13:17

and he called them war reparations.

## 13:20

Anyway, balance over the control volume.

## 13:25

So what I've done here

## 13:26

is I've actually just taken some slices from the textbook

## 13:28

to go through and discuss things

## 13:31

because a lot of the questions

## 13:32

that I was seeing in the notes

## 13:33

had to do with,

## 13:34

some of the, I guess,

## 13:37

really just the presentation of the material.

## 13:40

There are a couple of things in the book

## 13:42

as far as like typesetting goes

## 13:43

where it's not as clear as it could be.

## 13:47

Remind me when we get to the diffusion equation

## 13:49

in particular,

## 13:50

I want to clarify something

## 13:51

that is a pattern in the book

## 13:54

when doing a division that I don't like,

## 13:56

but we'll clear that up when we get there, okay?

## 14:00

So everything that we've done so far

## 14:03

has been about reaction rate,

## 14:04

right?

## 14:05

So that's a cross-section times a flux

## 14:07

and the source terms like from fission,

## 14:12

we've now covered things like the change in time, right?

## 14:17

So we're going to stay away from time.

## 14:19

We're going to assume time independence again

## 14:21

and steady state,

## 14:22

but now we're dealing with a finite volume.

## 14:24

It's no longer this infinite medium

## 14:26

that I've talked about, okay?

## 14:28

It's going to be a finite volume,

## 14:29

which means that things will change in space.

## 14:32

So in the book,

## 14:33

the idea is similar to what you probably have seen

## 14:36

in many other engineering classes.

## 14:39

We care about what's going on

## 14:40

in some sort of control volume, right?

## 14:43

And so everything here is in the Cartesian coordinate system,

## 14:46

so x, y, and z.

## 14:47

Here's the origin,

## 14:48

so x, y, z all equal to zero.

## 14:51

And what we care about is this cube

## 14:54

of size dy, dx, dz, right?

## 14:58

That's the volume.

## 14:59

And the point R is in the center.

## 15:00

So there had been some questions, right?

## 15:03

Can I get rid of that?

## 15:07

Okay, will this work?

## 15:08

I'm trying something slightly new with the Jupyter notebook

## 15:12

or something that I haven't done much of, right?

## 15:14

Can I write on here?

## 15:15

Do, do, do, no.

## 15:20

Where is it?

## 15:22

There we go.

## 15:22

Okay, so if this, are you serious?

## 15:33

It was just working a moment ago.

## 15:36

This is.

## 15:37

Okay.

## 15:37

Okay.

## 15:37

Okay.

## 15:37

Okay.

## 15:37

Okay.

## 15:37

Okay.

## 15:37

Okay.

## 15:37

Okay.

## 15:37

Okay.

## 15:37

Okay.

## 15:37

Okay.

## 15:37

Okay.

## 15:37

Okay.

## 15:38

Okay.

## 15:38

Okay.

## 15:38

Okay.

## 15:38

Not cool.

## 15:43

I, I, I, I, I, I, does this one work?

## 16:02

Well, that's interesting.

## 16:03

This whole thing was working before.

## 16:05

So I guess I can't sketch on it.

## 16:06

I don't know what the hell is up with that.

## 16:12

Oh, well, maybe I should just go to PowerPoint

## 16:21

and be like everyone else.

## 16:24

Okay.

## 16:24

Anyway, so there was a question on later on

## 16:29

in the presentation of one half that shows up.

## 16:33

Okay.

## 16:33

There's nothing tricky about that, but what, what it is, is we're assuming that X, Y, and

## 16:38

Z is in the center of the box and we're going to, because we're centered, then the D Y has

## 16:44

to be split, but the DX has to be split.

## 16:47

So I think the funky thing in the presentation of those equations, and that's on the next

## 16:51

slide is it's just kind of crammed together in one line and it looks a little wonky, right?

## 16:56

Um, so what do I mean by that?

## 17:00

So this is the, the, the neutron leakage.

## 17:02

So there's this term.

## 17:03

J, which is called the neutron current.

## 17:06

Okay.

## 17:07

And it's broken up into individual components, the J X and the J Y and the J Z.

## 17:14

Right.

## 17:14

And so at the right-hand side of the cube or on the left-hand side of the cube, right.

## 17:21

We can evaluate this, this neutron current.

## 17:24

Okay.

## 17:24

And there was another question.

## 17:26

Why is there a minus sign right at X minus one half?

## 17:32

Okay.

## 17:34

Well, what is J of X or J sub X?

## 17:40

Turn with the number of neutrons per second during the positive X.

## 17:44

Yeah.

## 17:45

So it's, it's relative to the X axis.

## 17:48

So J of X at J sub X at X tells us that the net flow going to the right.

## 17:54

Okay.

## 17:55

If I go to X minus DX over two, I'm on the left-hand side of this cube.

## 18:03

If I want to know the number that is leaving.

## 18:05

That means.

## 18:06

The number going to the left.

## 18:08

I have to negate the number going to the right.

## 18:11

So it's just, it's a, it's directing it out of the face.

## 18:15

Okay.

## 18:15

So, um, you might remember something from your vector, uh, calculus called the unit normal, right?

## 18:23

If you're talking about a vector field and a normal, uh, a particular surface, and you want to know
how many, uh, what, what, uh, the number of whatever your field represents going through that.

## 18:35

So you have to use the, the, uh, the, the appropriate normal vector with that.

## 18:41

And so it's like how many are going into the surface versus how many are going out.

## 18:44

It's all, it's all relative, right?

## 18:46

Because it's really just a sign change.

## 18:49

We just have to make sure that we're being very consistent here because we're trying to count the
number of neutrons leaving this box.

## 18:55

I'm really disappointed about this pen, man, refresh this.

## 19:06

And of course that's going to, does this help me?

## 19:15

Ah, there we go.

## 19:16

Why was that happening?

## 19:20

Right.

## 19:23

Cool.

## 19:25

All right.

## 19:26

So if we take the, so I'm going to zero in on just the, the X component here, right?

## 19:32

So we have six faces.

## 19:34

We can do the same thing in all the directions.

## 19:36

Now, remember when we have these three components, these are three components of a vector quantity,
right?

## 19:42

So this would be, if I want to do it like this.

## 19:46

So my J here.

## 19:47

Okay.

## 19:48

Okay.

## 19:48

Okay.

## 19:48

Okay.

## 19:48

Okay.

## 19:48

Okay.

## 19:48

So this is a function of X, Y, and Z, or of, of, of R.

## 19:52

I can write it either way.

## 19:55

Okay.

## 19:57

This is equal to I hat times J X plus J hat times J Y plus K hat times J Z.

## 20:14

Now this notation is familiar to you all.

## 20:18

I assume based on you having had math.

## 20:21

I assume based on you having had two, two, two, way back when is that, is that not true for anybody
who, like, if you remember, I, I think everybody's had two 22, right?

## 20:29

Cause I think that's a prereq.

## 20:31

The one thing that I don't like about our flow chart is we have the immediate prereqs, but there's a
whole host of other courses that are implied that, right?

## 20:38

So it's hard for me sometimes to look at it and make sure that I know exactly everything that you
have, but I assume that this is all familiar terminology.

## 20:46

And of course, if it wasn't, that should have been a big question mark that you had for me in your
notes.

## 20:50

Okay.

## 20:52

So we have these, um, the, the, the, the currents, but if we take the size of the cell to go to zero
and each of these three coordinates, right?

## 21:03

Then we end up with an expression that some of us had to review the last time we met, right?

## 21:09

The notion of a derivative.

## 21:10

So we get this derivative of the current J sub X, and we can do the same thing for all of them.

## 21:16

Right.

## 21:17

But I've got some questions for you, right?

## 21:20

So anytime.

## 21:20

I have these questions, of course, these are the sort of conceptual things that I think have tripped
some folks up either from, you know, for whatever reason, right?

## 21:29

So you get to an exam and you get a question like this.

## 21:32

Some of the plain English descriptions I saw were a little underwhelming, right?

## 21:38

And I think for many of you, if you had internalized the, uh, let's say the plain English definition
for each of the four factors, things might've been a little bit easier, right?

## 21:49

Rather than relying on a spin.

## 21:50

And if you're looking at a formula for something, right.

## 21:54

That kind of hides what the meaning is.

## 21:57

If you instead focus on the meaning and maybe have an exam, uh, an example formula to go with that
things can be, you can, you can do a lot more because you're closer to the sort of fundamental
principle, right?

## 22:09

If you, if you know the basics, the fundamental principles, you can build on that.

## 22:12

Okay.

## 22:12

So what in plain English does J sub X represent?

## 22:24

We know it's related to, to neutrons leaking.

## 22:27

from this volume okay but j sub x itself what does it represent it's a net number of neutrons

## 22:34

that passes through the y z point uh base right yes and so and then importantly what are the units

## 22:42

and i'll have somebody else answer that yeah correct yeah so it's got strangely it seems that

## 22:52

it has the same units as a flux right which does that mean that j sub x is a flux

## 23:00

well no not not not our scalar flux there's a one of the issues i think for some folks especially

## 23:08

if you've had physics i would pick on matt if he were here because i know he takes a lot of

## 23:12

physics classes in physics say the you know enm electricity and magnetism there's something

## 23:18

called an electric flux or a magnetic flux the flux in thewelless omega is a flux of physical

## 23:22

those classes is a vector it's not this quantity phi of r that we've dealt with before that also

## 23:29

has units of per centimeter squared per second but it's a vector quantity with that unit so

## 23:33

our current vector here j is like the electric flux or some other flux in another um in another

## 23:42

domain hell even fluid mechanics you can define the you know the um you know the flux of the mass

## 23:49

flux for instance right the basically the the mass per centimeter squared per second you know

## 23:55

in each of the the directions right but one vector that's the same thing that we have here so it'll

## 23:59

have the same units the one piece of information it carries along with it though is its direction

## 24:04

right that's the difference the flux that we've dealt with before phi has no direction right it's

## 24:10

it's just a quantity okay now we're breaking it up into um the individual components so yeah so j of

## 24:17

x is represents

## 24:18

you

## 24:19

that that net number of neutrons per centimeter squared per second through

## 24:23

the appropriate face so for x that would be the yz yeah

## 24:26

say that again

## 24:30

all right so it's it's relative to the positive direction but if j sub x were negative then we

## 24:40

that would imply that we have uh a net flow to the backward direction right so j of x the sign

## 24:47

of j of x matters right

## 24:48

so positive means that it's positive relative to the x axis if it's negative that means

## 24:54

negative flow so that means we have net flow toward the negative x axis okay does that make

## 25:00

sense okay so then the thing that we're getting after we we take this limit is the derivative

## 25:08

of j sub x so what does this represent and what are its units let's start with the units

## 25:20

we know that the unit of j sub x is per centimeter squared

## 25:23

per second what happens when i take the derivative with respect to x

## 25:30

per centimeter per second other

## 25:34

per centimeter cubed right per centimeter cubed per second okay interesting and what does a
derivative

## 25:45

with respect to x mean that that's just kind of a general thing it means how fast it's changing
right

## 25:54

if you think about it if my net

## 25:56

flow is changing as a function of x that means somehow i'm losing particles right because if

## 26:03

net flow is not we're not meaning that it's a net change that means if i'm shooting a gun of
neutrons

## 26:08

there's a specific neutron current right if i'm if i have my neutron gun shooting into a vacuum

## 26:16

in one direction right it's the beam port of the reactor shooting into

## 26:20

we can forget about error absorption or whatever that means i have just the constant stream of

## 26:25

neutrons

## 26:26

okay if i put in a like a piece of paper that could count neutrons what the piece of paper

## 26:32

would be telling me is j sub x now if i'm measuring a different j sub x downstream that means
somewhere

## 26:41

i've lost neutrons right it's like if i've measured my my flow of water in a pipe as being

## 26:47

some number some mass per per centimeter squared per second then i measure it later on and i don't

## 26:54

have the same i've lost mass so if i measure it later on and i don't have the same i've lost mass

## 26:56

right so the current is a great way to establish continuity of our neutron population or to assess

## 27:03

where neutrons are going away so if this thing is non-zero right if i do have a change in the

## 27:10

current that means i have neutrons leaking away from my volume right and so that's why

## 27:19

this will show up then in the diffusion equation okay so represent neutrons leaking out of a face

## 27:26

or so it's not it's not an absolute or net quantity itself right because that by the time

## 27:32

we take this this finite sorry the derivative we've gone from this finite difference over the

## 27:38

volume which is as written here is a finite volume right from dx is small but it's still big enough

## 27:45

that we can differentiate between a plus half dx and minus right as we take this to zero we've

## 27:53

established this this this

## 27:56

derivative at one point right so it no longer has this the same sort of meaning it just means that

## 28:02

in general though if this thing is non-zero that means that we're we have a net change in the

## 28:07

population right and that's got to be driven by something either we have a source term we have

## 28:11

absorption right uh neutrons are just writing down their gradient there's a change all right so

## 28:23

i reckon that you know how to compute a volumetric reaction rate because that's just a flux times a

## 28:30

section right so we can do that for the absorption cross-section we can do that for the fission

## 28:34

cross-section and then if we multiply it by the volume of our little cell then we get the total

## 28:42

absorption rate per second or the total number of neutrons born per second and then we can also

## 28:50

integrate or multiply s by a volume we get the total number of neutrons

## 28:56

inserted into the system from an external source per second okay

## 29:00

so if we do all that we end up with this thing here the neutron continuity equation okay and if

## 29:09

i can actually write that in vector form as well okay so this thing here is probably the more

## 29:15

common form um but this one kind of establishes that you've got these three individual components

## 29:21

right so straight out of the book as written 610 is basically an exact expression for neutron
balance

## 29:30

well actually that's just the way the table is we've got an example here you have some

## 29:35

of the energy that's getting applied to the society in the galaxy and what does that do

## 29:41

what's going on is that the energy that's getting transferred in the galaxy is actually

## 29:46

at some point going to something where it's just going to be something odd at the end of the course

## 29:50

and then the energy that's actually going to be points to this pitch meow program is going to be

## 29:54

a certain element of some sort of material sort of energy that's going to be there that's going to

## 29:57

vaporized to that particular spot or that particular single point or something like that so you've
got

## 30:00

on that one energy alone right but otherwise this is this is still uh a valid equation

## 30:07

oh why is that doing that okay not have uh there we go but my note at the bottom uh tells something

## 30:34

um telling about this equation we can't solve it so as you're reading through the the derivation

## 30:44

or the sort of description of the diffusion equation it gets to this point but you know of

## 30:48

course the next step is to make an assumption about what j is but as written i mean did it

## 30:53

bother you i guess you probably all have more going on in your life for this to you know to

## 31:03

to be a bother but we're already familiar with this thing right and if we didn't have this

## 31:09

then this starts to look like things that we've solved all along and we could put back in energy

## 31:13

and scattering and have slowing down spectrum equation all that jazz right uh basically just

## 31:19

state

## 31:19

of balance in in energy or time but now we have this but we don't have an expression for this

## 31:26

that's another unknown right if you notice everything that we've said about j has

## 31:31

absolutely nothing to do with the neutron flux right we're just saying kind of qualitatively

## 31:38

let there be a volume with six faces and let it be known that there are this many neutrons

## 31:45

leaving from this side and we'll call it j sub x and this side and j sub x at a different

## 31:49

point and then j so so we're basically just prescribing that there exists this quantity

## 31:58

the neutron current and if we make that that definition and say that it that this quantity j

## 32:05

is the net number of neutrons flowing through this this then we can write this down

## 32:10

the challenge though is figuring out how to relate j to phi because that's the only way

## 32:16

that we're going to get an equation that we can actually solve so when i say that this is

## 32:19

basically an exact equation this would work for neutron transport right that's the next step

## 32:26

beyond diffusion that you would see in a like a what is it any 806 neutronics right it's like

## 32:33

sort of the grad level reactor physics force so there's more going on under the hood but this

## 32:38

would this would capture this captures it for diffusion theory this captures it for

## 32:42

for uh neutron transport theory it all depends on what this term j is if i gave you the simple

## 32:48

like output from say open and the open and the open and the open and the open and the open and

## 32:49

c right where i said this is the number of neutrons i simulated coming out of this phase

## 32:54

you could call that j and write down a balance equation and it would everything would be peachy

## 32:59

okay it doesn't let you solve the equation though right that's that's what we'll be doing um

## 33:06

over the course of the the next several weeks okay so how do we bridge that gap

## 33:14

well the answer for us is something called fixed law out of curiosity had anybody ever

## 33:21

heard of fixed law before doing this reading did it even look remotely familiar you're lying

## 33:32

to yourselves anyway i i just but we'll see in a minute okay fixed law says that the neutron

## 33:41

current is proportional to the change in space of the flux okay what is the symbol

## 33:49

it's a gradient right if you if you're a latech user it's called nabla for no

## 33:56

what nabla means somebody should figure that out for me but it's the gradient right so if this were

## 34:02

one dimensional what is the gradient it's a derivative right so this is a spatial derivative

## 34:10

this is it because it's we're talking about three dimensions r is x y and z the gradient is like the

## 34:17

derivative in x derivative in y and derivative in c each with their own i j k vectors right so

## 34:23

that's a vector quantity this thing is a scalar quantity it's called the diffusion coefficient

## 34:27

the diffusion coefficient is a scalar quantity it's called the diffusion coefficient

## 34:29

is nothing more than a proportionality constant it says that hey the net flow of my neutrons

## 34:34

is proportional to the spatial rate of change of my neutron let's say concentration right we know

## 34:42

that the flux is not the concentration the concentration is actually the neutron density

## 34:48

but how do the flux and density correspond what's the missing link velocity velocity right so we

## 34:57

already said we're not really dealing

## 34:59

with energy so the energy is fixed and so the speed is fixed so v is is proportional to b in

## 35:06

that case right so b here is we can think of that as our neutron concentration and we're taking the

## 35:12

spatial derivative of it right so we get the gradient of it we see the hill going down and

## 35:18

we're saying that the net flow has to be proportional to that it seems somehow i don't

## 35:22

know it's sensible okay exactly what that diffusion coefficient is is

## 35:29

right so we could we could measure it right um in general the fixed law is what we would call the

## 35:34

phenomenal logical model that means we went out into nature we saw it and then we put it into a

## 35:43

mathematical form because it just works right there's this is not like based on any first

## 35:49

principle it's just kind of a it's like a uh what what's what am i there's a description i would use

## 35:59

for this it's sensible common sense it's like a common sense thing like if you've got if you've

## 36:04

got some concentration of something and it's changing in space well it's got to be changing

## 36:09

in space in a way that's proportional to the number that it like flowing right um anyway so

## 36:16

that's that's fixed law and it just works now for those who say you've never seen something like

## 36:24

this before here's a little screenshot that i took from a book called fundamentals of heat and mass

## 36:31

what are you using a heat transfer what book do you remember the author's name does de witt sound

## 36:42

that's this book so in chapter two of that book there is this uh why i really okay that's

## 36:54

i i'll just reset that and that's fine

## 37:01

uh i will get out of this and zoom in so that we can look at this okay now if we take a look at

## 37:10

equation 611 and then we take a look at equation 2.3 out of the book that you all read religiously

## 37:18

right in your heat transfer class i'm guessing it's dr hosney teaching it no who's teaching it

## 37:23

we don't talk about

## 37:27

i would agree with that

## 37:31

do we see any any relationship any similarity what what are the analogs what are the parallels

## 37:41

between this thing here which doesn't go by fixed law it goes instead by another famous dead white

## 37:49

guy fourier right fourier's law fourier's law says that the the the flow of heat is proportional

## 37:59

to the gradient of the temperature right and that's the law that's the law that's the law that's the

## 38:04

law that's the law that's the law of the heat transfer that constant proportionality is called

## 38:06

it's k in heat transfer what's k huh that that's what we've used k for right but in heat transfer

## 38:18

it's the thermal conductivity right so it's a in heat transfer conduction based on fourier's law

## 38:25

says that my my heat flux is proportional to my temperature gradient and the constant

## 38:34

proportionality is negative for the heat transfer right and so that's the law that's the law that's

## 38:36

and i mean it's so it's negative so that means our flow is goes with our downhill trajectory

## 38:41

and the constant proportionality is our conductivity so if you want to start making

## 38:46

connections in your neural network between your ears then you can say to yourself that

## 38:51

the thermal conductivity is like the diffusion coefficient the temperature is like my neutron

## 38:59

flux the neutron current is like my heat flux right so this is here's another example of what

## 39:08

when i say heat flux or a flux being a current the heat transfer conduction is one great example

## 39:14

i should never have bothered with the em stuff okay so yeah it's the same thing now the only

## 39:19

uh i guess apparent difference here is the fact that i'm writing my diffusion coefficient as

## 39:25

being a function of r but of course your conductivity can be a function of space in

## 39:29

your

## 39:29

you

## 39:29

, so every single problem solving technique you learned in that part of heat transfer which that

## 39:35

should be far behind you right that's in your rear view mirror right there's a reason why i put this

## 39:40

at the end so i didn't have to do any work you can just go to your getting okay so and there

## 39:47

exist other other expressions in other physics and other engineering disciplines of course fixed law

## 39:53

is most common in say uh probably chemical engineering

## 39:59

right when talking about the the um diffusion of species in fluids things like that i think

## 40:06

think that's where i would see it but anyway fixed law is sort of um uh that's sort of a more
general

## 40:12

name that i've heard for that approximation but it's it's fourier's law right in a different

## 40:17

context so nothing new for those who have had heat transfer right um but uh it should give you uh at

## 40:27

least something to to to degrade or any other way and another way of thinking about it is uh the hot
water

## 40:28

heat transfer right um um the uh but uh it it should give you uh at least something to to to to

## 40:28

uh the uh but uh it doesn't have to be a sort of red hot water fusion but that doesn't gonna happen

## 40:28

yet so that's kind of the general thing here right and that's that's the the the definition of heat
transfer

## 40:28

to use as a it's nice to see something familiar we'll put it that way yeah now when i say

## 40:37

phenomenological that means yeah we go out and it just seems to work for the thermal conductivity

## 40:43

in a class like heat transfer where do those numbers come from and if you say the back of

## 40:48

the book i'm going to get angry where do we get this from experiments right you put a slab of

## 40:55

material like aluminum whatever you put a heat flux on one side you measure what comes out

## 40:59

voila you you have everything you need in theory you could do the same thing for the diffusion

## 41:04

coefficient it turns out though for that there there is a sort of beyond phenomenological stuff

## 41:11

that you can do to define it right and that comes from neutron transport theory so the one little

## 41:16

result that i would say from transport theory that is of use to us here is this thing which is also

## 41:23

in um the

## 41:24

um

## 41:25

the x-book right and it the author says that the diffusion coefficient is equal to one over

## 41:30

three times sigma tr which we would call the transport cross-section the tr means transport

## 41:36

it kind of looks like the total cross-section and it turns out it's related to the total

## 41:40

cross-section because it's actually the total cross-section minus mu bar times sigma s now

## 41:45

what the flip is mu bar you remember what's that the average scattering yeah so if you remember it

## 41:52

back so it was i checked it was less than

## 41:54

less than seven we talked about neutron scattering okay the physics says that neutron scattering is

## 42:02

isotropic in the center of mass system right we don't live in the center of mass system a lot of

## 42:07

things are easier in the center of mass system right but we live in the laboratory system and

## 42:12

i gave you some pretty ugly expressions that let you relate the scattering angle in the center of

## 42:18

mass system to the scattering angle in the lab system all right it was messy it's a bunch of

## 42:24

cosines and signs it's just nasty right and that's also when we were talking a little bit

## 42:29

about probability distributions and you could do a transformation of variables whatever it was

## 42:33

you can compute this this thing it turns out that for um our for our application of neutrons

## 42:43

interacting with nuclei that mu bar is two over three a when we have isotropic scattering in the

## 42:51

center of mass right there are some situations where that's not true but everything that we've

## 42:57

done is just to sort of assume that okay so remember here this is the mass number a

## 43:02

uh and what this means is that as a goes very large i'd say 238 for uranium then two over three

## 43:10

times 238 that's pretty darn close to zero so in the book it it said something about if mu bar is

## 43:16

zero then the diffusion coefficient is just one over three times the total cross-section right

## 43:22

and so that's a fair approximation and unless we're doing something where we're really trying

## 43:27

to be faithful to some system we'll probably just use one over three times sigma t or that's

## 43:31

the assumption that you you can make now for small a right say a equal one this mu bar is two

## 43:40

thirds right so two-thirds is a pretty big fraction right and if we're taking our scattering

## 43:47

cross-section multiplying that by two-thirds and then peeling that off from sigma t that reduces

## 43:52

sigma t by a substantial margin right so sigma tr is

## 43:57

always less than sigma t right because of this non-zero scattering uh cosine okay what does that

## 44:05

mean if you think about sigma t what is sigma t if i'm a neutron i'm entering a medium that has a

## 44:14

total cross-section of sigma t what does sigma t tell me about me the neutron yeah right so it's

## 44:26

the remember that sigma t is one over the mean free path so i take one over sigma t i that tells

## 44:31

me on the average how far i'm going to go and i'm going to take one over sigma t and i'm going to

## 44:32

go well if we replace sigma t with sigma tr for something like hydrogen right where mu bar is now

## 44:41

two over three and we already know that the total cross-section of hydrogen is dominated by

## 44:45

scattering right because the absorption cross-section of hydrogen is like two times 0.002

## 44:52

barns or something small right compared to its scattering cross-section that means sigma t

## 44:57

already is mostly scattering but mu bar is two-thirds

## 45:02

right that means that my my sigma tr is like one-third of what it started with which means

## 45:09

that my diffusion coefficient is how much larger three times larger right so if sigma t is reduced

## 45:18

by a factor of three to make sigma tr that means that my effective mean free path has been amplified

## 45:24

by three times which means if i'm a hydrogen i'm i'm moving a hell of a lot farther from my origin

## 45:31

than i would have otherwise because when i have a

## 45:34

non-zero mu bar that means that i am forward peaked that means the remember if my my scattering

## 45:41

cosine is one that means that i'm going in the same direction i started with right so if i'm

## 45:46

not zero zero would just mean that i could go in any direction but if it's forward peaked it's it's

## 45:51

close to one that means on the average i'm going to keep going forward farther than i would

## 45:56

otherwise right that makes a huge difference why well for a light water moderated

## 46:04

nuclear reactor that means neutrons entering into that moderating region will tend to go further

## 46:10

than they would otherwise which means that they probably have a likelihood of going right back

## 46:14

into the fuel now of course things work out but it's it's a detail that has to be accounted for

## 46:19

right that's a that's a that's a big a big thing uh to account for anyway so that's this this mu bar

## 46:26

and that this is the diffusion coefficient this actually comes out of neutron transport theory we

## 46:31

can show that i'll i'll

## 46:34

maybe try to illustrate it with some pictures when we get to the lecture on validity of diffusion

## 46:39

but that's that's where it comes from okay in any case once we have that then we get the diffusion

## 46:50

equation right that's kind of the final takeaway from that section and if you take a look at that

## 46:58

compared to what i gave you before you even stepped into the room you can start to see even

## 47:02

more similar things right remember last time what we did

## 47:07

when we talked about time stuff is i just deleted all the space stuff well now i can delete all the

## 47:12

time stuff and delete the energy stuff and then we're to 6 12.

## 47:19

so um just a couple comments on on the homework problems now one of them there are two of them and

## 47:27

i'll bring them up here in my code okay so we've got this question

## 47:39

right uh let me blow that up so that people can actually see it okay we've got a non-multiplying

## 47:46

homogeneous system defined over the cube negative one to one negative one to one negative one to one

## 47:52

okay and this is on canvas so you can take a look at it too what i'm saying is the flux is a certain

## 48:00

function of x and y and then i ask you this scary sounding question of what's the source
distribution

## 48:07

okay

## 48:09

raise your hand if you don't know how to start that problem

## 48:17

okay so what do you think you need what are the inputs that you have what equations do we have

## 48:29

we have the neutron balance equation we have the neutron diffusion equation

## 48:33

right if i if i gave you the flux in this region right let me see if i can

## 48:41

uh open up

## 48:45

you know this um let me get this right into the notice is that it's going to go to something

## 48:55

where here we go use this right so if i have uh okay so what i'm telling you is that we have

## 49:03

phi of x and y is equal to some some function right what was it what was the actual function

## 49:10

it was like a polynomial right

## 49:14

if this was 1 minus x squared, 1 minus y squared, okay?

## 49:19

If I know what the flux is,

## 49:21

that means that maybe I already solved the diffusion equation, right?

## 49:28

So what can I do with that flux and the diffusion equation?

## 49:33

Remember, the diffusion equation for this case

## 49:35

where I don't have fission looks like minus plus sigma.

## 49:49

I got my phi.

## 49:51

And then I have a sigma a phi is equal to s.

## 49:59

And all these are functions of x and y, right?

## 50:03

That's my diffusion equation, right?

## 50:05

Without the fission term.

## 50:09

I guess the book likes to put the triple primes for things.

## 50:13

So I'll be consistent there.

## 50:14

So if I know my diffusion coefficient and it's constant,

## 50:20

and I know what my sigma a is and it's constant,

## 50:23

okay, I can write this actually slightly easier.

## 50:27

This ends up being this.

## 50:29

I can call that xy plus sigma a times phi of xy

## 50:37

is equal to whatever my source term is, right?

## 50:41

So I've given, usually, you're given an equation to solve, right?

## 50:47

What I've done for you is I've given you the solution

## 50:50

and parts of the equation,

## 50:52

and you're actually just,

## 50:53

coming up with the other part of the equation, okay?

## 50:56

So what things do you know, right?

## 50:59

This is what we have, right?

## 51:02

That's our diffusion equation.

## 51:05

You know what d is, right?

## 51:07

Because I say that you have the diffusion coefficient d.

## 51:10

We don't have a number.

## 51:11

You don't have to use numbers here.

## 51:12

And you have sigma a and you have phi.

## 51:16

What's missing, huh?

## 51:21

Just the right-hand side.

## 51:22

But the right-hand side shows up only

## 51:25

on the right-hand side.

## 51:26

You have everything on the left-hand side.

## 51:28

So what you're doing is evaluating this thing.

## 51:33

You're plugging in the flux to the left-hand side

## 51:35

of the diffusion equation.

## 51:36

Out pops whatever the source term must have been.

## 51:39

I picked this problem, I didn't, I created this problem

## 51:42

because I thought it would be a pretty straightforward way

## 51:45

of actually writing down the diffusion equation

## 51:47

and doing something with it, right?

## 51:48

The second problem is then do the integration

## 51:50

over the sides and so forth.

## 51:52

I'll let you puzzle that one out a little bit

## 51:54

and you can figure it out.

## 51:54

So I'll let you puzzle that one out a little bit and you can figure it out.

## 51:55

You can come in and ask questions on Friday.

## 51:57

But this idea of, hey, let's choose what the flux is,

## 52:02

put it into our equation,

## 52:04

and then getting the right-hand side,

## 52:06

this is a really, really important tool

## 52:09

in numerical methods called

## 52:13

the method of manufactured solutions.

## 52:16

Basically, if I have a set of equations

## 52:19

or something that I'm solving numerically

## 52:21

or in some way,

## 52:23

if I,

## 52:25

fake a solution,

## 52:26

I say, this is my solution.

## 52:28

I can get a right-hand side that should,

## 52:31

if my numerical method is a good one,

## 52:34

reproduce the solution I put into it.

## 52:37

So I can come up with arbitrary solution.

## 52:39

Basically, it's a good way to verify a numerical method works,

## 52:42

but it's not a bad way to verify that you understand

## 52:45

how to write down the equation in the first place, right?

## 52:49

So this has nothing to do with numerical methods,

## 52:51

but the process is very similar to this thing called,

## 52:54

manufactured solutions,

## 52:55

which is a technique in computational verification,

## 52:59

which is something I'm marginally interested in.

## 53:02

Okay, raise your hand if you have no idea how to start.

## 53:07

Boom, I think we made some progress.

## 53:09

I will see you on Friday.
