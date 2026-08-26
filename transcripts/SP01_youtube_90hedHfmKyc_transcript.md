# SP01 Local Audio Transcript

Course: NE 630

Playlist source: https://youtube.com/playlist?list=PLy481lNHlnHoEO95vM-xYX2bydD25v20L

Video: Spatial 1 - Diffusion in 1-D, Slab, Non-Multiplying Systems

URL: https://www.youtube.com/watch?v=90hedHfmKyc

Video ID: 90hedHfmKyc

YouTube upload date: 20221129

Duration: 38:36

Transcript source: Local faster-whisper transcription from YouTube audio.

Whisper model: large-v3; detected language: en.

Generated: 2026-06-28

Note: This transcript is machine-generated from audio and lightly wrapped only. It should be reviewed before being quoted, published, or used as polished lesson text.

Requested language: en

## 00:01

So today we'll talk about diffusion in a one-dimensional slab non-multiplying system.

## 00:07

The reading for this is 6.1 through 6.4 in the textbook.

## 00:11

It's a fairly straightforward read.

## 00:14

Some of what I'll talk about today is the same as what's in there.

## 00:17

My notation differs a little bit, and I think it's a little simpler notation.

## 00:22

You may disagree, and let me know if you do.

## 00:25

By the end of today, what I'd like you to be able to do is to write down the diffusion equation,

## 00:29

especially for this case of a 1D slab system, with appropriate boundary conditions,

## 00:34

and when we get to them, continuity conditions,

## 00:36

and then I want you to be able to solve the simplest slab problem.

## 00:40

If you can become an expert with this simple slab problem,

## 00:44

the rest of diffusion theory, in whatever context you might find it,

## 00:47

will be much, much more straightforward.

## 00:53

So remember that this all started on day one with the transport equation.

## 00:58

We've already gone through sort of a heuristic derivation of the transport equation.

## 01:01

Here I'm just going to write.

## 01:02

I'm going to write it down for you in the case of no energy dependence, all right?

## 01:06

So we have the simpler form here, where the unknown in question is psi, the angular flux,

## 01:11

and that depends on the location in space, and then this angle, omega hat.

## 01:16

The hat indicates a unit vector, right?

## 01:19

Its norm is one.

## 01:21

And on the left-hand side, we have the streaming term,

## 01:23

and that represents the change of the neutron density

## 01:26

due to the neutrons leaving a location in space, right?

## 01:30

They're streaming away.

## 01:31

We also have neutrons leaving the phase space due to collisions, right?

## 01:35

Whatever kind of collision it is, it's going to change that neutron.

## 01:38

It's going to delete it.

## 01:39

It's going to change its direction.

## 01:41

If we add energy, it would change its energy, so on and so forth.

## 01:44

So the left-hand side are all those things that will remove a neutron from a point in phase space.

## 01:49

Our phase space here is a differential spatial volume, right?

## 01:53

Dx, dy, dz, and a differential solid angle element, right?

## 02:00

In an element of 4 pi.

## 02:02

On the right-hand side, we have all the sources of neutrons.

## 02:05

So we have neutrons scattering from some angle omega prime to omega.

## 02:10

Sometimes you'll notice I have typos.

## 02:12

I don't have the hats.

## 02:13

Omega is always a unit vector, okay?

## 02:15

And so we have all those neutrons scattering from one direction into the direction of interest.

## 02:20

We could have fission, in which case our fission neutrons are emitted into our direction of
interest,

## 02:25

isotropically in this case,

## 02:27

and then we could have an external source.

## 02:30

A little s, which depends on r and omega, okay?

## 02:34

Remember, the units here are important to keep track of

## 02:37

because that will make sure that your equation is correct, right?

## 02:42

So the angular flux has units of per centimeter squared, per second, per steradian, okay?

## 02:47

And then the external source really drives what the unit of the whole equation is,

## 02:52

and that's per centimeter cubed, per second, per steradian.

## 02:56

If we had energy, we would also have per eV.

## 03:01

We can simplify.

## 03:01

We can simplify this a little bit if we assume that the scattering is isotropic.

## 03:05

We don't really need to do this, but it helps me give you a simpler form of the equation.

## 03:10

We don't have to quite be this explicit with our approximations.

## 03:14

But if we assume that the scattering law from omega prime to omega is isotropic,

## 03:20

meaning that there's no dependence on the sort of difference in those angles or the cosine between
them,

## 03:25

then we have sigma s of r over 4 pi.

## 03:27

That means any scattering angle is equally likely, okay?

## 03:30

And that's true.

## 03:31

For some systems, it's a good approximation for some.

## 03:34

It's not a good approximation for others.

## 03:36

But with this approximation, our equation simplifies to what's shown here as equation 2, right?

## 03:41

And we can break it.

## 03:43

Basically, we get rid of the integrals, and we get the right-hand side in terms of the scalar flux,

## 03:48

which is the integral of the angular flux over the 4 pi.

## 03:57

Integrals over 4 pi are actually kind of hard to imagine, right?

## 04:01

Because really, we know that the angular variable is a two-dimensional complex.

## 04:05

We have an azimuthal angle around some polar axis,

## 04:08

and then we have the angle made with respect to that polar axis.

## 04:11

So it's two-dimensional.

## 04:12

So really, when I write down an integral of 4 pi,

## 04:16

that's sort of a shorthand for a two-dimensional integral.

## 04:20

That integral is easiest to see in spherical coordinates.

## 04:23

So if I want to define the scalar flux phi of r,

## 04:26

I have to integrate psi, but I can break up psi into the two angular components.

## 04:31

So I have phi here, a slightly different form of phi,

## 04:34

so that we don't confuse it.

## 04:35

We'll put the flux, and then theta.

## 04:37

So phi is our 0 to 2 pi azimuth angle about the z-axis,

## 04:43

so straight up is usually what we take to be the polar axis.

## 04:46

And then we have the angle theta,

## 04:49

which goes from pointing straight down, negative pi, to straight up, pi.

## 04:53

And then we have d phi, and then sine theta d theta.

## 04:57

If you remember back from Calc 3,

## 04:59

the differential volume element in spherical coordinates

## 05:03

always has this strange sine theta d,

## 05:05

and you can justify that through geometry.

## 05:09

I won't get into that here.

## 05:10

But because of that, we can make a substitution

## 05:12

where we say mu is equal to cosine of theta,

## 05:15

so that d mu is equal to minus sine theta d theta,

## 05:18

and we get a slightly simpler integral.

## 05:21

And this helps us later in transport theory

## 05:23

if you ever find yourself in a course that covers that more explicitly.

## 05:28

So we have the transport equation.

## 05:31

It's kind of ugly, and what we struggle with is the fact that it's an integral.

## 05:35

It's an integral differential equation.

## 05:36

It's great that we can track these neutrons in their angular space,

## 05:39

but the equations are too hard for us to solve

## 05:42

given the mathematical tools that we have at this point in our sort of curriculum.

## 05:48

So what we need to do is find an alternative approach.

## 05:51

And what we had done earlier is to take that equation

## 05:54

and try to get rid of the angular variable.

## 05:58

So first of all, let's get ourselves a shorter version of the equation,

## 06:02

which I've listed here as 5.

## 06:04

All I've done is,

## 06:05

I've taken all those right-hand side terms,

## 06:07

the sources, right, external source, vision source, scattering source,

## 06:11

and I've just collected that into this term called Q.

## 06:14

This is often called the emissivity, right,

## 06:17

just basically all those neutrons that are emitted at that point in phase space.

## 06:22

And then I've also switched the order of the gradient operator,

## 06:26

sometimes called nabla, I don't know why, and omega.

## 06:30

And the reason for that is the gradient is a spatial derivative,

## 06:34

and omega is an angle.

## 06:35

So it doesn't have any spatial dependence, so we can switch the order.

## 06:39

Once I've done that, things get a little bit easier to do, okay?

## 06:45

So what I'll do is I'll take that equation, the simplified equation with Q on the right-hand side,

## 06:51

and I'll integrate it over the 4 pi, right?

## 06:54

So we've seen how that looks.

## 06:55

I have to break it into those two components,

## 06:57

but I'll keep it in the simpler notation here in equation 6.

## 07:00

And what I get is this, okay?

## 07:02

That's really ugly, all right?

## 07:03

I've got d omega omega psi.

## 07:05

What the heck is that?

## 07:06

Well, it turns out that that integral is known as the angular current.

## 07:10

We talked about this a little bit in class, and what the, what, what the angular,

## 07:14

sorry, the integral is, is the current, the, the, the argument of that integral,

## 07:20

so the, the omega times psi is the angular current.

## 07:23

And when we integrate it, we, we get this current vector.

## 07:26

And what the current vector tells us is something about the flow of neutrons in a certain direction.

## 07:33

And the easiest way to interpret that is to,

## 07:35

imagine some differential surface area element, right? Take some big sphere and just carve out

## 07:42

a small little chunk of it. And what we want to know is the net number of neutrons flowing through

## 07:47

that surface. Well, the way we get that is to take j, this current vector, and dot it with n hat

## 07:53

times whatever the area of the surface element is. That tells us what the net number of neutrons is.

## 08:00

So j is always useful when we talk about neutron preservation or continuity, making sure that we're

## 08:06

keeping track of all the neutrons. So with this current vector, we can greatly simplify the

## 08:12

equation that we had above, right? This one here, number six, okay? The challenge is with this

## 08:18

continuity equation is maybe obvious, right? We have our favorite scalar flux. This is a thing

## 08:26

that we've used. We probably saw it in an earlier class. But now we have a

## 08:29

second scalar flux. And we have our favorite scalar flux. And we have our favorite scalar

## 08:30

flux. And we have our second scalar flux. And we have our second scalar flux. And we have our

## 08:30

unknown and worse this unknown is a vector and if you're like me you

## 08:35

probably get a little bit uncomfortable when you have to do vector or deal with

## 08:39

vector unknowns in a differential equation because that means your

## 08:42

differential equation is definitely a partial differential equation that makes

## 08:47

things a little bit harder but anyway let's take this continuity equation and

## 08:50

try to simplify it a little bit okay well first of all here's an example what

## 08:57

would the equation 8 be this continuity equation what would this look like for

## 09:01

the case in which the neutron flux and the neutron current vary only along the

## 09:06

x-axis all right so think about what that that the gradient operator is it's

## 09:13

just a spatial derivative along the X and the Y and the C coordinates

## 09:17

separately and there's some with the appropriate unit vectors so in Cartesian

## 09:22

coordinates the X components will be along I hat right the x-axis

## 09:27

right so the X-axis is the gradient operator and the X-axis is the gradient

## 09:27

right and so when we dot that together we get I hat DX and then that's dotted

## 09:32

with I hat J X the X component of J however because we don't have any

## 09:36

dependence on Y and Z we can get rid of that X subscript which is the same

## 09:40

subscript used in the textbook and we end up with this thing on the bottom

## 09:44

right where we we have DJ DX and this should not I can't tell if that's

## 09:48

actually bolded or not let's make sure it's it's not bolded you do you do yes

## 09:58

yes not bolded okay right it should not be bolded because at this point it's

## 10:03

scalar because it's the dot of this I hat term and this I hat term so it's

## 10:07

just DJ DX plus the other stuff that we've seen before again this doesn't

## 10:12

really get us anywhere because we still have two unknowns J and Phi and so the

## 10:16

question is how can we relate the two of them to reduce this equation to an

## 10:21

equation in just one unknown and this is where something called Fick's law of diffusion is
happening.

## 10:28

shows up. Okay, Fick's law of diffusion says that the current vector is equal to minus d times the

## 10:36

gradient of phi, right? So basically we're taking the spatial derivative of the scalar flux in each

## 10:41

of the three directions and then multiplying it by some coefficient called d, whatever d is. We

## 10:47

call it the diffusion coefficient. Now because you are all, or most of you, are in simultaneously
the

## 10:54

heat transfer, you've seen Fourier's law. And Fourier's law is exactly this form. You take some

## 11:00

sort of diffusion coefficient, in the case of Fourier's law, that would be the thermal conductivity,

## 11:07

and you multiply it by the gradient, or in a one-dimensional case, the derivative of the

## 11:13

temperature, right? And this is how we can relate the changes in temperatures to this thing driving

## 11:19

it. And the thing that drives the change in temperature is a change in heat in the way we

## 11:24

quantify.

## 11:24

That is through a heat flux, okay? So the diffusion equation in neutron land is no different

## 11:31

from the heat conduction equation that you've seen before, with one small exception, and that's the

## 11:39

interaction term. That's the sigma times phi. We don't have temperature interacting and deleting

## 11:46

itself in a typical conduction problem. You have to go into some wild areas of heat transfer to

## 11:51

find something like that, okay? But otherwise,

## 11:54

the nomenclature is basically the same. Okay? Now, what is this diffusion coefficient?

## 12:02

In a class like heat transfer, you're given a heat conductivity. In a class like, you know,

## 12:06

reactor physics, I could just give you a diffusion coefficient, but there is a way to define it more

## 12:11

formally, and from transport theory, you end up with something that looks like this, where we have

## 12:16

1 divided by 3 times sigma t minus mu hat sigma s. Now, you might not remember what mu hat is,

## 12:23

but it's the

## 12:24

average cosine of the scattering angle. So when a neutron scatters off some target nucleus, it will

## 12:30

go off at some angle, right? The angle between its original and final trajectory is some number,

## 12:38

right? And the cosine of that is mu. Well, the average value of that cosine is mu bar, and we can

## 12:45

define that formally, right? And we did that before in class, and it turns out a good approximation

## 12:51

is 2 over 3a, where a is a cosine of the scattering angle, and the cosine of that cosine is mu bar.

## 12:54

So if we have a light element like hydrogen, that cosine tends to be about 2 over 3. And if you
think

## 13:01

about the cosine, a cosine of 1 means an angle of 0, right? So a cosine of 2 over 3 is reasonably

## 13:10

close to 1, which means it is forward peaked. On the average, neutrons that scatter with hydrogen

## 13:16

in the laboratory system will tend to keep going in a forward direction, right? That's not
isotropic,

## 13:23

right?

## 13:24

particularly true for hydrogen and other light elements, okay? You can take a look at this little

## 13:29

note here in the slides that I'll give you, but I put it in green here as sort of an aside.

## 13:36

Now, if we make the substitutions that we just saw, we get the neutron diffusion equation. So,

## 13:43

we put Fick's law into our continuity equation, and we end up with equation 10, and that should

## 13:48

look reasonably familiar to you, right? If you get rid of this term here, the interaction term,

## 13:54

and the other interaction terms, we have a change in something, a second derivative of something is

## 14:00

equal to a driving term. That's like Fourier's law, okay, in the conduction equation. All right,

## 14:06

now, if we're only going to do one-dimensional slab geometry, which means that the variation of

## 14:12

the physical properties, the fluxes, the currents, all that stuff, is only along the x-axis, then

## 14:17

what we have is equation 11, okay? And if we have the one-group approximation, where we assume

## 14:23

that we have one-dimensional slab geometry, and we have one-dimensional slab geometry,

## 14:24

just like we've been doing so far, that there is no energy dependence, then all this stuff on the

## 14:28

right-hand side, specifically the sigma sub s, the scattering, that can be brought over to the

## 14:33

left-hand side. So, sigma t minus sigma s gives us sigma a, right? I think I can draw on here. Can I

## 14:40

draw on here? Nope, that's not. Yeah, there we go. Yeah, so sigma a is just this thing right here

## 14:47

minus this thing right here, okay? I would commit equation 12 to memory. This is sort

## 14:53

of the bread-and-butter equation for reactor physics, and we'll see this for the rest of the

## 15:00

time we have, which, admittedly, is not too long, but it'll help if you remember. All right, so

## 15:07

we have this diffusion equation. We can write it down, but we need to say something about it,

## 15:17

okay? We can't just solve it. We have to have different conditions. So,

## 15:21

one of the things that we have to keep in mind is,

## 15:23

the things we're modeling are physical quantities. The neutron density is really

## 15:29

under the hood of this whole thing, and the neutron density is, the term density, anyway,

## 15:37

suggests that we're treating the neutrons as some sort of continuous fluid. Now, we know that

## 15:42

neutrons are discrete creatures, and that in a reactor, the density of neutrons is nowhere near

## 15:47

the density of atoms in, say, water. However, the math that we're using,

## 15:53

ignores that fact, right? When we write down anything with these derivatives and such,

## 15:59

we are treating it as a continuum. So, what we have to enforce is a continuity of the neutron

## 16:05

density. That means we can't have any, like, step jumps in the density of the neutrons.

## 16:10

That means that we can also not have any jumps in or discontinuities in the neutron flux,

## 16:15

because the flux itself is just a constant, right? The velocity times n of x, okay? Now,

## 16:21

that's one continuity constraint.

## 16:23

A second one is that the neutron current is also continuous, right? We cannot have discontinuities

## 16:30

in this, and that makes sense because the neutron current represents this net flow of the neutrons

## 16:35

in a particular direction, okay? So, the continuity equations that are defined here for the flux and

## 16:42

for the current, these are important when we have models where we have discontinuities in the

## 16:48

material properties. Now, we can definitely have material property discontinuities. I can have a

## 16:53

lump of fuel next to a lump of moderator. There's nothing that says that the properties have to be

## 16:58

continuous along the x-axis. We can definitely make very heterogeneous slab reactors, right,

## 17:08

which is exactly what we see in reality, heterogeneous systems, okay? But the solution,

## 17:15

at least in this diffusion theory framework and even before that, the transport theory framework,

## 17:20

requires that the solution is required to be continuous.

## 17:23

Okay? The other thing that we have to do is define boundary conditions, right? By the time we get to

## 17:31

the diffusion equation in the slab system, we have a second-order ordinary differential equation,

## 17:36

and so we have to have two boundary conditions, usually imposed on either side of the slab,

## 17:42

okay? The fixed flux condition is perhaps the easiest boundary condition to impose,

## 17:48

and that just says, hey, we've got the flux at some boundary, and the model problems that I'm

## 17:53

going to show you are going to be very different. So, we're going to have two boundary conditions,

## 17:53

and that just says, hey, we've got the flux at some boundary, and the model problems that I'm going
to show you

## 17:54

will have a left-hand boundary at x equals zero and a right-hand boundary at x equals a, right?

## 18:00

Just keep that nomenclature set. We'll use that for, I think, all of our problems. So, a left-hand

## 18:05

boundary condition will be at zero, and the right would be at a, and so I can just fix phi of zero

## 18:10

to be some phi naught and phi of a to be some phi sub a, right? Just values, right? Could be zero,

## 18:15

could be non-zero, whatever it is. That's a pretty easy thing to apply. For those who are interested

## 18:21

in math, this is what we would call a derivative. So, we're going to have a left-hand boundary
condition

## 18:23

condition. We can also define a vacuum condition. Now, what is a vacuum condition?

## 18:34

In many cases, the model or the system of interest is an isolated system. Think of a reactor. We've

## 18:40

got all the good stuff happening in the reactor, and on the outside of the reactor, we might have

## 18:44

some material that acts as what we call a reflector, and then we might have some protective

## 18:49

shielding and so forth, but everything outside of that is basically assumed to be negligible,

## 18:55

and what

## 18:56

we really care about is the fact that there are no neutrons coming from outside into the reactor,

## 19:02

okay? So, in order to impose that, we have to say something about the reactor's exterior,

## 19:09

and the easiest way to say that no neutrons can be coming from outside the reactor is to assume

## 19:14

the reactor is inside a vacuum. Another way to think of that is, or another way to define that

## 19:20

is to say that the reactor is inside a purely absorbing medium. In our case,

## 19:26

whether it's vacuum or purely absorbing, meaning no scattering, that the effect is the same. There's

## 19:32

no neutron that's going out of the reactor, scattering, doing whatever, and then coming back

## 19:36

in, and we don't have any sources that are injecting neutrons into the system from the outside,

## 19:43

okay? The easiest way to model that kind of condition is to set the boundary flux to zero,

## 19:49

right? That would be this thing here. The phi of zero is equal to zero, right? And there are some

## 19:55

tweaks on that that are going to be used to set the boundary flux to zero, right? And there are some

## 19:56

things that make it a little bit more accurate, but it's a quick and dirty approximation that is

## 20:00

sometimes easier to implement numerically, certainly easier to apply symbolically,

## 20:05

but it's really just an approximation, right? Diffusion theory is already an approximation,

## 20:11

and this is adding a further approximation, right? It's not even really consistent with

## 20:15

diffusion theory. A better approximation is to set the incident current to zero, okay? What is

## 20:22

the incident current? Well, we've already talked about the current vector, or,

## 20:26

in parentheses, I have net, because it means something about the net flow, because we're

## 20:30

integrating over all four pi, so we're getting a vector in which neutrons are, on the average,

## 20:36

flowing. But we can limit that integral, not over four pi, we can actually have it over two pi,

## 20:41

so it's over just a half space. Now, in the slab system, we're varying along the x-axis, right? So

## 20:47

if I have my slab, let's see, right? I've got a slab, I've got my neutrons going,

## 20:56

along the x-axis, sorry for the totally not straight x-axis. What I'd want to do is say,

## 21:02

hey, I've got this vertical plane here, and I want to know, of all the neutrons that are going,

## 21:07

right, whatever their direction is relative to the x-axis, I want to just, I want to know the

## 21:12

net number that are going to the right, okay? That really does look like chalk, right? And so

## 21:20

that would be integrating over the two pi, like the hemisphere that kind of points,

## 21:26

this way. And then I could do the same thing for the left-hand side and come up with a j sub left.

## 21:33

Okay, and if I do that, if I do that, what I end up with mathematically is this.

## 21:54

Why isn't it letting me do, I don't know why it's not letting me color on that, but

## 22:08

from transport theory, what we get is the following definition for j right and j left,

## 22:14

those net currents in the half,

## 22:17

spaces. So the partial currents is what we call it. So partial current to the right,

## 22:21

partial current to the left is a function of phi and of the current, right? But we already know

## 22:28

that the current itself is a function of phi. So it's phi over four minus or plus d over two times

## 22:33

the derivative of phi along the x-axis, okay? You are not required to understand how this form

## 22:40

is produced. It comes from transport theory. I'm giving it to you. It represents the partial

## 22:46

currents.

## 22:47

You can always understand it through its relationship to the net current, because if

## 22:51

we take the flow to the right, right, if we know the total number of neutrons or net number going

## 22:57

to the right, and then the number going to the left, their difference ought to be the net number

## 23:02

at that point in space. So j right minus j left actually gives us j of x, which is what we expect

## 23:10

for based on the definition of j of x, okay? So with this partial current defined, we can define

## 23:16

a zero flow. So we can define a zero flow. So we can define a zero flow. So we can define a zero

## 23:17

boundary condition at the left, or a vacuum boundary condition at the left, right? And for

## 23:21

this case, we'll say x is equal to zero. And then we would say that j right of zero is equal to
zero,

## 23:26

which means that phi of zero over four minus d, if it's a continuous quantity at zero over two,

## 23:34

times d phi dx evaluated at zero, that's all equal to zero, okay? You can imagine this is a slightly

## 23:40

more complicated condition to apply to the differential equation, right? Because we have

## 23:45

derivatives in the boundary condition.

## 23:47

All right, we can also model boundary sources. So if we don't have a volumetric source inside the

## 23:54

slab, but we say that we have a source of neutrons at the boundary, well, we can account for this

## 23:59

using the partial currents we just defined. So instead of saying it's a vacuum and saying

## 24:03

the incident current is zero, we say it's equal to some number, okay? Easy as that.

## 24:10

One boundary condition that can be useful for simplifying problems is pure reflection. What

## 24:16

this means is that a neutron that goes out of the system bounces right back into the boundary
condition.

## 24:21

Like a perfect mirror, okay? Well, if we have the condition that everything going out comes

## 24:29

immediately back, right? So anything that goes out leads to something coming back,

## 24:33

that would mean that we don't have a flow of neutrons at that point, right? Which means that

## 24:39

the net current ought to be zero. And so the easiest way or the way to implement a pure

## 24:45

reflecting boundary condition is to say that j at some boundary is equal to zero.

## 24:53

Relatedly, there's an albedo condition. And I really don't like the word albedo because

## 24:58

it doesn't, I don't use it in any other part of my life. It doesn't have any other

## 25:03

neutronic meaning. And looking into it, it comes from optics. It's something like an optical

## 25:08

reflection, right? Or partial reflection. What it means in plain English is

## 25:14

at a given boundary, an albedo defines the number of neutrons that come out of the

## 25:23

boundary back towards you given the number of neutrons that you put into it, right? So if we're

## 25:28

in a slab, the number of neutrons that are leaving the slab will lead to some proportion that come

## 25:33

back in. So not pure reflection, but not pure vacuum, right? The albedo condition gives you

## 25:38

something in between. And the way we do that is to define alpha, the albedo, and it's just j left

## 25:46

over j right at the appropriate boundary location, okay? So if we set alpha equal one, that is pure

## 25:52

reflection. If we set j left over j right at the appropriate boundary location, okay? So if we set

## 25:53

it to zero, that corresponds to vacuum. All right, we have all these things together. It's time for
a

## 26:00

model problem just to help put these things into some form of practice, okay? So we're going to

## 26:06

take a slab between x equals zero and x equals a. We're going to have a constant sigma a and

## 26:11

diffusion coefficient d. We'll ignore fission for now, bringing that back in when we care about

## 26:18

reactor or fissile systems. So sigma f is going to be zero. For now, we're going to take s of x is

## 26:23

equal to s of a. And we're going to take s of x is equal to s of a. And we're going to take s of a.
And we're going to

## 26:24

take s of a. And we're going to take s of a. And we're going to take s of a. And we're going to take
s of a. And we're going to

## 26:25

have a spatially uniform source. So the source is the same everywhere in the slab, okay? We also

## 26:31

have at the left phi of zero is equal to zero and phi of a is equal to zero. So this is sort of our

## 26:37

hackish vacuum condition, right, using a fixed flux definition. So next time, we'll apply the

## 26:43

other boundary conditions, okay? So what we want to do is find phi of x and the current j of x,

## 26:49

and then plot them for the specific case of a is equal to 10 centimeter sigma a is equal to,

## 26:54

one-half inverse centimeter, d is equal to one over six centimeters, and s-naught is equal to

## 26:59

one centimeter per centimeter cubed per second, okay? So let's solve for phi and j symbolically,

## 27:07

then we'll substitute the numbers. So I'm going to lay out sort of a procedure that you can use

## 27:11

to solve diffusion theory problems, and you can probably apply these also to things from heat

## 27:16

transfer and so forth, and we'll get some more practice with this next time. All right, so first

## 27:22

step, we'll write down the equations. I'm not going to write this down like with a blackboard

## 27:26

or anything, I'm just going to lay out the equations here and kind of just talk through,

## 27:30

right? So the diffusion equation that we had above was, it had the diffusion coefficient sigma a,

## 27:36

all that stuff. You'll notice that the very first term of this, I've simplified a little bit,

## 27:41

and that's because d is constant. Before we had a d dx times d times d phi dx, right? And that's

## 27:48

important. If d were a function of x, we would have to keep it in that form, and then

## 27:52

that's what we're going to do. So we're going to keep it in that form, and then we're going to

## 27:52

keep it in that form, and then that's what we're going to do. So we're going to keep it in that
form,

## 27:52

do a product rule with the derivatives. But if d is constant, as it is in our case,

## 27:57

we just pull it out and we get a second derivative directly for the scalar flux,

## 28:02

okay? So this is our differential equation, and then these are our boundary conditions,

## 28:07

so pretty straightforward. Step one is done. This is the first thing you have to do when

## 28:11

solving a differential equation like this, is write down the equations and the related constraints.

## 28:18

Step two, we have to come up with a homogeneous solution,

## 28:22

right? And that means that we'll have to come up with the particular solution and everything

## 28:29

like that. If you read the book, the author goes through some tricks to help simplify things. I'm

## 28:35

adopting those because they're pretty standard practice in reactor theory textbooks, and they're

## 28:40

pretty common in other disciplines. Basically, you just want to get your original equation into

## 28:45

the simplest form possible so that you can, or your symbolic algebra system can kind of immediately

## 28:51

give you a simple solution. So what we'll do is to divide through that original equation by minus

## 28:57

d, and then we'll define something called L through this equation, L squared is equal to d

## 29:03

over sigma a. L is called the diffusion length. You should check the units, make sure it actually

## 29:08

is a length. I can tell you it is, okay? If we do that, then our equation looks like this,

## 29:13

right? We have phi double prime, which is my second derivative shorthand, minus 1 over L

## 29:18

squared times phi is equal to minus s naught over d.

## 29:21

A little bit simpler, and the reason for that is that the L will show up in our solution pretty

## 29:29

clearly. So the homogeneous solution is the thing that satisfies the equation without the right-hand

## 29:35

side. So we need to come up with that first. Now, because L is greater than zero, because our

## 29:40

diffusion coefficient and our sigma a, our absorption cross-section are greater than zero,

## 29:46

our solution will have the form a prime times e to the x over L plus,

## 29:51

b prime times e to the minus x over L. I put the primes here because I'm going to actually use

## 29:56

the second solution that I have boxed here. Rather than use exponentials directly,

## 30:01

I'll use the hyperbolic functions, so the hyperbolic sine and hyperbolic cosine,

## 30:05

and with this, it would be a times sinh of the x over L plus b times cosh of x over L.

## 30:14

This turns out to be slightly easier to apply, right? Because the sinh and cosh functions

## 30:19

have some properties that are similar to each other, and so we're going to use the

## 30:21

similar to sines and cosines, right? So we can apply some identities and come up with a slightly,

## 30:27

let's see, more compact solution than we would otherwise be able to do with the exponentials

## 30:32

directly, okay? What I want you to do, I'm not going to pause or wait for you. You pause me if

## 30:37

you want. Plug sigma h, or sorry, phi of h back into the original differential equation. Do you

## 30:44

get zero on both sides, right? For the homogeneous equation, do you get zero on both sides? If not,

## 30:51

then I've made a mistake. I've made a mistake. I've made a mistake. I've made a mistake. I've made a

## 30:51

mistake. Or maybe you have. Verify, though, okay? Don't do it later. Do it right now.

## 30:58

Now we need to get the particular solution, right? Because we have a driving term,

## 31:02

the source function, we're going to have to have some component of the solution that accounts for

## 31:07

that source. The default trick that we use in engineering mathematics for finding the particular

## 31:14

solution is to guess a phi of, phi sub p, a particular solution that has the same functional

## 31:21

form as the original solution. So we're going to have to guess a phi of, phi sub p, a particular

## 31:21

solution that has the same functional form as the original »

## 31:27

alright, fa of f g eyebrow

## 31:30

seront

## 31:33

so

## 31:34

I'm going t

## 31:37

we get represented in the

## 31:39

Mansion

## 31:42

d

## 31:44

wi

## 31:45

j

## 31:46

and

## 31:48

i

## 31:50

dict'

## 31:51

box says this is our first part of the solution, right? We're a good part of the way to getting

## 31:55

what we want. We have the particular solution. Now, if you plug this solution back into the

## 32:00

equation, you should find that you get, you know, S naught equal S naught, or S naught over D equal

## 32:08

S naught over D, whatever it is. Both sides should be the same, okay? What the particular solution

## 32:12

does not do, though, by itself is satisfy the boundary conditions, in which case we have to

## 32:17

bring back the homogeneous solution, okay? So let's determine those constants by applying

## 32:25

the boundary conditions. So at the left, right, for X equals zero, we substitute the homogeneous

## 32:31

solution, which had our A and B in the sinh and cosh, and then we have our particular solution,

## 32:36

right? We put those in. You can see now why I chose the sinh and cosh, because I'm left with

## 32:42

just B, because sinh of zero is zero, so the A goes away, and the cosh of,

## 32:47

zero is one, so I get a B plus the S naught over sigma A equals zero. That means that B is equal

## 32:53

to minus S naught over sigma A, okay? Easy peasy. The right condition is a little bit uglier, right?

## 33:00

So I've, the A times sinh of A over L minus, I've plugged in the B here, so the minus S naught over

## 33:06

sigma A times the cosh of A over L plus our particular solution S naught over sigma A is

## 33:11

equal to zero, right? Because that's my right-hand side boundary condition, and if I solve for A,

## 33:16

I get this.

## 33:17

Not terrible looking thing, right? And that's that, okay? So now if I perform the substitutions,

## 33:28

right? I've finished step four. I got all those unknown coefficients defined. I perform the

## 33:33

substitutions, and voila, what I get is the scalar flux at any point within the slab, okay?

## 33:39

You might be able to tweak these things to get a slightly nicer form. If you look at equation 630

## 33:44

in the textbook, the same problem was solved with a slight variation. Rather than,

## 33:49

again, being defined for a slab from zero to A, it was defined from negative A to A, right? So it

## 33:56

had some symmetry built in, which leads to a slightly simpler solution, right? So the way

## 34:03

that you model your problem will impact the sort of compactness of your solution, but I urge you,

## 34:09

take this solution, take the one from the book for the appropriate values of A in both cases,

## 34:14

and show that they're the same, okay? But either way, this, this, this,

## 34:19

seems to be good. Of course, what should you do with it at this point? Plug it back into

## 34:25

the boundary conditions. Make sure everything checks out. All right. Now, step six. What did

## 34:32

I ask for? I asked for phi and for j. Now, I didn't analytically come up with j, but because

## 34:37

of the solution form, it's easy enough to kind of do that by hand in the plotting code. So that's

## 34:44

the way I've done it. All right. So I've imported my numpy and matplotlib. I've defined those

## 34:48

constants here. I've defined the unknown coefficients, the a and b, per the definitions

## 34:56

above. And then I substitute x in for this. Why do I hate Windows? I have phi. Then I define d phi

## 35:05

dx. If you notice, all I'm doing is I'm pulling up the argument, right? Because cosh and sinch

## 35:09

are just like sines and cosines. The argument pops out. And then I have to go to the next thing.

## 35:14

Now, the one difference is the derivative of sinch is cosh.

## 35:18

The derivative of cosh is sinch, not negative sinch. So it gets a little bit easier, right?

## 35:23

And so then that's d phi dx. j is just minus d times d phi dx. All right. Now, I set up the plot,

## 35:31

and I'll go ahead and run it. And that's my solution. Okay. So if you look at this,

## 35:38

does it seem to pass the sanity test that might be obvious to you? What's the first sanity check?

## 35:45

When you plot it, it ought to match the boundary conditions. If I look at the left

## 35:48

and the right, yeah, sure enough, I get zero. Okay. But there are some other sanity checks,

## 35:53

right? How about the middle of the slab? What would I expect the solution to be at the middle

## 35:59

of the slab? Now, think about this. This slab is 10 centimeters. How many mean-free paths is that?

## 36:05

Well, if the only thing that I have to consider is sigma a, right? Sigma a is 0.5 centimeters.

## 36:12

Then the average neutron mean-free path is two centimeters, right? One over sigma a, right? There

## 36:17

might be some other things that I have to consider, but I'm going to go ahead and do that.

## 36:18

Other things, but let's just assume that's the case. That means that this slab is five mean-free

## 36:23

paths. So if I'm a neutron born in the middle of this slab, then on the average, I have to travel

## 36:30

two to three mean-free paths to exit the slab, right? I'm probably going to have an interaction

## 36:35

between them. Okay. That means also that at the middle of the slab, I'm quite far away from the

## 36:41

neutronic effects of the boundary itself. What does the boundary do? Well, it causes neutrons

## 36:46

to leave the building, right? So you lose neutrons. So the ex-dependence of the solution

## 36:52

is pretty rapid. But as I get further from the sides, what I should find is that the solution

## 36:59

in the middle looks a little bit like the case in which I assume there is no spatial variation,

## 37:06

right? And if I think about that, well, if I don't have any spatial variation, then I don't have

## 37:13

this term, right? So I have d phi

## 37:16

dx squared. Oh, this is terrible, right? That thing just goes to zero. So then I'm left with

## 37:24

sigma a phi is equal to s in my original case. So if I don't have any spatial variation, then phi

## 37:36

should just be equal to my source term divided by

## 37:39

my sigma a, right? And my source term in this case was one. My sigma a in this case was 0.5,

## 37:47

and if I look at my solution, I see a solution of two. That seems to check out.

## 37:54

I'd also like you to think about what this current vector means. If I have a current at the right-
hand

## 37:59

side and the left-hand side, does that tell me anything about how many neutrons are leaving

## 38:03

the building, right? In this case of the fixed flux conditions, probably not because there will

## 38:10

be this fictitious incident neutron source. But when we get to next time and model it more
accurately,

## 38:16

we'll be able to assess the solution based on really just neutron accounting, okay?

## 38:22

So those are the seven steps to solving these diffusion problems. We'll apply them

## 38:28

in mass next time. I'll see you then.
