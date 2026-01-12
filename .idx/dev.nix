{ pkgs, ... }: {
  channel = "stable-24.05";
  packages = [ 
    pkgs.python3
    pkgs.python311Packages.flake8
  ];
  idx = {
    extensions = [
      "ms-python.python"
      "ms-python.pylint"
      "ms-python.black-formatter"
      "ms-python.flake8"
      "usernamehw.error-lens"
    ];
  };
}
