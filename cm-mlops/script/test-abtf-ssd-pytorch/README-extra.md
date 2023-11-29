cm rm cache -f

cmr "install python-venv" --name=test1

cmr "test abtf ssd-pytorch" --adr.python.name=test1 --input=computer_mouse.jpg --output=computer_mouse_ssd.jpg

#cmr "test abtf ssd-pytorch" --adr.python.name=test1 --adr.torch.version=1.13.1 --adr.torchvision.version=0.14.1 --input=computer_mouse.jpg --output=computer_mouse_ssd.jpg

