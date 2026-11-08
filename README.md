# schwarzschild_geodesics                  

Paketë Python për studimin numerik të gjeodezikëve në hapësirë-kohë Schwarzschild, e ndërtuar si **template profesional për studentët e vitit të parë Master në Fizikë**, në kuadër të lëndës **Relativiteti i Përgjithshëm**.

Ky projekt lidh në mënyrë të drejtpërdrejtë:

- formalizmin teorik të Relativitetit të Përgjithshëm,
- analizën me potencial efektiv,
- integrimin numerik të orbitave,
- krahasimin me gravitetin Njutonian,
- dhe prodhimin e figurave të gatshme për raportin përfundimtar në LaTeX.

---

## Objektivat pedagogjike

Studenti duhet të jetë në gjendje të:

1. kuptojë rolin e metrikës së Schwarzschild-it;
2. shohë si reduktohet problemi në planin ekuatorial;
3. identifikojë madhësitë e ruajtura;
4. ndërtojë dhe interpretojë potencialin efektiv;
5. integrojë numerikisht orbitat relativiste dhe Njutoniane;
6. analizojë precesionin e perihelit;
7. paraqesë rezultatet në mënyrë shkencore dhe të riprodhueshme.

---

## Struktura e repos

```text
schwarzschild_geodesics/
├── schwarzschild_geodesics/
│   ├── __init__.py
│   ├── constants.py
│   ├── models/
│   │   ├── __init__.py
│   │   ├── metric.py
│   │   ├── lagrangian.py
│   │   └── geodesic_equations.py
│   ├── numerics/
│   │   ├── __init__.py
│   │   ├── integrators.py
│   │   └── solver.py
│   └── visualization/
│       ├── __init__.py
│       ├── orbits.py
│       └── potentials.py
├── outputs/
├── gjeodezika_schwarzschild_notebook.ipynb
├── main.py
├── pyproject.toml
├── requirements.txt
└── README.md
```

---

## Instalimi

Rekomandohet përdorimi i një mjedisi virtual.

### 1. Krijimi i mjedisit virtual

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 2. Instalimi i varësive

```bash
python3 -m pip install --upgrade pip
python3 -m pip install -r requirements.txt
```

---

## Përdorimi nga terminali

### A. Vizualizimi i potencialeve efektive

```bash
python3 main.py --mode potential
```

### B. Simulimi i orbitës relativiste dhe Njutoniane

```bash
python3 main.py --mode orbit
```

### C. Vlerësimi i precesionit të perihelit

```bash
python3 main.py --mode precession
```

---

## Parametra të rëndësishëm

Mund të kontrolloni parametrat kryesorë drejtpërdrejt nga CLI:

```bash
python3 main.py --mode orbit --mass 1.98847e30 --r0 4.6e10 --L 5.2e15 --tau-max 2.0e7 --samples 25000
python3 main.py --mode orbit --mass 1.98847e30 --r0 4.6e10 --phi0 1.1 --vr0 3.0e07 --L 5.2e15 --tau-max 2.0e7 --samples 25000
```

Parametrat kryesorë janë:

- `--mass`: masa qendrore në kg
- `--r0`: rrezja fillestare në metra
- `--phi0`: këndi fillestar në radianë
- `--vr0`: shpejtësia radiale fillestare
- `--L`: momenti këndor specifik
- `--tau-max`: kufiri i integrimit
- `--samples`: numri i pikave për ruajtje
- `--output-dir`: dosja e figurave dalëse

---

## Daljet e pritshme

Paketa mund të prodhojë automatikisht:

- `effective_potential.pdf`
- `orbit_comparison.pdf`

brenda dosjes `outputs/`.

Këto figura mund të përfshihen drejtpërdrejt në raportin LaTeX.

---

## Lidhja me teorinë

### 1. Potenciali efektiv relativist

Për grimca test masive në planin ekuatorial përdorim:

$$
V_{\mathrm{eff}}(r)=\left(1-\frac{r_s}{r}\right)\left(c^2+\frac{L^2}{r^2}\right),
\qquad
r_s=\frac{2GM}{c^2}.
$$

### 2. Ekuacioni radial i reduktuar

Për analizën numerike përdorim formën:

$$
\ddot r = -\frac{GM}{r^2} + \frac{L^2}{r^3} - \frac{3GM L^2}{c^2 r^4}.
$$

Krahasimi me rastin Njutonian:

$$
\ddot r = -\frac{GM}{r^2} + \frac{L^2}{r^3}
$$

lejon nxjerrjen e precesionit relativist.

---

## Sugjerime për studentët

1. Ndryshoni vlerën e momentit këndor `L` dhe vëzhgoni ndryshimin e orbitës.
2. Rrisni `tau-max` për të kapur disa perihele.
3. Përdorni të dhëna të afërta me Merkurin dhe krahasoni me formulën afruese të precesionit.
4. Ruani figurat në PDF dhe përdorini në raportin final.
5. Shpjegoni fizikisht dallimin midis orbitës relativiste dhe asaj klasike.

---

## Set praktik “Merkuri rreth Diellit”

Kjo është bashkësia e parametrave të rastit klasik të precesionit të Mërkurit.

- `mass = 1.98847e30`
- `r0 ≈ 4.6001e10 m`
- `L ≈ 2.713e15 m²/s`
- `vr0 = 0`

Komanda:

```
python3 main.py --mode orbit --mass 1.98847e30 --r0 4.6001e10 --phi0 0 --vr0 0 --L 2.713e15 --tau-max 7.6e6 --samples 40000
```

Për precesion, një orbitë nuk mjafton. Provo:

```
python3 main.py --mode precession --mass 1.98847e30 --r0 4.6001e10 --phi0 0 --vr0 0 --L 2.713e15 --tau-max 1.5e8 --samples 250000
```

Ky rast është fizikisht i arsyeshëm, por precesioni për orbitë është shumë i vogël, prandaj vizualisht nuk del aq qartë sa në shembujt didaktikë.

### Set praktik “precesion i dukshëm”

Këtu efekti relativist shihet më qartë.

- `mass = 1.98847e30`
- `r0 = 1.0e10`
- `L ≈ 1.363e15`
- `vr0 = 0`

```
python3 main.py --mode orbit --mass 1.98847e30 --r0 1.0e10 --phi0 0 --vr0 0 --L 1.363e15 --tau-max 4.0e7 --samples 120000
```

Për precesion:

```
python3 main.py --mode precession --mass 1.98847e30 --r0 1.0e10 --phi0 0 --vr0 0 --L 1.363e15 --tau-max 4.0e7 --samples 120000
```

Ky është zakonisht kompromisi më i mirë mes stabilitetit numerik dhe precesionit të dukshëm.

### Set praktik “orbitë pothuajse rrethore”

Këtu bëhet dallimi mes orbitës stabile dhe asaj me ekscentricitet të vogël.

Për orbitë rrethore klasike:


$$
L_{circ}
\approx
\sqrt{G M r_0}
$$

për `r0 = 2.0e10 m` del afërsisht `L ≈ 1.63e15`.

Komanda:

```
python3 main.py --mode orbit --mass 1.98847e30 --r0 2.0e10 --phi0 0 --vr0 0 --L 1.63e15 --tau-max 6.0e7 --samples 100000
```

Nëse zvoglohet pak `L`, orbita bëhet më eliptike; nëse rritet pak, bëhet më rrethore.

### Vlera praktike për potencialin efektiv

Për potencialin, mjafton të japësh një `L` të arsyeshëm. P.sh.:

```
python3 main.py --mode potential --mass 1.98847e30 --L 2.713e15
```

ose për efekt relativist më të fortë:

```
python3 main.py --mode potential --mass 1.98847e30 --L 1.363e15
```

### Rregull i shpejtë për të ndërtuar vetë raste të mira

Nëse kërkohet një orbitë eliptike me perihel $r_p$ dhe ekscentricitet $e$, mund të përdoret:

$$
L
\approx
\sqrt{GMr_p(1 + e)}
$$

Pastaj vendosen:

- `r0 = r_p`
- `vr0 = 0`

Shembull:

- `r_p = 2.0e10`
- `e = 0.3`

atëherë:

$$
L
\approx
1.86 \times 10^{15} \\, \text{m}^{2}/\text{s}
$$

Pra:

```
python3 main.py --mode orbit --mass 1.98847e30 --r0 2.0e10 --vr0 0 --L 1.86e15 --tau-max 6.0e7 --samples 120000
```

---

## Rekomandime për zgjerim

Studentët mund ta zgjerojnë projektin me:

- orbitat e fotoneve,
- orbitat rrethore stabile dhe jostabile,
- analiza e minimave dhe maksimave të potencialit efektiv,
- krahasim me formulat analitike për precesionin,
- skanime parametrike për `L` dhe `r0`.

---

## Referenca të rekomanduara

1. Bernard Schutz, *A First Course in General Relativity*  
2. Sean Carroll, *Spacetime and Geometry*  
3. Misner, Thorne, Wheeler, *Gravitation*  
4. Robert Wald, *General Relativity*  
5. James Hartle, *Gravity: An Introduction to Einstein's General Relativity*

---

## Shënim për përdorim didaktik

Ky kod është ndërtuar si **template pedagogjik**, jo si bibliotekë kërkimore e plotë. Megjithatë, është i organizuar në mënyrë profesionale për t’i mësuar studentit:

- strukturimin e një projekti shkencor në Python,
- ndarjen midis modelit fizik, solver-it numerik dhe vizualizimit,
- dhe rëndësinë e riprodhueshmërisë në punën shkencore.
