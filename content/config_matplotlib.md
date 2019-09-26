
Source:
`https://stackoverflow.com/questions/28909747/how-do-i-configure-mathjax-for-ipython-notebooks/44290246#44290246`


I recently had the exact problem. I really don't like the default STIX-Web font to render equation.
After experimenting for a 
little while, I found a way to change the MathJax font in Jupyter Notebook.
My Jupyter Notebook version is 4.3.1 and it is shipped 
with Anaconda. I assume the solutions for other versions should be similar.

I tried to edit custom.js both in `/notebook/static/custom/custom.js` and `~/.jupyter/custom/custom.js`.

Doesn't work. I also tried to edit mathjaxutils.js. It does nothing.

Finaly I saw this post `https://github.com/jupyter/help/issues/109`. 

I realize Jupyter uses  main.min.js to read MathJax configuration. So here is the solutions:

Download MathJax (`https://github.com/mathjax/MathJax`) from Github.

Unzip the MathJax file and go into the folder

copy jax/output/HTML-CSS/fonts/TeX into directoy ../notebook/static/components/MathJax/jax/output/HTML-CSS/fonts/

copy fonts/HTML-CSS/TeX into ../notebook/static/components/MathJax/fonts/HTML-CSS/

open ../notebook/static/notebook/js/main.min.js, search for availableFonts. It should be around line 14894. Change it to

```
...
availableFonts: ["STIX-Web","TeX"],
imageFont: null;
preferredFont: "TeX",
webFont: "TeX"
...
```

    Refresh the notebook.

