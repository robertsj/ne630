# L33 Local Audio Transcript

Course: NE 630

Playlist source: https://youtube.com/playlist?list=PLy481lNHlnHoEO95vM-xYX2bydD25v20L

Video: NE 630 - Lesson 33

URL: https://www.youtube.com/watch?v=mhXa47hdBU0

Video ID: mhXa47hdBU0

YouTube upload date: 20231113

Duration: 52:36

Transcript source: Local faster-whisper transcription from YouTube audio.

Whisper model: large-v3; detected language: en.

Generated: 2026-06-28

Note: This transcript is machine-generated from audio and lightly wrapped only. It should be reviewed before being quoted, published, or used as polished lesson text.

Requested language: en

## 00:00

and i feel like i am running on fumes i went to chicago this weekend

## 00:49

for the first like vacation that i've had in a long time and uh of course on friday i got out

## 00:58

of here as quickly as i could because i had to drive to kansas city because even though manhattan's

## 01:02

airport has opened back up the flights seem to be fewer in number than they used to be and the

## 01:07

times just didn't work out anyway so i got back at like 10 p.m to kansas city last maybe 9 p.m

## 01:13

or whatever but anyway so i got home around midnight and uh and then i had isomnia start

## 01:19

starting at 3 30 a.m so i'm feeling like a zombie i know you all know that feeling

## 01:25

so anyway we can suffer together all right uh let's this all right okay so uh i don't think

## 01:48

i have the lesson 34 page up yet i'll have that up um shortly after class i i hope i wanted to

## 01:56

make sure that the problem statement i had was good and uh apologies for not getting this up

## 02:01

when i was in kansas city

## 02:01

i did i thought i had this up and then it wasn't but you knew what the reading was because i saw

## 02:06

that many of you had the notes and so um just to go over uh briefly what we did last time was

## 02:12

primarily setting up this equation right going from the three-dimensional version of it that

## 02:17

that we had seen uh before that and then writing this down for slab geometry doing a couple of

## 02:23

adjustments make it slightly easier to solve and then we solved it and specifically we solved it

## 02:28

for as an example the case where we set up the problem statement and then we solved it for

## 02:31

the flux to zero at some boundaries right and that's uh sort of the easiest thing that you can

## 02:36

do similar to the initial conditions that we had done for um the neutron genetics right just setting

## 02:44

the neutron density or the precursor density at some point in time to some number that's what we're

## 02:50

doing here with the flux but it turns out that that boundary condition setting the flux to some

## 02:54

value doesn't have a whole lot of physical meaning it's like an approximation to something physical

## 03:00

but uh there are a lot of things that we can do to set the flux to zero at some point in time and

## 03:01

there are better ways to describe the physical situation that we often care about right so

## 03:06

uh today what we'll do is look at some of those other boundary conditions and there are several

## 03:10

uh discussed in the section that you had to read for today right and then uh also we'll look at

## 03:16

multiple regions so thinking about what you'll be doing next you just read section six four i'm

## 03:22

having you read six five and six seven for next time now six five we'll go through some some

## 03:29

similar examples to what i'm doing here today and then we'll go through some similar examples to

## 03:30

what i'm doing here today and then we'll go through some similar examples to what i'm doing

## 03:31

today in class once you have the the other boundary conditions and ways to connect different

## 03:37

regions the process is all very similar to what we did last time and and reasonably straightforward

## 03:43

now i know that the details can be really tedious there's no question about that which is why i much

## 03:51

prefer to focus on interpreting solutions interpreting you know forms of a solution

## 03:58

i don't like doing algebra right and in fact i

## 04:01

i have in the lesson 34 pages it's not posted yet but um i don't find a whole lot of value

## 04:09

in like 10 pages of algebra right so as you can imagine you get a solution for the diffusion

## 04:16

equation with those exponentials and then you have those undetermined coefficients of integration

## 04:20

well if you go to multiple regions you have multiple sets of those coefficients which just

## 04:26

becomes a bunch of mathematical misery really to to go through it and i don't think that's

## 04:31

there's a whole lot of physics in it okay it's important to understand the conditions that you

## 04:35

need to satisfy when putting together multiple regions right but um to take it really further

## 04:40

than that on pen and paper i don't i don't know what the the real value is so that's not something

## 04:46

i'm focusing on having you do because of course then when it comes to an exam setting there's no

## 04:51

way that you're going to write 10 pages of algebra that makes zero sense so uh we'll do a little bit

## 04:56

of that today using the computational tools to help us out but at the end of the day

## 05:01

the most important thing is to be able to understand what the conditions are for setting

## 05:06

up the equations uh for for different situations interpreting results right and then as we head

## 05:13

into friday uh the well actually for next time six seven gets you into multiplication right so

## 05:21

we bring fission back which is something we've ignored and that will lead us into modeling

## 05:28

a reactor with the diffusion equation right now

## 05:31

we're just modeling a system that has neutrons not necessarily a reactor right we're either

## 05:36

right we have a source term or whatever or we're putting neutrons into the side of a slab of

## 05:41

material uh but starting wednesday and then definitely into friday we'll actually start

## 05:46

thinking about what what we can do with the diffusion equation as it uh applies to reactors

## 05:52

and when you think of reactors you think of reaction rates you think of balance of reaction

## 05:56

rates you think of one special letter right what letter

## 06:01

is uh representing a balance of reaction rates and everything we've done so far okay thank you

## 06:13

okay right the k iu value right so before everything we've talked about relative to k was

## 06:18

k is equal to the four factors right or gains to losses and the one piece of the puzzle that we've

## 06:24

never quantified yet is that leakage probability right we've always just said it's 0.95 or

## 06:30

something well with diffusion theory we actually have a way to quantify that and so uh by the time

## 06:35

we get to the

## 06:35

end of the course which i've sort of mapped out uh by topic uh for for me i'll get the pages up

## 06:41

as as they're done uh we'll be able to sort of sit down and model a reactor a simple reactor but
from

## 06:49

the base data that we started with all the way through now to this diffusion

## 06:54

equation and the non-leakage probability sort of a whole whole picture right i guess i've hinted

## 07:00

at that along the way but uh any questions that you have about what we did last night

## 07:05

last time or specifically the homework that's due this evening so you're done with the homework

## 07:16

i see a yes i see some yeses i see some no's any questions on it or does it seem like it's going

## 07:25

well right now i'm just working through it based on what we did last time okay it's pretty similar

## 07:31

yeah it should be pretty similar in fact i think it's identical to what we did last time

## 07:36

if you take one of the coefficients and set it to zero right because last in class i had a

## 07:42

sum of a constant term and a cosine i think this just says the cosine term so it was it was there

## 07:46

as part of that solution so what we did in class was actually slightly more complicated um to set

## 07:51

up the equation and solve it i guess i'm asking you to do a couple like application things with it

## 07:55

right so um all right so uh obviously that you did the reading there's a lot of stuff in there

## 08:02

a lot of definitions i'm going to touch on some of them right i'm not going to go through every

## 08:08

single thing because that's what the book is for so if we get through some of this

## 08:12

stuff here in my by hand slides i'd like you to to to ask or just ask if there's something that

## 08:19

i haven't addressed that you really want me to clarify let me know i did scan through some of

## 08:23

your notes i apologize because i didn't have that assignment ready to go until 9 a.m and then i

## 08:29

prepped i didn't have a chance to go through them in a whole lot of depth uh but hopefully those i

## 08:35

think i got all the notes assignments through the end of the semester so i'll be able to see them as

## 08:40

you give them to me

## 08:42

okay so um let me go ahead and move that forward okay so for the boundary conditions

## 08:53

let's use this letter x sub b as some boundary location right i think there's a similar thing

## 08:59

in the book okay boundary conditions are used to apply uh approximations whatever to model

## 09:08

some physical reality right we have the differential equation the

## 09:12

diffusion equation that that models at a differential scale the balance of neutrons

## 09:16

right the absorption uh the diffusion neutrons away from the location driven by a source term

## 09:22

okay in order for us to have a full solution we need to know what happens at some sort of

## 09:27

system boundary we're not interested in an infinite system at this point right that's

## 09:30

what we did in the past now we have to apply something at boundaries to to understand what

## 09:35

what's happening inside of our finite system okay so there are three physical situations that that

## 09:42

typically want to model and that are accessible with the diffusion equation and the boundary

## 09:47

conditions that we have available okay one and probably the one that is most um maybe most

## 09:54

important is this idea of no neutrons coming into the system and what i mean by that is if we have

## 10:01

our trigger reactor down in the hallway okay it's got its own neutrons we're not shooting it with a

## 10:06

neutron gun or anything like that that would actually probably not make the nrc very happy

## 10:12

and that's why we have to make an assumption that there are no neutrons coming in or at least

## 10:16

that's that i mean we have some neutrons coming i've talked about cosmic rays and things like that

## 10:22

but the the physical reality is the neutrons are in the core we're not having neutrons come in okay

## 10:28

so how do we model this idea of no neutrons coming into the system right i'm using this uh little

## 10:36

scheme of good better and best like they try to upsell you at menards when you want to get some

## 10:40

plumbing fixture or something like that right

## 10:42

nobody's doing plumbing all right well lucky you good better and best so

## 10:49

good is probably an overstatement in this particular case what's the what what have we

## 10:55

done so far what is our boundary condition that we've seen yeah and specifically what do we do

## 11:01

with it what do we say about the flux it's zero yeah so if we're talking about this system right

## 11:12

we have a system slab here okay if i have no neutrons coming into the system right these

## 11:18

would be the neutrons i i want this uh let's see number of neutrons equals zero now i could just

## 11:26

set my flux this is my flux of x i could just set that to zero right obviously if my flux is zero

## 11:37

the number of neutrons in that location is small right because we know that

## 11:41

the neutron density is proportional to the flux and vice versa right so we have v is equal to n

## 11:47

times v if the flux is zero we're actually saying that the neutron density is zero now is that the

## 11:52

number of neutrons coming in no but if there are no neutrons coming in we'd expect the density to

## 11:58

be very small and so if we set the density to be very small we're implying that the number

## 12:03

of neutrons coming in is also small okay so it's it's not unreasonable to set the flux

## 12:11

to zero it's just not the best okay so what we can do is say hey v of x b is equal to zero okay

## 12:21

now there was also a a very similar condition discussed in the book and it's still setting the

## 12:30

flux to zero but it's not setting it to zero at this physical boundary x sub b anybody remember

## 12:42

what the flight

## 12:43

what what condition i'm talking about

## 12:48

what so i get in a sense i would say all of these this good better and best that will will wrap up

## 12:54

these are all trying to represent vacuum so when i say vacuum boundary vacuum means no neutrons

## 13:00

coming in right so that that's a good a good reminder right so this is this is my vacuum

## 13:07

condition right because if i have a vacuum outside my reactor that means there are no neutrons
outside

## 13:12

of my reactor

## 13:13

okay i i could also model it or describe it instead of using vacuum uh with pure absorption

## 13:22

or infinite absorption right if i have if i surround my reactor with uh some isotope that

## 13:28

has an infinitely large absorption cross-section it would also be the case that i have no neutrons

## 13:33

out there right it's just vacuum is a little bit more pleasant to consider okay so anybody else

## 13:41

remember so i don't maybe maybe that's what you're thinking is vacuum so what do you what did

## 13:46

you write down for a vacuum condition um see there's a like a extrapolation yes the extrapolation

## 13:57

boundary right so we know that the that the neutron like if i have a neutron source inside

## 14:03

of this slab right we know that it'll maybe peak in the middle if it's a uniform thing but

## 14:07

we would also know that it doesn't go to zero because to force the flux to zero is an unphysical

## 14:13

uh constraint okay so what it would actually look like let me switch over to an orange of some

## 14:21

sort right it would actually look like something like this okay it will have curvature that looks

## 14:27

pretty similar throughout and they would overlap in the middle but in reality i would have a non

## 14:34

zero flux at the boundary and then those neutrons that leave the building as it were would just kind

## 14:39

of peter off into the distance and we could extrapolate

## 14:42

whatever that that slope is down to the appropriate axis okay and that distance this

## 14:50

thing here call it delta we would add on to the distance so if this is my uh distance a for my

## 15:01

width of the slab then we would define a tilde is the way that it's described in the book plus

## 15:09

uh is equal to a plus delta okay so it just means that we're going to take our

## 15:14

take whatever our normal boundary location is and we're going to push it out a little bit because

## 15:19

mathematically that captures the shape of the flux at the boundary a little bit better now the way

## 15:25

it's described in the book it's actually equivalent to what i'm calling the best so let me summarize

## 15:32

this one we could say that phi of x tilde b why don't why am i calling it a here i'm calling it

## 15:42

well i guess we have x equals zero and then x equal a both of those values would be my xb but

## 15:50

for the this better case we would say that phi of x tilde is equal to zero right where x

## 15:58

tilde is just slightly past um the boundary of interest okay and specifically uh x

## 16:06

tilde here is equal to x plus this delta and the delta

## 16:12

is equal to in the book two-thirds times lambda where lambda is the mean free path

## 16:19

right so this would be equal to two-thirds times one over sigma t right my total cross-section

## 16:28

if we had anisotropic scattering it would be better to use sigma tr that transport cross-section

## 16:33

okay now what's funny to me and it is in this the the book the fact that they're uh that he

## 16:42

called it the sigma t and the sigma t are the two-thirds times lambda where lambda is the mean free

## 16:42

path right so what's funny to me and it is in this the book the fact that they're uh that he called

## 16:42

it two-thirds lambda makes me think back to when i sat in this class as an undergrad right where

## 16:49

instead it was delta is equal to 0.71 times lambda uh yeah times lambda where does the 0.71 come
from

## 17:01

and why do i remember that i don't know why i remember it but it comes from transports here

## 17:06

right so remember we're using diffusion theory diffusion theory is not like the full real answer

## 17:12

right so remember we're using diffusion theory diffusion theory is not like the full real answer

## 17:12

and if you kind of have gleaned from the reading so far and if you happen to look at section 6.6
there

## 17:20

are a number of situations where diffusion theory is inaccurate and one of them is by boundaries

## 17:27

right so you can actually force the diffusion solution to look a little bit

## 17:32

closer to reality the transport solution here by fudging the boundary condition to

## 17:37

make the curvature look more like the transport solution rather than the

## 17:41

the you know diffusion solution okay i kind of like the fact that the book doesn't even bother

## 17:47

telling you that right here you can listen to me talk about it for two minutes and in one year out

## 17:52

the other you don't have to sit there and have read it before but um at any rate i don't like

## 17:57

the extrapolated condition whether it's the book's version where we're just kind of capturing the
zero

## 18:03

incident current condition or the transport 0.71 right i much rather do the best which is this

## 18:11

we say that the j right and i'll call it in for incident or incoming partial current at x b

## 18:24

not the tilde is equal to zero right so there is this thing called the partial current

## 18:33

right and the partial current in slab geometry can go either to the left or to the right so

## 18:40

depending on which boundary you're on the left or the right could be the

## 18:43

in-going current right so if you're at the left boundary the right word would be your in-going

## 18:48

current if you're at the right boundary then the left partial current be your in-going right i won't

## 18:53

write out exactly what the partial current is that'll be in the next page okay but those are our

## 18:58

three models for uh vacuum conditions right the situation where we don't have neutrons coming in

## 19:04

and that that's that's probably the most important of the um situations that we have related to that

## 19:13

we have a fixed number of neutrons entering the system right i guess it's related because it's

## 19:17

sort of the opposite in in the first case we're saying there are zero neutrons coming in but there

## 19:23

are some applications where we would specify the number of neutrons coming in right if we have say

## 19:28

this foil of some metal right where we have an incoming beam of neutrons right we could say that

## 19:36

that partial current incident on that side is our you know what that's our boundary condition okay
so

## 19:43

the fixed number of neutrons would be rather than j in at the boundary equals zero we would say

## 19:48

that j in at the boundary is equal to some source term right s double prime uh to use the book's

## 19:56

notation okay the final one and one that isn't necessary in practice right because there's no

## 20:04

real system that exhibits reflection but as a modeler sometimes you can simplify your life by

## 20:11

imposing reflection where

## 20:13

oh more of the two is bursting too far between j and my plane and then i have no way of still

## 20:19

hitting the Ts in Beijing on the both of those points which i've been looking at um a metaphor

## 20:22

for the intersectionones is when youять an equation where then almost any expression

## 20:27

can be defined by the lower step and then this has to go down the expression's like a

## 20:29

port end so it's like beefy all of the obj JavaScript for example if you look at a

## 20:34

hint there arehey if you'll look we did this our we loft we saw anything but the average

## 20:39

expression is the Repoda anything we e Fazil even if that's the case that the formula doesn't

## 20:43

at x equal xb is equal to zero.

## 20:48

That just means that the flux derivative is zero.

## 20:52

And if the flux derivative is zero,

## 20:54

then the current is zero, net current is zero.

## 20:58

And if there's no net flow,

## 20:59

that means we flatten out

## 21:00

and every neutron that goes out must come back in, right?

## 21:04

So it's a useful way to simplify some problems.

## 21:09

Okay, so these are the boundary conditions

## 21:12

that we have available in diffusion theory, okay?

## 21:15

We would have the same conditions

## 21:17

if we were outside of slab geometry, right?

## 21:19

We could, if we looked at the spherical or cylindrical,

## 21:22

I'll point out in the next reading,

## 21:25

everything is in terms of spherical coordinates.

## 21:27

I don't think spherical coordinates is very useful for us.

## 21:32

Okay, cylindrical, yes.

## 21:33

And then we'll see that in the next chapter.

## 21:36

Spherical, you'll see that the mathematics

## 21:39

or that sort of the trick

## 21:41

is to make some sort of substitution

## 21:43

and you end up with equations

## 21:44

that look just like the slab equations, right?

## 21:46

So in the end, it's really no different

## 21:48

in terms of dependent paperwork.

## 21:50

Just be aware that it's for spheres

## 21:52

and in practice, we don't need it.

## 21:54

Like the only spherical geometry

## 21:56

that I have ever seen in real systems

## 22:00

is the triso-fueled pebble for pebble bed reactors.

## 22:08

And I don't think diffusion,

## 22:11

theory would ever be the appropriate thing

## 22:12

to use for that system anyway, right?

## 22:14

So basically, there are very few applications

## 22:17

where you knowing how to solve something

## 22:20

in spherical coordinates

## 22:21

is going to make your life better.

## 22:23

And I think that having to do it

## 22:26

would make your life worse.

## 22:27

I don't want to do that.

## 22:29

Okay.

## 22:30

All right, so what is this partial current?

## 22:36

Now, the partial current, if you read,

## 22:39

requires that you go to transport theory

## 22:41

where you have neutrons,

## 22:43

and you are accounting for their direction.

## 22:46

Something that we talked about,

## 22:48

or that when we derived the,

## 22:50

or motivated the diffusion equation,

## 22:52

there was no notion of direction,

## 22:55

except for this concept of net neutrons

## 22:57

going out of a certain face,

## 22:59

certain other face,

## 23:00

and then we balance everything together.

## 23:02

We didn't have a direction assigned

## 23:03

to an individual neutron.

## 23:05

But if you think about it,

## 23:06

every neutron does have a direction, right?

## 23:08

Because every neutron has a velocity.

## 23:09

Even if we're doing one speed, one energy,

## 23:12

that neutron has a velocity,

## 23:14

and velocity is a 3D vector, right?

## 23:17

There's an X, Y, and Z component, okay?

## 23:20

So, neutrons always have direction.

## 23:22

We've sort of glossed over that, right?

## 23:25

That's the big thing.

## 23:26

And so, when you go to the appendix

## 23:27

where this partial current is defined,

## 23:35

within the confines of diffusion theory,

## 23:36

you can define this partial current,

## 23:38

which is basically limiting direction to be to the left,

## 23:42

or to the right,

## 23:43

in 1D slab geometry, right?

## 23:45

If we were in 3D Cartesian,

## 23:47

we'd have to the left, to the right,

## 23:49

to the up, to the down, to the back, to the forth.

## 23:51

But that would be it.

## 23:53

So, in slab geometry,

## 23:55

we have that this partial current

## 23:57

is equal to whatever our flux is

## 24:00

at X divided by four.

## 24:04

And then, where this is the plus or minus,

## 24:06

meaning, so this is to the right,

## 24:11

this,

## 24:12

this is to the left, okay?

## 24:18

We have plus or minus, this becomes minus or plus,

## 24:22

and then we have D over two,

## 24:25

and then the derivative of the flux

## 24:29

evaluated at X equal,

## 24:35

I guess if I were to put XB,

## 24:38

then this would be XB, this would be XB, okay?

## 24:42

That's the partial current.

## 24:43

Okay.

## 24:44

Probably in my own nomenclature,

## 24:47

I'm gonna drop the X subscript in 1D, right?

## 24:55

Because if we're in 1D,

## 24:56

we already know that we're along the X axis.

## 25:00

So, in some of the examples, I'll probably drop it.

## 25:02

So, I wanted to remind myself to point that out, okay?

## 25:07

So, that's the partial current.

## 25:08

The partial current is what we use to define

## 25:11

number of neutrons going in some of the sub-substances.

## 25:12

So, that's the partial current. The partial current is what we use to define number of neutrons
going in some of the sub-substances.

## 25:13

So, that's the partial current. The partial current is what we use to define number of neutrons
going in some of the sub-substances.

## 25:13

So, that's the partial current. The partial current is what we use to define number of neutrons
going in some of the sub-substances.

## 25:14

So, that's the partial current. The partial current is what we use to define number of neutrons
going in some of the sub-substances.

## 25:14

So, that's the partial current. The partial current is what we use to define number of neutrons
going in some of the sub-substances.

## 25:15

So, that's the partial current. The partial current is what we use to define number of neutrons
going in some of the sub-substances.

## 25:15

So, that's the partial current. The partial current is what we use to define number of neutrons
going in some of the sub-substances.

## 25:16

if we're talking about our left boundary before, we would be defining the right current into that

## 25:22

surface. Whether it's a zero, right, for the vacuum, like a true vacuum condition, or the best

## 25:28

vacuum condition from the previous slide, or if we are putting into the slab a surface source,

## 25:34

right, a number of neutrons per centimeter squared per second into that surface. The albedo is

## 25:41

related to the partial current, and in fact, it's just the ratio of the partial current. So you

## 25:45

probably saw the albedo come up in the reading, and so that is just the J plus. Actually, I'll

## 25:54

write it like this instead, because the albedo really means what's the ratio of neutrons coming

## 26:00

out given neutrons going in. So it really does have a dependence on which face and the orientation.

## 26:09

So I'll write it like this instead. I would say that this is J out at X,

## 26:15

divided by J in at X, right, where the out and the in depend on if you're on the left side or the

## 26:24

right side, okay? And the albedo is also related to some other terms that will show up in your

## 26:34

homework, right? There's nothing new that you'll have to understand. It's just, again, ratios,

## 26:42

right? So if I have a slab,

## 26:45

of material, and I put in an incident current, right, J in, then I will get out a J out at the

## 26:59

left, and I will get another partial current out at the right, okay? And obviously, the J left out

## 27:14

over the main surface is the J out. So I'll write it like this instead, because the albedo is

## 27:15

the jn is the albedo but we can also recognize that as a reflection coefficient right so the

## 27:24

albedo comes from optics right the word albedo is used in optics and it represents something to do

## 27:30

with reflection right of light when you have um what the hell is the word opaque when you have

## 27:36

an opaque media right so it's not completely transparent you have some light that's scattered

## 27:40

back that amount of scatter is called the albedo i have no idea where the word actually comes from

## 27:45

i just know that that's an application in neutronics if you put in neutrons to a slab of

## 27:51

material you get some out we also call that the albedo if the slab is finite you will also get a

## 27:57

certain number of neutrons that goes through it right and that would be my j right out over jn

## 28:08

right so put this number in get this number out on the other side and i would call that t

## 28:13

transmission coefficient right

## 28:15

so we have reflection we have transmission and i thought it was worth putting this into the

## 28:22

material because when i first started my phd work i played with one group diffusion where my whole

## 28:30

business was computing reflection and transmission coefficients because those form parts of
something

## 28:36

called the response matrix method which is what my work was on right so everything i did started

## 28:43

off with plain old one group diffusion like the

## 28:45

the most benign of the models that you can use for neutronics uh and that ultimately i went to

## 28:51

multi-dimensional transport and such but this is you can you can understand a whole lot under this

## 28:58

framework okay okay and yeah i point out here that uh we need more symbols because we've used alpha

## 29:06

for more than one thing but being consistent with the book all right so this is the last bit of hand

## 29:15

writing that i'll do and then we'll go to the

## 29:17

slides but i'm going to motivate the last topic um by handling or setting up equations to model

## 29:25

this problem so we've got a three region slab system here where we have reflection on the left

## 29:32

we have vacuum on the right and we have uh four x coordinates we're going to assume that the in each

## 29:40

of these regions one two and three that we have constant um cross-section data right so that means

## 29:46

that we have d i we have sigma a i or i or equivalently we have a diffusion length i and

## 29:55

then d two and so on and so forth and then in each region we can have a constant source term or
really

## 30:01

in an arbitrary source term right because we know how to solve it for uh we know how to solve the

## 30:06

diffusion equation for for any function of x but i'll just say s i s two s three right okay um

## 30:21

what does the solution look like in each of these regions so if i if i consider only region one

## 30:38

what two pieces do i have to put together to define the solution

## 30:43

same thing that we had to use for our single region last time there are two parts

## 30:51

what we could break the solution into those components right but i'm

## 30:54

talking about just solving the diffusion equation the differential equation itself

## 30:59

right so that's two pieces right just hard to describe with only two pieces it would be

## 31:09

except to pursue a fate of a victim of the évidemment fullness nueva espanola

## 31:16

which most of us do but i also wanted to talk about in another example let's just wear a着

## 31:23

and i'll go back to the machine here first here's the

## 31:30

in which you can just use any D4 key, right right to change the domain mode of such a function which
you can use as the verb to select the domain to enter formulas like T1 D0, safety vector, parts of a
function, or some other formula.

## 31:31

each of the other regions or any number of regions, right?

## 31:33

I will always have a homogeneous and a particular solution.

## 31:37

Those solutions in their general form

## 31:40

have no dependence on the other regions, right?

## 31:43

Because the particular solution depends on the right-hand side

## 31:46

within that region, the source term.

## 31:48

And until we apply boundary conditions,

## 31:51

the homogeneous solution is stuck in that C1 and C2 form, right?

## 31:55

So in this region, I would have my phi I of X

## 32:02

is equal to a C1 e to the X over L1

## 32:08

plus C2 e to the minus X L1

## 32:14

plus whatever my particular solution is in that region, right?

## 32:21

And if it's a constant source term,

## 32:22

it'll be a constant particular solution, okay?

## 32:25

But if it's a constant source term,

## 32:25

it'll be a constant particular solution, okay?

## 32:25

But we know how to solve for that coefficient, right?

## 32:28

This method of undetermined coefficients, right?

## 32:31

Totally unrelated to boundary conditions

## 32:33

or any other thing, right?

## 32:34

That we'll have to deal with multiple regions.

## 32:36

And that means in region two, we'd have the same thing.

## 32:39

And in region three, we'd have the same thing.

## 32:41

So to save a little space, I'll just do it for region three, okay?

## 32:45

So we have region three of X is equal to C.

## 32:49

If I'm using C1 and C2, I'll use C3 and C4

## 32:52

and then C5 and C6 for this region.

## 32:55

E to the X over L3 plus C to the six,

## 33:02

X of L3 minus plus whatever its particular solution is, okay?

## 33:12

Now, we already know how to deal with the boundary conditions, right?

## 33:17

Because if this is reflection,

## 33:20

can somebody tell me how I would define that equation?

## 33:25

Just in terms of phi one, this thing here, right?

## 33:33

If I have reflection, what's my boundary condition?

## 33:37

What has to go to zero?

## 33:43

The derivative of my flux, right?

## 33:45

Or equivalently, the derivative of my current.

## 33:48

Really, it comes from the current.

## 33:49

So minus D times D, the diffusion coefficient.

## 33:54

So I have this.

## 33:55

I have minus DI.

## 33:59

Time D phi I DX at X equals zero, equals zero.

## 34:06

But because we're assuming the diffusion coefficient is constant,

## 34:10

we're just saying that phi I DX at X equals zero, is equal to zero, right?

## 34:20

And then if I'm on the right-hand side, I have vacuum.

## 34:24

Now, I just described we have three options for doing vacuum, right?

## 34:28

So just to simplify what I write down here,

## 34:31

I could just say that phi three at X three is equal to zero, right?

## 34:38

Or I could set the incoming partial current to zero or whatever I want to do, okay?

## 34:43

Now, this is one equation.

## 34:46

This is another equation.

## 34:48

So I've got two equations.

## 34:50

How many unknowns do I have?

## 34:53

I have six unknowns.

## 34:54

So I'm, question.

## 34:58

It's not the unknowns.

## 35:00

Because the different regions share boundaries, does that mean your boundary coefficient,

## 35:07

like your C one and C three would be, would they be the same?

## 35:13

Nope.

## 35:14

Not necessarily, right?

## 35:15

Because C one and C two are governed by this boundary condition.

## 35:22

And then as we'll find, there's another condition that has to be satisfied.

## 35:25

But only the C's or the phi's, in this case, in a region are,

## 35:31

it's, it's local, right?

## 35:33

So this boundary condition gives us a constraint on what C one and C two are.

## 35:39

This boundary condition does not tell us anything about C three and C four.

## 35:44

This boundary condition on the right-hand side will tell us, or give us a constraint on C five and C
six, but not on the middle, right?

## 35:52

Because that flux doesn't show up in that, that, expression.

## 35:57

But of course we have to deal with them, right?

## 35:59

And so what, what, what are we going to do?

## 36:01

Right?

## 36:01

are our missing four conditions it seems like we're missing a hell of a lot of information what

## 36:05

what are the conditions that we're missing the interface conditions or what i would call the

## 36:13

continuity conditions right two quantities are conserved in our our neutronic model okay

## 36:20

the flux the flux has to be continuous and what else the net current right remember

## 36:30

one what's driving everything that we're doing is a balance of neutrons reaction rates the number

## 36:36

of neutrons entering or leaving a system so we've got to preserve that net flow of neutrons okay so

## 36:41

that means that we have the continuity conditions where phi i or one at x1 has to equal phi 2

## 36:57

at x1

## 37:00

and minus d i d phi i and dx at x equal x1 right that's the current on the left hand side of the

## 37:15

the interface that has to be equal to minus d 2 times d phi 2 dx x equal x1 okay so that's two

## 37:31

equations

## 37:32

right and then of course we could do the same thing at the second interface at x equal two

## 37:39

x equal x2 right so that gives us the six equations to solve this now this is not something that you

## 37:47

would want to do on paper i would never have you do what i would have you do is write down what

## 37:52

those equations are right because i know you can take the derivative of some flux form that you

## 37:57

have right that's that's not i think out of the mind because

## 38:02

the right hand sides that we're dealing with are a constant or a polynomial or a cosine or something

## 38:07

like that but to be able to write down what those those uh equations are it's important to be able

## 38:12

to solve more than two of them at a time is that's a waste of time i think okay so what we use to

## 38:18

solve them by the computer that's what the computer is there for okay any questions about this all

## 38:34

right so i think we've got enough time so i can dive into an example because i want to give lindsey

## 38:38

some numbers

## 38:42

so let us go then to the slides where i've got a couple um i've got one example that is mostly

## 39:00

worked out and if we have time we'll deal with the second one but i want to show you something

## 39:05

now it makes no sense for me to sit there and go through a whole bunch of symbolic manipulation i

## 39:10

mean i did that last time and you

## 39:12

know it takes some time we all know that writing out problems like this takes some time and i don't

## 39:16

know that it's a good use of my time to do that so what i'm going to do is use simpi right the

## 39:20

symbolic thing that i've shown before this is going to help me very quickly write down the

## 39:25

equations solve some equations and then get to a solution what's consistent though is that the

## 39:32

process the order of steps the logic the algorithm as a word is the same whether i'm doing it with

## 39:37

simpi or if i'm doing it with pen and paper right i still have to set up

## 39:42

the boundary conditions i still have to get a solution to a differential equation i have to set

## 39:47

up the boundary conditions so that i can solve for the undetermined coefficients okay and then i put

## 39:52

it all together substitute numbers and get a solution right it's the same thing it just

## 39:56

it goes a little bit quicker and uh i make less mistakes right and to actually that this this sort

## 40:05

of problem that i'm doing and the steps that i'm using here this is actually something that i used

## 40:10

to do in me400 right it was one

## 40:12

toward the end of ME400, we had a week where we did symbolic computation, setting up and solving

## 40:20

differential equations like this. So it's something that it would be cool if you all knew how to do
it

## 40:25

already, right? But here we are. I'll give you an example, and maybe you can apply it to your,

## 40:31

of course, to this class, and then maybe outside of that, okay? So here's the problem. We've got

## 40:38

just a single slab, but what I want to do is explore what happens when we change our vacuum

## 40:44

condition from our good old zero flux condition to this zero incident partial current condition,

## 40:50

right? And then we'll see if we can get some numbers plugged in and actually plot the solution

## 40:55

and see what happens to it, okay? So the very first thing I'm going to do is maybe get us to...

## 41:03

Is it going to... Actually, what I'm going to do is save it, and then...

## 41:08

to close that and i'm going to open it up again so that i have my scrolling enabled okay

## 41:17

okay so we'll substitute those numbers in at the end but first of course we have to do everything

## 41:22

symbolically so i've got sympy imported i guess i can just do this okay when we use

## 41:31

sympy the very first thing you have to do is define the symbols right you're still working

## 41:36

with python variables but these variables now have a value that is a symbolic quantity there's

## 41:41

not a number attached to the name it's now this this weird symbolic creature okay um and so once

## 41:48

i have those defined i can actually define the diffusion equation okay so do i need to blow up

## 41:56

the font for those in the back or is this good enough let's see if that i can join

## 42:06

well

## 42:06

see if this okay okay so i've got the neutron diffusion equation now where

## 42:11

i'm taking the symbolic uh derivative of b of x that function i just defined second

## 42:16

derivative in this case and uh everything down the line right and what comes out is a nice

## 42:21

pretty math um equation that looks a lot like what we've been dealing with okay now that i have this

## 42:27

equation right then i need to determine the solution now the one thing that sympy doesn't

## 42:35

let us

## 42:36

like take uh it doesn't let us take steps in this case because it will take this this differential

## 42:42

equation and give me the full general solution right but i think that's not a big problem here

## 42:48

because getting the particular solution is probably the easiest part of it but i guess

## 42:53

maybe the homogeneous solution is because it's always the sum of two exponentials at least in our

## 43:00

this lab geometry right so if i get this solution it'll be the homogeneous plus the particular

## 43:06

solution right and so it is c1 times e to the minus x over l it has no it doesn't like my

## 43:13

aesthetic of putting the positive one first i guess we'll allow that though right so we've got

## 43:18

c1 times e to the minus x over l c2 e to the plus x over l and then our particular solution

## 43:25

which is the constant that that we would expect okay

## 43:30

that's that's the the general solution that's something that that we all should be able to do

## 43:35

for a single region uh of a slab right now we can also define the partial currents right so this is

## 43:45

the the solution phi i can also use that to define the partial currents right so i've got my right

## 43:51

word current that's the solution that we just looked at divided by four d over two times its

## 43:57

derivative right of uh with respect to x and then the left is the the same thing but now uh plus

## 44:03

okay so this is the right word curve you can already see that dealing with the partial

## 44:08

currents is going to be a pain in the ass relatively speaking okay not too much though

## 44:14

right and so we'll take this and we'll then define our boundary condition so i'm going to do the
zero

## 44:23

flux ones first right so my boundary condition at the left is another simple equation where i'm

## 44:29

taking my flux solution the thing that we saw a few months ago

## 44:33

moments ago i'm substituting in x is equal to zero and i'm setting it equal to zero right this

## 44:41

is just a statement saying my incident current uh sorry my left side the flux at my left boundary

## 44:46

is equal to zero okay and this is the equation i get right c1 plus c2 plus my uh particular

## 44:56

solution is equal to zero nothing nothing weird about that okay and i do the same thing at the

## 45:03

right boundary okay and if i do that i get the c1 times that exponential term the c2 times the

## 45:09

other exponential term plus the particular solution is equal to zero right where now i

## 45:14

have a instead of x nothing magical about that this is where you would with pen and paper start

## 45:21

to do the real work because you would get to this point without doing a whole lot of work you'd have

## 45:25

the homogeneous solution you have the particular solution all you're doing is substituting x equal

## 45:29

whatever your two boundary values are that gives you

## 45:32

you

## 45:33

how many equations for how many unknowns two for two two equations two unknowns right

## 45:39

this solving this this is where solving uh differential equations is cumbersome and what

## 45:47

is really kind of weird about it is it's not calculus at all it's algebra right comes down

## 45:53

to it everything we do is algebra but i don't want to do algebra so what i can do instead

## 45:58

is well i could write this in in matrix form right so this is a little bit

## 46:03

of stuff that it kind of just forcing it into a matrix expression but if you look at it this

## 46:08

matrix system is identical to that now the reason i put it like this and i did this also in in the

## 46:16

last class if you are doing the homework right whether it's two region or four sorry one region

## 46:23

two region whatever when you get to this set of equations at this point you could choose to

## 46:29

substitute your values right we know what a is from the problem of the equation and we know what

## 46:33

a is from the problem statement a is equal to 10 centimeters we know what l is because we know what

## 46:36

the d and sigma a are if you put those in you now have a numerical two by two matrix if you have a

## 46:44

a numerical matrix you can use numpy np.linalg.solve that's something if you look at my

## 46:52

the the page for today i did so you had the reading the one additional thing i said is

## 46:57

you should know how to solve linear system right you can i know you all know how to solve a two by

## 47:01

two system by hand but you should know how to solve a two by two system by hand and you should

## 47:03

know how to solve a two by two system by hand but if you if you want to check your work or just

## 47:07

bypass doing it by hand at all right i'm not going to ask you to to come up with the symbolic

## 47:13

expression for c1 and c2 right if i'm asking you to plot i'm asking you to plot it with specific

## 47:19

numbers so you can just kind of bypass writing out the c1 and c2 like i did last time okay so

## 47:24

if you have that then you can substitute the numbers you can invert the matrix you get c1

## 47:28

and c2 and once you have that you have your entire numerical solution

## 47:33

all right so simpi does give us the ability to um solve it by ourselves uh with without using the

## 47:45

numpy right so i can also do the the um same thing with the partial current and yeah that matrix has

## 47:52

elements that look a little bit more complicated right than the previous one this is why i suggest

## 47:59

using numpy.linalg.solve because if i know what a is and i know what c is and i know what c is

## 48:05

what l is and i know what d is it doesn't matter this is still just a two by two matrix i can

## 48:10

solve for c1 and c2 and then i have my full solution defined does that make sense okay

## 48:24

so we can solve using sim pi we can solve everything right so for the uh the zero flux

## 48:31

boundary condition this would be my c1 and if i wanted to look at what c2 is it would

## 48:37

look like this

## 48:39

same thing from

## 48:40

symmetry and then this is what my solution is right once i substitute those coefficients okay

## 48:48

it'll look a little bit uglier if i put in the partial current conditions because those coefficients

## 48:52

were just more messier right i don't see any value in and doing it but so if you're doing it in pen

## 48:58

and paper you can come up with the same expression you can probably simplify it a bit this doesn't

## 49:02

tell me anything right it's useful if you get to this point because now you can also substitute

## 49:07

the numbers right and then you have strictly speaking a function of x and you can plot a

## 49:12

function of x using num num uh map.lib or excel or whatever right it's so everything i'm talking

## 49:20

about here is set yourself up in a way so that when you actually substitute the numbers you're

## 49:26

doing it at the place that minimizes the work you have to do that's the key thing right if the

## 49:32

problem statement or what i'm saying i'm looking for doesn't explicitly say give me a

## 49:36

nice

## 49:37

closed form solution for the flux don't spend your time doing it right that should be true in

## 49:42

everything else that you do right i mean maybe there are instructors who would just want that

## 49:47

but they should tell you that first right i'm telling you don't don't bother i would rather you

## 49:53

uh i i'm okay if you do it this way i'm okay if you use simpi to get to this point

## 49:57

or you do it by hand i'm thinking it's easier for you to set up that two

## 50:01

dimensional system plug in the values get the numerical quantities for c1 and c2 and

## 50:07

then you would have the same thing numerically for whatever the values are all right so um

## 50:17

once we get here i can actually substitute the values that i need so this one i didn't do so

## 50:25

what i'll do is this i'll say num data right these are my numerical

## 50:29

data's uh i will say that a is equal to 10 for the 10 centimeters d was equal to 1

## 50:38

sigma

## 50:40

a is equal to i think it was 0 1 my s was equal to 1 and then

## 50:51

i think that would so and then l would be equal to

## 50:55

psi square root of d as a 1 over 0.1 okay and if i do that now i can do phi sol subs coefs zero

## 51:10

and then subs num data

## 51:14

and now i have numbers of course this expression doesn't mean a whole lot to me either the point

## 51:26

now would be to take it and use it for the plot right or to evaluate the flux at a boundary or

## 51:31

to take this differentiate it multiply it by the diffusion coefficient to get me a net current

## 51:37

at any point in along the x-axis right so i'm hoping uh that you can take this and use this

## 51:44

to your advantage on on the homework um and then this will certainly help as we get to some of the

## 51:52

more complicated um problems but i don't that you have the homework ready to go for for next time

## 52:00

and then the one after that we build on on that so any questions all right then i will see you all
on

## 52:14

wednesday
