\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{ne630boardhandout}[2026/08/26 v1.2 Myriad Pro NE 630 handouts]

\newif\ifhandoutinstructor
\handoutinstructorfalse
\DeclareOption{student}{\handoutinstructorfalse}
\DeclareOption{instructor}{\handoutinstructortrue}
\DeclareOption*{\PassOptionsToClass{\CurrentOption}{article}}
\ProcessOptions\relax
\LoadClass[10pt]{article}

\RequirePackage{iftex}
\ifPDFTeX
  \ClassError{ne630boardhandout}
    {This class requires XeLaTeX or LuaLaTeX}
    {Run latexmk with the -xelatex option so Myriad Pro can be loaded.}
\fi
\RequirePackage{fontspec}
\RequirePackage{microtype}

% Use the locally installed Adobe fonts without redistributing them.
% The first path supports WSL; the second supports native Windows TeX.
\newcommand{\MyriadProPath}{}
\IfFileExists{/mnt/c/Windows/Fonts/Myriad-Pro-Regular.OTF}{%
  \renewcommand{\MyriadProPath}{/mnt/c/Windows/Fonts/}%
}{%
  \IfFileExists{C:/Windows/Fonts/Myriad-Pro-Regular.OTF}{%
    \renewcommand{\MyriadProPath}{C:/Windows/Fonts/}%
  }{%
    \ClassError{ne630boardhandout}
      {Myriad Pro was not found}
      {Install Myriad Pro in the Windows Fonts directory.}%
  }%
}

\defaultfontfeatures{Ligatures=TeX}
\setmainfont{Myriad-Pro-Regular.OTF}[
  Path=\MyriadProPath,
  BoldFont=Myriad-Pro-Semibold.OTF,
  ItalicFont=Myriad-Pro-Regular.OTF,
  ItalicFeatures={FakeSlant=0.18},
  BoldItalicFont=Myriad-Pro-Semibold-It.OTF
]
\setsansfont{Myriad-Pro-Regular.OTF}[
  Path=\MyriadProPath,
  BoldFont=Myriad-Pro-Semibold.OTF,
  ItalicFont=Myriad-Pro-Regular.OTF,
  ItalicFeatures={FakeSlant=0.18},
  BoldItalicFont=Myriad-Pro-Semibold-It.OTF
]
\RequirePackage[
  letterpaper,
  left=0.48in,
  right=0.48in,
  top=0.48in,
  bottom=0.44in,
  headheight=20pt,
  headsep=2pt,
  footskip=16pt,
  includeheadfoot
]{geometry}
\RequirePackage{xcolor}
\RequirePackage{amsmath,mathtools}
\RequirePackage{unicode-math}
\setmathfont{LibertinusMath-Regular.otf}
\RequirePackage{enumitem}
\RequirePackage{paracol}
\RequirePackage{ragged2e}
\RequirePackage{tabularx,booktabs,array}
\RequirePackage{tcolorbox}
\tcbuselibrary{skins}
\RequirePackage{needspace}
\RequirePackage{fancyhdr}
\RequirePackage{lastpage}
\RequirePackage{xparse}
\RequirePackage[hidelinks]{hyperref}

% K-State-inspired palette; all boxes remain intelligible in grayscale.
\definecolor{KSUPurple}{HTML}{512888}
\definecolor{KSUDeepPurple}{HTML}{3B1B64}
\definecolor{KSUTeal}{HTML}{008C95}
\definecolor{KSUOrange}{HTML}{CA7C1B}
\definecolor{KSUGray}{HTML}{5D5D5D}
\definecolor{KSULightGray}{HTML}{F3F3F3}

% Color communicates pedagogical role rather than topic:
% purple = supplied reference, gray = student construction space,
% orange = formative check, and teal = synthesis or a revealed result.
\colorlet{HandoutReference}{KSUPurple}
\colorlet{HandoutWorkspace}{KSUGray}
\colorlet{HandoutCheckpoint}{KSUOrange}
\colorlet{HandoutSynthesis}{KSUTeal}

\setlength{\parindent}{0pt}
\setlength{\parskip}{0pt}
\setlength{\columnsep}{0.24in}
\emergencystretch=1.5em

\setlist[itemize]{leftmargin=1.35em,itemsep=1pt,topsep=2pt,parsep=0pt,partopsep=0pt}
\setlist[enumerate]{leftmargin=1.55em,itemsep=1pt,topsep=2pt,parsep=0pt,partopsep=0pt}

\newcommand{\HandoutCourse}{NE 630}
\newcommand{\HandoutLesson}{00}
\newcommand{\HandoutTitle}{Handout}
\newcommand{\HandoutReading}{Preparation noted in the lesson plan.}
\NewDocumentCommand{\HandoutSetup}{m m m m}{%
  \renewcommand{\HandoutCourse}{#1}%
  \renewcommand{\HandoutLesson}{#2}%
  \renewcommand{\HandoutTitle}{#3}%
  \renewcommand{\HandoutReading}{#4}%
}

\pagestyle{fancy}
\fancyhf{}
\fancyhead[L]{\sffamily\bfseries\small \HandoutCourse}
\fancyhead[C]{\sffamily\small \HandoutTitle}
\fancyhead[R]{\sffamily\bfseries\small Lesson \HandoutLesson}
\fancyfoot[C]{\sffamily\scriptsize \thepage\ of \pageref*{LastPage}}
\renewcommand{\headrulewidth}{0.5pt}
\renewcommand{\footrulewidth}{0pt}
\makeatletter
\renewcommand{\headrule}{\hbox to\headwidth{\color{KSUPurple}\leaders\hrule height \headrulewidth\hfill}}
\makeatother

\fancypagestyle{handoutfirst}{%
  \fancyhf{}%
  \fancyfoot[C]{\sffamily\scriptsize \thepage\ of \pageref*{LastPage}}%
  \renewcommand{\headrulewidth}{0pt}%
  \renewcommand{\footrulewidth}{0pt}%
}

\NewDocumentCommand{\MakeHandoutTitle}{}{%
  \thispagestyle{handoutfirst}%
  \vspace*{\dimexpr-\headheight-\headsep\relax}%
  \begin{tcolorbox}[
    enhanced,
    frame hidden,
    colback=white,
    left=0pt,right=0pt,top=1pt,bottom=2pt,
    borderline west={4pt}{0pt}{KSUPurple},
    before skip=0pt,after skip=3pt
  ]
    \begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}X>{\raggedleft\arraybackslash}p{1.20in}@{}}
      {\sffamily\bfseries\fontsize{17}{19}\selectfont \HandoutTitle} &
      {\sffamily\bfseries\large Lesson \HandoutLesson}\\[-1pt]
      {\sffamily\small \HandoutCourse} &
      {}
    \end{tabularx}
  \end{tcolorbox}
  \begin{tcolorbox}[
    enhanced,
    boxrule=0.45pt,
    colframe=KSUPurple!45,
    colback=KSUPurple!4,
    arc=1.2pt,
    left=5pt,right=5pt,top=3pt,bottom=3pt,
    before skip=0pt,after skip=5pt
  ]
    \sffamily\small\textbf{Prepare:} \HandoutReading
  \end{tcolorbox}
}

\newenvironment{handoutcolumns}{%
  \columnratio{0.5}%
  \begin{paracol}{2}%
  \RaggedRight
}{%
  \end{paracol}
}

\NewDocumentCommand{\HandoutSection}{m m}{%
  \par\addvspace{5pt}\Needspace{3.2\baselineskip}%
  \noindent
  \colorbox{KSUPurple}{\color{white}\sffamily\bfseries\strut\hspace{2pt}#1\hspace{2pt}}%
  \hspace{0.45em}{\sffamily\bfseries\color{KSUDeepPurple}#2}\par
  \vspace{1pt}{\color{KSUPurple!35}\rule{\linewidth}{0.45pt}}\vspace{2pt}
}

\tcbset{
  handout base/.style={
    enhanced,
    boxrule=0.45pt,
    arc=1.2pt,
    left=5pt,right=5pt,top=4pt,bottom=4pt,
    before skip=4pt,after skip=4pt,
    fonttitle=\sffamily\bfseries\small,
    coltitle=KSUDeepPurple,
    attach boxed title to top left={xshift=4pt,yshift*=-1.4mm},
    boxed title style={frame hidden,colback=white,left=2pt,right=2pt,top=0pt,bottom=0pt}
  }
}

\newtcolorbox{fixedbox}[1]{
  handout base,
  title={#1},
  colframe=HandoutReference!45,
  colback=HandoutReference!3
}
\newtcolorbox{boardbox}[1]{
  handout base,
  title={#1},
  colframe=HandoutWorkspace!45,
  colback=white
}
\newtcolorbox{checkpoint}[1][Checkpoint]{
  handout base,
  title={#1},
  colframe=HandoutCheckpoint!70,
  colback=HandoutCheckpoint!7,
  coltitle=KSUDeepPurple
}
\newtcolorbox{takeawaybox}[1][Takeaway]{
  handout base,
  title={#1},
  colframe=HandoutSynthesis!65,
  colback=HandoutSynthesis!5,
  coltitle=KSUDeepPurple
}

\newenvironment{targetlist}{%
  \begin{itemize}[label={\raisebox{0.1ex}{\(\square\)}},leftmargin=1.45em]
}{%
  \end{itemize}
}

\NewDocumentCommand{\InstructorFigureContent}{+m}{%
  \ifhandoutinstructor #1\fi
}

\NewDocumentCommand{\Blank}{O{1.0in}}{%
  \leavevmode\makebox[#1][c]{\leaders\hbox to 0.42em{\hss.\hss}\hfill}%
}
\NewDocumentCommand{\RevealBlank}{O{1.0in} m}{%
  \ifhandoutinstructor
    \leavevmode\makebox[#1][c]{\textcolor{HandoutSynthesis}{\sffamily\bfseries #2}}%
  \else
    \Blank[#1]%
  \fi
}
\NewDocumentCommand{\MathBlank}{O{0.75in} m}{%
  \ifhandoutinstructor
    \makebox[#1][c]{\textcolor{HandoutSynthesis}{\ensuremath{#2}}}%
  \else
    \makebox[#1][c]{\rule[-0.15ex]{#1}{0.35pt}}%
  \fi
}

\newcount\handoutLineCount
\NewDocumentCommand{\RuledLines}{m}{%
  \begingroup
  \handoutLineCount=0
  \loop\ifnum\handoutLineCount<#1
    \par\vspace{0.48\baselineskip}\noindent
    {\color{KSUGray!28}\rule{\linewidth}{0.35pt}}%
    \advance\handoutLineCount by 1
  \repeat
  \endgroup
}

\NewDocumentCommand{\InstructorCue}{m}{%
  \ifhandoutinstructor
    \begin{tcolorbox}[
      enhanced,boxrule=0.4pt,arc=1pt,
      colframe=HandoutSynthesis!60,colback=HandoutSynthesis!5,
      left=4pt,right=4pt,top=2pt,bottom=2pt,
      before skip=3pt,after skip=3pt
    ]
      \sffamily\scriptsize\textbf{Instructor cue.} #1
    \end{tcolorbox}
  \fi
}

\NewDocumentCommand{\TermStrip}{m}{%
  \begin{tcolorbox}[
    enhanced,boxrule=0.35pt,arc=1pt,
    colframe=HandoutReference!35,colback=HandoutReference!3,
    left=4pt,right=4pt,top=3pt,bottom=3pt,
    before skip=3pt,after skip=3pt
  ]
    \sffamily\scriptsize\textbf{Vocabulary:} #1
  \end{tcolorbox}
}

\newcommand{\unit}[1]{\,\mathrm{#1}}
\newcommand{\Ktrue}{K_{\mathrm{true}}}
\newcommand{\Kclassical}{K_{\mathrm{classical}}}

\AtBeginDocument{\small}
