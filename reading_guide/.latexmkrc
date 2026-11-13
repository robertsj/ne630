# Build the reading guides with XeLaTeX; the shared handout class lives in ../handouts.
ensure_path('TEXINPUTS', '../handouts//');
$pdf_mode = 5;          # xelatex
$xelatex = 'xelatex -interaction=nonstopmode -halt-on-error %O %S';
