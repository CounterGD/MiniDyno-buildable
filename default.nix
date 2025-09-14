{ pkgs ? import <nixpkgs> {} }:

pkgs.stdenv.mkDerivation {
  pname = "minidyno";
  version = "1.0.0";

  src = ./.;

  buildInputs = [ pkgs.python3 pkgs.python3Packages.pip pkgs.docker ];

  installPhase = ''
    mkdir -p $out/bin
    echo "#!/usr/bin/env bash" > $out/bin/minidyno
    echo "python3 $src/bot.py" >> $out/bin/minidyno
    chmod +x $out/bin/minidyno
  '';
}
