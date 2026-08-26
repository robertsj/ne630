# L15 Local Audio Transcript

Course: NE 630

Playlist source: https://youtube.com/playlist?list=PLy481lNHlnHoEO95vM-xYX2bydD25v20L

Video: NE 630 - Lesson 15

URL: https://www.youtube.com/watch?v=DXLcFR83GKw

Video ID: DXLcFR83GKw

YouTube upload date: 20230925

Duration: 53:34

Transcript source: Local faster-whisper transcription from YouTube audio.

Whisper model: large-v3; detected language: en.

Generated: 2026-06-28

Note: This transcript is machine-generated from audio and lightly wrapped only. It should be reviewed before being quoted, published, or used as polished lesson text.

Requested language: en

## 00:00

and everybody's tested.

## 00:02

Everyone else is going to be tested.

## 00:04

So we're going to have to talk to them.

## 00:10

We're going to have to have them back up.

## 00:13

Oh, yeah, definitely.

## 00:18

You're going to have to do this.

## 00:20

You're going to have to do this.

## 00:22

You're going to have to do this.

## 00:24

I'm with you.

## 00:26

I'm with you.

## 00:28

I'm with you.

## 00:34

I'm with you.

## 00:39

It's going to be super horse like.

## 00:43

It's going to be super horse like.

## 00:46

We're going to be having 21 pipes going through.

## 00:56

We're going to be having 21وجes going through.

## 00:58

We're going to have 21edge.

## 01:03

We're going to getstanding.

## 01:05

We don't have any cell dieses.

## 01:09

Oh, really?

## 01:12

And so we're going to have confrontation.

## 01:14

We're going to have a large unity working group.

## 01:17

Huh?

## 01:18

all right let's go ahead and get started uh so this week is the exam week uh that'll be in class

## 01:37

on friday i'll talk uh a little bit about it i want to first um take a quick look at homework

## 01:46

five right so as we've been doing all the homework problems have been assigned during the

## 01:53

week associated with lessons right so i was in the lesson page uh and then i combined it all into

## 01:59

one document um making some corrections if i need to uh so i put together the homework for week five

## 02:05

and i recognized from from last week that we're on as a class there have been a lot of issues

## 02:14

with uh dealing with some of the data

## 02:16

and part of that is just me being oblivious in some sense uh where i try to make it easier and

## 02:25

then maybe it doesn't quite work out that way so i think with the data i've given you in that csv

## 02:31

file there's a csv raise your hand if you know what i'm talking about okay so what i did is i

## 02:38

took all the data that we've been using which was directly from the nndc i loaded it myself i put it

## 02:44

all onto one energy

## 02:46

grid so you've got this gigantic csv file that's like a two-dimensional you know matrix right so

## 02:51

one column are all the energies and then all the other columns are the cross sections of interest

## 02:56

the very top row has which cross section it is so it's something where you could load it into an

## 03:00

excel spreadsheet just just fine or you could load it into python or do whatever you've been doing

## 03:05

that way you don't have to deal with the interpolation stuff which i realize is like a

## 03:11

it's it's not very hard to do it once you've done it but i realize that if you don't know

## 03:16

how to do it you don't know how to do it you don't know how to do it you don't know how to do it

## 03:16

that can just be that can sink the ship before you've left the port as it were and that's not

## 03:23

the point i hate that sort of thing i'm in a math class right now math 725 it's all online it's
about

## 03:28

networks it's cool stuff but i find that the structure is infuriating right it's like i'm

## 03:36

there are quizzes that take longer than they should because they're talking about things

## 03:39

that are in the reading for two weeks from now right so like anytime that you have a disconnect

## 03:44

like that which you've suffered because

## 03:46

probably me uh it's frustrating right and i don't want i mean you you have every right to be

## 03:51

frustrated if that was an issue but uh hopefully we can move forward and uh reduce that and and

## 03:58

come away having learned what i wanted you to learn i'm hoping that by making these two problems

## 04:05

as extra credit one you don't have to do them this week right so that's that helps uh two

## 04:11

you can do it for next friday it's the same stuff that you've been doing or possibly have

## 04:16

been struggling to do uh now it's slightly easier because i've given you the the stuff in a more

## 04:21

um let's say easy to use format so go ahead and do that it's extra credit four points each that

## 04:27

just adds on to your homework score so if you've had um some scores that weren't quite what you

## 04:34

wanted on the past couple homeworks i got through all the grading of homeworks two and three and

## 04:39

mostly folks did fine but there were a couple instances where i don't know if just the group

## 04:44

you work with or whatever

## 04:46

finding issues with some of this stuff and you just didn't really tackle those things hopefully

## 04:51

this gives you a chance to fill in those gaps and uh you know i guess feel confident about the

## 04:57

stuff okay so those two things go ahead and do them for next week if you like um i've given you

## 05:04

the spectrum as well uh in the same sort of tabulated format so you can um it should be

## 05:09

pretty straightforward so that means these problems and i'm not going to say that they're

## 05:13

trivial but they should be pretty

## 05:16

straightforward it's like you know kind of pen and paper um a little bit of thinking about it so

## 05:21

because i'm putting these as extra credit and those are sort of the time crunch ones i'd like

## 05:27

this to be due thursday at 11 59 as opposed to the next day friday um the reason for that is

## 05:34

if you want to have done this in preparation for the exam and you want the solutions it's

## 05:40

got to be done before the exam right so hopefully that gives you enough time um if

## 05:46

you're done earlier than that and you want to come and talk to me about solutions i'll

## 05:51

be available for for that as well so i guess any questions about this homework yeah um the first

## 05:59

question that's not extra credits is the spectrum you just use which spectrum is that uh so that

## 06:05

would be the spectrum for these extra credits so when i wrote that it was originally the spectrum

## 06:11

that you would have come up with for the homework that was due last night right but in any case it's

## 06:16

the spectrum that's based on a 1 over e right so i'm asking you specifically what happens if you

## 06:22

were to use something like the narrow resonance instead of one over e of when computing k infinity

## 06:29

right they shouldn't be the same answer right because otherwise there's no point in having used

## 06:33

the narrow resonance the narrow resonance will do something important and we want to understand

## 06:37

what that that is so it shouldn't need to think about that uh a little bit uh i didn't i think i'll

## 06:44

have to check but i think the the spectrum is a complete research sensor now i think it it's an

## 06:45

spectrum file i gave you has two spectra one is the one over e i fixed up so remember we saw that

## 06:51

horrible looking spectrum last time right i wonder if i do i have uh eight let's see

## 07:05

is that the one

## 07:12

all right so this is the stuff that we were looking at last time right so we ended up with

## 07:18

that kind of goofy looking thing and if you're going to go ahead and do the problems that i've

## 07:23

now marked as as extra credit it makes more sense to use something that looks a little bit more

## 07:28

uh realistic that doesn't have that weird you know decrease right there so what i've done is

## 07:33

i've given you two spectra the the red one that you see has a narrow resonance uh built in and

## 07:39

then that's actually superimposed on a black one which has the smooth um curve so the file that

## 07:45

i've given you looks like this i mean it has a hundred thousand points or something like that

## 07:48

the the first column are the energies the second column is the spectrum with the one over e and then

## 07:55

there's the narrow resonance so if you're feeling ambitious when you answer that question like what

## 07:59

impact does the narrow resonance spectrum have over the one over e you can actually do that

## 08:04

numerically right i'll do that for the solution i'm not asking you to do that but um you have

## 08:10

that so when i say that spectrum for homework five the spectrum you just used that if if you do that

## 08:18

you do those i would ask you to use the spectrum i gave you right because one then you're not

## 08:22

interpolating two it looks a little bit better and three it'll match my solution if you get it right

## 08:27

you know or like we'll all be using the same thing so any other questions about this homework

## 08:39

there were a couple of folks who had some issues uh over the weekend so i'll release the

## 08:46

homework for solution um early this evening so that you can take a look at that

## 08:52

um hopefully no big surprises there all right so that's it for the homework obviously the homework

## 09:01

for this week that'll be due next week is going to be pretty light because we only have two classes

## 09:08

the reading for next time is section 4.3 i'll get the sheets up um i've been just focused on getting

## 09:16

some stuff ready for for deployment today um and then the reading for today would nominally be four

## 09:22

one and four two so lighthearted stuff um basically today i'm gonna show you some pretty

## 09:26

pictures and talk through what i understand about reactor systems out there um and uh yeah so on

## 09:35

wednesday we'll talk about fast spectrum um basically fast spectrum reactors and how to do

## 09:44

some some calculations with that but really if you'll see the section itself is like a a page

## 09:52

so there won't be a whole lot of technical stuff that i have to go through hopefully i can have a

## 09:57

numerical example using openmc using actual data uh but that should give us plenty of time to go

## 10:03

over exam questions i don't have anything formally prepared for a review i have not written the exam

## 10:10

formally yet but i have ideas for the questions based on what i'm seeing uh in homeworks and

## 10:15

so forth i don't expect it to be super number crunching intensive because i think that's a waste

## 10:22

of time i want to get to your understanding of the concepts and you know being able to manipulate

## 10:27

some some expressions in a way that shows me that you know what it is that i've been talking about

## 10:32

yeah are you going to post some sort of like format at least so we know like the format of the

## 10:37

uh i'll try to have that down for wednesday that the problem is this is only the second time i've

## 10:44

taught the course right um and last year was the first time i thought of that itself beyond being
just

## 10:52

the first time was an exception too right because i was uh preparing to go on leave and it was a
much

## 10:57

smaller class it's only seven students and so we we ended up doing a lot of computation which

## 11:04

if for better or worse right so very different so i don't have uh like old exams to go on right uh

## 11:11

good question period question i'll do my best on wednesday to make the format or um predictable uh

## 11:25

okay yeah so for

## 11:26

for the exam uh the format i did you know it'll be a handful of questions of course

## 11:36

uh what you can do on the exam is uh one 8.5 times 11 in sheet of notes right plus calculator

## 11:57

plus

## 12:00

pen or a pencil with an eraser if you're not confident

## 12:05

i i joke i had a math professor once say that and totally wasn't joking and i got a c in that math

## 12:15

class so when i said i don't feel like i'm that great at math there was one math class that i just

## 12:20

absolutely despised yeah did you use a pen in that class uh it wouldn't have mattered well i mean

## 12:26

i could have done this

## 12:29

it was not with confidence whatever i was writing uh at that time it was it was humbling too because

## 12:35

i actually had a classmate from high school who was in there and in high school he was always the

## 12:42

one that i thought was smart right and uh he was in that class and i'm sure he got an a and then

## 12:48

he went off to get his phd at stanford uh in physics and his advisor is a guy named

## 12:56

last name murner ended up getting the nobel prize and so

## 12:59

i've got a friend from high school public high school in the green bay area

## 13:03

who went off to get a physics phd and i think he's working for department of energy now too

## 13:08

sort of a strange uh job yeah good question is that both sides she or just

## 13:14

uh both sides yeah so and remember my my philosophy on this is not that i want

## 13:20

to keep you from using the book or these other things it's just

## 13:23

i think it's really really useful to go through because i know some folks take good notes and some

## 13:29

folksahan

## 13:29

take bad notes. I remember sitting in classes like this where I just kind of scribble half the time

## 13:34

I can't find the notebook that I was doing my notes so I've got this jumble of papers loosely

## 13:39

whatever and it never actually amounts to anything that I used again and there's no sense in you
know

## 13:45

suffering through that so just make yourself a nice sheet of notes. I guarantee there will be

## 13:49

no data that you need elsewhere. One of my favorite things to do is you know for instance

## 13:55

Avogadro's number 6.022 blah blah blah. I will probably put if I if we need to use Avogadro's

## 14:01

number I will just say it's 6 times 10 to the 23rd right. Is there any difference? Absolutely

## 14:07

not. Not for the purposes of an exam. I'd like you to be able to do very round math. That's my

## 14:13

favorite kind of stuff to do in these back of the envelope because it's not the number that

## 14:18

indicates your understanding. It's the process. Having the right number helps a lot right and

## 14:25

the easiest way to make sure that you have the best chance to get the right number is to make

## 14:28

the numbers easier to work with in the beginning right. So I will do my best to make all that true.

## 14:36

All right anything else for the exam? Yeah topic wise it's everything through last week.

## 14:42

Obviously not a lot that we can do about the Friday stuff because that was using large arrays

## 14:48

of multi-group data right. That was more for context than anything but two groups I could

## 14:54

have you.

## 14:55

i i can expect you to to work with um and hopefully you'll get a sense for that as you go

## 15:01

through the uh the homework problems all right um yeah so last time we talked about the multi-group

## 15:08

stuff and what this led to when we got the bounds equation written out in uh sort of matrix form

## 15:15

is that the solution to the slowing down or spectrum equation turned out to be a set of

## 15:20

eigenvalues and their eigenvectors and the eigenvalue that we cared about was k infinity

## 15:28

and the corresponding eigenvector was what we would call the critical spectrum right that's the

## 15:34

the flux spectrum all positive values corresponding to that particular value now because we're in
the

## 15:40

strictly energy space turns out all those other eigenvalues were zero and that has to do with

## 15:45

what for us that that fission matrix looks like right it was this

## 15:50

outer product

## 15:50

of two vectors um when we get to space and such the equivalent would look a little bit different

## 15:56

but by and large you set up a matrix system you compute the eigenvalues and eigenvectors and

## 16:03

one of those pairs will be our solution the other ones are not unimportant they actually represent

## 16:11

the higher order harmonics that damp in time if this system were subject to some sort of time

## 16:18

dependent impulse right rather than just

## 16:20

you know

## 16:20

having a steady state operation if it were instead the the system in some sort of unsteady state
those

## 16:26

other modes would be present and they would tend to decay in time as the system approaches the

## 16:32

steady state right we haven't talked about time stuff yet that's actually what we get to in chapter

## 16:38

five so we're going to buzz through chapter four next week which uh I I suspect we'll finish next

## 16:44

week and then we'll be on to the time dependent stuff and then I think we get to some spatial

## 16:48

diffusion um where we can actually

## 16:50

play with some real math as a just kidding uh anyway so that's what we did last time next time

## 17:00

go ahead and read four or three and then today what we're doing is talking about power reactors

## 17:05

so uh I don't expect that but well given that I'm pretty I'm a windbag when it comes to talking
we'll

## 17:12

probably go through the end but we probably shouldn't have to so uh but fill in the gaps for

## 17:19

me ask some questions

## 17:20

as we go along and uh yeah so what I've done earlier today is I've put together some some

## 17:31

pictures that I found there's lots that you can just find from Googling I apologize I have not

## 17:35

been very good at citing my sources um thoroughly right I can go back and do that for you if you

## 17:41

have any real complaints but what I want to try to uh describe today is what these reactors look
like

## 17:50

we we talked about nuclear reactors from from day one we understand that there are a couple

## 17:55

reactors that are reasonably close to us one very close just down the hallway and then the

## 18:00

closest power reactor is not so far over in Burlington is that correct right how far is

## 18:06

Burlington from here over 45 right and so that uh the the reactor Wolf Creek is is our closest

## 18:14

power reactor and there are a handful um probably within about 300 miles

## 18:20

um but anyway so what is a reactor what what is the system that we've been addressing in this very

## 18:26

simple energy only approximation right there's got to be some spatial uh part of it and so what I'd

## 18:34

like to do is take a look at what what some of these systems look like so this is a a cartoon

## 18:40

of a pressurized water reactor you can find tons of these these cartoons and often they're given

## 18:47

out by the doe and the the the the the the the the the the the the the the the the the the the

## 18:50

the basic form factor is the same for all PWRs all BWRs really any power reactor on the grid it

## 18:56

just happens that light water cooled reactors are the dominant ones here in the states if you go up

## 19:01

north to Canada then you'll find that things are not just water uh light water it's heavy

## 19:08

water and then it can do reactors um but anyway so what we have is this big uh building right

## 19:15

which is the the containment structure containment meaning stop things from

## 19:20

leaving that shouldn't leave right containment is a huge thing in nuclear provides one of the

## 19:26

barriers between the nasty fission products that we've talked about and you know humans right so

## 19:33

there are multiple levels of barriers of of of stopping that this um transmission of the radioactive

## 19:40

stuff diffused in nuclear power to to humans so we've got this containment structure and inside

## 19:44

of the containment structure we have a reactor pressure vessel which inside there is the

## 19:50

reactor core in addition to a number of things related to heat removal right either a heat

## 19:57

transfer and then uh exchanging through one loop maybe into another loop ultimately leaving this

## 20:06

producing electricity usually through spinning a turbine right and then somehow that has to be uh

## 20:14

that the the coolant used in all this has to be brought down to a temperature that can be then

## 20:18

brought in and so

## 20:20

inside of the pressure vessel into this small little region here this is where all the magic

## 20:27

happens so like if you're talking about like the scale of it this thing is pretty small compared to

## 20:33

everything else right um this schematic shows us with a cooling tower not all reactors have cooling

## 20:41

towers right does does Wolf Creek have cooling towers why not there's a big lake right next to

## 20:48

it yeah so if you've got a big body of water

## 20:50

that's your heat reservoir so if you're producing 3 000 um megawatts of electric of heat right to

## 20:59

produce roughly 1 000 megawatts of electricity there's a heck of a lot of heat energy that has

## 21:06

to be put somewhere right into a final sink and so what happens is water is forced through this

## 21:13

core and this so-called primary loop okay the water that the hot water is then

## 21:20

uh put into it a heat exchanger it's called a steam generator in a in the lingo of PWRs that

## 21:28

steam generators it's nothing more than a heat exchanger and so we've got water in the secondary

## 21:32

side right heat exchangers exchange heat from one loop of a working fluid to another on the

## 21:38

secondary side we have more water coming in that is going through the cooling tower or possibly

## 21:44

coming from the lake whatever taking away the heat spinning the turbine blah blah blah and the the

## 21:50

cycles repeat so you've got forced flow of water up through this PWR um core right and the core

## 21:59

itself is a pretty small geometrically small part of this whole thing so what does such a core need

## 22:08

to do if you look I know I didn't define the reading for today but if you read chapter four

## 22:14

kind of opens with a nice introduction for what power cores have to do number one they have to

## 22:19

produce power uh stably consistently

## 22:22

right which means steady state you don't want to be producing a thousand megawatts and then

## 22:28

2000 or you know fluctuating in time that might be good for some grid applications but for nuclear

## 22:35

power we need steady always on what we call base load energy and the reason for that is is it the

## 22:43

structural components of a nuclear reactor tend to be sensitive to changes in temperature and so

## 22:50

forth and so if you have

## 22:52

temperature cycles you can degrade your materials substantially quicker than if you were operating

## 22:58

at steady state so for the sake of the plant itself we want to do this in steady state and

## 23:05

we we've talked before about this word criticality being synonymous with steady state at least in
our

## 23:11

neutron chain reaction context yeah um sort of I'll talk about from this specific so PWRs they're

## 23:25

under pressure what's the

## 23:26

standard like pressure rate like so the how much pressure is more right yeah so the this containment

## 23:35

here for PWR everything is under pressure the the coolant the working fluid water stays in a liquid

## 23:41

state I mean there's some um there there is some small scale boiling right but as opposed to a

## 23:50

boiling water reactor where the water is actually boiling inside of this this uh core

## 23:56

uh the pressure for a PWR is about 14 megapascal which is about 140 atmospheres if I remember my

## 24:04

conversion so significantly pressurized okay uh with operating temperatures on the order of 300

## 24:12

degrees C so that's a big pressure right in other units that's 2200 psi right and again I think I've

## 24:23

talked about this before I know my car tires right

## 24:26

and 34 psi so 2200 big difference right imagine the sort of um the structural material you need

## 24:36

to have that kind of pressure and even though I say the core is pretty small this prector vessel

## 24:42

is on the order of 10 meters tall by roughly you know 10 meters is a like kind of a good estimate

## 24:52

for the the scale so very large and in fact I would say that the

## 24:56

construction of pressure vessels for PWR um reactor plants is it was one of the bottlenecks back
over

## 25:05

the last 20 years in the planning of new development across the U.S and elsewhere because the
facilities

## 25:12

out in the wild world that are capable of producing pressure vessels of the quality and size needed
for

## 25:19

nuclear power plants was I think just limited to one plant by the time things and that was uh Japan

## 25:26

right for uh of course Japan has lots of history in nuclear power um of course back about 10 years

## 25:33

ago it was a pretty bad footnote in nuclear power uh but if you watch the news the the government

## 25:40

is actually now back on to investing in nuclear so they have plans to um if not restart plants that

## 25:48

were shut down replace plants with new technologies and so forth so it's it's not game over for
nuclear

## 25:55

in Japan

## 25:56

um despite the the major setback that they and then the rest of the nuclear world suffered back

## 26:02

in 2012. okay so yeah huge pressures 14 megapascal as to compare a boiling water reactor is uh about

## 26:13

half that pressure right which has implications for the size of the core and other things but

## 26:20

we'll focus on the PWR now just to get a sense for what what the basic uh structure of of the fuel
is

## 26:26

right so you've got this pressure vessel if you were to take off the top cap and look down with

## 26:31

something like this you've got this you know grid of um uh basically a square grid where each of

## 26:38

these little squares is a fuel assembly and this is a I'd call it a cartoon but it's actually a

## 26:43

picture from a Monte Carlo model um that servant is the name of the Monte Carlo tool section
developed

## 26:50

in Finland they have lots of graphics from um the use of their tool for modeling this sort of stuff

## 26:56

a PWR core cutaway that looks like this each one of these is an assembly each assembly uh looks

## 27:03

kind of like this this is the sort of a blown-up view very common artsy fartsy one from um uh from

## 27:11

Westinghouse right so each one of these assemblies has uh 17 by 17 locations right for the fuel it's

## 27:19

now not every one of those locations is a fuel element some of them as indicated by

## 27:26

a little broad or for control we'll talk a little bit about control uh as we go along but you've got

## 27:32

17 by 17. what's 17 by 17 squared it's less than 400 right because that's 20 squared and then you've

## 27:40

got some number of control elements for a typical PWR the number of fuel elements is about 50 000

## 27:47

right you've got roughly 200 fuel assemblies a typical for Luke Westinghouse similar to what

## 27:53

you'd have at World Creek it's 193 of these assemblies each one was 17 by 17. overall

## 27:58

about 50 000 of these fuel elements now the actual fuel elements are built from the bottom

## 28:10

as little uranium pellets so these pellets are on the order of a centimeter they're cylindrical

## 28:16

right they're made out of uo2 density on the order of 10 grams per cubic centimeter these

## 28:23

things are stacked in a cylindrical array spring-loaded into some sort of canister that we

## 28:30

call cladding right that is one fuel element so when we think of a fuel element or a fuel rod

## 28:36

whatever name you want to use it's actually for most reactors just a series of vertically stacked

## 28:42

uo2 pellets right I used to have one of those you know fake uo2 pellets that you could pass

## 28:49

around for like class demos and so anybody see one of those before and I'll have to dig up mine

## 28:55

and pass it around right anyway so these things are arrayed then into fuel assemblies

## 29:00

now why would these fuel elements be put into fuel assemblies it's really just logistics

## 29:08

right you could never deal with individual pellets right so it makes sense to stack them

## 29:13

in some way but even if you do that with 50 000 if you're trying to do some maneuvering in a

## 29:18

reactor with 50 000 individual elements it would be a nightmare so it's much easier to reduce the

## 29:23

number of things that you work with to roughly 200 as is the case for a pretty large PWR

## 29:30

and that makes it easier to transport the fuel to move the fuel within the core to take out fuel

## 29:37

for inspection to put it into storage right outside of the plant and so forth just makes

## 29:42

life life easier so by and large nuclear power plants will use assemblies of fuel now they might

## 29:50

not all look like this but the idea is reasonably long cylindrical rods of fuel usually made up of

## 29:58

pellets assembled into something

## 30:00

like this right and you see for scale here this is about you know centimeter the actual height of

## 30:07

the fuel is three to four meters right so what what does that 30 feet or snow 15 foot yeah so so

## 30:16

that a small fraction of the overall height of that pressure vessel right you need a lot of space

## 30:21

in the pressure vessel to deal with the coolant flow and controlled drive mechanisms and so forth

## 30:27

right so I in the image here

## 30:30

you can see sort of a darker gray at a number of these locations that's the control rods so in the

## 30:37

PW oh you can see them here they look like the gaps with the background color associated with

## 30:44

water this is where the control elements would be inserted uh into a PWR from the top so that's part

## 30:51

of the reason why the diagram I showed you before is so much taller than the core itself you've got

## 30:56

these um rods that look form factor wise

## 31:00

right the fuel elements that are then inserted usually these things are made of boron sometimes

## 31:06

cadmium could be hafnium possibly even gadolinium these things are neutron poisons what's a poison

## 31:14

well neutron poison is just a material that eats up neutrons without giving us anything back so

## 31:20

strong absorption cross sections right boron 10 is probably the most common thing so

## 31:30

where do we get the power from

## 31:33

the reactor well we know that what's driving the entire thing is the chain nuclear reaction driven

## 31:39

by fission right for a thermal uh Spectrum reactor the neutrons get down through that nasty
resonance

## 31:46

range causing fission where the fission cross-section U-235 is very large okay I had a

## 31:51

good question from one of you earlier it's like you've got the fission happening in the fuel so

## 31:56

here's our fuel pin cell right and there are three regions we've got the for a PWR or light water

## 32:02

reactor it's going to be water

## 32:03

we've got the red fuel meat and then we have this little gray area which is that

## 32:09

can around it which we call the cladding right so for scale this is you know on the order of a

## 32:14

centimeter so the diameter of the fuel is going to be a little less than a centimeter and then

## 32:19

the thickness of the clad will be you know on the order of millimeters right usually made out of

## 32:24

zirconium zirconium is used because it's got a reasonably small neutron cross-section across the

## 32:32

energies of interest right it doesn't

## 32:33

dissipate and turn into something that's really radioactive it doesn't get brittle or anything

## 32:38

like that on the other hand something like stainless steel has iron chromium some other

## 32:44

things that have quite large neutron cross sections anytime and by large cross-section I

## 32:50

mean large absorption cross-section anytime you put something in your reactor that eats neutrons

## 32:55

without giving you something back is a basically a parasite right so the more stuff that you have in

## 33:01

your reactor that is absorbing neutrons

## 33:03

the more fuel you have to put in to compensate for those losses our trigger reactor the cladding on

## 33:10

the fuel is stainless steel it's a research reactor so there are different needs it's not

## 33:14

all about neutron economy it's about safety right stainless steel is a really robust material of

## 33:20

course they have an issue right now with some something growing or a bit deposited whether

## 33:26

it's corrosion i i don't know kind of looks orange which makes me think iron oxide but they'll get

## 33:33

that figured out but by and large stainless steel is really good robust but it does require you to

## 33:39

have more fuel okay so this is the basic uh sort of cutaway of the fuel and we're going to use this

## 33:46

uh next week when we get into uh kind of breaking up what contributions to k infinity there are

## 33:54

when we go from the energy only view of all this stuff to something that actually has a

## 33:59

spatial dependence right so we'll be able to break up fluxes into

## 34:03

things that are in the fuel and then not in the fuel but as far as the power if this is our fuel

## 34:10

what's happening in the fuel we've got fission right we're producing these really massive

## 34:15

charged fission fragments that have a lot of kinetic energy okay you know 200 mep work what

## 34:21

are they doing they're just bouncing around the rest of the o2 atoms and nuclei right and as they

## 34:27

lose the energy that causes everything to vibrate and what is vibration well that's the

## 34:33

thermal energy it's thermal agitation so as the kinetic energy is lost this entire red region

## 34:40

heats up right with all its thermal energy and so what you end up with is a heat flux that

## 34:46

has to go somewhere it goes through the cladding and into the coolant

## 34:51

and so the coolant is going to heat up and in order to get that heat taken away to somewhere

## 34:56

where it can be used it has to be flowing right you can probably rely a little bit on some natural

## 35:03

energy and some some alternative reactor designs specifically with an intent to be safe passively

## 35:11

right without any sort of forced flow and so forth would rely on that but for the reactors that we

## 35:16

have this coolant is flowing with substantial force right there are massive pumps at these

## 35:25

reactor plants to get the fluid going through this primary loop up through the assemblies

## 35:33

fuel elements and so forth right and so that coolant goes and then you know ultimately

## 35:40

enters a steam generator the heat exchanger dumps its heat into the other side that other side

## 35:46

will expand into steam hit the turbine spin the turbine get the generator going we get our

## 35:51

electricity because we're dealing with water of course the temperatures are limited to you know

## 35:57

what we can work with for our our system here it's about you know on the order of 300 degrees c

## 36:03

why there are a couple reasons one the cladding the zirconium will it has some some it has some

## 36:10

temperature peaks beyond which you can start having water zirconium interactions that lead

## 36:16

to hydrogen production that's not good because hydrogen is you know one it's a gas so anytime

## 36:23

you have gas in an otherwise fluid system you're going to get little pockets of gas that can

## 36:27

pressurize signal and not be good of course hydrogen is also flammable right so if you remember back
to the fruit

## 36:33

Shima accident, there was some apparent explosions. That wasn't the reactor exploding. That was

## 36:38

actually hydrogen that had built up from the melting of the cladding through this

## 36:43

zirconium water interaction. So we keep the overall temperatures set so that the cladding

## 36:51

is not, the cladding temperatures are not exceeded. The fuel, it's UO2, right, which

## 36:58

anytime you have an oxygen like that, you should think about ceramic, pretty high melting

## 37:04

temperature. I think something like 2,500 degrees Fahrenheit, possibly, right? So in a typical

## 37:10

reactor, though, the centerline temperature, which, you know, here, or this is, I guess, cut

## 37:16

away, that's where the fuel temperature is largest. That tends to be, you know, 12 to 1,500 degrees

## 37:23

Fahrenheit, if I recall, or maybe I think we see. Later in the course, we'll actually

## 37:28

probably spend a little bit of time analyzing this. Who's in heat transfer?

## 37:34

Right, so by this time in the course, you're probably experts with conduction.

## 37:39

Yeah, so you can analyze this problem primarily with conduction, although, of course, with

## 37:45

coolant flow, you've got to put in some magical H for the heat transfer coefficients. I'd use

## 37:51

some correlation. So heat transfer, it's just like what we've been doing with nuclear. We try

## 37:56

to take the data and simplify it, right? That's the way we do it.

## 37:58

That's the art of engineering. Any questions about this? So PWRs aren't the only reactor type

## 38:11

that we have, right? So here's, again, that PWR. A boiling water reactor, basically the same

## 38:18

structure of fuel. You've got these centimeter-sized things, array. The bundles tend to be

## 38:24

smaller, right? Rather than 17 by 17, it might be 8 by 8 or 10 by 10. The control mechanisms look a

## 38:31

little different. They're not the same. They're not the same. They're not the same. They're not the

## 38:31

same. So rather than having these fingers of boron 10 or whatever come down into the fuel, in a BWR,

## 38:40

you have cruciform elements that go up through or to the side of the fuel assembly. So I can

## 38:51

sketch that just briefly here, right? So if I've got in a BWR, I might have a fuel assembly that

## 39:00

looks like this. And then I might have a fuel assembly that looks like this. And then I might

## 39:01

have this with its fuel. Maybe I'll have two large water gaps for the purpose of moderation and

## 39:11

cooling, right? And then I'll have an array of these. And I won't repeat that. But in between

## 39:22

them, we'll have a cruciform. So it looks like a plus symbol, right? That is inserted in between

## 39:32

the assembly. And then I'll have a cruciform that looks like a plus symbol, right? That is inserted

## 39:32

in between the assemblies, not from the top, as in a PWR, but from the bottom. Why?

## 39:41

Well, so we had sketched before the PWR. You've got this pressure vessel. You've got the core.

## 39:50

You've got some sort of heat exchanger that we call the steam generator in there.

## 39:56

And you've got control that comes down from the top, okay? All of the water in that,

## 40:03

in the plant, is liquid, right? It's pressurized. Always under pressure. It's flowing liquid water.

## 40:10

Well, in a PWR, you've got your core. You've got primary water that goes, and the primary water,

## 40:25

rather than going through a heat exchanger, goes directly in to the turbine. So, by the time it

## 40:34

gets to the turbine, it can't be liquid water because you don't spin the turbine. So, it's a,

## 40:37

Because you don't spin the turbine with liquid water, right?

## 40:39

You spin it with steam.

## 40:40

So in a BWR, the water that is forced through the core, right?

## 40:48

I won't draw the rest of it, actually heats up to the point where it boils, which is why, of course,
it's called a boiling water reactor.

## 40:57

So a boiling water reactor is simpler in the sense that there is only one loop of fluid.

## 41:02

Your working fluid is exactly what goes through the core and spins the turbine.

## 41:06

In a PWR, you've got two loops that are separated by the heat exchanger, right?

## 41:11

So you've got primary and secondary.

## 41:13

Why would we choose one over the other?

## 41:17

That's a good question.

## 41:18

If you look back historically at the plants that were produced, we've got about two PWRs to every
BWR.

## 41:25

Part of that could be because of the origin of nuclear power.

## 41:30

What was the first nuclear reactor that produced power?

## 41:34

O1.

## 41:36

O1.

## 41:36

O2.

## 41:37

O3.

## 41:37

O4.

## 41:38

O5.

## 41:38

O6.

## 41:39

O7.

## 41:39

O8.

## 41:40

O9.

## 41:40

O11.

## 41:41

O12.

## 41:41

O13.

## 41:42

O14.

## 41:42

O15.

## 41:43

O16.

## 41:43

O17.

## 41:44

O18.

## 41:44

O19.

## 41:45

O20.

## 41:45

O21.

## 41:46

O22.

## 41:46

O23.

## 41:47

O24.

## 41:47

O25.

## 41:48

O26.

## 41:48

O27.

## 41:49

O28.

## 41:49

O29.

## 41:50

O30.

## 41:50

O31.

## 41:51

O32.

## 41:51

O34.

## 41:52

O35.

## 41:52

O36.

## 41:53

O37.

## 41:53

O38.

## 41:54

O39.

## 41:54

O40.

## 41:55

O41.

## 41:55

O42.

## 41:56

O43.

## 41:56

O44.

## 41:57

O45.

## 41:57

O46.

## 41:58

O47.

## 41:58

O41.

## 42:01

We probably have more time.

## 42:02

We probably have more time.

## 42:05

So that's all things for the current

## 42:07

ones.

## 42:07

I think I think now that I've

## 42:08

said probably the only thing we

## 42:09

can do, we would like to thank

## 42:10

for you, for discussed

## 42:11

talking about the

## 42:12

improvement that you've made

## 42:13

from the

## 42:24

mix that our

## 42:25

university have seen and

## 42:26

Ona небольшer other than

## 42:26

that,

## 42:27

but we led

## 42:28

a measured

## 42:28

All of the submarines have pressurized water reactors, not boiling water reactors.

## 42:33

Why?

## 42:34

What happens to water when it boils?

## 42:37

What happens to the density of water when it boils?

## 42:42

It goes down.

## 42:43

What is the moderator in a thermal spectrum water-cooled reactor?

## 42:51

At least in our water reactors, it's water.

## 42:54

So if you take the density of your moderator and you reduce it, what does that mean for the volume
of your reactor?

## 43:05

Well, if your density goes down, you need a larger volume to have the same amount of mass.

## 43:10

So for a given fuel, basically for the number of UO2 molecules that you have, there's a certain
amount of water that you need in order to slow those neutrons down.

## 43:20

And if on the average, the density is lower in a BW,

## 43:24

because you're boiling the water, you simply need a bigger reactor, which is why BWRs are
significantly larger than PWRs, right?

## 43:32

If you're talking about a submarine that is kind of lacking in space, you don't want to make your
reactor bigger than it needs to be, right?

## 43:40

So the fact that PWRs were the first sort of developed reactors might be one reason why we have more
of them, right?

## 43:47

That's what we started with.

## 43:49

BWRs can be nice because they don't have that secondary loop, right?

## 43:54

It's all just kind of direct.

## 43:56

And there are some other features of BWRs that are nice.

## 44:00

They're more complicated from a reactor physics standpoint.

## 44:02

If you've got a bigger reactor, you've got more stuff that can happen on the spatial side, right?

## 44:09

There can be instabilities when you've got boiling water, you've got power that's driving the
reduction in the density.

## 44:17

And so things can start to oscillate.

## 44:19

So it's significantly more challenging from the reactor physics side.

## 44:24

But the basic form factors that we're talking about for the fuel is the same.

## 44:31

Another type of fuel are these things.

## 44:34

Anybody recognize these?

## 44:35

These are essentially can-do assemblies.

## 44:42

So you'll find in the book, there's a nice diagram of can-do reactors.

## 44:46

They're a little bit strange because rather than being vertical, they are horizontal, right?

## 44:56

So in a can-do reactor, you've got your main building or the core area.

## 45:06

You've got a number of these pressure tubes, right?

## 45:11

And in each one of these pressure tubes, we put these bundles of fuel that we just saw a picture of.

## 45:27

And when they're done...

## 45:29

The other side, they pop, okay?

## 45:32

What's the rest of this stuff?

## 45:35

Where is my...

## 45:36

Right?

## 45:37

The rest of this stuff...

## 45:39

So these are the pressure tubes.

## 45:41

That's where these things go.

## 45:43

And then everything else is filled with heavy water, okay?

## 45:49

So it's a heavy water moderated reactor.

## 45:55

The pressure tube has pressurized light water reactors, the working heat transfer fluid.

## 46:01

But you've got this large volume of heavy water called calandria.

## 46:06

I have no idea where the name comes from.

## 46:08

But it's basically just a block of heavy water into which are these pressure tubes where you have
these fuel elements with whatever the number of rods is, right?

## 46:25

And so that's what's used in Canada.

## 46:28

Because the heavy water is used, there is a reduction in the enrichment.

## 46:34

So in a PWR, like Wolf Creek, enrichment is about 4%.

## 46:39

You cannot have a light water reactor be fueled with natural uranium.

## 46:44

You always have to have some enrichment.

## 46:46

And that's something that you can show even from the data that you've been using, okay?

## 46:51

When you go to D2O or graphite, you can't.

## 46:55

But you have to have a bigger reactor.

## 46:58

So it can do cores that are quite large, right?

## 47:01

This is a cutaway of one of the PWRs.

## 47:04

And that's...

## 47:04

And just as a comparison, I've put this here.

## 47:07

Anybody recognize this reactor?

## 47:10

Yeah, that's right from our reactor website.

## 47:13

So the fuel elements for our trigger reactor are also cylindrical.

## 47:17

They're a little bit bigger.

## 47:18

It's about an inch and a half diameter as opposed to a centimeter, right?

## 47:22

It's just bigger.

## 47:23

The fuel is uranium, but it's actually uranium mixed with zirconium hydride, right?

## 47:30

So it's a different fuel type.

## 47:32

But it's arranged in a form factor.

## 47:34

Not too dissimilar from a power reactor.

## 47:37

We don't make power, right?

## 47:39

We don't make usable power.

## 47:40

Certainly, we produce heat.

## 47:43

Anyway, I thought that that was sort of an interesting comparison to make, okay?

## 47:48

But those are all thermal spectrum reactors.

## 47:51

We've also talked about fast spectrum reactors.

## 47:55

Most fast spectrum reactors have the same form factor.

## 47:59

Long cylindrical tubes filled with pellets or some other cylindrical...

## 48:04

form of the fuel, and then everything is arranged in some sort of lattice.

## 48:09

Now, the one difference between a water pooled reactor, water moderated reactor, and a fast reactor
is the spacing of the fuel is usually smaller.

## 48:19

Why?

## 48:20

It reduces the amount of crap that could slow the neutrons down.

## 48:24

In a fast reactor, you want the neutrons to stay as fast as possible.

## 48:27

Any structural material that would cause neutrons to slow down, primarily, say, through inelastic
scattering,

## 48:34

has to be minimized, and so you do that by packing in the fuel as closely as you can without
limiting your ability to push some working fluid through to remove the heat.

## 48:46

Now, in a fast reactor, typically, that working fluid is going to be a molten metal, right?

## 48:51

So, sodium, lead, lead bismuth, all sorts of eutectics are used.

## 48:56

There are some fast reactor designs that use gas, so helium, as a coolant, right?

## 49:04

Right.

## 49:04

Right.

## 49:04

Right.

## 49:04

Right.

## 49:04

Right.

## 49:04

helium, as a gas, the density is not large enough for that low mass to have an impact on the neutron
spectrum, but it has been used.

## 49:15

I'm trying to think.

## 49:17

Maybe there's one demonstration reactor, but anyway, the point here is that the structure looks
quite a bit like that, but they don't have to be cylindrical rods.

## 49:28

Usually, where you see other form factors is not necessarily in power reactor applications.

## 49:34

This is a...

## 49:35

This is a diagram of ATR, the Advanced Test Reactor out at Idaho National Laboratory.

## 49:40

Here's another one of the serpent images, Monte Carlo tool.

## 49:44

This thing has a wild shape.

## 49:46

Why?

## 49:47

Why?

## 49:47

They do all sorts of materials testing, a lot for the Navy, and what they do by having this kind of
weird design is have incredibly large fluxes, you know, factors of two or more greater than what we
have in a typical commercial light water reactor.

## 50:05

So, you can...

## 50:05

Accelerate the degradation of materials that you put in there.

## 50:10

All sorts of things that can move around there, I believe a lot of these things, the circles on the
outside are beryllium reflectors, right, so that they can really drive reaction rates up in some of
the locations.

## 50:24

What else?

## 50:25

Let's see.

## 50:26

Yeah.

## 50:27

This is a cartoon of a concept called the pebble bed reactor, where the fuel is no longer a
cylinder.

## 50:35

I believe it's not a cylinder, right?

## 50:36

It's a cylinder, no matter how you put it.

## 50:38

But a sphere loaded with something called Triso fuel.

## 50:42

And I put this thing in the background, Triso X is the fuel produced by X Energy, which over the
past two years has been given several tens of millions of dollars from the US government through
contracts to do some demonstration stuff.

## 50:57

I believe they might have some links to the Department of Defense for exploring small reactors

## 51:04

for deployment in military operations, where things are...

## 51:05

increasing just as they are in the civilian space things are increasingly being electrified

## 51:10

and so having sources of electricity that go beyond you know fossil fuels is a increasing

## 51:16

interest in those spheres um but anyway yes we've got this now one comment i'll say about this

## 51:24

before we break is when you have the triso fuel with this multi-layered thing you've got the sort

## 51:30

of uo2 kernel on the inside but then it's surrounded by several barriers that increases

## 51:36

or builds in this this idea of containment and so you'll often find that triso fuel is an integral

## 51:43

part of so-called advanced but safer reactors right because if when done right you can

## 51:52

reduce the amount of containment that is there on site why does that matter turns out that

## 52:00

constantly

## 52:00

concrete and steel are really expensive doesn't seem like it right you know maybe per volume that

## 52:06

you're used to working with but the amounts needed for large-scale plants is really really

## 52:13

hard to comprehend which is why to build a brand new nuclear plant that would be similar to wolf

## 52:18

creek would be more than 10 billion dollars right and a large part of that is from the simplest

## 52:26

stuff the concrete the steel not the nuclear stuff the nuclear fuel

## 52:30

is actually pretty cheap comparatively speaking right it's that that infrastructure that's needed

## 52:36

and so anything like this that can possibly reduce that is of uh significant interest so i'm going
to

## 52:41

leave it off with that on wednesday we'll chat a little bit about fast spectrum reactor they'll try

## 52:46

to come up with some more detailed uh information for from some of those things but we're gonna

## 52:51

care for the next several lessons about the unit stuff that's just this picture of the fuel bin

## 52:58

surrounded by the coolant

## 53:00

Right. There'll be a new tube, water, we'll get the thermal connective stuff,

## 53:05

PWR type fuel cell. On Wednesday, it'll be UO2, maybe this is sodium, right, for the

## 53:12

related to capacity reactions, right. We're going to use that picture

## 53:16

for a lot of our analysis going forward. All right. I'll see you all on Wednesday.

## 53:32

Thank you.
