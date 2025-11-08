# moving_files



moving_files
mv currentlocation/file.txt wantedlocation



packages
 remove packages:
  sudo pacman -R packagename  
 list all packages:
   pacman -Q    
 list aur packages:
   pacman -Qm    

activate env:
source nameofenv/bin/activate


deactivate env:
deactivate

errors:
no module named pip in venv:
activate env
python -m ensurepip --default-pip
install -U pip


