{ pkgs ? import <nixpkgs> {} }:

pkgs.mkShell {
  buildInputs = with pkgs; [
    # Python and pip
    python311
    python311Packages.pip
    python311Packages.virtualenv
    
    # System dependencies for Python packages
    pkg-config
    cairo
    pango
    gdk-pixbuf
    
    # Image processing libraries (for Pillow)
    libjpeg
    libpng
    freetype
    zlib
    
    # Font rendering (for fonttools)
    fontconfig
    
    # Git (for github-readme-terminal)
    git
    
    # Optional: Docker if you want to use the Dockerfile
    docker
    docker-compose
  ];

  shellHook = ''
    echo "Entering grosheth development environment..."
    echo "Python version: $(python --version)"
    
    # Create virtual environment if it doesn't exist
    if [ ! -d "venv" ]; then
      echo "Creating Python virtual environment..."
      python -m venv venv
    fi
    
    # Activate virtual environment
    source venv/bin/activate
    
    # Upgrade pip
    pip install --upgrade pip
    
    # Install requirements if they haven't been installed yet
    if [ ! -f "venv/.requirements_installed" ]; then
      echo "Installing Python dependencies..."
      pip install -r requirements.txt
      touch venv/.requirements_installed
    fi
    
    echo "Virtual environment activated!"
    echo "To run the terminal animation: python terminal.py"
    echo "To deactivate: deactivate"
  '';

  # Set environment variables
  NIX_SHELL_PRESERVE_PROMPT = 1;
  
  # Make sure fonts are available
  FONTCONFIG_FILE = "${pkgs.fontconfig.out}/etc/fonts/fonts.conf";
  FONTCONFIG_PATH = "${pkgs.fontconfig.out}/etc/fonts/";
}
