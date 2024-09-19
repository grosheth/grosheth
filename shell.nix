let
  pkgs = import <nixpkgs> {};
in pkgs.mkShell {
  packages = [
    (pkgs.python311.withPackages (python-pkgs: [
      python-pkgs.pip
      python-pkgs.requests
      python-pkgs.jinja2
      python-pkgs.plotly
      python-pkgs.matplotlib
      python-pkgs.pandas
      python-pkgs.pip
      python-pkgs.urllib3
      python-pkgs.tomli
      python-pkgs.six
      python-pkgs.python-dotenv
      python-pkgs.dateutil
      python-pkgs.pygments
      python-pkgs.pillow
      python-pkgs.idna
      python-pkgs.executing
      python-pkgs.colorama
      python-pkgs.charset-normalizer
      python-pkgs.certifi
      python-pkgs.asttokens
      python-pkgs.icecream
    ]))
  ];
}
