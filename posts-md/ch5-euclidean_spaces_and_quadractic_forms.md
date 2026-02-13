# Chapter 5: Euclidean Spaces and Quadratic Forms

## I. Bilinear Forms

### ==1.1 Definition==

- Let $V$ be a vector space over $\mathbb{R}$. A mapping $f: V \times V \to \mathbb{R}$ is called a **bilinear form** on $V$ if it is linear with respect to each variable.
- **Conditions:** For all $\mathbf{u}, \mathbf{v}, \mathbf{w} \in V$ and $\lambda \in \mathbb{R}$:
    1. $f(\mathbf{u} + \mathbf{v}, \mathbf{w}) = f(\mathbf{u}, \mathbf{w}) + f(\mathbf{v}, \mathbf{w})$
    2. $f(\lambda \mathbf{u}, \mathbf{v}) = \lambda f(\mathbf{u}, \mathbf{v})$
    3. $f(\mathbf{u}, \mathbf{v} + \mathbf{w}) = f(\mathbf{u}, \mathbf{v}) + f(\mathbf{u}, \mathbf{w})$
    4. $f(\mathbf{u}, \lambda \mathbf{v}) = \lambda f(\mathbf{u}, \mathbf{v})$
- **Symmetric Bilinear Form:** $f$ is symmetric if $f(\mathbf{u}, \mathbf{v}) = f(\mathbf{v}, \mathbf{u})$ for all $\mathbf{u}, \mathbf{v} \in V$.

### 1.2 Matrix Representation

- Let $B = \{\mathbf{u}_1, \mathbf{u}_2, \dots, \mathbf{u}_n\}$ be a basis of $V$.
- The matrix $\mathbf{A} = (a_{ij})_{n \times n}$ where **$a_{ij} = f(\mathbf{u}_i, \mathbf{u}_j)$** is called the matrix of the bilinear form $f$ with respect to basis $B$.
- **Coordinate Expression:** Let $\mathbf{x} = [\mathbf{u}]_B$ and $\mathbf{y} = [\mathbf{v}]_B$ be the coordinate column vectors of $\mathbf{u}$ and $\mathbf{v}$. The value of the bilinear form is: $$f(\mathbf{u}, \mathbf{u}) = \mathbf{x}^T \mathbf{A} \mathbf{y} = \sum_{i=1}^n \sum_{j=1}^n a_{ij} x_i y_j$$
- **Symmetry:** $f$ is a symmetric bilinear form if and only if its matrix $\mathbf{A}$ is **symmetric** ($\mathbf{A} = \mathbf{A}^T$).

### 1.3 Change of Basis

- Let $\mathbf{A}_1$ be the matrix of $f$ relative to basis $B_1$.
- Let $\mathbf{A}_2$ be the matrix of $f$ relative to basis $B_2$.
- Let $\mathbf{C}$ be the **transition matrix** (change-of-basis matrix) from $B_1$ to $B_2$.
- **Formula:** $$\mathbf{A}_2 = \mathbf{C}^T \mathbf{A}_1 \mathbf{C}$$

---

## II. Quadratic Forms

### 2.1 Definition and Relationship to Bilinear Forms

- **Definition:** A mapping $q: V \to \mathbb{R}$ is a **quadratic form** if it is associated with a symmetric bilinear form $f$ such that **$q(\mathbf{u}) = f(\mathbf{u}, \mathbf{u})$**.
- **Polar Form:** The symmetric bilinear form $f$ can be recovered from the quadratic form $q$ via the polarization identity: $$f(\mathbf{u}, \mathbf{v}) = \frac{1}{2} [q(\mathbf{u}+\mathbf{v}) - q(\mathbf{u}) - q(\mathbf{v})]$$

### 2.2 Matrix and Expressions

- **Matrix Representation:** The matrix of the quadratic form $q$ in basis $B$ is the same as the matrix of its associated symmetric bilinear form $f$. It is always a **symmetric matrix** $A$.
- **Polynomial Expression:** If $\mathbf{x} = (x_1, \dots, x_n)^T$ are the coordinates of $\mathbf{u}$, the quadratic form is expressed as: $$q(\mathbf{u}) = \mathbf{x}^T \mathbf{A} \mathbf{x} = \sum_{i=1}^n \sum_{j=1}^n a_{ij} x_i x_j$$
- **Change of Variables:** Under a change of basis represented by matrix $\mathbf{C}$ (where $\mathbf{x} = \mathbf{C}\mathbf{y}$), the matrix of the quadratic form transforms to $\mathbf{C}^T \mathbf{A} \mathbf{C}$.

### ==2.3 Canonical Forms==

- **Definition:** A quadratic form is in **canonical form** if its matrix is diagonal. In this form, the expression contains only squared terms: $$q(\mathbf{u}) = \lambda_1 y_1^2 + \lambda_2 y_2^2 + \dots + \lambda_n y_n^2$$
- **Principal Axes:** The basis vectors in which the quadratic form takes a canonical shape are called the principal axes.
- **Normal form:** Is canonical form where $\lambda_i \in \{-1, 0, 1\}, \forall i$.
	- Start with canonical form
	- Scale each variables in such way that the coefficients $\lambda_i$ are normalized.
	- Proceed with caution, as space is stretched, and info on scale, eigenvalues,... is lost.

### 2.4 Methods of Diagonalization

Any quadratic form can be reduced to a canonical form.

1. ==**Lagrange Method:**== Uses the technique of **completing the square**.
	- Identify a term with non-zero coefficient ($a_{gg} x_g^2$ or $a_{gh}x_gx_h$).
	- Case 1: $a_{gg} \neq 0$:
		- Group all terms with $x_g$.
		- Factor out $\frac{1}{a_{gg}}$ and create a square of a linear combination of variables.
		- The remaining terms form a new quadratic form that doesn't contain $x_g$.
	- Case 2: $a_{gg} = 0, a_{gh} \neq 0$:
		- Create $u_i^2$: $xy = \frac{1}{4} [(x+y)^2 - (x-y)^2] = \frac{1}{4}(u_1^2 - u_2^2)$.
	- Repeat.
2. ==**Jacobi Method:**== Applicable when all **leading principal minors** $\Delta_k$ of the matrix $A$ are non-zero.
	- **Definition:** $\Delta_r$ is order-$r$ leading principal minor: $$
\Delta_r = \begin{vmatrix}
a_{11} & a_{12} & \cdots & a_{1r} \\
a_{21} & a_{22} & \cdots & a_{2r} \\
\vdots & \vdots & \ddots & \vdots \\
a_{r1} & a_{r2} & \cdots & a_{rr}
\end{vmatrix}, \quad \Delta_0 = 1
$$
	- **Formula:** $q(\mathbf{u}) = k_1y_1^2 + \dots + k_ny_n^2$, where $k_i = \dfrac{\Delta_{i-1}}{\Delta_i} \quad (\text{with } \Delta_0 = 1)$
3. **Orthogonal Diagonalization:** Since $A$ is real symmetric, there exists an **orthogonal matrix $\mathbf{P}$** ($\mathbf{P}^T = \mathbf{P}^{-1}$) such that $\mathbf{P}^T \mathbf{A} \mathbf{P} = \mathbf{D}$ (diagonal). The diagonal entries are the **eigenvalues** of $\mathbf{A}$.

### 2.5 Law of Inertia and Classification

- **Law of Inertia:** The number of positive terms ($p$) and negative terms ($m$) in the **canonical form** of a quadratic form is invariant (does not depend on the method of diagonalization).
- ==**Signature:**== The pair $(p, m)$ or the value $s = p - m$.
- ==**Definiteness:**==
    - **Positive Definite:**
	    - $q(\mathbf{u}) > 0$ for all $\mathbf{u} \neq \mathbf{0}$.
	    - All eigenvalues $> 0$.
	    - $p=n$.
	    - $\Delta_r > 0$ for all $r$ (Sylvester's criterion).
    - **Negative Definite:**
	    - $q(\mathbf{u}) < 0$ for all $\mathbf{u} \neq \mathbf{0}$.
	    - All eigenvalues $< 0$.
	    - $m=n$.
	    - $\Delta_{2k} > 0 \land \Delta_{2k-1} < 0$ for all $k \ge 1$ (Sylvester's criterion).
    - **Indefinite:**
	    - $q(\mathbf{u})$ can assume both positive and negative values.
- ==**Sylvester’s Criterion:**==
    - Positive Definite $\iff$ All leading principal minors $\Delta_k > 0$.
    - Negative Definite $\iff$ The signs alternate: $\Delta_1 < 0, \Delta_2 > 0, \Delta_3 < 0, \dots$ (i.e., $(-1)^k \Delta_k > 0$).

---

## III. Euclidean Spaces

### ==3.1 Inner Product Spaces==

- **Definition:** Given a real vector space $V$, equipped with an **inner product**, a mapping $\langle \cdot, \cdot \rangle: V \times V \to \mathbb{R}$ satisfying 3 axioms for all $\mathbf{u}, \mathbf{v}, \mathbf{w} \in V, \lambda \in \mathbb{R}$:
    1. **Symmetry:** $\langle \mathbf{u}, \mathbf{v} \rangle = \langle \mathbf{v}, \mathbf{u} \rangle$.
    2. **Bilinearity:** $\langle \mathbf{u}+\mathbf{v}, \mathbf{w} \rangle = \langle \mathbf{u}, \mathbf{w} \rangle + \langle \mathbf{v}, \mathbf{w} \rangle$ and $\langle \lambda \mathbf{u}, \mathbf{v} \rangle = \lambda \langle \mathbf{u}, \mathbf{v} \rangle$.
    3. **Positive Definiteness:** $\langle \mathbf{u}, \mathbf{u} \rangle \geq 0$, and $\langle \mathbf{u}, \mathbf{u} \rangle = 0 \iff \mathbf{u} = \mathbf{0}$.
   $\implies V$ Is an **Inner Product Space**
- _(Note: This is formally a positive definite symmetric bilinear form)._
- **Euclidean Space:** A finite-dimensional, real IPS.

### ==3.2 Standard Inner Product==

1. For $\mathbb{R}^n$ (The Dot/Scalar Product): $$\langle \mathbf{u}, \mathbf{v} \rangle = \mathbf{u} \cdot \mathbf{v} = \sum_{i=1}^{n} u_i v_i$$
2. For $C[a,b]$ (Continuous Functions): $$\langle f, g \rangle = \int_{a}^{b} f(x)g(x) \, dx$$
3. For $M_{m \times n}(\mathbb{R})$ (The Frobenius Inner Product): $$\langle \mathbf{A}, \mathbf{B} \rangle = \operatorname{tr}(\mathbf{A}^T \mathbf{B})$$

### 3.3 Norm, Distance, and Angle

- **Length (Norm):** $\|\mathbf{u}\| = \sqrt{\langle \mathbf{u}, \mathbf{u} \rangle}$.
- ==**Propositions:**==
	- $\|\mathbf{u}\| \ge 0$
	- $\|\lambda \mathbf{u}\| = |\lambda| \|\mathbf{u}\|$
	- $\|\mathbf{u}+\mathbf{v}\| \le \|\mathbf{u}\| + \|\mathbf{v}\|$ (Triangle Inequality).
	- $|\langle \mathbf{u}, \mathbf{v} \rangle| \le \|\mathbf{u}\| \cdot \|\mathbf{v}\|$ (Cauchy-Schwarz Inequality).
		- i.e. $\langle \mathbf{u}, \mathbf{v} \rangle^2 \le \langle \mathbf{u}, \mathbf{u} \rangle \cdot \langle \mathbf{v}, \mathbf{v} \rangle$
		- In $\mathbb{R}^n$ with usual scalar product: becomes Bunyakovsky inequality 
	- If $\|\mathbf{u}\| = 1$, then $\mathbf{u}$ is a **unit vector**.
- **Distance:** $d(\mathbf{u}, \mathbf{v}) = \|\mathbf{u} - \mathbf{v}\|$.
- **Angle:** The angle $\alpha$ between non-zero vectors $\mathbf{u}, \mathbf{v}$ is determined by: $$\cos \alpha = \frac{\langle \mathbf{u}, \mathbf{v} \rangle}{\|\mathbf{u}\| \cdot \|\mathbf{v}\|}, \quad 0 \le \alpha \le \pi$$

### 3.3 Orthogonality

#### A. Definitions

- **Orthogonal Vectors:** $\mathbf{u} \perp \mathbf{v} \iff \langle \mathbf{u}, \mathbf{v} \rangle = 0$.
- ==**Pythagorean Theorem:**== If $\mathbf{u} \perp \mathbf{v}$, then $\|\mathbf{u}+\mathbf{v}\|^2 = \|\mathbf{u}\|^2 + \|\mathbf{v}\|^2$.
- ==**Orthogonal Complement:**== $W^\perp = \{\mathbf{v} \in V \mid \langle \mathbf{v}, \mathbf{w} \rangle = 0, \forall \mathbf{w} \in W\}$.
	- $\mathbf{u}^\perp = \{\mathbf{u} \}^\perp = \{ \mathbf{v} \in V \mid \mathbf{v} \perp \mathbf{u} \}$.
	- If $W$ is any set: $W^\perp \cap W \subset \{ \mathbf{0} \}$.
		- Case $W$ is a subspace (contains $\mathbf{0}$), then: $W^\perp \cap W \subset \{ \mathbf{0} \}$.

#### B. Orthogonal/Orthonormal Sets and Bases

- ==**Orthogonal/Orthonormal Sets:**==
	- $S \text{ is orthogonal} \iff \langle \mathbf{u}_i, \mathbf{u}_j \rangle = 0, \forall i \neq j$.
	- $S \text{ is orthonormal} \iff \langle \mathbf{u}_i, \mathbf{u}_j \rangle = \begin{cases} 0, i \neq j \\ 1, i = j \end{cases}$
- **Orthogonal Basis:** A basis where vectors are pairwise orthogonal.
- **Orthonormal Basis (ON-basis):** An orthogonal basis where every vector has unit length ($\|\mathbf{u}_i\|=1$).
- ==**Coordinates in OG-/ON-basis:**==
	- If $B=\{\mathbf{e}_1, \dots, \mathbf{e}_n\}$ is an OG-basis,
		- then $\displaystyle \mathbf{u} = \sum_{i=1}^n \frac{\langle \mathbf{u}, \mathbf{e}_i \rangle}{\langle \mathbf{e}_i, \mathbf{e}_i \rangle} \mathbf{e}_i$.
	- If $B=\{\mathbf{e}_1, \dots, \mathbf{e}_n\}$ is an ON-basis,
		- then $\displaystyle \mathbf{u} = \sum_{i=1}^n \langle \mathbf{u}, \mathbf{e}_i \rangle \mathbf{e}_i$.

### 3.4 Gram-Schmidt Process

**Problem:** Convert basis $\{\mathbf{u}_1, \dots, \mathbf{u}_n\}$ into an orthogonal basis $\{\mathbf{v}_1, \dots, \mathbf{v}_n\}$, such that: $$ \operatorname{Span} \{\mathbf{v}_1, \dots, \mathbf{v}_k\} = \{\mathbf{u}_1, \dots, \mathbf{u}_k\}, \quad \forall k = \overline{1, n} $$

**Algorithm:** Use the recursive formula:
- $\mathbf{v}_1 = \mathbf{u}_1$
- $\displaystyle \mathbf{v}_k = \mathbf{u}_k - \sum_{i=1}^{k-1} \frac{\langle \mathbf{u}_k, \mathbf{v}_i \rangle}{\|\mathbf{v}_i\|^2} \mathbf{v}_i$
- To get an **orthonormal** basis, normalize each vector: $\mathbf{e}_i = \dfrac{\mathbf{v}_i}{\|\mathbf{v}_i\|}$.
 
### 3.5 Orthogonal Projection and Least Squares

- ==**Orthogonal Decomposition:**== For any subspace $W$, $V = W \oplus W^\perp$. Any $\mathbf{v} \in V$ can be uniquely written as $\mathbf{v} = \mathbf{w}_1 + \mathbf{w}_2$ where $\mathbf{w}_1 \in W$ and $\mathbf{w}_2 \in W^\perp$.
- **Projection:**
	- **Definition:** The vector $\mathbf{w}_1$ is called the **orthogonal projection** of $\mathbf{v}$ onto $W$, denoted $\operatorname{P}_W(\mathbf{v})$ or $\operatorname{Ch}_W(\mathbf{v})$.
	- ==**Computing:**==
		1. **ON-basis:** If $\{\mathbf{u}_1, \dots, \mathbf{u}_k\}$ is an ON-basis of $W$, then $\operatorname{P}_W(\mathbf{v}) = \sum\limits_{i=1}^k \langle \mathbf{v}, \mathbf{u}_i \rangle \mathbf{u}_i$.
		2. **Definition:**
			- Given $\{\mathbf{v}_1, \dots, \mathbf{v}_m\}$ spans $W$ (preferably a basis of $W$).
			- Define $P(\mathbf{v}) = x_1 \mathbf{v}_1 + \dots + x_m \mathbf{v}_m$.
			- Solve $m$ equations to get $x_i$: $\langle P(\mathbf{v}), \mathbf{v}_i) \rangle = \langle \mathbf{v}, \mathbf{v}_i \rangle$.
			- **Lemma:** $P(v) = \mathbf{A} ( \mathbf{A}^T \mathbf{A} ) ^{-1} \mathbf{A}^T \mathbf{v}$, where $\mathbf{A} = [\mathbf{v}_1 \ \mathbf{v}_2 \ \dots \mathbf{v}_n]$.
	- **Properties:**
		- $P$ is a linear operator.
		- Idempotency: $P^2 = P$.
		- $\operatorname{Im}P = W, \operatorname{Ker}P = W^\perp$.
		- If $\mathbf{v} \in W$, then $\operatorname{P}_W (\mathbf{v}) = \mathbf{v}$.
- ==**Best Approximation:**== $\|\mathbf{v} - \operatorname{P}_W(\mathbf{v})\| \le \|\mathbf{v} - \mathbf{w}\|$ for all $\mathbf{w} \in W$.
- ==**Least Squares:**== When $\mathbf{A}\mathbf{x}=\mathbf{b}$ has no solution, the least squares solution $\tilde{\mathbf{x}}$ minimizes $\|\mathbf{A}\mathbf{x} - \mathbf{b}\|$. It is found by solving the normal equations: **$\mathbf{A}^T \mathbf{A} \tilde{\mathbf{x}} = \mathbf{A}^T \mathbf{b}$**.

---

## IV. Orthogonal Matrices and Transformations

### ==4.1 Orthogonal Matrices==

- **Definition:** A square matrix $\mathbf{A}$ is orthogonal if $\mathbf{A}^T \mathbf{A} = \mathbf{A} \mathbf{A}^T = \mathbf{I}$ (i.e., $\mathbf{A}^{-1} = \mathbf{A}^T$).
- **Properties:**
    - Columns (and rows) form an orthonormal basis of $\mathbb{R}^n$.
    - $\det(\mathbf{A}) = \pm 1$.
    - Transition matrices between orthonormal bases are orthogonal (AB, BA, A^-1, B^-1).
    - Euclidean space: change-of-basis matrix from 1 ON-basis to another ON-basis is an OG matrix.

### ==4.2 Orthogonal Transformations (Operators)==

- **Definition:** A linear operator $f: V \to V$ is orthogonal if:
	- It preserves the inner product: $\langle f(\mathbf{u}), f(\mathbf{v}) \rangle = \langle \mathbf{u}, \mathbf{v} \rangle$;
	- and, Its matrix representation wrt any ON-basis is an OG matrix.
- **Equivalent Property:** It preserves length: $\|f(\mathbf{u})\| = \|\mathbf{u}\|$ (Isometry).
- **Matrix Connection:** The matrix of an orthogonal transformation with respect to an ONB is an orthogonal matrix.

### ==4.3 Symmetric Operators and Diagonalization==

- **Symmetric Transformation:** An operator $f$ is symmetric if $\langle f(\mathbf{u}), \mathbf{v} \rangle = \langle \mathbf{u}, f(\mathbf{v}) \rangle$. Its matrix in an ONB is **symmetric** ($\mathbf{A}=\mathbf{A}^T$).
- **Spectral Theorem:** A real symmetric matrix $\mathbf{A}$ is always **orthogonally diagonalizable**.
    - All eigenvalues are real.
    - ==Eigenvectors from different eigenspaces are orthogonal.==
    - There exists an orthogonal matrix $\mathbf{P}$ such that $\mathbf{P}^T \mathbf{A} \mathbf{P} = \mathbf{D}$ (diagonal).
- **Geometric Intuition:** A symmetric transformation stretches space in strictly orthogonal directions (thus eigenvectors are orthogonal).
- **Orthogonal diagonalization:**
	- Proceed as usual diagonalization.
	- Convert each eigenspace's basis into an ON-basis.

---

## V. Quadric Lines and Surfaces

### ==5.1 General Concept==

- A **hypersurface** in $\mathbb{R}^n$ is the set of points satisfying $\mathbf{x}^T \mathbf{A} \mathbf{x} + b^T \mathbf{x} + c = 0$ ($\mathbf{A}$ is symmetric).
- $n=2$: Quadric Line (Đường bậc hai).
- $n=3$: Quadric Surface (Mặt bậc hai).

### ==5.2 Canonical Reduction==

To identify the shape, the equation is simplified via:

1. **Rotation:** Using orthogonal diagonalization to eliminate cross-terms ($x_i x_j$).
2. **Translation:** Completing the square to eliminate linear terms ($x_i$).

### ==5.3 Classification==

**Quadric Lines ($n=2$):**

- Ellipse (real, imaginary), Hyperbola, Parabola.
- Degenerate cases: Intersecting lines, Parallel lines, Coincident lines, Single point.

**Quadric Surfaces ($n=3$):**

- **Ellipsoid:** $\dfrac{x^2}{a^2} + \dfrac{y^2}{b^2} + \dfrac{z^2}{c^2} = 1$
- **Hyperboloid of one sheet:** $\dfrac{x^2}{a^2} + \dfrac{y^2}{b^2} - \dfrac{z^2}{c^2} = 1$
- **Hyperboloid of two sheets:** $\dfrac{x^2}{a^2} + \dfrac{y^2}{b^2} - \dfrac{z^2}{c^2} = -1$
	- ($\dfrac{x^2}{a^2} - \dfrac{y^2}{b^2} - \dfrac{z^2}{c^2} = 1$)
- **Cone:** $\dfrac{x^2}{a^2} + \dfrac{y^2}{b^2} - \dfrac{z^2}{c^2} = 0$
- **Elliptic Paraboloid:** $\dfrac{x^2}{a^2} + \dfrac{y^2}{b^2} = pz$ (2pz)
- **Hyperbolic Paraboloid (Saddle):** $\dfrac{x^2}{a^2} - \dfrac{y^2}{b^2} = pz$ (2pz)
- **Cylinders:** Elliptic, Hyperbolic, Parabolic.