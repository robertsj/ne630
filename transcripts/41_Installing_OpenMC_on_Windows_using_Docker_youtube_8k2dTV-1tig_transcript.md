# 41_Installing_OpenMC_on_Windows_using_Docker Local Audio Transcript

Course: NE 630

Playlist source: https://youtube.com/playlist?list=PLy481lNHlnHoEO95vM-xYX2bydD25v20L

Video: Installing OpenMC on Windows using Docker

URL: https://www.youtube.com/watch?v=8k2dTV-1tig

Video ID: 8k2dTV-1tig

YouTube upload date: 20250924

Duration: 05:13

Transcript source: Local faster-whisper transcription from YouTube audio.

Whisper model: large-v3; detected language: en.

Generated: 2026-06-28

Note: This transcript is machine-generated from audio and lightly wrapped only. It should be reviewed before being quoted, published, or used as polished lesson text.

Requested language: en

## 00:06

All right. Let's see if we can get open and see on Windows using Docker. So I've already installed

## 00:12

the Docker desktop. This is an executable that you'll be able to find at the link here in the

## 00:19

Canvas page. It is available not only for Windows, but also Mac and Linux. So if you are using Mac,

## 00:26

the instructions that will follow should work also for that system, but I'm primarily trying

## 00:32

to get Windows covered here. Okay. So that's installed. Then we can search for OpenMC in the

## 00:39

search bar up here, and I'll do that here. And the one that we want is this one here with the

## 00:45

tag latest. And so I will pull this, which will download it. Now it is a substantial file and

## 00:55

it, because it contains all the nuclear data, as well as the OpenMC stuff, it's

## 01:01

called OpenMC. And so I'm going to go ahead and download it. So I'm going to go ahead and

## 01:02

download it. So I'm going to go ahead and download it. So I'm going to go ahead and download it. So

## 01:02

close to seven gigabytes. And let's see what I have for my images. So it looks like it is there.

## 01:10

And what I can do now is create a folder where I want to execute some examples. So I will go

## 01:18

here to my documents folder. And I already had an examples folder that I created when I was testing

## 01:25

this, but to make sure that this will work out of the box, I'll make a new folder, call it NE630

## 01:31

demo. I can spell. Okay. So once I have that, I can go into it and then I want to download these

## 01:40

files. So I will download Docker Compose, this .env file and the Docker file. Now here I can go

## 01:49

to downloads, find the three that were just downloaded. I will highlight them all, control

## 01:56

C to copy. I'll hit the back to go back to my demo. And then I will paste them all. And then I will

## 02:01

paste them here. You might have other ways that you do business, dragging and dropping, but this

## 02:05

is what I want to use to keep things going fast. All right. Now we have to open up the PowerShell.

## 02:12

Way that I do that is to enter PowerShell into this bottom search, click on it. We'll come up

## 02:18

with a black box that looks similar to some of what we've done on BayoCat. And I will then CD

## 02:24

into the directory I just created. So that should be from here. That will be CD

## 02:31

users. I'll use the full path. Roberts J is my username. Yours will be different, I hope.

## 02:39

And then I have it in documents and then NE630 demo. And if I want to check out what I have in

## 02:50

here, I hit use DIR or I think LS works in PowerShell. And there it is. Those are my three

## 02:57

files that I need in order to proceed. So if I click on it, I can see that I have a different

## 03:00

file that I need in order to proceed. So if I click on it and I click on it, I can see that I

## 03:00

need to proceed. So if I click on it, I can see that I need to proceed. So if I click on it, I can

## 03:01

want to build this environment in which I can run OpenMC, I can copy this command over here,

## 03:11

hit enter, and it will do some pre-processing that includes downloading Jupyter Notebook

## 03:19

for you and then getting things up and running. So if I copy this link, I should,

## 03:26

when I go to my browser, be able to see something that looks like this. Now,

## 03:38

all you need to do in order to run OpenMC in Jupyter Notebooks is put your Jupyter Notebook

## 03:44

there. As an example, I can do Python 3, and just to make sure that things are working as expected,

## 03:51

I'll do import OpenMC, I'll run this, and it imports, and that's that. The only thing

## 03:58

that you need to make sure that it's working is that the interface is running in Jupyter Notebook.

## 03:58

So that's it. We don't need to worry about that. I think the next step here is to run open mc to

## 03:58

know is that the data in the image in this environment is in a special location. If I do

## 04:07

ls on the root folder, there are a number of folders here that we have access to. The one

## 04:14

that we want is under, oh, I think it's under home. Nope, not under home, under

## 04:22

root. And then it's under NDC. And there are all of our H5 files. So in all the places that we had

## 04:38

something called data path defined before, we would have it defined like this. And from there,

## 04:46

you should be able to adapt all of the notebooks that we've had before. I will do my best to take

## 04:52

those notebooks and add them to the H5 folder. And then I'm going to go ahead and add them to

## 04:52

the H5 folder. And then I'm going to go ahead and add them to the H5 folder. And then I'm going to

## 04:52

update them so that they are ready to download and then place into that folder and work for

## 04:58

everybody. But this will be the major trick and really the only difference from what you needed

## 05:03

to do on Bailcat. So hopefully that works for everyone.
