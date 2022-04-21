import os
import time


user=input("Enter the correct user name:")
distro_list=["arch","debian"]
kvm_check="egrep -c '(vmx|svm)' /proc/cpuinfo"
arch_install  =["sudo pacman -Syu",
                "sudo pacman -S qemu virt-manager virt-viewer dnsmasq vde2 bridge-utils openbsd-netcat ebtables iptables libguestfs ovmf --needed",
                "sudo usermod -a -G libvirt "+user,
                "sudo reboot"]
debian_install=["sudo apt update && sudo apt upgrade",
                "sudo apt install qemu-kvm libvirt-clients libvirt-daemon-system bridge-utils virtinst libvirt-daemon virt-manager ovmf",
                "sudo adduser "+user+" libvirt && sudo adduser "+user+" libvirt-qemu",
                "sudo reboot"]
status="sudo systemctl status libvirtd.service"
kvm_net=["sudo virsh net-start default","sudo virsh net-autostart default"]
kvm_install=[arch_install,debian_install]


def installer(distro_index):
    distro=kvm_install[distro_index]
    answer=input("Would you like to update your system before continuing?(y/n)[Default=y]")
    if answer.lower() != "n":
        os.system(distro[0])
    os.system(distro[1])
    answer=input("Add the user to required groups?(y/n)[Default=y]")
    if answer.lower() != "n":
        os.system(distro[2])
    print("KVM status...")
    os.system(status)
    answer=input("Enable networking?(y/n)[Default=y]")
    if answer.lower() != "n" :
        os.system(kvm_net[0])
        os.system(kvm_net[1])
    answer=input("Reboot the system now?(y/n)[Default=y]")
    print()
    print("KVM installation is complete!\n")
    if answer.lower() != "n":
        print("Rebooting in 10 seconds...(Press Ctrl+C to cancel)")
        time.sleep(10)
        os.system(distro[3])
    




def find_distro():
    condition=1
    distro="arch"
    while condition:
        print("""Distro names:
        1)Arch
        2)Debian (Same option for Ubuntu)""")
        distro=input("Enter the distro name [Ex:Arch]:")
        print(distro)
        if distro.lower() in distro_list:
            print("Installing...")
            time.sleep(1)
            installer(distro_list.index(distro.lower()))
            break
        else:
            print("Wrong input. Try again or press Ctrl+D to exit")



os.system("clear")
print("""---KVM/QEMU Installer---

Supported Systems:  1)Arch/Arch based distros
                    2)Debian/Debian based distros
                    (including Ubuntu/Ubuntu based distros)
                    
                    (Press Ctrl+D to Exit)""")

find_distro()
