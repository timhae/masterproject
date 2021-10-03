with import <nixpkgs>{};

stdenv.mkDerivation rec {
    name = "masterprojekt";
    env = buildEnv {name = name; paths = buildInputs; };
    buildInputs = [
      python39Packages.opencv4
    ];
}
