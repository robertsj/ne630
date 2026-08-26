# L11 Local Audio Transcript

Course: NE 630

Playlist source: https://youtube.com/playlist?list=PLy481lNHlnHoEO95vM-xYX2bydD25v20L

Video: NE 630 - Lesson 11

URL: https://www.youtube.com/watch?v=9EPWVcwoR4Y

Video ID: 9EPWVcwoR4Y

YouTube upload date: 20230915

Duration: 54:08

Transcript source: Local faster-whisper transcription from YouTube audio.

Whisper model: large-v3; detected language: en.

Generated: 2026-06-28

Note: This transcript is machine-generated from audio and lightly wrapped only. It should be reviewed before being quoted, published, or used as polished lesson text.

Requested language: en

## 00:42

All right. So can folks hear me? I see a thumbs up. Can I get a few more thumbs up? I see two.

## 01:00

I see three. All right. That suggests then that I'm connected. I don't have a camera.

## 01:07

Man, has my morning been not what I expected. I have that laptop in class and I brought it

## 01:15

on this trip and I realized that on the other side, I didn't have the charger I thought I had.

## 01:21

And so I had to use my desktop and just a technology switch, but I believe everything is

## 01:27

set now. So let's go ahead and dive in to lesson 11, which is an extension of what we discussed

## 01:40

in lesson 10. Let me maximize.

## 01:45

This screen. So, and I'll get rid of the participant thing. Okay. So what we talked

## 01:52

about last time in lesson 10 on Wednesday was what happens when we bring back the resonance

## 01:59

absorption to this problem of neutrons slowing down, slowing down in purely elastic scattering

## 02:05

media, pretty straightforward because the solution ends up being just C over E, right? It's a one

## 02:15

over E times sigma S of E. But the basic solution form was pretty straightforward and you could all

## 02:24

verify that for yourself. And in fact, that's something you'll have to do for the homework,

## 02:27

plug it back into that integral expression and voila, you get back out what you put in.

## 02:31

What we did is we added the resonance absorption and we made some approximations about the shape

## 02:37

and size of the resonance relative to the amount of energy that neutrons lose as they,

## 02:45

say, scatter with the nuclides in the medium. We know that if a neutron scatters off a low mass

## 02:53

moderating nuclide, then it will scatter down on the average, pretty far in energy space. And for

## 03:01

the most part, bypass lots of resonances. So the resonances are small relative to that amount of

## 03:07

energy a neutron can lose when it scatters off of say hydrogen. For scattering off of the heavier

## 03:13

nuclides that represent the fuel, say uranium-238, the amount of energy lost is much smaller than

## 03:20

when a neutron interacts with hydrogen. And then there's a question, how big is the resonance

## 03:24

compared to that? Because if that energy loss is also larger than the resonance, then things are

## 03:30

pretty easy. What it meant for us is that the flux for most of the energy range through that

## 03:35

resonance region looks like one over E. And so we just use that shape in all of the integrals,

## 03:40

which makes the integral something that we can evaluate. And all of the energy loss is

## 03:43

ultimately what that gives us is this form for the narrow resonance flux. So let's see if I can

## 03:51

get some, choose pink, right? So the expression that is shown in the book is this thing where

## 03:59

I've added a little bit of notation here. So this EF is the cutoff before the fast energy range.

## 04:06

So this is what we've been calling or setting equal to 0.1 MeV, right?

## 04:13

Slowing down decrement with the bar is the average. So that's averaged over the things in

## 04:18

this material, right? It might be water mixed with U-238, but the basic shape is this. So because

## 04:25

this value of the slowing down density Q is a constant, right? That's just whatever the slowing

## 04:30

down density is at that cutoff energy. This thing is a constant. And so we're left with the fluxes

## 04:37

one over E times the sigma T. So I always think of it as being proportional to sigma T,

## 04:43

over E, sigma T times E, right? When we use the flux in a few lessons, specifically on Monday,

## 04:52

when we talk about, Monday and Tuesday, when we talk about effective cross-sections,

## 04:57

what we're going to do with the flux is use it as though it's a probability density

## 05:01

in energy. And so what we'll do is produce weighted averaged cross-section values so that

## 05:08

we can start computing reaction rates without dealing with that mess of energy dependent

## 05:13

cross-sections. And so what we're going to do is use it as though it's a probability density

## 05:13

cross-sections, right? So what we're trying to do is move toward a simpler representation of the

## 05:18

cross-sections so that we can get a little bit more done with the reaction rates and our balance

## 05:24

equations and so forth. The other thing that we talked about at the very end, and I don't feel

## 05:30

like I did a great job in explaining it, is this resonance escape probability. So what I've done

## 05:36

here is I've repeated what I ended with, and I've modified the notation just a little bit. So what I

## 05:42

mean by this sub i is for a resonance i, so this is for the i-th resonance. Okay, I've got to

## 05:58

admit one more person. Okay, so that's for the i-th resonance. And what I mean by that is, hey,

## 06:05

we've got all of these resonances for, say, U238, and this is the i-th one. So this is resonance i,

## 06:15

so this would be EI and EI plus one, right? So it's just kind of a generic way to say, hey,

## 06:22

when we're passing from this energy down through this energy, this is the expression that we have,

## 06:27

and it's just the absorption cross-section over that decrement times sigma T of E over E,

## 06:34

right? It's our narrow resonance flux plugged back into that, okay? So what's neat is we can

## 06:40

use this thing for multiple resonances, right? So if I want the total resonance,

## 06:45

resonance escape probability, P, that's going to be P1 times, we've got some, another

## 06:52

late tendy. Hopefully nobody had issues getting in. So send a message if you're having any

## 07:03

technical issues. Maybe I should check. Is there anything with comments? I don't see any.

## 07:12

There's a chat. Nothing in the chat. All right, cool. So this,

## 07:17

total escape probability is equal to the product of all the individuals, right? So we have a P1

## 07:22

times a P2 times P3, blah, blah, blah, blah, blah, to Pn, where n is the number of resonances here.

## 07:31

So because this probability expression is an exponential, well, we know that an exponential

## 07:38

times an exponential is just another exponential where the arguments are added. So that means that

## 07:44

we have something like...

## 07:47

Like E to the minus E1 to E2 with the arguments minus E2 to E3, so on and so forth. Well,

## 07:59

that's just equal to the integral from our very lowest energy that we care about,

## 08:05

which would be about 1EV all the way up to our maximum of 0.1 MeV with the same sigma A E dE over...

## 08:19

Squiggle, see the slowing down decrement, and then E, okay? So this is kind of like the

## 08:29

total resonance escape probability through all that. And the reason that I point out

## 08:36

the resonance escape probability here, we'll see it again in the chapter four material,

## 08:40

is because when we make the assumption, the assumptions that we do for the

## 08:45

narrow resonance flux spectrum, what we end up with is a flux spectrum that looks like this.

## 08:53

Basically, this is the one over E part of it, okay? But then we have these superimposed squiggles,

## 09:01

the dips that we see from resonance energy self-shielding. But what we don't account for

## 09:06

in that neutron flux is the fact that as neutrons go to the left in energy, the number of neutrons

## 09:13

slowing down tends to decrease, right? So the slowing down density that is discussed a bit more

## 09:21

in the book, in a purely scattering...

## 09:23

... system is unchanging. It's a constant. Whatever neutrons you have born from fission,

## 09:28

they're going to show up at all of those lower energies at a given time. And so in steady state,

## 09:33

pick any energy you want, the number of neutrons that's going past that energy is going to be

## 09:37

constant. That is not the case when you have absorption. It can't be because you're losing

## 09:41

neutrons along the way. And so what the actual shape would look like is on the average, something

## 09:48

that is close to the one over E, but it'll be damped a little bit. And so those little resonance

## 09:53

dips will be down a little bit lower. And this is something I didn't even really appreciate until

## 09:59

kind of having to put together material for courses like this one, because it's not something

## 10:05

that is maybe highlighted in the introductory material. Just kind of an aside, the pedagogical

## 10:14

tools, you know, the sort of illustrative methods, examples, and so forth that you see in a textbook

## 10:19

like ours and in earlier ones are based on...

## 10:23

Sort of thought processes that happened in the 70s and earlier. Most of those things aren't

## 10:29

totally relevant to sort of the practical use of the data using numerical methods and so forth.

## 10:35

It's more about understanding the principles, but that doesn't mean that... It doesn't mean

## 10:40

that that's the best way to represent the material. And so what I'm trying to do is kind of

## 10:47

put things together that helps explain why certain features of one approximation don't quite get

## 10:53

everything right. The narrow resonance spectrum is pretty good, but if you try to use that over

## 10:58

the entire energy range, you're missing out on the fact that a lot of neutrons are gone in that
lower

## 11:03

energy range. And so you'll be weighting things in a biased way when we get to that cross-section

## 11:09

stuff. So put them together though, and you have sort of the big picture. You have this

## 11:13

fine detailed spectrum from the narrow resonance approximation and this resonance escape
probability,

## 11:19

which you can evaluate also as a function of energy, right? You just choose which resonance

## 11:23

sequences you want to include going from the highest ones to the lowest ones can account for

## 11:27

the reduction in the neutrons. So any questions about that before we sort of move on to what we'll

## 11:34

deal with today, which is the thermal neutron spectrum? All right. I've waited my awkward five

## 11:46

seconds. Okay. So let me go ahead and put my lines here.

## 11:59

Oh, this interface is not letting me move it the way that the other one did. That's all right.

## 12:10

Okay. So what we're doing today is understanding what neutrons do below that thermal cutoff,

## 12:20

which we have said is about 1 eV. And I'm going to use E sub TH to represent this cutoff.

## 12:32

TH is equal to 1.0 eV.

## 12:34

Okay. So, and then E F for the fast is equal to 0.1 m eV. All right. So in order to understand

## 12:50

the spectrum of neutrons below that 1.0 eV mark, we have to go back to the balance equation. And

## 12:56

so like we did for the slowing down, we're going to ignore fission. All right. So that

## 13:01

was one of the major assumptions. For now we'll allow for absorption, which we took away originally

## 13:07

for slowing down. So what we'll keep the absorption, but there's one approximation

## 13:11

that we made in slowing down and that, that we are going to move away from. So in slowing down,

## 13:17

we had a sigma S from E prime to E was equal to zero. If E prime was less than E, right?

## 13:32

What this means is that the probability that a neutron scatters from a lower energy to a higher

## 13:37

energy is zero, right? Neutrons in that slowing down or resonance regime can only go down in

## 13:44

energy, right? Because there's no mechanism for them to gain energy or the mechanism is it, as

## 13:50

we'll kind of see the mechanism is there, but it's, it's sort of inconsequential, right? When, when

## 13:57

looking at the relative magnitudes of energy. So what we're going to do in for the thermal neutrons.

## 14:04

So for thermal neutrons,

## 14:08

we're going to say that this scattering cross section is not necessarily equal to zero for

## 14:18

E prime less than E. Okay. And so what, with this kind of idea, we can write down the balance

## 14:25

equation as we've done before, right? So we'll have sigma T of E, T of E, right? That's our

## 14:32

total interaction rate. That's the rate at which we are deleting neutrons from that, that energy.

## 14:38

They might not be deleted from the system,

## 14:40

but they might move to another energy. In this case, it might be a higher energy. Okay. So we've

## 14:45

got an integral bound from zero all the way up to E divided by alpha, right? So I'll treat this for

## 14:54

a single scattering isotope at the moment. What is that? That's interesting. Okay. So sigma S E
prime to E,

## 15:05

P of E prime, D E prime. Okay.

## 15:12

That's just the same balance law that we started with when dealing with slowing down. Okay. But

## 15:19

what we'll do is we'll take this integral and we'll split it into two parts. We're going to

## 15:23

have a part that's below the thermal cutoff, and then we're going to have a part that is greater

## 15:30

than, I guess, equal to the thermal cutoff. Okay. And so what this looks like then is we'll have an

## 15:38

integral from zero up to that thermal cutoff.

## 15:42

Now, we have this scattering cross-section that allows for neutrons to go up in energy. And we'll

## 15:48

talk in just a moment about what that cross-section form looks like. What does it look like? We know

## 15:56

what it looks like for slowing down. That's the one over one minus alpha E, right? But we don't

## 16:04

know what it would look like for neutrons to be able to gain energy. Okay. And so then we also

## 16:10

have the

## 16:12

thermal cutoff to e over alpha with the rest of this stuff what i'm going to do is call this

## 16:21

whole integral above the thermal energy cutoff as s right this is going to be my in scatter

## 16:33

uh maybe that's not the way i want to call it uh down scatter source let's see down scatter

## 16:40

source okay how did that happen interesting um all right at any rate so there we go

## 17:05

all right so um move this up now if we further ignore absorption for just a moment we don't

## 17:26

have to ignore and we cannot ignore absorption but if we ignore uh both the absorption and that

## 17:32

source term so for now we're going to ignore uh

## 17:38

sigma a and that slowing down source s if we do that then the balance equation that we have to

## 17:47

satisfy is sigma s of e phi of e is equal to that integral from zero up to our thermal cutoff

## 17:57

with this scattering cross section okay we have to satisfy that um and that's fine i mean that

## 18:14

looks like our balance equation

## 18:15

that we've already dealt with but in order for this to be satisfied our scattering cross section

## 18:23

and our flux has to satisfy the following we have our scattering cross section from e to e prime

## 18:35

times phi of e and this has to be exactly balanced by the cross section from e prime to e

## 18:48

times phi of e prime now that seems a little strange like why why would that necessarily be so

## 18:57

well if you take this expression and you integrate over uh e

## 19:10

prime in the range zero to eth then what you recover is what we started with okay so

## 19:21

it's it's at least consistent with our original uh balance law okay what this thing is called if

## 19:29

this thing is true this is called detailed balance and probably the first time i ever heard that
term

## 19:39

was when i was sitting in your shoes in a class like this learning about reactor theory and what

## 19:44

thermal neutrons do i think i heard about it again when i later had a class uh on statistical

## 19:51

physics it's like thermodynamics

## 19:53

but in the physics building okay what detailed balance is is a statement that says hey for every

## 20:00

process in your system in our case that process might be a neutron scattering from an energy e to

## 20:06

e prime we've already been familiar with this e uh this higher energy to lower energy uh interaction

## 20:14

right that that's what we saw throughout the slowing down process what detailed balance

## 20:18

requires is that for every process there is a reverse process

## 20:23

and the two processes the first one like slowing down and the the reverse i guess the up scattering

## 20:29

happen with exactly the same frequency on the average doesn't mean that for every down scatter

## 20:37

there is immediately an up scatter but it means that if you took a while and you and you counted

## 20:42

all of the down scatters from some energy down to a lower energy then during a similar period of

## 20:48

time you would see roughly the same number going from that lower energy back up to the

## 20:53

to the the higher energy right it's all about on the average and that that's something that

## 20:58

that you'll see in any discipline that's related to a statistical treatment what we're doing with

## 21:05

the neutron balance equation uh the past couple days everything that we're talking about is on

## 21:11

the average because we know that behind the neutron flux is this neutron density and the

## 21:17

neutron density is the expected number of neutrons at this point in time and that's the

## 21:23

point in in in three-dimensional space between e and e plus delta e you could toss in some angles

## 21:30

and all that other stuff but it's it's just the average quantity there if in a real system that

## 21:36

average will be the center of a distribution right you're not always going to have exactly

## 21:40

10 neutrons at some point in space it'll be 9 or 11 or whatever but on the average it'll be 10

## 21:46

and the equations that we're using represent that average all right so detailed

## 21:52

balance equation is the same as the equation that we're using and the equation that we're using

## 21:53

itself is pretty complicated it goes all the way back to the late 1800s when uh ludwig boltzmann

## 21:58

i believe it was his name uh anyway you've certainly heard of boltzmann uh he's the one

## 22:04

who who applied this principle and came up with the h theorem and this that was like a starting

## 22:09

point for proving the second law of thermodynamics right that entropy you know always increases

## 22:15

so that's that's kind of that now uh

## 22:21

what boltzmann also showed is that for a system of particles that satisfies this

## 22:27

detailed balance the distribution of those particle velocities or equivalently their

## 22:33

energies must follow a certain distribution and for our case the neutron uh the neutron energies

## 22:40

in terms of the flux must satisfy or must must exhibit the following uh energy distribution

## 22:49

in fact i'll i'll show you how to do that in just a moment but i'll show you how to do that in just
a moment

## 22:51

i'll use uh proportional to okay and we have the very famous boltzmann or maxwell

## 22:59

maxwell boltzmann distribution so boltzmann did a lot of this work maxwell about 10 years before him

## 23:05

had already been looking at some of this stuff and so as things go it's always a combination

## 23:09

of ideas so this this is the maxwell boltzmann distribution in energy i think in chapter two

## 23:15

we we also saw a maxwell boltzmann distribution um that might have been in terms

## 23:21

of velocity you can always change variables as we've seen before uh going as there's a one-to-one

## 23:27

correspondence between kinetic energy and the uh the neutron speed so you can change variables

## 23:33

you'll get a different functional form uh but they're equivalent through that transformation so

## 23:37

this is this is the distribution of neutron energies in a purely scattering system that

## 23:45

has reached thermal equilibrium right so in this equation we have

## 23:51

t

## 23:51

is the temperature of the system and that's in kelvin we have this constant k is

## 24:05

boltzmann's constant boltzmann constant which i'm i'm guessing you've seen that before in a

## 24:14

physics class uh whether you've used the same numerical version of it or not i'm not sure

## 24:19

and for our purposes it's easy to use uh an approximate value of

## 24:24

8.62 times 10 to the minus 5 ev per kelvin okay and importantly this product kt is

## 24:38

the most probable most probable energy of particles that follow that distribution right

## 24:50

it's not the average energy you can compute the average energy uh but it's the most probable and

## 24:54

you get that of course by taking this flux taking the derivative with respect to the

## 24:58

energy and doing that i don't know why i keep zooming that's a little bit bothersome okay

## 25:06

now what does this spectrum look like go ahead and here okay so so the maxwell boltzmann

## 25:30

distribution looks something like this and my artwork is not perfect here obviously okay and so

## 25:40

this is this is

## 25:41

the case where we have zero absorption right exactly what we've been talking about that kind

## 25:47

of led to this distribution now in reality the neutrons in a nuclear reactor are not in a purely

## 25:55

scattering medium we have absorption can anybody tell me what the shape of the absorption cross

## 26:03

section is as a function of energy for basically everything that we've seen so far that has an

## 26:08

absorption cross section either unmute or

## 26:13

put it in the comments i'll quickly uh go over to the comments a good guess uh danny gossian so i'm

## 26:30

thinking so if you imagine uh the hydrogen one absorption cross section the n gamma cross section

## 26:36

how does that depend on energy as you go from right to left it tends to go up in energy right

## 26:43

anybody else want to offer a guess earn some brownie points as it were attenuation

## 27:00

exponential. It kind of looks exponential on a certain plot. Logarithmic, not quite, no.

## 27:16

Remember, the way to remember it is blank absorption. It's a blank absorption or a one

## 27:23

over blank absorption. Anybody else? Take the low-hanging fruit. Linear? That's not linear.

## 27:38

All right. One over V. So it's close to one over E. So there are two things that we'll have to

## 27:51

remember. So there's, yep. Thank you, Brian. The one over V. So most absorption cross-sections

## 27:58

as a function of E tend to go as one over the square root of E, which is equal to,

## 28:05

or proportional to one over V. Okay.

## 28:10

One over E, one over.

## 28:12

One over V. Are those linear? I don't think I would call that linear, right? Because if it's

## 28:18

one over E, to be linear represents a proportionality where one over E tends to

## 28:28

infinity as E goes to zero, right? So that, like the function itself doesn't look like a line.

## 28:35

Um, and the same would go for one over V, right? But the key thing here is that it,

## 28:42

because that absorption cross-section is not a constant, right? It will preferentially delete

## 28:48

the neutrons on the left-hand side of the spectrum, right? So if we have a one over V,

## 28:53

I, I, I guess I'll try to draw it like this, right? So this is our, our one over V or a one

## 29:00

over square root. So if I'm a neutron over here, I'm, I'm preferentially being deleted from the

## 29:06

system. What that means then for this detailed balance is that things will shift to the,

## 29:12

to the right. Okay. So if I go up in absorption cross-section, I will shift this distribution

## 29:18

to have a peak that is elsewhere. And if I continue to do so, it will keep moving to the

## 29:27

right. I'm, I'm exaggerating these, these curves quite, quite a bit, right? So we have,

## 29:32

um, in this case, this would be like moderate values of sigma A and this yellow one would be

## 29:42

I values of sigma A. And we can treat this, uh, I mean, certainly we can, we can apply numerical

## 29:50

methods to all of this. So when it gets down to actually modeling systems, some of this stuff

## 29:56

just kind of naturally is treated. But if we want to understand conceptually how it can be tackled,

## 30:02

one way to do so is to, to, to look at these peaks. If I, if I'm moving the peak from here

## 30:08

to here or from here to here,

## 30:12

the, the peak of the distribution is moving to the right, which means that KT is moving to the

## 30:19

right, which means that I can choose a higher temperature to model the, the Maxwellian, uh,

## 30:25

distribution. And so, um, for what we can do is for, uh, sigma A not equal to zero,

## 30:35

choose some effective temperature that is greater,

## 30:42

then the, the physical temperature, right? So if we have a, a reactor system at, you know,

## 30:47

a hundred degrees Kelvin, then the neutrons in that system, assuming that there is absorption

## 30:53

will exhibit a distribution that is closer to a temperature, say of 120 Kelvin, right? The exact,

## 31:01

uh, increase for the effect of temperature, uh, totally depends on the system. But the idea

## 31:06

is that you can model it and that's still, it's just a model, which means it's an approximation.

## 31:11

It's not,

## 31:12

physically the same thing. It's not to put absorption in does not mean that the, the,

## 31:17

the temperature of the neutrons has increased. But if we, if we view the peak as being KT,

## 31:24

then out pops this effective temperature that might give us a better fit. Okay. So do I have

## 31:32

any more in the chat? All right. Cool. All right. Um, all right. Quick example.

## 32:00

So that we get some numbers to, to stick

## 32:03

in that bucket of important numbers. Uh, what is the temperature for the neutrons

## 32:17

that we've talked about before at 0.253 EV, or that somebody had mentioned in classes

## 32:28

going at about 2,200 meters per second, right? The, that energy, a neutron energy of 0.0253 feet,

## 32:36

five to 0.0253 EV,

## 32:38

corresponds to 2,200 meters per second. And if you've done, if you've looked at those

## 32:44

cross-section files that either I've given you, or that you've gotten from the NNDC,

## 32:48

there is always a value at 0.0253 EV. That is the standard energy at which a, a thermal

## 32:56

neutron cross-section is evaluated. And then using certain functions, we can evaluate the

## 33:01

cross-section at other energies, but that's the one that's tabulated most often. Okay. So what,

## 33:06

how do we compute this?

## 33:07

Okay.

## 33:08

Well, and specifically I, I want it in degrees F. So even though I've spent years now working in,

## 33:16

in a science field and I've been exposed to Celsius or Kelvin, I still don't have a feeling,

## 33:23

just like I don't have a feeling for kilograms, right? The best way that I've even gotten a sense

## 33:26

for kilograms is watching like powerlifting and strongman competitions where they use kilograms.

## 33:32

Like that, that's where I'm developing a sense. It's not from this repeated exposure. So maybe

## 33:37

some of you are like me and you can't think in terms of Celsius or Kelvin. And so Fahrenheit

## 33:42

is helpful. So let's, let's compute that temperature in Fahrenheit.

## 33:46

So the, the solution, obviously this is a pretty trivial problem, I think, but we take the energy

## 33:53

253 EV. We divide it by that Boltzmann constant that I gave you before, right? That's EV per

## 34:03

Kelvin and out pops 293.6.

## 34:05

Okay.

## 34:05

Okay.

## 34:06

Okay.

## 34:06

Okay.

## 34:06

Okay.

## 34:07

Okay.

## 34:07

Okay.

## 34:07

Okay.

## 34:07

Okay.

## 34:08

Okay.

## 34:08

Okay.

## 34:09

Okay.

## 34:09

Okay.

## 34:10

Okay.

## 34:10

Okay.

## 34:11

Okay.

## 34:11

Okay.

## 34:12

Okay.

## 34:12

Okay.

## 34:13

Okay.

## 34:13

Okay.

## 34:14

Okay.

## 34:14

Okay.

## 34:15

Okay.

## 34:15

Okay.

## 34:16

Okay.

## 34:16

Okay.

## 34:17

Okay.

## 34:17

Okay.

## 34:18

Okay.

## 34:18

Okay.

## 34:19

Okay.

## 34:19

Okay.

## 34:20

Okay.

## 34:20

Okay.

## 34:21

Okay.

## 34:21

Okay.

## 34:22

Okay.

## 34:39

Okay.

## 34:39

Okay.

## 34:40

Okay.

## 34:40

Okay.

## 34:41

Okay.

## 34:41

Okay.

## 34:42

Okay.

## 34:42

Okay.

## 34:43

Okay.

## 34:43

Okay.

## 34:44

Okay.

## 34:44

Okay.

## 34:45

Okay.

## 34:45

Okay.

## 34:46

Okay.

## 34:46

Okay.

## 34:47

Okay.

## 34:47

Okay.

## 34:48

Okay.

## 34:48

Okay.

## 34:49

Okay.

## 34:49

Okay.

## 34:50

Okay.

## 34:50

Okay.

## 34:51

0.6 C, right? And how, yeah, so, but it helps to go from, from Celsius to Fahrenheit because then,

## 34:58

then at least I remember the, uh, conversion a little bit better, right? I think from Celsius

## 35:10

to Fahrenheit, it'd be 20.6. Then we multiply that by nine fifths. Is that correct? I'm using

## 35:18

the wrong side of this thing. Plus 32. And if we do that, that should give us something like 69

## 35:25

degrees F, right? So 69 degrees F is within a couple of degrees of what I keep my own house at,

## 35:35

right? So when we talk about thermal neutrons, when, when, when folks say, oh, it's at room

## 35:41

temperature, literally the 0.0253 EV neutron is, uh, that energy corresponds to something that is

## 35:48

just about our typical room temperature, right? Of course, in winter, mine's closer to 65 and in

## 35:54

summer, closer to 70.

## 35:55

Because I'm a cheapskate, but you know, that's beside the point. All right. So, uh, sort of an

## 36:16

obvious question remains, what the heck is the scattering cross-section? Where do we get this

## 36:23

thing E to E prime that allows for upscatter? Okay. Sometimes for, for the, this application

## 36:36

to thermal neutrons, this, uh, cross-section is called a scattering law, or at least is generated

## 36:43

from something called a scattering law. So, uh, so, uh, so, uh, so, uh, so, uh, so, uh, so,

## 36:44

scattering law. All right. The details are really, really beyond our scope. Uh, I would say

## 36:51

that that's something that would, that belongs in an advanced reactor physics class. Although one

## 36:55

could argue that it belongs in a solid state physics class as well, because a lot of, of

## 37:00

neutron scattering applications are kind of in the reverse direction where neutrons are used to

## 37:06

understand the properties of materials. Okay. On the flip side, what the materials do to the

## 37:12

neutrons, uh, can be, uh, can be, uh, can be used to understand the properties of materials.

## 37:14

Uh, pretty, pretty varied and quite complicated, right? So these scattering laws typically are

## 37:21

measured, right? They'll either measure neutron scattering directly or some, some other function

## 37:28

of the material, or, uh, it can be, um, predicted through modeling, right? And by modeling here,

## 37:38

I mean some sort of, of, uh, lattice dynamics simulation. Uh,

## 37:44

it could be, uh, um, uh, with quantum mechanics as well. Most of the systems that we care about

## 37:51

are solid materials. There are some liquids like water and such, but a lot of things that we care

## 37:55

about are, are, um, solid like graphite, for instance, solid carbon. It's got a crystalline

## 38:02

structure that is, uh, very important, um, with respect to its impact on, on neutron energies,

## 38:08

right? So these scattering laws are typically measured or modeled. Um, the,

## 38:14

uh, scattering law depends on material properties like crystalline structure. So I believe you all

## 38:26

take, uh, one credit or maybe a sequence of, uh, one credit classes in the chemical engineering

## 38:31

department that teach you a little bit about material structure. So you should, you should

## 38:35

have heard the term crystalline structure, whether you remember the details or not,

## 38:40

uh, is not terribly important, but you'll know that, you know, maybe, maybe you have something,

## 38:45

um, uh, that's, that's, that's, that's, that's, that's, that's, that's, that's, that's, that's,

## 38:46

uh, a lattice system that looks like this, right? So this, uh, what was it? BCC, no face-centered

## 38:52

FCC, face-centered, face-centered cubic, something like that. So you have a certain interatomic

## 38:58

spacing that I'll, I'll just say D and that D might vary depending on which, which two atoms

## 39:03

you're talking about in a lattice system. Well, when neutrons get down to the energies that we're

## 39:07

talking about, their effective wavelength, their de Broglie wavelength becomes of the order of the

## 39:14

interatomic spacing. And necessarily we, we, we, we, we, we, we, we, we, we, we, we, we, we, we, we,
we,

## 39:16

we get these interference effects. Those interference effects show up pretty strongly

## 39:21

in the effective cross-section, right? Because if neutrons of certain energies are able to just

## 39:25

kind of buzz through a lattice because, uh, you know, everything was kind of constructive or

## 39:29

destructive or whatever, then that's going to show up as a function of energy in that cross-section.

## 39:34

Okay. Uh, the other thing that, that they depend on these scattering laws

## 39:39

on molecular binding. Okay. So think of water. We've got two,

## 39:50

uh, H2O, eight, uh, two hydrogen, one oxygen bound with, uh, their electrons with binding

## 39:58

energies on the order of several EV. Okay. So when the neutron at these low energies interacts

## 40:05

with the hydrogen, well, that hydrogen is not alone. It's not a free nucleus, which is kind

## 40:10

of the model that we've talked about with all the neutrons scattering so far, like the neutron comes

## 40:15

in, hits this isolated nucleus. Well, at those energies, you can't think of that nucleus as

## 40:20

being isolated.

## 40:20

Right. Because the neutron at a thermal neutron energy is lower than those binding

## 40:26

energies. So when the neutron hits that hydrogen, that the recoil is not just the hydrogen,

## 40:32

it's going to be the hydrogen connected to the other hydrogen and the oxygen in this,

## 40:36

this whole molecule that tends to have a pretty big impact. And in general, it increases the

## 40:42

effective cross-section. Okay. So if I'm scattering with a bound nucleus, in this case, it's kind of

## 40:50

like a, um,

## 40:50

uh, sort of like an infinite binding. Uh, so it's an approximation, but the, the bound cross-section

## 40:58

goes something like one plus one over a squared times, whatever the free cross-section is. So

## 41:11

for, for hydrogen, if we just had hydrogen alone, hydrogen never shows up as single, uh, single

## 41:18

atoms, right? They always bind together. It's a H two. It's always a diatomic. So,

## 41:23

for hydrogen, of course, a is as, uh, small as it can go. So what we end up with is one plus one

## 41:29

squared. So two. So for hydrogen, the bound cross-section typically is about four times

## 41:38

the free cross-section. So if we get the cross-section data from somewhere like NNDC,

## 41:44

that's evaluated for a single nucleus in practice, though, we would have to account for that binding

## 41:49

effect. And the cross-section ends up being quite a bit larger. And this actually has a pretty big

## 41:54

impact on, on the flux.

## 41:55

So if we took a look at the thermal neutron, as I guess, even the full spectrum of, uh, you know,

## 42:01

like a thermal spectrum reactor, we'll have a max volume peak, the one over E and then something to

## 42:07

do with fission, right? But if we have this binding effect, what tends to happen is it,

## 42:12

it sort of hardens the spectrum a little bit. So when, when we shift from left to right going in

## 42:18

higher energy, like what happens to the Maxwellian, when we add absorption, we call that a spectral

## 42:24

hardening.

## 42:30

And that matters if we're dealing with a thermal spectrum reactor, because all of our fission is

## 42:36

happening at those lower energy. So if we're shifting neutrons for whatever reason to higher

## 42:40

energies, we've got to account for that in our numerical models of the reactor, right? So, uh,

## 42:46

this binding effect is important. So the details kind of beyond us outside of this little, um,

## 42:52

cartoon, right. But, uh, it's, it's important to be aware of. And finally, I guess the final point

## 43:00

I want to make is that these laws, uh, are major, a major part, major part of nuclear data. So I've

## 43:17

said, at least in passing something about NDEF data, that's, that's the format that everything

## 43:24

starts in. That's where the resonance parameters are. That's, uh, obviously a huge part of the data

## 43:29

that we've used so far.

## 43:30

Okay.

## 43:31

Yeah.

## 43:31

of all that nuclear data are the scattering laws for the various nuclei that we care about,

## 43:37

right?

## 43:38

When they're in combination with others, whether it's a certain crystalline structure, right?

## 43:42

You can have different forms of metallic structures, right?

## 43:47

Different phases.

## 43:48

So the crystalline structure can change and you need a scattering law for each one of

## 43:52

those.

## 43:52

Those are also included as part of the evaluated nuclear data.

## 43:56

So when you use a code like FITS or MCNP or OpenMC, not only do you have to get the

## 44:03

cross-section data that we've seen before, right?

## 44:06

This is either the resonance parameters that lead to the tabulated cross-section that we

## 44:11

can actually use in practice, but you need this scattering law as well, okay?

## 44:15

And so I'm hoping that at some time in the next couple of weeks, we'll get to do some

## 44:20

examples with OpenMC.

## 44:22

I'm trying to set it up so that we can use it either locally on campus.

## 44:26

I'll set up a server to do some Jupyter notebooks, or we'll try to do it with Google

## 44:31

Colab.

## 44:32

The installation kind of makes it a little challenging, but with small enough data sets,

## 44:37

it should be doable.

## 44:38

And I'd like to actually show you how we get that nuclear data, including the scattering

## 44:43

laws, and use that in some simple models, whether it's infinite, medium, homogeneous

## 44:48

systems like we've been discussing so far, or smaller unit cells that'll be closer to

## 44:53

what we talk about when we get to chapter four.

## 44:56

So these scattering laws, as what I've said so far, makes it seem like they're total

## 45:03

black magic and that we'd never be able to do anything with them.

## 45:09

It turns out, though, that there are some analytic models, right, for the simplest cases,

## 45:15

and one of them we can write down, right?

## 45:19

So there are a close format, even approximations for hydrogen and oxygen in water.

## 45:24

There is a scattering law.

## 45:26

From, I think, the 1960s or something, Nelken.

## 45:30

But the one that is reasonably straightforward is for free gases, right?

## 45:37

Doesn't matter what's in the gas.

## 45:40

It could be uranium.

## 45:41

Not that I'd want to be exposed to a uranium gas, but it's this idea of having a nucleus

## 45:45

that is free in a gaseous state at some temperature, right?

## 45:50

So it accounts for the fact that this thing is, on the average, these nuclei are moving

## 45:54

around with some sort of...

## 45:56

kinetic energy that can be given to the neutron.

## 45:59

The closed form for arbitrary mass number A is pretty long-winded.

## 46:05

It would be like a...

## 46:06

I would take like 20 minutes to write it down, probably.

## 46:09

But for A equal one, it's pretty straightforward, and it looks like this, okay?

## 46:19

We've got the scattering from E prime to E, and it looks, let's see, we've got a scattering

## 46:27

cross section.

## 46:28

E prime, okay, got an exponential, E prime minus E over KT, and the error function, which

## 46:48

hopefully you've heard of before, maybe you haven't used it much, shows up a lot in heat

## 46:53

transfer in certain systems, especially time-dependent problems.

## 47:00

And so this...

## 47:17

This is if E prime is less than E, and this is if E prime is greater than equal to E.

## 47:25

And when I write this sigma S here, that's sigma S in the absence of thermal motion, right?

## 47:40

So that would be sort of the low-energy sigma S that you would get from the NNDC, right,

## 47:46

without caring about...

## 47:47

Without caring about what the temperatures are in the system, okay?

## 47:51

So what does this thing look like is probably the last thing that I want to kind of sketch

## 47:58

out for you, and for this case of hydrogen, it looks as follows.

## 48:08

So we're going to plot against the ratio of energies, right?

## 48:14

So E over E prime is one if it's, you know, E to itself.

## 48:19

If it's less...

## 48:20

If it's less, then we are upscattering, and if it's greater, then it's downscattering.

## 48:29

Okay, so get a couple things here.

## 48:34

And so I will do something like this, okay?

## 48:46

So that's if the energy of the neutron is equal to KT, right?

## 48:52

So this, of course, will depend on what the starting energy is of the neutron E, okay?

## 48:57

And then it scatters to...

## 48:59

The other energy, okay?

## 49:05

And then this would be something like, say, 4KT.

## 49:16

And then if we keep going up in energy, this kind of flattens out,

## 49:24

and it'll kind of just be like a step function eventually.

## 49:29

I'm really not doing a good job of that attenuation there.

## 49:32

That would be like 25KT.

## 49:35

So looking at this, I'll see if I can find a digital version of this to give you, too.

## 49:40

But the idea is that the higher the neutron energy is, the less likely that it can upscatter, right?

## 49:49

So for the highest energy neutrons in the range of interest,

## 49:52

basically in the limit of infinite energy, what we end up with is just pure slowing down, right?

## 50:00

But when we have lower energy, we have a certain probability of upscattering, right?

## 50:05

And that's what drives this detailed balance, right?

## 50:09

You couple this...

## 50:10

You can do this with the Maxwellian, and you get detailed balance.

## 50:12

The neat thing about the detailed balance that...

## 50:15

I can't prove it.

## 50:19

I've never seen the proof of it, is that the Maxwellian distribution is the distribution no matter
what the scattering law is.

## 50:28

As long as that scattering law satisfies the detailed balance, there could be many of them, right?

## 50:32

So for free gases, this is what we have.

## 50:34

If we're dealing with graphite, it would be a different scattering law, but it, too, would satisfy
this detailed balance.

## 50:40

And we would end up with a Maxwellian, right, in the absence of absorption and so forth.

## 50:46

So this is kind of the last little bit that I wanted to talk about.

## 50:51

What this means for us as we move forward is the following, right?

## 51:00

And this is kind of what we'll pick up on Monday, is we have a neutron flux that's a function of
energy.

## 51:09

And this...

## 51:09

This thing will be equal to whatever our fast flux is, right?

## 51:14

For 0.1 MeV less than E, less than, say, 10 MeV, it'll be equal to our intermediate flux for
energies between, say, 1 Ev up to that fast cutoff of 0.1 MeV.

## 51:29

And it'll be our thermal flux for energies less than 1 Ev, right?

## 51:36

And so for the fast flux, we saw that it's driven...

## 51:39

It's driven largely by that chi spectrum for the intermediate energies.

## 51:43

It's 1 over E with the fine structure given by the wide...

## 51:47

Sorry, narrow resonance.

## 51:48

Or, as you'll see in the homework, there's a wide resonance approximation that accounts for this
self-shielding.

## 51:54

And then as neutrons get to this thermal energy, we have the Maxwellian distribution that kind of
drives things, right?

## 52:03

And these three things together, if we can connect them across those energy barriers,

## 52:09

at least an approximate spectrum that we can use for defining things like this.

## 52:16

If I wanted to compute an effective cross-section, what I'll do is integrate it over everything with
my energy-dependent flux, right?

## 52:30

And I'll normalize it by integrating whatever that flux is to give me the normalization constant.

## 52:40

And when you take these two pieces...

## 52:42

Together, right?

## 52:43

Where this coupled with this, that's turning the flux into a probability distribution.

## 52:50

Dividing by that integral is the normalization.

## 52:54

And using this to define an effective cross-section will simplify our life significantly, okay?

## 53:03

So look for a page posted for Monday sometime in the next couple of days.

## 53:10

And what we'll do for Monday, Tuesday, and Wednesday, primarily, is just...

## 53:13

Just working with effective cross-sections and the balance equations that we get when using them

## 53:19

in place of the full energy-dependent cross-sections that we've seen so far, right?

## 53:25

Any questions?

## 53:27

Any questions about this?

## 53:28

Obviously, things are kind of free.

## 53:30

You can leave if you want.

## 53:31

If you've got questions about the homework, I can answer some of those, too.

## 53:39

Any issues with the homework?

## 53:49

All right.

## 53:51

Then have yourselves a great weekend.

## 53:53

And we will reconnect in the...

## 53:55

Same manner on Monday, okay?

## 54:00

All right.

## 54:00

Take care.
