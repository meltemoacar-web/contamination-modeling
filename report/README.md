## Building the PDF 

A quick note is that this paper uses the 'revtex4-1' document class, so if you come across any errors while building the pdf, you might want to try installing this: 
```
sudo apt install texlive-publishers texlive-latex-extra latexmk
```

Now to build the pdf, just follow these commands:
```
cd report
latexmk -pdf main.tex
```

If you want to remove the build file but keep the pdf use this command:
```
latexmk -c
```
