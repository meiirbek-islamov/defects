# Defects
Python package for introducing missing-linker defects in Metal-organic framework, namely HKUST-1 (3x3x3 supercell).

## Installation
------------
First, clone and install the defects repository:

```bash
git clone https://github.com/meiirbek-islamov/defects.git
cd defects
pip install -e ./
```

## Usage
------------
A defective HKUST-1 (3x3x3 supercell) can be generated for a cif file HKUST-1_3x3x3.cif with the
`remove-linkers` CLI as follows:
```
remove-linkers N
```
Here, `N` is the number of organic linkers you want to remove. Total number of linkers in the system is `432`. Thus, if you want to delete 50% of the linkers, then, `N` will be equal to `216`.
This will generate a defected HKUST-1 named `HKUST-1_3x3x3_defected.cif`.
=======
Python package for introducing missing-defects in Metal-organic framework, namely HKUST-1 (3x3x3 supercell).
