Title: Testing MathJax plugin
Date: 2019-09-27 23:55
Category: Post
Authors: Fadjar Fathurrahman

Don't mind me. This pages simply test whether `render_math` plugin is working.

An example of displayed equation:
\begin{equation}
\alpha + \beta
\end{equation}

An example of inline math: $\alpha + \frac{\beta}{\Gamma}$.


Environment align:

\begin{align}
A & = B + C \\
  & = D + E + C
\end{align}

Braket notation: (not working, need MathJax 3)
\begin{equation}
H \ket{\psi} = E \ket{\psi}
\end{equation}

Manual (using `langle`, `rangle`, and `vert`): (not perfect!)
\begin{eqnarray}
\left\vert \psi_{i} \right\rangle, \left\vert \frac{1}{2} \right\rangle \\
\langle \psi_{j} \vert, \left\langle \frac{1}{2} \right\vert \\
\left\langle \psi_{j} \right\vert H \left\vert \psi_{i} \right\rangle \\
\left\langle \frac{1}{2} \right\vert H \left\vert \frac{1}{2} \right\rangle \\
\end{eqnarray}

Using middle:
\begin{equation}
\left\langle \frac{1}{2} \middle| 1 \right\rangle
\end{equation}

Chemical formula using `mhchem`: $\ce{C6H5-CHO}$


