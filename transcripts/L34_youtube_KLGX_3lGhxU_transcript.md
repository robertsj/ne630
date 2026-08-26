# L34 Local Audio Transcript

Course: NE 630

Playlist source: https://youtube.com/playlist?list=PLy481lNHlnHoEO95vM-xYX2bydD25v20L

Video: NE 630 - Lesson 34

URL: https://www.youtube.com/watch?v=KLGX_3lGhxU

Video ID: KLGX_3lGhxU

YouTube upload date: 20231115

Duration: 56:31

Transcript source: Local faster-whisper transcription from YouTube audio.

Whisper model: large-v3; detected language: en.

Generated: 2026-06-28

Note: This transcript is machine-generated from audio and lightly wrapped only. It should be reviewed before being quoted, published, or used as polished lesson text.

Requested language: en

## 00:00

All right, so let's go ahead and get started.

## 00:44

We're going to continue from what we covered last time, which was continuing our discussion

## 00:51

of neutron diffusion, specifically in slab geometry.

## 00:55

And what we covered specifically was the set of boundary conditions that we have available

## 01:00

to model things that are physically relevant.

## 01:05

In addition to that, we looked at continuity conditions, which is something that we have

## 01:09

to apply if we're going to model anything with more than one region, right?

## 01:12

We need a way to connect the solution from one region to another, and so we have to preserve

## 01:17

continuity of the flux and of the current across those interfaces.

## 01:22

So the continuity conditions are also called interface conditions.

## 01:27

So what we'll do specifically today is add back multiplication, meaning that nu sigma

## 01:32

f is no longer assumed to be zero, right?

## 01:35

And it doesn't change the structure of the equation too much, but depending on the value

## 01:40

of nu sigma f.

## 01:42

Or rather, k infinity, the solution changes, right?

## 01:46

And in fact, we're actually constrained.

## 01:48

There are certain values that will let us not be able to solve the equation, right?

## 01:53

And there's a physical meaning for that.

## 01:55

So this is sort of the first time, I mean, we've seen a little bit of physics as we've

## 02:00

played with the diffusion equation, things like balancing reaction rates to leakage rates

## 02:04

and so forth, but it hasn't felt very reactor-ish.

## 02:08

Today, we actually get to see for the first time how the diffusion equation,

## 02:12

maps on to a reactor, a critical reactor, all right?

## 02:17

So next time, we won't have live class, right?

## 02:21

I assume that many folks will be traveling.

## 02:23

I'll be traveling, and this gives me a little bit of leeway.

## 02:27

So what I'm going to do is, what I'm hoping to do, we'll see how it actually works out,

## 02:33

is I'm going to do a video where it will be maybe five to 10-minute chunks, right?

## 02:40

Where after each chunk, there will be some sort of,

## 02:42

exercise that fills in the blank, as it were, and then that will be the home one for that lesson.

## 02:47

The reason I'm, I mean, it helps in this particular calendar case, but the topic that we're going to

## 02:53

do is sections 7.1 through 7.3 of the book.

## 02:57

7.1 and 7.2 are like throwaway sections.

## 03:00

It's, you know, introductory stuff.

## 03:01

So 7.3 is where the critical finite reactor is introduced, and specifically, it's for the case

## 03:09

of cylindrical geometry with a finite reactor.

## 03:12

So it's actually two-dimensional, which means that it's not an ordinary differential equation
anymore.

## 03:19

It's a partial differential equation, right?

## 03:22

And so, the solution technique for that is called something, it's called the separation of
variables,

## 03:30

right, where you make an assumption about the flux shape as a function of z and as a function of r.

## 03:34

That's not something that, I kind of forgot that that's in the book and that's the way it's
described.

## 03:39

So I'm going to sort of walk you through it.

## 03:42

Who's seen separation of variables?

## 03:45

I mean, I think it pops up sometimes.

## 03:47

I mean, hell, even if you, if you go back to NE495, in the book, there's separation of variables in
the early stage

## 03:54

in discussions of Schrodinger's equation, but I know that's not, like, covered in any real depth.

## 04:01

So we'll go through it.

## 04:02

In the end, the separation of variables technique basically splits the equation into two ordinary
differential equations, right?

## 04:09

So all the mechanics that we have for solving OD,

## 04:12

these will be there for us to solve that case as well, right?

## 04:17

So there are kind of two things that make it sort of a new topic.

## 04:21

One is this multivariable thing where we have to do separation of variables,

## 04:24

and then also the cylindrical coordinate system, which leads to a differential equation that is
different in structure from the slab case.

## 04:33

Remember, we like the slab case because it's a second-order linear ordinary differential equation
with constant coefficients.

## 04:41

So all of our,

## 04:42

all of our solutions are exponentials, right?

## 04:45

That makes it super nice.

## 04:46

When we go to cylindrical coordinates, we don't get exponentials anymore.

## 04:50

Sadly, what we get is this monstrosity known as the Bessel function.

## 04:54

And I'm going to do my darndest to make it not seem like some sort of black box is spitting out
these solutions.

## 05:00

I hate that.

## 05:01

You go to a textbook or you go to a lecture, it's like, and the solution is this.

## 05:05

So just plug and chuck.

## 05:06

Well, I'm going to spend a little bit of time trying to motivate where these nasty things like
Bessel functions,

## 05:11

and I'm going to spend a little bit of time trying to motivate where these nasty things like Bessel
functions,

## 05:12

or for the spherical case, spherical Bessel functions, even though that's not, I think, even pointed
out in the reading here,

## 05:17

or any number of other functions that might come up, right?

## 05:20

The air function, for instance, in some heat transfer applications, there's a way to get all these
functions.

## 05:25

They all come from, from a certain solution technique.

## 05:28

So I'm going to try to see if I can fit that in, in a sort of reasonable amount of time.

## 05:33

And if I, if it looks like it's going to take, you know, a full lecture in and of itself,

## 05:38

then I will probably just pull the, oh, here's the,

## 05:42

here's the solution card and we'll see.

## 05:44

So it's kind of a balance,

## 05:46

which is probably the same sort of balance question that instructors everywhere have to consider.

## 05:53

Or maybe they don't consider it. I'm considering it. We'll see.

## 05:55

Anyway, so no, no live class for next time.

## 05:59

And then the office hours tomorrow, I'll do that via Zoom, right?

## 06:03

And I'll send out a message if for some reason I'm not going to be able to connect at the normal
time.

## 06:07

But otherwise, it'd be 1230 to 130.

## 06:10

So you're reading for Friday at 7-1,

## 06:12

to 7-3, I'll have that page up sometime before then and link to any additional resources.

## 06:20

But I'm hoping that the video will be self-contained.

## 06:23

OK. Any questions from the material last time? Lesson 33.

## 06:30

I'm going to review a little bit, but yeah.

## 06:32

Will there be a reading due Monday following break?

## 06:39

Yes, probably.

## 06:42

And it'll be whatever the next section or two is of the book.

## 06:46

Will you put that in the video?

## 06:47

Yeah, I'll make sure that it's it.

## 06:49

I'm hoping that with this little break.

## 06:52

So obviously last week we were dealing with some some test stuff.

## 06:56

I've been trying to sort of shake things up a little bit to get folks that, you know,

## 07:03

so basically to connect us better in time.

## 07:05

And I think that's working out right because I've already got the homework that you've been you
turned in homework 31 last Friday.

## 07:12

that's graded now right and i'll be able to jump on 32 very quickly i think there's one student who

## 07:17

asked for um an extension for personal reasons so that that should be all tied up today then 33.

## 07:23

um so i'm thinking that over the break i'm gonna have plenty of time to to just knock out all the

## 07:28

rest of the semester stuff so we'll have a pretty clear pathway to the end of the um semester um

## 07:34

did i answer your question yeah yeah so any technical questions from last time or the

## 07:39

homework that's due today yeah i think most of us have questions about the homework at each

## 07:45

night okay do you have a specific one that you can talk my way you know like your uh

## 07:51

it's like your uh flux equation or

## 07:59

let's see first of all let's maybe open up the modules get rid of that

## 08:11

i did it all right so lesson 33. okay so it was finding the equations on the reflector side

## 08:24

because we did we did an example of the backing boundaries but we never did any

## 08:29

reflector like examples right okay um yeah so let me

## 08:48

so i have a little bit more that i i can talk

## 08:51

about for yeah i i guess just let me um go back here and i can sketch out what you would do for

## 09:03

that case okay so the question is how do you handle that reflecting condition right so um

## 09:11

let me make sure i see so that's uh we've got the two region case right and so reflection is in

## 09:21

the in the left region the first region okay so you know if we have zero

## 09:29

a is that a over two to a then yeah right okay so this is this is our reflection this

## 09:37

is vacuum over here right is that correct and then this is a fixed source term in this region

## 09:47

and this one it has i don't know s is equal to one and this is s equals to zero

## 09:51

is that correct okay so um what we have in each region is a solution that looks like um

## 10:05

in general it'll be obviously that you know in a region uh

## 10:11

called this region one right we would have c one e to the x over l plus c to e to the minus x over l

## 10:23

plus the particular solution which if i'm remembering off the top of my head would be

## 10:28

one over um d times is it l squared over d trying to remember what's that isn't that one

## 10:42

uh this is this is the times the source term but if the source is one is that but it's a

## 10:48

constant right so i could whatever it is it's this is vp so the question is how do you handle

## 10:55

the reflection right so what is the reflection uh condition yeah so in in essence what we're

## 11:04

saying in reflection is that there's no net current right whatever current whatever neutrons

## 11:08

come go out of that surface we have the same number coming back in which yeah maybe it's not

## 11:14

the same neutrons that would go out that come back in but effectively every neutron that goes out is

## 11:19

reflected by a mirror and it comes back in so that that's why we call it reflection so in this case

## 11:25

you would have uh the if so if the current so the current is equal to minus d d phi d x right but

## 11:34

because the diffusion coefficient is constant right it we can just say that the flux derivative

## 11:44

is equal to zero right so if that's the case and because it's only in region one that we're

## 11:51

talking about it has nothing to do with whatever the flux is in region two right so

## 11:55

in region two we would have the flux is equal to some other constant c3

## 12:03

plus c4 e to the minus x l right uh i guess if the l's are different then i would have to do

## 12:13

this as well okay right and there would be no particular solution because like that region

## 12:22

is sourceless right so really what we're doing is setting up an equation that uh helps us find what

## 12:28

we have the blended

## 12:40

mustn't or doesn't include the

## 12:43

inverse equation our

## 12:51

i

## 12:53

v

## 12:54

to

## 12:56

e

## 12:56

f

## 12:57

plus if you are

## 12:58

going to get an equal to zero yet is the derivative is set equal to zero so we have a c1 times one
over l1 e to the zero over l i plus c2 and then we have a minus l uh one over l1 that comes down and
e to the minus zero over l that comes down and e to the minus zero over l 1 then we

## 12:58

i, and that is equal to zero, right? And so simplifying that a little bit, we have

## 13:04

1 over li c1 plus minus 1 over li times c2 is equal to zero, right? Now, I'm not sure exactly

## 13:23

where, when you ask about this, did you get to this point, or is this sort of the example that

## 13:30

inspires you to move forward? Yeah. Okay. Any further questions on this?

## 13:49

I'm happy to stay on it or focus on it a little bit more.

## 13:55

I think the other thing I'm running into is taking, you gave us your example code in the

## 14:02

lecture, and it's only dealt with that. You know, trying to translate that into

## 14:07

something else. So, I think that's a good point.

## 14:07

Yeah. So, I mean, I caution you with the SymPy stuff. So, SymPy is something that I'm

## 14:26

primarily using to help my, like, the presentation out, right? Because it's very easy for me to

## 14:32

evaluate something like I just did by hand, right? You can certainly use it if you feel

## 14:37

comfortable and you're playing around with it. By all means, take it all the way home using SymPy.

## 14:43

It's not a requirement. And if you're not sure about what you're doing by hand, then don't use

## 14:49

SymPy, right? This is an important thing about using computers to help us. Computers should

## 14:54

help us do time-consuming things more quickly, but they should not be used when we couldn't

## 15:01

spend the time to do it by hand, right? So, there's a lot of algebraic stuff that I wouldn't

## 15:07

want to do.

## 15:07

But I know that I can do it, right? Like, even with some of these problems, looking

## 15:12

at the two region ones, it's like, oh, gosh, I don't want to do that, right? Because I've

## 15:17

done it before. You know, it was a long time ago. I've done it in this class. I've done

## 15:21

it in other classes that have similar things. I would never want to use the symbolic stuff

## 15:25

until I proved to myself that I could do it. Now, I'm making an assumption that you've

## 15:31

been able to solve some algebraic equations before. Definitely don't just try to copy

## 15:36

and paste my examples that I do.

## 15:37

I mean, for number one, I'm human. So, if I give you an example in class, it could have

## 15:43

mistakes in it, right? And then if you're playing this game of, well, this is his set

## 15:48

of equations for this vacuum here and vacuum here. I'm trying to translate it. When you

## 15:54

describe it like that, it means that you're not sitting down and actually writing the

## 15:58

equations and understanding what's happening with the solutions that you get, right? So,

## 16:03

you get the homogeneous solution, the particular solution. Those, I feel like everyone should

## 16:07

be able to do. And you probably could have done that before you got in here. It helps

## 16:10

to see it again and review it. But then, setting up these boundary conditions which is probably

## 16:16

different from something you've done before. I know you've done initial conditions, right?

## 16:20

But this, the idea of a two-sided problem, it's called a boundary value problem. This

## 16:26

is usually like a set of applications that shows up toward the end of a differential

## 16:31

equations book, which means that in a typical class that you have, you might not get to

## 16:36

the end of the book, right? You might get to the second part of the book and you reach

## 16:37

that 12 minutes of an answer. But then, you do, again, you have to figure out what the

## 16:37

Right. You have these massive textbooks often that you don't cover the last part of it.

## 16:41

So the actual boundary value problem application tends not to be covered as much, which is why I'm
kind of focusing on setting up these equations as much as I am.

## 16:51

So you need to be able to set up the equations, writing them down. Right.

## 16:54

So if I say, for instance, in fact, this is a good segue into a review of 33. Right.

## 17:03

So I we this is this set of slides from last time we went through most of this first example.

## 17:09

Right. The single region and the purpose in this example was to illustrate how you would apply these
in this case, the vacuum boundary condition.

## 17:17

So it's easy enough to say the flux is equal to some number at some point X. Right.

## 17:23

Phi of A is equal to zero, for instance. That was our kind of quasi vacuum condition. Right.

## 17:28

And it turns out that's not a great approximation for vacuum.

## 17:32

And I'll show you.

## 17:33

Right. If you haven't already seen the slide. So as soon as I was done with the lecture, I went and
wrapped up the example and then completed a second work one.

## 17:42

OK, so if you haven't seen it, I'm telling you now that that there's more in here that you can use.

## 17:47

And let's take a look. Right. So when we so in this one single region case, we end up with a system
of equations.

## 17:57

Let me blow that up a little bit. OK. Right. This is our system of equations.

## 18:03

Right. So this is our system of equations for the single region case, we get a C1 and C2, whether or
not it actually helps put it into a matrix for me, you simply hear it's two by two years like that,
that you solve for C1, plug it in, get C2, boom, right, that that should be straightforward enough.

## 18:17

It helps, though, to kind of see it in this form, because then it's nice and clean. You can write it
down.

## 18:23

What's more important for that problem is when we get to see what was this one.

## 18:29

This was the the partial current condition. Right.

## 18:31

Right. The big thing is, once we plugged it in, we can plug it back in.

## 18:32

Right. The big thing is, once we plugged it in, we can plug it back in.

## 18:32

Right. The big thing is, once we plugged it in, we can plug it back in.

## 18:32

Right. The big thing is, once we plugged it in, we can plug it back in.

## 18:32

See, once we plugged in the numbers that I originally gave you, the fluxes look very different,
right?

## 18:37

Right. The big thing is, once we plugged it in, we can plug it back in.

## 18:37

Right. The big thing is, once we plugged it in, we can plug it back in.

## 18:37

Right. The big thing is, once we plugged it in, we can plug it back in.

## 18:37

In this case.

## 18:38

Right. So we see here the blue curve, that's 0 flux, right?

## 18:41

We get this something that looks kind of like a cosine or parabola.

## 18:44

It's hard to say exactly, right?

## 18:46

But when we use the same numbers and apply the partial current condition,

## 18:51

look at that that's significantly different OK?

## 18:55

And the reason for that is if we are forcing the flux to 0 at a boundary,

## 19:00

what we're effectively

## 19:02

doing is forcing there to be some negative neutrons entering the building to bring down

## 19:07

that flux, right? Non-physical, right? But effectively, if I were to compute the, we know

## 19:14

how to compute partial currents. Partial currents means the number going in one direction or in the

## 19:18

other direction. And if I compute the partial current for this blue curve at x equals zero,

## 19:23

I actually have a negative number of neutrons going into the slab, right? Now, my purpose in

## 19:28

maybe using a zero flux was to approximate a vacuum condition where I have zero neutrons,

## 19:34

right? Effectively saying that I don't have a positive number of neutrons going in. But by

## 19:39

setting it to zero, I'm actually getting this weird effect of having a negative number to come

## 19:43

in, which is obviously bonkers, right? So it's not terrible, though, if the size of the problem,

## 19:49

right, the mean free paths of the slab is very large compared to the amount of leakage that you

## 19:55

have. So if I take the same problem, but I extend it from,

## 19:58

oh, what was I using here? 10, right? So this was a slab of 10 centimeters. If I increase that to,

## 20:07

let's say, 50 centimeters, I think is what I'm doing here. Yeah, 50 centimeters.

## 20:13

Then I get a picture that on the whole looks a lot better, like a lot more physical.

## 20:19

But still, I have a zero flux that is driving this down. So there's a huge

## 20:23

change in the curvature toward the boundary, which means that I'm going to be

## 20:28

wrong.

## 20:28

I'm going to be wrong with my leakage, right? The system itself will be balanced, right? So the

## 20:33

amount of neutrons, the number of neutrons that leave from either side will be balanced by the

## 20:38

number of neutrons introduced by the source term and then the absorption. It's just the shape of

## 20:43

the flux is different. So I have less absorption, right? Because this blue curve, if you think about

## 20:50

the integral of the blue curve, tells me what my absorption rate is when I multiply it by my

## 20:55

constant sigma A. And because the blue curve has this forced,

## 20:58

shaped down to zero, I'm going to have less absorption, which means I have more leakage, right?

## 21:05

Anyway, but in the middle, there's another little sort of something that I could feasibly ask on an

## 21:12

exam. When I look at that solution, what is it approaching in the middle for either of these

## 21:17

curves, meaning away from the boundaries where any of this leakage business is not

## 21:21

impacting the solution, right? What number are we hitting in the middle for the flux?

## 21:32

What does it look like?

## 21:32

Anyway, numerically, what's that asymptotic value in the middle away from the boundaries?

## 21:41

Nine, I would say it actually approaches 10. And there's a reason for that, okay? If we are in the

## 21:48

middle of the slab, right? Up above, I say what the mean free paths is, right? So if our diffusion

## 21:55

coefficient is one, then our total cross-section is one-third inverse centimeters, which is one-
third

## 22:02

which means my mean free path is three centimeters, okay? That means that if I'm a neutron that's
born

## 22:08

at A over two, right? So X is equal to 25. I am several mean free paths away from the boundary.

## 22:16

So what that means in practice is that if I'm a neutron born in the center of the slab,

## 22:20

the most likely thing that's going to kill me is absorption, right? I'm not going to have a good

## 22:24

chance of getting to the boundaries. And what that means is that the solution is dominated by

## 22:30

absorption as opposed to leakage.

## 22:32

So if I take the diffusion equation and I look at it, right? So I have the diffusion equation,

## 22:41

it's minus D, D, you don't have to write this down, this is just for illustration, okay? I have

## 22:48

this term, right? Now the leakage is embodied in this term and it's applied at the boundaries,

## 22:54

right? But if I'm away from the boundaries and I don't have, and my medium is homogeneous and my,

## 23:02

source term is constant, everything is uniform. There's no spatial change in any of that stuff.

## 23:07

The only thing that's driving the spatial change here is what's happening at the boundaries.

## 23:11

And what I'm saying is if I'm many mean free paths away from the boundaries,

## 23:14

then I'm not going to have any impact from the boundaries. And if everything else is

## 23:18

spatially constant, then my solution two should look spatially constant.

## 23:23

And so if I take my diffusion equation and I get rid of the stuff that looks spatially constant,

## 23:28

what do I, what am I left with? I get rid of this because if that's not spatially,

## 23:34

constant, then I'm left with my flux is equal to my source term over sigma A, right?

## 23:47

And if you remember our particular solution was equal to, what was it? It was L square times S

## 23:57

over D, right? Well, what, what is L? L, yeah, square root of D over sigma A. So

## 24:10

aren't these two things equivalent?

## 24:14

What that means is if, if everything is basically constant, right? Like my constant

## 24:20

homogeneous, I guess that maybe this works for non-constant source too, but if we have a uniform

## 24:25

source, constant materials, and our slab is very large, then in the middle of the slab away from

## 24:31

the boundaries, the solution is dominated by the particular solution, which in this case,

## 24:38

it's just a flax. So if I take my diffusion, or sorry, if I take my absorption coefficient

## 24:44

and my source term for,

## 24:46

this problem, right? What do I have for my numbers? I have 0.1 and I have one. Well,

## 24:52

what's one divided by 0.1? It's exactly that 10 that I'm approaching in the middle, right?

## 24:57

This is a great sanity check for when you're solving your problems. If you're not capturing

## 25:02

that behavior in the middle of a slab away from the boundaries, you're probably making a mistake.

## 25:08

Okay. Now do we hit that same asymptotic value in the middle of the slab for the smaller version?

## 25:16

Well, it's starting to approach it for the zero partial current case, but definitely not for the

## 25:20

zero flux. And that's, I mean, think of it this way. If we're at 10 centimeters big and our mean

## 25:26

three path is three centimeters, then a neutron born in the middle only needs to hop twice on the

## 25:31

average to get out. So it's going to have a pretty good shot of being absorbed, of leaking instead

## 25:38

of being absorbed, right? So you've got to be seven mean three paths away from the boundary to

## 25:44

be able to even start seeing that.

## 25:46

Asymptotic approach, right? So any questions about that? This is the sort of thing that

## 25:58

you can only start to really think about these things like this asymptotic solution once you

## 26:06

start seeing the solution. And you can't start seeing the solution until you set up your boundary

## 26:13

conditions, apply them, find your constants, and actually get to the plotting. So it might seem

## 26:21

like a little bit of computation for the fun of computation. It's not. I'm a visual learner myself.

## 26:31

I mean, you can look at the math and you can write down the equation like I did and motivate that,

## 26:35

yeah, the solution ought to look like the particular solution, but I don't think it

## 26:38

drives home for me anyway until I see it, right? And the only way you can see it is if you plot it.

## 26:43

So hopefully that adds a little bit of motivation.

## 26:49

Now, for this...

## 26:51

The second example, this is the one that I didn't do in class last time. I did complete it,

## 26:55

but it's worth kind of looking at what I'm doing with it, okay? So I set up the process in the

## 27:02

same way where we end up with a homogeneous solution in each region, just like I was

## 27:07

describing in the handwritten stuff, okay? I get the boundary conditions, right? So I have

## 27:12

partial currents and then I have the net currents in each region. And so then I use those things to

## 27:19

do the boundaries, right?

## 27:21

In this case, I have my rightward partial current on the left side is equal to whatever my source

## 27:27

function is, right? In this case, I'm pushing neutrons into this two-region slab, right? I

## 27:31

don't have a source from within. And then the right condition is the vacuum where I'm setting

## 27:35

the leftward partial current to zero. And then I have my two continuity conditions, right? And each

## 27:41

of those conditions, when blown up, like actually written out, looks like this. So this is the step

## 27:48

that... This is what I'm talking about. You should be able to do this. You should be able to do
this.

## 27:51

You should be able to write down these equations, okay? So once you have the general solution in

## 27:55

both parts of the slab, both regions, you should be able to substitute them into those boundary

## 28:00

conditions, whatever they are, whatever they happen to be. It's just taking some derivatives,

## 28:06

right? It might look a little messy because depending on the number of regions we have, but

## 28:12

you should be able to do this, okay? That's four equations for the four unknowns. Is that

## 28:17

necessarily trivial to solve? Absolutely not. This is...

## 28:21

That's the sort of stuff that I would not want to sit through and do the algebra for,

## 28:24

right? Which is why I'm not having you do it explicitly. What I am having you do though

## 28:29

is put it into a matrix form, right? Because you can take all those. You can separate the C1,

## 28:35

C2, C3, C4. And I would... Maybe it's not trivial, but I think it's trivial to write it in this
form.

## 28:43

Why do I want it in this form? Because once you've separated out the C1, C2, C3, and C4,

## 28:49

and you have just these...

## 28:51

Coefficients. If I give you what D1, D2, A, L1, all that stuff is, this is just a four by four

## 28:57

matrix, right? And when I suggest using NumPy to solve it, it's not... I'm not asking you to do

## 29:03

anything weird with NumPy. I'm literally saying make a matrix in NumPy, right? Or MATLAB.

## 29:10

I don't know if you have another place where you put matrices together. I know if you've had

## 29:14

MATH 551, you can use MATLAB for this sort of thing, correct? Raise your hand if you disagree.

## 29:21

With that statement. I'm pretty sure if you do anything with MATLAB in 551, it's often putting

## 29:29

together rows or columns to make a matrix, right? To solve an equation. Math is there to show you

## 29:36

how to put the numbers in and get the numbers out. An engineering class or a physics class is
telling

## 29:42

you how you get the numbers in the first place to put into those equations. So yeah, that's that.

## 29:50

And then when you get that out,

## 29:52

you have these four numbers for the coefficients. And at that point, what are you doing? Well,

## 29:58

for instance, my general solution in my second region was C3 times this exponential plus C4

## 30:04

times that exponential. You know what the exponent is because you've already been given L1 and L2.

## 30:09

Voila. Now you have an explicit form for what the flux is. And so in this case, I'm making that,

## 30:15

right? So I have my first region flux. I have my second region flux. I'm putting in the numbers

## 30:20

that I've just defined here.

## 30:22

Same thing that you would have for the homework. And then in this case, I'm plotting it, right? And

## 30:27

I'm breaking it up into the first region and then the second region. I think the only thing that

## 30:32

differed from what I had done before is maybe I'll have to upload these again. I think I had A plus
B

## 30:40

as the right boundary, which was just me writing too much when I sketched the model. But all the

## 30:46

stuff below that was consistent. So I don't know. Does that help describe what I'm after?

## 30:52

Right. It's not like the SymPy stuff is great because, I mean, hopefully it seems like some of you
are really getting into it.

## 31:00

When I was an undergrad, the class that we had that was kind of like ME 400, like my first
programming class,

## 31:09

it was probably two thirds MATLAB, right? So my first programming language outside of like two
lectures of basic in high school was MATLAB, right?

## 31:18

And then the last third of the class was using software called Maple.

## 31:22

I don't know if you've ever, anybody here of Maple?

## 31:25

Maple is a symbolic computational tool, similar to SymPy, but $1000 or something, unless you have a
student license.

## 31:33

Wolfram Mathematica is like another, I guess, those two compete in the commercial space.

## 31:39

SymPy is free, obviously, and it definitely lacks some of the power.

## 31:45

I've noticed there's some things that I could do in Maple. I got very, very good at Maple.

## 31:49

I thought it was an outstanding tool.

## 31:52

Mathematica is also very good.

## 31:53

Just never learned it quite as well.

## 31:56

That was what that class was.

## 31:57

And when I taught ME 400, I brought some of that experience into the class where I could.

## 32:06

And obviously, that's not something that you all had in your version of ME 400.

## 32:11

So I'm exposing it to you.

## 32:13

But if you want to turn it into an actual problem-solving tool, that's something that

## 32:18

you'll have to come and ask me.

## 32:20

I can help.

## 32:21

But hopefully, we're going to get another class going that's already on the books.

## 32:25

ME 415, it's on the catalog, Introduction to Engineering in Houses.

## 32:30

I'm hoping to just reboot my old ME 400 curriculum with tweaks specific to nuclear folks and

## 32:36

start offering that on a semi-regular basis so that we can get some of these tools.

## 32:41

They're not critical.

## 32:42

They don't stop you from learning the material.

## 32:44

But they can enhance the experience significantly.

## 32:47

OK.

## 32:49

All right.

## 32:51

Any other questions related to Lesson 33 stuff?

## 32:56

So we've taken quite a bit of time on that.

## 33:03

I do have a dessert.

## 33:04

But I've got an example ready to go for the stuff for today.

## 33:10

Let me go ahead and get myself back over here.

## 33:16

OK.

## 33:16

So we've just talked about that.

## 33:17

We've got reflection and vacuum conditions and continuity conditions.

## 33:22

We've just looked at the Lesson 33.

## 33:24

Slides.

## 33:24

OK.

## 33:25

Now, when we bring back multiplication, in a sense, nothing actually changes.

## 33:33

The equations can be written down in exactly the same way.

## 33:36

It's just the interpretation of the equations and where they're valid for what values of

## 33:41

the coefficients they are valid changes a bit.

## 33:45

OK.

## 33:46

So how do we see that?

## 33:48

All right.

## 33:49

So if we have our neutron diffusion equation now in slab.

## 33:54

So we have our neutron diffusion equation now in slab.

## 33:56

And I'm going to show you a little bit of geometry.

## 33:57

I know the book in 6.5 and 6.7 was cylindrical.

## 33:59

And that's why I had you read 6.5 so you could see the cylindrical stuff in 6.7.

## 34:01

Sorry, not cylindrical, spherical.

## 34:02

I don't care about the spherical coordinate system for a class like this because there

## 34:06

are, as I said last time, very few applications where that system would matter.

## 34:12

So I'm going to present everything in terms of slab geometry.

## 34:15

OK.

## 34:16

So if we want to take this and put it in terms of in the same notation that the book uses,

## 34:21

we would have minus phi.

## 34:22

So we're going to have minus phi.

## 34:23

So we're going to have minus phi.

## 34:24

So we're going to have minus phi.

## 34:25

Second derivative.

## 34:26

Right.

## 34:27

And then we would have plus sigma a minus sigma f all over L squared times phi equal

## 34:39

to our source term over D. Right.

## 34:43

And it's this thing here, this term here that now presents a challenge, right?

## 34:49

Because when we had 1 over L squared, we had 1 over L and all of our exponents.

## 34:54

OK.

## 34:55

So now we have this additional term.

## 34:56

We're going to rewrite it like this.

## 34:57

We're going to say that this is equal to 1 minus K infinity over L squared.

## 35:12

Actually, yeah, so this should be times – I'm getting ahead of myself.

## 35:18

Not bad.

## 35:20

This is not right.

## 35:23

This should be D, OK?

## 35:26

Right.

## 35:27

So this is just going from this equation.

## 35:30

equation the original equation divide by d and we bring the new sigma f over to the left hand side

## 35:35

but if we take that whole thing then we get one minus k infinity over l squared where what is k

## 35:42

infinity when we have one energy group yeah okay so we can now call this thing i think the book

## 35:59

uses kappa for that um but to make it so because i don't think i can make a kappa look very much

## 36:06

different from from k i'm going to call this alpha squared right to abuse alpha a little bit more so

## 36:12

what we have then is is this equation okay now the solution to this looks the same as it did before

## 36:28

with it with l right so our we'll have a particular solution but the homogeneous solution

## 36:34

is

## 36:34

that we get will be a sum of exponentials right so we'll have e to the alpha x i could make

## 36:43

e to the alpha x plus c to e to the minus alpha x uh and then our particular solution will still

## 36:54

be constant now we could proceed with that right using exponentials has served us pretty well so

## 36:59

far there's nothing that that would stop us doing uh that but one thing that is a challenge is

## 37:06

if k infinity becomes greater so if k infinity is zero that's exactly the same as what we've been

## 37:14

dealing with right because the new sigma happens then zero but if we start bringing back

## 37:18

multiplication then k infinity can range from zero i guess really up to infinity although we

## 37:24

know that in practice you know maybe we think of a value of two or something is like a kind of a

## 37:30

practical upper bound to what k infinity could be right but if k infinity exceeds one then the

## 37:36

sine of this thing changes right and if you have one minus something bigger than one and you have

## 37:42

a minus and that's equal to a square that means that the alpha is imaginary right so if i have

## 37:50

alpha squared is equal to a negative number that means alpha is proportional to the imaginary number

## 37:55

i okay that doesn't break anything it just makes our interpretation of the solution a little bit

## 38:01

different right because if alpha is actually a real number times i then we have e to the

## 38:06

i times you know what whatever it is so i i could actually write this as um you know for it if

## 38:16

alpha is complex uh or let's say not complex let's say imaginary then we would have c1 e to the

## 38:31

i and then we could take the absolute value of alpha plus c to e

## 38:41

to the minus i times okay now when you see an e to the i times something

## 38:56

do you have any feeling for what that looks like it's not something unless you do maybe signal

## 39:05

processing you do a bit of work and controls maybe you'd have a feeling for that but when you

## 39:10

have an expression that looks like this right for whatever your solution is when you have an i in

## 39:18

the exponent

## 39:19

you should think not exponential decay or attenuation but now you should think oscillation

## 39:26

right so rather than having a damped system right which is well modeled by exponential attenuation

## 39:34

you now have an oscillatory system right this is a called a plane wave right it's a as a function

## 39:41

of x you just have this plane that's changing in magnitude okay we have different sets of

## 39:46

functions though that are more familiar for modeling exactly the same thing so i'm going to

## 39:49

talk about the same thing so we're going to go back to that same sort of oscillatory behavior what
are they

## 39:54

so signs and cosines right so when we have this case where alpha would be imaginary for the case

## 40:01

that k infinity is greater than one then we would go to a solution that looks like this we have

## 40:08

for the homogeneous solution we would have c1 times cosine of alpha times x

## 40:19

plus c2 times sine of alpha times x, right?

## 40:28

And this comes from Euler's equation or Euler's rule.

## 40:34

I guess I don't even know what it's officially called, right?

## 40:38

But it's e to the ix is equal to cosine of alpha x plus i times sine.

## 40:49

Of alpha x, right?

## 40:52

So you could use that relationship to kind of explain to yourself

## 40:56

why you would have the cosine and sine being these things, okay?

## 41:01

So for the case where k infinity is less than one, nothing changes.

## 41:05

We've just used now the kappa in the book.

## 41:08

I'm using alpha, so it's a little bit clearer when I write it compared to k.

## 41:11

But when k infinity is greater than one, then we have to make a switch.

## 41:16

And where does this actually show up, okay?

## 41:18

This actually shows up in the diffusion equation

## 41:22

for the case of k infinity greater than one

## 41:26

when we can now write phi double prime minus alpha phi

## 41:33

is equal to our source term over d, okay?

## 41:44

The difference now is we have a minus sign in front of the alpha, right?

## 41:48

For the case that k infinity is greater than one,

## 41:51

in which case we say that alpha is equal to k infinity,

## 41:55

sorry, alpha squared is equal to k infinity minus one over l squared, right?

## 42:02

So we're switching the order of k infinity and the one.

## 42:06

And just making that switch changes the sign of this thing.

## 42:09

And what function satisfies that equation?

## 42:20

What function has a second derivative that cancels itself out?

## 42:24

Sines and cosines, right?

## 42:26

So in this case,

## 42:27

phi of x is equal to c1 sine of alpha x plus c2 cosine of alpha x, okay?

## 42:43

Now, while I'm on this topic of using cosine and sine,

## 42:49

I do want to bring in another representation

## 42:51

that will work for the case that k is less than one, right?

## 42:57

So for the case that k is less than,

## 43:00

k infinity is less than one,

## 43:02

then we have alpha squared is equal to k,

## 43:05

one minus k infinity over l2, right?

## 43:08

And we're back to this equation,

## 43:11

phi double prime plus phi prime is equal to s over d, right?

## 43:20

I should say that this is the homogeneous solution, okay?

## 43:23

We already know that this is what we saw before.

## 43:26

This is exponentials,

## 43:27

but there's a different way that we can write it, right?

## 43:29

So instead of writing it as a sum of the exponentials,

## 43:34

we can say that phi sub h of x is equal to c1

## 43:40

times the hyperbolic cosine of alpha x

## 43:46

plus c2 times the hyperbolic sine of alpha x, right?

## 43:53

And that's something that's introduced earlier in chapter six.

## 43:57

I haven't used it because we haven't had,

## 43:59

a real,

## 44:01

there hasn't been a motivating reason to do so.

## 44:04

For this problem,

## 44:05

there actually is a little bit of a motivating reason, right?

## 44:08

Because we can then see the symmetry of the solution

## 44:11

when we go from k infinity less than one

## 44:13

to k infinity greater than one, right?

## 44:15

There's a one-to-one.

## 44:16

I don't want to use e to the i.

## 44:19

e to the i is something that I don't like, right?

## 44:21

So I'm going to use sines and cosines.

## 44:23

And in order to see how the solution looks without,

## 44:26

or in the case without cosines and sines,

## 44:28

we can use like the,

## 44:30

coshes and cinches,

## 44:31

I think is how the kids call them, okay?

## 44:34

So let's take a quick break

## 44:39

to go over to the Jupyter notebook, right?

## 44:43

So what I'm going to do is use this

## 44:46

because we don't have a whole lot of time left.

## 44:48

This will let me very quickly apply some of the solutions

## 44:51

or get quickly to some of the solutions.

## 44:54

We're going to consider a slab of material

## 44:56

from minus a over two to a over two, right?

## 44:59

With constant d, sigma a, nu, sigma f, and s.

## 45:04

But we're going to treat this as variable

## 45:06

because this is one, the thing that would actually bring us

## 45:09

from one version of the solution to the other, okay?

## 45:12

We're going to keep it easy.

## 45:13

We're just going to set the flux to zero at the boundaries.

## 45:15

That'll make things a little bit more compact, right?

## 45:18

And what we want to do is explore phi as a function

## 45:21

of k infinity, right?

## 45:23

Where that's the ratio of fission to absorption.

## 45:26

And we know that we can start at zero.

## 45:28

That's exactly what we've been doing all day.

## 45:29

And then we want to see what happens as we increase it.

## 45:32

And can we increase it indefinitely?

## 45:34

And I would say no, right?

## 45:37

So let me blow this up a little bit, right?

## 45:42

I'll go ahead and restart and clear the output

## 45:47

just so that we're all looking at things for the first time.

## 45:50

So I'm going to put it in terms of kappa at first, right?

## 45:54

So I'm getting in my symbols and defining my flux

## 45:58

and then defining my diffusion equation.

## 46:01

Right?

## 46:01

Simplified now because I'm using it in kappa.

## 46:04

And I'm doing it first for the case that by k infinity is less than one.

## 46:09

So the sign on the second derivative versus the function itself,

## 46:14

there's a flip in the sign, right?

## 46:16

They're not the same sign.

## 46:17

So this would lead us to the normal exponentials

## 46:20

or the hyperbolic sines and cosines.

## 46:22

So let me go ahead and solve it and we'll end up with the exponentials, right?

## 46:29

I don't want the exponentials.

## 46:30

No.

## 46:31

Not yet anyway.

## 46:32

So what I'm going to do is force SimPy's hand

## 46:35

and I'm going to say that my solution is actually equal to

## 46:40

an undetermined constant times the cosh

## 46:43

and then same thing for the hyperbolic sign, okay?

## 46:46

Same thing.

## 46:47

This c1 and this c1 would not be the same

## 46:49

because this and the hyperbolic cosine are not the same,

## 46:52

but they're arbitrary.

## 46:53

We'll solve for what c1 and c2 are, okay?

## 46:56

So we've got that form for the flux.

## 47:00

My boundary conditions are particularly easy, right?

## 47:03

It's just setting it to 0 at minus a over 2 and then at a over 2.

## 47:08

And I can do that and I can look at the coefficients.

## 47:12

What's nice is with this choice of functions, c2 is 0

## 47:17

and c1 is a pretty easy-looking beast, right?

## 47:21

It's just proportional to my source term, right?

## 47:24

The actual boundary conditions that lead to that are this.

## 47:28

Now, if you look at that, it's not obvious

## 47:30

that things would be so simple.

## 47:31

But if you add these equations, notice that the c2 terms cancel

## 47:37

out and you can immediately find c1 in terms

## 47:40

of this term divided by the cosine.

## 47:43

That's the hyperbolic cosine.

## 47:45

That's exactly what we just saw, okay,

## 47:47

for the first coefficient, right?

## 47:51

So that's cool.

## 47:52

Once I have those, I can plug it in.

## 47:56

And if you look at that solution, right,

## 47:59

I think Claire is going to be able to do this.

## 48:00

I think Claire might recognize it because that's equivalent

## 48:03

to equation 6 point, oh, I wrote that down, right?

## 48:08

6.30, the one with the hyperbolic cosine term, right?

## 48:15

It wasn't obvious how you get there, but that's equivalent

## 48:18

to that for the case that we would have to take a to b minus a

## 48:22

to a, and then that 2 would go away.

## 48:24

But if you look in the book, that's equation 6.30, right?

## 48:27

Just putting our exponentials in terms

## 48:29

of hyperbolic cosine.

## 48:30

And sine, which are defined in the back of the book, okay?

## 48:34

Boom. So that's the solution for k infinity less than 1, right?

## 48:39

We can substitute everything into kappa.

## 48:41

Kappa is just 1 minus k infinity over l squared.

## 48:46

Now, I'm going to do the second case.

## 48:50

Let me add in a new cell here, right?

## 48:53

I'm going to, I've written down a separate equation

## 48:56

for the diffusion equation.

## 48:58

Now the sine on the,

## 49:00

the flux itself and its second derivative,

## 49:02

now these are the same sign, right?

## 49:05

So now I'm explicitly keeping kappa to be a real number,

## 49:09

but now its definition is k infinity minus 1 over l squared,

## 49:14

right?

## 49:14

It's that, the flip of the sign in the original equation.

## 49:16

And so we've got to compensate for that here, okay?

## 49:19

So now if I solve that, I will end up from SymPy

## 49:25

with the exponentials with the i, and I don't want that, right?

## 49:29

I recognize it as being a plane wave.

## 49:31

It will be a solitory, but that's not the easy form to use.

## 49:35

So what I will do, one, what I could do is this.

## 49:38

I could say, all right, take my right-hand side.

## 49:41

Okay. That's the expression with the exponentials.

## 49:43

If I want, I could have SymPy rewrite this in terms of the cosine,

## 49:50

and it would give me this.

## 49:51

And if I, maybe if I simplify that, it would work itself out to something better.

## 49:56

We'll see if that does anything.

## 50:00

Nah.

## 50:01

Really?

## 50:02

I mean, it would, like the coefficients would work out,

## 50:04

but what I'll do instead is just force its hand

## 50:07

and say that my solution is equal to a sum of a cosine and a sine term, right?

## 50:12

Notice that the particular solution has a negative sign now, right?

## 50:16

Because of that flipped sign.

## 50:18

So with this, I end up with a solution that looks like that, okay?

## 50:25

That's my final solution.

## 50:27

The one thing that I want to look at,

## 50:31

very carefully here, is this term, okay?

## 50:36

This solution is that this ratio of the cosine is minus one.

## 50:42

The only thing that, let's see, right?

## 50:46

So let's consider this cosine right here.

## 50:50

It's a function of kappa.

## 50:51

Kappa is equal to k infinity minus one over L squared, right?

## 50:59

Now, for a specific value of k infinity,

## 51:02

and then hence kappa,

## 51:04

cosine of a times kappa over two can go to zero, correct?

## 51:12

Where does cosine go to zero?

## 51:17

Multiples of pi over,

## 51:19

odd multiples of pi over two, right?

## 51:22

Pi over two, three pi over two, five pi over two.

## 51:25

So the very first one that we would get to is pi over two.

## 51:28

So if I set kappa to be whatever number I need,

## 51:33

so that a times kappa is over two,

## 51:36

over two is equal to pi over two,

## 51:39

then this term goes to zero.

## 51:41

This divided by zero blows up,

## 51:43

and my solution goes to infinity, okay?

## 51:47

What value of kappa gives me pi over two?

## 51:54

It would have to be pi over,

## 51:58

let's see, a times kappa over two.

## 52:00

So a times pi over a over two would give me, right?

## 52:06

So that means that, let me go.

## 52:09

Go ahead and if you give me just two minutes to do this,

## 52:15

what we're looking for is when cosine of a times kappa over two

## 52:21

is equal to zero.

## 52:23

And that means that a times kappa over two

## 52:26

is equal to pi over two,

## 52:28

which means that kappa is equal to pi over a, right?

## 52:36

Well, remember what kappa is.

## 52:38

So kappa squared was equal to k infinity minus one over l squared.

## 52:47

So kappa is equal to the square root of k infinity minus one over l,

## 52:55

which means that pi squared over a squared

## 52:59

is equal to k infinity minus one over l squared, right?

## 53:05

And this is,

## 53:11

is our condition for criticality, right?

## 53:19

So you can take this,

## 53:20

make the connection to the book,

## 53:22

which will connect you to the non-leakage probability, right?

## 53:26

And if we know what the non-leakage probability is, right?

## 53:30

That's p and l, right?

## 53:33

Then we know that k,

## 53:35

the actual multiplication factor for the system,

## 53:38

which is equal to gains over all losses, right?

## 53:39

Which is equal to gains over all losses, right?

## 53:40

Which is equal to gains over all losses,

## 53:41

not just absorptions.

## 53:42

Now we're accounting for leakage.

## 53:44

K is equal to p and l times k infinity, right?

## 53:48

And so there is some k infinity

## 53:50

that will lead us to k is equal to one.

## 53:54

K equal one means that gains are exactly balanced by losses.

## 53:59

That means that if we're putting a source term in, right?

## 54:02

Gains from fission are exactly balanced by losses

## 54:06

from absorption and leakage.

## 54:07

That means that if we have a source term driving it,

## 54:10

our solution would keep going up, right?

## 54:13

If you keep adding neutrons to a critical reactor,

## 54:15

the population has to keep going up

## 54:17

and it does so linearly, right?

## 54:19

Which means that there is no solution

## 54:21

for the steady state problem, right?

## 54:23

By definition, the critical reactor with a source term

## 54:26

cannot have a steady state population.

## 54:28

We already saw that in the time domain, right?

## 54:31

That's exactly what neutron kinetics was about.

## 54:34

What we're doing here is doing everything in steady state

## 54:38

until we get to k equal one, right?

## 54:39

Until we get to k equal one, right?

## 54:40

In which case we, by definition,

## 54:42

can't have a steady state with our source term, right?

## 54:45

So that's why we see the flux blowing up.

## 54:49

There's an example in the book that shows that.

## 54:51

In the homework that is assigned for today,

## 54:53

you'll be looking at the transmission coefficient

## 54:56

as sort of another example, right?

## 54:58

So we'll have a source of neutrons

## 54:59

going in one side of the slab.

## 55:02

And what we're doing is figuring out

## 55:03

what fraction may get out,

## 55:05

or what's the ratio of the outgoing partial current

## 55:08

to the ingoing partial current

## 55:09

on the opposite side.

## 55:11

And what you'll find is it increases up to a point

## 55:13

as you increase k infinity or turn up your fission dial

## 55:16

until you would actually break the equation, right?

## 55:21

And that happens exactly at the point when k infinity

## 55:24

leads to an eigenvalue k that's equal to one, right?

## 55:28

A critical system.

## 55:31

So, any questions?

## 55:38

Okay, so office hours today until four o'clock.

## 55:41

And...

## 55:43

And then office hours tomorrow will be via Zoom.

## 55:48

Friday's lecture is a video, right?

## 55:50

With homework that's gonna be intertwined with the video.

## 55:54

And then you guys all get a week to eat turkey

## 55:58

and reflect on watching people eat rotisserie chickens

## 56:02

or whatever it is you're going to do.

## 56:03

Sorry, I did not end early.

## 56:05

I apologize.

## 56:06

Hopefully the chicken isn't totally gone yet.

## 56:10

My bad.

## 56:12

Okay.

## 56:15

Have a good Thanksgiving break.
