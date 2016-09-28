{ pkgs ? import <nixpkgs> {} }:

let
  pythonPackages = pkgs.python35Packages;
  stdenv = pkgs.stdenv;
  python3 = pkgs.python35;
  paste3 = pythonPackages.buildPythonPackage rec {
    name = "paste-2.0.3";

    src = pkgs.fetchurl {
      url = mirror://pypi/P/Paste/Paste-2.0.3.tar.gz;
      sha256 = "062jk0nlxf6lb2wwj6zc20rlvrwsnikpkh90y0dn8cjch93s6ii3";
    };

    buildInputs = with pythonPackages; [ six ];

    doCheck = false; # some files required by the test seem to be missing

    meta = {
      description = "Tools for using a Web Server Gateway Interface stack";
      homepage = http://pythonpaste.org/;
    };
  };
in rec {
  pyEnv = stdenv.mkDerivation {
    name = "py-paste";
    buildInputs = [ stdenv python3 paste3 pythonPackages.ipdb ];
  };
}
