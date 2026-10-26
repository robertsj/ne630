% NE 630: the single formatting backend for all course handouts.
\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{ne630handout}[2026/10/25 v2.0 Unified course handouts]
\newif\ifhandoutsolutions
\newif\ifhandoutcompact
\newif\ifhandoutfallbackfonts
\newif\ifhandoutboard
\handoutsolutionsfalse
\DeclareOption{solutions}{\handoutsolutionstrue}
\DeclareOption{nosolutions}{\handoutsolutionsfalse}
\DeclareOption{board}{\handoutboardtrue}
\DeclareOption{compact}{\handoutcompacttrue}
\DeclareOption{fallbackfonts}{\handoutfallbackfontstrue}
\DeclareOption*{\PassOptionsToClass{\CurrentOption}{article}}
\ProcessOptions\relax
\LoadClass[10pt,letterpaper]{article}
\RequirePackage{iftex}
\ifPDFTeX
  \ClassError{ne630handout}{This class requires XeLaTeX or LuaLaTeX}
    {Build with latexmk -xelatex. No shell escape is required.}
\fi
\RequirePackage{fontspec,microtype}
\defaultfontfeatures{Ligatures=TeX}
\newcommand{\SetHandoutFileFonts}[4]{%
  \setmainfont{#2}[
    Path={#1},
    BoldFont=#3,
    ItalicFont=#2,
    ItalicFeatures={FakeSlant=0.18},
    BoldItalicFont=#4
  ]%
  \setsansfont{#2}[
    Path={#1},
    BoldFont=#3,
    ItalicFont=#2,
    ItalicFeatures={FakeSlant=0.18},
    BoldItalicFont=#4
  ]%
}

\newcommand{\SetHandoutFallbackFonts}{%
  \ClassWarningNoLine{ne630handout}
    {Myriad Pro was not found in a known file path; using TeX Gyre Heros for text}%
  \setmainfont{texgyreheros-regular.otf}[
    BoldFont=texgyreheros-bold.otf,
    ItalicFont=texgyreheros-italic.otf,
    BoldItalicFont=texgyreheros-bolditalic.otf
  ]%
  \setsansfont{texgyreheros-regular.otf}[
    BoldFont=texgyreheros-bold.otf,
    ItalicFont=texgyreheros-italic.otf,
    BoldItalicFont=texgyreheros-bolditalic.otf
  ]%
}

\ifhandoutfallbackfonts
  \SetHandoutFallbackFonts
\else
% Use locally installed Adobe fonts without redistributing them.
\IfFileExists{/mnt/c/Windows/Fonts/Myriad-Pro-Regular.OTF}{%
  \SetHandoutFileFonts{/mnt/c/Windows/Fonts/}
    {Myriad-Pro-Regular.OTF}
    {Myriad-Pro-Semibold.OTF}
    {Myriad-Pro-Semibold-It.OTF}%
}{%
  \IfFileExists{C:/Windows/Fonts/Myriad-Pro-Regular.OTF}{%
    \SetHandoutFileFonts{C:/Windows/Fonts/}
      {Myriad-Pro-Regular.OTF}
      {Myriad-Pro-Semibold.OTF}
      {Myriad-Pro-Semibold-It.OTF}%
  }{%
    \IfFileExists{/home/robertsj/.local/share/fonts/adobe-cc/MyriadPro-Regular.otf}{%
      \SetHandoutFileFonts{/home/robertsj/.local/share/fonts/adobe-cc/}
        {MyriadPro-Regular.otf}
        {MyriadPro-Semibold.otf}
        {MyriadPro-SemiboldIt.otf}%
    }{%
      \SetHandoutFallbackFonts
    }%
  }%
}
\fi

% Retain optical-size Latin Modern Mono in the legacy compact board profile.
\ifhandoutboard\else
\setmonofont{texgyrecursor-regular.otf}[
  BoldFont=texgyrecursor-bold.otf,ItalicFont=texgyrecursor-italic.otf,
  BoldItalicFont=texgyrecursor-bolditalic.otf]
\fi
\RequirePackage[letterpaper,left=.48in,right=.48in,top=.48in,bottom=.44in,
  headheight=20pt,headsep=5pt,footskip=17pt,includeheadfoot]{geometry}
\RequirePackage{amsmath,mathtools,unicode-math}
\setmathfont{LibertinusMath-Regular.otf}
\RequirePackage{graphicx,xcolor,enumitem,paracol,multicol,ragged2e}
\RequirePackage{siunitx,cancel,xfrac,fvextra}
\RequirePackage{tabularx,booktabs,array,needspace,fancyhdr,lastpage,xparse}
\RequirePackage{tikz,pgfplots,listings}
\usetikzlibrary{arrows.meta,angles,quotes,calc,intersections,positioning,
  patterns,decorations.pathreplacing,shapes.geometric}
\pgfplotsset{compat=1.18}
\RequirePackage{tcolorbox}
\tcbuselibrary{skins,breakable,listings}
\RequirePackage[hidelinks]{hyperref}

% The public Wildcat roles match slides/beamercolorthemewildcat.sty exactly.
% Kept here (not loaded from Beamer) so a source bundle is self-contained.
\definecolor{wcprimary}{RGB}{81,40,136}
\definecolor{wcalerted}{RGB}{202,124,27}
\definecolor{wcexample}{RGB}{0,134,86}
\definecolor{wcprimary160}{RGB}{29,2,53}
\definecolor{wcprimary150}{RGB}{38,8,65}
\definecolor{wcprimary140}{RGB}{48,16,78}
\definecolor{wcprimary130}{RGB}{56,23,90}
\definecolor{wcprimary120}{RGB}{64,31,104}
\definecolor{wcprimary110}{RGB}{72,36,118}
\definecolor{wcprimary90}{RGB}{91,59,140}
\definecolor{wcprimary80}{RGB}{104,76,150}
\definecolor{wcprimary70}{RGB}{118,93,160}
\definecolor{wcprimary60}{RGB}{131,110,170}
\definecolor{wcprimary50}{RGB}{147,128,182}
\definecolor{wcprimary40}{RGB}{164,149,195}
\definecolor{wcprimary30}{RGB}{182,172,209}
\definecolor{wcprimary20}{RGB}{204,196,223}
\definecolor{wcprimary10}{RGB}{228,224,238}
\colorlet{KSUPurple}{wcprimary}
\colorlet{KSUDeepPurple}{wcprimary120}
\colorlet{KSUOrange}{wcalerted}
\definecolor{KSUTeal}{HTML}{008C95} % historical name, still available
\definecolor{KSUGray}{HTML}{5D5D5D}
\definecolor{KSULightGray}{HTML}{F3F3F3}
\colorlet{ksupurple}{wcprimary}
\colorlet{purple}{wcprimary}
\colorlet{orange}{wcalerted}
\definecolor{skyblue}{RGB}{180,220,255}
\colorlet{HandoutReference}{wcprimary}
\colorlet{HandoutWorkspace}{KSUGray}
\colorlet{HandoutCheckpoint}{wcalerted}
\colorlet{HandoutSynthesis}{wcexample}
\NewDocumentCommand{\Primary}{m}{\textcolor{wcprimary}{#1}}
\NewDocumentCommand{\Alert}{m}{\textcolor{wcalerted}{#1}}
\NewDocumentCommand{\Example}{m}{\textcolor{wcexample}{#1}}
% Beamer-style text emphasis without Beamer or overlay syntax.
\providecommand{\alert}[1]{\Alert{#1}}

\setlength{\parindent}{0pt}
\setlength{\columnsep}{.24in}
\setlength{\emergencystretch}{1.5em}
\setlist[itemize]{leftmargin=1.35em,itemsep=2pt,topsep=3pt,parsep=0pt,partopsep=0pt,
  label=\textcolor{wcprimary}{\textbullet}}
\setlist[enumerate]{leftmargin=1.55em,itemsep=2pt,topsep=3pt,parsep=0pt,partopsep=0pt}
\renewcommand{\arraystretch}{1.12}
\ifhandoutboard\renewcommand{\arraystretch}{1}\fi
\newcolumntype{Y}{>{\RaggedRight\arraybackslash}X}
% Typography is configured here; wrappers may request a measured compact size.
\newcommand{\HandoutFontSize}{9.5}
\newcommand{\HandoutLeading}{11.5}
\newcommand{\HandoutParagraphSkip}{3pt}
\ifhandoutcompact
  \renewcommand{\HandoutFontSize}{9}
  \renewcommand{\HandoutLeading}{10.7}
  \renewcommand{\HandoutParagraphSkip}{2pt}
\fi
\ifhandoutboard
  \renewcommand{\HandoutFontSize}{9}
  \renewcommand{\HandoutLeading}{11}
  \renewcommand{\HandoutParagraphSkip}{0pt}
  \geometry{headsep=2pt,footskip=16pt}
  \setlist[itemize]{itemsep=1pt,topsep=2pt}
  \setlist[enumerate]{itemsep=1pt,topsep=2pt}
\fi
\NewDocumentCommand{\HandoutTypography}{m m m}{%
  \gdef\HandoutFontSize{#1}\gdef\HandoutLeading{#2}%
  \gdef\HandoutParagraphSkip{#3}}
\newcommand{\HandoutBody}{%
  \fontsize{\HandoutFontSize}{\HandoutLeading}\selectfont
  \setlength{\parskip}{\HandoutParagraphSkip}%
  \setlength{\topsep}{2pt}\setlength{\partopsep}{0pt}%
  \setlength{\abovedisplayskip}{4pt plus 1pt minus 1pt}%
  \setlength{\belowdisplayskip}{4pt plus 1pt minus 1pt}%
  \setlength{\abovedisplayshortskip}{3pt}%
  \setlength{\belowdisplayshortskip}{3pt}\setlength{\jot}{3pt}%
  \RaggedRight}
\AtBeginDocument{%
  \ifhandoutboard
    \small
    \fontsize{\HandoutFontSize}{\HandoutLeading}\selectfont
    \setlength{\parskip}{\HandoutParagraphSkip}%
  \else\HandoutBody\fi}

% One metadata/title API; both historical interfaces delegate to it.
\newcommand{\HandoutCourse}{NE 630}
\newcommand{\HandoutLesson}{00}
\newcommand{\LessonNo}{\HandoutLesson}
\newcommand{\HandoutTitle}{Handout}
\newcommand{\HandoutReading}{Preparation noted in the lesson plan.}
\newcommand{\HandoutQuestion}{}
\NewDocumentCommand{\HandoutSetup}{m m m m}{%
  \gdef\HandoutCourse{#1}\gdef\HandoutLesson{#2}%
  \gdef\HandoutTitle{#3}\gdef\HandoutReading{#4}}
\pagestyle{fancy}
\fancyhf{}
\fancyhead[L]{\sffamily\bfseries\small\HandoutCourse}
\fancyhead[C]{\sffamily\small\ifhandoutboard\HandoutTitle\else Nuclear Reactor Theory\fi}
\fancyhead[R]{\sffamily\bfseries\small Lesson \LessonNo}
\fancyfoot[C]{\sffamily\scriptsize\thepage\ of \pageref*{LastPage}}
\renewcommand{\headrulewidth}{.5pt}
\renewcommand{\footrulewidth}{0pt}
\renewcommand{\headrule}{\hbox to\headwidth{\color{wcprimary}\leaders\hrule height \headrulewidth\hfill}}
\fancypagestyle{handoutfirst}{%
  \fancyhf{}\fancyfoot[C]{\sffamily\scriptsize\thepage\ of \pageref*{LastPage}}%
  \renewcommand{\headrulewidth}{0pt}}
\NewDocumentCommand{\MakeHandoutTitle}{}{%
\ifhandoutboard
%
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

\else
%
  \thispagestyle{handoutfirst}%
  \vspace*{\dimexpr-\headheight-\headsep\relax}%
  \noindent\begin{minipage}[c]{.025\linewidth}\color{wcprimary}\rule{3.5pt}{38pt}\end{minipage}%
  \begin{minipage}[c]{.835\linewidth}
    {\sffamily\bfseries\fontsize{17}{19}\selectfont\HandoutTitle\par}%
    {\sffamily\fontsize{8.5}{10}\selectfont\HandoutCourse\enspace|\enspace Nuclear Reactor Theory\par}%
  \end{minipage}\hfill
  \begin{minipage}[c]{.12\linewidth}\raggedleft
    {\sffamily\bfseries\fontsize{26}{28}\selectfont\color{wcprimary}\HandoutLesson\par}%
    {\sffamily\scriptsize LESSON}
  \end{minipage}\par\vspace{3pt}%
  \begin{tcolorbox}[handout base,colback=wcprimary!4,colframe=wcprimary!35,
    top=3pt,bottom=3pt,before skip=0pt,after skip=4pt]
    {\sffamily\fontsize{8.5}{10}\selectfont\textbf{Read:} \HandoutReading}
  \end{tcolorbox}%
  \ifx\HandoutQuestion\empty\else
    {\sffamily\color{wcprimary120}\HandoutQuestion\par}\smallskip
  \fi
\fi
}
\NewDocumentCommand{\Lesson}{m m m m}{%
  \HandoutSetup{NE 630}{#1}{#2}{#3}\gdef\HandoutQuestion{#4}\MakeHandoutTitle}
\NewDocumentCommand{\HandoutContinue}{m}{%
  \par{\sffamily\bfseries\fontsize{13}{15}\selectfont\color{wcprimary}#1\par}%
  \vspace{2pt}{\color{wcprimary!35}\hrule height .5pt}\vspace{5pt}}
\NewDocumentCommand{\HandoutSection}{m m}{%
\ifhandoutboard
%
  \par\addvspace{5pt}\Needspace{3.2\baselineskip}%
  \noindent
  \colorbox{KSUPurple}{\color{white}\sffamily\bfseries\strut\hspace{2pt}#1\hspace{2pt}}%
  \hspace{0.45em}{\sffamily\bfseries\color{KSUDeepPurple}#2}\par
  \vspace{1pt}{\color{KSUPurple!35}\rule{\linewidth}{0.45pt}}\vspace{2pt}

\else
%
  \par\addvspace{6pt}\Needspace{3.2\baselineskip}\noindent
  \colorbox{wcprimary}{\color{white}\sffamily\bfseries\fontsize{9}{10}\selectfont\strut #1}%
  \hspace{3pt}{\sffamily\bfseries\color{wcprimary120}\fontsize{10.5}{12}\selectfont #2}\par\vspace{2pt}
\fi
}
\NewDocumentCommand{\Sec}{m m}{\HandoutSection{#1}{#2}}

% Two-column modes: automatic reading flow, board columns, and paired guide columns.
\NewDocumentEnvironment{handoutsmall}{O{8}}{\begingroup\fontsize{#1}{9.5}\selectfont}{\endgroup}
\newenvironment{handoutflow}{\begin{multicols}{2}\raggedcolumns\RaggedRight}{\end{multicols}}
\newenvironment{handoutcolumns}{\columnratio{.5}\begin{paracol}{2}\RaggedRight}{\end{paracol}}
\newcommand{\colstart}{\par\noindent\begin{minipage}[t]{.482\linewidth}\vspace{0pt}\RaggedRight}
\newcommand{\colnext}{\end{minipage}\hfill\begin{minipage}[t]{.482\linewidth}\vspace{0pt}\RaggedRight}
\newcommand{\colend}{\end{minipage}\par}

% All box families share one geometry; labels still distinguish grayscale copies.
% Optional final tcolorbox options can override defaults, e.g. [breakable].
\tcbset{handout base/.style={enhanced,boxrule=.45pt,arc=1pt,
  left=5pt,right=5pt,top=4pt,bottom=4pt,before skip=5pt,after skip=5pt,
  before upper=\RaggedRight,fonttitle=\sffamily\bfseries\small,
  coltitle=wcprimary120,colbacktitle=wcprimary!7,
  titlerule=0pt,toptitle=2pt,bottomtitle=2pt},
  handout reference/.style={handout base,colframe=HandoutReference!45,colback=HandoutReference!3},
  handout workspace/.style={handout base,colframe=HandoutWorkspace!45,colback=white,
    colbacktitle=HandoutWorkspace!8,coltitle=black!80},
  handout checkpoint/.style={handout base,colframe=HandoutCheckpoint!70,colback=HandoutCheckpoint!4,
    colbacktitle=HandoutCheckpoint!12},
  handout synthesis/.style={handout base,colframe=HandoutSynthesis!65,colback=HandoutSynthesis!4,
    colbacktitle=HandoutSynthesis!10,coltitle=HandoutSynthesis!60!black}}
\ifhandoutboard
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

\fi
\NewTColorBox{fixedbox}{m O{}}{handout reference,title={#1},#2}
\NewTColorBox{boardbox}{m O{}}{handout workspace,title={#1},#2}
\NewTColorBox{checkpoint}{O{Checkpoint} O{}}{handout checkpoint,title={#1},#2}
\NewTColorBox{takeawaybox}{O{Takeaway} O{}}{handout synthesis,title={#1},#2}
\NewTColorBox{KeyBox}{m O{}}{handout reference,title={#1},#2}
% Explore is intentionally generic; OpenMC is an explicit authoring choice.
\NewTColorBox{Explore}{m O{}}{handout checkpoint,title={#1},#2}
\NewTColorBox{OpenMCExplore}{m O{}}{handout checkpoint,title={OpenMC\enspace|\enspace #1},#2}
\NewTColorBox{ExampleBox}{m O{}}{handout synthesis,title={#1},#2}
% Useful slide-style aliases (no overlay arguments).
\NewTColorBox{block}{m}{handout reference,title={#1}}
\NewTColorBox{alertblock}{m}{handout checkpoint,title={#1}}
\NewTColorBox{exampleblock}{m}{handout synthesis,title={#1}}

\newcommand{\eqread}[1]{{\sffamily\fontsize{8}{9.5}\selectfont\color{KSUGray}#1}}
\newcommand{\figcap}[1]{\par\vspace{1pt}{\sffamily\fontsize{8}{9.5}\selectfont\color{KSUGray}#1\par}}
\newcommand{\SourceLine}[1]{\par\vspace{2pt}{\sffamily\fontsize{7.5}{9}\selectfont\color{KSUGray}#1\par}}
\newcommand{\SourceEq}[1]{\par\nobreak\hfill
  \ifhandoutboard{\sffamily\scriptsize\color{KSUGray}#1}\else\eqread{#1}\fi\par}
% Late-guide compatibility names: remove their old local definitions on migration.
\newcommand{\NEContinue}[2]{\gdef\HandoutLesson{#1}\HandoutContinue{Lesson #1\enspace|\enspace #2}}
\newcommand{\NEEx}[1]{\par\addvspace{4pt}\textbf{#1}\par}
\newcommand{\NECheck}{\textbf{Definition check.}\ }
\newcommand{\NEsmall}[1]{{\fontsize{8.3}{10}\selectfont\RaggedRight #1\par}}
\newcommand{\NEbody}{\HandoutBody}
\newcommand{\uunit}[1]{\,\mathrm{#1}}
\newcommand{\metal}{\mathrm{metal}}
\newcommand{\water}{\mathrm{w}}
\newcommand{\fiiso}{\mathrm{fi}}
\newcommand{\feiso}{\mathrm{fe}}
\newcommand{\nucl}[2]{\ensuremath{{}^{#1}\mathrm{#2}}}
\providecommand{\mathdefault}[1]{#1}

% One source for Python styling; no minted/Pygments/shell-escape dependency.
\lstdefinestyle{NEpython}{language=Python,
  basicstyle=\ttfamily\fontsize{7.5}{9}\selectfont,
  keywordstyle=\color{wcprimary}\bfseries,commentstyle=\color{KSUGray},
  stringstyle=\color{wcalerted!80!black},
  columns=fullflexible,keepspaces=true,showstringspaces=false,
  breaklines=true,breakatwhitespace=false,tabsize=4,
  frame=single,rulecolor=\color{wcprimary!35},framesep=4pt,
  xleftmargin=4pt,xrightmargin=4pt,aboveskip=5pt,belowskip=5pt}
\lstdefinestyle{omc}{
  language=Python,
  basicstyle=\ttfamily\fontsize{6.65}{7.45}\selectfont,
  keywordstyle=\color{KSUDeepPurple}\bfseries,
  commentstyle=\color{KSUGray}\itshape,
  stringstyle=\color{KSUOrange!85!black},
  columns=fullflexible,keepspaces=true,showstringspaces=false,
  breaklines=true,breakatwhitespace=true,
  aboveskip=2pt,belowskip=2pt,
  frame=single,rulecolor=\color{KSUPurple!25},
  framesep=3pt,xleftmargin=1pt,xrightmargin=1pt
}
% Verbatim alternative for Python identifiers containing Greek characters.
\newfontfamily\HandoutCodeFont{DejaVu Sans Mono}
\DefineVerbatimEnvironment{NEunicodecode}{Verbatim}{breaklines=true,
  breakanywhere=true,fontsize=\scriptsize,formatcom=\HandoutCodeFont,
  frame=single,rulecolor=\color{wcprimary!35},framesep=4pt}

% Board blanks, solution reveals, vocabulary, and unit helpers.
\newenvironment{targetlist}{%
  \begin{itemize}[label={\raisebox{0.1ex}{\(\square\)}},leftmargin=1.45em]
}{%
  \end{itemize}
}

\NewDocumentCommand{\SolutionFigureContent}{+m}{%
  \ifhandoutsolutions #1\fi
}

\NewDocumentCommand{\Blank}{O{1.0in}}{%
  \leavevmode\makebox[#1][c]{\leaders\hbox to 0.42em{\hss.\hss}\hfill}%
}
\NewDocumentCommand{\RevealBlank}{O{1.0in} m}{%
  \ifhandoutsolutions
    \leavevmode\makebox[#1][c]{\textcolor{HandoutSynthesis}{\sffamily\bfseries #2}}%
  \else
    \Blank[#1]%
  \fi
}
\NewDocumentCommand{\MathBlank}{O{0.75in} m}{%
  \ifhandoutsolutions
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

\NewDocumentCommand{\SolutionCue}{m}{%
  \ifhandoutsolutions
    \begin{tcolorbox}[
      enhanced,boxrule=0.4pt,arc=1pt,
      colframe=HandoutSynthesis!60,colback=HandoutSynthesis!5,
      left=4pt,right=4pt,top=2pt,bottom=2pt,
      before skip=3pt,after skip=3pt
    ]
      \sffamily\scriptsize\textbf{Solution cue.} #1
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

\RenewDocumentCommand{\unit}{m}{\,\mathrm{#1}}
\newcommand{\Ktrue}{K_{\mathrm{true}}}
\newcommand{\Kclassical}{K_{\mathrm{classical}}}


% Shared step headings and solution reveals.
\newcommand{\Step}[2]{\Sec{#1}{#2}}
\newcommand{\PageTitle}[1]{\HandoutContinue{Lesson \HandoutLesson\enspace|\enspace #1}}

\NewDocumentCommand{\Reveal}{O{0.75in} m}{%
  \ifhandoutsolutions
    \textcolor{HandoutSynthesis}{\sffamily\bfseries #2}%
  \else
    \makebox[#1][c]{\rule[-0.2ex]{#1}{0.35pt}}%
  \fi
}
\NewDocumentCommand{\RevealMath}{O{0.75in} m}{%
  \ifhandoutsolutions
    \textcolor{HandoutSynthesis}{\ensuremath{#2}}%
  \else
    \makebox[#1][c]{\rule[-0.2ex]{#1}{0.35pt}}%
  \fi
}

\endinput
