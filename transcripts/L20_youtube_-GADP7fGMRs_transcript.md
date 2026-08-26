# L20 Local Audio Transcript

Course: NE 630

Playlist source: https://youtube.com/playlist?list=PLy481lNHlnHoEO95vM-xYX2bydD25v20L

Video: NE 630 - Lesson 20

URL: https://www.youtube.com/watch?v=-GADP7fGMRs

Video ID: -GADP7fGMRs

YouTube upload date: 20231011

Duration: 54:17

Transcript source: Local faster-whisper transcription from YouTube audio.

Whisper model: large-v3; detected language: en.

Generated: 2026-06-28

Note: This transcript is machine-generated from audio and lightly wrapped only. It should be reviewed before being quoted, published, or used as polished lesson text.

Requested language: en

## 00:05

I heard a question and just heard you say something.

## 00:10

I don't know where it's going.

## 00:12

I don't know where it's going.

## 00:14

I don't know.

## 00:16

I don't know where it's going.

## 00:20

I don't know.

## 00:23

I don't know.

## 00:25

I don't know.

## 00:28

I don't know.

## 00:34

I don't know when it's going.

## 00:37

I don't know where it's going.

## 00:41

I don't know where it's going.

## 00:43

I don't know who it's going.

## 00:48

I don't know.

## 00:51

I don't know if you have more.

## 00:52

you probably .

## 00:56

.

## 00:58

that was so funny though that's the time you sit down

## 01:05

all right we will discombobulate it today but hopefully we make it through it

## 01:20

um so any questions from last time hopefully you are able to um do everything with the openmc

## 01:39

driven unit cell stuff that we talked about um more do i have others a minute

## 01:54

maybe i should just turn off the waiting room so i don't have to

## 01:58

do that i'll try to do that for next time

## 02:03

all right

## 02:04

so what we covered last time was the use of the unit cell classes to explore the sort of the

## 02:13

impact of geometry uh or material definitions on the multiplication factor of a unit cell so

## 02:22

the example in class was specifically the plutonium fraction for the uh sfr unit cell

## 02:28

and for the homework you'll be doing something very similar for the pressurized water reactor

## 02:33

unit cell where you're

## 02:34

now varying p over d right so the ratio of the pitch to the fuel diameter which is effectively

## 02:40

changing the ratio of the moderating volume to the fuel volume right and that will impact

## 02:45

the four factors in different ways uh and that your goal is to to explore that and understand

## 02:52

what those impacts are um what we're going to cover today it sort of extends that analysis

## 02:58

uh with a focus on something called reactivity and reactivity feedback so

## 03:03

obviously nuclear reactors are highly dynamic machines right they're systems that evolve in time

## 03:09

and we have to be able to control them right one of the things that helps us out immensely is the

## 03:16

fact that there are physical feedback mechanisms that keep uh the uh that make basically make it

## 03:25

possible to to operate a reactor and control a reactor and what we'll do today is understand how

## 03:30

to describe a reaction chakra and escape it from that reaction the moment we're going to use the
reaction

## 03:32

that keeps the reaction through its passive medium to the reaction develop that blocks that reaction
in

## 03:33

these feedback mechanisms and then dive in a little bit to uh actually characterize or quantify

## 03:39

some of them right with uh some homework problems and and some future stuff that we'll do um kind

## 03:45

of extending that so what is reactivity i probably used the word before right reactive or reactivity

## 03:58

obviously it's related to the word reactor and the word reaction we have reaction rates and so

## 04:04

that we've computed before for our reactor system but in your own words what is reactivity

## 04:10

anybody want to take a try play no you don't want to anybody yeah it's like similar to a

## 04:22

multiplication factor but um it's like the number of neutrons produced per uh i don't know uh but

## 04:31

related to multiplication factor yeah who agrees it's related to the mold

## 04:35

uh

## 04:36

the multiplication factor that's good that's certainly a takeaway you should get from from

## 04:42

the reading uh for today so what is reactivity all right so first of all we have k infinity uh

## 04:50

although it doesn't even have to be well yeah in this case k infinity is the appropriate label

## 04:55

right so it's the total fission rate over the total absorption rate we've talked about this

## 04:59

before gains to losses so if we wanted to get rid of the infinity we have to put leakage in the

## 05:04

bottom right but we don't have a mechanism to do that so we have to put leakage in the bottom

## 05:06

yet for for uh accounting for leakage so we'll still stick with this infinite system right so

## 05:12

k infinity is total fission rate over the total absorption rate but there's another quantity

## 05:17

called reactivity that we can use that is often more convenient right especially when we kind of

## 05:23

go back from chapter nine in the book to chapter five on kinetics where we look at the time

## 05:29

dependence of the neutron population the reactivity will be a significantly more convenient

## 05:35

quantity than the reactivity of the neutron population so we're going to go back to chapter

## 05:36

seven k infinity so the reactivity is defined as the difference between k infinity and one divided

## 05:43

by k infinity right so again when we get to something that has spatial dependence we can

## 05:49

drop the infinities but this the relationship will stay the same right in plain english and

## 05:56

this is the definition that i'd like you to to cut away in your minds yes question um is that

## 06:02

a p or is that rho that is rho okay right the greek letter

## 06:06

rho it's the most common sim i don't think i've seen another symbol used for reactivity

## 06:12

right but it's consistent with the book and this expression is equivalent to 9.1 in the book that

## 06:20

includes t for time right because the assumption is that we've already covered chapter five which

## 06:26

we have not okay so the plain english definition for rho that i'd like you to tuck away is it's

## 06:33

the relative departure from criticality

## 06:36

right remember k equal one is critical so by taking the difference of k infinity which might

## 06:43

be a little higher than one a little lower than one and then divided by k infinity this is a

## 06:47

relative departure from from from criticality if k infinity were equal to one exactly in the

## 06:53

system we're critical rho is equal to what zero right and so if i go above one i'm super critical

## 07:01

and rho therefore is greater than zero right and

## 07:06

uh contrarily if i were subcritical so k less than one then rho would be negative okay so

## 07:14

it it basically takes it it rescales our multiplication factor in such that zero is

## 07:21

now critical right so you want a reactivity of zero to be steady state okay and it's that that

## 07:26

fact that it centers at zero which makes it convenient for the time dependent stuff that we'll

## 07:31

do later on okay so as an example

## 07:36

just gently get into doing some work compute the reactivity associated with this eigenvalue

## 07:42

k infinity so you also hear me and you've probably heard me before all often called k or k infinity

## 07:50

the eigenvalue you remember we spent one day playing a little bit with numpy arrays and

## 07:54

matrices the two group problem that you've solved before where you got the flux ratio of 10 let's

## 08:00

say on the exam and you computed company you solved an eigenvalue problem it's just it was a two by
two

## 08:06

system with certain properties that made it very easy to solve right so that was one of the things

## 08:11

i saw on the homework is uh people wrote down a lot of things like basically copying and pasting

## 08:17

the uh matrix stuff without maybe recognizing that what we were doing all along solving the
eigenvalue

## 08:22

problem right anyway that's an aside but go ahead and compute the reactivity uh for for this i've

## 08:29

got myself a little computational cell here but somebody toss out a number when you get it

## 08:36

it comes to the name of three yes that's that sounds about right so i would take my row is equal

## 08:43

to 1.01 minus 1 divided by 1.01 and what i should get is 0.099 that whole thing repeating okay

## 08:57

all right that's fine that's a number okay and it gives us um the reactivity but so that you go
ahead

## 09:06

and jot that number down 0.099 okay but uh there are other ways that we can describe this reactivity

## 09:14

so just like the multiplication factor is unitless so is reactivity right so think about it k

## 09:19

infinity is what the reaction rate over a reaction rate per second over per second right you could
be

## 09:25

pedantic and say it's fissions per second over absorptions per second in which case you'd have

## 09:30

fissions to absorptions which it's not like it's not wrong but typically we

## 09:36

say that k is unitless and so that means reactivity is also unitless but more importantly

## 09:41

because k is this relative departure or sorry row is relative departure criticality you've got k
over

## 09:48

k and so the units would have to cancel out of it right so we can we can write down the number

## 09:54

like we just did the 0.099 repeating and the unit that we would assign that if we wanted to be very

## 10:00

clear about the unit or the lack of a unit is to call that dk over k right so it's a change in the

## 10:06

k relative to k it's exactly how rho is defined so if i don't if i don't give a unit

## 10:13

i mean dk over k that means just plugging in k infinity to that equation out pops a number but

## 10:19

there are two other units that are often used to scale that number to make it maybe easier

## 10:25

to understand or maybe it's for historical reasons the first one and this is one that'll

## 10:31

show up in reactor lab which i just found out today i'll be teaching so i'll be seeing you next

## 10:36

semester i hope that's not a bad thing in your uh opinion um but it's the reality and unfortunately

## 10:45

i'm not going to be teaching monte carlo uh because of that that's something the department

## 10:49

sort of pulled a fast one on unfortunately but i look forward to it because it'll let me extend

## 10:55

some of uh what i'm doing and uh sort of uh bring it all together anyway we'll see a dollar of

## 11:01

reactivity or cent right so we know dollars and cents is one cent is one hundredth of a

## 11:06

dollar but the dollar of reactivity is numerically equal to beta now beta is a number that i don't

## 11:13

think i've introduced before but we've talked about what it represents we know that neutrons

## 11:19

that come out of fission are mostly ejected immediately they show up immediately those are

## 11:25

called prompt neutrons but we know that from fission there are a number of these fission

## 11:30

products that are delayed neutron precursors that they're radioactive and one of the ways that they

## 11:35

get rid of their

## 11:36

energy is to pop out a neutron at some point in the future you remember that we have these

## 11:43

fission products that are almost always neutron rich and some of them are so excited that they

## 11:47

can pop out a neutron so beta is the fraction of all the neutrons produced from a fission event

## 11:53

that show up sometime in the future right so it's the fraction of neutrons that are delayed

## 11:58

or often it's called the delayed neutron fraction okay so that fraction beta for a uranium-235 field

## 12:08

reactor is roughly 0.007 it'll vary a little bit depending on the system but think of 0.007

## 12:18

as a representative value for plutonium it's lower it's 0.002

## 12:27

ish right these are sort of uh round numbers what um that will impact things on the

## 12:35

uh kinetic side because

## 12:38

smaller your delayed neutron fraction is the more your system dynamics depend on the fast or prompt

## 12:45

neutrons right we know the delayed neutrons they make this this sort of time constant row longer

## 12:52

than it would be if we just have the prompt neutrons so that that will be keep that in your

## 12:58

minds as we go on but that means that dollar if we use the dollar unit it's not absolute right it

## 13:05

depends on the system that you're talking about so for our reactor down and around the hall being

## 13:11

u-235 fueled its beta is you know 0.07 ish okay if we were talking about a sodium pooled fast

## 13:20

reactor which has a large fraction of plutonium 239 it's the beta would be uh considerably less

## 13:27

so reactivities when put in the dollar unit are not exchangeable between systems right that's one

## 13:34

reason why i don't really like it

## 13:35

you

## 13:35

because it has this implied system dependence okay the other unit the one that i do like quite

## 13:41

a bit is pcm or percent milling what this means is you take your numerical value that you started

## 13:47

with our 0.0099 and you divide it by 10 to the minus 5 okay so if you think about that we have

## 13:58

let's say so let's just say our reactivity is 0.01 so how many uh how many dollars would this be if

## 14:10

this were a uranium-235 system right so remember that beta beta is equal to 0.07 for u-235 okay so

## 14:22

if our rho is equal to 0.1 dk per k then rho in terms of dollars is equal to rho divided by beta

## 14:34

okay if we know that beta represents one dollar of reactivity then the number of dollars we have

## 14:40

have is our reactivity divided by beta, and that would give us a reactivity of $1.43, so $1.42

## 14:50

of reactivity. The value of the dollar unit will show up in kinetics, but it's pretty easy to

## 15:05

describe. Once you introduce a reactivity equal to a dollar or greater than a dollar, then the

## 15:12

delayed neutrons no longer matter, and your reactor will change according to the prompt

## 15:18

neutrons in their lifetime, which is much, much lower. That means that you will be increasing in

## 15:26

power very, very quickly, right? So reactivities that are greater than a dollar are something that

## 15:33

you don't deal with very often, right? In our reactor, we insert reactivities of a dollar or

## 15:41

more when we want to.

## 15:42

Pulse the reactor. Most reactors don't want to pulse. That's usually a bad thing, okay? So

## 15:48

dollars are great for large reactivities, right, for a given system. PCM, obviously a better unit

## 15:56

when we're dealing with very small reactivity. So what's the reactivity in terms of PCM?

## 16:03

Rho divided by 10 to the negative 5.

## 16:05

Yep. So 1e minus 5, so rho PCM would be about 1,000.

## 16:12

Okay. So just as, I guess, an example of where we could use these magnitudes, when we use OpenMC

## 16:28

through the unit cell classes, we get eigenvalues. And I actually just modified the script, and I'll

## 16:34

get that uploaded at some point for you to use. But you can get the uncertainty in your

## 16:41

multiplication factor from OpenMC. So you get, say, you get 1.3 as your k value. It will report

## 16:47

uncertainty in that value. And for the numbers that we've been using, that uncertainty tends to

## 16:52

be on the order of 0.001. So that means our k is, you know, 1.3 plus or minus 0.001. Now,

## 17:01

k is close enough to 1 in this case that the difference between, basically, that uncertainty

## 17:07

is like a reactivity, okay, or a delta reactivity. So the 0.001 in these same units would be 100
PCM,

## 17:17

right? 0.001. So rather 1,000 and 0.0, right? And then quite a bit less than a dollar reactivity.

## 17:25

So for just computing a k eigenvalue or multiplication factor, an uncertainty of 0.001

## 17:32

is reasonably okay. The challenge is, when you start taking differences of k, which is one way

## 17:39

that we'll be able to compute these reactivities, you're taking the difference of two numbers close

## 17:44

to 1.3. And then the uncertainty in that is going to remain. And then you're going to have a

## 17:47

difference of 0.001. So if you end up with a difference in k of 0.001, and you have an

## 17:52

uncertainty in that difference of 0.001, that's 100% uncertain, right? That's not good. So when

## 18:00

we do calculations with OpenMC to do these reactivities, we're going to have to increase

## 18:05

the number of particles that we use to drive down those uncertainties, okay? That's something I

## 18:10

point out in the homework statement for today's lesson. All right, so reactivity coefficients.

## 18:19

Are the thing that we use to quantify the feedback that this lesson is all about. So what we care

## 18:26

about is how the reactivity changes due to some change in a system property. What the book covers

## 18:32

and pretty much everything that I'm going to cover today, that parameter or the system property is

## 18:38

going to be a temperature. And it's either going to be the temperature of the fuel or the
temperature

## 18:42

of the coolant. There are other properties that can change that will impact the multiplication

## 18:48

factor. And therefore,

## 18:49

the reactivity, one of them would be densities. Another would be dimensions. These are much more

## 18:57

important parameters for fast reactors. But because when we're talking about dimensional changes,

## 19:02

we necessarily have to account for space. We're not going to cover them in any depth. And in fact,

## 19:07

the book doesn't cover them in depth. There's about a paragraph worth that covers some of the

## 19:12

differences between the reactivity coefficients for a pressurized water reactor, light water,

## 19:17

thermal spectrum reactors, and fast reactors. So

## 19:19

read that. And that'll basically be everything that we'll do for the fast reactors just because

## 19:26

we don't have the machine set up yet to cover some of those other influences.

## 19:34

All right. So let that property that we vary be x. So this could be a temperature for the fuel,

## 19:39

temperature for the coolant. What we want is to understand how rho changes when we change that.

## 19:45

So that's a derivative. That's how sensitive rho is to

## 19:49

change in that property. But because rho has this dependence on k or is defined in terms of k,

## 19:56

we can expand this total derivative into this product where we take the derivative of rho with

## 20:02

respect to k and then the k with respect to x. Have you seen partial differentiation before?

## 20:09

The way that this is set up is neat now because now if I had more than one parameter,

## 20:15

it would just be a sum of terms that look just like this. I would always have d rho dk,

## 20:19

but then I would have dk dx, dk dy. And when I say d here, I mean the partial derivative.

## 20:27

So what we want to be able to do is compute this derivative. And the first term on the right,

## 20:33

this d rho dk, that's something that we get directly out of the definition for rho. And

## 20:39

formally, it's 1 over k squared. But for some of the pen and paperwork that we do,

## 20:44

1 over k squared tends to be just a little too inconvenient. And so we make the approximation,

## 20:49

often, that d rho dk is 1 over k. Now obviously, 1 over k squared is not equal to 1 over k.

## 21:00

But it's pretty close when what is true. k equals 1 or k is very close to 1, which means that

## 21:09

this approximation is really valid only when we're nearly critical.

## 21:13

So that's actually a case that is often true. If we have a steady state reactor, we want to,

## 21:19

you know, what a small perturbation to, say, a fuel temperature will do. And if we're already

## 21:24

critical, then we can do this. Now this is all analytical. We can write this down directly.

## 21:35

A question for you is, if I didn't have this, if I couldn't compute this derivative,

## 21:43

and I were only able to compute single values of k, how might I

## 21:49

compute this derivative, d rho dk? I know what rho is as a function of k.

## 21:56

And suppose I want to compute this derivative, d rho dk. I can evaluate k for a temperature.

## 22:02

Let's call it 900 degrees Kelvin for the fuel. What could I do to approximate d rho dk?

## 22:10

What numerical approximation could I use to compute a derivative? Think back, I hope, to Me 400.

## 22:23

Although maybe that's not something that you covered in 400. How do you define the derivative?

## 22:30

It's not a slope, is it?

## 22:32

Well, the derivative is a slope, right? So in a sense, what we need to do is to compute a slope.

## 22:38

So remember, early in the class, we talked a very little bit about numerical integration. I offered

## 22:44

that little help session on that. Remember, what we did was to use either the trapezoid rule,

## 22:51

but I said you could use Riemann's sum. So in effect, numerical integration,

## 22:55

it's going back to KLT one or two, whichever you learned how to compute integrals,

## 23:00

and you actually take a step back. It's like, don't take that limit as the box size goes to

## 23:05

0. So the same thing can be done for derivatives. Remember, the definition of derivative is a

## 23:10

function evaluated at x plus delta minus f of x all over delta. Is that a ring of bell? What happens

## 23:18

if you don't let delta go to 0? You end up with something called a finite difference.

## 23:27

Have you ever heard of a function called the ling? Have you ever thought about that, and you
haven't?

## 23:28

finite difference approximation raise your hand if you've heard those words interesting all right

## 23:36

let me very very briefly go here what do we call secant uh sure yeah a secant line which you're

## 23:47

basically just taking two points and getting the slope near the point that you're interested in

## 23:52

yeah so um let me where am I here okay right so if I have a some function f and I want to compute

## 24:03

its derivative with respect to x right so my function is f of x then we know formally this

## 24:10

is equal to the limit delta goes to zero f of x plus delta minus f of x over delta

## 24:22

okay

## 24:22

now as long as f is a nice function in this limit exists blah blah blah all the other stuff that

## 24:29

you would have in a math class this this is what we would have right okay and call it f prime okay

## 24:36

so if we don't take that limit to zero what we end up with is just uh f prime of x is approximately

## 24:45

equal to f x plus delta uh minus okay for

## 24:57

for

## 24:58

some small delta obviously the approximation is better the smaller delta gets to a limit

## 25:07

if you make it too small then you run into numerical roundoff issues right because the

## 25:11

numbers that we use in python or matlab are not it's it's you have limited accuracy right limited

## 25:20

precision okay but for all intents and purposes we can use this sort of approximation okay so

## 25:27

I bring this

## 25:28

up because one this will be in the homework uh but two for for applications where we have sort

## 25:36

of a black box like openmc for k meaning that we give it some inputs and we get a k value to pop

## 25:43

out right we don't have functions that we can take derivatives of if we want to be able to compute d

## 25:48

rho dk then we need to get k at one value of the parameter and then k at that same value of the

## 25:56

parameter plus a little bit extra right so we get a k value of the parameter plus a little bit extra

## 25:57

right so we get a k value of the parameter plus a little bit extra right so we get a k value of the

## 25:58

or minus a little bit of extra right so if i were doing a fuel temperature coefficient right the

## 26:03

change in rho due to a change in the fuel temperature i might want to get k for a value

## 26:08

of 900 degrees for my fuel temperature and maybe k at a thousand degrees right how much that the two

## 26:15

values of the temperature differ depends on uh a couple things like how how accurately do you want

## 26:21

the derivative right do you want it to be very very precise um and if you're dealing with open

## 26:26

mc of course you have that uncertainty with k so if you take two k values at two temperatures that

## 26:31

are very close the difference in those k values is going to be very small and so the relative

## 26:36

uncertainty is going to be larger right so you've got to be careful about that too anyway that's d

## 26:43

rho dk now let me do this where uh it's that same crap where i'm gonna reload it so that it scrolls

## 26:57

for me there we go

## 27:02

okay so as in the book we can take this expression now that we have d rho dk is

## 27:09

equal to approximately one over k then we can actually take dk dx and expand it in terms of

## 27:16

the four factors right and so i won't go through that in derivation but this is equivalent to

## 27:22

equation 9.1 in the book okay this derivative d rho dx this is the reactivity coefficient right

## 27:31

so when we talk about the reactivity coefficient we're talking about the reactivity coefficient

## 27:32

we're talking about reactivity feedback and the coefficients that characterize that feedback

## 27:36

this is exactly what i'm talking about because if i know what d rho dx is for a given value of x

## 27:43

then if i know what delta x is some perturbation some change in a fuel temperature then d rho

## 27:49

dx times that delta will give me the change in the reactivity right so question

## 27:59

i've got these four factors that are driving my my reactivity coefficient right i've got the

## 28:05

fission factor resonance state probability uh the reproduction factor eta and then thermal

## 28:12

utilization cap if i'm changing the fuel temperature as an example which of these terms

## 28:20

is going to dominate the reactivity coefficient so suppose i i we're talking about a reactor

## 28:38

nominal conditions like a steady state fuel temperature might be 900 degrees kelvin for a

## 28:43

light water reactor pwr if i increase that

## 28:46

fuel temperature what physically is happening to the to the properties of the system the other

## 28:53

properties the nuclear properties of the system if i change the fuel temperature yeah doppler

## 29:07

broadening yeah yeah so what what is doppler broadening remember the the sort of analogy and

## 29:21

the reason for the name doppler was this idea of a siren you've got an ambulance that's going by

## 29:27

right you're standing there still

## 29:29

but as the ambulance comes it has one pitch and as it goes away it has a lower pitch

## 29:34

right the same thing happens to neutrons with resonances if a neutron is going toward

## 29:41

a moving nucleus the effective energy is higher than if the neutron is moving away

## 29:48

from the nucleus what that means for the resonances in that resonance region is the

## 29:55

following right so if i have if i have a resonance okay that looks like this okay

## 29:59

looks something like this right right maybe that's my resonance for uh at 6.67 ev or whatever

## 30:09

if i increase the temperature of the of the fuel then what i'm effectively doing

## 30:16

is broadening the range of energies that the neutron can be in order to land

## 30:24

in that resonance right the combined neutron energy and the combined thermal energy of the

## 30:29

nucleus the u238 in this case all they have to do is because it's their combined kinetic energy

## 30:35

that were um that that leads to the compound nucleus that's formed right so if that target

## 30:41

nucleus is moving that broadens the range of neutron energies that when combined with the

## 30:48

nucleus thermal energy leads to that resonant energy okay what that means graphically as i've

## 30:55

shown here is that the the cross section

## 30:59

broadens which if you remember this idea of neutrons slowing down from fast energies they're

## 31:04

bouncing around in the hydrogen or other moderating material and if this this resonance is broadened

## 31:11

meaning wider the real estate that the neutron can land in and be lost is greater right so if

## 31:18

i brought in the resonance more neutrons are going to land in the resonance and we know that

## 31:23

if a neutron lands inside of a resonance the chance that it's gobbled up to form you know

## 31:29

two-thirty-nine is is is higher okay it basically it's very high so we're increasing the number of

## 31:36

neutrons lost to resonance absorption the the factor of the four factors where this is uh

## 31:43

included is p the resonance escape probability so if i increase the temperature these resonances are

## 31:51

broadened the number of neutrons that make it past the resonances goes down what must happen to p

## 31:59

it decreases right so if p decreases then so too does k infinity and if k infinity decreases so

## 32:07

too does rho the reactivity so we should have an intuition for if my temperature in the fuel goes

## 32:15

up my reactivity goes down now if we're going to characterize this by the reactivity coefficient

## 32:21

which is this derivative d rho d t for the fuel what's the sign of that derivative

## 32:29

negative negative so when we talk about feedback being negative negative feedback that's

## 32:36

characterized by a negative feedback coefficient that's a negative derivative right so what that

## 32:42

means for the dynamics of a nuclear reactor is if i'm operating at steady state and something

## 32:47

changes about my system where my fuel temperature goes up what happens to my reactivity goes down

## 32:55

goes down if my reactivity goes down then my fuel temperature goes up and my fuel temperature goes

## 32:59

down then also my power will get down because if my reactivity goes down then my population will

## 33:05

start to decrease because i'm no longer at steady state and we know that um if i'm not if i if i'm

## 33:12

subcritical then the number of neutrons in each generation has to be less right i'm no longer

## 33:18

sustaining myself with this chain reaction so negative feedback in this case if i have like

## 33:22

an accident scenario where if i'm operating my reactor and somebody um somebody got their has

## 33:28

their cell phone and they have a nice plastic case that has uranium in it for whatever dumb

## 33:33

reason right that's going to increase my reactivity momentarily right because i'm adding new fissile

## 33:39

stuff but because the power then goes up that's going to drive these resonances more to be

## 33:45

broadened and that will have this negative um this sort of stabilizing effect on the reactivity

## 33:53

so the fuel temperature coefficient is dominated by by doppler broadening and

## 34:04

so in the book there are a number of equations that we can use to to explore this quantitatively

## 34:10

now last time i said that using something like openmc is great because it gives us access to

## 34:15

maybe the truest version of the physics right we're using the actual data

## 34:19

the stuff that's sort of encapsulated in these these equations is based on real data right for

## 34:25

instance this um this expression here for i remember i is uh the uh

## 34:34

resonance integral which is effectively a an average cross-section right the only thing it's

## 34:39

missing is that normalization by um where you divide by the total flux okay so this resonance

## 34:46

integral here which is from table 4.3 is specific to uo2 fuel it's one lump of fuel uh isolated

## 34:55

right but for as a function of temperature there's a reasonably straightforward relationship where

## 35:02

the the uh

## 35:04

resonance integral depends on the square root of the temperature so if i increase my temperature of

## 35:08

the fuel my resonant integral will increase uh as the square root of that temperature right it's

## 35:16

just something that you conserve and maybe it's something that you can actually show analytically

## 35:20

but uh this is the equation and then this gamma term is that that constant proportionality right

## 35:27

almost like a basically it's a derivative itself but this depends on whatever the fuel properties

## 35:34

are so we've got the density of the fuel which is usually 10 grams maybe 11 grams per cc and then

## 35:39

the fuel diameter right all these things come from experimental data and this would have been done

## 35:44

back in the 1950s by uh i think a guy named dresner if i remember correctly but the measure from

## 35:52

experiment so just like our cross-section data that we would use in openmc is measured from

## 35:57

experiments so too is this it's just this is a lot less detail right and we're making more
extrapolations

## 36:03

but

## 36:04

because of these reasonably straightforward equation we end up with a pretty straightforward

## 36:09

definition for the resonance escape probability right and once we can write it all down

## 36:13

mathematically that means that we can take things like derivatives and so forth okay so

## 36:19

if you look in the book i i don't think i have anything more on the slides

## 36:25

right but i do want to point out in chapter nine let's see where did it go

## 36:34

okay go back here switch to white okay so in the book there's equation 9.16

## 36:55

that says the following alpha f is equal to minus this lambda bar sorry gamma bar over two times

## 37:09

the square root of the

## 37:11

fuel temperature times the log of one over p of t not okay so let's break this down first of all

## 37:29

alpha is often the letter used for the the coefficient of reactivity so what this means is

## 37:38

this is d rho

## 37:42

d t f okay so we'll often use alpha to represent this derivative this change in rho

## 37:50

uh due to a change in whatever the parameter in this case uh the fuel temperature okay so it

## 37:55

basically if you took all those equations that i summarized on the slides put it put them together

## 38:01

and took the derivative you would end up with this uh expression this is the fuel temperature um

## 38:10

is it

## 38:11

is it and this is the fuel temperature

## 38:17

and this is some nominal fuel temperature where the resonant in the resonance integral

## 38:23

um that we saw before is evaluated this is going to be 300 k right sort of room temperature

## 38:31

now what i'd like you to do is take a few minutes substitute use those equations

## 38:39

and i want to see if we can come up with a numerical value for what

## 38:43

alpha f is okay and what i what i'd like to do is use the let's use the the nominal conditions

## 38:52

nominal parameters for our pwr that we've done with openmc so if you have your computer um

## 38:59

you could use the openmc to the unit cell you could plug in the default conditions

## 39:05

and you can get things like the number densities and so forth that you would need to to plug into

## 39:11

this expression okay so

## 39:13

let's say that i'm using this scale and what i mean is i'm going to put in i'm going to get my

## 39:21

openmc fired up here you can do the same thing but what i want to do is come up with this number

## 39:27

for the fuel temperature coefficient okay this is probably the one of the most important
coefficients

## 39:33

to have a sense for for what the the magnitude is all right so who i see about half of you have

## 39:39

computer so why don't you buddy up with somebody who has a computer and let's see if we can actually

## 39:43

Russians, right?

## 40:31

Yeah, wait, oh, that's a different.

## 40:34

So one of the things that I hadn't shown you,

## 41:26

but we have access to when you make the,

## 41:29

if I do PWR is equal to LWR unit self

## 41:32

with you could use all the defaults,

## 41:34

but here I'm specifically setting

## 41:36

the fuel temperature to 900.

## 41:38

When you get it internally,

## 41:39

there are a number of attributes

## 41:40

that represent the materials

## 41:42

that are actually given to OpenMC.

## 41:45

So if you create the PWR unit self

## 41:49

and you do PWR.fuel,

## 41:52

it will list out all the numerical properties

## 41:54

of the fuel that you need

## 41:56

for tackling a problem like this.

## 41:59

For instance, we have the density, right?

## 42:01

We have, of course,

## 42:02

we have the temperature

## 42:03

and then we have the nuclide atom densities, right?

## 42:07

So if you go back to,

## 42:09

or go up here to this definition

## 42:12

for the resonance escape probability,

## 42:15

one of the things that is needed is NFE,

## 42:22

which is the number density of the fertile fuel nuclide.

## 42:29

That's the U238, right?

## 42:31

Because the resonance escape probability

## 42:32

is all about resonance absorption in the U238.

## 42:34

So that would be the number density for the U238,

## 42:38

which we have automagically from OpenMC, right?

## 42:42

So we don't have to go and do the rho times NA

## 42:45

over the mass business that we've had to do before, okay?

## 42:49

And then the same thing can be done for the coolant.

## 42:51

So if I have PWR coolant,

## 42:57

then I have the number densities for the water.

## 43:00

Now notice, because under the hood,

## 43:03

I'm using the built-in, right?

## 43:04

Built-in elemental tables.

## 43:09

In nature, all water or all hydrogen is not just H1, right?

## 43:14

There's some small fraction that is the H2.

## 43:17

You don't have to account for the H2

## 43:19

in what we do up here, right?

## 43:22

So in the resonance escape probability,

## 43:24

there's also in the denominator, the fuel volume,

## 43:27

we have C for the moderator,

## 43:30

which remember that's the log that,

## 43:33

that,

## 43:34

that goes down decrement, what we called it.

## 43:37

And for water, it's less than one, right?

## 43:39

So for hydrogen, it's one.

## 43:41

For water, it's like .9 on change, right?

## 43:44

So that's, I think what's in chapter two of the book.

## 43:48

Then we have the scattering cross-section,

## 43:50

which we also have values of the cross-sections

## 43:54

in the book, in chapter three, right?

## 43:56

So you have everything that you need

## 43:58

in order to evaluate that with OpenMC helping a little bit.

## 44:02

So let's go ahead and, and dive in, and turn it off.

## 44:04

and try to get numbers for that, okay?

## 44:07

Anybody without a partner with a computer?

## 44:11

Anybody?

## 44:12

That's somebody.

## 44:13

Maybe not.

## 44:14

I don't know what it is, but what's the name?

## 44:17

That's what it is.

## 44:18

Yeah, what's his name?

## 44:20

Who are you?

## 44:21

What's his name?

## 44:21

Have you ever logged on Android's file?

## 44:24

I don't know, not yet.

## 44:25

Yeah, okay, thank you.

## 44:26

Yeah, so, I mean, you could use,

## 44:30

you could actually just log in and use the,

## 44:32

I mean, you can use the numbers that I have here too, right?

## 44:34

You don't have to actually do it yourself

## 44:37

if you don't want to log back in,

## 44:39

but you could log into on-demand

## 44:41

and use that lesson 19 notebook

## 44:46

that you'd already been using, right?

## 44:48

So you should all have that,

## 44:49

and you could just either copy that or add some new cells.

## 44:55

But these are the numbers that you would need.

## 45:08

Let's see, what else?

## 45:09

Is there any information that you don't have

## 45:12

that you would need, right?

## 45:18

So just kind of walking through, right?

## 45:21

We know what row is, right?

## 45:23

That's given in the output, that was the pangram.

## 45:25

We know what the, do we know what the diameter is?

## 45:30

Let's see, what do we have?

## 45:31

So we have PWR, fuel, let's see, radii.

## 45:49

So I've used the default.

## 45:50

So the fuel radius is 0.45.

## 45:52

I think that's the only thing that we didn't have.

## 45:55

Oh, what are you trying to find here?

## 46:05

What do we want?

## 46:07

What is the, what were you doing?

## 46:11

You give PWR, it's gonna be able to be large in itself.

## 46:14

Oh, yeah.

## 46:15

The ramage itself is, yeah, it's like, yeah.

## 46:21

Right.

## 46:53

Let me see if I can.

## 47:51

So looking back at this equation,

## 47:53

what you need first to do is compute

## 47:56

the resonance escape probability

## 47:57

at that nominal temperature of 300 K, okay?

## 48:02

And then we have gamma, that was one of the equations,

## 48:05

and then it's just whatever our fuel temperature is.

## 48:07

So really the challenge here is just plugging numbers

## 48:10

into the resonance escape probability.

## 48:31

It's more than one surprise change.

## 48:36

Well, I don't know if that's gonna be resonant

## 48:37

or if it's going to be resonant .

## 48:49

I don't know, but we don't know what that is.

## 48:51

No problem.

## 48:52

I think everything that we need to get

## 48:55

just by defining the PWR options, right?

## 48:58

And really this is just to save me time

## 49:00

on looking at the number that .

## 49:05

Is there anything that you thought?

## 49:07

No, I sometimes, I was just looking at this equation.

## 49:12

I have learned that I had a question about .

## 49:17

So now when you say that, what's the solution there?

## 49:22

.

## 49:27

I think the low level of inaudible

## 49:30

we might have to do the .

## 49:34

Or actually, I'm giving one to .

## 49:39

Right, so you've just gone down to the .

## 49:41

Okay.

## 49:42

You've just stolen the bubble .

## 49:43

Yeah, yeah.

## 49:44

Have you been .

## 49:46

Perhaps .

## 49:49

So raining some .

## 49:50

Going down.

## 49:51

Going down. Correct.

## 49:52

once you've run up one that helps you report up then you should be able to go back

## 50:04

i think it's one nine two but but that's what i did

## 50:22

um

## 50:39

they have documentation it's um i don't think it said you know

## 50:55

this uh

## 51:12

you can actually go ahead and look at the what i've done this last week

## 51:17

i did not make it very good

## 51:25

object of the rules and flatting materials right now but i'm accessing this and then

## 51:31

there's a lot of radii are stored and then you know only you have to be funded

## 51:40

there should it shouldn't be too much um like that in there

## 51:47

it's not super obvious

## 51:52

is that what you're asking about yeah okay

## 52:00

we got numbers

## 52:05

and now we got it

## 52:22

let me know

## 52:29

uh

## 52:41

um

## 52:52

uh

## 52:55

yeah

## 52:57

arbitrary because that's exactly what uh

## 52:59

This is part of what you're doing for the homework, not necessarily using OpenMC, but being able to
substitute the values into the various expressions.

## 53:09

So we're over time now.

## 53:14

So what I'd like to do is probably pick this up next time.

## 53:19

I guess I spent more time kind of explaining reactivity than I figured I would.

## 53:25

So we'll wrap this up next time and then finish the rest of the things that I want.

## 53:29

Which will set us up nicely for next week to move on to something else.

## 53:35

So take a look at the homework.

## 53:37

So the homework will be due at 5 o'clock on Friday.

## 53:40

We'll cover a little bit more on it.

## 53:43

But take a look at the homework and come in ready to ask questions about it.

## 53:46

I think it's straightforward, but because I'm having you use OpenMC, again, beyond just what we did
last Friday, which was submitting kind of what we did in class, you've actually got to use it.

## 53:56

Get a start on it so that you can come in and make use of it.

## 53:59

And then we'll wrap up the time that we have on Friday, okay?

## 54:02

All right.

## 54:03

Then I will see you then.
